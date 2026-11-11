"""Bounded BV14 Section 6 coordinate-routing audit, standard-library Python 3.

Addresses include every retained edge label, the shape and the local coordinate.
One column hop replaces that edge by its row sibling, which lies outside T.
Both absolute and seed-relative (inherited coordinate XOR slot) leaf points
are tested. Gates, symbol-bit packaging and the full Boolean PCP layout lie
outside this coordinate model.
"""
from collections import Counter
from dataclasses import dataclass
import json
import random


def require(condition, message):
    if not condition:
        raise ValueError(message)


def bits(value, width):
    return tuple((value >> i) & 1 for i in range(width))


def word(xs):
    return sum(x << i for i, x in enumerate(xs))


def routes(k, a):
    if k <= 2 * a:
        yield (), k
        return
    for edge, child in (("R", k // 2 + a), ("C", k - k // 2)):
        for suffix, leaf_size in routes(child, a):
            yield (edge,) + suffix, leaf_size


ZERO, ONE = -1, -2


@dataclass(frozen=True)
class Candidate:
    fields: tuple  # plain token t >= 0, complemented token -3-t, constants ZERO and ONE
    guards: tuple  # pairs (tuple of tested tokens, should all be zero)
    destination: str
    pops: int


@dataclass(frozen=True)
class Layout:
    k: int
    a: int
    depth: int

    @property
    def payload_width(self):
        # Descending R adds a slots; C adds a-1. Replacing a C by R fits this width.
        return self.k + self.a * self.depth

    def encode_symbolic(self, frames, coord):
        header = []
        payload = []
        for edge, label in frames:
            header.extend((ONE, ZERO) if edge == "R" else (ZERO, ONE))
            payload.extend(label)
        header += [ZERO] * (2 * self.depth - len(header))
        payload.extend(coord)
        require(len(payload) <= self.payload_width, "symbolic address exceeds payload width")
        return tuple(header + payload + [ZERO] * (self.payload_width - len(payload)))

    def encode_concrete(self, frames, value, local_size):
        header = payload = off = 0
        for level, (edge, label, width) in enumerate(frames):
            header |= (1 if edge == "R" else 2) << (2 * level)
            payload |= label << off
            off += width
        require(value < (1 << local_size) and off + local_size <= self.payload_width,
                "invalid local coordinate or payload length")
        return header | ((payload | (value << off)) << (2 * self.depth))

    def decode(self, address):
        header = address & ((1 << (2 * self.depth)) - 1)
        payload = address >> (2 * self.depth)
        dimension = self.k
        frames = []
        for _ in range(self.depth):
            tag = header & 3
            header >>= 2
            if tag == 0:
                require(header == 0, "interior padding in shape")
                break
            require(tag in (1, 2) and dimension > 2 * self.a, "bad shape")
            lo = dimension // 2
            if tag == 1:
                edge, width, dimension = "R", dimension - lo, lo + self.a
            else:
                edge, width, dimension = "C", lo + self.a - 1, dimension - lo
            frames.append((edge, payload & ((1 << width) - 1), width))
            payload >>= width
        require(payload < (1 << dimension), "noncanonical trailing payload")
        return tuple(frames), payload, dimension


def symbolic(layout, route, fixed_leaf, mode):
    coord = tuple(range(layout.k))
    frames = []
    for depth, edge in enumerate(route):
        lo = len(coord) // 2
        fresh = tuple(range(layout.k + depth * layout.a, layout.k + (depth + 1) * layout.a))
        low, high = coord[:lo], coord[lo:]
        if edge == "R":
            frames.append(("R", high))
            coord = low + fresh
        else:
            frames.append(("C", low + fresh[:-1]))
            coord = high

    slot_bits = bits(fixed_leaf, len(coord))
    if mode == "absolute":
        overwritten = {t for t in coord if t < layout.k}
        coord = tuple(ONE if bit else ZERO for bit in slot_bits)
    else:
        require(mode == "relative", "unknown mode")
        overwritten = set()
        coord = tuple(-3 - t if bit else t for t, bit in zip(coord, slot_bits))
    candidates, guards = [], []
    pops = 0
    while frames:
        edge, label = frames[-1]
        if edge == "C":
            sibling = frames[:-1] + [("R", coord)]
            fields = layout.encode_symbolic(sibling, label + (ONE,))
            candidates.append(Candidate(fields, tuple(guards), "sibling", pops))
            break
        tested = coord[-layout.a:]
        # Both candidates exist before applying the guard, even if one is never active.
        fields = layout.encode_symbolic(frames, coord)
        candidates.append(Candidate(fields, tuple(guards + [(tested, False)]), "row", pops))
        guards.append((tested, True))
        coord = coord[:-layout.a] + label
        frames.pop()
        pops += 1
    else:
        fields = layout.encode_symbolic((), coord)
        candidates.append(Candidate(fields, tuple(guards), "root", pops))
    return overwritten, candidates


def concrete_down(layout, route, original, fresh):
    dimension = layout.k
    local = original
    stack = []
    for depth, edge in enumerate(route):
        lo = dimension // 2
        hi = dimension - lo
        low = local & ((1 << lo) - 1)
        high = local >> lo
        pad = (fresh >> (layout.a * depth)) & ((1 << layout.a) - 1)
        if edge == "R":
            stack.append(("R", high, hi))
            local, dimension = low | (pad << lo), lo + layout.a
        else:
            aux = pad & ((1 << (layout.a - 1)) - 1)
            stack.append(("C", low | (aux << lo), lo + layout.a - 1))
            local, dimension = high, hi

    return stack, local, dimension


def direct(layout, route, fixed_leaf, original, fresh, mode):
    """Integer reference, with no variable labels or guessed up-phase branches."""
    stack, inherited, dimension = concrete_down(layout, route, original, fresh)
    require(fixed_leaf < (1 << dimension), "leaf literal out of domain")
    local = fixed_leaf if mode == "absolute" else inherited ^ fixed_leaf
    while stack:
        edge, label, width = stack[-1]
        if edge == "C":
            stack[-1] = ("R", local, dimension)
            local, dimension = label | (1 << width), width + 1
            break
        low_size = dimension - layout.a
        if local >> low_size:
            break
        stack.pop()
        local |= label << low_size
        dimension = low_size + width

    address = layout.encode_concrete(stack, local, dimension)
    require(layout.decode(address) == (tuple(stack), local, dimension), "address round-trip")
    return address


def variable(token):
    if token < ONE:
        return -3 - token
    return token if token >= 0 else None


def bit_value(token, assignment):
    index = variable(token)
    if index is None:
        return int(token == ONE)
    return ((assignment >> index) & 1) ^ int(token < ONE)


def active(candidate, assignment):
    return all((not any(bit_value(t, assignment) for t in tested)) == is_zero
               for tested, is_zero in candidate.guards)


def projected_word(candidate, assignment):
    return word(bit_value(t, assignment) for t in candidate.fields)


def audit(k, a, mode):
    branch_list = list(routes(k, a))
    layout = Layout(k, a, max(len(path) for path, leaf_size in branch_list))
    rng = random.Random(110001 + 17 * k + a)
    counts = Counter()
    bounds = []
    active_cases = set()
    for route, leaf_size in branch_list:
        pad_bits = len(route) * a
        pads = {0, (1 << pad_bits) - 1, word(i % 2 for i in range(pad_bits)),
                rng.getrandbits(pad_bits), rng.getrandbits(pad_bits)}
        probes = {0, (1 << leaf_size) - 1, 1 << (leaf_size - 1), rng.getrandbits(leaf_size)}
        for leaf in range(1 << leaf_size):
            overwritten, candidates = symbolic(layout, route, leaf, mode)
            expected = set(range(k)) - overwritten
            bounds.append(len(expected))
            counts["leaf_route_pairs"] += 1
            for c in candidates:
                indices = (variable(t) for t in c.fields)
                original_fields = [i for i in indices if i is not None and i < k]
                require(set(original_fields) == expected and len(original_fields) == len(expected),
                        "candidate lost or duplicated an original token")
                guards = (variable(t) for tested, _ in c.guards for t in tested)
                require(all(i is None or i >= k for i in guards),
                        "up guard depends on an original token")
                counts["symbolic_candidates"] += 1
            if leaf not in probes:
                continue
            for pad in sorted(pads):
                assignment = pad << k
                chosen = [c for c in candidates if active(c, assignment)]
                require(len(chosen) == 1, "guards fail to partition assignments")
                c = chosen[0]
                active_cases.add((c.destination, c.pops))
                # Compare all original-coordinate derivatives and mixed assignments.
                originals = [0] + [1 << i for i in range(k)] + [rng.getrandbits(k) for _ in range(3)]
                for original in originals:
                    d = direct(layout, route, leaf, original, pad, mode)
                    require(projected_word(c, assignment | original) == d,
                            "direct and symbolic addresses differ")
                counts["concrete_symbolic_matches"] += len(originals)
            if k <= 10 and leaf == 0:
                # Entire address histogram for one absolute occurrence per path,
                # with the mixed pad pattern. Includes all ambient seed assignments.
                pad = word(i % 2 for i in range(pad_bits))
                bins = Counter(direct(layout, route, leaf, x, pad, mode) for x in range(1 << k))
                require(len(bins) == 1 << len(expected)
                        and set(bins.values()) == {1 << len(overwritten)}, "fiber histogram")
                counts["exhaustive_fiber_routes"] += 1
    return {"k": k, "a": a, "mode": mode, "depth": layout.depth, "routes": len(branch_list),
            "min_original_rank": min(bounds), "max_original_rank": max(bounds),
            "observed_destination_pops": [list(x) for x in sorted(active_cases)],
            **dict(sorted(counts.items()))}


def dropped_path_control():
    layout = Layout(7, 3, 1)
    addresses = [direct(layout, ("R",), 1 << 5, x, 0, "absolute") for x in range(128)]
    locals_only = {layout.decode(z)[1] for z in addresses}
    require(len(set(addresses)) == 16 and len(locals_only) == 1,
            "path-dropping control did not collapse addresses")
    return {"k": 7, "a": 3, "leaf_point": 32, "route": "R",
            "full_address_image": 16, "local_coordinate_only_image": 1}


def compare_leaf_enumerations(samples):
    # On each path the relative list is the absolute list permuted by ONE
    # inherited leaf point; compare every slot, including duplicate addresses.
    streams = slots = changed_slots = 0
    rng = random.Random(1111)
    for k, a in samples:
        all_routes = list(routes(k, a))
        layout = Layout(k, a, max(len(path) for path, _ in all_routes))
        for path, dim in all_routes:
            for original, pad in ((0, 0), ((1 << k) - 1, 0),
                                  (rng.getrandbits(k), rng.getrandbits(a * len(path)))):
                _, inherited, _ = concrete_down(layout, path, original, pad)
                absolute = [direct(layout, path, v, original, pad, "absolute")
                            for v in range(1 << dim)]
                relative = [direct(layout, path, v, original, pad, "relative")
                            for v in range(1 << dim)]
                require(relative == [absolute[v ^ inherited] for v in range(1 << dim)],
                        "full leaf address list not permuted as claimed")
                streams += 1
                slots += len(relative)
                changed_slots += sum(x != y for x, y in zip(absolute, relative))
    # The full lists are permuted, yet a predicate reading slot zero can distinguish them.
    layout = Layout(7, 3, 1)
    abs0 = direct(layout, ("R",), 0, 1, 0, "absolute")
    rel0 = direct(layout, ("R",), 0, 1, 0, "relative")
    require(abs0 != rel0, "identity of ordered slots unexpectedly preserved")
    return {"seed_path_lists": streams, "compared_slots": slots,
            "different_same_index_addresses": changed_slots,
            "order_control": {"k": 7, "a": 3, "path": "R", "seed": 1, "fresh": 0,
                              "slot": 0, "absolute_address": abs0, "relative_address": rel0}}


if __name__ == "__main__":
    samples = [(7, 3), (8, 3), (10, 3), (15, 3), (21, 3), (17, 4), (33, 3)]
    print(json.dumps({"cases": [audit(k, a, mode) for k, a in samples
                                for mode in ("absolute", "relative")],
                      "leaf_permutation": compare_leaf_enumerations(samples),
                      "dropped_path_control": dropped_path_control()}, indent=2, sort_keys=True))
