#!/usr/bin/env python3
"""Finite checks only. Same-author implementations, no universal/independent proof.
Python >=3.10, no third-party dependencies. Explicit checks survive python -O.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations_with_replacement
from math import comb
import json


def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)


def fwht(values):
    a = list(values)
    h = 1
    require(len(a) > 0 and len(a) & (len(a)-1) == 0, 'power-of-two input')
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                u, v = a[k], a[k+h]
                a[k], a[k+h] = u+v, u-v
        h *= 2
    return a


def affine_rows(n):
    N = 1 << n
    return tuple(sum((((a & x).bit_count() & 1) ^ b) << x for x in range(N))
                 for a in range(N) for b in (0, 1))


def reduction_checks():
    counts = Counter()
    for n, d in ((0, 3), (1, 5), (2, 3), (3, 2)):
        monomials = [e for e in product(range(d+1), repeat=n) if sum(e) <= d]
        xs = tuple(product((0, 1), repeat=n))
        seen = set()
        for coeff in range(1 << len(monomials)):
            terms = [e for j, e in enumerate(monomials) if coeff >> j & 1]
            reduced = set()
            for e in terms:
                support = tuple(int(t > 0) for t in e)
                if support in reduced:
                    reduced.remove(support)
                else:
                    reduced.add(support)
            require(max(map(sum, reduced), default=0) <= d, 'degree reduction')
            values = []
            for x in xs:
                direct = sum(__import__('functools').reduce(lambda a, b: a*b,
                             (b**e for b, e in zip(x, term)), 1) for term in terms) % 2
                squarefree = sum(all(not e or b for b, e in zip(x, term))
                                 for term in reduced) % 2
                require(direct == squarefree, 'actual power/squarefree value')
                values.append(direct)
                counts['point_evaluations'] += 1
            seen.add(tuple(values))
            counts['actual_polynomials'] += 1
        M = sum(comb(n, j) for j in range(min(n, d)+1))
        require(len(seen) == 1 << M, 'evaluation-row count')
        counts['parameter_cases'] += 1
    return dict(counts)


def affine_detection():
    cases, total = [], 0
    for n in range(5):
        N = 1 << n
        rows = affine_rows(n)
        hist = Counter()
        for f in range(1 << N):
            direct = min((f ^ p).bit_count() for p in rows)
            spectrum = fwht(1 - 2*((f >> x) & 1) for x in range(N))
            require((N-max(map(abs, spectrum))) % 2 == 0, 'distance parity')
            fast = (N-max(map(abs, spectrum))) // 2
            require(direct == fast, 'Walsh/brute affine mismatch')
            hist[direct] += 1
            total += 1
        volume = sum(comb(N, j) for j in range(N//3+1))
        covered = sum(c for d, c in hist.items() if d <= N//3)
        require(covered <= len(rows)*volume, 'cover union bound')
        cases.append(dict(n=n, targets=1 << N, covered=covered,
                          far=(1 << N)-covered, distance_histogram=dict(sorted(hist.items()))))
    return dict(targets=total, cases=cases)


def mixture_checks():
    tested = good = 0
    # Restricted denominator-three tests, not classification of real feasibility.
    for n in range(3):
        N = 1 << n
        rows = affine_rows(n)
        for selected in combinations_with_replacement(range(len(rows)), 3):
            for f in range(1 << N):
                tested += 1
                fails = [sum(((rows[i]^f) >> x) & 1 for i in selected) for x in range(N)]
                if max(fails) <= 1:
                    good += 1
                    require(any((rows[i]^f).bit_count() <= N//3 for i in selected),
                            'positive support integer witness')
    return dict(tested=tested, qualifying_pointwise_mixtures=good,
                scope='denominator-three finite mixtures only; unselected rows have weight zero')


def residue_coefficients(n, k):
    # Coefficient of z^0 in (1-z)^k(1+z)^(n-k) modulo z^3-1.
    v = (1, 0, 0)
    for j in range(n):
        sign = -1 if j < k else 1
        v = tuple(v[i]+sign*v[(i-1) % 3] for i in range(3))
    return v[0]


def mod3_checks():
    counts = (1, 0, 0)
    phases = (2, 1, -1, -2, -1, 1)
    population_cases = spectrum_cases = balanced_pass = 0
    examples = []
    for n in range(513):
        N = 1 << n
        direct = tuple(sum(comb(n, j) for j in range(s, n+1, 3)) for s in range(3))
        require(counts == direct and sum(counts) == N, 'residue counting recurrence')
        C = counts[0]
        require(3*C == N+phases[n % 6], 'six-phase exact population formula')
        require((C <= N//3) == (n % 6 in (2, 3, 4)), 'constant-zero cover phase')
        population_cases += 1
        if 1 <= n <= 128:
            vals = [residue_coefficients(n, k) for k in range(n+1)]
            require(vals[0] == C, 'signed constant character')
            require(all(9*a*a <= 4*3**n for a in vals[1:]), 'complex-free spectral bound control')
            spectrum_cases += n
            best = max(abs(a) for a in vals[1:])
            balanced_corr = Fraction(N*best, 2*C*(N-C))
            balanced_error = (1-balanced_corr)/2
            if n >= 8:
                require(balanced_error > Fraction(1, 3), 'balanced MOD3 affine strict gap')
                balanced_pass += 1
            unif_corr = max(abs(N-2*C), *(2*abs(a) for a in vals[1:]))
            unif_distance = (N-unif_corr)//2
            if n <= 14:
                bits = [int(x.bit_count() % 3 == 0) for x in range(N)]
                spectrum = fwht(1-2*b for b in bits)
                for mask, w in enumerate(spectrum):
                    expected = N-2*C if mask == 0 else -2*vals[mask.bit_count()]
                    require(w == expected, 'actual-cube/signed-residue spectrum')
            if 7 <= n <= 20:
                examples.append(dict(n=n, ones=C, radius=N//3,
                                     nearest_affine_distance=unif_distance,
                                     uniform_detector_accepts=unif_distance > N//3,
                                     balanced_best_error=str(balanced_error)))
        counts = (counts[0]+counts[2], counts[1]+counts[0], counts[2]+counts[1])
    return dict(population_cases=population_cases, signed_character_cases=spectrum_cases,
                balanced_gap_cases=balanced_pass, explicit_cube_checked_through_n=14,
                examples=examples)


def easy_far_checks():
    out = []
    for n in range(4, 17):
        m, N = n//2, 1 << n
        f = [sum(((x >> (2*j)) & 1)*((x >> (2*j+1)) & 1)
                 for j in range(m)) % 2 for x in range(N)]
        spectrum = fwht(1-2*b for b in f)
        maximum = 1 << (n-m)
        require(max(map(abs, spectrum)) == maximum, 'pair-product Walsh maximum')
        require(all(w == 0 or abs(w) == maximum for w in spectrum), 'pair-product spectrum')
        dist = (N-maximum)//2
        require(3*dist > N, 'easy quadratic lies in affine-far property')
        out.append(dict(n=n, quadratic_monomials=m, max_walsh=maximum,
                        nearest_affine_distance=dist, radius=N//3))
    return out


def nonvacuity():
    out = []
    for d in range(5):
        first = None
        checked = 0
        for n in range(max(1, d), 13):
            N = 1 << n
            M = sum(comb(n, j) for j in range(d+1))
            V = sum(comb(N, j) for j in range(N//3+1))
            if (1 << M)*V < 1 << (N-1) and first is None:
                first = n
            checked += 1
        out.append(dict(degree=d, first_tested_half_density_n=first, cases=checked,
                        scope='finite exact inequalities only, not extrapolation'))
    # A written all-n>=7,d<=1 consequence uses this exact base inequality.
    require(2**27 * 27**128 < 32**128, 'n7 exponential-volume base')
    return out


def main():
    # Signed and unnormalized shortcuts genuinely falsify support extraction.
    require(sum(m*v for m, v in zip((-1, 2), (3, 1))) <= 0,
            'signed mass counterexample setup')
    require(not any(m > 0 and v <= 0 for m, v in zip((-1, 2), (3, 1))),
            'signed mass false witness')
    require(1 != 2 and (1 != 0) == (2 != 0), 'nonbinary error-set collision')
    print(json.dumps(dict(status='PASS', scope='finite exact evidence; no independent semantic review',
                         reduction=reduction_checks(), affine=affine_detection(),
                         mixtures=mixture_checks(), mod3=mod3_checks(),
                         easy_far=easy_far_checks(),
                         nonvacuity=nonvacuity(),
                         counterexamples=dict(signed_mass=[[-1, 3], [2, 1]],
                                              unnormalized_zero_mass='no positive support',
                                              nonbinary='1 and 2 have same error set against 0')),
                     sort_keys=True, separators=(',', ':')))

if __name__ == '__main__':
    main()
