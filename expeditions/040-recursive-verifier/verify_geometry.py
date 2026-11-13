"""Exact reference checks for one BV14-shaped k=7, a=3 RS recursion.

Python 3, standard library. The reference interpolates separately from eight
external values per coset. Its field arithmetic uses polynomial convolution,
long division, and E products expanded in a two-term basis. Source geometry:
BV14 section 6.1, equations (6)--(9), Proposition 6.1 and Definition 6.2.
"""
from collections import Counter
from functools import cache
import json

import recursive_rs as implementation


def require(condition, message):
    if not condition:
        raise ValueError(message)


@cache
def base_mul(a, b):
    product = 0
    for i in range(7):
        if b & (1 << i):
            product ^= a << i
    while product.bit_length() > 7:
        product ^= 0x83 << (product.bit_length() - 8)
    return product


def mul(x, y):
    coefficients = [0, 0, 0]
    for i, a in enumerate((x & 127, x >> 7)):
        for j, b in enumerate((y & 127, y >> 7)):
            coefficients[i + j] ^= base_mul(a, b)
    # theta^2 + theta + 1 = 0.
    return ((coefficients[0] ^ coefficients[2]) |
            ((coefficients[1] ^ coefficients[2]) << 7))


@cache
def inverse(x):
    require(x != 0, "zero denominator")
    output = 1
    for bit in bin((1 << 14) - 2)[2:]:
        output = mul(output, output)
        if bit == "1":
            output = mul(output, x)
    require(mul(output, x) == 1, "multiplicative inverse failed")
    return output


def parity_sum(seq):
    result = 0
    for x in seq:
        result ^= x
    return result


def product(seq):
    result = 1
    for x in seq:
        result = mul(result, x)
    return result


THETA = 128
ROOT = tuple(THETA ^ i for i in range(128))


def subspace_polynomial(x):
    return product(x ^ i for i in range(8))


def row_point(r, w):
    beta = ROOT[r << 3]
    return beta ^ parity_sum(v for i, v in enumerate((1, 2, 4, 4*THETA, 8*THETA, 2*THETA ^ beta))
                             if w & (1 << i))


ROWS = tuple(tuple(row_point(r, w) for w in range(64)) for r in range(16))
COLUMNS = tuple(subspace_polynomial(ROOT[r << 3]) for r in range(16))


def polynomial(coefficients, x):
    powers = [1]
    for _ in coefficients[1:]:
        powers.append(mul(x, powers[-1]))
    return parity_sum(mul(c, v) for c, v in zip(coefficients, powers))


@cache
def weights(nodes, x):
    return tuple(mul(product(x ^ u for u in nodes if u != v),
                     inverse(product(v ^ u for u in nodes if u != v)))
                 for v in nodes)


def interpolate(nodes, values, x):
    return parity_sum(mul(w, y) for w, y in zip(weights(nodes, x), values))


def degree_below(nodes, values, cutoff):
    return all(interpolate(nodes[:cutoff], values[:cutoff], x) == y
               for x, y in zip(nodes[cutoff:], values[cutoff:]))


def extend_rows(external):
    """Interpolate each row separately from its eight physical parent symbols."""
    cells = [None] * 1024
    for r, row in enumerate(ROWS):
        root_values = external[8*r:8*r+8]
        for w, x in enumerate(row):
            cells[implementation.row_cell(r, w)] = interpolate(row[:8], root_values, x)
    require(None not in cells and cells[:128] == external, "row-parent alias mismatch")
    return cells


def projected_coordinates(all_addresses):
    """Classify each little-endian output bit by its complete truth table."""
    addresses = tuple(all_addresses)
    require(len(addresses) == 128 and len(set(addresses)) == 128, "rank is not seven")
    require(all(0 <= address < 1024 for address in addresses), "out-of-range symbol")
    for bit in range(10):
        column = tuple((a >> bit) & 1 for a in addresses)
        if len(set(column)) == 1:
            continue
        require(any(all(value == (((z >> source_bit) & 1) ^ column[0])
                        for z, value in enumerate(column)) for source_bit in range(7)),
                "nonconstant address bit is not a seed literal")


def check_geometry():
    physical = {}
    for r, row in enumerate(ROWS):
        require(len(set(row)) == 64 and tuple(implementation.ROW_POINTS[r]) == row,
                "row ordered field points")
        require(set(row) & set(ROOT) == set(row[:8]), "row-parent overlap")
        for w, x in enumerate(row):
            cell = implementation.row_cell(r, w)
            expected = (w // 8) * 128 + 8 * r + w % 8
            require(cell == expected and cell not in physical, "physical coordinate encoding")
            physical[cell] = (x, COLUMNS[r])
    require(len(set(physical.values())) == 1024, "distinct geometric cells collided")
    require(tuple(implementation.COL_POINTS) == COLUMNS and len(set(COLUMNS)) == 16,
            "column ordered field points")
    for z, x in enumerate(ROOT):
        require(physical[z] == (x, subspace_polynomial(x)), "root mismatch on graph of q")
    for c in range(32):
        x = 2 * THETA ^ c % 8 ^ (4 * THETA if c & 8 else 0) ^ (8 * THETA if c & 16 else 0)
        for v, y in enumerate(COLUMNS):
            require(physical[implementation.col_cell(c, v)] == (x, y), "column-sibling alias")
    return physical


def routing(physical):
    counts = Counter()
    # For each fixed tape and offset test all seeds, including the rank and
    # each output-bit literal. Compare endpoints as ordered field pairs.
    for fresh in range(8):
        for offset in range(64):
            field_pairs = []
            cells = []
            for z in range(128):
                r, u = divmod(z, 8)
                w = ((fresh << 3) | u) ^ offset
                cell = implementation.row_query(z, fresh, offset)
                pair = (ROWS[r][w], COLUMNS[r])
                field_pairs.append(pair)
                cells.append(cell)
                require(physical[cell] == pair, "wrong routed row point")
                counts["row_to_parent" if pair[0] in ROOT else "row_extension"] += 1
            require(len(set(field_pairs)) == 128, "row seed rank on actual field points")
            projected_coordinates(cells)
    for fresh in range(4):
        for offset in range(16):
            cells = []
            for z in range(128):
                r, u = divmod(z, 8)
                c = (fresh << 3) | u
                cell = implementation.col_query(z, fresh, offset)
                expected_x = ROWS[0][32 + c]
                require(physical[cell] == (expected_x, COLUMNS[r ^ offset]), "wrong routed column")
                cells.append(cell)
                counts["column_to_sibling"] += 1
            projected_coordinates(cells)
    return {"fixed_tape_and_offset_maps": 8*64 + 4*16, "seeds_per_map": 128,
            "word_addresses": dict(sorted(counts.items()))}


def column_ordinates(cells, c):
    return [cells[implementation.col_cell(c, v)] for v in range(16)]


def check_honest():
    polynomials = [[0], [1]] + [[0]*degree + [1] for degree in range(1, 16)]
    polynomials += [[(13*i*i + 2*i + 7) % 128 for i in range(16)]]
    nonconstant_degree15_columns = []
    for coefficients in polynomials:
        external = [polynomial(coefficients, x) for x in range(128)]
        cells = extend_rows(external)
        require(cells == list(implementation.honest_cells(coefficients)),
                "honest cells disagree with separate interpolation from eight external values")
        for r, row in enumerate(ROWS):
            values = [cells[implementation.row_cell(r, w)] for w in range(64)]
            require(implementation.row_ok(cells, r) and degree_below(row, values, 8),
                    "honest row failed independent membership checks")
        affine_columns = 0
        for c in range(32):
            values = column_ordinates(cells, c)
            require(implementation.col_ok(cells, c) and degree_below(COLUMNS, values, 2),
                    "honest column failed independent membership checks")
            affine_columns += int(len(set(values)) > 1)
        if len(coefficients) == 16:
            require(affine_columns > 0, "did not exercise nonconstant column")
            nonconstant_degree15_columns.append(affine_columns)
    return {"polynomials": len(polynomials), "field_cells_per_polynomial": 1024,
            "nonconstant_columns_degree15_monomial_then_mixed": nonconstant_degree15_columns}


def split_controls():
    # The external F-word has value one at zero and zero elsewhere. Its
    # 127 zeros prohibit any polynomial of degree <16. An unconstrained
    # parent copy can be set to zero for all leaf tests.
    external = [1] + [0]*127
    require(not degree_below(ROOT, external, 16), "one-hot root incorrectly passed")
    all_zero = [0]*1024
    require(all(implementation.row_ok(all_zero, r) for r in range(16)) and
            all(implementation.col_ok(all_zero, c) for c in range(32)),
            "zero independent leaf tables failed")
    # Sharing parent reads but detaching columns permits a separate honest
    # local row interpolant for each parent block, and independent zero columns.
    cells = extend_rows(external)
    require(all(implementation.row_ok(cells, r) for r in range(16)), "one-hot row fits")
    bad_columns = 0
    for c in range(32):
        values = column_ordinates(cells, c)
        require(not degree_below(COLUMNS, values, 2) and not implementation.col_ok(cells, c),
                "row extension failed to expose the expected non-affine column")
        bad_columns += 1
    bare_delta = [1] + [0]*1023
    bad_rows = [r for r in range(16) if not implementation.row_ok(bare_delta, r)]
    bad_cols = [c for c in range(32) if not implementation.col_ok(bare_delta, c)]
    rejecting_seeds = [z for z in range(128) if z // 8 in bad_rows or
                       any((fresh*8 + z % 8) in bad_cols for fresh in range(4))]
    require(bad_rows == [0] and bad_cols == [] and rejecting_seeds == list(range(8)),
            "sharp eight-seed witness failed")
    coset_indicator = [1]*8 + [0]*1016
    coset_bad_rows = [r for r in range(16) if not implementation.row_ok(coset_indicator, r)]
    coset_bad_cols = [c for c in range(32) if not implementation.col_ok(coset_indicator, c)]
    require(coset_bad_rows == [0] and not coset_bad_cols, "sharp distance witness failed")
    external_weight = sum(value != 0 for value in coset_indicator[:128])
    zero_positions = 128 - external_weight
    nonzero_poly_disagreements = zero_positions - 15  # nonzero degree <=15 has <=15 roots
    require(nonzero_poly_disagreements > external_weight, "zero is not certified closest")
    # The unique degree<8 interpolant on the nonzero row vanishes exactly
    # on its seven zero interpolation nodes. Every rectangle column has one
    # nonzero and fifteen zero values, and so fails the affine test.
    return {"one_coset_indicator_all_extension_zero": {
                "bad_rows": coset_bad_rows, "bad_columns": coset_bad_cols,
                "root_distance_in_symbols": external_weight,
                "nonzero_polynomial_disagreement_lower_bound": nonzero_poly_disagreements,
                "rejected_public_seeds": [z for z in range(128) if z // 8 in coset_bad_rows]},
            "one_hot_root_all_extension_zero": {"bad_rows": bad_rows, "bad_columns": bad_cols,
                                                 "rejected_public_seeds": rejecting_seeds},
            "one_hot_root_index": 0, "one_hot_root_zero_count": 127,
            "detached_parent_and_zero_leaf_tables": {"rejecting_rows": 0, "rejecting_columns": 0},
            "parent_shared_columns_detached_zero": {"rejecting_rows": 0, "rejecting_columns": 0},
            "parent_shared_columns_aliased_to_interpolated_rows": {
                "rejecting_rows": 0, "rejecting_columns": bad_columns}}


if __name__ == "__main__":
    print(json.dumps({"fixture": "k=7, a=3, F_128 in F_16384", "routing": routing(check_geometry()),
                      "honest_controls": check_honest(), "split_copy_attacks": split_controls()},
                     indent=2, sort_keys=True))
