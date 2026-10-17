#!/usr/bin/env python3
"""Explore subsets of nine saved n11 seeds; no global minimality is proved."""
import json, itertools, math
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
p=Path(__file__).resolve().parent
d=json.loads((p/'certificate.json').read_text()); S=d['seeds']; sizes=np.array([math.comb(11,w) for w in range(12)])
A=np.array([s['good'] for s in S])/sizes
best=None; trials=0
for k in range(1,10):
    for subset in itertools.combinations(range(9),k):
        trials+=1; a=A[list(subset)]
        r=linprog(np.r_[np.zeros(k),-1], A_ub=np.c_[-a.T,np.ones(12)],b_ub=np.zeros(12), A_eq=[np.r_[np.ones(k),0]],b_eq=[1],bounds=[(0,None)]*k+[(0,1)],method='highs')
        if not r.success or r.x[-1]<=2/3+1e-6: continue
        if best is None or r.x[-1]>best[0]:best=(float(r.x[-1]),subset,r.x[:k])
    if best:break
print('trials',trials,'first_support_size_with_numerical_margin_not_a_proof',k,'best',best)
if best:
    for D in range(2,501):
        ideal=best[2]*D; masses=np.floor(ideal).astype(int)
        for i in np.argsort(-(ideal-masses))[:D-int(masses.sum())]:masses[i]+=1
        exact=[sum(F(int(m),D)*F(S[idx]['good'][w],int(sizes[w])) for idx,m in zip(best[1],masses)) for w in range(12)]
        if min(exact)>F(2,3) and all(masses):
            out={key:value for key,value in d.items() if key!='search'}
            out['probability_denominator']=D
            out['seeds']=[dict(S[i],weight=int(m)) for i,m in zip(best[1],masses)]
            out['search']={'kind':'subset refinement of nine known seed orbits','numerical_trials':trials,'numerical_best_minimum_in_selected_subset':best[0], 'denominator':D,'optimality_claim':'none; optimizer is candidate selector only'}
            (p/'compact-candidate.json').write_text(json.dumps(out,indent=2)+'\n')
            print('denominator',D,'indices',best[1], 'masses',list(map(int,masses)),'min',str(min(exact)),'by_layer',list(map(str,exact)));break
