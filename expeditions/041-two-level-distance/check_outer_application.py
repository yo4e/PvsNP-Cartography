"""Check the finite GF(256) ACSP residual against the paired physical RS verifier."""
from functools import reduce
from operator import xor
import json

import two_level_oracle as rs


def require(ok, message):
    if not ok:
        raise ValueError(message)


def base_product(a, b):
    """Carryless product followed by long division modulo X^8+X^4+X^3+X+1."""
    raw = reduce(xor, (a << k for k in range(8) if b & (1 << k)), 0)
    for k in range(raw.bit_length() - 1, 7, -1):
        if raw & (1 << k):
            raw ^= 0x11B << (k - 8)
    return raw


def product(values):
    return reduce(base_product, values, 1)


def vanishing_at(points, x):
    return product(x ^ h for h in points)


def vanishing_coefficients(points):
    polynomial = [1]
    for h in points:
        extended = [0] * (len(polynomial) + 1)
        for degree, coeff in enumerate(polynomial):
            extended[degree] ^= base_product(h, coeff)
            extended[degree + 1] ^= coeff
        polynomial = extended
    return polynomial


def evaluate(polynomial, x):
    return reduce(lambda high, coeff: base_product(x, high) ^ coeff, reversed(polynomial), 0)


def residual(a, b, x, no):
    first_last = x if no else x ^ 1
    second = x ^ 1 if no else x
    at_range = a[x ^ 2]
    return (product((vanishing_at((1, 2, 3), x), a[x] ^ 1, a[x] ^ 1, a[first_last] ^ 1))
            ^ product((vanishing_at((0, 2, 3), x), a[second], a[second], a[second]))
            ^ product((vanishing_at((0, 1), x), at_range, at_range ^ 1))
            ^ product((vanishing_at(range(4), x), b[x])))


def affine_root(a):
    constant, slope = a[0], a[1] ^ a[0]
    return all(base_product(slope, x) ^ constant == actual for x, actual in enumerate(a))


def physical_extension(root_values, leaves):
    """Fill each row from the interpolant on its shared parent sites, in physical order."""
    cells = [0] * rs.WORD_COUNT
    cells[:256] = root_values
    def extend_row(abscissae, cutoff, addresses):
        anchors = [cells[idx] for idx in addresses[:cutoff]]
        weights = rs.check_weights(abscissae, cutoff)
        for idx, row in zip(addresses[cutoff:], weights):
            cells[idx] = reduce(xor, (rs.mul(w, y) for w, y in zip(row, anchors)), 0)

    for v, (origin, basis) in enumerate(rs.OUTER_COORDS):
        points = tuple(origin ^ rs.vector(basis, w) for w in range(128))
        extend_row(points, 16, [rs.outer_cell(v, w) for w in range(128)])
        for j in range(16):
            leaf = leaves["inner_row", v, j]
            extend_row(leaf.points, leaf.cutoff, leaf.addresses)
    return cells


def measure(name, a, cells, no, leaves, expected):
    direct_pass = affine_root(a)
    residual_pass = {x for x in range(256) if residual(a, cells, x, no) == 0}
    _, rs_pass, passing_leaves = rs.run_check(leaves, cells)
    accepted = residual_pass & rs_pass if direct_pass else set()
    require(accepted == expected, f"joint acceptance mismatch: {name}")
    return {"affine_A": direct_pass, "ACSP_accepts": len(residual_pass),
            "paired_RS_accepts": len(rs_pass), "joint_accepts": len(accepted),
            "joint_rejects": 256 - len(accepted), "passing_leaves": passing_leaves}


def run():
    f = range(256)
    require(all(base_product(x, y) == rs.BASE[x][y] for x in f for y in f),
            "scalar and geometry field tables disagree")
    leaves = rs.geometry()
    a_yes = [x ^ 1 for x in f]
    a_no = [0] * 256
    nodes = list(range(4, 36))
    u = vanishing_coefficients(nodes)
    scale = next(x for x in f if base_product(x, u[0]) == 1)
    b_coeffs = [base_product(scale, c) for c in u[1:]]
    require(len(b_coeffs) == 32 and b_coeffs[-1] != 0, "quotient degree is not 31")
    b_no = [evaluate(b_coeffs, x) for x in f]
    require(all(base_product(x, b_no[x]) == 1 for x in nodes), "failed interpolation")
    require(all(residual(a_no, b_no, x, True)
                == product((vanishing_at((1, 2, 3), x), vanishing_at(nodes, x), scale))
                for x in f), "NO residual factorization mismatch")
    c_yes = physical_extension(list(f), leaves)
    c_no = physical_extension(b_no, leaves)
    records = {}
    records["YES"] = measure("YES", a_yes, c_yes, False, leaves, set(f))
    records["NO_extremizer"] = measure("NO_extremizer", a_no, c_no, True, leaves,
                                      set(range(1, 36)))
    c_no[48] ^= 1
    records["NO_noncode_at_48"] = measure("NO_noncode_at_48", a_no, c_no, True, leaves,
                                         set(range(1, 36)))
    require(records["NO_noncode_at_48"]["paired_RS_accepts"] == 240,
            "paired RS should exclude the one damaged coset")
    return {"field_size": 256, "seed_count": 256, "witness_degree": len(b_coeffs) - 1,
            "NO_accepting_seeds": list(range(1, 36)), "fixtures": records}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
