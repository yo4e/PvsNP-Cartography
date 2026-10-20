#!/usr/bin/env python3
"""Exact n11 source-data audit, independent of the previous verifier.

This is finite computation, not Lean execution or human semantic review.
All checks raise exceptions under both normal and optimized Python.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json
import re

N = 11
PAIRS = tuple(combinations(range(N), 2))
SIZES = [comb(N, w) for w in range(N + 1)]
TARGET = [int(x.bit_count() % 3 == 0) for x in range(1 << N)]


def require(ok, why):
    if not ok:
        raise ValueError(why)


def subset_value(r, x):
    if r == 0:
        return 0
    k = (x & ((1 << (9-r))-1)).bit_count()
    linear = x.bit_count() if r == 1 else (x >> 7).bit_count()
    return (1 + linear + comb(k, 2)) % 2


def recover(r):
    c = subset_value(r, 0)
    a = [subset_value(r, 1 << i) ^ c for i in range(N)]
    b = [subset_value(r, (1 << i) | (1 << j)) ^ c ^ a[i] ^ a[j]
         for i, j in PAIRS]
    return c, sum(v << i for i, v in enumerate(a)), sum(v << i for i, v in enumerate(b))


def eval_row(row, x):
    c, a, b = row
    return (c + (a & x).bit_count() + sum(((b >> k) & 1) * ((x >> i) & 1) * ((x >> j) & 1)
            for k, (i, j) in enumerate(PAIRS))) % 2


def block_value(seed, x):
    ks = []
    start = 0
    for size in seed['blocks']:
        ks.append(((x >> start) & ((1 << size)-1)).bit_count())
        start += size
    terms = [1, *ks, *(comb(k, 2) for k in ks)]
    terms += [ks[i]*ks[j] for i,j in combinations(range(3), 2)]
    return sum(v for i,v in enumerate(terms) if seed['code'] >> i & 1) % 2


def walsh(values):
    v = list(values)
    size = 1
    while size < len(v):
        for start in range(0,len(v),2*size):
            for i in range(start,start+size):
                a,b = v[i],v[i+size]
                v[i],v[i+size] = a+b,a-b
        size *= 2
    return v


def literal_tables(source):
    def sec(start,end):
        return source.split(start,1)[1].split(end,1)[0]
    pairs = [tuple(map(int,z)) for z in re.findall(r'\((\d+),\s*(\d+)\)', sec('def pairs', 'def rows'))]
    rows = [tuple(map(int,z)) for z in re.findall(r'\((\d+),\s*(\d+),\s*(\d+)\)', sec('def rows','def weights'))]
    def array(text):
        return list(map(int,re.search(r'!\[([^]]+)\]',text).group(1).split(',')))
    weights = array(sec('def weights','def tickets'))
    layers = array(sec('def layerTickets','theorem layer_tickets_exact'))
    return pairs,rows,weights,layers


def check_source(source, expected):
    require(literal_tables(source)==expected,'Lean literal data differ')
    require('abbrev target : BooleanCube 11 → ZMod 2 := @SmallSupportMod3.target 11' in source,
            'wrong formal target binding')
    require(not re.search(r'\b(sorry|admit|native_decide)\b',source),'unsupported placeholder or decision')


def main():
    root = Path(__file__).resolve().parents[2]
    d = json.loads((root/'expeditions/015-n11-mixture/compact-certificate.json').read_text())
    require(d['n']==N and d['field']=='GF(2)' and d['error']=='1/3','wrong model')
    require(d['target']=='one iff Hamming weight divisible by three','wrong target')
    require(d['probability_denominator']==7 and [s['weight'] for s in d['seeds']]==[1,4,2],
            'wrong orbit probabilities')
    rows = [recover(r) for r in range(3)]
    values = [[subset_value(r,x) for x in range(1<<N)] for r in range(3)]
    for r,row in enumerate(rows):
        require(values[r]==[eval_row(row,x) for x in range(1<<N)],'monomial/subset mismatch')
        require(values[r]==[block_value(d['seeds'][r],x) for x in range(1<<N)],'block/subset mismatch')
        anf = values[r][:]
        for i in range(N):
            for x in range(1<<N):
                if x>>i&1:
                    anf[x] ^= anf[x^(1<<i)]
        require(all(x.bit_count()<=2 for x,a in enumerate(anf) if a),'degree exceeds two')
    good = [[sum(v[x]==TARGET[x] for x in range(1<<N) if x.bit_count()==w)
             for w in range(N+1)] for v in values]
    require(good==[s['good'] for s in d['seeds']],'stored block layers differ')
    weights = [3,12,6]
    layer_tickets = [sum(t*g[w] for t,g in zip(weights,good)) for w in range(N+1)]
    layers = [F(v,21*SIZES[w]) for w,v in enumerate(layer_tickets)]
    require(min(layers)==F(158,231)>F(2,3),'invalid upper bound')
    raw = [sum(t for t,v in zip(weights,values) if v[x]==TARGET[x]) for x in range(1<<N)]
    require(raw[63]==0,'wrong raw-mixture counterexample')

    # Independent quotient reconstruction: choose coordinate subsets directly.
    # Every resulting polynomial has the same individual mass as in the old orbit witness.
    point = [165*int(f==0) for f in TARGET]
    formula_evaluations = 1<<N
    for size,ticket,all_linear in [(8,4,True),(7,1,False)]:
        for A in combinations(range(N),size):
            mask = sum(1<<i for i in A)
            edge_mask = sum(1<<k for k,(i,j) in enumerate(PAIRS) if mask>>i&1 and mask>>j&1)
            linear_mask = (1<<N)-1 if all_linear else ((1<<N)-1)^mask
            # Algebraic evaluation uses the precomputed square-free monomials.
            for x in range(1<<N):
                k = (x & mask).bit_count()
                v = (1+(x & linear_mask).bit_count()+comb(k,2))%2
                edge_value = sum((x>>i&1)*(x>>j&1) for i,j in combinations(A,2))%2
                require(v==(1+(x&linear_mask).bit_count()+edge_value)%2,'expanded evaluation mismatch')
                point[x] += ticket*int(v==TARGET[x])
                formula_evaluations += 1
    require(all(F(v,1155)==layers[x.bit_count()] for x,v in enumerate(point)),
            'all-input expansion differs from layer mean')

    mass = [15 if x.bit_count()==1 else 1 if x.bit_count()==3 else 0 for x in range(1<<N)]
    require(sum(mass)==330,'dual normalization')
    support = [(x,m) for x,m in enumerate(mass) if m]
    scores = [[sum(m for x,m in support if (c^((a&x).bit_count()%2))==TARGET[x])
               for a in range(1<<N)] for c in (0,1)]
    W = walsh([m*(1-2*f) for m,f in zip(mass,TARGET)])
    require(scores==[[(330+(1-2*c)*v)//2 for v in W] for c in (0,1)],'direct/Walsh mismatch')
    require(max(map(max,scores))==207 and F(207,330)==F(69,110)<F(2,3),'lower gap')
    canonical = [[s[(1<<k)-1] for k in range(N+1)] for s in scores]
    require(all(scores[c][a]==canonical[c][a.bit_count()] for c in (0,1) for a in range(1<<N)),
            'coefficient orbit coverage')
    for k in range(N+1):
        odd = sum(comb(k,j)*comb(N-k,3-j) for j in (1,3) if j<=k and 0<=3-j<=N-k)
        require(canonical[0][k]==15*(N-k)+odd,'hypergeometric lower mismatch')
    mutated = 0
    for r,row in enumerate(rows):
        for bit in range(1+N+len(PAIRS)):
            q = list(row)
            if bit==0:
                q[0] ^= 1
            elif bit<=N:
                q[1] ^= 1<<(bit-1)
            else:
                q[2] ^= 1<<(bit-1-N)
            require(any(eval_row(q,x)!=values[r][x] for x in range(1<<N)), 'undetected coefficient mutation')
            mutated += 1
    path = root/'formal/PvsNPCartography/Mod3ElevenDegree.lean'
    source = path.read_text()
    expected = (list(PAIRS),rows,weights,layer_tickets)
    check_source(source,expected)
    rejected = []
    for name,old,new in [('coefficient','38605195639935','38605195639934'),
                         ('weight','![3,12,6]','![3,12,7]'),
                         ('layer','18,189,795','18,189,794'),
                         ('edge','(0,1),(0,2)','(0,2),(0,1)'),
                         ('target','@SmallSupportMod3.target 11','@SmallSupportMod3.target 10')]:
        require(old in source, 'inactive mutation')
        try:
            check_source(source.replace(old,new,1),expected)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('mutated source was accepted: '+name)
    result = {'state':'exact finite source-data audit, not Lean acceptance',
              'n':N,'all_inputs':1<<N,'rows':rows,'triple_weights':weights,
              'triple_denominator':21,'layer_tickets':layer_tickets,
              'upper_by_layer':list(map(str,layers)),'upper_minimum':str(min(layers)),
              'affine_rows':4096,'canonical_affine_scores':canonical,'affine_maximum':'69/110',
              'quotient_distinct_rows':496,'quotient_denominator':1155,
              'expanded_formula_evaluations':formula_evaluations,
              'raw_counterexample':{'mask':63,'success':'0'},
              'coefficient_mutations_detected':mutated,'source_mutations_rejected':rejected,
              'lean_source_sha256':hashlib.sha256(source.encode()).hexdigest()}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
