"""Check exact physical-cell seed incidence against the independent literal router."""
from collections import Counter, defaultdict
import importlib.util
import json
from pathlib import Path
import sys


def load_router():
    file = Path(__file__).resolve().parents[1] / "042-accepted-sites" / "check_overlap.py"
    spec = importlib.util.spec_from_file_location("physical_router", file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(test, message):
    if not test:
        raise ValueError(message)


def left_leaf(tokens, a):
    while len(tokens) > 2*a:
        tokens = tokens[:len(tokens)//2] + [None]*a
    return [x for x in tokens if x is not None]


def span(block):
    values = [0]
    for i in block:
        values += [x | 1 << i for x in values]
    return values


def predicted(k, a, address):
    """Recover original-token positions from the canonical owner, not a down tape."""
    frames, coordinate = address
    tokens = list(range(k))
    recovered = 0
    owner_parent = None
    for side, dimension, label in frames:
        require(dimension == len(tokens), "parent dimension")
        lo = dimension // 2
        low, high = tokens[:lo], tokens[lo:]
        owner_parent = tokens
        if side == "row":
            saved = high
            tokens = low + [None]*a
        else:
            saved = low + [None]*(a-1)
            tokens = high
        for position, token in enumerate(saved):
            if token is not None and label & (1 << position):
                recovered |= 1 << token
    for position, token in enumerate(tokens):
        if token is not None and coordinate & (1 << position):
            recovered |= 1 << token

    blocks = [left_leaf(tokens, a)]
    if frames:
        require(frames[-1][0] == "row", "canonical owner is not a row")
        lo = len(owner_parent)//2
        if coordinate & (1 << (lo+a-1)):
            blocks.append(left_leaf(owner_parent[lo:], a))
    return {recovered ^ shift for block in blocks for shift in span(block)}


def main():
    router = load_router()
    outputs = []
    for k in (7, 8, 9, 10):
        incidence = defaultdict(set)
        sizes = set()
        for z in range(1 << k):
            view = router.full_view(k, 3, z)
            sizes.add(len(view))
            for address in view:
                incidence[address].add(z)
        require(len(sizes) == 1, "unequal physical view sizes")
        maximum = 0
        histogram = Counter()
        for address, centers in incidence.items():
            require(centers == predicted(k, 3, address), "incidence formula")
            histogram[len(centers)] += 1
            maximum = max(maximum, len(centers))
        bound = (1 << 6)+(1 << 3)-1
        require(maximum <= bound, "universal fixed-rate multiplicity")
        require(sum(t * n for t, n in histogram.items()) == (1 << k)*next(iter(sizes)),
                "double count")
        outputs.append({"k": k, "a": 3, "distinct_cells_in_one_view": sizes.pop(),
                        "physical_cells": len(incidence), "max_seeds_reading_a_cell": maximum,
                        "incidence_histogram": dict(sorted(histogram.items()))})
    # Check the sharper shape bound across different rates and recursion depths.
    # This is a finite control of the written last-row-split proof.
    shape_cases = 0
    for a in range(3, 8):
        for k in range(2*a, 64*a+1):
            leaves, pairs = router.blocks(k, a)
            require(max(map(len, leaves)) <= 2*a, "leaf support")
            require(all(len(left) <= a and len(left)+len(right) <= 3*a
                        for left, right in pairs), "paired support")
            shape_cases += 1
        leaves, pairs = router.blocks(4*a, a)
        require(max(len(left)+len(right) for left, right in pairs) == 3*a,
                "sharp displacement support")
    # A common-rectangle address at k=4a attains the multiplicity bound. Check
    # all 71 predicted reader seeds and 16 outside seeds via actual full views.
    a, k = 3, 12
    address = ((("row", k, 0),), 1 << (k//2+a-1))
    readers = predicted(k, a, address)
    require(len(readers) == (1 << (2*a))+(1 << a)-1, "sharp multiplicity")
    outside = [z for z in range(1 << k) if z not in readers][:16]
    for z in sorted(readers)+outside:
        require((address in router.full_view(k, a, z)) == (z in readers),
                "literal sharp-cell membership")
    return {"scope": "physical addresses only", "exact_replays": outputs,
            "shape_controls": shape_cases,
            "sharp_cell_control": {"k": k, "a": a, "predicted_readers": len(readers),
                                   "all_predicted_readers_checked": len(readers),
                                   "outside_seeds_checked": len(outside)}}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
