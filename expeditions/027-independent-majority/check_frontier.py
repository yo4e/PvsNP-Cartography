#!/usr/bin/env python3
"""Bounded exact checks of the next growing-degree argument, not its proof.
This companion is not part of the completed majority CI run.
"""
from fractions import Fraction as F
from math import comb
import json

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def run():
    central = prefix = recurrence = 0
    for s in range(151):
        C = F(comb(2*s,s),4**s)
        Cp = F(comb(2*s+2,s+1),4**(s+1))
        require(Cp == C*F(2*s+1,2*s+2),'central recurrence')
        require((3*s+1)*C*C <= 1,'central square bound')
        require((3*s+1)*(2*s+2)**2-(3*s+4)*(2*s+1)**2==s,
                'inductive polynomial difference')
        recurrence += 1
    for m in range(1,151):
        c = F(comb(m,m//2),2**m)
        require(m*c*c <= 1,'parity-uniform central estimate')
        central += 1
        for d in range(16):
            B = F(sum(comb(m,j) for j in range(min(m,(m+8*d)//2)+1)),2**m)
            require(B <= F(1,2)+(4*d+F(1,2))*c,'parity-aware prefix')
            if m >= (16*d+2)**2:
                require(B <= F(3,4),'conditional prefix obstruction')
            prefix += 1
    delta=F(422009,4782969)
    margin = 1-2*delta-F(3,4)
    require(margin == F(1406897,19131876)>0,'amplified margin')
    return {'central_recurrence_checks':recurrence,'central_mass_checks':central,
            'prefix_checks':prefix,'amplified_margin_above_three_quarters':str(margin),
            'candidate_threshold':'n >= (16*d+2)^2 + 2',
            'scope':'same-author bounded exact checks; next-frontier proof is written but not Lean-accepted or independently reviewed; not covered by main exact CI'}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
