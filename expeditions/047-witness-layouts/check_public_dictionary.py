#!/usr/bin/env python3
"""Exact standalone public symbolic-layout control; no external dependencies.

This is a new, deliberately easy constrained witness relation, not the
Expedition046 circuit. Its raw NO minimum is four, not 109 or 477.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
import random


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# The PUBLIC symbolic basis is (1, w0, w1, z0, z1, u*v, w0*w1).
# XOR signatures are derived without assigning a witness.
K, N, L = 2, 4, 7
ROWS = (
    ("one", 1), ("w0", 2), ("w1", 4), ("z0", 8), ("z1", 16),
    ("u", 2 ^ 8), ("v", 4 ^ 16), ("uv", 32), ("p", 64),
    ("sum", 2 ^ 8 ^ 4 ^ 16), ("copy_u", 2 ^ 8), ("copy_uv", 32),
)
INDEX = {name: i for i, (name, _) in enumerate(ROWS)}
R = len(ROWS)
counts = Counter(signature for _, signature in ROWS)
rank_bits = (max(counts.values()) - 1).bit_length()
tag_bits = L + rank_bits
Q = N * (1 << tag_bits)
compact_Q = N * (1 << (R - 1).bit_length())
ranks = defaultdict(int)
TAGS = []
for _, signature in ROWS:
    TAGS.append(signature | (ranks[signature] << L))
    ranks[signature] += 1
require(len(set(TAGS)) == R, "physical row tags must remain distinct")


def addr(name, z):
    return INDEX[name] * N + z


def literal(name, z, positive=True):
    a = addr(name, z) + 1
    return a if positive else -a


def map_literal(lit):
    old = abs(lit) - 1
    row, z = divmod(old, N)
    new = TAGS[row] * N + z + 1
    return new if lit > 0 else -new


def copy_clauses(a, b):
    return [(-a, b), (a, -b)]


def xor_clauses(a, b, c):
    return [(a, b, -c), (a, -b, c), (-a, b, c), (-a, -b, -c)]


def and_clauses(a, b, c):
    return [(-a, -b, c), (a, -c), (b, -c)]


def clauses(no=False):
    out = []
    for z in range(N):
        out.append((literal("one", z),))
        for j in range(K):
            out.append((literal(f"z{j}", z, bool(z >> j & 1)),))
        for a, b, c in [("w0", "z0", "u"), ("w1", "z1", "v"),
                         ("u", "v", "sum")]:
            out += xor_clauses(literal(a, z), literal(b, z), literal(c, z))
        for a, b, c in [("u", "v", "uv"), ("w0", "w1", "p")]:
            out += and_clauses(literal(a, z), literal(b, z), literal(c, z))
        for a, b in [("u", "copy_u"), ("uv", "copy_uv")]:
            out += copy_clauses(literal(a, z), literal(b, z))
        out.append((-literal("p", z),))
        if no:
            out += [(literal("w0", z),), (literal("w1", z),)]
    # One globally shared witness: enforce the same w at every seed.
    for name in ("w0", "w1"):
        for z in range(1, N):
            out += copy_clauses(literal(name, 0), literal(name, z))
    return out


YES_CLAUSES = clauses()
NO_CLAUSES = clauses(True)
MAPPED_YES = [tuple(map_literal(l) for l in c) for c in YES_CLAUSES]
MAPPED_NO = [tuple(map_literal(l) for l in c) for c in NO_CLAUSES]


def basis(w, z):
    w0, w1 = w
    z0, z1 = z & 1, z >> 1 & 1
    return (1, w0, w1, z0, z1, (w0 ^ z0) & (w1 ^ z1), w0 & w1)


def completion(w, tag, z):
    b = basis(w, z)
    return sum(((tag >> i) & 1) * b[i] for i in range(L)) & 1


def physical(w):
    return [completion(w, sig, z) for _, sig in ROWS for z in range(N)]


def mapped_physical(values):
    out = [0] * Q
    for row in range(R):
        for z in range(N):
            out[TAGS[row] * N + z] = values[row * N + z]
    return out


def failures(values, cs):
    return sum(not any(values[abs(l) - 1] == (l > 0) for l in c) for c in cs)


def degree(table):
    co = table.copy()
    for j in range((len(table) - 1).bit_length()):
        for x in range(len(table)):
            if x >> j & 1:
                co[x] ^= co[x ^ (1 << j)]
    return max((i.bit_count() for i, b in enumerate(co) if b), default=-1)


def exact_gate_controls():
    # Coefficients are twice the proposed charge, retaining integer arithmetic.
    checked = 0
    for gate, cfun in (("and", and_clauses), ("xor", xor_clauses)):
        for a, b in product(range(2), repeat=2):
            c = a & b if gate == "and" else a ^ b
            for errors in product(range(2), repeat=3):
                bits = [a ^ errors[0], b ^ errors[1], c ^ errors[2]]
                cost = 2 * failures(bits, cfun(1, 2, 3))
                charges = (2, 2, 4) if gate == "and" else (2, 2, 2)
                require(cost <= sum(q * e for q, e in zip(charges, errors)), "gate charge")
                if gate == "and" and a == b == 0:
                    require(cost <= errors[0] + errors[1] + 4 * errors[2], "zero AND charge")
                checked += 1
    for a in range(2):
        for e0, e1 in product(range(2), repeat=2):
            require(failures([a ^ e0, a ^ e1], copy_clauses(1, 2)) <= e0 + e1, "copy charge")
            checked += 1
    return checked


def loads(w):
    result = [Fraction(0) for _ in range(R * N)]
    def add(name, z, val):
        result[addr(name, z)] += val
    for z in range(N):
        for name in ("one", "z0", "z1"):
            add(name, z, 1)
        for a, b, c in [("w0", "z0", "u"), ("w1", "z1", "v"), ("u", "v", "sum")]:
            for name in (a, b, c):
                add(name, z, 1)
        for name in ("u", "v"):
            add(name, z, 1)
        add("uv", z, 2)
        for name in ("w0", "w1"):
            add(name, z, Fraction(1, 2) if w == (0, 0) else 1)
        add("p", z, 2)
        add("p", z, 1)
        for a, b in [("u", "copy_u"), ("uv", "copy_uv")]:
            add(a, z, 1)
            add(b, z, 1)
    for name in ("w0", "w1"):
        for z in range(1, N):
            add(name, 0, 1)
            add(name, z, 1)
    return result


def main():
    require(len(YES_CLAUSES) == 116 and len(NO_CLAUSES) == 124, "actual clause census")
    require(R == 12 and compact_Q == 64 and Q == 1024, "actual storage census")
    local_controls = exact_gate_controls()
    # On each seed, p = w0 AND w1 together with w0=w1=1 and p=0 is
    # inconsistent, even if all other proof cells are arbitrary.
    local_no = and_clauses(1, 2, 3) + [(1,), (2,), (-3,)]
    local_no_values = [failures(list(x), local_no) for x in product(range(2), repeat=3)]
    require(min(local_no_values) == 1, "per-seed NO lower bound")
    reports = []
    rng = random.Random(20261124)
    mixed_checked = 0
    for w in product(range(2), repeat=2):
        values = physical(w)
        moved = mapped_physical(values)
        f_yes, f_no = failures(values, YES_CLAUSES), failures(values, NO_CLAUSES)
        require(failures(moved, MAPPED_YES) == f_yes, "honest YES reindex")
        require(failures(moved, MAPPED_NO) == f_no, "honest NO reindex")
        require((f_yes == 0) == (w[0] * w[1] == 0), "actual satisfying witness relation")
        require(f_no >= N, "NO lower bound")
        table = [completion(w, t, z) for t in range(1 << tag_bits) for z in range(N)]
        for row in range(R):
            for z in range(N):
                require(table[TAGS[row] * N + z] == values[row * N + z], "used-cell completion")
        d = degree(table)
        require(d == 3, "canonical exact degree")
        # These two full seed slices form an affine 3-cube. Their union has
        # odd parity, forcing degree >=3 for EVERY completion of used cells.
        parity_rows = (INDEX["one"], INDEX["uv"])
        parity = sum(values[row * N + z] for row in parity_rows for z in range(N)) & 1
        require(parity == 1, "padding-independent affine-cube lower bound")
        max_ratio = Fraction(0)
        sigma = max(loads(w)) if f_yes == 0 else None
        if f_yes == 0:
            expected = Fraction(9, 2) if w == (0, 0) else Fraction(5)
            require(sigma == expected, "global mixed-error charge bound")
            require(Fraction(N, 1) / sigma < 1, "one-error obstruction exceeds strict budget")
            for n in (1, 2):
                for sites in combinations(range(R * N), n):
                    changed = values.copy()
                    for p in sites:
                        changed[p] ^= 1
                    fails = failures(changed, YES_CLAUSES)
                    require(Fraction(fails, n) <= sigma, "mixed-error charge control")
                    require(failures(mapped_physical(changed), MAPPED_YES) == fails, "signed mixed-error reindex")
                    max_ratio = max(max_ratio, Fraction(fails, n))
                    mixed_checked += 1
            require(max_ratio == sigma, "attaining error set for exact sigma")
        for _ in range(256):
            changed = [rng.randrange(2) for _ in range(R * N)]
            mapped = mapped_physical(changed)
            for cs, mcs in ((YES_CLAUSES, MAPPED_YES), (NO_CLAUSES, MAPPED_NO)):
                require(failures(changed, cs) == failures(mapped, mcs), "arbitrary global assignment reindex")
            if sigma is not None:
                errors = sum(a != b for a, b in zip(changed, values))
                require(failures(changed, YES_CLAUSES) <= sigma * errors, "global charge control")
            mixed_checked += 1
        reports.append({"witness": list(w), "yes_failures": f_yes, "no_failures": f_no,
                        "minimum_exact_degree_over_padding": d,
                        "minimum_budgeted_degree_over_padding": d if sigma is not None else None,
                        "signed_sigma": str(sigma) if sigma is not None else None})
    require(failures(physical((1, 1)), NO_CLAUSES) == N, "NO lower bound attainment")
    return {
        "scope": "new standalone relation w0*w1=0; not Expedition046",
        "witness_bits": 2, "seed_bits": K, "seed_count": N,
        "and_gates": 2, "and_depth": 1, "xor_gates": 3, "copy_gates": 2,
        "dictionary_dimension": L, "rank_bits": rank_bits,
        "rows": R, "yes_expanded_clauses": len(YES_CLAUSES), "no_expanded_clauses": len(NO_CLAUSES),
        "compact_Q": compact_Q, "public_dictionary_Q": Q, "storage_factor": Q // compact_Q,
        "public_tags": TAGS, "satisfying_witnesses": 3, "raw_NO_minimum": N,
        "global_mixed_error_sigma_max": "5", "strict_uniform_error_threshold": "1/1280",
        "local_charge_controls": local_controls, "global_assignment_controls": mixed_checked,
        "witness_results": reports,
        "limits": ["written argument plus exact finite checks; no Lean acceptance",
                   "no novelty, hard language, or general PCP claim",
                   "exact degree applies to this example and all its padding completions",
                   "all-assignment reindex invariance follows from injection; finite controls are not its proof"],
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
