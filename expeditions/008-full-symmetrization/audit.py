#!/usr/bin/env python3
"""Finite semantic checks for full symmetrization, not a proof for arbitrary n.

Standard library only. No assert statements: python -O must run identical tests.
Polynomial exponents are retained, so degree is not a truth-table degree label.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from hashlib import sha1
from itertools import combinations, permutations, product
from math import factorial
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
Poly = frozenset[tuple[int, ...]]


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def degree(p: Poly) -> int:
    return max(map(sum, p), default=0)


def evaluate(p: Poly, x: tuple[int, ...]) -> int:
    return sum(all(e == 0 or x[i] == 1 for i, e in enumerate(m)) for m in p) % 2


def rename(p: Poly, e: tuple[int, ...]) -> Poly:
    out: Counter = Counter()
    for monomial in p:
        new = [0] * len(e)
        for i, power in enumerate(monomial):
            new[e[i]] += power
        out[tuple(new)] += 1
    return frozenset(m for m, c in out.items() if c % 2)


def pullback(e: tuple[int, ...], x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x[e[i]] for i in range(len(e)))


def transport_audit() -> dict:
    polynomials = permutations_checked = evaluations = 0
    for n in range(4):
        monomials = list(product(range(2), repeat=n))
        cube = list(product(range(2), repeat=n))
        perms = list(permutations(range(n)))
        for mask in range(1 << len(monomials)):
            p = frozenset(m for i, m in enumerate(monomials) if mask >> i & 1)
            polynomials += 1
            for e in perms:
                q = rename(p, e)
                require(degree(q) == degree(p), 'permutation lost actual degree')
                permutations_checked += 1
                for x in cube:
                    require(evaluate(q, x) == evaluate(p, pullback(e, x)), 'evaluation pullback reversed')
                    evaluations += 1
    # Nonmultilinear polynomial objects and cancellation are separate from ANF.
    higher = 0
    for n in range(1, 5):
        exps = [m for m in product(range(4), repeat=n) if sum(m) <= 5]
        cube = list(product(range(2), repeat=n))
        for k, m in enumerate(exps):
            p = frozenset([m, exps[(k + 1) % len(exps)]])
            for e in permutations(range(n)):
                q = rename(p, e)
                require(degree(p) == degree(q), 'higher-exponent degree changed')
                for x in cube:
                    require(evaluate(q, x) == evaluate(p, pullback(e, x)), 'higher-exponent eval changed')
                    higher += 1
    return {'all_squarefree_polynomials_n0_through_n3': polynomials,
            'polynomial_permutation_pairs': permutations_checked,
            'squarefree_evaluations': evaluations, 'higher_exponent_evaluations': higher}


def finite_average_audit() -> dict:
    cases = 0
    for n in range(4):
        cube = list(product(range(2), repeat=n))
        perms = list(permutations(range(n)))
        idx = {x: i for i, x in enumerate(cube)}
        transforms = [[idx[pullback(e, x)] for x in cube] for e in perms]
        for bits in range(1 << len(cube)):
            g = [F((bits >> i) & 1) for i in range(len(cube))]
            avg = [sum((g[t[i]] for t in transforms), F(0)) / len(perms) for i in range(len(cube))]
            for i, x in enumerate(cube):
                layer = [j for j, y in enumerate(cube) if sum(x) == sum(y)]
                require(avg[i] == sum((g[j] for j in layer), F(0)) / len(layer), 'orbit/layer discrepancy')
                for t in transforms:
                    require(avg[t[i]] == avg[i], 'full average not invariant')
            cases += 1
        # Signed values test the identity separately from probability assumptions.
        g = [F(i - 3, 7) for i in range(len(cube))]
        avg = [sum((g[t[i]] for t in transforms), F(0)) / len(perms) for i in range(len(cube))]
        require(min(avg) >= min(g), 'averaging violated a lower bound')
    return {'all_boolean_score_tables_n0_through_n3': cases,
            'empty_variable_case_included': True, 'signed_score_lower_bound_checks': 4}


def mixture_audit() -> dict:
    cases = 0
    for n in range(4):
        cube = list(product(range(2), repeat=n))
        perms = list(permutations(range(n)))
        p = frozenset([tuple(int(i == 0) for i in range(n))])
        q = frozenset([tuple(int(i == n - 1) for i in range(n))])
        rows, weights = [p, q, p], [F(1, 3), F(2, 3), F(0)]
        require(sum(weights) == 1 and min(weights) >= 0, 'invalid rational mixture')
        for target_mask in range(1 << (n + 1)):
            f = lambda x: (target_mask >> sum(x)) & 1
            def original(x):
                return sum((w for r, w in zip(rows, weights) if evaluate(r, x) == f(x)), F(0))
            direct = [sum((w / len(perms) for r, w in zip(rows, weights) for e in perms
                           if evaluate(rename(r, e), x) == f(x)), F(0)) for x in cube]
            indirect = [sum((original(pullback(e, x)) for e in perms), F(0)) / len(perms) for x in cube]
            require(direct == indirect, 'nonuniform real-mixture identity failed')
            require(min(direct) >= min(map(original, cube)), 'mixture minimum deteriorated')
            cases += 1
    return {'nonuniform_mixtures_with_zero_and_duplicate_rows': cases}


def rejected_mutations() -> list[str]:
    def probability(ws):
        require(min(ws) >= 0 and sum(ws) == 1, 'not a probability distribution')
    def full_group(es, n):
        require(len(es) == factorial(n) and len(set(es)) == len(es)
                and all(sorted(e) == list(range(n)) for e in es), 'not the complete permutation group')
    tests = [('signed_weights', lambda: probability([F(2), F(-1)])),
             ('unnormalized_weights', lambda: probability([F(1), F(1)])),
             ('repeated_permutation', lambda: full_group([(0, 1), (0, 1)], 2)),
             ('missing_permutation', lambda: full_group([(0, 1)], 2))]
    out = []
    for name, check in tests:
        try:
            check()
        except ValueError:
            out.append(name)
        else:
            raise ValueError('mutation unexpectedly accepted: ' + name)
    return out


def countermodels() -> dict:
    cube2 = list(product(range(2), repeat=2))
    perms2 = list(permutations(range(2)))
    p = frozenset([(1, 0)])
    x = (1, 0)
    original = F(evaluate(p, x) == x[0])
    after = sum((F(evaluate(rename(p, e), x) == x[0]) for e in perms2), F(0)) / 2
    require(original == 1 and after == F(1, 2), 'missing symmetry attack failed')
    global_zero_vs_and = F(sum(int(not all(y)) for y in cube2), 4)
    require(global_zero_vs_and == F(3, 4) and
            all(evaluate(rename(frozenset(), t), (1, 1)) != int(all((1, 1))) for t in perms2),
            'global average attack failed')
    e, x3 = (1, 2, 0), (0, 1, 0)
    inv = tuple(e.index(i) for i in range(3))
    p3 = frozenset([(1, 0, 0)])
    require(evaluate(rename(p3, e), x3) == 1 and evaluate(p3, pullback(inv, x3)) == 0,
            'inverse direction attack failed')
    p4 = frozenset([(1, 1, 0, 0)])
    cyclic = [tuple((i + k) % 4 for i in range(4)) for k in range(4)]
    full = list(permutations(range(4)))
    def zero_success(group, x):
        return F(sum(evaluate(rename(p4, t), x) == 0 for t in group), len(group))
    adjacent, opposite = (1, 1, 0, 0), (1, 0, 1, 0)
    require([zero_success(cyclic, x) for x in [adjacent, opposite]] == [F(3, 4), F(1)],
            'cyclic counterexample failed')
    require([zero_success(full, x) for x in [adjacent, opposite]] == [F(5, 6), F(5, 6)],
            'full group repair failed')
    collision = frozenset([(1, 0), (0, 1)])
    collapsed = rename(collision, (0, 0))
    require(degree(collision) == 1 and not collapsed, 'nonbijective renaming attack failed')
    bool_zero = frozenset([(2,), (1,)])
    require(degree(bool_zero) == 2 and all(evaluate(bool_zero, y) == 0 for y in [(0,), (1,)]),
            'formal vs functional degree attack failed')
    require(2 % 2 == 0 and F(1, 2) > 0, 'field/probability distinction failed')
    return {'nonsymmetric_target': {'target': 'x0', 'original_success': '1', 'symmetrized_success': '1/2', 'input': x},
            'whole_cube_average': {'target': 'AND2', 'polynomial': '0', 'average': '3/4', 'bad_input': [1, 1], 'bad_success': 0},
            'inverse_pullback': {'permutation': e, 'input': x3, 'correct_value': 1, 'wrong_inverse_value': 0},
            'cyclic_not_full': {'polynomial': 'x0*x1', 'target': '0', 'same_weight_inputs': [adjacent, opposite],
                                'cyclic_success': ['3/4', '1'], 'full_success': ['5/6', '5/6']},
            'nonbijective_degree': {'before': 1, 'after': 0},
            'functional_degree_is_not_totalDegree': {'polynomial': 'x0^2+x0', 'actual_degree': 2, 'boolean_truth_table': [0, 0]},
            'do_not_average_coefficients_in_GF2': {'two_in_GF2': 0, 'probability_one_half_in_R': '1/2'}}


def n7_audit() -> dict:
    raw = (ROOT / 'expeditions/007-small-support-mod3/certificate.json').read_bytes()
    digest = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    require(digest == 'c34de5b562d89b0ba19c735d0ca37c0e709c4f8b', 'historical certificate bytes changed')
    cert = json.loads(raw)['7']
    n, pairs = 7, list(combinations(range(7), 2))
    rows = []
    for c, a, b in cert['rows']:
        monomials = []
        if c: monomials.append((0,) * n)
        for i in range(n):
            if a >> i & 1: monomials.append(tuple(int(j == i) for j in range(n)))
        for k, (i, j) in enumerate(pairs):
            if b >> k & 1: monomials.append(tuple(int(t in (i, j)) for t in range(n)))
        rows.append(frozenset(monomials))
    cube = list(product(range(2), repeat=n))
    target = [int(sum(x) % 3 == 0) for x in cube]
    original = [sum(w for p, w in zip(rows, cert['weights']) if evaluate(p, x) == y)
                for x, y in zip(cube, target)]
    pushed = Counter()
    for e in permutations(range(n)):
        for p, w in zip(rows, cert['weights']):
            pushed[rename(p, e)] += w
    denom = 24 * 5040
    require(sum(pushed.values()) == denom, 'pushed weights not normalized')
    direct = [F(sum(w for p, w in pushed.items() if evaluate(p, x) == y), denom)
              for x, y in zip(cube, target)]
    by_layer = []
    for w in range(n + 1):
        members = [i for i, x in enumerate(cube) if sum(x) == w]
        expected = F(sum(original[i] for i in members), 24 * len(members))
        require(all(direct[i] == expected for i in members), 'literal renamed family does not match layer average')
        by_layer.append(str(expected))
    require(by_layer == ['2/3', '2/3', '2/3', '11/15', '2/3', '2/3', '2/3', '2/3'], 'unexpected layer result')
    require(min(direct) == F(2, 3), 'pointwise guarantee lost')
    return {'literal_polynomial_permutation_pairs': 18 * 5040,
            'distinct_renamed_polynomials': len(pushed), 'normalizing_denominator': denom,
            'all_inputs_checked': 128, 'success_by_weight': by_layer,
            'minimum_success': str(min(direct)), 'source_certificate_git_blob': 'c34de5b562d89b0ba19c735d0ca37c0e709c4f8b'}


def main() -> None:
    paths = ['PermutationTransport.lean', 'FiniteSymmetrization.lean']
    hashes = {}
    for name in paths:
        raw = (ROOT / 'formal/PvsNPCartography' / name).read_bytes()
        hashes[name] = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    report = {'scope': 'finite semantic self-audit; arbitrary-n validity requires the separate Lean proof',
              'formal_source_git_blobs': hashes, 'transport': transport_audit(),
              'averaging': finite_average_audit(), 'mixtures': mixture_audit(),
              'countermodels': countermodels(), 'mutations_rejected': rejected_mutations(), 'n7': n7_audit()}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
