#!/usr/bin/env python3
"""Exact n10 MOD3 mixture witness, all-input and affine-dual audit.

A numerical LP was used only to select candidates; the stored integer weights
are accepted solely after exact validation. This is NOT a Lean proof or
independent human review. No assertion relies on Python assert/-O behaviour.
"""
import copy,json
from math import comb,factorial,lcm
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

N=10
PAIRS=list(combinations(range(N),2))
IDX={p:k for k,p in enumerate(PAIRS)}
TARGET=[int(x.bit_count()%3==0) for x in range(1<<N)]
FEATURE=[]
for x in range(1<<N):
    z=1|(x<<1)
    for k,(i,j) in enumerate(PAIRS):
        if x>>i&1 and x>>j&1:z|=1<<(1+N+k)
    FEATURE.append(z)

def req(ok,why):
    if not ok:raise ValueError(why)

def row_of(partition,code):
    m=len(partition);result=code&1
    for blockid,block in enumerate(partition):
        if code>>(1+blockid)&1:
            result|=sum(1<<(1+i) for i in block)
        if code>>(1+m+blockid)&1:
            result|=sum(1<<(1+N+IDX[(i,j)])
                        for i,j in combinations(sorted(block),2))
    bit=1+2*m
    for i,j in combinations(range(m),2):
        if code>>bit&1:
            result|=sum(1<<(1+N+IDX[tuple(sorted((a,b)))])
                        for a in partition[i] for b in partition[j])
        bit+=1
    return result

def eval_polynomial(row,x):
    return ((row&FEATURE[x]).bit_count())%2

def eval_blocks(partition,code,x):
    ks=[sum(x>>i&1 for i in block) for block in partition]
    m=len(ks)
    terms=[1]+[k%2 for k in ks]+[comb(k,2)%2 for k in ks]+[
        ks[i]*ks[j]%2 for i,j in combinations(range(m),2)]
    return (code&sum(z<<i for i,z in enumerate(terms))).bit_count()%2

def all_partitions(shape):
    a,b,c=shape
    for aa in combinations(range(N),a):
        A=frozenset(aa)
        rest=tuple(i for i in range(N) if i not in A)
        for bb in combinations(rest,b):
            B=frozenset(bb)
            yield (A,B,frozenset(rest)-B)

def canonical(shape):
    offset=0;result=[]
    for s in shape:
        result.append(tuple(range(offset,offset+s)));offset+=s
    return tuple(result)

def mobius(values):
    result=values[:]
    for i in range(N):
        for x in range(1<<N):
            if x>>i&1:result[x]^=result[x^(1<<i)]
    return result

def walsh(vals):
    result=vals[:];size=1
    while size<len(result):
        for start in range(0,len(result),size*2):
            for i in range(start,start+size):
                a,b=result[i],result[i+size]
                result[i],result[i+size]=a+b,a-b
        size*=2
    return result

def check(data,full):
    req(data['n']==10 and data['field']=='GF(2)' and data['error']=='1/3',
        'wrong problem model')
    req(data['target']=='one iff Hamming weight divisible by three',
        'wrong target')
    req(data['one_seed_distribution']=='for each selected block pattern, uniformly randomize all coordinate partitions',
        'unjustified averaging convention')
    seeds=data['seeds'];D=data['probability_denominator']
    req(len(seeds)==8 and D==100 and
        sum(s['weight'] for s in seeds)==D and
        all(isinstance(s['weight'],int) and s['weight']>0 for s in seeds),
        'probabilities not normalized')
    sizes=[comb(N,w) for w in range(N+1)]
    L=[F(0)]*(N+1);osizes=[]
    for s in seeds:
        shape=s['blocks'];code=s['code']
        req(len(shape)==3 and all(x>0 for x in shape) and sum(shape)==10
            and 0<=code<1024,'bad polynomial')
        orbit=factorial(N)
        for size in shape:orbit//=factorial(size)
        osizes.append(orbit)
        partition=canonical(shape)
        row=row_of(partition,code)
        values=[eval_polynomial(row,x) for x in range(1<<N)]
        req(values==[eval_blocks(partition,code,x) for x in range(1<<N)],
            'independent polynomial representations disagree')
        coefficients=mobius(values)
        req(all(i.bit_count()<=2 for i,k in enumerate(coefficients) if k),
            'higher-than-quadratic term')
        counts=[sum(values[x]==TARGET[x] for x in range(1<<N)
                    if x.bit_count()==w) for w in range(N+1)]
        req(counts==s['good'],'canonical block layer count mismatch')
        for w in range(N+1):
            L[w]+=F(s['weight']*counts[w],D*sizes[w])
    minimum=min(L)
    req(minimum==F(data['expected_minimum'])==F(2123,3000)>F(2,3),
        'finite upper certificate invalid')
    den=lcm(*(D*o for o in osizes))
    total=0;point=[0]*(1<<N)
    if full:
        for s,orbit in zip(seeds,osizes):
            ticket=s['weight']*den//(D*orbit)
            req(ticket*D*orbit==s['weight']*den,'noninteger expansion')
            count=0
            for part in all_partitions(s['blocks']):
                row=row_of(part,s['code']);count+=1
                for x in range(1<<N):
                    v=eval_polynomial(row,x)
                    req(v==eval_blocks(part,s['code'],x),
                        'expanded polynomial/partition mismatch')
                    point[x]+=ticket*(v==TARGET[x])
            req(count==orbit,'orbit size wrong')
            total+=ticket*count
        req(den==252000 and total==den,'expanded mass differs')
        req(all(F(point[x],den)==L[x.bit_count()] for x in range(1<<N)),
            'pointwise probabilities differ from orbit averages')
        req(min(point)*3>2*den,'not pointwise better than 2/3')
    masses=[data['dual_mass_by_weight'].get(str(x.bit_count()),0)
            for x in range(1<<N)]
    dd=data['dual_denominator']
    req(dd==240 and min(masses)>=0 and sum(masses)==dd,
        'dual weights invalid')
    scores=[sum(masses[x] for x in range(1<<N)
         if (c^((a&x).bit_count()&1))==TARGET[x])
         for c in (0,1) for a in range(1<<N)]
    W=walsh([m*(1-2*f) for m,f in zip(masses,TARGET)])
    req(scores==[(dd+(1-2*c)*v)//2 for c in (0,1) for v in W],
        'Walsh and exhaustive lower checker differ')
    req(max(scores)==data['affine_upper_score']==152 and
        F(max(scores),dd)==F(19,30)<F(2,3),
        'universal affine obstruction invalid')
    for k in range(N+1):
        odd=sum(comb(k,j)*comb(N-k,3-j)
                for j in (1,3) if j<=k and 0<=3-j<=N-k)
        formula=F(N-k,2*N)+F(odd,2*comb(N,3))
        req(F(scores[(1<<k)-1],dd)==formula and
            F(scores[(1<<N)+(1<<k)-1],dd)==1-formula,
            'hypergeometric degree-one check mismatch')
    return {'n':N,'seed_orbits':len(seeds),'expanded_indexed_polynomials':sum(osizes),
            'expanded_prob_denominator':den,'all_inputs':1<<N,
            'affine_polynomials':len(scores),
            'upper_by_weight':list(map(str,L)),
            'upper_minimum':str(minimum),'lower_maximum':str(F(max(scores),dd)),
            'upper_margin':str(minimum-F(2,3)),
            'lower_gap':str(F(2,3)-F(max(scores),dd))}

def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--full',action='store_true')
    args=parser.parse_args()
    d=json.loads(Path(__file__).with_name('certificate.json').read_text())
    summary=check(d,args.full)
    controls=[]
    changes=[('changed_coefficient',lambda d:d['seeds'][0].__setitem__('code',97)),
             ('changed_layer',lambda d:d['seeds'][0]['good'].__setitem__(4,209)),
             ('unnormalized',lambda d:d['seeds'][0].__setitem__('weight',11)),
             ('incorrect_field',lambda d:d.__setitem__('field','GF(3)')),
             ('wrong_target',lambda d:d.__setitem__('target','parity')),
             ('invalid_dual',lambda d:d['dual_mass_by_weight'].__setitem__('1',11)),
             ('false_lower',lambda d:d.__setitem__('affine_upper_score',151)),
             ('false_upper',lambda d:d.__setitem__('expected_minimum','3/4'))]
    for name,mutate in changes:
        q=copy.deepcopy(d);mutate(q)
        try:check(q,False)
        except ValueError:controls.append(name)
        else:raise ValueError('negative control accepted: '+name)
    print(json.dumps({'state':'exact n10 finite evidence, not yet Lean',
        'result':summary,'mutations_rejected':controls},sort_keys=True,indent=2))

if __name__=='__main__':main()
