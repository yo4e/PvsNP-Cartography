"""Exact finite tests for same-direction local correction on H={0,1} in GF(8)^2."""

import json
from fractions import Fraction
from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


def multiply(a, b):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011  # X^3 + X + 1.
    return value


def inverse(value):
    return next(x for x in range(1, 8) if multiply(x, value) == 1)


TAPS = (1, 2, 4)
GRID = tuple(product(range(2), repeat=2))
FIELD_POINTS = tuple(product(range(8), repeat=2))


def lagrange_weights():
    weights = []
    for t in TAPS:
        weight = 1
        for other in TAPS:
            if other != t:
                weight = multiply(weight, multiply(other, inverse(t ^ other)))
        weights.append(weight)
    return tuple(weights)


def lde_symbol(target, point):
    # Lagrange basis on {0,1} is (1+u, u) in characteristic two.
    value = 0
    for i, (a, b) in enumerate(GRID):
        if (target >> i) & 1:
            value ^= multiply(point[0] ^ (1 - a), point[1] ^ (1 - b))
    return value


def shift(x, direction, t):
    return tuple(u ^ multiply(t, a) for u, a in zip(x, direction))


def address(point, tag):
    return point[0] + (point[1] << 3) + (tag << 6)


def xor_values(bits):
    value = 0
    for bit in bits:
        value ^= bit
    return value


def correction_reads(x, direction, weights):
    return [address(shift(x, direction, t), j)
            for t, weight in zip(TAPS, weights) for j in range(3)
            if multiply(weight, 1 << j) & 1]


def degree_two_variable(values):
    constant, y, x, xy = values  # GRID enumerates 00, 01, 10, 11.
    if constant ^ y ^ x ^ xy:
        return 2
    return int(y != constant or x != constant)


def check_full_line():
    # Every nonzero field element has weight 1. Just one basis bit is stored.
    # x + t*a is a translation in characteristic two, for each fixed a,t.
    taps = range(1, 8)
    cases = 0
    for target in range(16):
        bits = {p: lde_symbol(target, p) & 1 for p in FIELD_POINTS}
        for i, x in enumerate(GRID):
            for a in FIELD_POINTS:
                predicted = xor_values(bits[shift(x, a, t)] for t in taps)
                require(predicted == (target >> i) & 1, "full-line identity")
                cases += 1
    x, bad_point = (0, 0), (1, 0)
    bad_directions = sum(xor_values(shift(x, a, t) == bad_point for t in taps)
                         for a in FIELD_POINTS)
    require(bad_directions == 7, "one flipped bit must attain the union bound")
    # At the first excluded degree, every nonzero t satisfies t^7 = 1.
    def power_seven(t):
        result = 1
        for _ in range(7):
            result = multiply(result, t)
        return result
    wrong = xor_values(power_seven(t) for t in taps)
    require(wrong == 1 and power_seven(0) == 0, "missing degree boundary failure")
    return {"exact_grid_decodes": cases, "single_flip_uniform_error": "1/64",
            "single_flip_fixed_anchor_error": str(Fraction(bad_directions, 64)),
            "boundary_degree": 7, "boundary_sum": wrong, "value_at_zero": 0}


def main():
    weights = lagrange_weights()
    require(len(set(TAPS)) == 3 and 0 not in TAPS, "invalid interpolation points")
    for j in range(3):
        require(xor_values(multiply(w, (1, t, multiply(t, t))[j])
                           for t, w in zip(TAPS, weights)) == int(j == 0),
                "incorrect moment for interpolation at zero")

    reads = {(x, a): correction_reads(x, a, weights) for x in GRID for a in FIELD_POINTS}
    field_decodes = 0
    for target in range(16):
        extension = {point: lde_symbol(target, point) for point in FIELD_POINTS}
        bits = {address(p, j): (extension[p] >> j) & 1 for p in FIELD_POINTS for j in range(3)}
        for index, x in enumerate(GRID):
            correct = (target >> index) & 1
            for a in FIELD_POINTS:
                symbol = xor_values(multiply(w, extension[shift(x, a, t)])
                                    for t, w in zip(TAPS, weights))
                binary = xor_values(bits[i] for i in reads[x, a])
                require(symbol == binary == correct, "honest decoding failed")
                field_decodes += 1

    # Corruption effects are target independent by linearity. Check every single
    # physical bit, including all unused tag-3 bits, then a multitag corruption.
    faults = [(i,) for i in range(256)]
    faults.append((address((0, 1), 0), address((2, 3), 1), address((7, 4), 2), address((4, 2), 3)))
    max_single = 0
    max_multi = 0
    for fault_set in faults:
        changed = set(fault_set)
        # Four equally sized tags, including the unused tag 3. A tap is uniform
        # on 64 field points, so sum of the three active tag error rates is at
        # most 4 times full-cube bit error. The union covers three taps.
        bound = 3 * 4 * Fraction(len(changed), 256)
        for x in GRID:
            wrong = sum(xor_values(int(i in changed) for i in reads[x, a]) for a in FIELD_POINTS)
            require(Fraction(wrong, 64) <= bound, "union bound on corrupt reads failed")
            if len(changed) == 1:
                max_single = max(max_single, wrong)
            else:
                max_multi = max(max_multi, wrong)

    # A decoder is linear in its oracle. Test every square-free monomial in
    # all eight input bits (including both tag bits) for each fixed direction.
    for mask in range(256):
        for a in FIELD_POINTS:
            values = [xor_values(int((i & mask) == mask) for i in reads[x, a]) for x in GRID]
            require(degree_two_variable(values) <= mask.bit_count(), "degree increased")

    target = 0b1000  # x*y on the Boolean grid.
    x = (0, 0)
    attack = None
    for a in FIELD_POINTS:
        if attack is not None:
            break
        directions = [a, (0, 0), (0, 0)]
        result = xor_values(multiply(w, lde_symbol(target, shift(x, di, t)))
                            for w, di, t in zip(weights, directions, TAPS))
        if result & 1:
            attack = {"field_directions": directions, "true_bit": 0, "decoded_bit": result & 1}
    require(attack is not None, "missing different-direction counterexample")
    return {"all_nonzero_taps": check_full_line(), "field_modulus": "X^3+X+1", "grid": "{0,1}^2", "taps": TAPS, "weights": weights,
            "honest_target_point_direction_cases": field_decodes, "directions_including_zero": 64,
            "fault_sets": len(faults), "fault_set_point_tests": 4 * len(faults),
            "maximum_single_bit_wrong_directions_over_64": max_single,
            "multiple_bit_wrong_directions_over_64_max_over_points": max_multi,
            "monomial_direction_pairs": 256 * 64, "different_direction_attack": attack}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
