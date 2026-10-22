#!/usr/bin/env python3
"""Independent bit-packed truth tables, exact rational profiles, and boundary attacks.
Standard library only. Critical checks remain enabled under python -O.
This is finite computational evidence, not Lean execution or an all-n theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def run():
    n = 12
    size = 1 << n
    full = (1 << size) - 1
    layers = [sum(1 << x for x in range(size) if x.bit_count() == w)
              for w in range(n + 1)]
    variables = [sum(1 << x for x in range(size) if (x >> i) & 1)
                 for i in range(n)]
    target = sum(layers[w] for w in range(0, n + 1, 3))

    def poly(kind, subset):
        # Each bit is one ACTUAL Boolean input. Multiplication is AND, addition XOR.
        if kind == 'zero':
            return 0
        value = full
        linear = range(n) if kind == 'q' else [i for i in range(n) if i not in subset]
        for i in linear:
            value ^= variables[i]
        for i, j in combinations(subset, 2):
            value ^= variables[i] & variables[j]
        return value

    def good(value):
        return full ^ (value ^ target)

    def measured(value):
        g = good(value)
        return [F((g & layer).bit_count(), choose(n, w)) for w, layer in enumerate(layers)]

    def profile(kind, a, w):
        if kind == 'zero':
            return F(int(w % 3 != 0))
        count = 0
        for k in range(w + 1):
            lin = w if kind == 'q' else w - k
            output = (1 + lin + choose(k, 2)) % 2
            count += choose(a, k) * choose(n - a, w - k) * int(output == int(w % 3 == 0))
        return F(count, choose(n, w))

    candidates = [('zero', ())]
    candidates += [('q', a) for a in combinations(range(n), 9)]
    candidates += [('r', a) for a in combinations(range(n), 8)]
    seen = set()
    union = 0
    totals = {'zero': [], 'q': [], 'r': []}
    primal = [60 * ((good(0) >> x) & 1) for x in range(size)]
    for kind, a in candidates:
        value = poly(kind, a)
        require(value not in seen, 'duplicate truth-table row')
        seen.add(value)
        union |= good(value)
        means = measured(value)
        predicted = [profile(kind, len(a), w) for w in range(n + 1)]
        require(means == predicted, f'actual polynomial/profile mismatch: {kind} {a}')
        integer_score = 5 * (good(value) & layers[6]).bit_count() + 126 * (good(value) & layers[10]).bit_count()
        score = F(integer_score, 12936)
        require(score == F(5, 14) * means[6] + F(9, 14) * means[10], 'dual normalization mismatch')
        expected = F(241, 462) if kind == 'r' else F(9, 14)
        require(score == expected, 'restricted candidate score')
        totals[kind].append(integer_score)
        if kind == 'q':
            bits = good(value)
            for x in range(size):
                primal[x] += (bits >> x) & 1
    require(len(candidates) == 716, 'family cardinality')
    require(5 * choose(12, 6) + 126 * choose(12, 10) == 12936, 'total input mass')
    require(union == full, 'input-dependent selection attack did not cover cube')

    require(60 + choose(12, 9) == 280, 'primal normalization')
    require(min(primal) == 180, 'matching restricted primal')
    primal_layers = []
    for w in range(n + 1):
        scores = {primal[x] for x in range(size) if x.bit_count() == w}
        require(len(scores) == 1, 'uniform subset mixture is pointwise layer-invariant')
        primal_layers.append(scores.pop())

    # Missing support restriction: a genuine degree-two polynomial defeats THIS dual.
    q8 = measured(poly('q', tuple(range(8))))
    q8score = F(5, 14) * q8[6] + F(9, 14) * q8[10]
    require(q8score == F(5, 6) > F(9, 14), 'q8 boundary counterexample')
    outside = []
    for kind in ('q', 'r'):
        for a in range(n + 1):
            means = measured(poly(kind, tuple(range(a))))
            require(means == [profile(kind, a, w) for w in range(n + 1)], 'outside profile mismatch')
            score = F(5, 14) * means[6] + F(9, 14) * means[10]
            if score > F(9, 14):
                outside.append([kind, a, str(score)])

    wrong_per_input_mass = F(5, 14) * choose(12, 6) + F(9, 14) * choose(12, 10)
    require(wrong_per_input_mass != 1, 'wrong measure control')
    swapped_q9 = F(9, 14) * F(9, 11) + F(5, 14) * F(6, 11)
    require(swapped_q9 > F(2, 3), 'swapped layers control')
    signed_score = 2 * F(9, 14) - F(241, 462)
    require(signed_score > F(2, 3), 'negative probability control')
    ordered = 0
    for i in range(9):
        for j in range(9):
            if i != j:
                ordered ^= variables[i] & variables[j]
    require(ordered == 0, 'ordered edges must cancel in characteristic two')
    wrong = full
    for v in variables:
        wrong ^= v
    require(wrong != poly('q', tuple(range(9))), 'ordered-edge mutation must differ')
    literal_q9 = measured(poly('q', tuple(range(9))))
    literal_r8 = measured(poly('r', tuple(range(8))))
    # A signed test of expectation linearity is algebraic, not a probability claim.
    signed_layer = []
    for w in (6, 10):
        s = sum(2 * ((good(poly('q', tuple(range(9)))) >> x) & 1)
                - ((good(poly('r', tuple(range(8)))) >> x) & 1)
                for x in range(size) if x.bit_count() == w)
        require(F(s, choose(n, w)) == 2 * literal_q9[w] - literal_r8[w], 'signed linearity')
        signed_layer.append(str(F(s, choose(n, w))))

    return {
        'scope': 'n12 zero/all q9/all r8 only; exact finite bit-packed evaluation',
        'candidate_count': len(candidates), 'distinct_truth_tables': len(seen),
        'inputs_per_candidate': size, 'covered_polynomial_input_pairs': len(candidates) * size,
        'actual_profile_equalities': len(candidates) * (n + 1),
        'positive_mass_inputs': choose(12, 6) + choose(12, 10),
        'integer_mass_total': 12936,
        'integer_scores': {k: sorted(set(v)) for k, v in totals.items()},
        'candidate_counts_by_kind': {k: len(v) for k, v in totals.items()},
        'q9_means_at_6_10': [str(literal_q9[w]) for w in (6, 10)],
        'r8_means_at_6_10': [str(literal_r8[w]) for w in (6, 10)],
        'matching_primal': {'zero_mass': '3/14', 'each_q9_mass': '1/280',
                            'each_r8_mass': '0', 'positive_support_size': 221,
                            'denominator': 280, 'minimum_numerator': min(primal),
                            'layer_numerators': primal_layers, 'pointwise_inputs_checked': size},
        'restricted_bound': '9/14', 'gap_to_two_thirds': str(F(2, 3) - F(9, 14)),
        'q8_means_at_6_10': [str(q8[w]) for w in (6, 10)],
        'q8_dual_score': str(q8score), 'outside_family_controls': outside,
        'input_dependent_selection_success': '1 on every input (not a fixed distribution)',
        'wrong_per_input_normalization_total': str(wrong_per_input_mass),
        'swapped_layer_q9_score': str(swapped_q9),
        'signed_normalized_mixture_score': str(signed_score),
        'signed_layer_linearity_6_10': signed_layer,
        'ordered_edge_cancellation': True,
        'claims_not_established': ['unrestricted n12 degree', 'all-n theorem', 'Lean verification', 'novelty']
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
