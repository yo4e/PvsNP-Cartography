#!/usr/bin/env python3
"""Exact finite controls, not a PCP implementation or a general/Lean proof.
Python >=3.10, standard library only. All checks survive python -O.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import product, combinations_with_replacement
from pathlib import Path
from random import Random
import hashlib
import json


def require(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError(label)


def rank(rows: tuple[int, ...]) -> int:
    pivots: dict[int, int] = {}
    for value in rows:
        while value:
            k = value.bit_length()-1
            if k in pivots:
                value ^= pivots[k]
            else:
                pivots[k] = value
                break
    return len(pivots)


def affine(rows: tuple[int, ...], bias: int, z: int) -> int:
    return sum((((mask & z).bit_count() & 1) ^ ((bias >> j) & 1)) << j
               for j, mask in enumerate(rows))


def projection_controls() -> dict:
    maps = error_sets = 0
    for r in range(4):
        for m in range(4):
            for rows in product(range(1 << r), repeat=m):
                d = rank(rows)
                for bias in range(1 << m):
                    hist = Counter(affine(rows, bias, z) for z in range(1 << r))
                    require(len(hist) == 1 << d, 'image size versus independently computed rank')
                    require(set(hist.values()) == {1 << (r-d)}, 'fiber size')
                    density = F((1 << m)*max(hist.values()), 1 << r)
                    require(density == F(2)**(m-d), 'joint density')
                    for e in range(1 << (1 << m)):
                        hit = F(sum(v for x, v in hist.items() if e >> x & 1), 1 << r)
                        require(hit <= density*F(e.bit_count(), 1 << m), 'error pullback')
                        error_sets += 1
                    maps += 1
    return dict(affine_maps=maps, error_sets=error_sets,
                scope='all affine maps with 0<=input/output bits<=3, all output error sets')


def accepts(row: int, clause: tuple[tuple[int, int], ...]) -> bool:
    return any(((row >> x) & 1) ^ sign for x, sign in clause)


def constants(n: int, target: int, clauses, weights) -> tuple[F, F]:
    require(n > 0 and len(clauses) == len(weights), 'shape')
    total = sum(weights)
    require(total > 0 and all(w >= 0 for w in weights), 'weights')
    true_sets = []
    for clause in clauses:
        require(1 <= len(clause) <= 3 and all(0 <= x < n and sign in (0, 1)
                    for x, sign in clause), 'clause')
        a = sum(1 << x for x in set(x for x, s in clause if ((target >> x) & 1) ^ s))
        require(a != 0, 'target satisfies every clause')
        true_sets.append(a)
    capacity = actual = F(0)
    for e in range(1, 1 << n):
        forced = sum(w for a, w in zip(true_sets, weights) if a & e == a)
        failure = sum(w for c, w in zip(clauses, weights) if not accepts(target ^ e, c))
        capacity = max(capacity, F(n*forced, total*e.bit_count()))
        actual = max(actual, F(n*failure, total*e.bit_count()))
    require(actual <= capacity, 'signed constant/certificate')
    return capacity, actual


def lift(n: int, target: int, clauses, weights, permutations):
    require(all(sorted(p) == list(range(n)) for p in permutations), 'permutations')
    out_target = sum(((target >> x) & 1) << (s*n+p[x])
                     for s, p in enumerate(permutations) for x in range(n))
    out_clauses = tuple(tuple((s*n+p[x], sign) for x, sign in c)
                        for s, p in enumerate(permutations) for c in clauses)
    return n*len(permutations), out_target, out_clauses, tuple(weights)*len(permutations)


def best_acceptance(n: int, clauses, weights) -> F:
    return max(F(sum(w for c, w in zip(clauses, weights) if accepts(row, c)), sum(weights))
               for row in range(1 << n))


def copy_controls() -> dict:
    cases = soundness = 0
    pool = tuple(combinations_with_replacement(tuple(product(range(2), range(2))), 3))
    for target in range(4):
        valid = tuple(c for c in pool if accepts(target, c))
        for clauses in combinations_with_replacement(valid, 2):
            for weights in ((1, 1), (1, 2), (0, 1)):
                original = constants(2, target, clauses, weights)
                args = lift(2, target, clauses, weights, ((0, 1), (1, 0)))
                require(constants(*args) == original, 'copy invariance of BOTH constants')
                cases += 1
    rng = Random(20261110)
    for _ in range(80):
        n, target = 4, rng.randrange(16)
        clauses = []
        while len(clauses) < 3:
            c = tuple((rng.randrange(n), rng.randrange(2)) for _ in range(3))
            if accepts(target, c):
                clauses.append(c)
        weights = (1, rng.randrange(3), rng.randrange(3))
        perm = list(range(n))
        rng.shuffle(perm)
        args = lift(n, target, clauses, weights, (tuple(range(n)), tuple(perm)))
        require(constants(*args) == constants(n, target, clauses, weights), 'seeded copies')
        cases += 1
    # Universal soundness is tested on arbitrary, including unsatisfiable, families.
    for clauses in combinations_with_replacement(pool, 2):
        weights = (1, 2)
        _, _, copies, w = lift(2, 0, clauses, weights, ((0, 1), (1, 0)))
        require(best_acceptance(4, copies, w) == best_acceptance(2, clauses, weights),
                'all-global-proof soundness preserved')
        soundness += 1
    c = (((0, 1),)*3, ((1, 0),)*3)  # honest proof [0,1]
    untagged = tuple(tuple((x ^ s, sign) for x, sign in clause)
                     for s in (0, 1) for clause in c)
    require(best_acceptance(2, c, (1, 1)) == 1, 'original perfect completeness')
    require(best_acceptance(2, untagged, (1,)*4) == F(1, 2), 'untagged completeness loss')
    return dict(capacity_and_actual_invariance=cases, universal_soundness_cases=soundness,
                untagged_counterexample=dict(original='1', after_shifting='1/2'), seed=20261110)


def poly_mul(p: set[int], q: set[int]) -> set[int]:
    out: set[int] = set()
    for u in p:
        for v in q:
            mask = u | v
            if mask in out:
                out.remove(mask)
            else:
                out.add(mask)
    return out


def poly_value(p: set[int], z: int) -> int:
    return sum(z & m == m for m in p) & 1


def concentration_controls() -> dict:
    rows = []
    for m in range(1, 6):
        for k in range(1, m+1):
            # Variables y_0..y_(m-1), s_0..s_(m-1); disjoint factors so ordinary
            # expansion is already squarefree, not merely a quotient-degree check.
            p = {0}
            for j in range(k):
                p = poly_mul(p, {0, 1 << j, 1 << (m+j)})
            p ^= {0}
            require(max(map(int.bit_count, p)) == k, 'actual polynomial degree')
            errors = sum(poly_value(p, v) != 1 for v in range(1 << (2*m)))
            hist, marginal = Counter(), Counter()
            failures = 0
            for z in range(1 << m):
                q = z & ~((1 << k)-1)
                for s in range(1 << m):
                    y = q ^ s
                    v = y | (s << m)
                    hist[v] += 1
                    marginal[y] += 1
                    failures += poly_value(p, v) != 1
            require(F(errors, 1 << (2*m)) == F(1, 1 << k), 'uniform joint error')
            require(failures == 1 << (2*m), 'every queried copy is wrong')
            require(len(set(marginal.values())) == 1 and len(marginal) == 1 << m,
                    'first marginal uniform')
            require(max(hist.values()) == 1 << k, 'joint density unchanged')
            rows.append(dict(bits=m, codimension=k, degree=k, error=str(F(1, 1 << k)),
                             marginal_density=1, joint_density=1 << k, queried_failure='1'))
    return dict(families=len(rows), examples=[rows[0], rows[-1]])


def hardwiring_controls() -> dict:
    cases = 0
    for k in range(1, 10):
        # f(x,y)=[x=0], candidate constant0: average promise is lost on x=0.
        target = lambda x, y: int(x == 0)
        candidate = lambda x, y: 0
        errors = sum(target(x, y) != candidate(x, y) for x in range(1 << k) for y in range(4))
        require(F(errors, (1 << k)*4) == F(1, 1 << k), 'global joint error')
        require(all(target(0, y) != candidate(0, y) for y in range(4)), 'fixed-input error one')
        for repeats in (1, 3, 7):
            repeated = int(sum([0]*repeats) > repeats//2)
            require(repeated == 0, 'independent draws of point mass do not amplify')
        cases += 1
    # Source-style seed translations preserve every original query histogram.
    shifts = 0
    for r in range(5):
        for frozen in range(r+1):
            q = lambda z: z & ~((1 << frozen)-1)
            original = Counter(q(z) for z in range(1 << r))
            for s in range(1 << r):
                require(Counter(q(z ^ s) for z in range(1 << r)) == original,
                        'seed translation histogram')
                shifts += 1
    return dict(hardwired_input_cases=cases, seed_translations=shifts,
                constant_candidate_degree=0, fixed_input_error='1',
                amplification_scope='point-mass distribution; same wrong address survives every repetition')


def main() -> None:
    result = dict(status='PASS', scope='finite exact same-author controls; not whole-PCP execution or Lean verification',
                  projections=projection_controls(), copies=copy_controls(),
                  concentration=concentration_controls(), hardwiring=hardwiring_controls(),
                  self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
