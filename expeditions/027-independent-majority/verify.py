#!/usr/bin/env python3
"""Exact finite adversarial controls, NOT proof of the all-arity theorem.
Independent implementations: tuple enumeration vs binomial formula vs recurrence;
Boolean Mobius transform vs elementary DP; sparse actual polynomial composition;
Pascal rows vs multiplicative binomials. No assertion disappears under python -O.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, prod
import json
import random


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


@lru_cache(None)
def tail(p, r, k):
    if k == 0:
        return F(1)
    if r == 0:
        return F(0)
    return p*tail(p, r-1, k-1) + (1-p)*tail(p, r-1, k)


def binomial_tail(p, r, k):
    return sum((F(comb(r, j))*p**j*(1-p)**(r-j) for j in range(k, r+1)), F(0))


def pmul(p, q):
    out = set()
    for e in p:
        for f in q:
            g = tuple(a+b for a, b in zip(e, f))
            if g in out:
                out.remove(g)
            else:
                out.add(g)
    return out


def elementary8(polys, n):
    es = [{(0,)*n}] + [set() for _ in range(8)]
    for p in polys:
        for k in range(8, 0, -1):
            es[k] ^= pmul(es[k-1], p)
    return es[8]


def peval(p, x):
    # No multilinear reduction occurs in p. Boolean evaluation is a separate step.
    return sum(prod(bit**degree for bit, degree in zip(x, e)) for e in p) % 2


def degree(p):
    return max((sum(e) for e in p), default=0)


def run():
    delta = F(422009, 4782969)
    law_checks = tuple_evaluations = 0
    distributions = [(F(1,3),F(2,3)), (F(0),F(1,7),F(6,7)),
                     (F(1,6),F(1,3),F(1,2)), (F(0),F(1,10),F(2,5),F(1,2))]
    for mu in distributions:
        for flags in product((0,1), repeat=len(mu)):
            p = sum((w*b for w,b in zip(mu,flags)), F(0))
            for r in range(6):
                hist = [F(0)]*(r+1)
                for v in product(range(len(mu)), repeat=r):
                    weight = prod((mu[i] for i in v), start=F(1))
                    hist[sum(flags[i] for i in v)] += weight
                    tuple_evaluations += 1
                require(sum(hist)==1, 'actual independent product normalization')
                for k in range(r+2):
                    actual = sum(hist[k:], F(0))
                    require(actual == binomial_tail(p,r,k) == tail(p,r,k), 'three-way failure law')
                    law_checks += 1

    monotone_checks = 0
    for r in range(16):
        for k in range(r+2):
            previous = F(0)
            for a in range(25):
                p = F(a,24)
                got = tail(p,r,k)
                require(previous <= got <= 1, 'bounded monotonic tail')
                require(got == binomial_tail(p,r,k), 'recurrence versus closed binomial law')
                require(tail(p,r,k+1) <= got, 'threshold antitone')
                previous = got
                monotone_checks += 1
    require(tail(F(1,3),15,8)==delta, 'exact majority15 error')

    # Evaluate elementary8 by a DP distinct from the choose-parity identity.
    truth = []
    for mask in range(1<<15):
        es = [1]+[0]*8
        for j in range(15):
            bit = (mask>>j)&1
            for k in range(8,0,-1):
                es[k] ^= es[k-1]*bit
        expected = int(mask.bit_count()>=8)
        require(es[8]==expected, 'actual majority truth table')
        truth.append(expected)
    anf = truth.copy()
    for j in range(15):
        for mask in range(1<<15):
            if mask>>j&1:
                anf[mask] ^= anf[mask^(1<<j)]
    require(all(c==int(mask.bit_count()==8) for mask,c in enumerate(anf)), 'independent majority ANF')
    require(sum(anf)==comb(15,8)==6435, 'eighth elementary polynomial support')

    rng = random.Random(20261028)
    compositions = composition_evaluations = restriction_evaluations = 0
    largest_composed_degree = 0
    cases = [(n,d) for n in range(4) for d in range(3)]+[(2,3)]
    for n,d in cases:
        monomials = [e for e in product(range(d+1),repeat=n) if sum(e)<=d]
        for _ in range(3):
            polys = [{e for e in monomials if rng.randrange(2)} for _ in range(15)]
            q = elementary8(polys,n)
            require(degree(q)<=8*d, 'genuine total-degree composition bound')
            largest_composed_degree = max(largest_composed_degree,degree(q))
            for x in product((0,1),repeat=n):
                vals = [peval(p,x) for p in polys]
                require(peval(q,x)==int(sum(vals)>=8), 'polynomial composition vs Boolean majority')
                for target in (0,1):
                    require(int(peval(q,x)!=target)==int(sum(a!=target for a in vals)>=8),
                            'majority failure threshold including target one')
                composition_evaluations += 1
            if n:
                for p in polys:
                    restricted = {e[1:] for e in p if e[0]==0}
                    require(degree(restricted)<=degree(p), 'actual zero restriction degree')
                    for x in product((0,1),repeat=n-1):
                        require(peval(restricted,x)==peval(p,(0,)+x), 'actual zero restriction evaluation')
                        require((sum((0,)+x)%3==0)==(sum(x)%3==0), 'target zero padding')
                        restriction_evaluations += 1
            compositions += 1

    # Actual constant-polynomial family: correct0 mass2/3, wrong1 mass1/3.
    # Independent tuples give delta; the diagonal reuse has error1/3.
    reused = F(1,3)
    independent = sum(F(comb(15,k)*2**(15-k),3**15) for k in range(8,16))
    require(independent==delta<reused, 'correlation invalidates error reduction')
    # Signed normalized family2,-1 has apparent success2 but p=-1.
    # Its exact product identity survives; a probability upper bound does not.
    require(tail(F(-1),15,8)==580865>delta, 'signed mass defeats amplification')

    row = [1]
    binomial_checks = 0
    for n in range(301):
        fast = [1]
        for k in range(n):
            numerator = fast[-1]*(n-k)
            require(numerator%(k+1)==0, 'multiplicative binomial exact division')
            fast.append(numerator//(k+1))
        require(row==fast, 'Pascal vs multiplicative row')
        binomial_checks += len(row)
        row = [1]+[row[k-1]+row[k] for k in range(1,len(row))]+[1]
    B = sum(comb(297,j) for j in range(157))
    require(B==209660394993883821947535023324611441185492248181130328034971979979928832110669599839817888,
            'n299 binomial prefix')
    gap = (1-2*delta)*2**297-B
    require(gap>0, 'strict exact obstruction gap')
    B300 = sum(comb(298,j) for j in range(158))
    gap300 = (1-2*delta)*2**298-B300
    require(gap300<0, 'parity prevents naive all-n numerical extrapolation')
    return {
      'seed':20261028,'tuple_evaluations':tuple_evaluations,'exact_failure_law_checks':law_checks,
      'tail_comparisons':monotone_checks,'majority_truth_inputs':1<<15,'majority_anf_degree':8,
      'majority_anf_terms':sum(anf),'actual_polynomial_families':compositions,
      'composition_input_evaluations':composition_evaluations,
      'zero_restriction_evaluations':restriction_evaluations,'largest_composed_degree_seen':largest_composed_degree,
      'binomial_coefficients_cross_checked':binomial_checks,'delta':str(delta),
      'tickets_15_8':int(delta*3**15),'B_297_16':B,
      'strict_gap_n299':{'numerator':gap.numerator,'denominator':gap.denominator},
      'parity_countercontrol_n300':{'B_298_16':B300,'gap_numerator':gap300.numerator,
                                  'gap_denominator':gap300.denominator},
      'negative_controls':{'diagonal_reuse_error':str(reused),'independent_error':str(independent),
        'signed_mass':[2,-1],'signed_product_error':580865,
        'degree_seven_majority15':'refuted by nonzero degree-eight ANF coefficients',
        'direct_binomial_gap_monotone_in_n':'refuted at n299 to n300'},
      'scope':'finite exact corroboration and counterexamples; no independent semantic review, general proof, novelty or optimal threshold inferred from these tests'}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
