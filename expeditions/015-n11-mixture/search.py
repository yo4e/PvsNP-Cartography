#!/usr/bin/env python3
"""Bounded exploratory n11 block-orbit LP. Floating output is NOT evidence.
Exact rounded weights are separately certified by verify.py.
"""
from itertools import product
from math import comb
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
N=11
sizes=np.array([comb(N,w) for w in range(N+1)],dtype=np.int64)
parity=np.array([i.bit_count()%2 for i in range(1024)],dtype=np.int64)
codes=np.arange(1024,dtype=np.int64)
shapes=[(N-b-c,b,c) for c in range(1,N//3+1)
        for b in range(c,(N-c)//2+1)]
profiles={}
for shape in shapes:
    good=np.zeros((1024,N+1),dtype=np.int64)
    for k in product(*(range(s+1) for s in shape)):
        w=sum(k)
        vals=[1,*k,*(comb(v,2) for v in k),k[0]*k[1],k[0]*k[2],k[1]*k[2]]
        feature=sum((v%2)<<i for i,v in enumerate(vals))
        multiplicity=int(np.prod([comb(s,v) for s,v in zip(shape,k)]))
        good[:,w]+=(parity[codes&feature]==int(w%3==0))*multiplicity
    for code,g in enumerate(good):
        key=tuple(map(int,g))
        profiles.setdefault(key,(shape,code))
counts=np.array(list(profiles),dtype=np.float64)
A=counts/sizes
v=len(A)
res=linprog(np.r_[np.zeros(v),-1.0],A_ub=np.c_[-A.T,np.ones(N+1)],
            b_ub=np.zeros(N+1),A_eq=np.array([np.r_[np.ones(v),0.0]]),b_eq=[1.0],
            bounds=[(0,None)]*v+[(0,1)],method='highs')
if not res.success:
    raise RuntimeError(res.message)
positive=np.flatnonzero(res.x[:v]>1e-9)
weights=res.x[positive];D=10000
integer=np.floor(weights*D).astype(int)
for i in np.argsort(-(weights*D-integer))[:D-int(integer.sum())]: integer[i]+=1
seeds=[]
keys=list(profiles)
for idx,mass in zip(positive,integer):
    if mass:
        shape,code=profiles[keys[idx]]
        seeds.append({'blocks':list(shape),'code':int(code),'weight':int(mass),'good':list(keys[idx])})
out={'n':N,'field':'GF(2)','target':'one iff Hamming weight divisible by three','error':'1/3',
     'distribution':'choose seed with fixed weight, then uniformly permute all coordinates',
     'probability_denominator':D,'seeds':seeds,
     'dual_mass_by_weight':{'1':15,'3':1},'dual_denominator':330,
     'search':{'three_block_shapes':shapes,'raw_patterns_including_duplicates':len(shapes)*1024,
               'distinct_layer_profiles':len(profiles),'numerical_maximin_not_a_proof':float(res.x[-1]),
               'numerical_solver':'scipy.optimize.linprog(method=highs)',
               'rounding':'largest remainders at integer denominator10000'}}
Path(__file__).with_name('candidate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'search':out['search'],'positive_orbits':len(seeds),'seeds':seeds},indent=2))
