"""Unshifted GF(256) root certificate for the two-level parity witness.

This small verifier does not import the recursive proof implementation. It
enumerates all coordinates and constant targets, not all degree-31 polynomials.
The latter bound uses the root theorem as explained in counterexample.md.
"""
from collections import Counter
from fractions import Fraction
import json


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def multiply(x, y):
    """Polynomial product and long division modulo X^8 + X^4 + X^3 + X + 1."""
    p = 0
    for i in range(8):
        if y & (1 << i):
            p ^= x << i
    while p.bit_length() > 8:
        p ^= 0x11B << (p.bit_length() - 9)
    return p


def ext_product(x, y):
    # E = F[theta]/(theta^2+theta+32); hi and lo are F-coefficients.
    a, b, c, d = x & 255, x >> 8, y & 255, y >> 8
    bd = multiply(b, d)
    return ((multiply(a, c) ^ multiply(32, bd)) |
            ((multiply(a, d) ^ multiply(b, c) ^ bd) << 8))


def vanishing(points, x):
    value = 1
    for root in points:
        value = ext_product(value, x ^ root)
    return value


def alternate_basis_control():
    # Only outer row zero differs from the zero proof. Vary the two
    # auxiliary directions in the recursive row's child geometry.
    theta = 256
    c0, c1, c2 = 16*theta, 17, 32
    outer_basis_for_v0 = (1, 2, 4, 8, 4*theta, 8*theta, 2*theta ^ theta)
    family = {0}
    for direction in (theta, *outer_basis_for_v0, c0, c1, c2):
        require(direction not in family, "alternate basis lost rank")
        family |= {p ^ direction for p in family}

    def at_parent_coordinate(w):
        return theta ^ (w & 15) ^ (4*theta if w & 16 else 0) ^ (
            8*theta if w & 32 else 0) ^ (2*theta ^ theta if w & 64 else 0)

    zeros = (c0, c0 ^ c1, c0 ^ c2, c0 ^ c1 ^ c2)
    bad_columns = []
    counts = []
    root = [0]*256
    for j in range(16):
        beta = at_parent_coordinate(8*j)
        row_values = []
        for i in range(64):
            x = beta ^ (i & 7) ^ (c1 if i & 8 else 0) ^ (
                c2 if i & 16 else 0) ^ (c0 ^ beta if i & 32 else 0)
            y = vanishing(zeros, x) if j < 2 else 0
            row_values.append(y)
            if i < 8:
                if j < 2:
                    require(0 < y < 256, "root symbol on support must lie in the base field")
                    root[8*j + i] = y
                else:
                    require(y == 0, "all outer extension aliases must remain zero")
        counts.append(row_values)
    for column in range(32):
        values = [row[32 + column] for row in counts]
        if any(values):
            require(values[0] == values[1] != 0 and set(values[2:]) == {0},
                    "column root-count witness failed")
            bad_columns.append(column)
    require(bad_columns == [c for c in range(32) if c % 8 != 0], "column pattern")
    bad_set = {z for z in range(256) if z >> 4 == 0 and any(
        z % 8 + 8*f in bad_columns for f in range(4))}
    paired = {z for z in range(256) if z in bad_set or (z ^ 8) in bad_set}
    require(len(bad_set) == 14 and paired == bad_set, "XOR8 control did not survive")
    support = sum(y != 0 for y in root)
    require(support == 16 and 256 - support - 31 > support, "wrong nearest codeword")
    return {"scope": "alternate legal inner auxiliary basis in row zero",
            "inner_aux_field_encodings": [c0, c1, c2],
            "nonzero_root_values": root[:support], "root_distance_in_symbols": support,
            "failing_inner_columns_in_row_zero": len(bad_columns),
            "ordinary_rejected_seeds": sorted(bad_set), "xor8_rejected_seeds": sorted(paired)}


def matrix_rank(rows):
    rows = [list(row) for row in rows]
    pivots = 0
    for j in range(len(rows[0])):
        source = next((i for i in range(pivots, len(rows)) if rows[i][j]), None)
        if source is None:
            continue
        rows[pivots], rows[source] = rows[source], rows[pivots]
        pivot = rows[pivots]
        scalar = next(a for a in range(1, 256) if multiply(a, pivot[j]) == 1)
        pivot[:] = [multiply(scalar, a) for a in pivot]
        for i in range(pivots + 1, len(rows)):
            factor = rows[i][j]
            rows[i] = [x ^ multiply(factor, y) for x, y in zip(rows[i], pivot)]
        pivots += 1
    return pivots


def interpolation_ansatz_ranks():
    # A leaf polynomial of degree <8 with four prescribed zeros factors
    # as D*T with deg T<4. These are eight F-linear conditions that D*T
    # has zero theta component on all eight external parent points.
    theta = 256
    out = {}
    for name, (c1, c2) in {"standard": (32*theta, 64*theta), "alternate": (17, 32)}.items():
        ranks = []
        zeros = [16*theta ^ d for d in (0, c1, c2, c1 ^ c2)]
        for j in (0, 1):
            matrix = []
            for i in range(8):
                x = theta ^ (j*8 + i)
                y = vanishing(zeros, x)
                row = []
                for _ in range(4):
                    row.extend([y >> 8, ext_product(y, theta) >> 8])
                    y = ext_product(y, x)
                matrix.append(row)
            ranks.append(matrix_rank(matrix))
        out[name] = ranks
    require(out["standard"] == [8, 8] and max(out["alternate"]) < 8,
            "expected auxiliary basis distinction was lost")
    return out


def frobenius32(x):
    for _ in range(5):
        x = multiply(x, x)
    return x


def row_choice(z):
    return (z >> 4) & 1


def primary_schedule_pass(z):
    return (z >> 3) & 1 == row_choice(z)


def main():
    xs = range(256)
    high_values = [frobenius32(x) for x in xs]
    require(sorted(high_values) == list(xs), "32nd powers are not a permutation")
    root = [row_choice(x) if primary_schedule_pass(x) else high_values[x] for x in xs]
    blocks = [sum(primary_schedule_pass(x) and row_choice(x) == v for x in xs) for v in (0, 1)]
    disagreement_block = sum(not primary_schedule_pass(x) for x in xs)
    require(blocks + [disagreement_block] == [64, 64, 128], "wrong root partition")

    # On these disjoint blocks a nonconstant candidate h of degree <=31
    # must respectively solve h(x)=0, h(x)=1 or h(x)=x^32. Each difference
    # is nonzero, with degree <=31, <=31, or exactly 32.
    nonconstant_cap = sum(min(size, degree) for size, degree in zip(blocks + [disagreement_block],
                                                                    [31, 31, 32]))
    histogram = Counter(root)
    constant_cap = max(histogram.values())
    require(constant_cap == 64, "unexpected constant agreement")
    require(root[0] == 0 and root[1] == 0, "boundary word changed")
    cap = max(nonconstant_cap, constant_cap)
    lower_distance = 256 - cap
    upper_distance = 256 - constant_cap
    reject_counts = {shift: sum(not (primary_schedule_pass(z) and primary_schedule_pass(z ^ shift))
                                for z in xs) for shift in range(256)}
    require(set(reject_counts.values()) == {128, 256}, "unexpected two-seed outcomes")
    for shift, count in reject_counts.items():
        flip = ((shift >> 3) ^ (shift >> 4)) & 1
        require(count == (256 if flip else 128), "shift classification mismatch")
    require(reject_counts[0] < lower_distance, "no contradiction to distance domination")
    p = Fraction(reject_counts[0], 256)
    return {"alternate_basis_xor8_control": alternate_basis_control(), "modulus": "0x11b",
            "quartic_factor_ansatz_F_ranks_at_two_external_rows": interpolation_ansatz_ranks(), "degree_cutoff_exclusive": 32,
            "root_block_sizes": {"forced_0": blocks[0], "forced_1": blocks[1],
                                 "external_x_to_32": disagreement_block},
            "constant_max_agreement": constant_cap,
            "maximizing_constants": [a for a in xs if histogram[a] == constant_cap],
            "nonconstant_agreement_upper_bound": nonconstant_cap,
            "distance_in_symbols_lower_bound": lower_distance,
            "distance_in_symbols_upper_bound_from_constants": upper_distance,
            "rejection_original": str(p),
            "ratio_rejection_over_distance_upper_bound": str(p / Fraction(lower_distance, 256)),
            "two_seed_rejections": {hex(t): reject_counts[t] for t in (0, 1, 8, 16, 24)},
            "number_of_xor_shifts_by_rejected_seeds": dict(sorted(Counter(reject_counts.values()).items()))}


if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, indent=2))
