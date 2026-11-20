"""Deduplicate actual offset queries by their canonical zero-seed addresses.

The general covariance argument is in compiler.md. This bounded control uses
038's symbolic router and literal descent/ascent, then compares the resulting
whole views with 042's independently represented physical router.
"""
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


def load(name, relative):
    path = Path(__file__).resolve().parents[1] / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def require(test, message):
    if not test:
        raise ValueError(message)


def canonical(layout, address):
    frames, point, _ = layout.decode(address)
    d = layout.k
    result = []
    for side, label, _ in frames:
        result.append(("row" if side == "R" else "column", d, label))
        d = d // 2 + layout.a if side == "R" else d - d // 2
    return tuple(result), point


def main():
    source = load("offset_source", "038-recursive-query-fibers/verify_recursive.py")
    physical = load("independent_physical", "042-accepted-sites/check_overlap.py")
    outputs = []
    for k, a in ((7, 3), (8, 3)):
        paths = list(source.routes(k, a))
        layout = source.Layout(k, a, max(len(route) for route, _ in paths))
        by_zero = {}
        slots = comparisons = 0
        probes = sorted({0, 1, (1 << k) - 1, sum(1 << i for i in range(0, k, 2))})
        for route, width in paths:
            for offset in range(1 << width):
                overwritten, candidates = source.symbolic(layout, route, offset, "relative")
                require(not overwritten, "lost original seed bit")
                for tape in range(1 << (a * len(route))):
                    selected = [c for c in candidates if source.active(c, tape << k)]
                    require(len(selected) == 1, "ambiguous canonical route")
                    chosen = selected[0]
                    signature = tuple(t if source.variable(t) is not None and source.variable(t) < k
                                      else source.ONE if source.bit_value(t, tape << k) else source.ZERO
                                      for t in chosen.fields)
                    variables = [source.variable(t) for t in signature if source.variable(t) is not None]
                    require(sorted(variables) == list(range(k)), "not injective full-rank projection")
                    zero = source.word(source.bit_value(t, 0) for t in signature)
                    if zero in by_zero:
                        require(by_zero[zero] == signature, "zero coincidence is not equal query maps")
                    by_zero[zero] = signature
                    slots += 1
                    for z in probes:
                        address = source.word(source.bit_value(t, z) for t in signature)
                        require(address == source.direct(layout, route, offset, z, tape, "relative"),
                                "symbolic map disagrees with literal routing")
                        comparisons += 1

        incidence = Counter()
        for z in range(1 << k):
            encoded = [source.word(source.bit_value(t, z) for t in sig) for sig in by_zero.values()]
            require(len(set(encoded)) == len(encoded), "distinct maps collide at another seed")
            view = {canonical(layout, x) for x in encoded}
            require(view == physical.full_view(k, a, z), "deduplicated view changes physical reads")
            incidence.update(view)
        maximum = max(incidence.values())
        require(maximum <= (1 << (2*a)) + (1 << a) - 1, "physical multiplicity bound")
        outputs.append({"k": k, "a": a, "raw_slots_including_unused_tape_bits": slots,
                        "unique_query_maps": len(by_zero), "literal_route_comparisons": comparisons,
                        "whole_seed_views_compared": 1 << k, "physical_cells": len(incidence),
                        "max_input_copy_load": maximum})
    return {"scope": "bounded query-map and alias controls; no gate circuit or asymptotic proof",
            "cases": outputs}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
