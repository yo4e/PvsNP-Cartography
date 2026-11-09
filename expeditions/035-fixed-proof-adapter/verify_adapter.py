#!/usr/bin/env python3
"""Exact finite attacks for the fixed-proof adapter. No general/independent proof.
Standard library, Python >=3.10. Explicit exceptions survive python -O.
The degree checker keeps ordinary exponent vectors; count construction uses a
separate integer residue-ring implementation, and the oracle reads source bits.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product, combinations_with_replacement
from math import comb, prod
from random import Random
from pathlib import Path
import hashlib
import json


def require(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError(label)


def source_value(masks: tuple[int, ...], x: int) -> int:
    return sum((x & m) == m for m in masks) % 2


def address(codes: tuple[int, ...], x: int) -> int:
    # 0/1 are constants; 2+2*j is x_j; 3+2*j is not x_j.
    return sum((code if code < 2 else ((x >> ((code-2)//2)) & 1) ^ (code & 1)) << j
               for j,code in enumerate(codes))


def mv_add(p: set[tuple], q: set[tuple]) -> set[tuple]:
    return p ^ q


def mv_mul(p: set[tuple], q: set[tuple]) -> set[tuple]:
    out: set[tuple] = set()
    for e in p:
        for f in q:
            g = tuple(a+b for a,b in zip(e,f))
            out.symmetric_difference_update((g,))
    return out


def mv_value(p: set[tuple], x: int) -> int:
    return sum(prod(((x >> j)&1)**k for j,k in enumerate(e)) for e in p) % 2


def substituted(r: int, masks: tuple[int, ...], codes: tuple[int, ...]) -> set[tuple]:
    zero = (0,)*r
    variables = []
    for c in codes:
        if c < 2:
            variables.append({zero} if c else set())
        else:
            e = tuple(int(j == (c-2)//2) for j in range(r))
            variables.append({e,zero} if c&1 else {e})
    out: set[tuple] = set()
    for mask in masks:
        term = {zero}
        for j,v in enumerate(variables):
            if mask >> j & 1:
                term = mv_mul(term,v)
        out ^= term
    return out


def constructed_clause(r: int, masks: tuple[int, ...], queries, signs) -> set[tuple]:
    one = {(0,)*r}
    term = one
    for q,s in zip(queries,signs):
        literal = substituted(r,masks,q) ^ (one if s else set())
        term = mv_mul(term, one ^ literal)
    return one ^ term


def canonical_masks(p: set[tuple]) -> tuple[int, ...]:
    out: set[int] = set()
    for e in p:
        mask = sum(int(k>0) << j for j,k in enumerate(e))
        out.symmetric_difference_update((mask,))
    return tuple(sorted(out))


def ring_mul(p: dict[int,int], q: dict[int,int], modulus: int) -> dict[int,int]:
    out: dict[int,int] = {}
    for e,c in p.items():
        for f,d in q.items():
            out[e|f] = (out.get(e|f,0)+c*d) % modulus
    return {m:c for m,c in out.items() if c}


def block_counts(r: int, b: int, masks: tuple[int, ...]) -> list[int]:
    # Integer Bernstein amplifier, not Boolean polynomial OR arithmetic.
    s, a = b+1, r-b
    modulus = 1 << s
    p = {m:1 for m in masks}
    other = {0:1}
    for m in masks:
        other[m] = (other.get(m,0)-1) % modulus
    ps, qs = [{0:1}], [{0:1}]
    for _ in range(2*s-1):
        ps.append(ring_mul(ps[-1],p,modulus))
        qs.append(ring_mul(qs[-1],other,modulus))
    amp: dict[int,int] = {}
    for j in range(s,2*s):
        for m,c in ring_mul(ps[j],qs[2*s-1-j],modulus).items():
            amp[m] = (amp.get(m,0)+comb(2*s-1,j)*c) % modulus
    table = [0]*(1 << a)
    for m,c in amp.items():
        table[m & ((1 << a)-1)] += c*(1 << (b-(m >> a).bit_count()))
    for j in range(a):
        for x in range(1 << a):
            if x >> j & 1:
                table[x] += table[x ^ (1 << j)]
    return [v % modulus for v in table]


def polynomial_checks() -> dict:
    substitutions = points = clauses = blocks = heads = degree_checks = 0
    for n in range(3):
        for r in range(3):
            for coeff in range(1 << (1 << n)):
                masks = tuple(m for m in range(1 << n) if coeff >> m & 1)
                d = max((m.bit_count() for m in masks),default=0)
                for q in product(range(2+2*r),repeat=n):
                    poly = substituted(r,masks,q)
                    require(max(map(sum,poly),default=0) <= d,'ordinary substitution degree')
                    degree_checks += 1
                    for x in range(1 << r):
                        require(mv_value(poly,x) == source_value(masks,address(q,x)), 'actual substitution')
                        points += 1
                    substitutions += 1
    rng = Random(20261109)
    for n in range(4):
        for r in range(4):
            for _ in range(12):
                masks = tuple(m for m in range(1 << n) if rng.randrange(2))
                d = max((m.bit_count() for m in masks),default=0)
                queries = [tuple(rng.randrange(2+2*r) for _ in range(n)) for _ in range(3)]
                for signs in product(range(2),repeat=3):
                    poly = constructed_clause(r,masks,queries,signs)
                    require(max(map(sum,poly),default=0) <= 3*d, 'actual unreduced OR degree')
                    degree_checks += 1
                    expected = [int(any(source_value(masks,address(q,x)) ^ s
                                        for q,s in zip(queries,signs))) for x in range(1 << r)]
                    require([mv_value(poly,x) for x in range(1 << r)] == expected,'signed clause fidelity')
                    points += 1 << r
                    for b in range(r+1):
                        got = block_counts(r,b,canonical_masks(poly))
                        brute = [sum(expected[x | (y << (r-b))] for y in range(1 << b))
                                 for x in range(1 << (r-b))]
                        require(got == brute,'folded residue versus original proof bits')
                        require(sum(got) == sum(expected),'total count over all heads')
                        blocks += 1
                        heads += len(got)
                    clauses += 1
    return dict(exhaustive_substitutions=substitutions,pointwise_comparisons=points,
                ordinary_degree_checks=degree_checks,seeded_signed_clauses=clauses,
                block_cases=blocks,exact_head_counts=heads,seed=20261109)


def accepts(row: int, queries, signs) -> int:
    return int(any(((row >> a)&1) ^ s for a,s in zip(queries,signs)))


def mixture_checks() -> dict:
    clauses = list(product(product(range(2),repeat=3),product(range(2),repeat=3)))
    mixtures = local = weighted = positive = 0
    for target in range(4):
        valid = [c for c in clauses if accepts(target,*c)]
        for rows in combinations_with_replacement(range(4),3):
            for w0 in range(5):
                for w1 in range(5-w0):
                    mu = tuple(F(w,4) for w in (w0,w1,4-w0-w1))
                    epsilon = max(sum(mu[i] for i,row in enumerate(rows)
                                      if ((row >> a)&1) != ((target >> a)&1)) for a in range(2))
                    outcomes = [[accepts(row,*c) for row in rows] for c in valid]
                    for values in outcomes:
                        require(sum(w*(1-v) for w,v in zip(mu,values)) <= epsilon,'sharp clause error')
                        local += 1
                    for mode in range(3):
                        weights = [1 if mode==0 else (j%5 if mode==1 else int(j==0))
                                   for j in range(len(valid))]
                        total = sum(weights)
                        scores = [sum(F(w,total)*v[i] for w,v in zip(weights,outcomes)) for i in range(3)]
                        require(sum(w*v for w,v in zip(mu,scores)) >= 1-epsilon,'weighted transfer')
                        witnesses = [i for i in range(3) if mu[i]>0 and scores[i]>=1-epsilon]
                        require(bool(witnesses),'positive-mass single witness')
                        weighted += 1
                        positive += len(witnesses)
                    mixtures += 1
    return dict(mixtures=mixtures,sharp_clause_checks=local,
                normalized_test_distributions=weighted,positive_witnesses=positive,
                scope='rational denominator-4 mixtures; all rows on two addresses; zero masses included')


def threshold_checks() -> dict:
    checks = equality = 0
    for clauses in range(1,6):
        for a in range(5):
            for b in range(5):
                N = clauses*(1 << (a+b))
                for C in sorted({0,1,N//2,max(0,N-1),N}):
                    for v in range(1,8):
                        for u in range(v+2):
                            require((F(u,v) <= F(C,N)) == (u*N <= v*C),'integer threshold')
                            checks += 1
                            equality += u*N == v*C
    # This pins why a nonempty test set and a positive denominator appear.
    require(1*0 <= 1*0 and not F(1,1) <= 0,'empty-domain mutation')
    require(0 <= F(1,2) and not 1*2 <= 0*1,'zero-denominator totalization mutation')
    return dict(comparisons=checks,equality_boundaries=equality,
                empty_tests_integer_test=True,empty_tests_real_test=False,
                zero_denominator_integer_test=False,zero_denominator_totalized_real_test=True)


def attacks() -> dict:
    target,rows = 3,(1,2,0)
    signed = (F(1),F(1),F(-1))
    success = [sum(w for w,row in zip(signed,rows) if (row>>a)&1) for a in range(2)]
    scores = [F(row.bit_count(),2) for row in rows]
    require(success == [1,1] and scores[:2] == [F(1,2)]*2,'signed measure countermodel')
    unnormalized = [sum(int((row>>a)&1) for row in rows[:2]) for a in range(2)]
    require(unnormalized == [1,1] and max(scores[:2]) < 1,'normalization countermodel')
    # Three actual degree-2 GF2 polynomials, each wrong at one distinct two-bit address.
    and_rows = (0b1110,0b1101,0b1011)
    point_errors = [sum(F(1,3) for row in and_rows if not ((row>>a)&1)) for a in range(4)]
    and_success = sum(F(1,3) for row in and_rows if all((row>>a)&1 for a in (0,1,2)))
    require(max(point_errors)==F(1,3) and and_success==0,'OR-to-AND mutation')
    global_scores = [F(accepts(row,(0,0,0),(0,0,0))+accepts(row,(0,0,0),(1,1,1)),2)
                     for row in (0,1)]
    resampled = F(sum(any(bits) for bits in product(range(2),repeat=3)),8)
    require(global_scores == [F(1,2)]*2 and resampled==F(7,8),'independent resampling mutation')
    return dict(signed_weights=[str(x) for x in signed],pointwise_success=[str(x) for x in success],
                positive_row_acceptance=[str(x) for x in scores[:2]],unnormalized_total_mass=2,
                and_mutation=dict(pointwise_error='1/3',clause_failure='1'),
                fixed_proof_acceptance='1/2',independent_occurrences_acceptance=str(resampled))


def main() -> None:
    out=dict(status='PASS',scope='finite exact same-author controls; not arbitrary-real proof or Lean execution',
             polynomials=polynomial_checks(),mixtures=mixture_checks(),thresholds=threshold_checks(),
             countermodels=attacks(),self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
