#!/usr/bin/env python3
"""Exhaustive exact n12 dual for zero + all q_9 + all r_8, NOT all quadratics."""
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    n = 12
    universe = (1 << n) - 1
    support = []
    for w, mass in [(6,5), (10,126)]:
        for positions in combinations(range(n), w):
            x = sum(1 << i for i in positions)
            support.append((x, mass, int(w % 3 == 0)))
    denominator = sum(m for _,m,_ in support)
    require(denominator == 12936, 'normalization')
    require(Fraction(5*comb(n,6),denominator) == Fraction(5,14), 'layer six mass')
    require(Fraction(126*comb(n,10),denominator) == Fraction(9,14), 'layer ten mass')
    zero_score = sum(m for _,m,target in support if target == 0)
    all_scores = [zero_score]
    family_scores = {}
    comparisons = len(support)
    for name, size, outside in [('q9',9,False), ('r8',8,True)]:
        scores = []
        for positions in combinations(range(n), size):
            subset = sum(1 << i for i in positions)
            linear = universe ^ subset if outside else universe
            edges = tuple((1 << i) | (1 << j) for i,j in combinations(positions,2))
            score = 0
            for x,mass,target in support:
                value = (1 + (x & linear).bit_count()
                         + sum((x & edge) == edge for edge in edges)) % 2
                if value == target:
                    score += mass
                comparisons += 1
            scores.append(score)
        require(len(scores) == comb(n,size), 'not every subset enumerated')
        expected = 8316 if name == 'q9' else 6748
        require(set(scores) == {expected}, 'unexpected deterministic score')
        all_scores += scores
        family_scores[name] = {'count':len(scores), 'integer_score':expected,
                              'success':str(Fraction(expected,denominator))}
    require(len(all_scores) == 716, 'candidate family size')
    require(max(all_scores) == 8316, 'dual maximum')
    require(Fraction(max(all_scores),denominator) == Fraction(9,14) < Fraction(2,3), 'strict obstruction')
    # Independent binomial profile counts at the two supported input weights.
    def choose(a,b):
        return comb(a,b) if 0 <= b <= a else 0
    for size,outside,expected in [(9,False,8316),(8,True,6748)]:
        total = 0
        for w,mass in [(6,5),(10,126)]:
            count = sum(choose(size,t)*choose(n-size,w-t)
                        * int((1+(w-t if outside else w)+choose(t,2))%2 == int(w%3==0))
                        for t in range(w+1))
            total += mass*count
        require(total == expected, 'independent profile formula differs')
    print(json.dumps({
        'scope':'n12: zero, all q_A with |A|=9, all r_B with |B|=8; arbitrary finite real mixtures of this restricted family only',
        'input_mass_by_weight':{'6':5,'10':126}, 'input_mass_total':denominator,
        'supported_inputs':len(support), 'candidate_polynomials':len(all_scores),
        'actual_polynomial_input_comparisons':comparisons,
        'family_scores':family_scores,
        'zero_integer_score':zero_score, 'maximum_integer_score':max(all_scores),
        'maximum_success':'9/14','strict_gap':'1/42',
        'not_claimed':'not all degree-two polynomials, not a separately compiled Lean corollary, not n12 probabilistic degree'
    },sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
