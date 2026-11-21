"""Check the cross-shaped additive difference cover behind the affine test.

This checks finite group geometry, not the all-field-proof NO theorem or a
Boolean compiler census.  Those follow from the separately written arguments.
"""
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def cross(a):
    s = 1 << a
    n = 2 * s * s
    return n, set(range(s)) | set(range(0, n, s))


def check(a):
    s = 1 << a
    n, offsets = cross(a)
    require(len(offsets) == 3 * s - 1, "wrong cross size")
    require({0, 1, 2} <= offsets, "outer read missing")
    histogram = {}
    for h in range(1, n):
        lo, hi = h & (s - 1), h & ~(s - 1)
        require(lo in offsets and hi in offsets and lo != hi, "invalid decomposition")
        overlap = offsets & {h ^ d for d in offsets}
        require(lo in overlap and hi in overlap, "two-point overlap lost")
        expected = 2 if lo and hi else s if lo else 2 * s
        require(len(overlap) == expected, "incorrect overlap size")
        histogram[str(len(overlap))] = histogram.get(str(len(overlap)), 0) + 1
    pairs = 0
    if a == 3:
        for x in range(n):
            for y in range(x + 1, n):
                h = x ^ y
                lo, hi = h & (s - 1), h & ~(s - 1)
                first, second = x ^ lo, x ^ hi
                left, right = {x ^ d for d in offsets}, {y ^ d for d in offsets}
                require(first != second and {first, second} <= left & right,
                        "absolute star pair has no certified intersection")
                pairs += 1
    return {"a": a, "dimension": 2 * a + 1, "N": n,
            "distinct_A_maps": len(offsets), "outer_offsets_present": [0, 1, 2],
            "nonzero_shifts_checked": n - 1, "overlap_histogram": histogram,
            "absolute_pairs_checked": pairs,
            "minimum_two_star_intersection": 2}


def main():
    n, offsets = cross(3)
    broken = offsets - {8}
    missing = [h for h in range(1, n)
               if not (broken & {h ^ d for d in broken})]
    require(missing, "deleted-offset mutant unexpectedly covers the field")
    require(9 in missing, "expected missing difference 9")
    output = {"actual_GF128_offsets": sorted(offsets),
              "finite_family_checks": [check(a) for a in range(3, 7)],
              "deleted_high_offset_8_counterexample": {"missing_differences": missing,
                                                       "named_missing_difference": 9},
              "scope": "finite additive geometry; written NO proof is separate"}
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
