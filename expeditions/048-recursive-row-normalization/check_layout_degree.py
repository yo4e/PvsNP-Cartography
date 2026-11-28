#!/usr/bin/env python3
"""Exact controls on the k=8, a=3 normalized recursive address cube.

This is a geometry/representation test. The artificial bit assignment used in
the degree certificates is NOT claimed to satisfy the Reed--Solomon or ACSP
constraints. All checks survive python -O; no random search is performed.
"""
from collections import Counter
from importlib import util
import json
from pathlib import Path
import sys


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def import_file(name, path):
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def repository_root():
    for parent in Path(__file__).resolve().parents:
        if (parent / "AGENTS.md").is_file():
            return parent
    raise RuntimeError("run this file within the repository snapshot")


def coefficients(values):
    answer = list(values)
    size = len(answer)
    require(size and size & (size - 1) == 0, "non-cube truth table")
    for j in range(size.bit_length() - 1):
        step = 1 << j
        for mask in range(size):
            if mask & step:
                answer[mask] ^= answer[mask ^ step]
    return answer


def degree(values):
    return max((mask.bit_count() for mask, value in enumerate(coefficients(values))
                if value), default=0)


def parity(values):
    result = 0
    for value in values:
        result ^= value
    return result


def main():
    repo = repository_root()
    normal = import_file("recursive_normalization", Path(__file__).with_name("check_recursive_normalization.py"))
    g = normal.load_geometry(repo)
    k, a, n = 8, 3, 256
    layout = g.Layout(k, a, 2)
    row_index = normal.row_index(layout)
    row_count = len(row_index)
    b = (row_count - 1).bit_length()
    require(row_count == 64 and b == 6, "unexpected recursive row universe")

    # A permutation of the ENTIRE normalized cube, not a row-only relabeling.
    # Its inverse is itself. The same seed-dependent tag change is used globally.
    # Seven binary ANDs and one XOR suffice; this is a construction count, not a
    # claim that all other possible circuits for the map are larger.
    def shear(address):
        root = address & (n - 1)
        return address ^ (int(root == n - 1) << k)

    universe = n * row_count
    images = [shear(address) for address in range(universe)]
    require(len(set(images)) == universe, "global shear collides")
    require(all(shear(shear(address)) == address for address in range(universe)),
            "global shear inverse law")
    pullback = [(shear(address) >> k) & 1 for address in range(universe)]
    require(degree(pullback) == k, "linear output did not acquire degree k")
    # This is an actual depth-two RR query with zero fresh tape and offset.
    original = [g.direct(layout, ("R", "R"), 0, seed, 0, "relative")
                for seed in range(n)]
    packed = [normal.pack_address(layout, address, row_index) for address in original]
    require(packed == list(range(n)), "RR root-return query is not normalized identity")
    query_values = [pullback[address] for address in packed]
    require(degree(query_values) == 8 and sum(query_values) == 1,
            "actual query shear-degree control")

    # A proof bit on just one complete physical transverse row is AND_4.
    # The remaining four root coordinates repeat each value sixteen times.
    def and4(root):
        return int(root & 15 == 15)

    dense = [int(address >> k == 0) * and4(address & (n - 1))
             for address in range(universe)]
    dense_degree = degree(dense)
    row_degrees = Counter(degree(dense[row * n:(row + 1) * n])
                          for row in range(row_count))
    require(dense_degree == 10 and dict(row_degrees) == {4: 1, 0: 63},
            "dense/row degree mismatch")

    # Labels (value-selector, within-class rank) use seven tag bits. The
    # completion on unqueried labels is chosen by this degree-five polynomial.
    labels = [1] + [2 * rank for rank in range(row_count - 1)]
    t = 7
    require(len(set(labels)) == row_count and max(labels) < 1 << t,
            "adaptive labels are not injective")
    completed = [((address >> k) & 1) * and4(address & (n - 1))
                 for address in range(n << t)]
    require(degree(completed) == 5, "adaptive completion degree")
    transported = [(labels[row] << k) | root
                   for row in range(row_count) for root in range(n)]
    require(all(dense[old] == completed[new] for old, new in enumerate(transported)),
            "adaptive labels changed physical bits")

    # Sixteen disjoint 10-dimensional subcubes in the completely used dense
    # layout have odd parity. Any degree<=9 approximant has >=16 raw errors.
    dense_cubes = []
    for high in range(16):
        cube = [(row << k) | (high << 4) | low
                for row in range(row_count) for low in range(16)]
        require(len(cube) == 1 << 10 and parity(dense[x] for x in cube) == 1,
                "dense odd-cube certificate")
        dense_cubes.append(set(cube))
    require(len(set.union(*dense_cubes)) == universe,
            "dense certificates overlap or omit cells")

    # In ANY injective tag layout the two selected full rows span an affine
    # 5-cube (one direction between their tag vectors, four low seed bits).
    # Its two slices are AND_4 and zero, so parity is odd regardless of padding.
    # Enumerate every unordered pair of distinct 7-bit labels and the sixteen
    # disjoint high-seed sections; the generic affine-cube proof is in the notes.
    pair_certificates = 0
    for left in range(1 << t):
        for right in range(left + 1, 1 << t):
            require(left ^ right, "zero tag direction")
            for high in range(16):
                addresses = [(tag << k) | (high << 4) | low
                             for tag in (left, right) for low in range(16)]
                values = [and4(low) if tag == left else 0
                          for tag in (left, right) for low in range(16)]
                require(len(set(addresses)) == 32 and parity(values) == 1,
                        "two-row affine-cube certificate")
                pair_certificates += 1

    # The zero polynomial has exactly sixteen errors in either representation.
    require(sum(dense) == 16, "upper witness at error budget sixteen")
    padded_zero = [0] * len(completed)
    for old, new in enumerate(transported):
        padded_zero[new] = dense[old]
    padding_errors = sum(x != y for x, y in zip(completed, padded_zero))
    require(padding_errors == 1008, "free-padding caveat changed")
    require(degree(padded_zero) == 11, "zero-filled sparse-layout degree")

    # Error preservation is a bijection on used cells, independent of values.
    error_sites = {0, 15, 255, 256, 16383}
    damaged = list(completed)
    for old in error_sites:
        damaged[transported[old]] ^= 1
    after = {old for old, new in enumerate(transported) if dense[old] != damaged[new]}
    require(after == error_sites, "raw physical error set changed")

    return {
        "scope": "one bit per actual canonical symbol cell; artificial assignment, not an RS witness",
        "geometry": {"k": k, "a": a, "depth": layout.depth,
                     "physical_rows": row_count, "physical_cells": universe},
        "general_succinct_map_counterexample": {
            "map": "first tag bit XOR AND of all eight root-coordinate bits",
            "binary_AND_gates_in_displayed_circuit": 7, "XOR_gates": 1,
            "permutation_checks": universe, "inverse_checks": universe,
            "encoded_polynomial_degree": 1, "global_pullback_degree": 8,
            "actual_query": {"route": "RR", "fresh_tape": 0, "offset": 0,
                             "pullback_degree": 8, "nonzero_seeds": 1}},
        "layout_degree_control": {
            "row_degree_histogram": dict(sorted(row_degrees.items())),
            "dense_tag_bits": b, "dense_exact_degree": dense_degree,
            "adaptive_tag_bits": t, "adaptive_free_padding_exact_degree": 5,
            "used_cell_matches": universe,
            "dense_disjoint_odd_cubes": len(dense_cubes),
            "dense_odd_cube_dimension": 10,
            "distinct_tag_pairs_checked": ((1 << t) * ((1 << t) - 1)) // 2,
            "pair_section_odd_certificates": pair_certificates,
            "error_budget_up_to_15": {"minimum_dense_degree": 10,
                                      "minimum_over_all_injective_tag_layouts_with_free_padding": 5,
                                      "minimum_maximum_row_degree": 4},
            "error_budget_16": {"zero_polynomial_errors": 16, "minimum_degree": 0},
            "padding_warning": {"free_completion_cube": n << t,
                                "zero_filled_exact_degree": 11,
                                "degree_five_errors_against_zero_filled_target": padding_errors},
            "transported_error_sites": sorted(after)}
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
