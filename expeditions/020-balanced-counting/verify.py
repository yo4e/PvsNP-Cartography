#!/usr/bin/env python3
"""Independent exact audit of ordered-single/triple balanced affine sampling.

No Lean compiler is invoked here. Finite ranges do not prove generic lemmas.
All checks use explicit exceptions, so Python -O cannot disable them.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from math import comb
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def moment(values):
    return sum(values[i]*values[j]*values[k]
               for i,j,k in permutations(range(len(values)),3))


def cubic(n,k):
    t=n-2*k
    return F(1,2)+F(t*(n*n-t*t),4*n*(n-1)*(n-2))


def sample_mass(n):
    """Integer measure with denominator 2*n*(n-1)*(n-2)."""
    require(n>=3,'empty triple layer')
    masses=Counter()
    for i in range(n):
        masses[1<<i]+=(n-1)*(n-2)
    for i,j,k in product(range(n),repeat=3):
        if len({i,j,k})==3:
            masses[(1<<i)|(1<<j)|(1<<k)]+=1
    return masses,2*n*(n-1)*(n-2)


def main():
    moment_cases=0
    for size in range(7):
        for values in product((-1,0,1),repeat=size):
            s=sum(values); q=sum(v*v for v in values); r=sum(v**3 for v in values)
            require(moment(values)==s**3-3*q*s+2*r,'moment identity')
            moment_cases+=1
    cube_records=[]; raw_evaluations=0
    for n in range(3,13):
        masses,D=sample_mass(n)
        require(sum(masses.values())==D,'normalization')
        require(len(masses)==n+comb(n,3),'support')
        for x,m in masses.items():
            w=x.bit_count()
            require(w in (1,3),'wrong input layer')
            require(F(m,D)==F(1,2*comb(n,w)),'pushforward is not uniform on a layer')
        maxima=F(0)
        for a in range(1<<n):
            k=a.bit_count()
            score0=sum(m for x,m in masses.items()
                       if ((a&x).bit_count()%2)==int(x.bit_count()%3==0))
            observed=F(score0,D)
            odd=k*comb(n-k,2)+comb(k,3)
            counted=F(n-k,2*n)+F(odd,2*comb(n,3))
            require(observed==counted==cubic(n,k),'actual/counted/cubic mismatch')
            values=[1-2*((a>>i)&1) for i in range(n)]
            t=sum(values)
            require(moment(values)==t**3-(3*n-2)*t,'sign moment')
            score1=sum(m for x,m in masses.items()
                       if (1^((a&x).bit_count()%2))==int(x.bit_count()%3==0))
            require(score1==D-score0,'direct constant complement')
            require(F(score1,D)==cubic(n,n-k),'constant-one complement')
            maxima=max(maxima,observed,F(score1,D))
            raw_evaluations+=2*len(masses)
        if n>=7:
            envelope=F(1,2)+F(n*n,10*(n-1)*(n-2))
            require(maxima<=envelope<F(2,3),'strict uniform envelope')
        cube_records.append({'n':n,'input_support':len(masses),'sample_denominator':D,
                             'affine_rows':2**(n+1),'maximum':str(maxima)})
    formula_cases=0
    for n in range(3,257):
        for k in range(n+1):
            odds=k*comb(n-k,2)+comb(k,3)
            counted=F(n-k,2*n)+F(odds,2*comb(n,3))
            require(counted==cubic(n,k),'bounded formula identity')
            if n>=7:
                require(F(1,3)<counted<F(2,3),'bounded strict gap')
            formula_cases+=1
    controls={
        'omit_double_diagonal_correction':{'n':3,'values':[1,1,1],
            'actual_distinct_sum':moment([1,1,1]),'incorrect_expression':27-3*3*3},
        'use_unordered_denominator_for_ordered_triples':{'n':3,'total_mass':str(F(1,2)+F(6,2*comb(3,3)))},
        'allow_repeated_coordinates_with_distinct_denominator':{'n':3,'total_mass':str(F(1,2)+F(3**3,2*3*2*1))},
        'extend_strict_gap_to_six':{'n':6,'coefficient_weight':1,'success':str(cubic(6,1))}
    }
    require(controls['omit_double_diagonal_correction']['actual_distinct_sum']!=
            controls['omit_double_diagonal_correction']['incorrect_expression'],'diagonal mutation escaped')
    require(F(controls['use_unordered_denominator_for_ordered_triples']['total_mass'])!=1,'sixfold mutation escaped')
    require(F(controls['allow_repeated_coordinates_with_distinct_denominator']['total_mass'])!=1,'duplicate mutation escaped')
    require(cubic(6,1)==F(2,3),'boundary')
    print(json.dumps({'state':'bounded exact audit, not generic formal acceptance',
                      'moment_cases':moment_cases,'moment_sizes':[0,6],
                      'moment_values':[-1,0,1], 'cube_checks':cube_records,
                      'actual_affine_input_checks':raw_evaluations,
                      'formula_cases':formula_cases,'formula_n_range':[3,256],
                      'negative_controls':controls},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
