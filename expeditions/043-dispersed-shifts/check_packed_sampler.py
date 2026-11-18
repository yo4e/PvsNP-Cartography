"""Packed AGHP masks, exact Fourier checks and physical-view pooling controls."""
from collections import Counter
from fractions import Fraction
from functools import cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def remainder(value, divisor):
    while value.bit_length() >= divisor.bit_length():
        value ^= divisor << (value.bit_length() - divisor.bit_length())
    return value


@cache
def modulus(degree):
    for candidate in range((1 << degree) | 1, 1 << (degree + 1), 2):
        if all(remainder(candidate, divisor) != 0
               for divisor in range(2, 1 << (degree//2 + 1))):
            return candidate
    raise ValueError("missing irreducible modulus")


def multiply(x, y, field_modulus):
    result = 0
    while y:
        if y & 1:
            result ^= x
        x <<= 1
        if x.bit_length() == field_modulus.bit_length():
            x ^= field_modulus
        y >>= 1
    return result


def parameters(dimension, squared_bias):
    """Choose the first m with (ceil(k/m)-1)^2 <= bias^2 2^(2m)."""
    require(dimension > 0 and 0 < squared_bias < 1, "parameter range")
    m = 1
    while True:
        coefficient_count = (dimension+m-1)//m
        q = 1 << m
        if (coefficient_count-1)**2 <= squared_bias*q*q:
            return m, q, coefficient_count
        m += 1


def masks(dimension, m):
    q = 1 << m
    field_modulus = modulus(m)
    weights = Counter()
    nonzero_pairs = []
    for y in range(q):
        functions = []
        power = 1
        for position in range(dimension):
            coefficient, basis_bit = divmod(position, m)
            if position and basis_bit == 0:
                power = multiply(power, y, field_modulus)
            functions.append(multiply(1 << basis_bit, power, field_modulus))
        for w in range(q):
            mask = sum(((w & value).bit_count() % 2) << j
                       for j, value in enumerate(functions))
            weights[mask] += 1
            if y and w:
                nonzero_pairs.append(mask)
    if dimension >= 2*m:
        require(len(weights) == q*q-q+1, "support size")
        require(len(set(nonzero_pairs)) == (q-1)**2, "nonzero parameter injectivity")
        require(weights[0] == q, "zero multiplicity")
    return weights, nonzero_pairs


def walsh_spectrum(dimension, weights):
    values = [weights.get(i, 0) for i in range(1 << dimension)]
    half = 1
    while half < len(values):
        for block in range(0, len(values), 2*half):
            for offset in range(half):
                x, y = values[block+offset], values[block+offset+half]
                values[block+offset] = x+y
                values[block+offset+half] = x-y
        half *= 2
    return values


def spectral_checks():
    output = []
    for k, target in [(4, Fraction(1, 4)), (8, Fraction(1, 16)),
                      (12, Fraction(1, 16)), (16, Fraction(1, 64))]:
        m, q, d = parameters(k, target)
        weights, _ = masks(k, m)
        spectrum = walsh_spectrum(k, weights)
        bound = Fraction(d-1, q)
        actual = Fraction(max(map(abs, spectrum[1:])), q*q)
        require(actual <= bound and min(spectrum[1:]) >= 0, "weighted character bound")
        require(actual*actual <= target, "requested precision")
        # The character sum also equals Q times the exact number of roots of
        # its packed coefficient polynomial. Test all characters independently.
        field_modulus = modulus(m)
        root_checks = 0
        for character in range(1, 1 << k):
            coefficients = [(character >> (j*m)) & (q-1) for j in range(d)]
            roots = 0
            for y in range(q):
                value = 0
                for coefficient in reversed(coefficients):
                    value = multiply(value, y, field_modulus) ^ coefficient
                roots += value == 0
            require(spectrum[character] == q*roots, "field-root character identity")
            root_checks += 1
        output.append({"k": k, "m": m, "Q": q, "coefficient_count": d,
                       "weighted_calls": q*q, "distinct_masks": len(weights),
                       "guaranteed_bias": str(bound), "actual_bias": str(actual),
                       "characters_verified": root_checks})
    return output


def load_overlap(path):
    spec = spec_from_file_location("packed_sampler_overlap", path)
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def physical_checks(overlap):
    output = []
    for k, m in [(7, 3), (8, 3), (9, 3)]:
        weights, _ = masks(k, m)
        h = sorted(weights)
        views = {shift: overlap.full_view(k, 3, shift) for shift in h}
        base = overlap.base_masks(k, 3)
        compared = 0
        for index, left in enumerate(h):
            for right in h[index+1:]:
                require((not views[left].isdisjoint(views[right])) == ((left^right) in base),
                        "actual bundle overlap")
                compared += 1
        pool = set().union(*views.values())
        output.append({"k": k, "m": m, "mask_count": len(h),
                       "one_call_physical_reads": len(views[0]),
                       "unpooled_physical_reads": len(views[0])*len(h),
                       "pooled_physical_reads": len(pool), "view_pairs": compared})
    return output


def dispersion_checks(overlap):
    k, a, m = 160, 3, 6
    weights, regular = masks(k, m)
    q = 1 << m
    full_blocks = k//m
    require(full_blocks >= 6*a+2, "disjointness parameter regime")
    minimum = k
    pairs = 0
    for index, left in enumerate(regular):
        for right in regular[index+1:]:
            distance = (left^right).bit_count()
            require(distance >= full_blocks//2, "two consecutive blocks")
            minimum = min(minimum, distance)
            pairs += 1
    special = set(weights)-set(regular)
    require(len(special) == q, "exceptional y=0 support")
    for left in regular:
        for right in special:
            require((left^right).bit_count() >= full_blocks-1, "exceptional separation")
    base = overlap.base_masks(k, a)
    require(max(x.bit_count() for x in base) <= 3*a, "physical overlap radius")
    return {"k": k, "a": a, "m": m, "Q": q, "full_coefficient_blocks": full_blocks,
            "pairwise_masks_checked": pairs, "actual_minimum_distance_regular": minimum,
            "regular_views_pairwise_disjoint": len(regular), "exceptional_masks": len(special),
            "base_overlap_size": len(base),
            "base_overlap_maximum_weight": max(x.bit_count() for x in base),
            "proved_overlap_weight_bound": 3*a,
            "required_complete_blocks": 6*a+2,
            "uniform_cell_reader_bound": (1 << (2*a)) + (1 << a) - 1,
            "pooled_read_lower_multiplier": (q-1)**2,
            "pooled_read_upper_multiplier": len(weights)}


def cost_table():
    output = []
    for k, inverse in [(64, 4), (256, 8), (1024, 32), (4096, 64)]:
        target = Fraction(1, inverse**2)
        m, q, d = parameters(k, target)
        old_q = 2
        while old_q < (k-1)*inverse:
            old_q *= 2
        output.append({"k": k, "target_bias": f"1/{inverse}", "new_m": m,
                       "new_Q": q, "old_Q": old_q, "new_weighted_calls": q*q,
                       "old_weighted_calls": old_q*old_q,
                       "call_saving_factor": (old_q//q)**2,
                       "new_guaranteed_bias": str(Fraction(d-1, q))})
    return output


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--overlap", type=Path, default=Path(__file__).resolve().parent.parent /
                        "042-accepted-sites" / "check_overlap.py")
    args = parser.parse_args()
    overlap = load_overlap(args.overlap)
    result = {"exact_spectral_checks": spectral_checks(), "cost_comparison": cost_table(),
              "physical_pooling": physical_checks(overlap),
              "asymptotic_disjointness_control": dispersion_checks(overlap)}
    print(json.dumps(result, indent=2, sort_keys=True))
