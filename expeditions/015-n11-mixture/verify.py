#!/usr/bin/env python3
"""Exact n11 certificate verification. Standard library; no optimizer trusted.

Compare combinatorial and truth-query quadratic encodings, all 2048 input
values, layer counts, full partition expansion and an exhaustive affine dual.
This checks finite evidence, not a separately executed Lean n11 theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial, lcm
from pathlib import Path
import argparse
import copy
import json

N = 11
PAIRS = tuple(combinations(range(N), 2))
EDGE = {p:k for k,p in enumerate(PAIRS)}
TARGET = [int(x.bit_count() % 3 == 0) for x in range(1 << N)]
FEATURES = [1 | (x << 1) | sum(1 << (1 + N + k) for k,(i,j) in enumerate(PAIRS)
            if x >> i & 1 and x >> j & 1) for x in range(1 << N)]

def require(ok, why):
    if not ok:
        raise ValueError(why)

def canonical(shape):
    offset = 0; result = []
    for s in shape:
        result.append(tuple(range(offset,offset+s))); offset += s
    return result

def block_value(partition, code, x):
    counts = [sum(x >> i & 1 for i in block) for block in partition]
    terms = [1] + counts + [comb(k,2) for k in counts]
    terms += [counts[i]*counts[j] for i,j in combinations(range(3),2)]
    return sum(v for k,v in enumerate(terms) if code >> k & 1) % 2

def explicit_row(partition, code):
    row = code & 1
    for b,block in enumerate(partition):
        if code >> (1+b) & 1:
            row |= sum(1 << (1+i) for i in block)
        if code >> (4+b) & 1:
            row |= sum(1 << (1+N+EDGE[tuple(sorted(p))]) for p in combinations(block,2))
    for k,(i,j) in enumerate(combinations(range(3),2)):
        if code >> (7+k) & 1:
            row |= sum(1 << (1+N+EDGE[tuple(sorted((a,b)))]) for a in partition[i] for b in partition[j])
    return row

def queried_row(partition, code):
    c = block_value(partition,code,0)
    lin = [block_value(partition,code,1<<i)^c for i in range(N)]
    quad = [block_value(partition,code,(1<<i)|(1<<j))^c^lin[i]^lin[j] for i,j in PAIRS]
    return c | sum(v<<(1+i) for i,v in enumerate(lin)) | sum(v<<(1+N+i) for i,v in enumerate(quad))

def partitions(shape):
    a,b,_ = shape
    for A in combinations(range(N),a):
        rest = tuple(i for i in range(N) if i not in A)
        for B in combinations(rest,b):
            yield A,B,tuple(i for i in rest if i not in B)

def walsh(values):
    values = values[:]; size = 1
    while size < len(values):
        for start in range(0,len(values),2*size):
            for i in range(start,start+size):
                a,b = values[i],values[i+size]
                values[i],values[i+size] = a+b,a-b
        size *= 2
    return values

def check(d, full):
    require(d['n']==N and d['field']=='GF(2)' and d['error']=='1/3', 'wrong model')
    require(d['target']=='one iff Hamming weight divisible by three', 'wrong target')
    require(d['distribution']=='choose seed with fixed weight, then uniformly permute all coordinates', 'wrong quantifiers')
    D = d['probability_denominator']; seeds = d['seeds']
    require(isinstance(D,int) and D>0 and sum(s['weight'] for s in seeds)==D
            and all(isinstance(s['weight'],int) and s['weight']>0 for s in seeds), 'invalid probability')
    sizes = [comb(N,w) for w in range(N+1)]
    layers = [F(0)]*(N+1); orbits = []; rows = []
    for s in seeds:
        shape = s['blocks']; code = s['code']
        require(len(shape)==3 and all(isinstance(k,int) and k>0 for k in shape)
                and sum(shape)==N and isinstance(code,int) and 0<=code<1024, 'bad seed')
        p = canonical(shape); row = explicit_row(p,code)
        require(row==queried_row(p,code), 'coefficient reconstruction differs')
        values = [(row&f).bit_count()%2 for f in FEATURES]
        require(values==[block_value(p,code,x) for x in range(1<<N)], 'polynomial values differ')
        anf = values[:]
        for i in range(N):
            for x in range(1<<N):
                if x>>i&1: anf[x] ^= anf[x^(1<<i)]
        require(all(x.bit_count()<=2 for x,v in enumerate(anf) if v), 'degree exceeds two')
        counts = [sum(values[x]==TARGET[x] for x in range(1<<N) if x.bit_count()==w) for w in range(N+1)]
        require(counts==s['good'], 'stored layer profile differs')
        for w in range(N+1): layers[w] += F(s['weight']*counts[w], D*sizes[w])
        o = factorial(N)
        for k in shape: o //= factorial(k)
        orbits.append(o); rows.append([row&1,(row>>1)&((1<<N)-1),row>>(N+1)])
    require(min(layers)>F(2,3), 'upper certificate failed')
    common = lcm(*(D*o for o in orbits)); expanded_min = None
    if full:
        point = [0]*(1<<N); total = 0
        for s,o in zip(seeds,orbits):
            ticket = s['weight']*common//(D*o)
            require(ticket*D*o==s['weight']*common, 'bad integer expansion')
            count = 0
            for p in partitions(s['blocks']):
                row = explicit_row(p,s['code']); count += 1
                for x,feature in enumerate(FEATURES):
                    if (row&feature).bit_count()%2 == TARGET[x]: point[x] += ticket
            require(count==o, 'partition count differs'); total += ticket*count
        require(total==common, 'expanded mass differs')
        require(all(F(v,common)==layers[x.bit_count()] for x,v in enumerate(point)), 'pointwise/layer mismatch')
        expanded_min = str(F(min(point),common))
    masses = [d['dual_mass_by_weight'].get(str(x.bit_count()),0) for x in range(1<<N)]
    dd = d['dual_denominator']
    require(dd==330 and sum(masses)==dd and min(masses)>=0, 'bad lower distribution')
    support = [(x,m) for x,m in enumerate(masses) if m]
    scores = [sum(m for x,m in support if (c^((a&x).bit_count()%2))==TARGET[x])
              for c in (0,1) for a in range(1<<N)]
    W = walsh([m*(1-2*f) for m,f in zip(masses,TARGET)])
    require(scores==[(dd+(1-2*c)*v)//2 for c in (0,1) for v in W], 'independent lower algorithms differ')
    require(max(scores)==207 and F(max(scores),dd)==F(69,110)<F(2,3), 'lower obstruction failed')
    for k in range(N+1):
        odd = sum(comb(k,j)*comb(N-k,3-j) for j in (1,3) if j<=k and 0<=3-j<=N-k)
        require(scores[(1<<k)-1]==15*(N-k)+odd, 'hypergeometric formula differs')
    return {'state':'exact finite evidence; n11 Lean not run','inputs':1<<N,
            'seed_orbits':len(seeds),'coefficient_rows':rows,
            'expanded_indexed_polynomials':sum(orbits),'expanded_denominator':common,
            'expanded_minimum':expanded_min,'upper_by_layer':list(map(str,layers)),
            'upper_minimum':str(min(layers)),'upper_margin':str(min(layers)-F(2,3)),
            'affine_rows':len(scores),'affine_maximum':str(F(max(scores),dd)),
            'lower_gap':str(F(2,3)-F(max(scores),dd))}

def main():
    p = argparse.ArgumentParser(); p.add_argument('--full',action='store_true'); p.add_argument('--candidate',action='store_true')
    args = p.parse_args()
    path = Path(__file__).with_name('candidate.json' if args.candidate else 'certificate.json')
    d = json.loads(path.read_text()); result = check(d,args.full)
    changes = [('coefficient',lambda q:q['seeds'][0].__setitem__('code',1)),
               ('layer',lambda q:q['seeds'][0]['good'].__setitem__(0,1)),
               ('normalization',lambda q:q.__setitem__('probability_denominator',9999)),
               ('field',lambda q:q.__setitem__('field','GF(3)')),
               ('target',lambda q:q.__setitem__('target','parity')),
               ('quantifier',lambda q:q.__setitem__('distribution','choose seed after seeing input')),
               ('dual',lambda q:q['dual_mass_by_weight'].__setitem__('1',14))]
    rejected = []
    for name,change in changes:
        q = copy.deepcopy(d); change(q)
        try: check(q,False)
        except ValueError: rejected.append(name)
        else: raise ValueError('bad negative control accepted: '+name)
    print(json.dumps({'result':result,'mutations_rejected':rejected},indent=2,sort_keys=True))

if __name__=='__main__': main()
