#!/usr/bin/env python3
"""Bounded actual-GF2-ANF controls for full-XOR-copy invariance at fixed degree.
Same author as the written argument; not independent or Lean verification.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from random import Random
import hashlib
import json
import verify_smoothing as base


def polynomial_tables(bits: int, degree: int) -> list[int]:
    rows = [0]
    for mask in range(1 << bits):
        if mask.bit_count() <= degree:
            monomial = sum(int(x & mask == mask) << x for x in range(1 << bits))
            rows += [row ^ monomial for row in rows]
    base.require(len(set(rows)) == len(rows), 'ANF basis independence')
    return rows


def scores(target: int, n: int, clauses, weights, rows: list[int]):
    total = sum(weights)
    best_ratio, min_error = F(0), F(1)
    patterns = [(sum(1 << x for x in {x for x, s in c if not s}),
                 sum(1 << x for x in {x for x, s in c if s})) for c in clauses]
    for row in rows:
        err = (row ^ target).bit_count()
        fail = sum(w for (pos, neg), w in zip(patterns, weights)
                   if row & pos == 0 and row & neg == neg)
        base.require(bool(err) or not fail, 'correct proof rejected')
        min_error = min(min_error, F(err, n))
        if err:
            best_ratio = max(best_ratio, F(n*fail, total*err))
    return best_ratio, min_error


def main() -> None:
    expected = 'c994160443a1dbe828daa830772f61e3043a84587c07584f3ebc3b9522065e3a'
    base.require(hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest() == expected,
                 'unchanged prerequisite')
    rng = Random(20261110)
    cases = comparisons = slice_checks = lifted_witnesses = 0
    for bits in (1, 2):
        n = 1 << bits
        for target in range(1 << n):
            clauses = []
            while len(clauses) < 3:
                c = tuple((rng.randrange(n), rng.randrange(2)) for _ in range(3))
                if base.accepts(target, c):
                    clauses.append(c)
            weights = (1, 2, 3)
            args = base.lift(n, target, clauses, weights,
                             tuple(tuple(x ^ s for x in range(n)) for s in range(n)))
            for degree in range(bits+1):
                original = polynomial_tables(bits, degree)
                copied = polynomial_tables(2*bits, degree)
                small_set, large_set = set(original), set(copied)
                for row in copied:
                    for s in range(n):
                        section = sum(((row >> (s*n+(x ^ s))) & 1) << x for x in range(n))
                        base.require(section in small_set, 'degree retained by affine slice')
                        slice_checks += 1
                for row in original:
                    lifted = sum(((row >> (y ^ s)) & 1) << (s*n+y)
                                 for s in range(n) for y in range(n))
                    base.require(lifted in large_set, 'degree retained by joint XOR lift')
                    lifted_witnesses += 1
                before = scores(target, n, clauses, weights, original)
                after = scores(args[1], args[0], args[2], args[3], copied)
                base.require(before == after, 'fixed-degree loss AND minimum distance invariant')
                comparisons += len(original)+len(copied)
                cases += 1
    out = dict(status='PASS', scope='all truth-table targets on 1/2 address bits; one seeded satisfied family each; all ANFs up to degrees1/2 respectively',
               family_degree_cases=cases, polynomial_score_evaluations=comparisons,
               affine_slice_memberships=slice_checks, joint_lift_memberships=lifted_witnesses,
               seed=20261110, prerequisite_sha256=expected,
               self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
