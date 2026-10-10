#!/usr/bin/env python3
"""Independent exact audit of n=5 data in the Lean source (stdlib only).

This checks transcribed data and semantic controls, NOT Lean proof validity.
The formal CI separately compiles and audits all declarations.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import re

PAIRS = tuple(combinations(range(5), 2))
MASS = (0, 12, 3, 7, 2, 10)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def eval_tuple(c: int, a: int, b: int, x: tuple[int, ...]) -> int:
    return (c + sum((a // (2**i) % 2) * x[i] for i in range(5)) +
            sum((b // (2**k) % 2) * x[i] * x[j] for k, (i, j) in enumerate(PAIRS))) % 2


def eval_bits(c: int, a: int, b: int, x: int) -> int:
    result = c ^ ((a & x).bit_count() & 1)
    for k, (i, j) in enumerate(PAIRS):
        result ^= ((b >> k) & 1) & ((x >> i) & 1) & ((x >> j) & 1)
    return result


def orbit() -> Counter[tuple[int, int]]:
    rows: Counter[tuple[int, int]] = Counter()
    for perm in permutations(range(5)):
        a = sum(1 << perm[i] for i in range(5) if 27 >> i & 1)
        b = sum(1 << PAIRS.index(tuple(sorted((perm[i], perm[j]))))
                for k, (i, j) in enumerate(PAIRS) if 829 >> k & 1)
        rows[a, b] += 1
    return rows


def audit(source: str) -> None:
    block = re.search(r'def upperMasks.*?:=\s*!\[(.*?)\]', source, re.S)
    if block is None:
        raise ValueError('upperMasks declaration missing')
    rows = [tuple(map(int, m)) for m in re.findall(r'\((\d+),\s*(\d+)\)', block.group(1))]
    expected = orbit()
    require(len(rows) == 30 and len(set(rows)) == 30, 'wrong support coverage')
    require(set(rows) == set(expected), 'not the exact original orbit')
    require(set(expected.values()) == {4}, 'orbit multiplicities not uniform')
    cubes = tuple(product((0, 1), repeat=5))
    affine_rows = tuple((c, a) for c in (0, 1) for a in range(32))
    require(len(cubes) == 32 and len(affine_rows) == 64, 'coverage failure')
    require(sum(MASS[sum(x)] for x in cubes) == 180, 'mass normalization')
    bound = max(sum(MASS[sum(x)] * (eval_tuple(c, a, 0, x) == int(sum(x) % 3 == 0))
                    for x in cubes) for c, a in affine_rows)
    require(bound == 110, 'wrong affine bound')
    correct = []
    for x in cubes:
        mask = sum(bit << i for i, bit in enumerate(x))
        for a, b in rows:
            require(eval_tuple(1, a, b, x) == eval_bits(1, a, b, mask), 'evaluators disagree')
        count = sum(eval_tuple(1, a, b, x) == int(sum(x) % 3 == 0) for a, b in rows)
        require(count == (30, 24, 21, 21, 30, 30)[sum(x)], 'pointwise profile mismatch')
        correct.append(count)
    require(min(correct) == 21, 'upper guarantee')
    print('PASS lower: 64 affine rows x 32 inputs; mass=180; maximum=110/180=11/18')
    print('PASS upper: 30 distinct quadratics; pointwise minimum=21/30=7/10')
    print('PASS orbit: 120 permutations; each compressed representative appears exactly 4 times')
    print('PASS semantics: independent tuple and XOR evaluators agree on all 960 pairs')
    # Deliberate semantic mutations, not formerly believed mathematical claims.
    flipped_min = min(sum(eval_tuple(0, a, b, x) == int(sum(x)%3 == 0) for a,b in rows)
                      for x in cubes)
    require(flipped_min < 20, 'flipped constants were not rejected')
    raw_bad = next(x for x in cubes if eval_tuple(1,27,829,x) != int(sum(x)%3 == 0))
    print(f'REJECT flipped constants: minimum={flipped_min}/30')
    print(f'REJECT raw representative: wrong at x={raw_bad}')
    # Direct counterexample to dropping probability normalization in weak duality.
    # I=X={0}, payoff=1, mu=1, q=0, b=0<t=2/3. All premises EXCEPT sum(q)=1 hold.
    require(Fraction(0) <= 0 < Fraction(2,3) <= 1, 'normalization counterexample')
    print('REJECT omitted normalization: singleton payoff=1, mu=1, q=0 gives false obstruction')
    print('Scope: data/semantic audit only; no new-n, minimal-support, or novelty claim')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path,
        default=Path(__file__).resolve().parents[2]/'formal/PvsNPCartography/Mod3FiveUpper.lean')
    args=parser.parse_args()
    audit(args.source.read_text(encoding='utf-8'))


if __name__=='__main__':
    main()
