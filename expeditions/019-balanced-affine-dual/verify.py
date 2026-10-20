#!/usr/bin/env python3
"""Exact finite tests for a generic balanced affine-dual score formula.

Bounded tests do not prove the all-n counting bridge. The separate Lean file
proves only the real algebraic inequality after the score formula is supplied.
"""
from fractions import Fraction as F
from math import comb
import json


def require(ok, why):
    if not ok:
        raise ValueError(why)


def hypergeom(n, k):
    odd = k*comb(n-k,2)+comb(k,3)
    return F(n-k,2*n)+F(odd,2*comb(n,3))


def cubic(n, k):
    t = n-2*k
    return F(1,2)+F(t*(n*n-t*t),4*n*(n-1)*(n-2))


def walsh(values):
    v = values[:]
    step = 1
    while step < len(v):
        for start in range(0,len(v),2*step):
            for i in range(start,start+step):
                a,b = v[i],v[i+step]
                v[i],v[i+step] = a+b,a-b
        step *= 2
    return v


def main():
    cases = 0
    selected = {}
    for n in range(3,257):
        vals = []
        for k in range(n+1):
            v = cubic(n,k)
            require(v==hypergeom(n,k), 'counting formula mismatch')
            require(cubic(n,n-k)==1-v,'constant/complement identity')
            if n>=7:
                require(F(1,3)<v<F(2,3),'strict interval failed')
                require(v<=F(1,2)+F(n*n,10*(n-1)*(n-2)), 'rational envelope failed')
            vals.append(v)
            cases += 1
        if n<=12 or n in (16,32,64,128,256):
            selected[str(n)] = {'maximum':str(max(vals)), 'argmax_k':[k for k,v in enumerate(vals) if v==max(vals)]}

    counts = []
    for n in range(3,13):
        C = comb(n,3)
        target = [int(x.bit_count()%3==0) for x in range(1<<n)]
        mass = [C if x.bit_count()==1 else n if x.bit_count()==3 else 0 for x in range(1<<n)]
        D = 2*n*C
        require(sum(mass)==D,'equal-half input mass failed')
        W = walsh([m*(1-2*f) for m,f in zip(mass,target)])
        for a,w in enumerate(W):
            require(F(D+w,2*D)==cubic(n,a.bit_count()),'full Walsh versus cubic mismatch')
            require(F(D-w,2*D)==1-cubic(n,a.bit_count()),'constant-one scores mismatch')
        support = [(x,m) for x,m in enumerate(mass) if m]
        for k in range(n+1):
            a = (1<<k)-1
            direct = sum(m for x,m in support if ((a&x).bit_count()%2)==target[x])
            require(F(direct,D)==hypergeom(n,k),'direct canonical summation mismatch')
        counts.append({'n':n,'inputs':1<<n,'affine_rows':2*(1<<n)})

    # Exact adversarial boundaries, not evidence that affine families are feasible.
    require(cubic(6,1)==F(2,3),'n6 tight counterexample missing')
    require(cubic(5,1)==F(7,10)>F(2,3),'n5 failure missing')
    require(cubic(11,2)==F(69,110),'known n11 bound mismatch')
    require(F(1,2)-F((11-4)*(121-(11-4)**2),4*11*10*9)!=cubic(11,2),
            'wrong-sign negative control inactive')
    print(json.dumps({'state':'bounded exact tests; not an all-n counting proof',
                      'formula_n_range':[3,256],'formula_cases':cases,
                      'full_cube_n_range':[3,12],'full_cube_checks':counts,
                      'selected_maxima':selected,
                      'counterexamples':{'strict_bound_n6_k1':'2/3','strict_bound_n5_k1':'7/10'},
                      'negative_controls_rejected':['extend_strict_bound_to_n6','extend_to_n5','reverse_cubic_sign']},
                     sort_keys=True,indent=2))


if __name__=='__main__':
    main()
