#!/usr/bin/env python3
"""Exact controls for the known error-reduction/restriction bridge, not its generic proof."""
from fractions import Fraction as F
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mobius(values):
    out = values.copy()
    bit = 1
    while bit < len(out):
        for mask in range(len(out)):
            if mask & bit:
                out[mask] ^= out[mask ^ bit]
        bit <<= 1
    return out


def run():
    tails = {t: sum(F(comb(t, k) * 2**(t-k), 3**t)
                    for k in range(t//2 + 1, t+1)) for t in range(1, 18, 2)}
    require(tails[17] == F(1082987, 14348907) < F(1, 12), '17-copy bound')
    require(all(tails[t] > F(1, 12) for t in tails if t < 17), 'smaller odd repetition control')
    # Exact coefficient identity for ALL real p, not sampled monotonicity.
    tail_coeff = [0] * 18
    for k in range(9, 18):
        for j in range(18-k):
            tail_coeff[k+j] += comb(17,k) * comb(17-k,j) * (-1)**j
    derivative = [(k+1)*tail_coeff[k+1] for k in range(17)]
    factored = [0] * 17
    for j in range(9):
        factored[8+j] = 17 * comb(16,8) * comb(8,j) * (-1)**j
    require(derivative == factored, 'Bernoulli-tail derivative factorization')
    truth = [int(x.bit_count() >= 9) for x in range(1 << 17)]
    coeff = mobius(truth)
    require(mobius(coeff) == truth, 'ANF round-trip')
    degree = max(x.bit_count() for x, c in enumerate(coeff) if c)
    by_degree = {k: sum(c for x, c in enumerate(coeff) if x.bit_count() == k) for k in range(18)}
    # Symmetric coefficient c_k = sum_{j=9}^k choose(k,j) mod 2.
    require(all(c == sum(comb(x.bit_count(), j) for j in range(9, x.bit_count()+1)) % 2
                for x, c in enumerate(coeff)), 'coefficient formula')
    require(degree == 16, 'exact GF2 majority17 degree')
    # Do NOT infer error reduction from reusing one sample: on a fixed input
    # P=wrong with mass1/3, and majority(P,...,P) remains wrong with mass1/3.
    reused_error = F(1, 3)
    require(reused_error > F(1, 12), 'independence control')
    # Padding by TWO bits realizes all residue shifts without input dependence.
    shifts = {i: (-i) % 3 for i in range(3)}
    count = 0
    for m in range(13):
        for i, s in shifts.items():
            for x in range(1 << m):
                require(int((x.bit_count()+s) % 3 == 0) == int(x.bit_count() % 3 == i),
                        'residue restriction mismatch')
                count += 1
    # A deliberately wrong +i padding fails already at residue1 and weight1.
    require((1 + 1) % 3 != 0 and 1 % 3 == 1, 'wrong padding sign control')
    return {
        'odd_copy_error_tails': {str(t): str(v) for t, v in tails.items()},
        'chosen_amplifier': {'copies': 17, 'error_bound': str(tails[17]),
                             'required_error': '1/12', 'safe_degree_overhead': 17},
        'tail_derivative_identity': 'B17_prime(p) = 218790*p^8*(1-p)^8',
        'derivative_coefficients_checked': len(derivative),
        'gf2_majority17_exact_anf_degree': degree,
        'majority_inputs_checked': len(truth),
        'nonzero_anf_coefficients_by_degree': {str(k): v for k, v in by_degree.items() if v},
        'reused_single_draw_error': str(reused_error),
        'padding_weights_by_target_residue': shifts,
        'padding_truth_table_checks_m0_through12': count,
        'source_application': 'STV arXiv:1910.02465v1 Lemma9, m=n-2,b=3,epsilon=1/12',
        'not_claimed': ['generic Lean error reduction', 'Smolensky proof reconstruction',
                        'explicit finite degree threshold', 'new lower-bound result']
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
