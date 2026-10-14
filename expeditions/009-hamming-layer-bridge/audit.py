#!/usr/bin/env python3
"""Exact finite tests of layer counting and the existing n=8 certificate.

This is same-author executable validation, not the arbitrary-n Lean proof.
Only the standard library is used. Safety checks survive python -O.
"""
from __future__ import annotations
import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, permutations
import json
from math import comb, factorial
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def git_blob(data: bytes) -> str:
    return sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def pullback(x: int, p: tuple[int, ...]) -> int:
    return sum(((x >> j) & 1) << i for i, j in enumerate(p))


def fibers(n: int, x: int, ps: list[tuple[int, ...]]) -> Counter:
    return Counter(pullback(x, p) for p in ps)


def check_fibers(n: int, x: int, counts: Counter) -> None:
    w = x.bit_count()
    layer = {y for y in range(1 << n) if y.bit_count() == w}
    require(set(counts) == layer, "incomplete Hamming-layer coverage")
    require(len(layer) == comb(n, w), "binomial layer count failed")
    require(set(counts.values()) == {factorial(w) * factorial(n - w)},
            "fiber multiplicities are not the exact factorial product")
    require(sum(counts.values()) == factorial(n), "wrong total permutation mass")
    # Signed rational score: positivity is not needed for the averaging theorem.
    g = {y: Fraction((11 * y + 3) % 19 - 9, (y % 5) + 1) for y in layer}
    left = sum(counts[y] * g[y] for y in layer) / factorial(n)
    right = sum(g.values()) / comb(n, w)
    require(left == right, "signed-score averages disagree")


def count_audit() -> dict:
    cases = 0
    applications = 0
    summary = []
    for n in range(9):
        ps = list(permutations(range(n)))
        # Exhaust all inputs at small n; canonical representatives at n=6,7,8.
        xs = list(range(1 << n)) if n <= 5 else [(1 << w) - 1 for w in range(n + 1)]
        for x in xs:
            check_fibers(n, x, fibers(n, x, ps))
            cases += 1
            applications += len(ps)
        summary.append({"n": n, "input_cases": len(xs), "permutations": len(ps),
                        "layer_sizes": [comb(n, w) for w in range(n + 1)],
                        "fiber_sizes": [factorial(w) * factorial(n - w) for w in range(n + 1)]})
    # Exhaustion is finite, explicitly bounded; n=0 and weights0,n are included.
    return {"cases": cases, "permutation_applications": applications, "by_arity": summary}


def eval_masks(row: dict, x: int, n: int) -> int:
    pairs = list(combinations(range(n), 2))
    terms = [((1 << i) | (1 << j)) for k, (i, j) in enumerate(pairs) if row["b"] >> k & 1]
    return (row["c"] + (row["a"] & x).bit_count() + sum(x & m == m for m in terms)) % 2


def eval_expanded(row: dict, x: int, n: int) -> int:
    bits = [(x // (2 ** i)) % 2 for i in range(n)]
    return (row["c"] + sum((row["a"] // (2 ** i) % 2) * bits[i] for i in range(n)) +
            sum((row["b"] // (2 ** k) % 2) * bits[i] * bits[j]
                for k, (i, j) in enumerate(combinations(range(n), 2)))) % 2


def mobius(table: list[int], n: int) -> list[int]:
    a = table[:]
    for i in range(n):
        for s in range(1 << n):
            if s >> i & 1:
                a[s] ^= a[s ^ (1 << i)]
    return a


def walsh(table: list[int]) -> list[int]:
    a = table[:]
    width = 1
    while width < len(a):
        for offset in range(0, len(a), 2 * width):
            for j in range(offset, offset + width):
                left, right = a[j], a[j + width]
                a[j], a[j + width] = left + right, left - right
        width *= 2
    return a


def verify_n8(c: dict) -> dict:
    require(c["n"] == 8 and c["field"] == "GF(2)" and c["threshold"] == "2/3", "wrong mathematical scope")
    n = 8
    rows = c["upper"]
    weights = [Fraction(row["weight"]) for row in rows]
    require(len(rows) == 4 and all(w >= 0 for w in weights) and sum(weights) == 1, "invalid seed probabilities")
    truth = [int(x.bit_count() % 3 == 0) for x in range(256)]
    tables = []
    profiles = []
    for row in rows:
        require(row["c"] in (0,1) and 0 <= row["a"] < 256 and 0 <= row["b"] < (1 << 28), "invalid coefficient masks")
        table = [eval_masks(row, x, n) for x in range(256)]
        require(table == [eval_expanded(row, x, n) for x in range(256)], "polynomial evaluators disagree")
        anf = mobius(table, n)
        expected = [0] * 256
        expected[0] = row["c"]
        for i in range(8):
            expected[1 << i] = row["a"] >> i & 1
        for k, (i, j) in enumerate(combinations(range(8), 2)):
            expected[(1 << i) | (1 << j)] = row["b"] >> k & 1
        require(anf == expected, "ANF coefficients disagree")
        require(all(s.bit_count() <= 2 for s, a in enumerate(anf) if a), "degree above two")
        good = [sum(table[x] == truth[x] for x in range(256) if x.bit_count() == w) for w in range(9)]
        require(good == row["good"], "incorrect per-layer certificate counts")
        tables.append(table)
        profiles.append(good)
    layer_success = [sum(a * Fraction(good[w], comb(8,w)) for a, good in zip(weights, profiles)) for w in range(9)]
    require(layer_success == list(map(Fraction, c["upper_layer_success"])), "saved layer success disagrees")
    require(min(layer_success) >= Fraction(2,3), "layer upper bound fails")
    # Direct full-permutation averaging at all nine canonical layer representatives.
    ps = list(permutations(range(8)))
    for w in range(9):
        x = (1 << w) - 1
        total = [0] * 4
        for p in ps:
            y = pullback(x, p)
            for r, table in enumerate(tables):
                total[r] += table[y] == truth[x]
        value = sum(a * Fraction(t, len(ps)) for a, t in zip(weights, total))
        require(value == layer_success[w], "literal full permutation mean disagrees")
    masses = [7 if x.bit_count() == 1 else 1 if x.bit_count() == 3 else 0 for x in range(256)]
    require(sum(masses) == 112, "unnormalized dual")
    require([Fraction(sum(m for x,m in enumerate(masses) if x.bit_count()==w),112) for w in range(9)] ==
            list(map(Fraction,c["lower_layer_mass"])), "dual layer mass mismatch")
    scores = [sum(m for x,m in enumerate(masses) if (b ^ ((a & x).bit_count() & 1)) == truth[x])
              for b in range(2) for a in range(256)]
    W = walsh([m * (-1 if t else 1) for m,t in zip(masses,truth)])
    require(scores == [(112 + (-1 if b else 1)*v)//2 for b in range(2) for v in W], "Walsh dual disagreement")
    require(max(scores) == 72 and Fraction(72,112) == Fraction(c["lower_maximum"]) < Fraction(2,3), "dual bound fails")
    # Check the symmetry-reduced lower proof against all 512 exhaustive rows.
    def binomial(a: int, b: int) -> int:
        return comb(a, b) if 0 <= b <= a else 0
    canonical_scores = [
        [7*(8-k) + k*binomial(8-k,2) + binomial(k,3) for k in range(9)],
        [7*k + binomial(8-k,3) + binomial(k,2)*(8-k) for k in range(9)],
    ]
    require(scores == [canonical_scores[b][a.bit_count()] for b in range(2) for a in range(256)],
            "coefficient-weight reduction disagrees with exhaustive affine scores")
    # A genuine 3-cycle detects confusing coefficient pullback with the input inverse.
    cycle = (1,2,0,3,4,5,6,7)
    inverse = tuple(cycle.index(i) for i in range(8))
    for a in range(256):
        transformed_a = pullback(a, cycle)
        require(scores[a] == scores[transformed_a], "dual score permutation invariance failed")
        for x in range(256):
            require((transformed_a & x).bit_count() % 2 ==
                    (a & pullback(x, inverse)).bit_count() % 2,
                    "coefficient/input inverse transport failed")
    raw = [sum(a for a,table in zip(weights,tables) if table[x]==truth[x]) for x in range(256)]
    return {"inputs":256, "seed_evaluations":1024, "affine_rows":512,
            "affine_input_evaluations":131072, "dual_total":112, "dual_maximum":72,
            "lower_fraction":"9/14", "canonical_affine_scores":canonical_scores,
            "coefficient_transport_checks":65536, "upper_layer_success":list(map(str,layer_success)),
            "upper_minimum":str(min(layer_success)),
            "direct_permutation_input_pairs":9*factorial(8),
            "raw_seed_mixture_counterexample":{"input":raw.index(min(raw)), "success":str(min(raw)),
                "inputs_below_threshold":sum(s<Fraction(2,3) for s in raw)},
            "dual_scores_sha256":sha256(json.dumps(scores).encode()).hexdigest()}


def countermodels() -> dict:
    # Four distinct permutations cover the weight-one layer, with unequal fibers.
    ps = [(0,1,2),(0,2,1),(1,0,2),(2,1,0)]
    c = fibers(3,1,ps)
    require(dict(c)=={1:2,2:1,4:1}, "coverage-only counterexample changed")
    require(Fraction(c[1],4)==Fraction(1,2) != Fraction(1,3), "biased mean not detected")
    missing = list(permutations(range(3)))[:-1]
    controls = []
    for name, counts in [("distinct_but_biased_cover",c),
                         ("missing_permutation",fibers(3,1,missing)),
                         ("deduplicate_without_reweighting",Counter({y:1 for y in c}))]:
        try:
            check_fibers(3,1,counts)
        except ValueError:
            controls.append(name)
        else:
            raise ValueError(f"failed to reject {name}")
    return {"coverage_alone_not_uniform":{"n":3,"input":1,"permutations":ps,
             "fiber_counts":dict(c),"biased_indicator_mean":"1/2","correct_layer_mean":"1/3"},
            "malformed_fibers_rejected":controls}


def lean_array(text: str, name: str) -> list:
    match = re.search(r"def " + name + r"\s*:[^\n]*:=\s*!\[(.*?)\]", text, re.S)
    require(match is not None, f"missing Lean array {name}")
    return ast.literal_eval("[" + match.group(1) + "]")


def check_lean_data(text: str, certificate: dict) -> None:
    rows = lean_array(text, "rows")
    weights = lean_array(text, "weights")
    pairs = lean_array(text, "pairs")
    require(rows == [(r["c"], r["a"], r["b"]) for r in certificate["upper"]],
            "Lean seed coefficient arrays differ from Expedition004")
    require([Fraction(w, 12) for w in weights] ==
            [Fraction(r["weight"]) for r in certificate["upper"]], "Lean seed weights differ")
    require(pairs == list(combinations(range(8), 2)), "Lean pair convention differs")
    block = text.split("def mass (", 1)[1].split("theorem", 1)[0]
    masses = {int(w): int(m) for w,m in re.findall(r"\|\s*(\d+)\s*=>\s*(\d+)", block)}
    require(masses == {1: 7, 3: 1}, "Lean dual masses differ")


def lean_controls(text: str, certificate: dict) -> list[str]:
    controls = []
    for name, old, new in [
        ("changed_lean_seed", "(0,0,268435455)", "(1,0,268435455)"),
        ("changed_lean_weight", "![1,3,4,4]", "![2,3,4,4]"),
        ("changed_lean_pair_order", "(0,1),(0,2)", "(0,2),(0,1)"),
        ("changed_lean_dual", "| 1 => 7", "| 1 => 8")]:
        require(old in text, f"mutation target absent: {name}")
        try:
            check_lean_data(text.replace(old, new, 1), certificate)
        except ValueError:
            controls.append(name)
        else:
            raise ValueError(f"accepted {name}")
    return controls


def main() -> None:
    source = ROOT / "expeditions/004-exact-mod3-n8/certificate.json"
    snapshot = HERE / "n8-source-certificate.json"
    source_bytes = source.read_bytes()
    require(source_bytes==snapshot.read_bytes(), "upstream n8 certificate differs from snapshot")
    certificate = json.loads(source_bytes)
    lean_text = (ROOT / "formal/PvsNPCartography/Mod3EightDegree.lean").read_text(encoding="utf-8")
    check_lean_data(lean_text, certificate)
    lean_rejections = lean_controls(lean_text, certificate)
    n8 = verify_n8(certificate)
    rejections = []
    for name, mutation in [("corrupt_layer_count",lambda d:d["upper"][0]["good"].__setitem__(0,1)),
                           ("unnormalized_seed_weights",lambda d:d["upper"][0].__setitem__("weight","1/6")),
                           ("weakened_threshold",lambda d:d.__setitem__("threshold","1/2"))]:
        altered=json.loads(source_bytes)
        mutation(altered)
        try:
            verify_n8(altered)
        except ValueError:
            rejections.append(name)
        else:
            raise ValueError(f"accepted broken n8 certificate: {name}")
    formal = ROOT / "formal/PvsNPCartography"
    hashes = {p.name:git_blob(p.read_bytes()) for p in sorted(formal.glob("*.lean"))
              if p.name in {"HammingLayers.lean","LayerCertificates.lean","Mod3EightDegree.lean"}}
    print(json.dumps({"scope":"finite exact same-author audit; not independent human review or all-n proof",
        "source_certificate_git_blob":git_blob(source_bytes),"formal_source_git_blobs":hashes,
        "counting":count_audit(),"n8":n8,"countermodels":countermodels(),
        "n8_mutations_rejected":rejections,"lean_data_mutations_rejected":lean_rejections},indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
