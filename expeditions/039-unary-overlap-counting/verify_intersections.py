"""Check signed-projection image intersections and their native seed coordinates.

A literal (i, b) evaluates to the i-th bit XOR b. Index -1 denotes the
constant zero before the XOR. Bits and coordinates are least-significant first.
"""

from collections import defaultdict
from itertools import combinations_with_replacement, product
import json


def evaluate(literals, word):
    return sum((((word >> i) & 1 if i >= 0 else 0) ^ b) << j
               for j, (i, b) in enumerate(literals))


def image_constraints(slot):
    """Express the image by equations between address bits or a ground node."""
    first = {}
    for coord, (var, sign) in enumerate(slot):
        if var < 0:
            yield coord, -1, sign
        elif var in first:
            previous, previous_sign = first[var]
            yield coord, previous, sign ^ previous_sign
        else:
            first[var] = coord, sign


def intersect(left, right):
    """Return an injective literal parametrization, or None for an empty image."""
    width = len(left)
    graph = defaultdict(list)
    for slot in (left, right):
        for i, j, sign in image_constraints(slot):
            graph[i].append((j, sign))
            graph[j].append((i, sign))
    name = {}
    free_bits = 0
    for root in range(-1, width):
        if root in name:
            continue
        component = -1 if root < 0 else free_bits
        if root >= 0:
            free_bits += 1
        name[root] = (component, 0)
        stack = [root]
        while stack:
            current = stack.pop()
            for other, parity in graph[current]:
                implied = (component, name[current][1] ^ parity)
                if other in name:
                    if name[other] != implied:
                        return None
                else:
                    name[other] = implied
                    stack.append(other)
    return free_bits, tuple(name[i] for i in range(width))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def run(seed_width, address_width):
    alphabet = list(product(range(-1, seed_width), range(2)))
    slots = list(product(alphabet, repeat=address_width))
    images = {}
    for slot in slots:
        by_address = defaultdict(list)
        for z in range(1 << seed_width):
            by_address[evaluate(slot, z)].append(z)
        rank = len({var for var, _ in slot if var >= 0})
        require(len(by_address) == 1 << rank, "image rank")
        require(all(len(v) == 1 << (seed_width - rank) for v in by_address.values()),
                "unequal fibers")
        images[slot] = set(by_address)
    histogram = defaultdict(int)
    for left, right in combinations_with_replacement(slots, 2):
        expected = images[left] & images[right]
        description = intersect(left, right)
        if description is None:
            require(not expected, "spurious contradiction")
            histogram["empty"] += 1
            continue
        b, literals = description
        points = [evaluate(literals, v) for v in range(1 << b)]
        require(set(points) == expected and len(points) == len(expected),
                "incorrect intersection or multiplicity")
        for slot in (left, right):
            # Recover precisely the used seed bits from a physical address.
            representatives = {}
            for j, (var, flip) in enumerate(slot):
                if var >= 0:
                    representatives[var] = (j, flip)
            section = tuple(representatives.get(i, (-1, 0)) for i in range(seed_width))
            require(all(evaluate(slot, evaluate(section, a)) == a for a in points),
                    "section is not a right inverse on the intersection")
        histogram[str(b)] += 1
    return {"seed_bits": seed_width, "address_bits": address_width,
            "signed_projection_maps": len(slots), "unordered_pairs_with_self": sum(histogram.values()),
            "by_intersection_dimension": dict(sorted(histogram.items()))}


if __name__ == "__main__":
    print(json.dumps([run(2, 3), run(3, 2)], indent=2))
