#!/usr/bin/env python3
"""Exact independent checker for Expedition 002; Python standard library only.

Verifies pdeg_{1/3}^{GF(2)}(MOD_3^n) = 2 at n=5,6,7. The lower
certificate exhausts affine polynomials; the upper certificate evaluates
specified quadratic representatives and rational permutation-orbit mixtures.
No LP, float arithmetic, randomness, or non-standard packages are used.

Run: python3 expeditions/002-exact-probabilistic-degree-mod3/verify_certificates.py
Optional independent pointwise audit: append --permutation-audit.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb, factorial


@dataclass(frozen=True)
class Orbit:
    weight: Q
    constant: int
    linear: int
    quadratic: int
    expected_good: tuple[int, ...]


# Independently transcribed from certificates.md. A mismatch with any
# expected-good row is a failing test, not an adjusted numerical fit.
CASES = {
    5: (
        (Q(0), Q(1, 3), Q(1, 6), Q(7, 18), Q(1, 18), Q(1, 18)),
        (Orbit(Q(1), 1, 27, 829, (1, 4, 7, 7, 5, 1)),),
        Q(11, 18), Q(7, 10),
    ),
    6: (
        (Q(0), Q(11, 36), Q(0), Q(7, 18), Q(2, 9), Q(1, 12), Q(0)),
        (Orbit(Q(1), 1, 59, 31421, (1, 5, 10, 14, 10, 5, 1)),),
        Q(11, 18), Q(2, 3),
    ),
    7: (
        (Q(0), Q(2, 15), Q(1, 10), Q(13, 30), Q(1, 30), Q(3, 10), Q(0), Q(0)),
        (
            Orbit(Q(1851, 15922), 0, 0, 0, (0, 7, 21, 0, 35, 21, 0, 1)),
            Orbit(Q(2291, 15922), 0, 0, 2097151, (0, 7, 0, 35, 35, 21, 7, 0)),
            Orbit(Q(955, 15922), 0, 127, 0, (0, 0, 21, 35, 35, 0, 0, 0)),
            Orbit(Q(885, 15922), 1, 127, 2097151, (1, 7, 21, 35, 0, 21, 0, 0)),
            Orbit(Q(4487, 7961), 1, 71, 1887847, (1, 4, 15, 24, 20, 12, 6, 1)),
            Orbit(Q(7, 838), 1, 8, 1802215, (1, 1, 13, 21, 26, 17, 6, 0)),
            Orbit(Q(147, 15922), 1, 11, 1855511, (1, 3, 17, 21, 26, 15, 2, 0)),
            Orbit(Q(343, 7961), 1, 119, 1980222, (1, 6, 16, 19, 20, 14, 7, 0)),
        ),
        Q(17, 30), Q(10825, 15922),
    ),
}


def target(x: int) -> int:
    return int(x.bit_count() % 3 == 0)


def quadratic_values(n: int, orbit: Orbit) -> tuple[int, ...]:
    pairs = tuple(combinations(range(n), 2))
    assert orbit.constant in (0, 1)
    assert 0 <= orbit.linear < 2**n
    assert 0 <= orbit.quadratic < 2**len(pairs)
    values = []
    for x in range(1 << n):
        p = orbit.constant ^ ((orbit.linear & x).bit_count() % 2)
        for j, (a, b) in enumerate(pairs):
            if (orbit.quadratic >> j) & 1 and (x >> a) & 1 and (x >> b) & 1:
                p ^= 1
        values.append(p)
    return tuple(values)


def verify(n: int, permutation_audit: bool = False) -> None:
    layer_q, orbits, expected_lower, expected_upper = CASES[n]
    assert len(layer_q) == n + 1 and all(q >= 0 for q in layer_q)
    assert sum(layer_q) == 1
    assert all(o.weight >= 0 for o in orbits) and sum(o.weight for o in orbits) == 1
    sizes = tuple(comb(n, w) for w in range(n + 1))
    layer_inputs = tuple(tuple(x for x in range(1 << n) if x.bit_count() == w)
                         for w in range(n + 1))
    assert tuple(map(len, layer_inputs)) == sizes

    # Lower: direct exhaustive enumeration of every affine polynomial c + a.x.
    maxima = []
    for c in (0, 1):
        for linear in range(1 << n):
            correct = tuple(sum((c ^ ((linear & x).bit_count() & 1)) == target(x)
                                for x in xs) for xs in layer_inputs)
            mean = sum((layer_q[w] * Q(correct[w], sizes[w])
                        for w in range(n + 1)), Q(0))
            maxima.append(mean)
    affine_max = max(maxima)
    assert affine_max == expected_lower, (n, affine_max, expected_lower)
    assert affine_max < Q(2, 3), (n, affine_max)

    # Upper: every orbit representative is evaluated on the entire cube.
    values = []
    for orbit in orbits:
        vals = quadratic_values(n, orbit)
        actual = tuple(sum(vals[x] == target(x) for x in xs)
                       for xs in layer_inputs)
        assert actual == orbit.expected_good, (n, orbit, actual)
        values.append(vals)

    layer_success = tuple(sum((o.weight * Q(o.expected_good[w], sizes[w])
                               for o in orbits), Q(0)) for w in range(n + 1))
    upper_min = min(layer_success)
    assert upper_min == expected_upper, (n, upper_min, expected_upper)
    assert upper_min >= Q(2, 3), (n, upper_min)

    if permutation_audit:
        # Different calculation: enumerate all n! variable permutations at
        # EACH of the 2^n fixed Boolean inputs, not merely one per layer.
        variable_perms = tuple(permutations(range(n)))
        assert len(variable_perms) == factorial(n)
        for x in range(1 << n):
            active = tuple(i for i in range(n) if (x >> i) & 1)
            images = tuple(sum(1 << perm[i] for i in active)
                           for perm in variable_perms)
            point_success = sum((o.weight * Q(sum(vals[y] == target(x) for y in images),
                                                len(images))
                                 for o, vals in zip(orbits, values)), Q(0))
            assert point_success == layer_success[x.bit_count()], (
                n, x, point_success, layer_success[x.bit_count()])
            assert point_success >= Q(2, 3), (n, x, point_success)

    print(f'n={n}: {2**(n+1)} affine polynomials; lower max={affine_max}; '
          f'upper min={upper_min}; {len(orbits)} orbits; '
          f'pointwise permutation audit={"PASS" if permutation_audit else "skipped"}')


def negative_control() -> None:
    # Flipping c in the n=5 witness must destroy its >=2/3 upper certificate.
    n = 5
    original = CASES[n][1][0]
    flipped = Orbit(original.weight, 1 - original.constant,
                    original.linear, original.quadratic, ())
    vals = quadratic_values(n, flipped)
    sizes = [comb(n, w) for w in range(n + 1)]
    min_success = min(Q(sum(vals[x] == target(x) for x in range(1 << n)
                            if x.bit_count() == w), sizes[w])
                      for w in range(n + 1))
    assert min_success < Q(2, 3), min_success
    print(f'negative control (n=5 constant flipped): rejected, minimum={min_success}')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--permutation-audit', action='store_true',
                        help='also check every permutation at every point (slower)')
    args = parser.parse_args()
    for n in sorted(CASES):
        verify(n, permutation_audit=args.permutation_audit)
    negative_control()
    print('PASS: exact finite certificate checks completed; no asymptotic claim')


if __name__ == '__main__':
    main()
