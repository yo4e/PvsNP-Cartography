#!/usr/bin/env python3
"""Exact, bounded audits of fibers and subset intersections. No Lean claim.

No optimizer, symbolic engine, or assert statements. Normal and -O runs must
produce identical output. Direct sample enumeration and closed formulas are
separate implementations; include every subset, not just sampled examples.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
import json


def require(ok: bool, reason: str) -> None:
    if not ok:
        raise ValueError(reason)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def main() -> None:
    fiber_cases = 0
    sample_cases = 0
    expectation_cases = 0
    input_records = []
    for n in range(13):
        single = Counter(1 << i for i in range(n))
        triple = Counter()
        mass = [Q(0) for _ in range(1 << n)]
        if n >= 3:
            for i in range(n):
                mass[1 << i] += Q(1, 2*n)
        for i, j, k in product(range(n), repeat=3):
            sample_cases += 1
            if len({i, j, k}) == 3:
                x = (1 << i) | (1 << j) | (1 << k)
                triple[x] += 1
                mass[x] += Q(1, 2*n*(n-1)*(n-2))
        for x in range(1 << n):
            w = x.bit_count()
            require(single[x] == int(w == 1), 'singleton fiber')
            require(triple[x] == 6*int(w == 3), 'distinct triple fiber')
            fiber_cases += 1
            if n >= 3:
                closed = Q(1,2*n) if w == 1 else Q(1,2*comb(n,3)) if w == 3 else Q(0)
                require(mass[x] == closed, 'actual pushforward vs closed mass')
        if n >= 3:
            require(sum(mass) == 1, 'normalization')
            require(all(p >= 0 for p in mass), 'positivity')
            require(sum(p for x,p in enumerate(mass) if x.bit_count()==1)==Q(1,2), 'layer one')
            require(sum(p for x,p in enumerate(mass) if x.bit_count()==3)==Q(1,2), 'layer three')
            # Signed and nonsymmetric test functions attack hidden positivity/symmetry assumptions.
            for g in (lambda x:Q(1), lambda x:Q(x*x-7*x+3,11),
                      lambda x:Q((-1)**(x.bit_count())*(x%7-3),5)):
                actual = sum(p*g(x) for x,p in enumerate(mass))
                layers = sum(g(x) for x in range(1<<n) if x.bit_count()==1)/Q(2*n)
                layers += sum(g(x) for x in range(1<<n) if x.bit_count()==3)/Q(2*comb(n,3))
                require(actual == layers, 'signed nonsymmetric expectation')
                expectation_cases += 1
            input_records.append({'n':n,'cube_inputs':1<<n,'positive_inputs':n+comb(n,3),
                                  'singleton_fiber':1,'distinct_triple_fiber':6})

    pair_cases = 0
    histogram_cases = 0
    for n in range(11):
        for A in range(1<<n):
            k = A.bit_count()
            hist = Counter()
            for X in range(1<<n):
                hist[X.bit_count(), (X&A).bit_count()] += 1
                pair_cases += 1
            for w in range(n+2):
                for r in range(n+2):
                    expected = choose(k,r)*choose(n-k,w-r) if r<=w else 0
                    require(hist[w,r] == expected, f'intersection n={n},k={k},w={w},r={r}')
                    histogram_cases += 1

    # A natural-subtraction implementation without r<=w has a concrete false count.
    bad_no_guard = choose(1,1)*choose(0,max(0,0-1))
    actual_empty_intersection = sum(X.bit_count()==0 and (X&1).bit_count()==1 for X in range(2))
    require(bad_no_guard == 1 and actual_empty_intersection == 0, 'range guard control')
    missing_factor_six_total = Q(1,2) + Q(1,12)
    require(missing_factor_six_total == Q(7,12) != 1, 'sixfold fiber control')
    # Extending normalization to n=2 loses the nonexistent weight-three half.
    require(sum(Q(1,4) for x in range(4) if x.bit_count()==1)==Q(1,2), 'n>=3 control')
    result = {'state':'bounded exact tests; formal generic claims require separate Lean execution',
              'fiber_arity_range':[0,12], 'fiber_input_cases':fiber_cases,
              'ordered_triple_samples':sample_cases,'normalization_arity_range':[3,12],
              'signed_expectation_tests':expectation_cases, 'input_records':input_records,
              'intersection_arity_range':[0,10], 'all_subset_pairs':pair_cases,
              'intersection_histogram_cells':histogram_cases,
              'negative_controls':{'missing_r_le_w':{'n':1,'k':1,'w':0,'r':1,'actual':0,'wrong':1},
                'drop_sixfold_fiber_mass':str(missing_factor_six_total),
                'extend_normalization_to_n2':'1/2'}}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
