#!/usr/bin/env python3
"""Exact tiny controls for the row-degree sandwich and recoding cost audit.

This is independent of the previous expedition generators. It measures only
explicitly listed used addresses and never assumes a zero padding lower bound.
"""
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def degree(table, bits):
    coefficients = [(table >> x) & 1 for x in range(1 << bits)]
    for j in range(bits):
        for x in range(1 << bits):
            if (x >> j) & 1:
                coefficients[x] ^= coefficients[x ^ (1 << j)]
    return max((x.bit_count() for x, c in enumerate(coefficients) if c), default=0)


def monomial_table(mask, addresses):
    return sum(int((x & mask) == mask) << i for i, x in enumerate(addresses))


def restricted_code(addresses, bits, maximum_degree):
    # Span evaluations directly; this enumerates distinct restrictions, not
    # syntactically distinct polynomials that could coincide on the used set.
    code = {0}
    for mask in range(1 << bits):
        if mask.bit_count() <= maximum_degree:
            v = monomial_table(mask, addresses)
            if v not in code:
                code |= {x ^ v for x in tuple(code)}
    return sorted(code)


def nearest(word, code):
    return min((word ^ candidate).bit_count() for candidate in code)


def all_two_row_controls():
    k, R, b = 2, 2, 1
    N = 1 << k
    row_codes = [restricted_code(list(range(N)), k, d) for d in range(k + 1)]
    dense_addresses = list(range(R * N))
    dense_codes = [restricted_code(dense_addresses, k + b, d)
                   for d in range(k + b + 1)]
    sparse_labels = [(0, 7), (2, 5), (3, 4)]
    sparse_codes = []
    for labels in sparse_labels:
        addresses = [(tag << k) | z for tag in labels for z in range(N)]
        codes = [restricted_code(addresses, k + 3, d)
                 for d in range(k + b + 1)]
        # For two distinct labels, affine separation can realize their dense
        # bit, and restriction cannot reduce seed degree. This exact equality
        # is a finite control, not the proof of the general sandwich.
        require(codes == dense_codes, "two-row sparse-code equality")
        sparse_codes.append([len(code) for code in codes])
    tested, maximum_gap = 0, 0
    positive_gap_example = None
    for word in range(1 << (R * N)):
        rows = [(word >> (i * N)) & ((1 << N) - 1) for i in range(R)]
        row_error = [sum(nearest(row, row_codes[d]) for row in rows)
                     for d in range(k + 1)]
        dense_error = [nearest(word, code) for code in dense_codes]
        for E in range(R * N + 1):
            delta = next(d for d, error in enumerate(row_error) if error <= E)
            actual = next(d for d, error in enumerate(dense_error) if error <= E)
            require(delta <= actual <= delta + b, "row sandwich violated")
            tested += 1
            if actual - delta > maximum_gap:
                maximum_gap = actual - delta
                positive_gap_example = {"truth_table": word, "raw_error_budget": E,
                                        "row_optimum": delta, "dense_optimum": actual}
    return {"rows": R, "seed_bits": k, "dense_tag_bits": b,
            "truth_tables": 256, "budgets_per_table": 9,
            "table_budget_pairs_checked": tested,
            "sparse_injections": sparse_labels,
            "distinct_codeword_counts_per_degree": [len(c) for c in dense_codes],
            "sparse_counts": sparse_codes,
            "maximum_dense_minus_row_degree": maximum_gap,
            "example": positive_gap_example}


def adaptive_constant_rows():
    b, k = 4, 2
    R, N = 1 << b, 1 << k
    rows = [0] * (R - 1) + [(1 << N) - 1]
    native = sum(row << (i * N) for i, row in enumerate(rows))
    require(degree(native, b + k) == b, "dense constant-row degree")
    # Public row identities are retained; this injective guessed table sends
    # the one-valued row to label 1, and distinct zero rows to even labels.
    labels = [2 * i for i in range(R - 1)] + [1]
    require(len(set(labels)) == R and max(labels) < (1 << (b + 1)),
            "adaptive injectivity")
    for i, tag in enumerate(labels):
        for z in range(N):
            require((tag & 1) == ((rows[i] >> z) & 1), "adaptive degree-one match")
    require(any(rows) and any(row == 0 for row in rows), "constant cannot fit exactly")
    # The native leading term is the product of all four tag bits. Summing
    # over those four bits for each of the four seed assignments gives four
    # disjoint odd-parity cubes. Any degree <=3 polynomial has even parity
    # on every cube, so at least four used-cell errors are necessary.
    parity_cubes = []
    for z in range(N):
        cells = [(i << k) | z for i in range(R)]
        parity = sum((native >> x) & 1 for x in cells) & 1
        require(parity == 1, "direct odd parity")
        parity_cubes.append({"seed": z, "parity": parity})
    require(native.bit_count() == N, "zero polynomial attains distance")
    return {"rows": R, "seed_bits": k, "dense_tag_bits": b,
            "raw_row_error_budget": 0, "row_optimum": 0,
            "dense_exact_degree": b, "adaptive_exact_degree": 1,
            "adaptive_tag_bits": b + 1, "adaptive_label_table_bits": R * (b + 1),
            "adaptive_labels": labels, "public_dense_upper_is_attained": True,
            "nearest_degree_at_most3_raw_error": N,
            "padding_used_for_lower_bound": False,
            "direct_odd_parity_cubes": parity_cubes}


def low_degree_composition_sharpness():
    # Two disjoint reversible shears on six bits:
    # y0=x0+x1*x2, y3=x3+x4*x5. Other coordinates stay unchanged.
    m = 6
    def phi(x):
        y = x
        if ((x >> 1) & 1) and ((x >> 2) & 1):
            y ^= 1
        if ((x >> 4) & 1) and ((x >> 5) & 1):
            y ^= 1 << 3
        return y
    image = [phi(x) for x in range(1 << m)]
    require(len(set(image)) == (1 << m), "shear bijection")
    require(all(phi(phi(x)) == x for x in range(1 << m)), "shear inverse")
    p = sum(int((y & 1) and ((y >> 3) & 1)) << y for y in range(1 << m))
    pulled = sum(((p >> phi(x)) & 1) << x for x in range(1 << m))
    coord_degrees = [degree(sum(((phi(x) >> j) & 1) << x for x in range(1 << m)), m)
                     for j in range(m)]
    require(degree(p, m) == 2 and max(coord_degrees) == 2,
            "composition input degrees")
    require(degree(pulled, m) == 4, "composition degree product sharpness")
    return {"address_bits": m, "coordinate_degrees": coord_degrees,
            "approximant_degree": 2, "decoded_degree": 4,
            "bijection": True, "inverse_is_same_map": True,
            "generic_degree_product_bound_attained": True}


def precision_counterexample():
    # Inject old 2-bit addresses into a codimension-three slice. The new
    # target is zero everywhere, but the degree-three slice indicator has
    # error 1/8 globally and error one on every queried address.
    k, c = 2, 3
    m = k + c
    image = list(range(1 << k))
    p = sum(int((y >> k) == 0) << y for y in range(1 << m))
    require(degree(p, m) == c and p.bit_count() == (1 << k), "slice indicator")
    require(all((p >> y) & 1 for y in image), "queried errors")
    return {"native_bits": k, "new_bits": m, "codimension": c,
            "global_error_numerator": p.bit_count(),
            "global_error_denominator": 1 << m,
            "used_error_numerator": len(image), "used_error_denominator": len(image),
            "precision_loss_factor": 1 << c, "indicator_degree": c,
            "map_injective": True}


def complementary_clamp_gluing():
    k = 3
    # A whole row can have one more degree than its two complementary
    # clamp restrictions. Requiring only one half would not cover the row.
    native = 1 << ((1 << k) - 1)  # x0*x1*x2
    halves = []
    for epsilon in (0, 1):
        table = sum(((native >> ((z & ~1) | epsilon)) & 1) << z
                    for z in range(1 << k))
        halves.append(table)
    glued = sum(((halves[z & 1] >> z) & 1) << z for z in range(1 << k))
    require(glued == native, "complementary clamp gluing")
    require([degree(t, k) for t in halves] == [0, 2] and degree(glued, k) == 3,
            "clamp degree addition sharpness")
    return {"seed_bits": k, "clamped_coordinate": 0,
            "half_degrees": [degree(t, k) for t in halves],
            "glued_degree": degree(glued, k),
            "whole_row_exactly_recovered": True,
            "one_degree_gluing_cost_attained": True}


if __name__ == "__main__":
    print(json.dumps({"two_rows": all_two_row_controls(),
                      "adaptive_constants": adaptive_constant_rows(),
                      "degree_composition": low_degree_composition_sharpness(),
                      "precision": precision_counterexample(),
                      "clamp_gluing": complementary_clamp_gluing()},
                     indent=2, sort_keys=True))
