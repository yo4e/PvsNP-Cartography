"""Physical k=8, a=3 two-level Reed–Solomon oracle and bundled verifier fixtures."""
from dataclasses import dataclass
from functools import cache, reduce
from operator import xor
import json

THETA = 256
OUTER_AUX = (2 * THETA, 4 * THETA, 8 * THETA)
INNER_AUX = (16 * THETA, 32 * THETA, 64 * THETA)
WORD_COUNT = 16384


def require(test, message):
    if not test:
        raise ValueError(message)


def base_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 256:
            a ^= 0x11B
    return result


BASE = tuple(bytes(base_mul(a, b) for b in range(256)) for a in range(256))
BASE_INV = [0] + [row.index(1) for row in BASE[1:]]


def mul(x, y):
    """In the basis 1,θ, use θ²=θ+0x20."""
    a, b = x & 255, x >> 8
    c, d = y & 255, y >> 8
    ac, bd = BASE[a][c], BASE[b][d]
    return (ac ^ BASE[32][bd]) | ((BASE[a ^ b][c ^ d] ^ ac) << 8)


def inv(x):
    if not x:
        raise ZeroDivisionError("zero field element")
    a, b = x & 255, x >> 8
    norm = BASE[a][a ^ b] ^ BASE[32][BASE[b][b]]
    scalar = BASE_INV[norm]
    return BASE[scalar][a ^ b] | (BASE[scalar][b] << 8)


def field_power(x, degree):
    y = 1
    while degree:
        if degree & 1:
            y = mul(x, y)
        x = mul(x, x)
        degree >>= 1
    return y


def vector(basis, index):
    return reduce(xor, (b for i, b in enumerate(basis) if index & (1 << i)), 0)


def subspace_value(width, x):
    y = 1
    for u in range(width):
        y = mul(y, x ^ u)
    return y


def row_coordinates(shift, basis, auxiliaries, high):
    low = len(basis) // 2
    beta = shift ^ vector(basis[low:], high)
    c0, c1, c2 = auxiliaries
    return beta, (*basis[:low], c1, c2, c0 ^ beta)


ROOT_BASIS = tuple(1 << i for i in range(8))
OUTER_COORDS = [row_coordinates(THETA, ROOT_BASIS, OUTER_AUX, v) for v in range(16)]


def outer_cell(v, w):
    return ((w >> 4) << 8) | (v << 4) | (w & 15)


def inner_cell(v, j, i):
    if i < 8:
        return outer_cell(v, (j << 3) | i)
    return 2048 + 896*v + 128*((i >> 3) - 1) + 8*j + (i & 7)


@dataclass(frozen=True)
class Leaf:
    addresses: tuple
    points: tuple
    cutoff: int


def geometry():
    leaves = {}
    outer_y = tuple(subspace_value(16, beta) for beta, _ in OUTER_COORDS)
    require(len(set(outer_y)) == 16, "outer ordinates must distinguish the rows")
    for c in range(64):
        addresses = tuple(outer_cell(v, 64+c) for v in range(16))
        leaves[("outer_col", c)] = Leaf(addresses, outer_y, 2)
    for v, (beta, basis) in enumerate(OUTER_COORDS):
        for w in range(16):
            x = beta ^ vector(basis, w)
            require(x == THETA ^ outer_cell(v, w) and subspace_value(16, x) == outer_y[v],
                    "outer parent geometric alias")
        for c in range(64):
            x = beta ^ vector(basis, 64+c)
            require(x == OUTER_AUX[0] ^ vector((*ROOT_BASIS[:4], *OUTER_AUX[1:]), c),
                    "outer rectangle geometric alias")
        inner_y = []
        for j in range(16):
            delta, directions = row_coordinates(beta, basis, INNER_AUX, j)
            inner_y.append(subspace_value(8, delta))
            points = tuple(delta ^ vector(directions, i) for i in range(64))
            for i in range(8):
                parent_x = beta ^ vector(basis, 8*j+i)
                require(points[i] == parent_x and subspace_value(8, parent_x) == inner_y[-1],
                        "inner parent geometric alias")
            for c in range(32):
                require(points[32+c] == INNER_AUX[0] ^ vector((*basis[:3], *INNER_AUX[1:]), c),
                        "inner rectangle geometric alias")
            addresses = tuple(inner_cell(v, j, i) for i in range(64))
            leaves[("inner_row", v, j)] = Leaf(addresses, points, 8)
        for c in range(32):
            addresses = tuple(inner_cell(v, j, 32+c) for j in range(16))
            leaves[("inner_col", v, c)] = Leaf(addresses, tuple(inner_y), 2)
    for leaf in leaves.values():
        require(len(set(leaf.points)) == len(leaf.points), "repeated field abscissa")
        require(len(set(leaf.addresses)) == len(leaf.addresses), "repeated physical cell in leaf")
    return leaves


@cache
def check_weights(points, cutoff):
    """Absolute Lagrange weights; all operations are in the actual extension field."""
    weights = []
    for x in points[cutoff:]:
        row = []
        for i, xi in enumerate(points[:cutoff]):
            numerator = denominator = 1
            for j, xj in enumerate(points[:cutoff]):
                if i != j:
                    numerator = mul(numerator, x ^ xj)
                    denominator = mul(denominator, xi ^ xj)
            row.append(mul(numerator, inv(denominator)))
        weights.append(row)
    return weights


def leaf_passes(cells, leaf):
    values = [cells[a] for a in leaf.addresses]
    weights = check_weights(leaf.points, leaf.cutoff)
    fixed = values[:leaf.cutoff]
    return all(reduce(xor, (mul(weight, y) for weight, y in zip(row, fixed)), 0) == actual
               for row, actual in zip(weights, values[leaf.cutoff:]))


def templates():
    cells = [0] * WORD_COUNT
    for v in range(16):
        d = v & 1
        for w in range(128):
            p = (w >> 3) & 1
            value = p
            if w < 16:
                value = d if p == d else field_power((v << 4) | w, 32)
            cells[outer_cell(v, w)] = value
        for j in range(16):
            for i in range(8, 64):
                cells[inner_cell(v, j, i)] = d
    return cells


def legal_extension(power):
    """Independently interpolate each child row from its parent for a legal monomial."""
    cells = [0] * WORD_COUNT
    cells[:256] = [field_power(x, power) for x in range(256)]
    for v, (beta, basis) in enumerate(OUTER_COORDS):
        points = tuple(beta ^ vector(basis, w) for w in range(128))
        parent = [cells[outer_cell(v, w)] for w in range(16)]
        for w, row in enumerate(check_weights(points, 16), start=16):
            cells[outer_cell(v, w)] = reduce(xor, (mul(c, y) for c, y in zip(row, parent)), 0)
        for j in range(16):
            delta, directions = row_coordinates(beta, basis, INNER_AUX, j)
            points = tuple(delta ^ vector(directions, i) for i in range(64))
            parent = [cells[inner_cell(v, j, i)] for i in range(8)]
            for i, row in enumerate(check_weights(points, 8), start=8):
                cells[inner_cell(v, j, i)] = reduce(xor, (mul(c, y) for c, y in zip(row, parent)), 0)
    return cells


def selected(z):
    """Enumerate actual independent control settings, pooling identical full leaves."""
    u, v = z & 15, z >> 4
    chosen = {("outer_col", u | (h << 4)) for h in range(4)}
    for f in range(8):
        child_seed = u | (f << 4)
        j, b = child_seed >> 3, child_seed & 7
        chosen.add(("inner_row", v, j))
        for h in range(4):
            chosen.add(("inner_col", v, b | (h << 3)))
    return chosen


def ordered_routes(leaves):
    """Replay offset reads over all distinct leaf words/coordinate translations.

    Full leaf evaluation can then use canonical order for its polynomial test.
    """
    seen = set()
    for z in range(256):
        u, v = z & 15, z >> 4
        for h in range(4):
            seen.add((("outer_col", u | (h << 4)), v))
        for f in range(8):
            child_seed = u | (f << 4)
            j, b = child_seed >> 3, child_seed & 7
            for fresh in range(8):
                seen.add((("inner_row", v, j), b | (fresh << 3)))
            for h in range(4):
                seen.add((("inner_col", v, b | (h << 3)), j))
    comparisons = 0
    for key, start in seen:
        leaf = leaves[key]
        for offset in range(len(leaf.points)):
            slot = start ^ offset
            if key[0] == "outer_col":
                addr = outer_cell(slot, 64+key[1])
            elif key[0] == "inner_col":
                addr = inner_cell(key[1], slot, 32+key[2])
            else:
                addr = inner_cell(key[1], key[2], slot)
            require(addr == leaf.addresses[slot], "routed cell differs from shared leaf")
            comparisons += 1
    return comparisons


def run_check(leaves, cells):
    # One verdict per actual leaf is reusable only after establishing the
    # complete coordinate permutations. No pass flag is used for an outer row.
    verdict = {key: leaf_passes(cells, leaf) for key, leaf in leaves.items()}
    accepted = {z for z in range(256) if all(verdict[key] for key in selected(z))}
    paired = {z for z in accepted if (z ^ 9) in accepted}
    counts = {kind: sum(ok for key, ok in verdict.items() if key[0] == kind)
              for kind in ("outer_col", "inner_row", "inner_col")}
    return accepted, paired, counts


def run():
    trace = reduce(xor, (field_power(32, 1 << i) for i in range(8)), 0)
    require(trace == 1, "quadratic constant must have trace one")
    leaves = geometry()
    reachable = set().union(*(set(leaf.addresses) for leaf in leaves.values()))
    require(reachable == set(range(WORD_COUNT)), "invalid physical address range")
    comparisons = ordered_routes(leaves)

    coset = [0] * WORD_COUNT
    coset[:16] = [1] * 16
    cases = {"zero": [0]*WORD_COUNT, "honest_degree31": legal_extension(31),
             "single_root_coset": coset, "two_templates": templates()}
    output = {}
    for name, cells in cases.items():
        accepted, paired, counts = run_check(leaves, cells)
        if name in ("zero", "honest_degree31"):
            expected = set(range(256))
        elif name == "single_root_coset":
            expected = set(range(16, 256))
        else:
            expected = {z for z in range(256) if ((z >> 3) & 1) == ((z >> 4) & 1)}
        require(accepted == expected, f"unexpected acceptance set: {name}")
        require(paired == (set() if name == "two_templates" else expected),
                f"unexpected paired acceptance: {name}")
        output[name] = {"passing_leaves": counts, "accepts": len(accepted), "paired_accepts": len(paired)}
        if name == "two_templates":
            by_shift = [sum((z ^ h) in accepted for z in accepted) for h in range(16)]
            require(by_shift == [128]*8 + [0]*8, "low mask spectrum")
            output[name]["pair_accepts_by_low_xor_0_to_15"] = by_shift
            output[name]["root_matches_constants_0_1"] = [cells[:256].count(c) for c in (0, 1)]
        if name == "honest_degree31":
            active = {kind: sum(len({cells[a] for a in leaf.addresses}) > 1
                                for key, leaf in leaves.items() if key[0] == kind)
                      for kind in counts}
            require(all(n > 0 for n in active.values()), "trivialized degree-31 control")
            output[name]["nonconstant_leaves"] = active
    return {"physical_words": WORD_COUNT, "distinct_leaves": len(leaves),
            "offset_reads_compared": comparisons, "fixtures": output}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
