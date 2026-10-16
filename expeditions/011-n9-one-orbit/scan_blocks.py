#!/usr/bin/env python3
"""Exhaust the restricted <=3 nonempty block types, NOT all GF(2) quadratics.

All blockwise-permutation-invariant quadratic polynomials on a fixed partition
are encoded by constant, block linear parities, intra-block degree-two terms,
and inter-block products. Only single uniform block-partition orbits are tested.
"""
from itertools import product
from math import comb,prod,factorial
from fractions import Fraction as F
import json

def require(ok,msg):
    if not ok:raise ValueError(msg)

def scan(part):
    m=len(part)
    atoms=[]
    for ks in product(*[range(v+1) for v in part]):
        w=sum(ks)
        features=[1]+[k%2 for k in ks]+[comb(k,2)%2 for k in ks]+[
            (ks[i]*ks[j])%2 for i in range(m) for j in range(i+1,m)]
        mask=sum(v<<j for j,v in enumerate(features))
        atoms.append((w,mask,prod(comb(v,k) for v,k in zip(part,ks))))
    require(all(sum(mult for w,mask,mult in atoms if w==k)==comb(9,k)
                for k in range(10)),'block layer not normalized')
    successes=[]
    best=(F(-1),None)
    for code in range(1<<(1+2*m+m*(m-1)//2)):
        good=[0]*10
        for w,mask,mult in atoms:
            value=(code&mask).bit_count()%2
            if value==int(w%3==0):good[w]+=mult
        v=min(F(g,comb(9,w)) for w,g in enumerate(good))
        if v>best[0]:best=(v,code)
        if v>=F(2,3):successes.append((code,v,good))
    return {'part':list(part),'tried':1<<(1+2*m+m*(m-1)//2),
            'best_minimum':str(best[0]),'best_mask':best[1],
            'successful':[(code,str(v),good) for code,v,good in successes]}

def main():
    parts=sorted({p for m in (1,2,3) for p in product(range(1,10),repeat=m)
                  if sum(p)==9 and p==tuple(sorted(p,reverse=True))})
    results=[scan(p) for p in parts]
    require(sum(r['tried'] for r in results)==7432,'search size drift')
    hits=[(r['part'],v) for r in results for v in r['successful']]
    require(hits==[([4,3,2],(727,'85/126',[1,7,27,59,85,85,59,27,7,1]))],
            'restricted search witness count changed')
    print(json.dumps({'restricted_model':
        'single orbit of a quadratic invariant within 1..3 labelled blocks',
        'ordered_size_partitions':len(parts),
        'coefficient_patterns_tested':7432,'successful_patterns':len(hits),
        'hits':hits,'best_by_block_size':[
           {'part':r['part'],'best_minimum':r['best_minimum'],
            'best_mask':r['best_mask'],'tried':r['tried']} for r in results]},
           sort_keys=True,indent=2))
if __name__=='__main__':main()
