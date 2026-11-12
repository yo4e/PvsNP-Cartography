"""Exact finite controls for the unary length and free-padding arguments.

Truth-table indexing uses the address in the low bits and the padding slice
in the high bits. All polynomials are multilinear over GF(2).
"""

import json
from fractions import Fraction
from functools import cache


def require(condition, message):
    if not condition:
        raise ValueError(message)


def width(n, constant):
    # ceil(log2(n+2)) = bit_length(n+1) for integer n >= 0.
    return n + constant * (n + 1).bit_length() + constant


@cache
def anf_degree(table, num_variables):
    coefficients = [(table >> point) & 1 for point in range(1 << num_variables)]
    for variable in range(num_variables):
        bit = 1 << variable
        for mask in range(len(coefficients)):
            if mask & bit:
                coefficients[mask] ^= coefficients[mask ^ bit]
    return max((i.bit_count() for i, value in enumerate(coefficients) if value),
               default=0)


def check_replication(base_width, padding_width):
    base_size = 1 << base_width
    num_slices = 1 << padding_width
    full_width = base_width + padding_width
    full_size = base_size * num_slices
    base_mask = (1 << base_size) - 1
    num_full_tables = 1 << full_size
    restrictions = []
    for polynomial in range(num_full_tables):
        slices = [(polynomial >> (s * base_size)) & base_mask
                  for s in range(num_slices)]
        require(max(anf_degree(table, base_width) for table in slices) <= anf_degree(
            polynomial, full_width
        ), "restriction raised degree")
        restrictions.append(slices)

    for target in range(1 << base_size):
        extended = sum(target << (s * base_size) for s in range(num_slices))
        require(anf_degree(extended, full_width) == anf_degree(target, base_width),
                "extension changed degree")
        best_full = [full_size + 1] * (full_width + 1)
        best_base = [base_size + 1] * (full_width + 1)
        for polynomial, slices in enumerate(restrictions):
            misses = (polynomial ^ extended).bit_count()
            errors = [(table ^ target).bit_count() for table in slices]
            require(sum(errors) == misses and min(errors) * num_slices <= misses,
                    "slice errors do not average to cube error")
            d = anf_degree(polynomial, full_width)
            best_full[d] = min(best_full[d], misses)
        for polynomial in range(1 << base_size):
            misses = (polynomial ^ target).bit_count()
            d = anf_degree(polynomial, base_width)
            best_base[d] = min(best_base[d], misses)
        for d in range(full_width + 1):
            require(min(best_full[:d+1]) == num_slices * min(best_base[:d+1]),
                    "optimal distances differ")

    # The zero target and polynomial 1[padding = 0] realize the entire loss
    # from always querying the zero slice of the supplied polynomial.
    witness = base_mask
    require(anf_degree(witness, full_width) == padding_width, "wrong indicator degree")
    require(restrictions[witness][0] == base_mask and min(restrictions[witness]) == 0,
            "fixed-slice counterexample failed")
    return {
        "base_width": base_width, "padding_bits": padding_width,
        "target_polynomial_pairs": (1 << base_size) * num_full_tables,
        "optimum_equalities": (1 << base_size) * (full_width + 1),
        "fixed_slice_error": "1",
        "whole_cube_error_of_witness": str(Fraction(witness.bit_count(), full_size)),
        "indicator_degree": anf_degree(witness, full_width),
    }


def check_widths():
    constants = (1, 2, 3, 7)
    levels = range(2, 15)
    for c in constants:
        for j in levels:
            n = (1 << j) - 2
            require(width(n + 1, c) - width(n, c) == c + 1, "wrong gap")
            require(width(n, c) - width(n - 1, c) == 1, "unexpected preceding gap")
    return {"constants": list(constants), "exponents": [levels.start, levels.stop - 1],
            "checked_gap_transitions": len(constants) * len(levels)}


if __name__ == "__main__":
    print(json.dumps({
        "padding": [check_replication(2, 1), check_replication(1, 2)],
        "length_map": check_widths(),
    }, indent=2))
