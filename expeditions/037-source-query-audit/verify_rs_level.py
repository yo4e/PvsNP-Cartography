"""One RS-PCPP level in Ben-Sasson--Viola, TR14-017, §6. No field arithmetic.

Enumerate formal coordinates in the linearly independent basis of Def. 6.2.
The high-bit label H indexes q(beta), which is injective on L1 (Prop. 6.1).
The pair (H, alpha) suffices to distinguish the geometric points in (9).
Run: python3 verify_rs_level.py
"""
import json
from collections import Counter
from itertools import product


def check(condition, message):
    if not condition:
        raise ValueError(message)


def check_level(a, k):
    low_bits = k // 2
    high_bits = k - low_bits
    low, high, aux = range(1 << low_bits), range(1 << high_bits), range(1 << (a - 1))
    b0, c0 = 1 << (k + a - 1), 1 << (k + a)

    def beta(h):
        return b0 ^ (h << low_bits)

    def column_point(l, j):
        return c0 ^ l ^ (j << k)

    def row_point(h, l, j, marker, convention):
        # convention 0: row shift beta (Def. 6.2); convention 1: shift c0.
        shift = c0 if convention else beta(h)
        direction = c0 ^ beta(h)
        return shift ^ l ^ (j << k) ^ (direction if marker else 0)

    t_rows = [{beta(h) ^ l for l in low} for h in high]  # (9), keyed by q(beta).
    columns = {column_point(l, j) for l, j in product(low, aux)}  # (6).
    check(all(row.isdisjoint(columns) for row in t_rows), "Prop. 6.1 column in T")
    row_domains = [columns | {beta(h) ^ l ^ (j << k) for l, j in product(low, aux)}
                   for h in high]  # (7), without using the row_point basis.
    check(all(len(domain) == 1 << (low_bits + a) for domain in row_domains), "row sizes")

    def terminal(h, l, j, marker, convention):
        if j == 0 and marker == convention:
            return ("parent", (h << low_bits) | l)
        return ("row", h, l, j, marker)

    kernel_cases = []
    for convention in (0, 1):
        row_outputs, column_outputs = set(), set()
        wrong_marker = 0
        for h in high:
            geometric_row = set()
            for l, j, marker in product(low, aux, (0, 1)):
                alpha = row_point(h, l, j, marker, convention)
                geometric_row.add(alpha)
                target = terminal(h, l, j, marker, convention)
                on_t = alpha in t_rows[h]
                check((target[0] == "parent") == on_t, "membership predicate")
                if on_t:
                    check((b0 ^ target[1]) == alpha, "parent reconstruction")
                else:
                    check(target[1:] == (h, l, j, marker), "row payload")
                row_outputs.add(target)
                wrong_marker += (j == 0 and marker != convention) != on_t
            check(geometric_row == row_domains[h], "Def. 6.2 vs Eq. (7)")
        check(len(row_outputs) == 1 << (k + a), "collision after row redirection")
        check(wrong_marker == 2 * (1 << k), "inverted guard negative control")

        for h, l, j in product(high, low, aux):
            marker = 1 - convention
            alpha = column_point(l, j)
            check(alpha == row_point(h, l, j, marker, convention), "sibling point")
            target = terminal(h, l, j, marker, convention)
            check(target[0] == "row", "incorrect column-to-parent redirect")
            column_outputs.add(target)
        check(len(column_outputs) == 1 << (k + a - 1), "collision after column redirect")
        check(column_outputs <= row_outputs, "column missing from sibling")

        # Each fixed query to an enumerated leaf replaces its entire child coordinate.
        # Freeze new edge auxiliary bits at zero to count loss of ORIGINAL parent bits.
        fixed_rows = fixed_cols = 0
        if low_bits + a <= 2 * a:
            for l, j, marker in product(low, aux, (0, 1)):
                fibers = Counter(terminal(h, l, j, marker, convention)
                                 for h, unused_low in product(high, low))
                check(len(fibers) == len(high) and set(fibers.values()) == {len(low)},
                      "fixed row leaf occurrence")
                fixed_rows += 1
        if high_bits <= 2 * a:
            for h_fixed in high:
                fibers = Counter(terminal(h_fixed, l, 0, 1 - convention, convention)
                                 for unused_high, l in product(high, low))
                check(len(fibers) == len(low) and set(fibers.values()) == {len(high)},
                      "fixed column leaf occurrence")
                fixed_cols += 1
        kernel_cases.append((len(row_outputs), len(column_outputs), wrong_marker,
                             fixed_rows, fixed_cols))
    check(kernel_cases[0] == kernel_cases[1], "inconsistent marker conventions")
    nr, nc, wrong, fr, fc = kernel_cases[0]
    return {"a": a, "k": k, "row_states_per_encoding": nr,
            "column_states_per_encoding": nc, "wrong_guard_disagreements_per_encoding": wrong,
            "fixed_row_leaf_occurrences_per_encoding": fr,
            "fixed_column_leaf_occurrences_per_encoding": fc,
            "fixed_row_original_bits_lost": low_bits if fr else None,
            "fixed_column_original_bits_lost": high_bits if fc else None}


if __name__ == "__main__":
    cases = [(3, 7), (3, 8), (3, 9), (4, 9), (4, 10)]
    print(json.dumps({"marker_encodings": 2, "one_level": [check_level(a, k) for a, k in cases]},
                     indent=2, sort_keys=True))
