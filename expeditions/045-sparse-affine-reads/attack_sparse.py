"""Exact field-level attacks on sparse A predicates; no compiler dependency.

Run from any working directory.  Imports only the pinned Expedition 040 field
geometry and honest shared-cell constructor.  Its GF(128) arithmetic below
is a separate shift/reduce implementation, not the Boolean circuit evaluator.
"""
from itertools import combinations
from pathlib import Path
import json
import sys

OLD = Path(__file__).resolve().parents[1] / "040-recursive-verifier"
sys.path.insert(0, str(OLD))
import recursive_rs as rs
import verify_geometry as ref

N = 128
SPACES = {
    "radius1": tuple(x for x in range(N) if x.bit_count() <= 1),
    "radius2": tuple(x for x in range(N) if x.bit_count() <= 2),
    "radius3": tuple(x for x in range(N) if x.bit_count() <= 3),
    "cross": tuple(sorted(set(range(8)) | set(range(0, N, 8)))),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def mul(x, y):
    """GF(128), polynomial-basis modulus X^7+X+1 (0x83)."""
    require(0 <= x < N and 0 <= y < N, "not a base-field symbol")
    result = 0
    while y:
        if y & 1:
            result ^= x
        y >>= 1
        x <<= 1
        if x & N:
            x ^= 0x83
    return result


def product(values):
    answer = 1
    for value in values:
        answer = mul(answer, value)
    return answer


def residual(a, cells, x, no=True):
    first = product([x ^ t for t in (1, 2, 3)] +
                    [a[x] ^ 1, a[x] ^ 1, a[x ^ int(not no)] ^ 1])
    second = product([x ^ t for t in (0, 2, 3)] + [a[x ^ int(no)]] * 3)
    ranged = product([x, x ^ 1, a[x ^ 2], a[x ^ 2] ^ 1])
    quotient = product([x ^ t for t in (0, 1, 2, 3)] + [cells[x]])
    return first ^ second ^ ranged ^ quotient


def a_passes(a, x, offsets):
    slope = a[x] ^ a[x ^ 1]
    return all(a[x ^ delta] == (a[x] ^ mul(delta, slope)) for delta in offsets)


def b_passes(cells):
    """Second field implementation, absolute points, one global physical table."""
    rows = [ref.degree_below(ref.ROWS[v],
                            [cells[(w // 8) * N + v * 8 + w % 8]
                             for w in range(64)], 8) for v in range(16)]
    cols = [ref.degree_below(ref.COLUMNS,
                            [cells[(4 + c // 8) * N + v * 8 + c % 8]
                             for v in range(16)], 2) for c in range(32)]
    return rows, cols


def evaluate(a, cells, schedule, no=True):
    offsets = SPACES[schedule]
    rows, cols = b_passes(cells)
    a_good = [x for x in range(N) if a_passes(a, x, offsets)]
    accepted = [x for x in a_good
                if rows[x >> 3]
                and all(cols[(x & 7) + 8 * fresh] for fresh in range(4))
                and residual(a, cells, x, no) == 0]
    return {"A_good_count": len(a_good), "passing_B_rows": sum(rows),
            "passing_B_columns": sum(cols), "accepted": accepted,
            "rejected": N - len(accepted)}


def sharp_coefficients(points):
    require(len(points) == 16 and len(set(points)) == 16 and 0 not in points,
            "need sixteen distinct nonzero interpolation sites")
    coeffs = rs.vanishing(points)
    scale = rs.inv(coeffs[0])
    quotient = [rs.mul(c, scale) for c in coeffs[1:]]
    require(all(rs.eval_poly(quotient, x) == ref.inverse(x) for x in points),
            "reciprocal interpolation failed")
    return quotient


RADIUS2_POINTS = (5, 6, 7, 9, 10, 11, 15, 17, 18, 19, 23, 27, 33, 34, 35, 39)


def fixtures():
    """Public API: each value is (A[128], shared_B_cells[1024])."""
    sharp = rs.honest_cells(sharp_coefficients(tuple(range(4, 20))))
    one = [0] * N
    for delta in SPACES["radius1"]:
        y = 96 ^ delta
        one[y] = mul(100, y)
    packed = [0] * N
    occupied = set()
    for x, slope in ((96, 100), (117, 92), (122, 98)):
        star = {x ^ delta for delta in SPACES["radius1"]}
        require(not (star & occupied), "packed stars overlap")
        occupied |= star
        for y in star:
            packed[y] = mul(slope, y)
    wide = [1 ^ mul(121, y) if (124 ^ y).bit_count() <= 2 else 0
            for y in range(N)]
    wide_cells = rs.honest_cells(sharp_coefficients(RADIUS2_POINTS))
    return {"old_sharp": ([0] * N, sharp),
            "radius1_one_star": (one, sharp),
            "radius1_three_stars": (packed, sharp),
            "radius2_one_star": (wide, wide_cells)}


def run():
    require(all(mul(x, y) == rs.BASE_MUL[x][y]
                for x in range(N) for y in range(N)), "field mismatch")
    results = {}
    for name, (a, cells) in fixtures().items():
        results[name] = {schedule: evaluate(a, cells, schedule)
                         for schedule in SPACES}
        results[name]["A_nonzero"] = [[x, value] for x, value in enumerate(a) if value]
        require(all(result["passing_B_rows"] == 16 and result["passing_B_columns"] == 32
                    for key, result in results[name].items() if key in SPACES),
                "dishonest or inconsistent B extension")
    require(results["radius1_one_star"]["radius1"]["accepted"] == list(range(1, 20)) + [96],
            "lost single-star counterexample")
    require(results["radius1_three_stars"]["radius1"]["accepted"] ==
            list(range(1, 20)) + [96, 117, 122], "lost packed counterexample")
    require(results["radius2_one_star"]["radius2"]["accepted"] ==
            sorted([1, 2, 3, 124] + list(RADIUS2_POINTS)), "lost radius-two counterexample")
    require(all(results["old_sharp"][name]["rejected"] == 109 for name in SPACES),
            "old affine extremizer changed")

    cross = set(SPACES["cross"])
    overlap_histogram = {}
    for h in range(1, N):
        low, high = h & 7, h & ~7
        intersection = cross & {h ^ d for d in cross}
        require(low != high and {low, high} <= intersection, "cross intersection broke")
        overlap_histogram[len(intersection)] = overlap_histogram.get(len(intersection), 0) + 1
    require(overlap_histogram == {8: 7, 16: 15, 2: 105}, "wrong overlap census")

    # Removing the high basis direction leaves two unrelated affine pieces.
    restricted = tuple(sorted(set(range(8)) | set(range(0, 64, 8))))
    nonaffine = [int(x >= 64) for x in range(N)]
    require(all(a_passes(nonaffine, x, restricted) for x in range(N)),
            "dropped-direction counterexample failed")
    require(not ref.degree_below(tuple(range(N)), nonaffine, 2),
            "counterexample accidentally affine")
    require(not any(a_passes(nonaffine, x, SPACES["cross"]) for x in range(N)),
            "full cross did not catch high-coordinate split")
    results["cross_pair_overlap"] = {
        "differences_checked": 127, "distinct_offsets": len(cross),
        "intersection_size_histogram": overlap_histogram}
    results["dropped_high_direction"] = {
        "offsets": list(restricted), "A_definition": "indicator of bit 6",
        "restricted_A_accepted": 128, "full_cross_A_accepted": 0,
        "scope": "membership counterexample only, not a joined NO soundness witness"}
    results["radius2_B_coefficients"] = sharp_coefficients(RADIUS2_POINTS)
    results["search_scope"] = {
        "radius1_eligible_centers": [x for x in range(N)
            if min((x ^ y).bit_count() for y in range(1, 20)) >= 3],
        "selected_packing": [96, 117, 122],
        "radius2_selected_center": 124,
        "radius2_interpolation_points": list(RADIUS2_POINTS),
        "scope": "explicit witnesses; no optimization of the true radius1/radius2 NO minimum"}
    return results


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
