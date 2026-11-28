#!/usr/bin/env python3
"""Transport the actual Expedition041 two-level field oracle through normalization.

The old field arithmetic and leaf tests are reused, explicitly not claimed as
an independently reconstructed agreement theorem or Boolean clause compiler.
"""

import argparse
from collections import Counter
from importlib import util
import json
from pathlib import Path
import sys

import check_recursive_normalization as norm


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_module(name, path):
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def canonical_outer_name(layout, v, w):
    if w < 16:
        return layout.encode_concrete([], (v << 4) | w, 8)
    return layout.encode_concrete([("R", v, 4)], w, 7)


def canonical_inner_name(layout, v, j, i):
    if i < 8:
        return canonical_outer_name(layout, v, (j << 3) | i)
    return layout.encode_concrete([("R", v, 4), ("R", j, 4)], i, 6)


def source_transport(layout, index, rs):
    """Old16384-address source layout -> normalized64 rows ×256 coordinates."""
    forward = {}
    canonical = {}
    checked_names = 0
    def record(old, source_name):
        nonlocal checked_names
        new = norm.pack_address(layout, source_name, index)
        require(old not in forward or forward[old] == new, "shared source alias maps inconsistently")
        require(old not in canonical or canonical[old] == source_name, "shared source name is not canonical")
        forward[old] = new
        canonical[old] = source_name
        checked_names += 1
    for v in range(16):
        for w in range(128):
            record(rs.outer_cell(v, w), canonical_outer_name(layout, v, w))
        for j in range(16):
            for i in range(64):
                record(rs.inner_cell(v, j, i), canonical_inner_name(layout, v, j, i))
    require(set(forward) == set(range(rs.WORD_COUNT)), "source physical universe not covered")
    require(set(forward.values()) == set(range(rs.WORD_COUNT)), "normalized transport not a bijection")
    require(all(forward[x] == x for x in range(2048)), "root/outer extension geometry changed unexpectedly")
    return forward, checked_names


def move_cells(cells, forward):
    result = [None] * len(cells)
    for old, new in forward.items():
        result[new] = cells[old]
    require(all(value is not None for value in result), "incomplete transported physical proof")
    return result


def boolean_row_audit(symbol_rows, widths):
    """Exact ANFs and GF(2) span of all named physical bit rows."""
    histogram = Counter()
    distinct = set()
    echelon = {}
    row_count = 0
    for values, width in zip(symbol_rows, widths):
        require(len(values) == 256, "wrong literal-row seed length")
        for bit in range(width):
            table = [(value >> bit) & 1 for value in values]
            for j in range(8):
                for mask in range(256):
                    if mask >> j & 1:
                        table[mask] ^= table[mask ^ (1 << j)]
            degree = max((mask.bit_count() for mask, value in enumerate(table) if value), default=-1)
            histogram[degree] += 1
            coefficients = sum(value << mask for mask, value in enumerate(table))
            distinct.add(coefficients)
            x = coefficients
            while x:
                pivot = x.bit_length() - 1
                if pivot not in echelon:
                    echelon[pivot] = x
                    break
                x ^= echelon[pivot]
            row_count += 1
    return {"physical_bit_rows": row_count,
            "seed_degree_histogram": {str(d): n for d, n in sorted(histogram.items())},
            "maximum_seed_degree": max(histogram), "distinct_ANF_vectors": len(distinct),
            "GF2_row_span_dimension": len(echelon),
            "scope": "these fixed physical proofs only; a public symbolic dictionary is not inferred"}


def main(repo_root):
    repo_root = Path(repo_root)
    g = norm.load_geometry(repo_root)
    layout = g.Layout(8, 3, 2)
    index = norm.row_index(layout)
    path = repo_root / "expeditions/041-two-level-distance"
    rs = load_module("two_level_oracle", path / "two_level_oracle.py")
    outer = load_module("actual_outer_application", path / "check_outer_application.py")
    forward, checked_names = source_transport(layout, index, rs)
    leaves = rs.geometry()
    moved_leaves = {key: rs.Leaf(tuple(forward[a] for a in leaf.addresses), leaf.points, leaf.cutoff)
                    for key, leaf in leaves.items()}
    nodes = list(range(4, 36))
    u = outer.vanishing_coefficients(nodes)
    scale = next(x for x in range(256) if outer.base_product(x, u[0]) == 1)
    b_coeffs = [outer.base_product(scale, c) for c in u[1:]]
    require(len(b_coeffs) == 32 and b_coeffs[-1] != 0, "wrong extremal polynomial degree")
    b_no = [outer.evaluate(b_coeffs, x) for x in range(256)]
    c_yes = outer.physical_extension(list(range(256)), leaves)
    c_no = outer.physical_extension(b_no, leaves)
    c_noncode = c_no.copy()
    c_noncode[48] ^= 1
    fixtures = [
        ("YES", [x ^ 1 for x in range(256)], c_yes, False, set(range(256))),
        ("NO_extremizer", [0] * 256, c_no, True, set(range(1, 36))),
        ("NO_noncode_at_48", [0] * 256, c_noncode, True, set(range(1, 36))),
    ]
    reports = {}
    checked_leaf_values = checked_field_reads = 0
    for name, a, cells, no, expected in fixtures:
        moved = move_cells(cells, forward)
        require(moved[:256] == cells[:256], "physical root not shared with residual")
        for key, leaf in leaves.items():
            moved_leaf = moved_leaves[key]
            before = [cells[q] for q in leaf.addresses]
            after = [moved[q] for q in moved_leaf.addresses]
            require(before == after, "actual leaf's ordered symbol sequence changed")
            checked_field_reads += len(before)
        old_accepts, old_paired, old_counts = rs.run_check(leaves, cells)
        new_accepts, new_paired, new_counts = rs.run_check(moved_leaves, moved)
        require((old_accepts, old_paired, old_counts) == (new_accepts, new_paired, new_counts), "field verdict transport failed")
        checked_leaf_values += len(leaves)
        residual_before = [outer.residual(a, cells, x, no) for x in range(256)]
        residual_after = [outer.residual(a, moved, x, no) for x in range(256)]
        require(residual_before == residual_after, "actual ACSP residual changed")
        residual_pass = {x for x, value in enumerate(residual_after) if value == 0}
        require(outer.affine_root(a), "A is not affine")
        joint = residual_pass & new_paired
        require(joint == expected, "residual-constrained expected fixture fails")
        reports[name] = {"root_residual_accepts": len(residual_pass),
                         "unpaired_RS_accepts": len(new_accepts), "paired_RS_accepts": len(new_paired),
                         "joint_accepts": len(joint), "joint_rejects": 256 - len(joint),
                         "passing_leaves": new_counts,
                         "B_raw_bit_rows": boolean_row_audit(
                             [moved[row * 256:(row + 1) * 256] for row in range(len(index))],
                             [8] + [16] * (len(index) - 1)),
                         "A_raw_bit_rows": boolean_row_audit([a], [8])}
    return {
        "scope": "actual two-level GF(256) residual-constrained Expedition041 fixtures, reindexed",
        "field_size": 256, "extension_symbol_bits": 16, "root_symbol_bits": 8,
        "source_physical_symbols": rs.WORD_COUNT, "normalized_rows": len(index),
        "source_names_checked_including_aliases": checked_names,
        "actual_leaf_tests_per_fixture": len(leaves), "fixture_leaf_verdict_controls": checked_leaf_values,
        "ordered_field_values_compared": checked_field_reads,
        "physical_transport_bijection": True, "ACSP_and_RS_share_same_root": True,
        "fixtures": reports,
        "limits": ["uses the existing field arithmetic, interpolation and acceptance implementation",
                   "exact all-assignment transport follows from the address bijection, not these fixtures",
                   "221 is inherited from the separate Expedition041 field-symbol argument",
                   "no Boolean gate/template census or signed-error precision newly established",
                   "no Lean acceptance, source theorem reconstruction or novelty claim"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    print(json.dumps(main(args.repo_root), indent=2, sort_keys=True))
