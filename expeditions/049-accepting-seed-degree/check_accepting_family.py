#!/usr/bin/env python3
"""Three genuinely residual-constrained accepting two-level field proofs.

The residual is NEW. The GF(256) two-level physical geometry and interpolation
implementation are reused from Expeditions041/048. No Boolean compiler or
221-rejection bound is asserted for the new YES relation.
"""

import argparse
from importlib import util
import json
from pathlib import Path
import sys

# All imported predecessor code is read-only during this standalone check.
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
    p = list(poly)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [0]


def poly_add(*polys):
    result = [0] * max(map(len, polys))
    for poly in polys:
        for i, coefficient in enumerate(poly):
            result[i] ^= coefficient
    return trim(result)


def poly_mul(left, right, mul):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] ^= mul(a, b)
    return trim(result)


def poly_div_monic(numerator, denominator, mul):
    require(denominator[-1] == 1, "divisor not monic")
    remainder = trim(numerator)
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    while remainder != [0] and len(remainder) >= len(denominator):
        power = len(remainder) - len(denominator)
        leading = remainder[-1]
        quotient[power] = leading
        for i, coefficient in enumerate(denominator):
            remainder[i + power] ^= mul(leading, coefficient)
        remainder = trim(remainder)
    return trim(quotient), remainder


def evaluate(poly, x, mul):
    result = 0
    for coefficient in reversed(poly):
        result = mul(result, x) ^ coefficient
    return result


def scalar_numerator(a, x, mul):
    t0 = mul(mul(x ^ 1, x ^ 2), x ^ 3)
    first = mul(t0, mul(mul(a[x] ^ 1, a[x] ^ 1), a[x ^ 1] ^ 1))
    boolean = mul(mul(x, x ^ 1), mul(a[x ^ 2], a[x ^ 2] ^ 1))
    return first ^ boolean


def numerator_polynomial(constant, slope, t0, mul):
    a_plus_one = [constant ^ 1, slope]
    a_shift_one_plus_one = [constant ^ slope ^ 1, slope]
    first = poly_mul(t0, poly_mul(poly_mul(a_plus_one, a_plus_one, mul), a_shift_one_plus_one, mul), mul)
    a_shift_two = [constant ^ mul(slope, 2), slope]
    second = poly_mul([0, 1, 1], poly_mul(a_shift_two, poly_add(a_shift_two, [1]), mul), mul)
    return poly_add(first, second)


def main(repo_root):
    repo_root = Path(repo_root)
    p041 = repo_root / "expeditions/041-two-level-distance"
    p048 = repo_root / "expeditions/048-recursive-row-normalization"
    normal = load("check_recursive_normalization", p048 / "check_recursive_normalization.py")
    bridge = load("actual_recursive_field_bridge", p048 / "check_recursive_field_bridge.py")
    rs = load("two_level_oracle", p041 / "two_level_oracle.py")
    old_outer = load("actual_outer_application", p041 / "check_outer_application.py")
    mul = lambda a, b: rs.BASE[a][b]
    t0 = old_outer.vanishing_coefficients((1, 2, 3))
    zpoly = old_outer.vanishing_coefficients((0, 1, 2, 3))
    require(t0 == [6, 7, 0, 1] and zpoly == [0, 6, 7, 0, 1], "selector polynomial mismatch")
    zvalues = [evaluate(zpoly, x, mul) for x in range(256)]
    require({x for x, value in enumerate(zvalues) if value == 0} == {0, 1, 2, 3}, "wrong vanishing set")

    # Every affine A is uniquely determined by (A(0),A(1)). H endpoints
    # evaluate to (6*(A0+1)^2*(A1+1), 0, 6*A0*(A0+1), 6*A1*(A1+1)).
    accepted_pairs = []
    boolean_pairs = []
    endpoint_cases = 0
    for a0 in range(256):
        for a1 in range(256):
            conditions = (mul(6, mul(mul(a0 ^ 1, a0 ^ 1), a1 ^ 1)), 0,
                          mul(6, mul(a0, a0 ^ 1)), mul(6, mul(a1, a1 ^ 1)))
            if conditions[2:] == (0, 0):
                boolean_pairs.append((a0, a1))
            if not any(conditions):
                accepted_pairs.append((a0, a1))
            endpoint_cases += 1
    require(boolean_pairs == [(0, 0), (0, 1), (1, 0), (1, 1)], "Boolean restriction changed")
    require(accepted_pairs == [(0, 1), (1, 0), (1, 1)], "not exactly the OR witnesses")

    leaves = rs.geometry()
    g = normal.load_geometry(repo_root)
    layout = g.Layout(8, 3, 2)
    index = normal.row_index(layout)
    forward, names_checked = bridge.source_transport(layout, index, rs)
    moved_leaves = {key: rs.Leaf(tuple(forward[q] for q in leaf.addresses), leaf.points, leaf.cutoff)
                    for key, leaf in leaves.items()}
    require(len(leaves) == 832 and len(index) == 64, "unexpected actual recursive geometry")
    selected_union = set().union(*(rs.selected(x) for x in range(256)))
    require(selected_union == set(leaves), "full seed acceptance does not cover every leaf")
    expected = {(0, 1): ("A=X", [0, 0, 1]),
                (1, 0): ("A=1+X", [1, 1, 1]),
                (1, 1): ("A=1", [0])}
    reports = {}
    saved = {}
    for a0, a1 in accepted_pairs:
        constant, slope = a0, a0 ^ a1
        name, expected_b = expected[a0, a1]
        a = [constant ^ mul(slope, x) for x in range(256)]
        numerator = numerator_polynomial(constant, slope, t0, mul)
        b_coefficients, remainder = poly_div_monic(numerator, zpoly, mul)
        require(remainder == [0] and b_coefficients == expected_b, "forced quotient mismatch")
        b = [evaluate(b_coefficients, x, mul) for x in range(256)]
        require(old_outer.affine_root(a), "A failed direct affine check")
        for x in range(256):
            scalar = scalar_numerator(a, x, mul)
            require(scalar == evaluate(numerator, x, mul), "symbolic and scalar numerator disagree")
            require(scalar ^ mul(zvalues[x], b[x]) == 0, "new residual does not vanish")
        cells = old_outer.physical_extension(b, leaves)
        moved = bridge.move_cells(cells, forward)
        old_pass, old_paired, old_counts = rs.run_check(leaves, cells)
        new_pass, new_paired, new_counts = rs.run_check(moved_leaves, moved)
        require(old_pass == old_paired == new_pass == new_paired == set(range(256)), "actual shared RS test failed")
        require(old_counts == new_counts == {"outer_col": 64, "inner_row": 256, "inner_col": 512}, "wrong passing leaves")
        require(moved[:256] == b, "ACSP and proximity no longer share one root")
        b_rows = bridge.boolean_row_audit(
            [moved[row * 256:(row + 1) * 256] for row in range(len(index))],
            [8] + [16] * (len(index) - 1))
        a_rows = bridge.boolean_row_audit([a], [8])
        require(b_rows["maximum_seed_degree"] <= 1 and a_rows["maximum_seed_degree"] <= 1,
                "an accepting raw row unexpectedly nonaffine")
        reports[name] = {"A0": a0, "A1": a1, "A_coefficients": [constant, slope],
                         "numerator_coefficients": numerator, "B_coefficients": b_coefficients,
                         "new_residual_accepts": 256, "paired_RS_accepts": len(new_paired),
                         "joint_accepts": 256, "joint_rejects": 0,
                         "A_raw_rows": a_rows, "B_raw_rows": b_rows}
        saved[name] = (a, cells, moved)

    # The four vanishing-factor sites do not determine B from the residual.
    # A wrong root at 0 is invisible to that residual and exposed by shared RS.
    a, cells, moved = saved["A=X"]
    damaged = moved.copy()
    damaged[0] ^= 1
    residual_damaged = [scalar_numerator(a, x, mul) ^ mul(zvalues[x], damaged[x]) for x in range(256)]
    require(not any(residual_damaged), "masked-site damage should be residual-invisible")
    unpaired, paired, counts = rs.run_check(moved_leaves, damaged)
    require(len(unpaired) == 248 and len(paired) == 240, "masked-site shared RS control changed")

    # Pointwise quotient is not the polynomial quotient: A=0 and B(x)=1/x
    # makes the residual vanish at 255 seeds but violates the RS code.
    a0 = [0] * 256
    reciprocal = [0] + list(rs.BASE_INV[1:])
    reciprocal_cells = old_outer.physical_extension(reciprocal, leaves)
    reciprocal_moved = bridge.move_cells(reciprocal_cells, forward)
    reciprocal_residual = {x for x in range(256)
                           if scalar_numerator(a0, x, mul) ^ mul(zvalues[x], reciprocal_moved[x]) == 0}
    reciprocal_pass, reciprocal_paired, reciprocal_counts = rs.run_check(moved_leaves, reciprocal_moved)
    require(reciprocal_residual == set(range(1, 256)), "reciprocal residual control changed")
    require(reciprocal_paired != set(range(256)), "noncode pointwise quotient unexpectedly accepted")

    return {
        "scope": "new residual-constrained YES relation with exactly three fully accepting used field proofs",
        "base_commit": "2a546c3781d71cd159b388997bd5312a7ceb78e6",
        "field_size": 256, "rate_exponent_B": 3, "recursive_B_depth": 2,
        "A_degree_cutoff_strict": 2, "B_degree_cutoff_strict": 32,
        "physical_B_symbols": rs.WORD_COUNT, "physical_B_raw_bit_rows": 1016,
        "physical_A_symbols": 256, "physical_A_raw_bit_rows": 8,
        "physical_names_checked": names_checked, "actual_leaf_tests_per_proof": len(leaves),
        "affine_endpoint_pairs_enumerated": endpoint_cases,
        "Boolean_pairs_after_range_constraints": [list(p) for p in boolean_pairs],
        "accepting_pairs": [list(p) for p in accepted_pairs], "fully_accepting_field_proof_count": 3,
        "witnesses": reports,
        "masked_root_error_control": {"reference": "A=X", "changed_root": 0,
                                      "new_residual_accepts": 256, "unpaired_RS_accepts": len(unpaired),
                                      "paired_RS_accepts": len(paired), "joint_rejects": 256 - len(paired),
                                      "passing_leaves": counts},
        "pointwise_quotient_control": {"A": "0", "B": "0 at0, reciprocal elsewhere",
                                       "new_residual_accepts": len(reciprocal_residual),
                                       "unpaired_RS_accepts": len(reciprocal_pass),
                                       "paired_RS_accepts": len(reciprocal_paired),
                                       "joint_accepts": len(reciprocal_residual & reciprocal_paired),
                                       "passing_leaves": reciprocal_counts},
        "limits": ["all-proof classification uses the separate written degree/RS uniqueness argument",
                   "raw row degrees do not include a Boolean compiler's internal gates",
                   "affine A and low-degree residual force quadratic B, an intentionally easy witness family",
                   "no new NO gap; predecessor221 is not transported to this new residual",
                   "no Lean acceptance, novelty, external review or complexity-class separation"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    print(json.dumps(main(args.repo_root), indent=2, sort_keys=True))
