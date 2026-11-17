"""Exact finite tests of the sampler, weighted mixing and a translated toy residual."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def multiply_four(left, right):
    """Multiply in the binary basis 1,t with t^2=t+1."""
    result = 0
    while right:
        if right & 1:
            result ^= left
        left <<= 1
        if left & 4:
            left ^= 0b111
        right >>= 1
    return result


def powering_shifts(dimension):
    weights = Counter()
    for x, y in product(range(4), repeat=2):
        mask, power = 0, 1
        for i in range(dimension):
            mask |= ((power & y).bit_count() % 2) << i
            power = multiply_four(power, x)
        weights[mask] += 1
    return weights


def spectral_bias(dimension, weights):
    return max(abs(Fraction(sum(weight * (-1) ** ((mask & c).bit_count() % 2)
                                for mask, weight in weights.items()), sum(weights.values())))
               for c in range(1, 1 << dimension))


def all_masks(dimension):
    n = 1 << dimension
    weights = powering_shifts(dimension)
    bias = spectral_bias(dimension, weights)
    require(bias == Fraction(dimension - 1, 4), "unexpected bias")
    neighbor_sets = [sum(1 << (z ^ mask) for mask in weights) for z in range(n)]
    survivors = []
    for failure in range(1 << n):
        accept = sum(1 << z for z, neighbors in enumerate(neighbor_sets) if not neighbors & failure)
        f, s = failure.bit_count(), accept.bit_count()
        require(s * f <= bias**2 * (n - s) * (n - f), "centered mixing bound failed")
        survivors.append(accept)
    return survivors, {"dimension": dimension, "weighted_masks": sum(weights.values()),
                       "distinct_masks": len(weights), "weighted_bias": str(bias),
                       "unweighted_support_bias": str(spectral_bias(dimension, dict.fromkeys(weights, 1))),
                       "failure_sets": len(survivors)}


def translated_residual(survivors):
    # The external RS code in this isolated arithmetic test is the constants on GF(8).
    # The symbolic residual X + c has exactly one root for each admissible c.
    # No multiplication on GF(8) is needed. The sampler's GF(4) is a different field.
    n, cutoff, loss = 8, 1, 2
    shift, bias = 2, Fraction(1, 2)
    checked, maximum, witness = 0, 0, None
    for planted in range(1 << n):
        # At the origin read offset, X=0 gives physical value zero either way.
        if planted & 1:
            continue
        word = [0] * n
        for x in range(1, n):
            if planted & (1 << x):
                word[x ^ shift] = x
        freq = Counter(word)
        nearest = freq.most_common(1)[0][0]
        delta = n - freq[nearest]
        for failure, survival in enumerate(survivors):
            if delta > loss * failure.bit_count():
                continue
            joint = [x for x in range(n) if (survival >> x) & 1 and word[x ^ shift] == x]
            j = Fraction(len(joint), n)
            # j*(j-b) <= (1-j)*C*lambda^2 for one translated occurrence.
            require(j * (j - Fraction(1, n)) <= loss * bias**2 * (1 - j),
                    "outer root-count bound failed")
            if len(joint) > maximum:
                maximum = len(joint)
            if (witness is None and len(joint) > cutoff
                    and any(word[x ^ shift] != nearest and not (survival >> (x ^ shift)) & 1 for x in joint)):
                witness = {"base_reject": [x for x in range(n) if (failure >> x) & 1],
                           "amplified_accept": [x for x in range(n) if (survival >> x) & 1],
                           "word": word, "nearest_constant": nearest, "joint_accept": joint,
                           "offset": shift, "distance_symbols": delta}
            checked += 1
    require(witness is not None, "missing non-invariance control")
    return {"admissible_word_failure_pairs": checked, "largest_joint_count": maximum,
            "residual_root_cap": cutoff, "out_of_acceptance_read": witness}


def main():
    s3, audit3 = all_masks(3)
    _, audit4 = all_masks(4)
    print(json.dumps({"powering_and_mixing": [audit3, audit4], "toy_outer": translated_residual(s3)},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
