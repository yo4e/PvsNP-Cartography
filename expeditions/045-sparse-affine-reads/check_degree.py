"""Exact ANF degree of one specified, zero-padded cross YES proof function.

Only Python's standard library is required. Truth-table position is the
little-endian integer (physical tag << 7) | seed. The first six Boolean
Mobius stages run within 64-bit Python integers, and all higher stages XOR
whole words. This is a fixed-target audit, not an optimization over padding,
satisfying proofs, or polynomial approximants.
"""
import hashlib
import json
import random
import struct

from sparse_compiler import build, rs


LOCAL_STAGES = (
    (1, 0x5555555555555555),
    (2, 0x3333333333333333),
    (4, 0x0F0F0F0F0F0F0F0F),
    (8, 0x00FF00FF00FF00FF),
    (16, 0x0000FFFF0000FFFF),
    (32, 0x00000000FFFFFFFF),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def mobius_words(words, address_bits):
    require(address_bits >= 0, "negative dimension")
    require(len(words) == 1 << max(0, address_bits - 6), "wrong word count")
    require(all(0 <= word < 1 << 64 for word in words), "invalid word")
    transformed = list(words)
    for shift, mask in LOCAL_STAGES[:min(6, address_bits)]:
        for i, word in enumerate(transformed):
            transformed[i] = word ^ ((word & mask) << shift)
    for axis in range(max(0, address_bits - 6)):
        stride = 1 << axis
        for start in range(0, len(transformed), 2 * stride):
            for i in range(start, start + stride):
                transformed[i + stride] ^= transformed[i]
    return transformed


def bit(words, address):
    return (words[address >> 6] >> (address & 63)) & 1


def pack_small(table):
    words = [0] * max(1, (len(table) + 63) // 64)
    for address, value in enumerate(table):
        require(value in (0, 1), "non-Boolean table")
        words[address >> 6] |= value << (address & 63)
    return words


def subset_parity(words, mask):
    """Direct subset definition; independent of packed butterfly stages."""
    if mask == len(words) * 64 - 1:
        return sum(word.bit_count() for word in words) & 1
    value = 0
    submask = mask
    while True:
        value ^= bit(words, submask)
        if submask == 0:
            return value
        submask = (submask - 1) & mask


def scalar_controls():
    rng = random.Random(452218)
    cases = 0
    exhaustive = 0
    for n in range(9):
        size = 1 << n
        if n <= 3:
            tables = [[(encoded >> x) & 1 for x in range(size)]
                      for encoded in range(1 << size)]
            exhaustive += len(tables)
        else:
            tables = [[rng.getrandbits(1) for _ in range(size)] for _ in range(16)]
            # Include monomials crossing the within-word / between-word
            # boundary, as well as the constant and full-degree monomial.
            for monomial in (0, 1, 1 << (n - 1), size - 1):
                tables.append([int((x & monomial) == monomial) for x in range(size)])
        for table in tables:
            original = pack_small(table)
            transformed = mobius_words(original, n)
            require(all(bit(transformed, mask) == subset_parity(original, mask)
                        for mask in range(size)), "small scalar ANF convention mismatch")
            require(mobius_words(transformed, n) == original, "small transform inversion")
            cases += 1
    return {"scalar_tables_compared": cases,
            "exhaustive_tables_at_dimensions_0_through_3": exhaustive,
            "largest_scalar_dimension": 8,
            "random_seed": 452218,
            "monomial_index_convention": "bit i of mask means variable i is present"}


def summarize_coefficients(coefficients, address_bits):
    histogram = [0] * (address_bits + 1)
    highest = -1
    leading = []
    for block, word in enumerate(coefficients):
        while word:
            lowest = word & -word
            index = (block << 6) | (lowest.bit_length() - 1)
            degree = index.bit_count()
            histogram[degree] += 1
            if degree > highest:
                highest = degree
                leading = [index]
            elif degree == highest:
                leading.append(index)
            word ^= lowest
    return highest, histogram, leading


def main():
    controls = scalar_controls()
    circuit, layout = build(no=False, cap=21, radius="cross")
    a = [x ^ 1 for x in range(128)]
    cells = rs.honest_cells([0, 1])
    physical = layout.pack_assignment(circuit.evaluate(a, cells))
    require(layout.failures(physical) == 0, "chosen reference is not satisfying")
    padded_rows = 1 << (layout.num_tags - 1).bit_length()
    Q = 128 * padded_rows
    n = Q.bit_length() - 1
    require(Q == 1 << n and n == 22, "unexpected address cube")
    require(layout.num_tags == 21845, "unexpected cross reference layout")
    packed_truth = b"".join(word.to_bytes(16, "little") for word in physical)
    packed_truth += bytes((padded_rows - layout.num_tags) * 16)
    words = list(struct.unpack(f"<{Q // 64}Q", packed_truth))
    coefficients = mobius_words(words, n)
    require(mobius_words(coefficients, n) == words, "full-cube transform inversion")
    degree, histogram, leading = summarize_coefficients(coefficients, n)
    require(degree == 18 and len(leading) == 202, "changed target degree checkpoint")
    require(sum(histogram) == 1261076, "changed coefficient support checkpoint")
    packed_coefficients = struct.pack(f"<{len(coefficients)}Q", *coefficients)

    # Direct coefficient checks use the original truth table, not a second
    # call to the butterfly implementation.
    leading_controls = sorted({leading[0], leading[len(leading) // 2], leading[-1]})
    require(all(subset_parity(words, index) == 1 for index in leading_controls),
            "leading coefficient did not match direct subcube parity")

    # Evaluate the complete recovered ANF by its subset definition at selected
    # actual input addresses. Full inversion already checks all Q truth values.
    rng = random.Random(452222)
    addresses = {0, 127, 128, layout.num_tags * 128 - 1,
                 layout.num_tags * 128, Q - 1}
    addresses.update(1 << axis for axis in range(n))
    addresses.update(rng.randrange(Q) for _ in range(64))
    require(all(subset_parity(coefficients, address) == bit(words, address)
                for address in addresses), "direct ANF evaluation mismatch")

    threshold_numerator, threshold_denominator = 109, 23
    min_lower_degree_error_weight = 1 << (n - degree)
    require(min_lower_degree_error_weight * threshold_denominator > threshold_numerator,
            "minimum-distance argument does not exclude the threshold")
    result = {
        "target": {
            "schedule": "cross", "private_fanout_cap": 21,
            "A": "A(x)=1+x in GF(128)", "B": "B(x)=x with the honest shared extension",
            "address_convention": "integer address = (physical tag << 7) | seed; variable 0 is LSB",
            "used_rows": layout.num_tags, "padded_rows": padded_rows,
            "zero_padding_rows": padded_rows - layout.num_tags,
            "address_bits": n, "Q": Q,
            "padding": "Every bit of every unused tag row is explicitly zero",
            "truth_table_weight": sum(word.bit_count() for word in words),
            "packed_truth_sha256": hashlib.sha256(packed_truth).hexdigest(),
        },
        "anf": {
            "exact_degree": degree, "nonzero_coefficients": sum(histogram),
            "coefficient_degree_histogram": histogram,
            "highest_degree_coefficients": len(leading),
            "highest_degree_monomial_indices": leading,
            "packed_coefficients_sha256": hashlib.sha256(packed_coefficients).hexdigest(),
            "directly_checked_leading_indices": leading_controls,
        },
        "verification": controls | {
            "full_inversion_bits_checked": Q,
            "direct_anf_evaluation_addresses": len(addresses),
            "direct_evaluation_random_seed": 452222,
            "truthful_physical_clause_failures": 0,
            "external_runtime_dependencies": [],
        },
        "approximation_consequence": {
            "polynomials_excluded": "Every GF(2) polynomial of total degree at most17, after Boolean multilinearization",
            "minimum_wrong_bits": min_lower_degree_error_weight,
            "strict_transfer_mean_wrong_bit_threshold": "109/23",
            "guaranteed_arbitrary_integer_error_radius": 4,
            "fixed_target_least_degree_meeting_threshold": 18,
            "reason": "For a degree<=17 approximant p, f+p is nonzero of degree18; the written minimum-weight lemma gives weight>=2^(22-18)=16. An exact degree18 representation exists.",
        },
        "scope": "Only this specified honest YES assignment with explicit zero padding. No minimum over free padding, other satisfying proofs, or compiler encodings; no new Lean check or novelty claim.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
