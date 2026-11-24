#!/usr/bin/env python3
"""Independent finite controls for the scoped satisfying-RS-witness obstruction.

Does not import the expedition 046 compiler. All error distances are measured
on used raw cells, so filling any padding cannot repair a failed check.
"""
from collections import Counter
from itertools import product
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


class Field:
    def __init__(self, k, modulus):
        self.k, self.modulus, self.n = k, modulus, 1 << k

    def mul(self, x, y):
        out = 0
        while y:
            if y & 1:
                out ^= x
            x <<= 1
            y >>= 1
            if x & self.n:
                x ^= self.modulus
        return out

    def power(self, x, power):
        out = 1
        while power:
            if power & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            power >>= 1
        return out

    def inv(self, x):
        require(x != 0, "inverse of zero")
        out = self.power(x, self.n - 2)
        require(self.mul(x, out) == 1, "invalid field inverse")
        return out


def evaluate(coefficients, x, mul):
    value = 0
    for c in reversed(coefficients):
        value = mul(value, x) ^ c
    return value


def linear_factor(coefficients, x, mul):
    out = [0] * (len(coefficients) + 1)
    for j, c in enumerate(coefficients):
        out[j] ^= mul(x, c)
        out[j + 1] ^= c
    return out


def vanishing(nodes, mul):
    out = [1]
    for x in nodes:
        out = linear_factor(out, x, mul)
    return out


def interpolate(nodes, values, field):
    out = [0] * len(nodes)
    for i, y in enumerate(values):
        basis = vanishing(nodes[:i] + nodes[i + 1:], field.mul)
        scale = field.mul(y, field.inv(evaluate(basis, nodes[i], field.mul)))
        for j, c in enumerate(basis):
            out[j] ^= field.mul(c, scale)
    require([evaluate(out, x, field.mul) for x in nodes] == values,
            "interpolation failed")
    return out


def affine_tables(addresses, ambient_bits):
    # Bits constant on the queried set contribute only to the affine constant.
    active = [j for j in range(ambient_bits)
              if len({(x >> j) & 1 for x in addresses}) > 1]
    masks = [sum(((x >> j) & 1) << i for i, x in enumerate(addresses))
             for j in active]
    tables = {0, (1 << len(addresses)) - 1}
    for mask in masks:
        tables |= {t ^ mask for t in tuple(tables)}
    return active, sorted(tables)


def truth_on_raw(word, tags, k, seeds):
    bits = [(word[z] >> j) & 1 for j in range(k) for z in seeds]
    addresses = [(tags[j] << k) | z for j in range(k) for z in seeds]
    return addresses, sum(bit << i for i, bit in enumerate(bits))


def gf8_toy():
    f = Field(3, 0b1011)
    for x in range(1, f.n):
        f.inv(x)
    nodes = list(range(4))
    raw_addresses, _ = truth_on_raw([0] * 8, [0, 1, 2], 3, range(8))
    active, affine = affine_tables(raw_addresses, 5)
    histogram = Counter()
    systematic = set()
    words = set()
    x3_distance = None
    for coeffs in product(range(8), repeat=4):
        word = [evaluate(coeffs, x, f.mul) for x in range(8)]
        _, bits = truth_on_raw(word, [0, 1, 2], 3, range(8))
        words.add(bits)
        systematic.add(tuple(word[x] for x in nodes))
        nearest = min((bits ^ table).bit_count() for table in affine)
        histogram[nearest] += 1
        if coeffs == (0, 0, 0, 1):
            x3_distance = nearest
    require(len(systematic) == 8**4 == len(words), "RS systematic dimension")
    require(sum(histogram.values()) == 4096, "toy enumeration count")
    require(x3_distance > 1, "toy explicit counterexample")
    return {
        "scope": "GF(8) Reed-Solomon toy, not the a>=3 cross NO theorem",
        "field_modulus": "0xb", "degree_less_than": 4,
        "systematic_symbols": 4, "systematic_bits": 12,
        "codewords_enumerated": len(words), "raw_used_cells": 24,
        "ambient_address_bits": 5, "active_bits": active,
        "affine_restrictions": len(affine),
        "nearest_affine_distance_histogram": dict(sorted(histogram.items())),
        "X3_nearest_affine_distance": x3_distance,
        "arbitrary_layout_degree1_radius1_cover_upper": 2**6 * (1 + 12),
        "all_systematic_patterns": 2**12,
    }


def cross_a3():
    a, k, s = 3, 7, 8
    f = Field(k, 0x83)
    N, theta = f.n, f.n
    mask = N - 1
    for x in range(1, N):
        f.inv(x)

    def emul(x, y):
        u, v, r, t = x & mask, x >> k, y & mask, y >> k
        ur, vt = f.mul(u, r), f.mul(v, t)
        return (ur ^ vt) | ((f.mul(u ^ v, r ^ t) ^ ur) << k)

    q = vanishing(list(range(s)), f.mul)
    ordinates = [evaluate(q, v * s, f.mul) for v in range(2 * s)]
    require(len(set(ordinates)) == 2 * s, "distinct ordinates")
    for x in range(N):
        for u in range(s):
            require(evaluate(q, x ^ u, f.mul) == evaluate(q, x, f.mul),
                    "q constant on U cosets")

    def point(v, p, u):
        ext = 0
        for j in range(a - 1):
            if (p >> j) & 1:
                ext ^= (1 << (j + 2)) * theta
        return (v * s if p < s // 2 else 3 * theta) ^ ext ^ u

    def check_code(coeffs):
        residual = list(coeffs) + [0] * (2 * s - len(coeffs))
        quotient = [0] * s
        for j in range(s - 1, -1, -1):
            quotient[j] = residual[j + s]
            for i, c in enumerate(q):
                residual[j + i] ^= f.mul(quotient[j], c)
        remainder = residual[:s]
        require(not any(residual[s:]), "division by q")
        # Each row is this explicitly represented degree <s polynomial.
        row_coeffs = [[r ^ emul(y, c) for r, c in zip(remainder, quotient)]
                      for y in ordinates]
        pages = [[evaluate(row_coeffs[z // s], point(z // s, p, z % s), emul)
                  for z in range(N)] for p in range(s)]
        root = [evaluate(coeffs, z, f.mul) for z in range(N)]
        require(pages[0] == root, "shared root values")
        row_checks = 0
        column_checks = 0
        for v in range(2 * s):
            abscissae = [point(v, p, u) for p in range(s) for u in range(s)]
            require(len(set(abscissae)) == s * s, "row abscissae injective")
            for p in range(s):
                for u in range(s):
                    require(pages[p][v * s + u] ==
                            evaluate(row_coeffs[v], point(v, p, u), emul),
                            "row membership")
                    row_checks += 1
        # A common column is R(t)+y S(t); check all same physical cells.
        for p in range(s // 2, s):
            for u in range(s):
                t = point(0, p, u)
                b = evaluate(remainder, t, emul)
                slope = evaluate(quotient, t, emul)
                for v, y in enumerate(ordinates):
                    require(point(v, p, u) == t, "common abscissa")
                    require(pages[p][v * s + u] == b ^ emul(y, slope),
                            "shared affine column membership")
                    column_checks += 1
        return root, row_checks, column_checks

    systematic_nodes = list(range(2 * s))
    # Independent interpolation demonstrates an arbitrary non-affine data row.
    systematic_values = [((19 * i * i) ^ (7 * i) ^ 93) & mask
                         for i in systematic_nodes]
    arbitrary_coeffs = interpolate(systematic_nodes, systematic_values, f)
    code_counts = []
    for name, coefficients in [("zero", [0]), ("X", [0, 1]),
                               ("X3", [0, 0, 0, 1]),
                               ("arbitrary_systematic", arbitrary_coeffs)]:
        root, rows, columns = check_code(coefficients)
        code_counts.append({"name": name, "coefficients": coefficients,
                            "row_cells_checked": rows,
                            "column_cells_checked": columns})
        if name == "X3":
            x3_root = root
    # Source tag order: 7 A bit rows, then the seven B-root bit rows.
    addresses, truth = truth_on_raw(x3_root, list(range(7, 14)), k,
                                   systematic_nodes)
    active, affine = affine_tables(addresses, 22)
    distances = Counter((truth ^ table).bit_count() for table in affine)
    require(min(distances) == 42, "X3 exact restricted affine distance")
    require(len(affine) == 512, "affine restriction space")
    R, e = 2 * s * k, 4
    upper = 2**23 * sum(comb(R, j) for j in range(e + 1))
    require(upper < 2**R, "finite arbitrary-layout counting obstruction")
    return {
        "scope": "shared a=3 code-only relation; outer residual assertion removed",
        "original_YES_residual_not_claimed_for_alternative_roots": True,
        "field_modulus": "0x83", "a": a, "k": k, "N": N, "s": s,
        "code_checks": code_counts,
        "systematic_nodes": systematic_nodes,
        "systematic_values": systematic_values,
        "systematic_dimension_bits": R,
        "X3_raw_tags": list(range(7, 14)),
        "X3_used_slice_cells": len(addresses),
        "ambient_address_bits": 22, "active_slice_bits": active,
        "affine_restrictions": len(affine),
        "X3_nearest_affine_distance_on_used_slice": min(distances),
        "X3_affine_distance_histogram": dict(sorted(distances.items())),
        "counting_degree": 1, "counting_radius": e,
        "arbitrary_layout_cover_upper": upper,
        "all_systematic_patterns": 2**R,
        "padding_assumption": "none; all distances use queried raw cells",
        "soundness_caveat": "code-only relaxation has no inherited NO gap",
    }


if __name__ == "__main__":
    print(json.dumps({"gf8_toy": gf8_toy(), "cross_a3": cross_a3()},
                     sort_keys=True, indent=2))
