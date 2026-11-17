"""Compute physical view intersections at all 256 seeds for every two-shift bundle."""
from collections import Counter
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "041-two-level-distance"))
import two_level_oracle as rs


def require(condition, message):
    if not condition:
        raise ValueError(message)


def translate(bitset, h):
    return sum(1 << (z ^ h) for z in range(256) if bitset & (1 << z))


def main():
    leaves = rs.geometry()
    views = []
    for z in range(256):
        addresses = {i for leaf in rs.selected(z) for i in leaves[leaf].addresses}
        require(z in addresses, "center root missing")
        views.append(sum(1 << i for i in addresses))

    def neighbors(target, collection):
        return sum(1 << z for z, view in enumerate(collection) if target & view)

    base = neighbors(views[0], views)
    for z in range(256):
        require(neighbors(views[z], views) == translate(base, z), "overlap not covariant")
    counts = Counter()
    for h in range(256):
        bundled = [view | views[z ^ h] for z, view in enumerate(views)]
        predicted = base | translate(base, h)
        require(neighbors(bundled[0], bundled) == predicted, "wrong pair neighborhood")
        sizes = {view.bit_count() for view in bundled}
        require(len(sizes) == 1, "nonuniform physical footprint")
        counts[sizes.pop(), predicted.bit_count()] += 1

    # General lists of 3/4 translations: compare sumset expansion with real reads.
    patterns = {}
    for masks in ((0, 1, 16), (0, 1, 2, 3), (0, 1, 16, 17), (0, 9, 18, 27)):
        bundled = []
        for z in range(256):
            view = 0
            for h in masks:
                view |= views[z ^ h]
            bundled.append(view)
        sums = {h ^ g for h in masks for g in masks}
        predicted = 0
        for shift in sums:
            predicted |= translate(base, shift)
        for z in range(256):
            require(neighbors(bundled[z], bundled) == translate(predicted, z),
                    "sumset mismatch on multi-shift schedule")
        patterns[",".join(map(str, masks))] = {"sumset_size": len(sums),
                                                "overlap_neighbors": predicted.bit_count()}
    rows = [{"unique_cells": u, "overlap_neighbors": d, "mask_count": n}
            for (u, d), n in sorted(counts.items())]
    return {"root_seeds": len(views), "base_unique_cells": views[0].bit_count(),
            "base_overlap_neighbors": base.bit_count(), "two_shift_schedules": rows,
            "other_mask_sets": patterns}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
