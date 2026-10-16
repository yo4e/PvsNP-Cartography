#!/usr/bin/env python3
"""Exact bounded attack on n=10 GF(2) MOD3 single orbit, <=3 blocks.

EXHAUSTS ONLY the class of degree <=2 polynomials invariant under arbitrary
permutations within each of at most 3 nonempty coordinate blocks, and takes
a uniform orbit for ONE such polynomial. Does not test mixtures, >3 blocks,
or arbitrary nonsymmetric quadratics. No SciPy, assert, random sampling.
"""
import json
from itertools import product
from fractions import Fraction as F
from math import comb,prod,factorial

N=10
def check(cond, why):
    if not cond:raise ValueError(why)

def bitmask(k):
    m=len(k)
    feats=[1]+[a%2 for a in k]+[comb(a,2)%2 for a in k]+[
        (k[i]*k[j])%2 for i in range(m) for j in range(i+1,m)]
    return sum((v<<j) for j,v in enumerate(feats))

def search(part):
    m=len(part)
    atoms=[]
    for ks in product(*[range(p+1) for p in part]):
        atoms.append((sum(ks),bitmask(ks),
                      prod(comb(p,k) for p,k in zip(part,ks))))
    for w in range(N+1):
        check(sum(weight for ww,mask,weight in atoms if ww==w)==comb(N,w),
              'incorrect Hamming layer normalization')
    best=(F(-1),-1,None);valid=[]
    for code in range(1<<(1+2*m+m*(m-1)//2)):
        counts=[0]*(N+1)
        for w,mask,multiplicity in atoms:
            if (code&mask).bit_count()%2==int(w%3==0):
                counts[w]+=multiplicity
        minimum=min(F(g,comb(N,w)) for w,g in enumerate(counts))
        if minimum>best[0]:
            best=(minimum,code,counts)
        if minimum>=F(2,3):
            valid.append((code,str(minimum)))
    return {'part':list(part),'tried':1<<(1+2*m+m*(m-1)//2),
            'best_minimum':str(best[0]),'best_mask':best[1],
            'best_good_counts':best[2],'passing':valid}

def direct_truth_table(part,code):
    check(sum(part)==N,'wrong part sizes')
    # Independent, literal Boolean input truth table for the canonical
    # partition; compares with the weight-profile combinatorial calculator.
    boundaries=[0]
    for n in part:boundaries.append(boundaries[-1]+n)
    counts=[0]*(N+1)
    for x in range(1<<N):
        ks=[sum((x>>i)&1 for i in range(boundaries[j],boundaries[j+1]))
            for j in range(len(part))]
        w=x.bit_count()
        if (code&bitmask(ks)).bit_count()%2==int(w%3==0):
            counts[w]+=1
    return counts

def main():
    partitions=sorted({p for m in (1,2,3)
        for p in product(range(1,N+1),repeat=m)
        if sum(p)==N and p==tuple(sorted(p,reverse=True))})
    outcomes=[search(p) for p in partitions]
    check(len(partitions)==14,'size-partition coverage changed')
    check(sum(r['tried'] for r in outcomes)==8520,'coefficient coverage changed')
    check(not any(r['passing'] for r in outcomes),'unexpected passing certificate')
    best=max(outcomes,key=lambda r:F(r['best_minimum']))
    check(best['part']==[4,3,3] and best['best_minimum']=='62/105'
          and best['best_mask']==727,'best candidate changed')
    check(direct_truth_table((4,3,3),727)==
        [1,7,33,88,124,174,148,72,36,7,1],
          'independent full-cube evaluation disagrees')
    check(best['best_good_counts']==direct_truth_table((4,3,3),727),
          'best finite layer counts do not match')
    print(json.dumps({'scope':'n=10 single uniform orbit; blockwise symmetric quadratics <=3 blocks only',
         'partitions':len(partitions),'quadratics_checked':8520,
         'successful_in_restricted_class':0,
         'best':best,'all_partitions':outcomes,
         'warning':'no global degree-two impossibility claim; mixtures and other classes unsearched'},sort_keys=True,indent=2))

if __name__=='__main__':main()
