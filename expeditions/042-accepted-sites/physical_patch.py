"""Replay patched transcripts on Expedition 041's physical GF(256) checker."""
from functools import cache
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "041-two-level-distance"))
import check_outer_application as acsp
import two_level_oracle as rs


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def translated(accepted, masks):
    return {z for z in range(256) if all((z ^ h) in accepted for h in masks)}


def reciprocal_extension(nodes, leaves):
    # (V(X)/V(0) + 1)/X interpolates 1/x on the nonzero roots of V.
    polynomial = acsp.vanishing_coefficients(nodes)
    require(polynomial[0] and len(nodes) == len(set(nodes)) == 32, "bad nodes")
    scale = rs.BASE_INV[polynomial[0]]
    coefficients = [acsp.base_product(scale, c) for c in polynomial[1:]]
    values = [acsp.evaluate(coefficients, x) for x in range(256)]
    require(all(acsp.base_product(x, values[x]) == 1 for x in nodes), "reciprocal")
    cells = acsp.physical_extension(values, leaves)
    require(len(rs.run_check(leaves, cells)[0]) == 256, "honest extension failed")
    return cells


def physical():
    leaves = rs.geometry()
    views = [{z} | {i for key in rs.selected(z) for i in leaves[key].addresses}
             for z in range(256)]
    marked = views[0]
    one_patch = [int(i in marked) for i in range(rs.WORD_COUNT)]
    pure, _, _ = rs.run_check(leaves, one_patch)
    zero_sites = {z for z in range(256) if views[z].isdisjoint(marked)}
    require(len(zero_sites) == 120 and pure == zero_sites | {0}, "constant splice")
    require(sum(one_patch[z] for z in pure) == 1, "accepted values")
    require(len(zero_sites) >= 32, "polynomial root certificate")
    root_ones = sum(one_patch[:256])
    # Any nonzero polynomial matches at most 31 zero entries and all root ones.
    require(31 + root_ones < 256 - root_ones, "nearest word certificate")

    centers = [z for z in range(256) if 1 <= (z >> 4) <= 4 and z & 8]
    patch = set.union(*(views[z] for z in centers))
    untouched = {z for z in range(256) if views[z].isdisjoint(patch)}
    require({1, 2, 3} <= untouched, "forced roots touched")
    anchors = sorted(untouched - {0, 1, 2, 3})[:32]
    outside = reciprocal_extension(anchors, leaves)
    inside = reciprocal_extension(centers, leaves)
    cells = [inside[i] if i in patch else x for i, x in enumerate(outside)]
    passes, _, _ = rs.run_check(leaves, cells)
    zero_a = [0] * 256
    residual = {x for x in range(256) if acsp.residual(zero_a, cells, x, True) == 0}
    simplified = {x for x in range(256) if x in (1, 2, 3)
                  or acsp.base_product(x, cells[x]) == 1}
    expected = set(anchors) | set(centers) | {1, 2, 3}
    require(residual == simplified and passes & residual == expected, "joint sites")
    counts = {}
    for masks in [(0,), (0, 1), (0, 9), (0, 16)]:
        actual = translated(passes, masks) & residual
        if masks in [(0,), (0, 1)]:
            require(actual == expected and len(actual) == 67, "67-site witness")
        if masks == (0, 9):
            require(not actual, "paired positive control")
        counts[",".join(map(str, masks))] = len(actual)
    return {
        "constant_patch": {"physical_cells_marked": len(marked), "accepted_zeros": len(zero_sites),
                           "accepted_ones": 1, "exact_root_distance_in_symbols": root_ones},
        "outer_patch": {"physical_cells_marked": len(patch), "total_cells": len(cells),
                        "external_sites": 256, "degree_cutoff_exclusive": 32,
                        "honest_NO_root_cap": 35, "RS_only_accepts": len(passes),
                        "residual_only_accepts": len(residual), "joint_accepts_by_XOR_masks": counts,
                        "center_sites": centers, "untouched_interpolation_sites": anchors}}


def large_example():
    @cache
    def reads(d):
        if d <= 6:
            return 2 ** d
        return 8 * reads(d // 2 + 3) + 4 * reads(d - d // 2)

    n = 2 ** 64
    degree = n // 8
    slots = 1 + 4 * reads(64)
    centers = min(degree, n - 3 * slots**2 - 1, (n - degree - 4) // slots**2)
    require(centers == 278 and reads(64) == 60231680, "symbolic cost checkpoint")
    return {"scope": "recurrence and integer bound only", "k": 64, "a": 3,
            "single_call_slots": reads(64), "augmented_four_call_slots": slots,
            "certified_extra_joint_acceptances": centers}


if __name__ == "__main__":
    print(json.dumps({"finite_replay": physical(), "symbolic_budget": large_example()},
                     indent=2, sort_keys=True))
