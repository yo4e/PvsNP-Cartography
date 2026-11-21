"""Exact free-suffix padding completion for the fixed honest cross YES proof.

Used truth values are held fixed at every address below M=21845*128. This
does not optimize A/B choices or any other used physical proof bits. The
canonical completion keeps ANF coefficients indexed below M and sets all
remaining coefficients to zero. Only the standard library is required.
"""
import hashlib
import json
import struct

from sparse_compiler import build, rs
from check_degree import (bit, mobius_words, require, scalar_controls,
                          subset_parity, summarize_coefficients)


def packed(words):
    return struct.pack(f"<{len(words)}Q", *words)


def coset_parity(words, free_mask, base):
    require(free_mask & base == 0, "overlapping free and fixed variables")
    answer = 0
    subset = free_mask
    while True:
        answer ^= bit(words, base | subset)
        if subset == 0:
            return answer
        subset = (subset - 1) & free_mask


def main():
    controls = scalar_controls()
    circuit, layout = build(no=False, cap=21, radius="cross")
    a = [x ^ 1 for x in range(128)]
    cells = rs.honest_cells([0, 1])
    physical = layout.pack_assignment(circuit.evaluate(a, cells))
    require(layout.num_tags == 21845, "unexpected physical layout")
    require(layout.failures(physical) == 0, "chosen used proof is not satisfying")
    used_bits = layout.num_tags * 128
    Q, n = 1 << 22, 22
    require(used_bits % 64 == 0, "used prefix not word aligned")
    require(all(0 <= tag < layout.num_tags and 0 <= delta < 128
                for tag, delta in layout.read.values()), "query leaves used prefix")
    queried_tags = {layout.read[abs(literal)][0]
                    for clause in layout.templates for literal in clause}
    queried_tags.update(layout.read[wire][0] for wire in circuit.public)
    require(queried_tags == set(range(layout.num_tags)),
            "actual clause support has a hole in the claimed used prefix")
    source_packed = b"".join(word.to_bytes(16, "little") for word in physical)
    source_packed += bytes(Q // 8 - len(source_packed))
    source_words = list(struct.unpack(f"<{Q // 64}Q", source_packed))
    source_anf = mobius_words(source_words, n)
    source_degree, source_histogram, source_leading = summarize_coefficients(source_anf, n)
    require(source_degree == 18 and len(source_leading) == 202,
            "zero-padded reference changed")
    require(all(index >= used_bits for index in source_leading),
            "a degree18 coefficient is already forced by used bits")

    # Numeric prefixes are downward closed for the subset order on masks:
    # if T is a submask of S, then T<=S. Every coefficient below M is fixed
    # by values below M; coefficients outside that downset can be chosen.
    cut = used_bits // 64
    completion_anf = source_anf[:cut] + [0] * (len(source_anf) - cut)
    completion_words = mobius_words(completion_anf, n)
    require(completion_words[:cut] == source_words[:cut], "used truth values changed")
    require(mobius_words(completion_words, n) == completion_anf,
            "full completion transform inversion")
    degree, histogram, leading = summarize_coefficients(completion_anf, n)
    require(degree == 17 and len(leading) == 202 and sum(histogram) == 833770,
            "canonical completion checkpoint changed")
    require(all(index < used_bits for index in leading), "unforced leading term retained")
    completed_rows = [completion_words[2 * tag] | (completion_words[2 * tag + 1] << 64)
                      for tag in range(Q // 128)]
    require(completed_rows[:layout.num_tags] == physical, "physical used rows changed")
    # The evaluator reads only observed used tags; extra suffix rows are free.
    require(layout.failures(completed_rows) == 0, "completion violates a physical clause")
    completion_packed = packed(completion_words)

    # The entire first half is an immutable21-variable subcube, x21=0.
    half_bits, half_n = 1 << 21, 21
    require(half_bits <= used_bits, "first-half subcube is not wholly fixed")
    fixed_half_words = source_words[:half_bits // 64]
    half_anf = mobius_words(fixed_half_words, half_n)
    half_degree, half_histogram, half_leading = summarize_coefficients(half_anf, half_n)
    require(half_degree == 17 and len(half_leading) == 202,
            "fixed-half degree checkpoint changed")
    require(mobius_words(half_anf, half_n) == fixed_half_words, "fixed-half inversion")
    require(all(subset_parity(source_words, index) == 1
                for index in (leading[0], leading[len(leading) // 2], leading[-1])),
            "forced leading coefficient parity changed")

    # Independent lower-bound certificate: 16 disjoint17-dimensional
    # subcubes cover the fixed half. Each target parity is directly read
    # from used truth bits and is1. Any degree<=16 polynomial has parity0
    # on each such subcube and must therefore err in every one.
    free_mask = half_leading[0]
    require(free_mask.bit_count() == 17 and free_mask < half_bits, "bad free-variable mask")
    complementary = [i for i in range(half_n) if not (free_mask >> i) & 1]
    bases = [sum(((choice >> j) & 1) << i for j, i in enumerate(complementary))
             for choice in range(1 << len(complementary))]
    require(len(bases) == len(set(bases)) == 16, "wrong subcube partition")
    require(all(base & free_mask == 0 and base | free_mask < half_bits for base in bases),
            "parity certificate leaves fixed half")
    parities = [coset_parity(source_words, free_mask, base) for base in bases]
    require(parities == [1] * 16, "a subcube lacks the claimed odd target parity")
    require(16 * 23 > 109, "parity lower bound does not exclude transfer budget")

    changed_padding_bits = sum((new ^ old).bit_count()
                               for new, old in zip(completion_words, source_words))
    require(changed_padding_bits == sum(word.bit_count() for word in completion_words[cut:]),
            "change was not confined to formerly-zero free padding")
    result = {
        "fixed_used_target": {
            "schedule": "cross", "fanout_cap": 21,
            "A": "A(x)=1+x", "B": "B(x)=x and its honest shared extension",
            "address_convention": "(tag<<7)|seed, least significant bit is variable0",
            "used_rows": layout.num_tags, "used_bits": used_bits,
            "fixed_domain": "numeric prefix [0,2796160), downward closed in subset order",
            "Q": Q, "address_bits": n,
            "allowed_changes": "only bits at addresses2796160 through4194303",
            "used_truth_sha256": hashlib.sha256(source_packed[:used_bits // 8]).hexdigest(),
        },
        "canonical_completion": {
            "rule": "keep original ANF coefficients with mask<M; set all other coefficients to0",
            "zero_padded_source_degree": source_degree,
            "source_degree18_terms_removed": len(source_leading),
            "exact_degree": degree, "minimum_exact_degree_over_allowed_padding": degree,
            "nonzero_coefficients": sum(histogram),
            "coefficient_degree_histogram": histogram,
            "leading_coefficient_count": len(leading),
            "leading_monomial_indices": leading,
            "truth_table_weight": sum(word.bit_count() for word in completion_words),
            "changed_padding_bits": changed_padding_bits,
            "used_bits_changed": 0, "physical_clause_failures": 0,
            "packed_truth_sha256": hashlib.sha256(completion_packed).hexdigest(),
            "packed_anf_sha256": hashlib.sha256(packed(completion_anf)).hexdigest(),
        },
        "fixed_subcube": {
            "constraint": "address variable21 equals0",
            "dimension": half_n, "fixed_truth_bits": half_bits,
            "exact_degree": half_degree, "leading_coefficient_count": len(half_leading),
            "coefficient_degree_histogram": half_histogram,
            "packed_truth_sha256": hashlib.sha256(packed(fixed_half_words)).hexdigest(),
            "packed_anf_sha256": hashlib.sha256(packed(half_anf)).hexdigest(),
        },
        "disjoint_parity_certificate": {
            "free_mask": free_mask,
            "free_variables": [i for i in range(half_n) if (free_mask >> i) & 1],
            "complementary_variables": complementary,
            "fixed_zero_variable": 21, "base_masks": bases,
            "target_parities": parities,
            "disjoint_subcubes": len(bases), "dimension_each": 17,
            "direct_truth_bits_read": 1 << 21,
            "degree_at_most16_polynomial_parity_each": 0,
            "minimum_wrong_used_bits_for_degree_at_most16": 16,
        },
        "approximation_consequence": {
            "strict_mean_wrong_bit_threshold": "109/23", "integer_error_radius": 4,
            "minimum_degree_over_allowed_padding_at_threshold": 17,
            "reason": "Every degree<=16 polynomial has at least one wrong used bit in each of16 disjoint odd-parity17-cubes. The canonical degree17 completion is exact.",
            "mixtures": "The same16-bit lower bound holds for the expectation of every input-independent probability distribution supported on degree<=16 polynomials.",
        },
        "verification": controls | {
            "used_prefix_bits_compared": used_bits,
            "completed_truth_inversion_bits": Q,
            "fixed_half_inversion_bits": half_bits,
            "all_clause_queries_remain_in_used_prefix": True,
            "actually_queried_tags": len(queried_tags),
            "no_unused_internal_tag_rows": True,
            "external_runtime_dependencies": [],
        },
        "scope": "Minimum only over the unused suffix padding, with every used bit of this named honest YES proof fixed. Other satisfying proofs, other layouts, and changes to used bits are not optimized. No new Lean verification or novelty claim.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
