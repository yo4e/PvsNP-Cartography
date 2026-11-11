"""Exact finite controls for two interfaces of the recursive query reconstruction."""

import json
from collections import Counter
from itertools import product


def check(condition, reason):
    if not condition:
        raise ValueError(reason)


def multiply(left, right):
    """Polynomial-basis GF(16), modulo X^4 + X + 1."""
    result = 0
    while right:
        if right & 1:
            result ^= left
        right >>= 1
        left <<= 1
        if left & 16:
            left ^= 19
    return result


def field_control():
    field = tuple(range(16))
    base = tuple(x for x in field if multiply(multiply(x, x), multiply(x, x)) == x)
    check(len(base) == 4, "subfield size")
    theta = next(x for x in field if x not in base)
    projection = {c ^ multiply(theta, d): c for c, d in product(base, repeat=2)}
    check(len(projection) == 16, "extension coordinates are not unique")
    coset = {theta ^ x for x in base}
    check(coset.isdisjoint(base), "affine origin")
    words = list(product(base, repeat=4))
    base_code = {tuple(c ^ multiply(d, x) for x in base) for c, d in product(base, repeat=2)}
    extension_code = []
    for c, d in product(field, repeat=2):
        word = tuple(c ^ multiply(d, theta ^ x) for x in base)
        shifted = c ^ multiply(d, theta)
        projected_word = tuple(projection[shifted] ^ multiply(projection[d], x) for x in base)
        check(tuple(projection[y] for y in word) == projected_word, "coefficient projection")
        check(projected_word in base_code, "degree-one projection leaves base code")
        extension_code.append(word)
    histogram = Counter()
    for word in words:
        def nearest(code):
            return min(sum(v != w for v, w in zip(candidate, word)) for candidate in code)
        distance = nearest(base_code)
        check(distance == nearest(extension_code), "embedding changed distance")
        histogram[distance] += 1
    return {"subfield_size": len(base), "ambient_size": len(field),
            "base_words": len(words), "affine_extension_polynomials": len(extension_code),
            "distance_histogram": dict(sorted(histogram.items()))}


def public_bit_control():
    # Public decision on a two-bit seed: accept iff the two public bits XOR to 1.
    # A dishonest proof can freely choose two alleged public bits and an XOR gate
    # at each of four seeds. All clauses have fixed signs and width at most three.
    seeds = range(4)
    pins = [(b, value) for b in range(2) for value in range(2)]
    clauses = [((0, 1), (1, 1), (2, 0)), ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 0), (2, 1)), ((0, 0), (1, 1), (2, 1)),
               ((2, 1),)]
    clamped = {(z, b, v): (z & ~(1 << b)) | (v << b)
               for z in seeds for b, v in pins}
    for b, v in pins:
        multiplicities = Counter(clamped[z, b, v] for z in seeds)
        check(sorted(multiplicities.values()) == [2, 2], "pin address fibers")
    # Sum over unnormalized test types and uniform seeds. A bad public bit at a
    # given seed contributes twice to the total pin failure count.
    expected_bad = sum((z.bit_count() % 2) == 0 for z in seeds)
    best, best_without_pins = 1000, 1000
    for rows in product(range(8), repeat=4):
        def bit(z, wire):
            return (rows[z] >> wire) & 1
        circuit_bad = sum(not any(bit(z, w) == truth for w, truth in clause)
                          for z in seeds for clause in clauses)
        pin_bad = sum(bit(clamped[z, b, v], b) != v for z in seeds for b, v in pins)
        wrong_public_bits = sum(bit(z, b) != ((z >> b) & 1) for z in seeds for b in range(2))
        check(pin_bad == 2 * wrong_public_bits, "clamped pin accounting")
        check(circuit_bad + wrong_public_bits >= expected_bad, "compiled rejection bound")
        best = min(best, circuit_bad + pin_bad)
        best_without_pins = min(best_without_pins, circuit_bad)
    check(best_without_pins == 0 and best == expected_bad, "cheating or tightness control")
    return {"arbitrary_global_wire_tables": 8 ** 4, "original_rejecting_seeds": expected_bad,
            "total_seed_test_pairs": len(seeds) * (len(pins) + len(clauses)),
            "minimum_rejected_pairs": best, "minimum_without_public_pins": best_without_pins}


if __name__ == "__main__":
    print(json.dumps({"extension_distance": field_control(), "public_seed": public_bit_control()},
                     indent=2, sort_keys=True))
