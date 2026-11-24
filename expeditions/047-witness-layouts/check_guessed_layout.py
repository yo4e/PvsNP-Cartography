#!/usr/bin/env python3
"""Exact finite controls for a shared guessed row map.

The mathematical lemma is in sources-and-quantifiers.md.  This checker
does not import the preceding compiler or enumerate an asymptotic family.
All checks remain enabled under python -O.
"""
from collections import Counter
from itertools import permutations, product
import json


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def bit(word, index):
    return (word >> index) & 1


def parity(word):
    return word.bit_count() & 1


def anf_degree(values):
    coefficients = list(values)
    check(len(values) > 0 and len(values) & (len(values) - 1) == 0,
          "truth table size")
    for j in range(len(values).bit_length() - 1):
        for mask in range(len(values)):
            if mask & (1 << j):
                coefficients[mask] ^= coefficients[mask ^ (1 << j)]
    return max((mask.bit_count() for mask, c in enumerate(coefficients) if c),
               default=0)


# A(z)=B(z xor 1), B(z xor 1)=C(z xor 2), A(z)!=C(z xor 2).
# Each equality/inequality is represented by two signed clauses.
K, N, ROWS = 2, 4, 3
TEMPLATES = (
    ((0, 0, False), (1, 1, True)),
    ((0, 0, True), (1, 1, False)),
    ((1, 1, False), (2, 2, True)),
    ((1, 1, True), (2, 2, False)),
    ((0, 0, True), (2, 2, True)),
    ((0, 0, False), (2, 2, False)),
)


def failures(reader):
    return sum(
        not any(bool(reader(row, z ^ delta)) == positive
                for row, delta, positive in clause)
        for z in range(N) for clause in TEMPLATES
    )


def main():
    # All physical old proofs, including nonconstant rows, establish the
    # finite NO minimum independently of any low-degree restriction.
    histogram = Counter()
    originals = []
    for proof in range(1 << (ROWS * N)):
        failed = failures(lambda row, z: bit(proof, row * N + z))
        histogram[failed] += 1
        originals.append(failed)
    check(min(histogram) == N, "triangle NO minimum")

    # Move rows to every permutation of one sparse set of occupied tags.
    # Padding is filled differently on each proof and is never queried.
    relabel_checks = 0
    for labels in permutations((0, 3, 5)):
        for proof, before in enumerate(originals):
            padded = [(parity(i & proof) ^ (i & 1)) for i in range(8 * N)]
            for row in range(ROWS):
                for z in range(N):
                    padded[labels[row] * N + z] = bit(proof, row * N + z)
            after = failures(lambda row, z: padded[labels[row] * N + z])
            check(before == after, "injective reindexing changed failures")
            relabel_checks += 1

    # Shared collisions still decode to a global original proof.  They
    # restrict the proof set; they cannot defeat a universal NO bound.
    # Exhaust every row map to two tag bits and every affine polynomial
    # on two tag plus two seed bits, rather than only injective maps.
    guessed_counts = Counter()
    minimum = {"injective": None, "colliding": None}
    substitution_degrees = Counter()
    for labels in product(range(4), repeat=ROWS):
        kind = "injective" if len(set(labels)) == ROWS else "colliding"
        for coeff in range(1 << 5):
            table = [bit(coeff, 0) ^ parity((coeff >> 1) & address)
                     for address in range(16)]
            failed = failures(lambda row, z: table[labels[row] * N + z])
            decoded = sum(table[labels[row] * N + z] << (row * N + z)
                          for row in range(ROWS) for z in range(N))
            check(failed == originals[decoded] and failed >= N,
                  "shared guessed map broke global soundness")
            guessed_counts[kind] += 1
            minimum[kind] = failed if minimum[kind] is None else min(minimum[kind], failed)
            # The failure polynomial of a width-two signed clause has
            # degree at most two after these signed projections.
            for clause in TEMPLATES:
                truth = [int(not any(bool(table[labels[row] * N + (z ^ delta)]) == positive
                                     for row, delta, positive in clause))
                         for z in range(N)]
                degree = anf_degree(truth)
                check(degree <= 2, "signed composition degree")
                substitution_degrees[degree] += 1

    # Deliberately invalid: choose different tags for two occurrences of
    # the SAME physical row.  Positive and negative units then both pass.
    original_units_minimum = min(
        sum((1 - bit(word, z)) + bit(word, z) for z in range(N))
        for word in range(1 << N)
    )
    detached_table = [tag for tag in range(2) for _ in range(N)]
    detached_units_failures = sum(
        (1 - detached_table[N + z]) + detached_table[z] for z in range(N)
    )
    check(original_units_minimum == N and detached_units_failures == 0,
          "detached-alias negative control")

    # Every constant row vector has an injective value/rank layout and
    # the SAME degree-one padded polynomial: read the high tag bit.
    # This layout depends on the witness; its table must be charged.
    adaptive_vectors, max_tag, max_rank = 0, 0, 0
    adaptive_examples = []
    for witness in range(256):
        counts = [0, 0]
        labels = []
        for row in range(8):
            value = bit(witness, row)
            labels.append(value * 8 + counts[value])
            counts[value] += 1
        check(len(set(labels)) == 8, "value/rank labels collided")
        for row, tag in enumerate(labels):
            check((tag >> 3) == bit(witness, row), "adaptive exact completion")
        adaptive_vectors += 1
        max_tag = max(max_tag, max(labels))
        max_rank = max(max_rank, max(counts))
        if witness in (0, 3, 85, 255):
            adaptive_examples.append({"witness": witness, "labels": labels})
    check(anf_degree([tag >> 3 for tag in range(16)]) == 1,
          "adaptive common polynomial degree")

    # At a FIXED list of eight four-bit tags the exact affine image has
    # at most 2^(4+1)=32 patterns.  Enumerate every occupied eight-tag set
    # to expose the contrast without assuming a particular fixed layout.
    from itertools import combinations
    fixed_pattern_histogram = Counter()
    for tags in combinations(range(16), 8):
        patterns = {
            sum((bit(coeff, 0) ^ parity((coeff >> 1) & tag)) << i
                for i, tag in enumerate(tags))
            for coeff in range(32)
        }
        check(len(patterns) <= 32 < 256, "fixed-layout affine capacity")
        fixed_pattern_histogram[len(patterns)] += 1
    check(sum(fixed_pattern_histogram.values()) == 12870, "tag-set enumeration")

    # Collisions preserve NO soundness but can multiply error sensitivity:
    # R identical positive unit rows, all true honestly, can share a tag.
    # One changed new cell violates R clauses instead of one.
    old_units = [1] * (8 * N)
    old_units[0] = 0
    merged_units = [1] * N
    merged_units[0] = 0
    old_singleton = sum(1 - value for value in old_units)
    merged_singleton = sum(1 - merged_units[z] for _row in range(8) for z in range(N))
    check(merged_singleton > old_singleton, "merged sensitivity control")

    result = {
        "scope": "finite row-map and signed-alias controls; no hierarchy or general verifier claim",
        "triangle": {
            "seed_bits": K, "rows": ROWS, "templates": len(TEMPLATES),
            "all_physical_proofs": len(originals),
            "failure_histogram": dict(sorted(histogram.items())),
            "NO_minimum": N, "injective_reindexing_checks": relabel_checks,
            "affine_guessed_maps": dict(sorted(guessed_counts.items())),
            "guessed_map_minima": minimum,
            "signed_clause_degree_histogram": dict(sorted(substitution_degrees.items())),
        },
        "detached_occurrence_attack": {
            "old_NO_minimum": original_units_minimum,
            "invalid_detached_failures": detached_units_failures,
            "invalid_change": "same old row assigned a different tag at each unit occurrence",
        },
        "adaptive_constant_rows": {
            "rows": 8, "all_witness_vectors": adaptive_vectors,
            "tag_bits": 4, "table_description_bits": 32,
            "padded_tag_slots": 16, "exact_degree": 1,
            "max_tag": max_tag, "max_signature_multiplicity": max_rank,
            "fixed_tag_sets": sum(fixed_pattern_histogram.values()),
            "fixed_exact_pattern_count_histogram": dict(sorted(fixed_pattern_histogram.items())),
            "examples": adaptive_examples,
        },
        "collision_sensitivity_attack": {
            "old_singleton_failure": old_singleton,
            "merged_singleton_failure": merged_singleton,
            "old_NO_soundness_survives": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
