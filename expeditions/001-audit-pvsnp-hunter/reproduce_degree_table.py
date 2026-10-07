#!/usr/bin/env python3
"""Independent reproduction and exact tiny-instance audit for Expedition 001.

Target: GISMO-1/p-vs-np-hunter at
  ee4a4b80f8df505def85304af882a8bbff7de194

This script does not import the target repository. It independently reconstructs
its active formula/extrapolation path, independently recomputes the graph table,
and exactly solves a small finite optimization problem matching the prediction
and error semantics of the target's dormant _can_approximate helper, but without
that helper's n+3 monomial truncation.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

TARGET_REPOSITORY = "GISMO-1/p-vs-np-hunter"
TARGET_COMMIT = "ee4a4b80f8df505def85304af882a8bbff7de194"


def hunter_formula(name: str, n: int, p: int) -> int:
    name = name.lower()
    if name in {"parity", "xor"}:
        return n if p == 2 else max(1, n // 2)
    if name == "majority":
        base = max(1, int(n**0.5))
        return min(n, base if p == 2 else base + (n % 2))
    if name == "php":
        return min(n, max(2, int(0.6 * n) + (1 if p == 3 and n >= 7 else 0)))
    raise ValueError(name)


def hunter_estimate(name: str, n: int, p: int) -> int:
    if n <= 8:
        return hunter_formula(name, n, p)
    d6 = hunter_formula(name, 6, p)
    d7 = hunter_formula(name, 7, p)
    d8 = hunter_formula(name, 8, p)
    growth = max(0, d8 - d7, d7 - d6)
    return min(n, d8 + growth * (n - 8))


def power_fit(rows: dict[int, int]) -> dict[str, float]:
    pts = [(math.log(n), math.log(d)) for n, d in sorted(rows.items()) if d > 0]
    xs, ys = zip(*pts)
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    denom = sum((x - mx) ** 2 for x in xs)
    alpha = sum((x - mx) * (y - my) for x, y in pts) / denom
    intercept = my - alpha * mx
    pred = [intercept + alpha * x for x in xs]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - yp) ** 2 for y, yp in zip(ys, pred, strict=True))
    return {
        "alpha": alpha,
        "coefficient": math.exp(intercept),
        "r2": 1.0 if ss_tot == 0 else max(0.0, 1.0 - ss_res / ss_tot),
    }


def graph_value(mask: int, vertices: int, independent: bool) -> int:
    edges = [(u, v) for u in range(vertices) for v in range(u + 1, vertices)]
    adj = [[False] * vertices for _ in range(vertices)]
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            adj[u][v] = adj[v][u] = True
    threshold = max(2, math.ceil(vertices / 2))
    for size in range(threshold, vertices + 1):
        for subset in combinations(range(vertices), size):
            pairs = (adj[u][v] for i, u in enumerate(subset) for v in subset[i + 1 :])
            if (not independent and all(pairs)) or (independent and not any(pairs)):
                return 1
    return 0


def multilinear_degree(values: list[int], n: int, p: int) -> int:
    coeffs = [v % p for v in values]
    for i in range(n):
        bit = 1 << i
        for mask in range(1 << n):
            if mask & bit:
                coeffs[mask] = (coeffs[mask] - coeffs[mask ^ bit]) % p
    return max((m.bit_count() for m, c in enumerate(coeffs) if c), default=0)


def exact_graph_degree(name: str, vertices: int, p: int) -> int:
    n_edges = vertices * (vertices - 1) // 2
    values = [
        graph_value(mask, vertices, name == "independent_set")
        for mask in range(1 << n_edges)
    ]
    return multilinear_degree(values, n_edges, p)


def truth_table(name: str, n: int):
    for bits in product((0, 1), repeat=n):
        if name == "parity":
            target = sum(bits) % 2
        elif name == "majority":
            target = int(sum(bits) >= n // 2 + 1)
        else:
            raise ValueError(name)
        yield bits, target


def monomials(n: int, degree: int):
    out = [()]
    for k in range(1, degree + 1):
        out.extend(combinations(range(n), k))
    return out


def exact_nonzero_classifier_degree(name: str, n: int, p: int):
    """Exact minimum degree for the target helper's finite average-error semantics."""
    table = list(truth_table(name, n))
    for degree in range(n + 1):
        mons = monomials(n, degree)
        for coeffs in product(range(p), repeat=len(mons)):
            mistakes = 0
            for bits, target in table:
                value = 0
                for coeff, mon in zip(coeffs, mons, strict=True):
                    if not coeff:
                        continue
                    term = 1
                    for i in mon:
                        term = term * bits[i] % p
                    value = (value + coeff * term) % p
                mistakes += int(int(value != 0) != target)
            if Fraction(mistakes, len(table)) <= Fraction(1, 3):
                witness = [
                    {"monomial": list(m), "coefficient": c}
                    for m, c in zip(mons, coeffs, strict=True)
                    if c
                ]
                return {
                    "degree": degree,
                    "mistakes": mistakes,
                    "total": len(table),
                    "error": f"{mistakes}/{len(table)}",
                    "witness": witness,
                }
    raise AssertionError("degree n should suffice")


def build_result():
    php = {
        n: {"GF2": hunter_estimate("php", n, 2), "GF3": hunter_estimate("php", n, 3)}
        for n in range(2, 16)
    }
    graph = {}
    for name in ("clique", "independent_set"):
        graph[name] = {}
        for vertices in range(3, 7):
            n_edges = vertices * (vertices - 1) // 2
            graph[name][n_edges] = {
                "vertices": vertices,
                "GF2": exact_graph_degree(name, vertices, 2),
                "GF3": exact_graph_degree(name, vertices, 3),
            }
    exact = {}
    for name in ("majority", "parity"):
        exact[name] = {}
        for n in range(2, 5):
            exact[name][n] = {}
            for p in (2, 3):
                e = exact_nonzero_classifier_degree(name, n, p)
                h = hunter_estimate(name, n, p)
                exact[name][n][f"GF{p}"] = {
                    "hunter_reported": h,
                    "exact_audit_degree": e["degree"],
                    "matches": h == e["degree"],
                    "mistakes": e["mistakes"],
                    "total": e["total"],
                    "error": e["error"],
                    "witness": e["witness"],
                }
    return {
        "target": {"repository": TARGET_REPOSITORY, "commit": TARGET_COMMIT},
        "audit_quantity": (
            "For exact_small_n only: minimum degree among all multilinear GF(p) "
            "polynomials whose nonzero/zero classifier has uniform Boolean-cube "
            "misclassification rate <= 1/3. This mirrors the target helper's "
            "prediction/error semantics but removes its n+3 monomial truncation."
        ),
        "php_reconstruction": {
            "table": php,
            "GF2_power_fit": power_fit({n: r["GF2"] for n, r in php.items()}),
            "GF3_power_fit": power_fit({n: r["GF3"] for n, r in php.items()}),
        },
        "graph_exact_reproduction": graph,
        "exact_small_n_comparison": exact,
    }


def verify(result):
    php = result["php_reconstruction"]
    assert php["table"][15] == {"GF2": 11, "GF3": 15}
    assert math.isclose(php["GF2_power_fit"]["alpha"], 0.9533698286984779, abs_tol=1e-12)
    assert math.isclose(php["GF3_power_fit"]["alpha"], 1.2079016267666487, abs_tol=1e-12)
    expected = {
        3: {"vertices": 3, "GF2": 3, "GF3": 3},
        6: {"vertices": 4, "GF2": 6, "GF3": 6},
        10: {"vertices": 5, "GF2": 9, "GF3": 10},
        15: {"vertices": 6, "GF2": 15, "GF3": 14},
    }
    assert result["graph_exact_reproduction"]["clique"] == expected
    assert result["graph_exact_reproduction"]["independent_set"] == expected
    exact = result["exact_small_n_comparison"]
    for n in (2, 3, 4):
        assert exact["parity"][n]["GF2"]["exact_audit_degree"] == 1
        assert exact["parity"][n]["GF2"]["hunter_reported"] == n
    assert exact["majority"][2]["GF2"]["exact_audit_degree"] == 0
    assert exact["majority"][3]["GF3"]["exact_audit_degree"] == 1
    assert exact["majority"][4]["GF2"]["exact_audit_degree"] == 0


def stringify_keys(value):
    if isinstance(value, dict):
        return {str(k): stringify_keys(v) for k, v in value.items()}
    if isinstance(value, list):
        return [stringify_keys(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_result()
    verify(result)
    text = json.dumps(stringify_keys(result), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
