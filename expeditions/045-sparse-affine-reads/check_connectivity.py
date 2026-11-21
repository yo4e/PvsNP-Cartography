"""Finite path certificates for powers 2, 4 and 6 of the 7-cube.

Default: check the saved paths by direct combinatorial predicates, then lift
them and check every unordered pair of vertices.  --generate deterministically
rebuilds the small certificate using an integral max-flow search.  Acceptance
of the saved result never calls that search or trusts its maximum-flow value.
"""
import argparse
from collections import deque
from copy import deepcopy
import json
from math import comb
from pathlib import Path

DIMENSION = 7
SIZE = 1 << DIMENSION
HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def connectivity(radius):
    return sum(comb(DIMENSION, i) for i in range(1, 2 * radius + 1))


def adjacent(x, y, radius):
    return 1 <= (x ^ y).bit_count() <= 2 * radius


def check_paths(paths, source, target, radius):
    require(len(paths) == connectivity(radius), "wrong number of paths")
    occupied = set()
    for index, path in enumerate(paths):
        require(isinstance(path, list), "path must be a list")
        require(len(path) >= 3, "these nonadjacent endpoints need an interior")
        require(path[0] == source and path[-1] == target, "wrong endpoints")
        require(all(type(v) is int and 0 <= v < SIZE for v in path), "bad vertex")
        require(len(path) == len(set(path)), "path is not simple")
        require(all(adjacent(x, y, radius) for x, y in zip(path, path[1:])), "nonedge")
        interior = set(path[1:-1])
        require(not (interior & occupied), "path interiors intersect")
        occupied.update(interior)
    return {"paths": len(paths), "internal_vertices": len(occupied),
            "min_edges": min(len(p) - 1 for p in paths),
            "max_edges": max(len(p) - 1 for p in paths)}


def validate_case(document, radius, all_pairs=True):
    degree = connectivity(radius)
    require(document.get("radius") == radius, "wrong radius")
    require(document.get("connectivity") == degree, "wrong claimed connectivity")
    cases = document.get("cases", {})
    require(set(cases) == set(map(str, range(2 * radius + 1, 8))),
            "missing canonical pair")
    summary = {}
    for d in range(2 * radius + 1, 8):
        summary[str(d)] = check_paths(cases[str(d)], 0, (1 << d) - 1, radius)
    checked = 0
    direct = 0
    if all_pairs:
        for source in range(SIZE):
            for target in range(source + 1, SIZE):
                difference = source ^ target
                d = difference.bit_count()
                if d <= 2 * radius:
                    require(adjacent(source, target, radius), "lost direct edge")
                    direct += 1
                else:
                    order = ([i for i in range(7) if difference & (1 << i)] +
                             [i for i in range(7) if not difference & (1 << i)])
                    mapping = [source ^ sum(((v >> i) & 1) << order[i]
                                            for i in range(7)) for v in range(SIZE)]
                    paths = [[mapping[v] for v in path] for path in cases[str(d)]]
                    check_paths(paths, source, target, radius)
                    checked += 1
    cut = [v for v in range(SIZE) if adjacent(0, v, radius)]
    require(len(cut) == degree, "wrong isolating cut size")
    require(127 not in cut and 0 not in cut, "cut deletes a named endpoint")
    require(not any(adjacent(0, v, radius) for v in range(SIZE) if v not in cut),
            "cut does not isolate zero")
    star = {v for v in range(SIZE) if v.bit_count() <= radius}
    overlap_checks = 0
    for h in range(1, SIZE):
        intersection = star & {h ^ v for v in star}
        require((len(intersection) >= 2) == adjacent(0, h, radius),
                "affine-overlap graph differs from claimed cube power")
        if adjacent(0, h, radius):
            coordinates = [i for i in range(7) if h & (1 << i)]
            witness = sum(1 << i for i in coordinates[:len(coordinates) // 2])
            require(witness != (witness ^ h), "equal overlap witnesses")
            require(witness in intersection and (witness ^ h) in intersection,
                    "overlap witness outside star intersection")
        overlap_checks += 1
    return {"radius": radius, "canonical_pairs": summary,
            "star_size": len(star), "nonzero_overlap_shifts_checked": overlap_checks,
            "all_pairs_checked": checked + direct,
            "direct_edge_pairs": direct, "lifted_nonadjacent_pairs": checked,
            "certified_vertex_connectivity": degree,
            "deletions_tolerated": degree - 1,
            "exact_cut_size": len(cut), "exact_cut_rule": "neighbors of zero"}


def validate(document, all_pairs=True):
    require(document.get("dimension") == DIMENSION, "wrong dimension")
    require(document.get("adjacency") == "Hamming distance 1 through twice radius",
            "wrong graph")
    require(set(document.get("radii", {})) == {"1", "2", "3"}, "wrong radius set")
    return {"dimension": DIMENSION, "vertices": SIZE,
            "radii": {str(r): validate_case(document["radii"][str(r)], r, all_pairs)
                      for r in range(1, 4)},
            "evidence_kind": "explicit finite path certificate; no proof-assistant run"}


def find_paths(target, radius):
    """A deterministic search, deliberately separate from certificate checking."""
    degree = connectivity(radius)
    count = 2 * SIZE
    graph = [[] for _ in range(count)]
    originals = []

    def edge(source, dest, capacity):
        a = [dest, len(graph[dest]), capacity, capacity]
        b = [source, len(graph[source]), 0, 0]
        graph[source].append(a)
        graph[dest].append(b)
        originals.append((source, len(graph[source]) - 1))

    for v in range(SIZE):
        edge(2 * v, 2 * v + 1, degree if v in (0, target) else 1)
    for x in range(SIZE):
        for y in range(SIZE):
            if adjacent(x, y, radius):
                edge(2 * x + 1, 2 * y, degree)
    source, sink = 1, 2 * target
    flow = 0
    while True:
        level = [-1] * count
        level[source] = 0
        pending = deque([source])
        while pending:
            v = pending.popleft()
            for dest, _, capacity, _ in graph[v]:
                if capacity and level[dest] < 0:
                    level[dest] = level[v] + 1
                    pending.append(dest)
        if level[sink] < 0:
            break
        positions = [0] * count

        def augment(v, amount):
            if v == sink:
                return amount
            while positions[v] < len(graph[v]):
                index = positions[v]
                dest, reverse, capacity, _ = graph[v][index]
                if capacity and level[dest] == level[v] + 1:
                    pushed = augment(dest, min(amount, capacity))
                    if pushed:
                        graph[v][index][2] -= pushed
                        graph[dest][reverse][2] += pushed
                        return pushed
                positions[v] += 1
            return 0

        while True:
            pushed = augment(source, degree)
            if not pushed:
                break
            flow += pushed
    require(flow == degree, "generator failed to find the requested paths")
    positive = [[] for _ in range(count)]
    for v, index in originals:
        dest, _, capacity, original = graph[v][index]
        if original > capacity:
            positive[v].append([dest, original - capacity])
    paths = []
    for _ in range(flow):
        parent = {source: None}
        pending = deque([source])
        while pending and sink not in parent:
            v = pending.popleft()
            for index, (dest, amount) in enumerate(positive[v]):
                if amount and dest not in parent:
                    parent[dest] = (v, index)
                    pending.append(dest)
        require(sink in parent, "flow decomposition failed")
        node_path = [sink]
        while node_path[-1] != source:
            v, index = parent[node_path[-1]]
            positive[v][index][1] -= 1
            node_path.append(v)
        node_path.reverse()
        path = []
        for node in node_path:
            v = node // 2
            if not path or path[-1] != v:
                path.append(v)
        paths.append(path)
    check_paths(paths, 0, target, radius)
    return paths


def mutant_checks(document):
    rejected = {}
    variants = {}
    missing = deepcopy(document)
    missing["radii"]["1"]["cases"]["3"].pop()
    variants["only_27_paths"] = missing
    duplicate = deepcopy(document)
    duplicate["radii"]["1"]["cases"]["3"][1] = duplicate["radii"]["1"]["cases"]["3"][0].copy()
    variants["shared_interior"] = duplicate
    nonedge = deepcopy(document)
    nonedge["radii"]["1"]["cases"]["3"][0] = [0, 127, 7]
    variants["nonedge"] = nonedge
    endpoint = deepcopy(document)
    endpoint["radii"]["1"]["cases"]["3"][0][-1] = 6
    variants["wrong_endpoint"] = endpoint
    for name, variant in variants.items():
        try:
            validate(variant, all_pairs=False)
        except ValueError as error:
            rejected[name] = str(error)
        else:
            raise ValueError("invalid certificate accepted: " + name)
    return rejected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true")
    args = parser.parse_args()
    path = HERE / "connectivity-paths.json"
    if args.generate:
        document = {"dimension": DIMENSION,
                    "adjacency": "Hamming distance 1 through twice radius",
                    "radii": {str(r): {"radius": r, "connectivity": connectivity(r),
                              "cases": {str(d): find_paths((1 << d) - 1, r)
                                        for d in range(2 * r + 1, 8)}}
                              for r in range(1, 4)}}
        validate(document)
        path.write_text(json.dumps(document, sort_keys=True, indent=2) + "\n")
    document = json.loads(path.read_text())
    result = validate(document)
    result["invalid_certificates_rejected"] = mutant_checks(document)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
