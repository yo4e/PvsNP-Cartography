#!/usr/bin/env python3
"""Exact GF(4) agreement/compression controls, not a proof for arbitrary n.
Independent implementations: sparse polynomial arithmetic, truth-table evaluation,
finite-field row reduction, and Boolean Mobius coefficients. Standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return r


def inv(a):
    require(a != 0, 'division by zero')
    return mul(a, a)


def prod(xs):
    r = 1
    for x in xs:
        r = mul(r, x)
    return r


def peval(p, y):
    r = 0
    for e, c in p.items():
        v = c
        for a, k in zip(y, e):
            for _ in range(k):
                v = mul(v, a)
        r ^= v
    return r


def pmul(p, q):
    r = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(x+y for x, y in zip(e, f))
            r[g] = r.get(g, 0) ^ mul(a, b)
    return {e: c for e, c in r.items() if c}


def reduce_grid(p, a=1, b=2):
    # y^2 = (a+b)y + ab in characteristic two. No assumption y^2=y.
    r = {}
    n = len(next(iter(p))) if p else 0
    for e, coefficient in p.items():
        partial = {(0,)*n: coefficient}
        for i, power in enumerate(e):
            c0, c1 = 1, 0
            for _ in range(power):
                c0, c1 = mul(c1, mul(a,b)), c0 ^ mul(c1, a^b)
            unit = tuple(int(j == i) for j in range(n))
            factor = {(0,)*n: c0, unit: c1}
            partial = pmul(partial, {k: v for k, v in factor.items() if v})
        for k, v in partial.items():
            r[k] = r.get(k, 0) ^ v
    return {k: v for k, v in r.items() if v}


def rank(rows):
    basis = {}
    for row in rows:
        row = list(row)
        for j in range(len(row)):
            c = row[j]  # Read the CURRENT row after earlier elimination steps.
            if c == 0:
                continue
            if j in basis:
                row = [a ^ mul(c,b) for a,b in zip(row,basis[j])]
            else:
                z = inv(c)
                basis[j] = [mul(z,a) for a in row]
                break
    return len(basis)


def tail(copies):
    return sum(F(comb(copies,k)*2**(copies-k), 3**copies)
               for k in range(copies//2+1, copies+1))


def main():
    # Independent field identities, including the nontrivial inverse alpha^-1=alpha+1.
    for a,b,c in product(range(4), repeat=3):
        require(mul(a,b^c) == mul(a,b)^mul(a,c), 'distributivity')
        require(mul(mul(a,b),c) == mul(a,mul(b,c)), 'associativity')
    for a in (1,2,3):
        require(mul(a, inv(a)) == 1, 'inverse')
    # Adversarial regression: rebinding a list inside enumerate(old_list) reads stale pivots.
    require(rank([[1,1],[1,0]]) == 2, 'rank stale-iterator counterexample')
    require(rank([[1,1],[1,1]]) == 1, 'dependent rows must not acquire fake pivots')
    matrix_checks = 0
    for a,b,c,d in product(range(4), repeat=4):
        determinant = mul(a,d) ^ mul(b,c)
        expected_rank = 2 if determinant else int(any((a,b,c,d)))
        require(rank([[a,b],[c,d]]) == expected_rank, 'independent 2x2 determinant rank')
        matrix_checks += 1
    inverse_cases = 0
    for a,b in product((1,2,3),repeat=2):
        for y in (a,b):
            require(mul(y,mul(a^b^y, inv(mul(a,b)))) == 1, 'affine inverse')
            inverse_cases += 1
    require(mul(2,2) != 1, 'y itself is not the inverse on this grid')

    configurations = [(n,d) for n in range(5) for d in range(min(n,1)+1)] + [(2,2),(3,2)]
    counts = []
    compression_checks = 0
    rank_checks = 0
    for n,d in configurations:
        grid = list(product((1,2), repeat=n))
        masks = [s for s in range(1<<n) if s.bit_count() <= d]
        exponents = [tuple((s>>i)&1 for i in range(n)) for s in masks]
        values = [[prod(y[i] for i in range(n) if (s>>i)&1) for y in grid] for s in masks]
        full = [prod(y) for y in grid]
        t = (n+d)//2
        low = [s for s in range(1<<n) if s.bit_count() <= t]
        lowvalues = [[prod(y[i] for i in range(n) if (s>>i)&1) for s in low] for y in grid]
        bound = sum(comb(n,j) for j in range(min(n,t)+1))
        max_agreement = 0
        for cs in product(range(4),repeat=len(masks)):
            v = [0]*len(grid)
            for c, vs in zip(cs,values):
                for j,u in enumerate(vs):
                    v[j] ^= mul(c,u)
            H = [j for j in range(len(grid)) if v[j] == full[j]]
            max_agreement = max(max_agreement,len(H))
            require(len(H) <= bound, 'dimension agreement bound')
            require(rank([lowvalues[j] for j in H]) == len(H), 'low-degree evaluation surjectivity')
            rank_checks += 1
            R = {e:c for e,c in zip(exponents,cs) if c}
            for S in range(1<<n):
                if S.bit_count() <= t:
                    continue
                Q = R
                # For a=1,b=alpha, inverseFactor = alpha + (alpha+1)*y.
                for i in range(n):
                    if not (S>>i)&1:
                        unit = tuple(int(j==i) for j in range(n))
                        Q = pmul(Q, {(0,)*n:2, unit:3})
                require(max((sum(e) for e in Q), default=0) <= t, 'actual compressed degree')
                red = reduce_grid(Q)
                require(max((sum(e) for e in red), default=0) <= t, 'multilinear reduction degree')
                for j in H:
                    expected = prod(grid[j][i] for i in range(n) if (S>>i)&1)
                    require(peval(Q,grid[j]) == peval(red,grid[j]) == expected, 'compression evaluation')
                    compression_checks += 1
        counts.append({'n':n,'degree':d,'polynomials':4**len(masks),
                       'dimension_bound':bound,'max_agreement':max_agreement})

    # Hostile boundary controls.
    boolean_zero_agreement = sum(prod(y) == 0 for y in product((0,1), repeat=3))
    wrong_nonzero_free_bound = sum(comb(3,j) for j in range(2))
    require(boolean_zero_agreement > wrong_nonzero_free_bound, 'zero-grid counterexample')
    require(peval({}, (1,)) == 0 != 1, 'agreement-set condition is necessary')
    # On {1,alpha}^2, constant alpha agrees at the two weight1 points.
    require(sum(prod(y)==2 for y in product((1,2),repeat=2)) == 2 > 1,
            'rounding threshold down too far')

    # Majority15 is e8 over GF(2): independent Mobius transform of the full truth table.
    truth = [int(x.bit_count() >= 8) for x in range(1<<15)]
    anf = truth.copy()
    for i in range(15):
        for s in range(1<<15):
            if (s>>i)&1:
                anf[s] ^= anf[s^(1<<i)]
    require(all(c == int(s.bit_count()==8) for s,c in enumerate(anf)), 'majority15 exact ANF')
    require(all(comb(w,8)%2 == int(w>=8) for w in range(16)), 'binomial majority identity')
    err = tail(15)
    require(err == F(422009,4782969), 'majority tail')
    # Exact coefficient proof of monotonicity for all real p in [0,1].
    coeff = [0]*16
    for k in range(8,16):
        for j in range(16-k):
            coeff[k+j] += comb(15,k)*comb(15-k,j)*(-1)**j
    deriv = [(i+1)*coeff[i+1] for i in range(15)]
    expected = [0]*15
    for j in range(8):
        expected[7+j] = 15*comb(14,7)*comb(7,j)*(-1)**j
    require(deriv == expected, 'tail derivative identity')
    require(F(1,3) > err, 'reusing one draw does not amplify')

    # Two residue indicators encode all three roots without multiplying indicators.
    root_cases = 0
    for m in range(13):
        for x in range(1<<m):
            w = x.bit_count()
            f0, f1 = int(w%3==0), int((w+2)%3==0)
            encoded = 3 ^ mul(2,f0) ^ f1
            expected = (1,2,3)[w%3]
            require(encoded == expected, 'root encoding / padding')
            root_cases += 1
    require((1,2,3)[1] != (1,2,3)[2], 'single residue indicator loses information')

    # This exact numerical obstruction is only one part of the unformalized whole bridge.
    m,D = 297,16
    t = (m+D)//2
    Bnum = sum(comb(m,j) for j in range(t+1))
    B = F(Bnum, 2**m)
    required = 1-2*err
    require(B < required, 'n299 parameter inequality')
    # Independent binomial recurrence, not another call to comb.
    terms = [1]
    for k in range(m):
        numerator = terms[-1]*(m-k)
        require(numerator%(k+1)==0, 'binomial recurrence integral')
        terms.append(numerator//(k+1))
    require(sum(terms)==2**m and sum(terms[:t+1])==Bnum, 'independent binomial calculation')
    return {
      'field':'GF(4)=GF(2)[alpha]/(alpha^2+alpha+1), alpha=2',
      'exhaustive_cases':counts,'rank_checks':rank_checks,'compression_input_checks':compression_checks,
      'affine_inverse_cases':inverse_cases,'independent_matrix_checks':matrix_checks,
      'negative_controls':{'zero_grid_agreement':boolean_zero_agreement,'invalid_zero_grid_bound':wrong_nonzero_free_bound,
          'wrong_inverse_rejected':True,'outside_agreement_rejected':True,'overaggressive_rounding_rejected':True,
          'single_residue_encoding_rejected':True,'dependent_repetition_error':'1/3'},
      'majority15':{'truth_values':len(truth),'anf_degree':8,'nonzero_coefficients':sum(anf),
          'error':str(err),'derivative':'51480*p^7*(1-p)^7'},
      'root_encoding_cases':root_cases,
      'numerical_bridge':{'original_n':299,'restricted_m':m,'degree_before':2,'degree_after':D,
          'cutoff':t,'agreement_numerator':Bnum,'agreement_denominator':2**m,
          'required_success':str(required),'positive_gap':str(required-B),
          'status':'exact arithmetic; full n299 proof is author reconstruction, not end-to-end Lean'},
      'not_established':['novelty','independent semantic review','full Lean dimension or n299 theorem','n12 degree','P vs NP']}

if __name__ == '__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
