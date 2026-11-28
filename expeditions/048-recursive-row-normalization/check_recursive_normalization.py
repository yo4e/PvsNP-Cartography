#!/usr/bin/env python3
"""Canonical BV14-variant physical coordinates, normalized to literal rows.

The coordinate model is Expedition038's stated variant, including its corrected
row-return polarity. This does not execute the field verifier or price a full
recursive Boolean circuit. All arithmetic below is integer/bit arithmetic.
"""

import argparse
from collections import Counter
from importlib import util
from functools import cache
import json
from pathlib import Path
import sys


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_geometry(repo_root):
    path = Path(repo_root) / "expeditions/038-recursive-query-fibers/verify_recursive.py"
    spec = util.spec_from_file_location("original_recursive_geometry", path)
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def shape_dimensions(layout, shape):
    """Return the parent dimension of each edge, then the terminal dimension."""
    dims = [layout.k]
    for edge in shape:
        d = dims[-1]
        require(d > 2 * layout.a and edge in ("R", "C"), "invalid recursive shape")
        dims.append(d // 2 + layout.a if edge == "R" else d - d // 2)
    require(len(shape) <= layout.depth, "shape exceeds header capacity")
    return dims


def auxiliary_widths(layout, shape):
    return [layout.a if edge == "R" else layout.a - 1 for edge in shape]


def normalize_address(layout, address):
    """Return (canonical shape, fresh-coordinate integer, root-coordinate integer).

    This reads only the physical address. It does not know the calling tape,
    query slot, seed, witness or stored symbol. Edge labels are NOT discarded.
    """
    frames, local, _ = layout.decode(address)
    shape = tuple(edge for edge, label, width in frames)
    dims = shape_dimensions(layout, shape)
    pads = [None] * len(shape)
    for i in reversed(range(len(shape))):
        edge, label, width = frames[i]
        lo = dims[i] // 2
        if edge == "R":
            pads[i] = local >> lo
            local = (local & ((1 << lo) - 1)) | (label << lo)
        else:
            pads[i] = label >> lo
            local = (label & ((1 << lo) - 1)) | (local << lo)
    aux = shift = 0
    for pad, width in zip(pads, auxiliary_widths(layout, shape)):
        require(0 <= pad < 1 << width, "auxiliary chunk overflow")
        aux |= pad << shift
        shift += width
    require(0 <= local < 1 << layout.k, "root-coordinate overflow")
    return shape, aux, local


def denormalize_address(layout, shape, aux, root_coordinate):
    """Inverse map, defined also on noncanonical overlapping row names."""
    dims = shape_dimensions(layout, shape)
    widths = auxiliary_widths(layout, shape)
    require(0 <= root_coordinate < 1 << layout.k, "bad root coordinate")
    require(0 <= aux < 1 << sum(widths), "bad auxiliary coordinate")
    frames = []
    local = root_coordinate
    for i, edge in enumerate(shape):
        lo, hi = dims[i] // 2, dims[i] - dims[i] // 2
        low, high = local & ((1 << lo) - 1), local >> lo
        pad = aux & ((1 << widths[i]) - 1)
        aux >>= widths[i]
        if edge == "R":
            frames.append(("R", high, hi))
            local = low | (pad << lo)
        else:
            frames.append(("C", low | (pad << lo), lo + layout.a - 1))
            local = high
    return layout.encode_concrete(frames, local, dims[-1])


def all_shapes(layout):
    """All syntactically valid physical-tree prefixes, including leaf prefixes."""
    result = []
    def walk(shape, d):
        result.append(shape)
        if d > 2 * layout.a:
            walk(shape + ("R",), d // 2 + layout.a)
            walk(shape + ("C",), d - d // 2)
    walk((), layout.k)
    return result


def canonical_rows(layout):
    """List (shape,aux) rows of distinct stored symbols, independent of seed.

    A terminal C is an alias of its R sibling. A terminal R whose last fresh
    chunk is zero is an alias of its parent. Earlier chunks remain unrestricted.
    """
    rows = [((), 0)]
    for shape in all_shapes(layout):
        if not shape or shape[-1] != "R":
            continue
        width = sum(auxiliary_widths(layout, shape))
        for aux in range(1 << width):
            if aux >> (width - layout.a):
                rows.append((shape, aux))
    return rows


def row_index(layout):
    return {row: i for i, row in enumerate(canonical_rows(layout))}


@cache
def row_count_recurrence(k, a):
    if k <= 2 * a:
        return 1
    lo = k // 2
    return (1 << a) * row_count_recurrence(lo + a, a) + (1 << (a - 1)) * (row_count_recurrence(k - lo, a) - 1)


def pack_address(layout, address, index):
    shape, aux, root = normalize_address(layout, address)
    require((shape, aux) in index, "noncanonical physical address")
    return (index[shape, aux] << layout.k) | root


def unique_tapes(layout, route):
    """Original code stores a bits per edge; C's top bit is unused and fixed 0."""
    tapes = [0]
    for depth, edge in enumerate(route):
        width = layout.a if edge == "R" else layout.a - 1
        tapes = [tape | (pad << (layout.a * depth)) for tape in tapes for pad in range(1 << width)]
    return tapes


def normalize_fields(layout, fields):
    """Symbolic bit-position version, independent of root/fresh-token values."""
    # Header coordinates must be constants for the chosen symbolic candidate.
    shape = []
    for level in range(layout.depth):
        pair = fields[2 * level:2 * level + 2]
        if pair == (-1, -1):
            break
        require(pair in ((-2, -1), (-1, -2)), "nonconstant candidate shape")
        shape.append("R" if pair == (-2, -1) else "C")
    shape = tuple(shape)
    dims = shape_dimensions(layout, shape)
    payload = fields[2 * layout.depth:]
    pos = 0
    labels = []
    for i, edge in enumerate(shape):
        d, lo = dims[i], dims[i] // 2
        width = d - lo if edge == "R" else lo + layout.a - 1
        labels.append(payload[pos:pos + width])
        pos += width
    live = payload[pos:pos + dims[-1]]
    pads = [None] * len(shape)
    for i in reversed(range(len(shape))):
        lo = dims[i] // 2
        if shape[i] == "R":
            pads[i] = live[lo:]
            live = live[:lo] + labels[i]
        else:
            pads[i] = labels[i][lo:]
            live = labels[i][:lo] + live
    return shape, tuple(t for chunk in pads for t in chunk), live


def symbolic_controls(g, samples):
    results = []
    for k, a in samples:
        routes = list(g.routes(k, a))
        layout = g.Layout(k, a, max(len(route) for route, leaf in routes))
        checked = 0
        for route, leaf in routes:
            for offset in range(1 << leaf):
                lost, candidates = g.symbolic(layout, route, offset, "relative")
                require(not lost, "relative query loses tokens")
                for candidate in candidates:
                    shape, extras, root = normalize_fields(layout, candidate.fields)
                    require(tuple(g.variable(t) for t in root) == tuple(range(k)), "unshuffle fails to restore root order")
                    require(all(g.variable(t) is None or g.variable(t) >= k for t in extras), "tag still depends on root seed")
                    checked += 1
        row_count = len(canonical_rows(layout))
        require(row_count == row_count_recurrence(k, a), "shape and subtree row counts disagree")
        results.append({"k": k, "a": a, "depth": layout.depth, "routes": len(routes),
                        "symbolic_candidates": checked,
                        "canonical_row_count": row_count})
    return results


def first_depth_two(g):
    k, a = 8, 3
    routes = list(g.routes(k, a))
    layout = g.Layout(k, a, max(len(route) for route, leaf in routes))
    require(layout.depth == 2, "not genuine depth two")
    index = row_index(layout)
    n = 1 << k
    require(len(index) == 64, "literal-row census")
    counts = Counter("".join(shape) or "root" for shape, aux in index)
    require(dict(counts) == {"root": 1, "R": 7, "RR": 56}, "canonical shape census")
    seen = set()
    for (shape, aux), row in index.items():
        for root in range(n):
            old = denormalize_address(layout, shape, aux, root)
            require(normalize_address(layout, old) == (shape, aux, root), "global inverse law")
            require(pack_address(layout, old, index) == row * n + root, "packed inverse law")
            require(old not in seen, "distinct physical cells collide")
            seen.add(old)
    occurrence_count = checks = 0
    physical_hits = Counter()
    row_hits = Counter()
    witnesses = []
    for route, leaf in routes:
        for tape in unique_tapes(layout, route):
            for offset in range(1 << leaf):
                old0 = g.direct(layout, route, offset, 0, tape, "relative")
                shape0, aux0, delta = normalize_address(layout, old0)
                packed0 = pack_address(layout, old0, index)
                row = packed0 >> k
                occurrence_count += 1
                for seed in range(n):
                    old = g.direct(layout, route, offset, seed, tape, "relative")
                    shape, aux, root = normalize_address(layout, old)
                    require((shape, aux) == (shape0, aux0), "normalized row varies with seed")
                    require(root == seed ^ delta, "not a fixed signed seed translation")
                    require(pack_address(layout, old, index) == (row << k) | (seed ^ delta), "packed query mismatch")
                    require(old in seen, "query leaves canonical storage universe")
                    physical_hits[old] += 1
                    checks += 1
                row_hits[row] += 1
                if len(witnesses) < 8 and shape0 == ("R", "R"):
                    witnesses.append({"route": "".join(route), "tape": tape, "offset": offset,
                                      "shape": "".join(shape0), "aux": aux0,
                                      "row": row, "delta": delta})
    require(set(physical_hits) == seen, "enumerated queries miss canonical cells")
    require(occurrence_count == 4672 and checks == 1196032, "query census")
    # Original leaf C and its sibling R names must route to one physical cell.
    alias_pairs = 0
    for seed in range(n):
        for fresh in range(4):
            for offset in range(16):
                old_c = g.direct(layout, ("C",), offset, seed, fresh, "relative")
                shape, aux, root = normalize_address(layout, old_c)
                require(shape == ("R",) and aux == fresh | 4, "column sibling tag")
                require(root == seed ^ (offset << 4), "column sibling root translation")
                old_r = denormalize_address(layout, shape, aux, root)
                require(old_c == old_r, "column/row alias detached")
                alias_pairs += 1
    # A per-occurrence root normalization without the fresh tag detaches aliases
    # or merges distinct extension cells. Explicitly retain two distinct rows.
    a0 = denormalize_address(layout, ("R",), 1, 0)
    a1 = denormalize_address(layout, ("R",), 2, 0)
    require(a0 != a1 and normalize_address(layout, a0)[2] == normalize_address(layout, a1)[2], "tag-drop countercontrol")
    payload = layout.payload_width
    original_q = 1 << (2 * layout.depth + payload)
    return {
        "k": k, "a": a, "depth": layout.depth,
        "routes": [{"shape": "".join(route), "leaf_dimension": leaf,
                    "unique_tapes": len(unique_tapes(layout, route))} for route, leaf in routes],
        "canonical_rows_by_shape": dict(counts), "canonical_rows": len(index),
        "canonical_symbols": len(seen), "original_padded_symbol_cube": original_q,
        "packed_symbol_cube": len(index) * n,
        "raw_bit_rows_if_root_k_internal_2k": k * (2 * len(index) - 1),
        "packed_raw_bit_cube": n * (1 << (k * (2 * len(index) - 1) - 1).bit_length()),
        "fixed_tape_offset_occurrences": occurrence_count,
        "direct_seed_query_checks": checks, "column_sibling_alias_controls": alias_pairs,
        "minimum_occurrences_per_row": min(row_hits.values()),
        "maximum_occurrences_per_row": max(row_hits.values()),
        "all_physical_cells_reached": True, "query_coordinate_degree": 1,
        "signed_three_query_composition_bound": "3d",
        "sample_normalized_queries": witnesses,
        "tag_drop_countercontrol": {"old_addresses": [a0, a1], "shared_root_coordinate": 0},
    }


def main(repo_root):
    g = load_geometry(repo_root)
    return {
        "scope": "canonical coordinate semantics of Expedition038 fixed-rate variant; no field/CNF execution",
        "source": "expeditions/038-recursive-query-fibers/verify_recursive.py",
        "symbolic_controls": symbolic_controls(g, [(7, 3), (8, 3), (10, 3), (15, 3), (21, 3), (17, 4), (33, 3)]),
        "first_genuine_depth_two": first_depth_two(g),
        "limits": ["symbolic controls supplement a separate induction, not an arbitrary-size experiment",
                   "no recursive Boolean template census, exact soundness or approximation theorem",
                   "normalization is public and witness-independent; any later row map is separate",
                   "no Lean acceptance or novelty claim"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    print(json.dumps(main(args.repo_root), indent=2, sort_keys=True))
