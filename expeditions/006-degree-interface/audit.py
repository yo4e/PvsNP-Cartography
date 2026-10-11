#!/usr/bin/env python3
"""Exact finite semantic controls for the new degree interface (stdlib only).

This does not prove the generic normal-form theorem or validate Lean syntax.
The pinned Lean workflow separately checks those proof terms and their axioms.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

N = 5
CUBE = tuple(product((0, 1), repeat=N))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def target(x: tuple[int, ...]) -> int:
    return int(sum(x) % 3 == 0)


def tuple_affine(c: int, a: tuple[int, ...], x: tuple[int, ...]) -> int:
    return (c + sum(ai * xi for ai, xi in zip(a, x))) % 2


def mobius_coefficients(table: list[int]) -> list[int]:
    """Recover the Boolean algebraic normal form, by subset inversion over GF(2)."""
    require(len(table) == 1 << N, 'truth-table size mismatch')
    coeff = table.copy()
    for bit in range(N):
        for mask in range(1 << N):
            if mask & (1 << bit):
                coeff[mask] ^= coeff[mask ^ (1 << bit)]
    return coeff


def evaluate_anf(coeff: list[int], x: int) -> int:
    return sum(c for monomial, c in enumerate(coeff) if monomial & x == monomial) % 2


def main() -> None:
    # All canonical affine truth tables, with a second reconstruction algorithm.
    rows = tuple((c, a) for c in (0, 1) for a in product((0, 1), repeat=N))
    truth_tables: set[tuple[int, ...]] = set()
    for c, a in rows:
        table = [tuple_affine(c, a, tuple(mask >> i & 1 for i in range(N)))
                 for mask in range(1 << N)]
        recovered = mobius_coefficients(table)
        require(recovered[0] == c, 'lost constant term')
        require(tuple(recovered[1 << i] for i in range(N)) == a,
                'lost linear coefficient')
        require(all(v == 0 for m, v in enumerate(recovered) if m.bit_count() > 1),
                'affine row acquired higher-degree monomial')
        require([evaluate_anf(recovered, x) for x in range(1 << N)] == table,
                'recovered coefficients do not evaluate to original table')
        truth_tables.add(tuple(table))
    require(len(rows) == len(truth_tables) == 64, 'affine collision or coverage failure')
    print('PASS: 64 affine coefficient rows; Mobius reconstruction and 2048 evaluations agree')

    # Deliberately remove the degree premise: x0*x1 cannot be reconstructed by
    # keeping only its constant and linear coefficients. Even checking 0 and
    # the five basis vectors would miss the error.
    quadratic = [(mask & 1) * ((mask >> 1) & 1) for mask in range(1 << N)]
    qcoeff = mobius_coefficients(quadratic)
    require(qcoeff[3] == 1 and sum(qcoeff) == 1, 'quadratic countermodel corrupted')
    truncated = [v if m.bit_count() <= 1 else 0 for m, v in enumerate(qcoeff)]
    sparse_inputs = (0,) + tuple(1 << i for i in range(N))
    require(all(evaluate_anf(truncated, x) == quadratic[x] for x in sparse_inputs),
            'sparse-test negative control malformed')
    require(evaluate_anf(truncated, 3) == 0 and quadratic[3] == 1,
            'missing-degree-premise counterexample not detected')
    print('REJECT: omit degree bound; x0*x1 passes zero/basis tests but fails at input mask 3')

    # The wrong quantifiers allow a different constant for each input.
    inputwise_constants = tuple(target(x) for x in CUBE)
    require(all(c == target(x) for x, c in zip(CUBE, inputwise_constants)),
            'input-dependent constant construction failed')
    require(set(inputwise_constants) == {0, 1}, 'target accidentally became constant')
    # In the correct quantifiers a fixed mixture on constants 0,1 has
    # success p at x=0, and 1-p at x=e0. The exact dual q gives each half
    # the mass, so BOTH deterministic constants have q-success 1/2.
    x0 = (0,) * N
    e0 = (1,) + (0,) * (N-1)
    dual_rows = [Q(int(c == target(x0)) + int(c == target(e0)), 2) for c in (0, 1)]
    require(dual_rows == [Q(1, 2), Q(1, 2)], 'constant-class dual mismatch')
    require(max(dual_rows) < Q(2, 3), 'dual gap missing')
    # The argument for ALL real mixtures is algebraic, not a grid search:
    # p*(1/2)+(1-p)*(1/2)=1/2. No discretization of probability is used.
    print('REJECT: swapped input/family quantifiers; input-dependent constants achieve 1')
    print('PASS: fixed constant class has exact two-input dual maximum 1/2 < 2/3')
    print('PASS: finite semantic controls; generic proof and degree equality require Lean CI')


if __name__ == '__main__':
    main()
