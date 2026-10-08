#!/usr/bin/env python3
"""Expedition 003: exact attack on a *sample-restricted* n=8 dual.

Default check needs only Python stdlib. For the deterministic 10,016-row
random/structured candidate pool also install numpy==2.3.5 and run --pool.
The pool is a subset of the quadratic model; no result here determines n=8
probabilistic degree or establishes a universal lower bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import combinations
from math import comb

N = 8
SIZES = tuple(comb(N, w) for w in range(N + 1))
PAIRS = tuple(combinations(range(N), 2))  # bit 0 is pair (0,1)
DUAL_NUM = (207, 1983, 6550, 4969, 3150, 1085, 3482, 1901, 125)
DUAL_DEN = 23452
T = F(569, 902)

# (orbit weight, constant, linear_mask, quadratic_mask, expected good counts).
# The weights achieve T on *all* nine layers, using representatives in the
# deterministic finite sampling pool described by the --pool test.
PRIMAL = (
    (F(293, 10824), 0, 255, 0, (0, 0, 28, 56, 70, 0, 0, 0, 1)),
    (F(29, 451), 0, 127, 0, (0, 1, 21, 35, 35, 35, 21, 7, 0)),
    (F(851, 5412), 0, 0, 268435455, (0, 8, 0, 56, 70, 56, 28, 0, 1)),
    (F(35, 451), 0, 0, 167875084, (0, 8, 20, 34, 34, 28, 12, 6, 1)),
    (F(155, 3608), 0, 0, 0, (0, 8, 28, 0, 70, 56, 0, 8, 1)),
    (F(35, 902), 1, 9, 121753088, (1, 2, 22, 38, 44, 22, 14, 6, 0)),
    (F(147, 451), 1, 162, 248984699, (1, 3, 19, 31, 43, 29, 19, 7, 1)),
    (F(7, 33), 1, 246, 197300836, (1, 6, 20, 26, 36, 30, 20, 6, 0)),
    (F(73, 1353), 1, 255, 268435455, (1, 8, 28, 56, 0, 56, 0, 0, 0)),
)

# A separate polynomial, absent from the 10,016 sampled candidates.
# It defeats the tempting (INVALID) extension of the dual to ALL quadratics.
REFUTER = (1, 255, 60548413, (1, 8, 17, 34, 39, 28, 21, 6, 1))


def layer_good_counts(c: int, a: int, b: int) -> tuple[int, ...]:
    assert c in (0, 1) and 0 <= a < 2**N and 0 <= b < 2**len(PAIRS)
    counts = [0] * (N + 1)
    for x in range(1 << N):
        p = c ^ ((a & x).bit_count() & 1)
        for j, (i, k) in enumerate(PAIRS):
            p ^= ((b >> j) & 1) & ((x >> i) & 1) & ((x >> k) & 1)
        if p == int(x.bit_count() % 3 == 0):
            counts[x.bit_count()] += 1
    return tuple(counts)


def dual_average(counts: tuple[int, ...]) -> F:
    return sum((F(DUAL_NUM[w], DUAL_DEN) * F(counts[w], SIZES[w])
                for w in range(N + 1)), F(0))


def verify_explicit() -> None:
    assert sum(DUAL_NUM) == DUAL_DEN
    assert all(x > 0 for x in DUAL_NUM)
    assert sum(wt for wt, *_ in PRIMAL) == 1
    for wt, c, a, b, expected in PRIMAL:
        assert wt > 0
        assert layer_good_counts(c, a, b) == expected, (c, a, b)
        assert dual_average(expected) == T, (c, a, b)
    for layer in range(N + 1):
        actual = sum((wt * F(cnt[layer], SIZES[layer])
                      for wt, _, _, _, cnt in PRIMAL), F(0))
        assert actual == T, (layer, actual, T)
    c, a, b, expected = REFUTER
    assert layer_good_counts(c, a, b) == expected
    value = dual_average(expected)
    assert value == F(27376, 41041)
    assert value > F(2, 3), value
    print('EXACT: 9-orbit sampled primal and dual agree at 569/902')
    print('EXACT: separate quadratic refutes a global use of that dual;')
    print(f'  c={c}, linear_mask={a}, quadratic_mask={b}, q-success={value}, excess={value-F(2, 3)}')
    print('PASS: n=8 model remains unresolved; counterexample is to the proposed q, NOT to degree <=2')


def verify_sampled_pool(optimize: bool = False) -> None:
    import numpy as np  # optional, pin 2.3.5 to reproduce the candidate pool

    x = np.arange(1 << N, dtype=np.uint64)
    degree = 1 + N + len(PAIRS)
    monoms = np.array([np.ones_like(x)] + [(x >> i) & 1 for i in range(N)]
                      + [((x >> i) & 1) * ((x >> j) & 1) for i, j in PAIRS],
                      dtype=np.uint8).T
    weights = np.array([int(y).bit_count() for y in x])
    target = (weights % 3 == 0).astype(np.uint8)
    random_rows = np.random.default_rng(20261008).integers(
        0, 2, size=(10000, degree), dtype=np.uint8)
    special = [np.zeros(degree, dtype=np.uint8) for _ in range(2)]
    special[1][0] = 1
    for coords in (range(1, 1 + N), range(1 + N, degree), range(1, degree)):
        for c in (0, 1):
            v = np.zeros(degree, dtype=np.uint8)
            v[list(coords)] = 1
            v[0] = c
            special.append(v)
    # Historical n=7 orbit representatives lifted by ignoring x_7.
    old_pairs = tuple(combinations(range(7), 2))
    for c, a, b in ((0, 0, 0), (0, 0, (1 << 21) - 1),
                    (0, 127, 0), (1, 127, (1 << 21) - 1),
                    (1, 71, 1887847), (1, 8, 1802215),
                    (1, 11, 1855511), (1, 119, 1980222)):
        v = np.zeros(degree, dtype=np.uint8)
        v[0] = c
        for i in range(7):
            v[1 + i] = (a >> i) & 1
        for i, pair in enumerate(old_pairs):
            v[1 + N + PAIRS.index(pair)] = (b >> i) & 1
        special.append(v)
    candidates = np.vstack([np.array(special), random_rows])
    assert candidates.shape == (10016, degree)
    successes = ((candidates.astype(np.int16) @ monoms.T.astype(np.int16)) & 1) == target
    all_counts = np.column_stack([successes[:, weights == w].sum(axis=1)
                                  for w in range(N + 1)])
    uniq, indices = np.unique(all_counts, axis=0, return_index=True)
    assert len(uniq) == 6407, len(uniq)
    # Integral, exact check of dual constraint for ALL sampled candidates.
    # lcm(C(8,w))=280; T*(DUAL_DEN*280)=569*7280 exactly.
    factors = np.array([DUAL_NUM[w] * (280 // SIZES[w])
                        for w in range(N + 1)], dtype=np.int64)
    scaled = uniq.astype(np.int64) @ factors
    assert int(scaled.max()) == 569 * 7280, int(scaled.max())
    assert np.all(scaled <= 569 * 7280)
    # Ensure the 9 rational primal rows really belong to the sampled pool.
    sampled_coeff = set(map(tuple, candidates.tolist()))
    for _, c, a, b, _ in PRIMAL:
        bits = (c,) + tuple((a >> i) & 1 for i in range(N)) + tuple(
            (b >> i) & 1 for i in range(len(PAIRS)))
        assert bits in sampled_coeff, (c, a, b)
    c, a, b, _ = REFUTER
    refuter_bits = (c,) + tuple((a >> i) & 1 for i in range(N)) + tuple(
        (b >> i) & 1 for i in range(len(PAIRS)))
    assert refuter_bits not in sampled_coeff
    print('POOL: 10016 deterministic candidates, 6407 distinct layer vectors')
    print('POOL: exact dual bound matches 569/902; primal support belongs to pool')
    if optimize:
        from scipy.optimize import linprog
        success = uniq / np.asarray(SIZES)[None, :]
        m = len(uniq)
        r = linprog(np.r_[np.zeros(m), -1.],
                    A_ub=np.column_stack([-success.T, np.ones(N + 1)]),
                    b_ub=np.zeros(N + 1),
                    A_eq=np.r_[np.ones(m), 0][None, :], b_eq=[1],
                    bounds=[(0, None)] * m + [(0, 1)], method='highs')
        assert r.success and abs(-r.fun - float(T)) < 1e-9
        print(f'NUMERIC REPLICATION: scipy LP optimum approx {-r.fun:.12f}')
    print('PASS: sampled-subset optimum is exact; the whole quadratic class is NOT exhausted')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pool', action='store_true', help='recreate candidate pool with numpy')
    parser.add_argument('--optimize', action='store_true', help='also reproduce floating LP with scipy')
    args = parser.parse_args()
    if args.optimize:
        args.pool = True
    verify_explicit()
    if args.pool:
        verify_sampled_pool(optimize=args.optimize)


if __name__ == '__main__':
    main()
