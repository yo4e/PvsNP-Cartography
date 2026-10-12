#!/usr/bin/env python3
"""Exact, standard-library audit of the n=6/7 small-support certificates.

Reads the actual Lean coefficient arrays, checks them against certificate.json,
then verifies all inputs with two evaluators and reconstructs the ANF. The lower
certificate is checked both exhaustively and by an integer Walsh transform.
This is an executable semantic self-audit, not independent human review or Lean.
"""
from __future__ import annotations
import argparse
import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, permutations
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LEAN = ROOT / "formal/PvsNPCartography/SmallSupportMod3.lean"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def array(text: str, name: str) -> list:
    match = re.search(r"def " + name + r"\s*:[^\n]*:=\s*!\[(.*?)\]", text, re.S)
    require(match is not None, f"missing Lean array {name}")
    return ast.literal_eval("[" + match.group(1) + "]")


def load_lean() -> dict:
    text = LEAN.read_text(encoding="utf-8")
    weights = array(text, "weights")
    result = {}
    for n, name in [(6, "Six"), (7, "Seven")]:
        block = text.split(f"namespace {name}\n", 1)[1].split(f"end {name}\n", 1)[0]
        mass = {int(w): int(v) for w, v in re.findall(r"\|\s*(\d+)\s*=>\s*(\d+)", block)}
        result[str(n)] = {
            "n": n, "denominator": 24, "threshold": 16,
            "weights": weights, "rows": [list(r) for r in array(block, "rows")],
            "pairs": [list(p) for p in array(block, "pairs")],
            "mass_by_weight": [mass.get(w, 0) for w in range(n + 1)],
            "lower_denominator": 1080 if n == 6 else 1050,
            "lower_bound": 660 if n == 6 else 595,
        }
    return result


def evaluate_masks(row: list | tuple, x: int, pairs: list) -> int:
    c, linear, quadratic = row
    parity = c ^ ((linear & x).bit_count() & 1)
    for k, (i, j) in enumerate(pairs):
        monomial = (1 << i) | (1 << j)
        if (quadratic >> k) & 1 and x & monomial == monomial:
            parity ^= 1
    return parity


def evaluate_expanded(row: list | tuple, x: int, pairs: list, n: int) -> int:
    c, a, b = row
    bits = [(x // (2 ** i)) % 2 for i in range(n)]
    return (c + sum(((a // (2 ** i)) % 2) * bits[i] for i in range(n)) +
            sum(((b // (2 ** k)) % 2) * bits[i] * bits[j]
                for k, (i, j) in enumerate(pairs))) % 2


def mobius(values: list[int], n: int) -> list[int]:
    out = values[:]
    for i in range(n):
        for s in range(1 << n):
            if (s >> i) & 1:
                out[s] ^= out[s ^ (1 << i)]
    return out


def walsh(values: list[int]) -> list[int]:
    out = values[:]
    width = 1
    while width < len(out):
        for start in range(0, len(out), 2 * width):
            for j in range(start, start + width):
                a, b = out[j], out[j + width]
                out[j], out[j + width] = a + b, a - b
        width *= 2
    return out


def verify(data: dict) -> dict:
    n, rows, weights, pairs = data["n"], data["rows"], data["weights"], data["pairs"]
    D, T = data["denominator"], data["threshold"]
    require(n in (6, 7), "scope is n=6 or n=7 only")
    require(pairs == [list(p) for p in combinations(range(n), 2)], "wrong pair order")
    require(len(rows) == len(weights) == 18, "incorrect support length")
    require(all(type(w) is int and w >= 0 for w in weights), "negative or noninteger mass")
    require(sum(weights) == D == 24, "probabilities are not normalized")
    require(3 * T >= 2 * D, "threshold weakened below 2/3")
    truth = [int(x.bit_count() % 3 == 0) for x in range(1 << n)]
    tables = []
    for row in rows:
        c, a, b = row
        require(c in (0, 1) and 0 <= a < 2 ** n and 0 <= b < 2 ** len(pairs), "bad mask")
        table = [evaluate_masks(row, x, pairs) for x in range(1 << n)]
        require(table == [evaluate_expanded(row, x, pairs, n) for x in range(1 << n)], "evaluator disagreement")
        anf = mobius(table, n)
        expected = [0] * (1 << n)
        expected[0] = c
        for i in range(n):
            expected[1 << i] = (a >> i) & 1
        for k, (i, j) in enumerate(pairs):
            expected[(1 << i) | (1 << j)] = (b >> k) & 1
        require(anf == expected, "Mobius coefficient reconstruction failed")
        require(max((s.bit_count() for s, v in enumerate(anf) if v), default=0) <= 2, "degree exceeds two")
        tables.append(table)
    good = [sum(w for w, table in zip(weights, tables) if table[x] == truth[x]) for x in range(1 << n)]
    require(min(good) >= T, "pointwise upper certificate fails")
    masses = [data["mass_by_weight"][x.bit_count()] for x in range(1 << n)]
    lowerD, bound = data["lower_denominator"], data["lower_bound"]
    require(all(type(w) is int and w >= 0 for w in masses), "bad dual mass")
    require(sum(masses) == lowerD > 0, "dual is not normalized")
    scores = [sum(masses[x] for x in range(1 << n) if
                  (c ^ ((a & x).bit_count() & 1)) == truth[x])
              for c in range(2) for a in range(1 << n)]
    W = walsh([mass * (-1 if f else 1) for mass, f in zip(masses, truth)])
    recovered = [(lowerD + (-1 if c else 1) * w) // 2 for c in range(2) for w in W]
    require(scores == recovered, "Walsh and exhaustive lower scores disagree")
    require(max(scores) == bound and 3 * bound < 2 * lowerD, "lower obstruction fails")
    return {"n": n, "distinct_polynomials": len(set(map(tuple, rows))),
            "inputs": 2 ** n, "polynomial_evaluations": len(rows) * 2 ** n,
            "affine_rows": len(scores), "affine_evaluations": len(scores) * 2 ** n,
            "lower_maximum": str(Fraction(bound, lowerD)),
            "upper_minimum": str(Fraction(min(good), D)),
            "upper_maximum": str(Fraction(max(good), D)),
            "integer_success_histogram": dict(sorted(Counter(good).items())),
            "pointwise_success_numerators": good,
            "lower_scores_sha256": sha256(json.dumps(scores).encode()).hexdigest()}


def permute_row(row: tuple, permutation: tuple) -> tuple:
    n = len(permutation)
    pairs = list(combinations(range(n), 2))
    index = {p: i for i, p in enumerate(pairs)}
    c, a, b = row
    aa = sum(1 << permutation[i] for i in range(n) if (a >> i) & 1)
    bb = sum(1 << index[tuple(sorted((permutation[i], permutation[j]))) ]
             for k, (i, j) in enumerate(pairs) if (b >> k) & 1)
    return c, aa, bb


def cyclic_attack() -> dict:
    # Exhaustive failure of one SPECIFIC 12-ticket compression family, not all
    # possible 12-ticket quadratic witnesses, and not MILP infeasibility as proof.
    seed = (1, 71, 1887847)
    cycles = [tuple((i + k) % 7 for i in range(7)) for k in range(7)]
    all_rows = {permute_row(seed, p) for p in permutations(range(7))}
    orbits = {tuple(sorted({permute_row(r, p) for p in cycles})) for r in all_rows}
    require(len(all_rows) == 2520 and len(orbits) == 360, "orbit coverage changed")
    pairs = list(combinations(range(7), 2))
    sym = [(0, 0, 0), (0, 0, 2097151), (0, 127, 0), (1, 127, 2097151)]
    base = [sum(w for w, row in zip([1, 2, 1, 1], sym) if
                evaluate_masks(row, x, pairs) == int(x.bit_count() % 3 == 0)) for x in range(128)]
    best = -1
    example = None
    for orbit in sorted(orbits):
        good = [base[x] + sum(evaluate_masks(row, x, pairs) == int(x.bit_count() % 3 == 0)
                             for row in orbit) for x in range(128)]
        if min(good) > best:
            best = min(good)
            x = good.index(best)
            example = {"orbit": orbit, "input_integer": x, "bits_lsb_first": [(x >> i) & 1 for i in range(7)],
                       "success_numerator": best, "denominator": 12}
    require(best == 7, "claimed cyclic counterexample was not reproduced")
    return {"permutations": 5040, "distinct_seed_rows": 2520, "cyclic_orbits_checked": 360,
            "best_pointwise_minimum": "7/12", "example": example,
            "scope": "one cyclic orbit plus fixed symmetric ticket masses [1,2,1,1] only"}


def negative_controls(cert: dict) -> list[str]:
    names = []
    def reject(name: str, edit) -> None:
        changed = json.loads(json.dumps(cert["7"]))
        edit(changed)
        try:
            verify(changed)
        except ValueError:
            names.append(name)
        else:
            raise ValueError(f"negative control was accepted: {name}")
    reject("flipped_constant", lambda d: d["rows"][0].__setitem__(0, 1))
    reject("unnormalized_weights", lambda d: d["weights"].__setitem__(0, 3))
    reject("negative_weight", lambda d: d["weights"].__setitem__(0, -1))
    reject("reversed_pair_order", lambda d: d["pairs"].reverse())
    reject("corrupt_dual_mass", lambda d: d["mass_by_weight"].__setitem__(1, 21))
    reject("strict_slack_claim", lambda d: d.__setitem__("threshold", 17))
    return names


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cyclic-attack", action="store_true")
    parser.add_argument("--write-certificate", action="store_true")
    args = parser.parse_args()
    extracted = load_lean()
    path = HERE / "certificate.json"
    if args.write_certificate:
        path.write_text(json.dumps(extracted, indent=2) + "\n", encoding="utf-8")
    saved = json.loads(path.read_text(encoding="utf-8"))
    require(extracted == saved, "Lean arrays and saved certificate differ")
    results = [verify(saved[str(n)]) for n in (6, 7)]
    for row6, row7 in zip(saved["6"]["rows"], saved["7"]["rows"]):
        for x in range(64):
            require(evaluate_masks(row6, x, saved["6"]["pairs"]) ==
                    evaluate_masks(row7, x, saved["7"]["pairs"]), "zero-restriction mismatch")
    controls = negative_controls(saved)
    source = LEAN.read_bytes()
    report = {"scope": "exact finite n6/n7 certificates; novelty unknown; not independent human review",
              "lean_blob_sha1": sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest(),
              "results": results, "negative_controls_rejected": controls,
              "zero_restriction_checks": 18 * 64}
    if args.cyclic_attack:
        report["cyclic_attack"] = cyclic_attack()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
