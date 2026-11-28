#!/usr/bin/env python3
"""Exact finite controls for interpolation, affine selectors and division.

No predecessor arithmetic is imported. General statements are proved in
linearized-degree.md; the enumerations here are finite checks, not proofs.
"""

import argparse
from collections import Counter
import json
from pathlib import Path


def require(test, message):
    if not test:
        raise RuntimeError(message)


class Field:
    def __init__(self, k, modulus):
        self.k, self.n, self.modulus = k, 1 << k, modulus
        def multiply(a, b):
            result = 0
            while b:
                if b & 1:
                    result ^= a
                b >>= 1
                a <<= 1
                if a & self.n:
                    a ^= modulus
            return result
        self.table = [bytes(multiply(a, b) for b in range(self.n)) for a in range(self.n)]
        self.inverses = [0] + [self.table[a].index(1) for a in range(1, self.n)]
        require(all(self.mul(a, self.inverses[a]) == 1 for a in range(1, self.n)), "not a field")

    def mul(self, a, b):
        return self.table[a][b]

    def power(self, a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, a)
            exponent >>= 1
            a = self.mul(a, a)
        return result


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [0]


def add(a, b):
    c = [0] * max(len(a), len(b))
    for p in (a, b):
        for i, x in enumerate(p):
            c[i] ^= x
    return trim(c)


def multiply(a, b, field):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[i+j] ^= field.mul(x, y)
    return trim(c)


def vanisher(points, field):
    p = [1]
    for x in points:
        p = multiply(p, [x, 1], field)
    return p


def evaluate(p, x, field):
    answer = 0
    for c in reversed(p):
        answer = field.mul(answer, x) ^ c
    return answer


def divide(p, divisor, field):
    require(divisor[-1] == 1, "division needs monic divisor")
    remainder = trim(p)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    while remainder != [0] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        c = remainder[-1]
        quotient[shift] ^= c
        for j, d in enumerate(divisor):
            remainder[j+shift] ^= field.mul(c, d)
        remainder = trim(remainder)
    return trim(quotient), remainder


def degree(values):
    """Vectorial Boolean degree: one XOR Mobius transform over field words."""
    coefficients = list(values)
    n = len(coefficients)
    require(n > 0 and n & (n-1) == 0, "truth table length is not a power of two")
    bit = 1
    while bit < n:
        for mask in range(n):
            if mask & bit:
                coefficients[mask] ^= coefficients[mask ^ bit]
        bit <<= 1
    return max((mask.bit_count() for mask, c in enumerate(coefficients) if c), default=-1)


def polynomial_weight(p):
    return max((i.bit_count() for i, c in enumerate(p) if c), default=-1)


def chi(e, h):
    s = 1 << h
    return e // s + (e % s).bit_count()


def chi_degree(p, h):
    return max((chi(i, h) for i, c in enumerate(p) if c), default=-1)


def linear_spaces(k):
    spaces = {frozenset([0])}
    for _ in range(k):
        enlarged = set(spaces)
        for space in spaces:
            for x in range(1 << k):
                if x not in space:
                    enlarged.add(frozenset(space | {v ^ x for v in space}))
        spaces = enlarged
    return sorted(spaces, key=lambda s: (len(s), sorted(s)))


def affine_spaces(k):
    result = []
    for space in linear_spaces(k):
        unseen = set(range(1 << k))
        while unseen:
            b = min(unseen)
            coset = frozenset(b ^ x for x in space)
            result.append((space, b, coset))
            unseen.difference_update(coset)
    require(len({item[2] for item in result}) == len(result), "duplicate affine space")
    return result


def ordered_span(space):
    values = [0]
    for x in sorted(space):
        if x not in values:
            values += [v ^ x for v in values]
    require(set(values) == set(space), "span coordinates failed")
    return values


def monomial_checks(field):
    powers = [[1] * field.n for _ in range(field.n)]
    for x in range(field.n):
        for e in range(1, field.n):
            powers[e][x] = field.mul(powers[e-1][x], x)
    for e, values in enumerate(powers):
        require(degree(values) == e.bit_count(), "full-field binary-weight identity failed")
    return field.n


def division_checks(field, spaces):
    columns = 0
    bounds = Counter()
    for space, b, points in spaces:
        s, h = len(points), len(points).bit_length() - 1
        divisor = vanisher(sorted(points), field)
        require(all(not c or i == 0 or i & (i-1) == 0 for i, c in enumerate(divisor)),
                "affine vanisher is not affine-linearized")
        for e in range(min(3*s, field.n)):
            monomial = [0]*e + [1]
            quotient, remainder = divide(monomial, divisor, field)
            require(add(multiply(quotient, divisor, field), remainder) == monomial,
                    "division reconstruction failed")
            if quotient != [0]:
                require(chi_degree(quotient, h) <= chi(e, h)-1, "chi quotient bound failed")
                require(polynomial_weight(quotient) <= e.bit_count(), "low-ratio weight bound failed")
            observed = degree([evaluate(quotient, x, field) for x in range(field.n)])
            require(observed == polynomial_weight(quotient), "quotient ANF/weight mismatch")
            bounds[h] += 1
            columns += 1
    return {"affine_divisors": len(spaces), "monomial_columns": columns,
            "columns_by_dimension": dict(sorted(bounds.items())),
            "method": "all columns of each F-linear Euclidean-division map, not all polynomial inputs"}


def selector_checks(field, spaces):
    zeroes = {points: vanisher(sorted(points), field) for _, _, points in spaces}
    cases, by_codim = 0, Counter()
    for _, _, hpoints in spaces:
        for _, _, upoints in spaces:
            if not upoints <= hpoints:
                continue
            selector, remainder = divide(zeroes[hpoints], zeroes[upoints], field)
            require(remainder == [0], "nested-space selector did not divide")
            c = len(hpoints).bit_length() - len(upoints).bit_length()
            values = [evaluate(selector, x, field) for x in range(field.n)]
            require(degree(values) == c, "selector degree differs from codimension")
            on_u = {values[x] for x in upoints}
            require(len(on_u) == 1 and 0 not in on_u, "selector scale is not constant and nonzero")
            require(all(values[x] == 0 for x in hpoints - upoints), "selector did not vanish")
            cases += 1
            by_codim[c] += 1
    return {"nested_affine_pairs": cases, "by_codimension": dict(sorted(by_codim.items()))}


def interpolation_checks(field, spaces):
    cases, hist = 0, Counter()
    for space, b, points in spaces:
        if len(points) > 8:
            continue
        ordered = [b ^ v for v in ordered_span(space)]
        basis = []
        for p in ordered:
            numerator = vanisher([x for x in ordered if x != p], field)
            scale = field.inverses[evaluate(numerator, p, field)]
            basis.append([field.mul(c, scale) for c in numerator])
        for truth in range(1 << len(points)):
            data = [(truth >> i) & 1 for i in range(len(points))]
            polynomial = [0]
            for bit, basis_polynomial in zip(data, basis):
                if bit:
                    polynomial = add(polynomial, basis_polynomial)
            require(len(polynomial) <= len(points), "interpolant exceeds its cutoff")
            require([evaluate(polynomial, x, field) for x in ordered] == data, "interpolation mismatch")
            r = degree(data)
            values = [evaluate(polynomial, x, field) for x in range(field.n)]
            require(degree(values) == polynomial_weight(polynomial) == r, "interpolation degree changed")
            hist[r] += 1
            cases += 1
    return {"Boolean_assignments": cases, "assignment_degree_histogram": dict(sorted(hist.items())),
            "scope": "all Boolean data on every affine subspace of dimension at most3 in GF16"}


class Circuit:
    """Actual public bit-gate topology with exhaustive parallel truth tables."""
    def __init__(self, field):
        self.field, self.full = field, (1 << field.n)-1
        self.values = [0, self.full]
        self.gates = []
        self.inputs = [self.add_input(sum(((x >> bit) & 1) << x for x in range(field.n)))
                       for bit in range(field.k)]

    def add_input(self, value):
        self.values.append(value)
        return len(self.values)-1

    def gate(self, op, a, b):
        value = self.values[a] ^ self.values[b] if op == "xor" else self.values[a] & self.values[b]
        self.values.append(value)
        node = len(self.values)-1
        self.gates.append((op, a, b, node))
        return node

    def constant(self, value):
        return [(value >> bit) & 1 for bit in range(self.field.k)]

    def xor_words(self, a, b):
        return [self.gate("xor", x, y) for x, y in zip(a, b)]

    def linear(self, word, columns, constant=0):
        result = self.constant(constant)
        for i, column in enumerate(columns):
            for bit in range(self.field.k):
                if column >> bit & 1:
                    result[bit] = self.gate("xor", result[bit], word[i])
        return result

    def scale(self, word, coefficient):
        return self.linear(word, [self.field.mul(1 << i, coefficient) for i in range(self.field.k)])

    def square(self, word):
        return self.linear(word, [self.field.mul(1 << i, 1 << i) for i in range(self.field.k)])

    def product(self, a, b):
        result = self.constant(0)
        for i in range(self.field.k):
            for j in range(self.field.k):
                node = self.gate("and", a[i], b[j])
                column = self.field.mul(1 << i, 1 << j)
                for bit in range(self.field.k):
                    if column >> bit & 1:
                        result[bit] = self.gate("xor", result[bit], node)
        return result

    def affine_linearized(self, polynomial):
        constant = polynomial[0]
        columns = [evaluate(polynomial, 1 << i, self.field) ^ constant for i in range(self.field.k)]
        return self.linear(self.inputs, columns, constant)

    def report(self, output):
        cache = {}
        def node_degree(node):
            value = self.values[node]
            if value not in cache:
                cache[value] = degree([(value >> x) & 1 for x in range(self.field.n)])
            return cache[value]
        hist = Counter(node_degree(node) for _, _, _, node in self.gates)
        output_values = [sum(((self.values[node] >> x) & 1) << bit for bit, node in enumerate(output))
                         for x in range(self.field.n)]
        return {"gate_count": len(self.gates), "gate_degree_histogram": dict(sorted(hist.items())),
                "maximum_gate_degree": max(hist, default=-1), "output_degree": degree(output_values)}, output_values


def circuit_checks(field):
    reports = []
    for c in range(1, field.k+1):
        hpoints = list(range(field.n))
        upoints = list(range(1 << (field.k-c)))
        zu = vanisher(upoints, field)
        selector, remainder = divide(vanisher(hpoints, field), zu, field)
        require(remainder == [0], "circuit selector division failed")
        images = sorted({evaluate(zu, x, field) for x in hpoints})
        image_zero = vanisher(images, field)
        require(len(images) == 1 << c, "wrong image codimension")
        optimized = Circuit(field)
        y = optimized.affine_linearized(zu)
        power = optimized.constant(1)
        result = optimized.constant(0)
        for j in range(c+1):
            result = optimized.xor_words(result, optimized.scale(power, image_zero[1 << j]))
            if j < c:
                power = optimized.product(optimized.square(power), y)
        optimized_report, optimized_values = optimized.report(result)
        require(optimized_report["maximum_gate_degree"] <= c, "Frobenius compiler degree bound failed")
        naive = Circuit(field)
        result = naive.constant(1)
        for x in sorted(set(hpoints)-set(upoints)):
            result = naive.product(result, naive.xor_words(naive.inputs, naive.constant(x)))
        naive_report, naive_values = naive.report(result)
        expected = [evaluate(selector, x, field) for x in range(field.n)]
        require(optimized_values == naive_values == expected, "two public circuits compute different selectors")
        reports.append({"codimension": c, "Frobenius": optimized_report, "factor_product": naive_report})
    require(reports[0]["factor_product"]["maximum_gate_degree"] > 1, "missing high-degree intermediate control")
    return reports


def main():
    f16, f256 = Field(4, 0x13), Field(8, 0x11B)
    spaces = affine_spaces(4)
    require(len(spaces) == 307, "wrong GF16 affine-space count")
    monomial_count = monomial_checks(f16) + monomial_checks(f256)
    division = division_checks(f16, spaces)
    selectors = selector_checks(f16, spaces)
    interpolation = interpolation_checks(f16, spaces)
    circuits = circuit_checks(f16)

    # Outside the fixed degree ratio, division CAN greatly raise Boolean degree.
    numerator = [0]*129
    numerator[1] = numerator[128] = 1
    quotient, remainder = divide(numerator, [0, 1, 1], f256)
    require(remainder == [0] and len(quotient)-1 == 126, "large-ratio division changed")
    q_degree = degree([evaluate(quotient, x, f256) for x in range(256)])
    n_degree = degree([evaluate(numerator, x, f256) for x in range(256)])
    require(n_degree == 1 and q_degree == 6, "large-ratio degree control failed")

    # Exact degree extension says nothing about preservation of Hamming errors.
    points = list(range(16))
    selector = vanisher(points[1:], f256)
    scale = f256.inverses[evaluate(selector, 0, f256)]
    lagrange = [f256.mul(c, scale) for c in selector]
    values = [evaluate(lagrange, x, f256) for x in range(256)]
    require(sum(values[x] != 0 for x in points) == 1, "assignment delta changed")
    require(sum(x != 0 for x in values) == 241, "one-error interpolation spread changed")
    return {"scope": "finite exact controls, not general proof or weighted approximation theorem",
            "fields": [{"k": f.k, "modulus": f.modulus} for f in (f16, f256)],
            "full_field_monomial_weight_checks": monomial_count,
            "Euclidean_division": division, "affine_selectors": selectors,
            "canonical_interpolation": interpolation, "public_selector_circuits_GF16": circuits,
            "large_ratio_counterexample": {"divisor": "X^2+X", "numerator": "X^128+X",
                                             "quotient_univariate_degree": 126,
                                             "numerator_seed_degree": n_degree, "quotient_seed_degree": q_degree},
            "Hamming_instability_control": {"field_size": 256, "assignment_domain_size": 16,
                                            "changed_assignment_symbols": 1, "changed_root_symbols": 241},
            "limits": ["all finite fields use independently implemented carryless arithmetic",
                       "general lemmas require the separate written proofs",
                       "no recursive source Boolean compiler or soundness gap is generated here",
                       "no Lean, external review, novelty or complexity separation is claimed"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(main(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end="")
