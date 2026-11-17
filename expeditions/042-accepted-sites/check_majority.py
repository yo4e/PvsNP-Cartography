"""Audit the partition and count protected centers, without expanding huge RS proofs."""
from collections import Counter
from itertools import product
import json
from math import comb


def require(test, message):
    if not test:
        raise ValueError(message)


def disjoint_checks(k, basis):
    width = len(basis) + 1
    result = []
    for low in range(0, k - width + 1, width):
        check = next(candidate << low for candidate in range(1, 1 << width)
                     if all(((candidate << low) & v).bit_count() % 2 == 0 for v in basis))
        require(all(old & check == 0 for old in result), "overlapping parity support")
        result.append(check)
    return result


def small_partition():
    # Abstract combinatorial control: 12 seed bits, 1 generator, 2 groups,
    # 3 parities per group, overlap displacements of weight at most 1 modulo H.
    # Its radius is chosen for a nonempty small interior, not a claim about RS at a=2.
    k, generator, groups, n, radius = 12, 0b111001011101, 2, 3, 1
    checks = disjoint_checks(k, [generator])
    require(len(checks) == groups*n, "incorrect check count")
    labels, protected = [], []
    for z in range(1 << k):
        parities = [(z & check).bit_count() % 2 for check in checks]
        weights = [sum(parities[i:i+n]) for i in range(0, groups*n, n)]
        labels.append(tuple(2*u > n for u in weights))
        protected.append(all(abs(2*u-n) > 2*radius for u in weights))
    require(set(Counter(labels).values()) == {1 << (k-groups)}
            and len(set(labels)) == 1 << groups, "regions not equiprobable")
    moves = {h ^ x for h, x in product((0, generator), [0] + [1 << j for j in range(k)])}
    checks_done = 0
    for z, interior in enumerate(protected):
        if interior:
            for step in moves:
                require(labels[z ^ step] == labels[z], "cross-region adjacency")
                checks_done += 1
    require(sum(protected) == 256, "interior size")
    return {"seed_count": len(labels), "regions": len(set(labels)), "interior": sum(protected),
            "neighbor_checks": checks_done, "radius": radius, "scope": "abstract partition only"}


def count_interior(k, a, rank):
    total_checks = k // (rank + 1)
    n = total_checks // a
    n -= int(n % 2 == 0)
    require(n >= 1, "not enough invariant checks")
    w = 4*a
    low = max(0, n//2 - w + 1)
    high = min(n, n//2 + w)
    boundary = sum(comb(n, i) for i in range(low, high + 1))
    interior = ((1 << n)-boundary)**a
    denominator = 1 << (a*n)
    ppm = (10**6 * interior) // denominator
    return {"k": k, "a": a, "rank": rank, "group_length": n,
            "interior_parts_per_million_rounded_down": ppm}


if __name__ == "__main__":
    examples = [count_interior(k, 3, 2) for k in (16384, 65536, 262144)]
    require([v["interior_parts_per_million_rounded_down"] for v in examples]
            == [188759, 471836, 700620], "integer count checkpoints")
    print(json.dumps({"partition": small_partition(), "symbolic_integer_counts": examples},
                     indent=2, sort_keys=True))
