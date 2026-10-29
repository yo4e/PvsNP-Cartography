#!/usr/bin/env python3
"""Exact finite adversarial controls. No assertion is disabled by python -O.

Unreduced sparse GF(2) polynomials and a separate Boolean gate interpreter.
Every nonlinear gate reuses one common r-by-2 matrix, but different argument
POSITIONS use different coefficients, even when they reference the same wire.
Exhaust all two-gate programs with two inputs, constants, fan-in 0..2 and
NOT/XOR/AND/OR. Curated deeper shared DAGs use r=1,2,3. This is finite evidence,
not a proof for arbitrary circuits, an independent reviewer or a novelty claim.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from typing import Iterable

Monomial = tuple[int, int]
Poly = frozenset[Monomial]
Gate = tuple[str, tuple[int, ...]]
ZERO: Poly = frozenset()
ONE: Poly = frozenset({(0, 0)})
X: tuple[Poly, ...] = (frozenset({(1, 0)}), frozenset({(0, 1)}), ZERO, ONE)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def plus(a: Poly, b: Poly) -> Poly:
    return a ^ b


def times(a: Poly, b: Poly) -> Poly:
    out: set[Monomial] = set()
    for u in a:
        for v in b:
            m = (u[0] + v[0], u[1] + v[1])
            if m in out:
                out.remove(m)
            else:
                out.add(m)
    return frozenset(out)


def total_degree(p: Poly) -> int:
    return max((sum(m) for m in p), default=0)


def evaluate(p: Poly, x: tuple[int, int]) -> int:
    return sum((x[0] ** m[0]) * (x[1] ** m[1]) for m in p) % 2


def matrices(r: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    return tuple(product(tuple(product((0, 1), repeat=2)), repeat=r))


def or_hash(A: tuple[tuple[int, int], ...], z: tuple[int, ...]) -> int:
    return int(any(sum(a[j] * z[j] for j in range(len(z))) % 2 for a in A))


def true_gate(op: str, z: tuple[int, ...]) -> int:
    if op == 'or':
        return int(any(z))
    if op == 'and':
        return int(all(z))
    if op == 'xor':
        return sum(z) % 2
    require(op == 'not' and len(z) == 1, 'invalid gate')
    return 1 - z[0]


def approximate_gate(op: str, A: tuple[tuple[int, int], ...], z: tuple[int, ...]) -> int:
    if op == 'or':
        return or_hash(A, z)
    if op == 'and':
        return 1 - or_hash(A, tuple(1 - b for b in z))
    return true_gate(op, z)


def polynomial_gate(op: str, A: tuple[tuple[int, int], ...], ps: tuple[Poly, ...]) -> Poly:
    if op == 'not':
        return plus(ONE, ps[0])
    if op == 'xor':
        out = ZERO
        for p in ps:
            out = plus(out, p)
        return out
    if op == 'and':
        return plus(ONE, polynomial_gate('or', A, tuple(plus(ONE, p) for p in ps)))
    require(op == 'or', 'invalid polynomial gate')
    out = ONE
    for a in A:
        row = ZERO
        for j, p in enumerate(ps):
            if a[j]:
                row = plus(row, p)
        out = times(out, plus(ONE, row))
    return plus(ONE, out)


def gate_options(wires: int) -> Iterable[Gate]:
    for op in ('or', 'and', 'xor'):
        for k in range(3):
            for refs in product(range(wires), repeat=k):
                yield op, refs
    for i in range(wires):
        yield 'not', (i,)


def check_program(program: tuple[Gate, ...], r: int, counts: Counter) -> None:
    require(r >= 1, 'positive r required for circuit degree bound')
    counts['program_parameter_pairs'] += 1
    heights = [0, 0, 0, 0]
    S = 0
    for op, refs in program:
        require(all(0 <= j < len(heights) for j in refs), 'not a topological DAG')
        nonlinear = op in ('or', 'and')
        S += nonlinear
        heights.append(max((heights[j] for j in refs), default=0) + nonlinear)
    inputs = tuple(product((0, 1), repeat=2))
    true_tables = []
    for x in inputs:
        values = list(x) + [0, 1]
        for op, refs in program:
            values.append(true_gate(op, tuple(values[j] for j in refs)))
        true_tables.append(values)
    bad_counts = [[0] * len(program) for _ in inputs]
    local_counts = [[0] * len(program) for _ in inputs]
    union_counts = [0] * len(inputs)
    space = matrices(r)
    for A in space:
        counts['program_matrix_pairs'] += 1
        polys = list(X)
        for i, (op, refs) in enumerate(program):
            polys.append(polynomial_gate(op, A, tuple(polys[j] for j in refs)))
            require(total_degree(polys[-1]) <= r ** heights[4+i], 'actual degree bound')
            counts['actual_degree_checks'] += 1
        for xi, x in enumerate(inputs):
            true = true_tables[xi]
            values = list(x) + [0, 1]
            local_bad = []
            for i, (op, refs) in enumerate(program):
                values.append(approximate_gate(op, A, tuple(values[j] for j in refs)))
                require(evaluate(polys[4+i], x) == values[-1], 'polynomial/interpreter mismatch')
                local = approximate_gate(op, A, tuple(true[j] for j in refs)) != true[4+i]
                local_bad.append(local)
                local_counts[xi][i] += local
                wrong = values[-1] != true[4+i]
                bad_counts[xi][i] += wrong
                require(not wrong or any(local_bad), 'topological true-input union implication')
                counts['node_input_checks'] += 1
            union_counts[xi] += any(local_bad)
    for xi, true in enumerate(true_tables):
        require(union_counts[xi] * 2**r <= S * len(space), 'shared-matrix union bound')
        for i, (op, refs) in enumerate(program):
            require(bad_counts[xi][i] * 2**r <= S * len(space), 'pointwise DAG error')
            z = tuple(true[j] for j in refs)
            active = (op == 'or' and any(z)) or (op == 'and' and not all(z))
            expected = Fraction(1, 2**r) if active else Fraction(0)
            require(Fraction(local_counts[xi][i], len(space)) == expected, 'local exact error law')
            counts['pointwise_node_bounds'] += 1
            counts['local_exact_laws'] += 1
        counts['pointwise_union_bounds'] += 1


def attacks() -> dict:
    A2 = matrices(2)
    # FALSE: a coefficient per source-wire identity is enough with duplicate refs.
    wrong_duplicate = sum(int(any((a[0] + a[0]) % 2 for a in A)) != 1 for A in A2)
    correct_duplicate = sum(or_hash(A, (1, 1)) != 1 for A in A2)
    require(Fraction(wrong_duplicate, len(A2)) == 1, 'duplicate-wire attack')
    require(Fraction(correct_duplicate, len(A2)) == Fraction(1, 4), 'duplicate-wire repair')
    # FALSE: shared gate events are independent. Identical true vectors give identical events.
    marginal = Fraction(sum(or_hash(A, (1, 1)) == 0 for A in A2), len(A2))
    joint = Fraction(sum(or_hash(A, (1, 1)) == 0 and or_hash(A, (1, 1)) == 0 for A in A2), len(A2))
    require(joint == Fraction(1, 4) and joint != marginal**2, 'cross-gate dependence attack')
    # FALSE: a pointwise law applies to a mask-dependent adversarial input.
    adaptive = []
    for A in matrices(1):
        a = A[0]
        z = (a[1], a[0]) if any(a) else (1, 0)
        require(any(z) and or_hash(A, z) == 0, 'adaptive input attack')
        adaptive.append({'mask': list(a), 'input': list(z)})
    # FALSE: r>=1 can be omitted from r^h bound in the presence of an exact skip wire.
    p = plus(polynomial_gate('or', (), (X[0], X[0])), X[0])
    require(total_degree(p) == 1 and 0**1 == 0, 'zero-row degree attack')
    # Historical distinction: genuine powers must not be Boolean-reduced for degree.
    p3 = polynomial_gate('or', ((1,0),)*3, (X[0],))
    require(p3 == frozenset({(1,0),(2,0),(3,0)}) and total_degree(p3) == 3, 'actual degree control')
    return {
        'per_wire_identity_hash': {'wrong_error':'1', 'repaired_error':'1/4', 'r':2, 'gate':'OR(x,x)', 'input':1},
        'inter_gate_independence': {'marginal':'1/4','actual_joint':'1/4','false_product':'1/16'},
        'adaptive_input': {'failure_probability':'1','false_fixed_input_bound':'1/2','choices':adaptive},
        'r_zero_circuit_degree': {'program':'OR(x,x) XOR x','actual_degree':1,'false_bound':0},
        'historical_actual_degree': {'polynomial':'x+x^2+x^3','actual_degree':3,'boolean_function':'x'}
    }


def main() -> None:
    exhaustive: Counter = Counter()
    programs = 0
    for first in gate_options(4):
        for second in gate_options(5):
            programs += 1
            for r in (1, 2):
                check_program((first, second), r, exhaustive)
    curated_programs: tuple[tuple[Gate,...], ...] = (
        (('or',(0,1)), ('and',(4,4)), ('xor',(4,5))),
        (('and',(0,1)), ('not',(4,)), ('or',(4,5))),
        (('or',(0,0)), ('xor',(4,0)), ('and',(4,5))),
        (('and',()), ('or',()), ('xor',(4,5))),
        (('xor',(0,0)), ('and',(4,3)), ('not',(5,))),
        (('or',(0,1)), ('not',(4,)), ('and',(4,5)), ('xor',(4,6))),
        (('or',(0,1)), ('or',(4,4)), ('or',(5,5)), ('or',(6,6))),
        (('and',(0,1)), ('and',(4,4)), ('and',(5,5)), ('and',(6,6))),
    )
    curated: Counter = Counter()
    for program in curated_programs:
        for r in (1,2,3):
            check_program(program, r, curated)
    print(json.dumps({
        'status':'PASS', 'arithmetic':'exact integers and Fraction; unreduced sparse GF2 polynomials',
        'scope':'finite controls; same author, two implementations; not a general proof',
        'sampler':'one shared r-by-2 matrix; argument-position coefficients; independent rows',
        'exhaustive': {'two_gate_programs':programs,'n':2,'fan_in':[0,1,2],'r':[1,2],**dict(exhaustive)},
        'curated': {'programs':len(curated_programs),'r':[1,2,3],**dict(curated)},
        'counterexamples': attacks(),
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
