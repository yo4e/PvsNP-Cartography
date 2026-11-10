#!/usr/bin/env python3
"""Finite corroboration of the written sharp factor-four signed-OR bound.
No general proof, independent review, or formalization is inferred from this run.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import hashlib
import json


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def controls(n, pairs, weights):
    total = sum(weights)
    require(total > 0 and all(w >= 0 for w in weights), 'weights')
    require(all(a and not a & b and (a | b).bit_count() <= 3 for a, b in pairs),
            'satisfied, non-tautological, width-three clauses')
    best, cut = F(0), 0
    for s in range(1, 1 << n):
        value = F(n * sum(w for (a, _), w in zip(pairs, weights) if a & s == a),
                  total * s.bit_count())
        if value > best:
            best, cut = value, s
    failures = []
    exact = F(0)
    for e in range(1 << n):
        # Direct evaluation of the signed literals at pi XOR error; pi=all ones.
        failed = 0
        for (a, b), w in zip(pairs, weights):
            accepted = any(not (e >> x & 1) for x in range(n) if a >> x & 1)
            accepted = accepted or any(e >> x & 1 for x in range(n) if b >> x & 1)
            failed += w * (not accepted)
        failures.append(F(failed, total))
        if e:
            exact = max(exact, F(n * failed, total * e.bit_count()))
    require(exact <= best <= 4 * exact, 'factor-four sandwich')
    subsets = [e for e in range(1 << n) if e & cut == e]
    mean_fail = sum(failures[e] for e in subsets) / len(subsets)
    mean_size = F(sum(e.bit_count() for e in subsets), len(subsets))
    forced = F(sum(w for (a, _), w in zip(pairs, weights) if a & cut == a), total)
    require(mean_fail >= forced / 8 and mean_size == F(cut.bit_count(), 2),
            'half-thinning argument')
    return best, exact


def main():
    exhaustive = seeded = 0
    for n in range(1, 4):
        pool = [(a, b) for a in range(1, 1 << n) for b in range(1 << n) if not a & b]
        for size in (1, 2):
            for pairs in product(pool, repeat=size):
                for weights in product(range(3), repeat=size):
                    if sum(weights):
                        controls(n, pairs, weights)
                        exhaustive += 1
    rng = Random(20261110)
    for n in (4, 5):
        pool = [(a, b) for a in range(1, 1 << n) for b in range(1 << n)
                if not a & b and (a | b).bit_count() <= 3]
        for _ in range(100):
            pairs = tuple(rng.choice(pool) for _ in range(4))
            weights = tuple(rng.randrange(4) for _ in range(4))
            if not sum(weights):
                weights = (1, 0, 0, 0)
            controls(n, pairs, weights)
            seeded += 1
    pairs = tuple((a, 7 ^ a) for a in range(1, 8))
    weights = tuple(a.bit_count() for a in range(1, 8))
    kappa, exact = controls(4, pairs, weights)
    require((kappa, exact) == (F(4, 3), F(1, 3)), 'sharp example')
    # Actual GF2 polynomial p(y0,y1)=y1, target constant one, error addresses0,1.
    e = sum((1 ^ ((x >> 1) & 1)) << x for x in range(4))
    fail = F(sum(w for (a, b), w in zip(pairs, weights) if a & e == a and not b & e), 12)
    require(fail == F(1, 6) and F(e.bit_count(), 4) == F(1, 2), 'linear witness')
    # The non-tautology premise is essential: v OR not-v never fails.
    require(all(any((bit, 1-bit, bit)) for bit in (0, 1)), 'tautology control')
    print(json.dumps(dict(status='PASS', scope='finite same-author controls; general bound is a separate written proof',
        exhaustive_families=exhaustive, seeded_families=seeded, seed=20261110,
        sharp_example=dict(addresses=4, true_subsets=list(range(1,8)), raw_weights=weights,
            certificate_constant=str(kappa), actual_constant=str(exact), ratio=str(kappa/exact),
            polynomial='p(y0,y1)=y1', uniform_error='1/2', failure=str(fail)),
        excluded_tautology=dict(certificate_constant='1', actual_constant='0'),
        self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
