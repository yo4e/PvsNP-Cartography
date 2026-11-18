"""Exact matrix, geometry and interior-count controls for dense masks.

The large examples count binomial interiors only. They do not construct a
2**k-point field, oracle assignment, or all verifier decisions.
"""

import argparse
import importlib.util
import json
from math import comb
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rank(columns):
    pivots = {}
    for value in columns:
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
    return len(pivots)


def apply_columns(columns, value):
    result = 0
    while value:
        least = value & -value
        result ^= columns[least.bit_length() - 1]
        value ^= least
    return result


def rotate_pairs(value, r):
    result = 0
    for shift in range(0, r, 2):
        low = (value >> shift) & 1
        high = (value >> (shift + 1)) & 1
        result |= high << shift
        result |= (low ^ high) << (shift + 1)
    return result


def triples(r):
    require(r % 2 == 0, "paired coordinate count must be even")
    remaining = set(range(1, 1 << r))
    result = []
    while remaining:
        first = min(remaining)
        second = rotate_pairs(first, r)
        third = rotate_pairs(second, r)
        orbit = {first, second, third}
        require(len(orbit) == 3, "a nonzero fixed vector")
        require(rotate_pairs(third, r) == first, "order three")
        require(first ^ second ^ third == 0, "orbit sum")
        require(orbit <= remaining, "overlapping orbits")
        result.append(tuple(sorted(orbit)))
        remaining -= orbit
    return result


def syndrome(rows, value):
    return sum(((row & value).bit_count() % 2) << i
               for i, row in enumerate(rows))


def finite_frame(r, geometry):
    k = (1 << r) - 1
    core = [sum((((x & y).bit_count() % 2) << (x - 1))
                for x in range(1, k + 1))
            for y in range(1, k + 1)]
    masks = [word ^ (1 << i) for i, word in enumerate(core)]
    require(rank(core) == r, "simplex rank")
    require(rank(masks) == k, "mask rank")
    for i in range(k):
        require(apply_columns(core, core[i]) == 0, "nilpotent core")
        require(apply_columns(masks, masks[i]) == (1 << i), "mask involution")
    weights = {word.bit_count() for word in masks}
    distances = {(left ^ right).bit_count()
                 for i, left in enumerate(masks) for right in masks[:i]}
    half = 1 << (r - 1)
    require(weights <= {half - 1, half + 1}, "mask weight range")
    require(min(distances) >= half - 2 and max(distances) <= half + 2,
            "pairwise distance range")
    orbits = triples(r)
    rows = [sum(1 << (x - 1) for x in orbit) for orbit in orbits]
    require(rank(rows) == k // 3, "independent syndrome checks")
    membership = {x: i for i, orbit in enumerate(orbits) for x in orbit}
    for y in range(1, k + 1):
        require(syndrome(rows, core[y - 1]) == 0, "core parity")
        require(syndrome(rows, masks[y - 1]) == (1 << membership[y]), "unit syndrome")
    # B(H+H) contains all syndromes of weight at most two, exactly.
    mask_images = {0} | {syndrome(rows, word) for word in masks}
    double_images = {x ^ y for x in mask_images for y in mask_images}
    require(len(double_images) == 1 + len(rows) + comb(len(rows), 2),
            "double-mask syndrome set")
    K = geometry.base_masks(k, 3)
    base_images = {syndrome(rows, word) for word in K}
    max_base = max(x.bit_count() for x in base_images)
    require(max_base <= 9, "physical base displacement")
    # Independent direct product of the two finite image sets, including the
    # recursive shape result rather than just a Hamming-weight upper bound.
    max_bundle = max((x ^ y).bit_count() for x in base_images for y in double_images)
    require(max_bundle <= 11, "translated physical displacement")
    require(max_bundle == min(len(rows), max_base + 2), "image maximum")
    return {"r": r, "k": k, "mask_count": k + 1, "rank": k,
            "mask_weights": sorted(weights), "pair_distances": sorted(distances),
            "independent_checks": len(rows), "base_overlap_size": len(K),
            "base_syndrome_maximum": max_base, "bundle_syndrome_maximum": max_bundle,
            "one_triple_bias_numerator": k - 5, "one_triple_bias_denominator": k + 1}


def interior_count(n, w):
    require(n > 0 and n % 2 == 1, "majority group must be nonempty and odd")
    low = max(0, (n + 1) // 2 - w)
    high = min(n, (n - 1) // 2 + w)
    term = comb(n, low)
    boundary = 0
    for j in range(low, high + 1):
        boundary += term
        term = term * (n - j) // (j + 1)
    total = 1 << n
    require(0 <= boundary <= total, "boundary probability")
    return total - boundary, total


def check_small_count():
    cases = 0
    for n in (1, 3, 5, 7, 9, 11):
        for w in (0, 1, 2, 3, 6):
            counted, total = interior_count(n, w)
            actual = sum(abs(2*x.bit_count() - n) > 2*w for x in range(1 << n))
            require(counted == actual and total == (1 << n), "binomial enumeration")
            cases += 1
    return cases


def analytic_case(r, a=3):
    k = (1 << r) - 1
    m = k // 3
    n = m // a
    n -= 1 - (n % 2)
    numerator, denominator = interior_count(n, 3*a + 2)
    numerator **= a
    denominator **= a
    scale = 1_000_000
    accepted_ppm = numerator * scale // denominator
    rejection_ppm = ((denominator - numerator)*scale + denominator - 1) // denominator
    # Subtract exactly one potential failure at field input zero for the NO
    # residual. The multiplication by 2**k is symbolic integer accounting.
    no_accepted = max(0, (numerator << k) - denominator)
    no_denominator = denominator << k
    return {"r": r, "k": k, "checks": m, "odd_group_size": n, "w": 3*a + 2,
            "RS_accept_at_least_ppm": accepted_ppm,
            "RS_reject_at_most_ppm": rejection_ppm,
            "NO_joint_accept_at_least_ppm": no_accepted * scale // no_denominator,
            "far_root_distance_numerator": (1 << a) - 1,
            "far_root_distance_denominator": 1 << a}


def main():
    parser = argparse.ArgumentParser()
    default_source = Path(__file__).resolve().parent.parent / "042-accepted-sites" / "check_overlap.py"
    parser.add_argument("--geometry-source", type=Path, default=default_source)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("previous_physical_overlap", args.geometry_source)
    geometry = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(geometry)
    output = {"finite_frames": [finite_frame(r, geometry) for r in (4, 6, 8)],
              "exhaustive_binomial_controls": check_small_count(),
              "analytical_large_cases": [analytic_case(r) for r in (12, 16, 18, 20)]}
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
