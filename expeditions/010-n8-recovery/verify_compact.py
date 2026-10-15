#!/usr/bin/env python3
"""Check only the explicit compact n=8 data, with no group-action code.

Standard library only. The checker validates actual coefficient masks and real
probabilities represented by integer tickets, exhausts all 256 inputs, and
checks the affine lower certificate with exact integer arithmetic. No assert,
no optimizer, no import from either discovery/averaging checker.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify(data: dict) -> dict:
    require(data["n"] == 8 and data["field"] == "GF(2)" and data["degree_bound"] == 2,
            "wrong polynomial model")
    require(data["target"] == "weight divisible by 3" and data["success_threshold"] == "2/3",
            "wrong target or threshold")
    denominator = data["denominator"]
    require(type(denominator) is int and denominator > 0, "invalid denominator")
    rows = data["rows_c_a_b_tickets"]
    require(len(rows) > 0 and all(len(row) == 4 for row in rows), "invalid row array")
    pairs = tuple(combinations(range(8), 2))
    tuples = [tuple((x // (2 ** i)) % 2 for i in range(8)) for x in range(256)]
    truths = [int(sum(x) % 3 == 0) for x in tuples]
    good = [0] * 256
    total = 0
    distinct = set()
    for c, a, b, tickets in rows:
        require(all(type(v) is int for v in (c, a, b, tickets)), "noninteger coefficient or weight")
        require(c in (0, 1) and 0 <= a < 256 and 0 <= b < 2 ** 28,
                "out-of-range degree-two coefficient")
        require(tickets > 0, "nonpositive ticket mass")
        require((c, a, b) not in distinct, "explicit compact rows contain duplicates")
        distinct.add((c, a, b))
        total += tickets
        linear = tuple(i for i in range(8) if (a // (2 ** i)) % 2)
        edges = tuple(pair for k, pair in enumerate(pairs) if (b // (2 ** k)) % 2)
        for x, bits in enumerate(tuples):
            actual = (c + sum(bits[i] for i in linear) + sum(bits[i] * bits[j] for i, j in edges)) % 2
            if actual == truths[x]:
                good[x] += tickets
    require(total == denominator, "probability normalization failed")
    require(all(3 * x >= 2 * denominator for x in good), "pointwise success below two thirds")
    # All 512 actual binary affine coefficient rows, not a sampled list.
    dual = [7 if sum(x) == 1 else 1 if sum(x) == 3 else 0 for x in tuples]
    require(sum(dual) == 112, "lower input distribution unnormalized")
    scores = []
    for c in (0, 1):
        for a in range(256):
            selected = tuple(i for i in range(8) if (a // (2 ** i)) % 2)
            score = sum(w for bits, truth, w in zip(tuples, truths, dual)
                        if (c + sum(bits[i] for i in selected)) % 2 == truth)
            scores.append(score)
    require(max(scores) == 72 and 3 * max(scores) < 2 * 112, "affine obstruction failed")
    ratios = [str(Fraction(v, denominator)) for v in good]
    layers = [sorted({ratios[x] for x in range(256) if sum(tuples[x]) == w}) for w in range(9)]
    return {"n": 8, "distinct_polynomials": len(distinct), "denominator": denominator,
            "inputs_checked": 256, "polynomial_input_evaluations": 256 * len(rows),
            "minimum_success": str(Fraction(min(good), denominator)), "success_values_by_weight": layers,
            "pointwise_success_sha256": sha(ratios), "affine_rows_checked": 512,
            "maximum_affine_score": "9/14", "lower_threshold_gap": "1/42",
            "expanded_coefficient_rows_sha256": sha(rows)}


def negative_controls(data: dict) -> list[str]:
    rejected = []
    variants = []
    bad = deepcopy(data); bad["denominator"] += 1; variants.append(("wrong_total_mass", bad))
    bad = deepcopy(data); bad["rows_c_a_b_tickets"][0][3] = -1; variants.append(("negative_mass", bad))
    bad = deepcopy(data); bad["rows_c_a_b_tickets"][0][2] += 2 ** 28; variants.append(("degree_mask_out_of_range", bad))
    bad = deepcopy(data); bad["success_threshold"] = "1/2"; variants.append(("weakened_threshold", bad))
    bad = deepcopy(data)
    for row in bad["rows_c_a_b_tickets"]:
        row[0] ^= 1
    variants.append(("complement_all_polynomials", bad))
    for name, bad in variants:
        try:
            verify(bad)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError("accepted damaged certificate: " + name)
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=HERE / "compact-certificate.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    data = json.loads(raw)
    report = {"scope": "independently structured finite data check; same author; not Lean or human review",
              "certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "result": verify(data), "mutations_rejected": negative_controls(data)}
    text = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
