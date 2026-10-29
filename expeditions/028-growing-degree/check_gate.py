#!/usr/bin/env python3
"""Finite exploration for the NEXT gate bridge, not a generic circuit proof."""
from itertools import product
from fractions import Fraction
from collections import Counter
import json


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def multiply(p, q):
    ans = set()
    for a in p:
        for b in q:
            e = tuple(x+y for x,y in zip(a,b))
            if e in ans:
                ans.remove(e)
            else:
                ans.add(e)
    return ans


def or_polynomial(k, masks):
    zero = (0,)*k
    p = {zero}
    for mask in masks:
        factor = {zero}
        for j in range(k):
            if mask>>j&1:
                e = tuple(int(i==j) for i in range(k))
                factor.add(e)
        p = multiply(p, factor)
    return p ^ {zero}  # 1-product in GF2


def evaluate(p, x):
    return sum(all(not e or (x>>j&1) for j,e in enumerate(a)) for a in p)%2


def direct(masks, x):
    return int(any((mask & x).bit_count()%2 for mask in masks))


def run():
    families = evaluations = pointwise_laws = 0
    max_degree = 0
    for k in range(5):
        for r in range(4):
            errors = Counter()
            for masks in product(range(1<<k), repeat=r):
                p = or_polynomial(k,masks)
                degree = max((sum(a) for a in p),default=0)
                need(degree <= r, 'actual, unreduced polynomial degree')
                max_degree = max(max_degree,degree)
                for x in range(1<<k):
                    value = evaluate(p,x)
                    need(value == direct(masks,x), 'sparse polynomial versus Boolean hash evaluation')
                    errors[x] += value != int(x!=0)
                    evaluations += 1
                families += 1
            total = 1 << (k*r)
            for x in range(1<<k):
                expected = Fraction(0) if x==0 else Fraction(1,1<<r)
                need(Fraction(errors[x],total)==expected, 'exact pointwise gate law')
                pointwise_laws += 1
    # One hash copied three times has the right one-trial marginal, not independence.
    repeated = Fraction(sum(direct((a,a,a),3)!=1 for a in range(4)),4)
    need(repeated == Fraction(1,2)>Fraction(1,8), 'shared-mask shortcut must fail')
    need((1+((0 & 0).bit_count()%2))%2 == 1, 'affine hash with constant1 fails at zero')
    p = or_polynomial(1,(1,1,1))
    need(p == {(1,),(2,),(3,)}, 'Boolean equivalence is not equality of actual degrees')
    return {'scope':'finite next-frontier controls, not a Lean theorem or circuit lower bound',
            'k_range':[0,4],'r_range':[0,3],'families':families,'input_evaluations':evaluations,
            'pointwise_laws':pointwise_laws,'largest_actual_degree':max_degree,
            'negative_controls':{'repeated_mask_error':str(repeated),'false_independent_bound':'1/8',
            'affine_constant_one_zero_input_output':1,
            'non_multilinear_example':'Q(x)=x+x^2+x^3 has actual degree3, Boolean function x'}}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
