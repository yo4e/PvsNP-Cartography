#!/usr/bin/env python3
"""Audit Boolean degree of actual honest k=8,a=3 recursive RS extensions.

Uses Expedition041's legal_extension(e), not naive global monomial evaluation
at a cell's extension-field abscissa. Source arithmetic/geometry are reused.
All writes are confined to this standalone check's caller-selected outputs.
"""

import argparse
from collections import Counter
from importlib import util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(name, path):
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def trim(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def multiply(left, right, mul):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] ^= mul(a, b)
    return trim(result)


def add(left, right):
    result = [0] * max(len(left), len(right))
    for poly in (left, right):
        for i, value in enumerate(poly):
            result[i] ^= value
    return trim(result)


def divide_monic(numerator, denominator, mul):
    require(denominator[-1] == 1, "denominator not monic")
    remainder = trim(numerator)
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    while remainder != [0] and len(remainder) >= len(denominator):
        offset = len(remainder) - len(denominator)
        coefficient = remainder[-1]
        quotient[offset] = coefficient
        for j, value in enumerate(denominator):
            remainder[offset + j] ^= mul(coefficient, value)
        remainder = trim(remainder)
    return trim(quotient), remainder


def q_adic(poly, q, mul):
    """P(X)=sum_j result[j](X)*q(X)^j, each remainder degree<deg(q)."""
    remaining, chunks = trim(poly), []
    while remaining != [0]:
        remaining, remainder = divide_monic(remaining, q, mul)
        chunks.append(remainder)
    chunks = chunks or [[0]]
    rebuilt = [0]
    for chunk in reversed(chunks):
        rebuilt = add(multiply(rebuilt, q, mul), chunk)
    require(rebuilt == trim(poly), "q-adic polynomial identity failed")
    return chunks


def vanisher(points, mul):
    result = [1]
    for point in points:
        result = multiply(result, [point, 1], mul)
    require(result[-1] == 1 and result[0] == 0, "wrong monic subspace vanisher")
    require(all(i and i & (i - 1) == 0 for i, c in enumerate(result) if c),
            "subspace vanisher is not linearized")
    return result


def anf(values):
    coefficients = list(values)
    require(len(coefficients) == 256, "unexpected seed cube")
    for bit in range(8):
        for mask in range(256):
            if mask & (1 << bit):
                coefficients[mask] ^= coefficients[mask ^ (1 << bit)]
    return coefficients


def row_audit(cells, index, expected_bound):
    histogram = Counter()
    by_shape = {"root": Counter(), "R": Counter(), "RR": Counter()}
    maximum = -1
    root_maximum = -1
    symbolic_coefficients_checked = 0
    for (shape, auxiliary), row in index.items():
        values = cells[row * 256:(row + 1) * 256]
        coefficients = anf(values)
        width = 8 if not shape else 16
        component_degrees = [-1] * width
        for mask, value in enumerate(coefficients):
            require(value < 1 << width, "symbol exceeds its actual physical bit width")
            degree = mask.bit_count()
            require(degree <= expected_bound or value == 0,
                    f"degree inflation on shape={shape},aux={auxiliary},mask={mask}")
            symbolic_coefficients_checked += 1
            for bit in range(width):
                if value & (1 << bit):
                    component_degrees[bit] = max(component_degrees[bit], degree)
        name = "".join(shape) or "root"
        histogram.update(component_degrees)
        by_shape[name].update(component_degrees)
        maximum = max(maximum, *component_degrees)
        if not shape:
            root_maximum = max(component_degrees)
    require(maximum == root_maximum == expected_bound,
            "root monomial should attain its binary-weight degree")
    require(sum(histogram.values()) == 1016, "wrong physical bit-row count")
    return {
        "maximum_raw_seed_degree": maximum,
        "root_maximum_seed_degree": root_maximum,
        "raw_bit_row_degree_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "by_shape_degree_histogram": {
            shape: {str(k): v for k, v in sorted(counts.items())}
            for shape, counts in by_shape.items()},
        "vector_ANF_coefficients_checked": symbolic_coefficients_checked,
    }


def main(repo_root):
    repo = Path(repo_root)
    p048 = repo / "expeditions/048-recursive-row-normalization"
    normal = load("check_recursive_normalization", p048 / "check_recursive_normalization.py")
    bridge = load("actual_recursive_field_bridge", p048 / "check_recursive_field_bridge.py")
    rs = load("actual_two_level_oracle", repo / "expeditions/041-two-level-distance/two_level_oracle.py")
    geometry = normal.load_geometry(repo)
    layout = geometry.Layout(8, 3, 2)
    index = normal.row_index(layout)
    forward, names_checked = bridge.source_transport(layout, index, rs)
    leaves = rs.geometry()
    q0 = vanisher(range(16), rs.mul)
    q1 = vanisher(range(8), rs.mul)

    outer_bases = set()
    inner_bases = set()
    inner_low_spaces = set()
    for beta, basis in rs.OUTER_COORDS:
        outer_bases.add(basis)
        require(basis[:4] == (1, 2, 4, 8), "outer row lower space unexpectedly varies")
        for j in range(16):
            delta, directions = rs.row_coordinates(beta, basis, rs.INNER_AUX, j)
            inner_bases.add(directions)
            inner_low_spaces.add(directions[:3])
            require(directions[:3] == (1, 2, 4), "inner lower space unexpectedly varies")

    # Directly check that each physical point and the two row ordinates are
    # affine functions on a fixed normalized row. Basis dependence is visible.
    geometry_rows_checked = 0
    for (shape, auxiliary), row in index.items():
        point_values, outer_ordinates, inner_ordinates = [], [], []
        for z in range(256):
            u, v = z & 15, z >> 4
            beta, basis = rs.OUTER_COORDS[v]
            y0 = rs.subspace_value(16, beta)
            if not shape:
                x, y1 = rs.THETA ^ z, 0
            elif shape == ("R",):
                p = auxiliary
                x = beta ^ rs.vector(basis, u | (p << 4))
                y1 = 0
            else:
                require(shape == ("R", "R"), "unexpected recursive physical shape")
                p, q = auxiliary & 7, auxiliary >> 3
                j = (u >> 3) | (p << 1)
                delta, directions = rs.row_coordinates(beta, basis, rs.INNER_AUX, j)
                x = delta ^ rs.vector(directions, (u & 7) | (q << 3))
                y1 = rs.subspace_value(8, delta)
            point_values.append(x)
            outer_ordinates.append(y0)
            inner_ordinates.append(y1)
        for values in (point_values, outer_ordinates, inner_ordinates):
            require(all(value == 0 or mask.bit_count() <= 1
                        for mask, value in enumerate(anf(values))),
                    "actual point/ordinate is not affine across the normalized row")
        geometry_rows_checked += 1

    monomials = []
    for exponent in range(32):
        bound = exponent.bit_count()
        # P translated to the actual root abscissa: (X+theta)^exponent.
        translated = [rs.field_power(rs.THETA, exponent - i)
                      if i & exponent == i else 0 for i in range(exponent + 1)]
        outer_chunks = q_adic(translated, q0, rs.mul)
        outer_weight = max(i.bit_count() + j.bit_count()
                           for j, chunk in enumerate(outer_chunks)
                           for i, coefficient in enumerate(chunk) if coefficient)
        inner_weight = -1
        for j, chunk in enumerate(outer_chunks):
            inner_chunks = q_adic(chunk, q1, rs.mul)
            for t, child_chunk in enumerate(inner_chunks):
                for h, coefficient in enumerate(child_chunk):
                    if coefficient:
                        inner_weight = max(inner_weight,
                                           h.bit_count() + t.bit_count() + j.bit_count())
        require(outer_weight <= bound and inner_weight <= bound,
                "fixed-vanisher expansion increased weighted degree")

        source_cells = rs.legal_extension(exponent)
        accepted, paired, passing_leaves = rs.run_check(leaves, source_cells)
        require(accepted == paired == set(range(256)), "legal monomial extension failed actual RS")
        require(passing_leaves == {"outer_col": 64, "inner_row": 256, "inner_col": 512},
                "not all genuine leaves accepted")
        moved = bridge.move_cells(source_cells, forward)
        audit = row_audit(moved, index, bound)
        monomials.append({"exponent": exponent, "expected_binary_weight": bound,
                          "outer_q_adic_weight": outer_weight,
                          "nested_q_adic_weight": inner_weight,
                          "actual_leaf_tests_passed": len(leaves),
                          "paired_RS_accepts": len(paired), **audit})

    return {
        "scope": "all32 legal monomials in the actual fixed two-level GF256 fixture",
        "base_commit": "2a546c3781d71cd159b388997bd5312a7ceb78e6",
        "field_size": 256, "extension_field_size": 65536,
        "root_degree_cutoff_strict": 32, "physical_symbols_per_proof": rs.WORD_COUNT,
        "normalized_symbol_rows": len(index), "physical_raw_bit_rows_per_proof": 1016,
        "monomials_checked": len(monomials), "source_names_checked": names_checked,
        "actual_leaf_checks": 32 * len(leaves),
        "raw_bit_rows_checked": 32 * 1016,
        "raw_bit_truth_values_checked": 32 * 1016 * 256,
        "vector_ANF_coefficients_checked": sum(m["vector_ANF_coefficients_checked"] for m in monomials),
        "fixed_geometry": {
            "outer_low_basis": [1, 2, 4, 8], "inner_low_basis": [1, 2, 4],
            "outer_vanisher_coefficients": q0, "inner_vanisher_coefficients": q1,
            "distinct_outer_full_bases": len(outer_bases),
            "distinct_inner_full_bases": len(inner_bases),
            "distinct_inner_low_spaces": len(inner_low_spaces),
            "normalized_rows_with_affine_point_and_ordinates": geometry_rows_checked},
        "monomials": monomials,
        "limits": [
            "actual predecessor field arithmetic, interpolation, geometry and leaf tests are reused",
            "all-proof degree preservation also needs the written fixed-basis argument or linearity argument",
            "full node bases vary with seed; only the relevant low vanishing spaces are fixed in this fixture",
            "no generic recursive basis dependence claim, Boolean gate degree, NO gap, Lean or novelty claim"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    print(json.dumps(main(args.repo_root), indent=2, sort_keys=True))
