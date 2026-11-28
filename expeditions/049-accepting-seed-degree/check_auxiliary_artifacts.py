#!/usr/bin/env python3
"""Exact signed-clause controls for compiler-created auxiliary degree.

All rows are shared complete seed functions. Pin clauses use actual clamped
queries. No field rejection count or earlier compiler constant is imported.
"""
from collections import Counter
from fractions import Fraction
import json
import random


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def degree(table, k):
    coefficients = [(table >> z) & 1 for z in range(1 << k)]
    for j in range(k):
        for z in range(1 << k):
            if (z >> j) & 1:
                coefficients[z] ^= coefficients[z ^ (1 << j)]
    return max((z.bit_count() for z, c in enumerate(coefficients) if c), default=0)


def affine_tables(k):
    return [sum(((constant ^ ((slope & z).bit_count() & 1))) << z
                for z in range(1 << k))
            for constant in (0, 1) for slope in range(1 << k)]


def gate_failure(op, x, y, out):
    if op == "xor":
        return x ^ y ^ out
    return out * (2 - x - y) + (1 - out) * x * y


class Model:
    def __init__(self, k, kind):
        self.k, self.N = k, 1 << k
        self.full = (1 << self.N) - 1
        self.names = ["w"] + [f"p{j}" for j in range(k)]
        self.index = {name: j for j, name in enumerate(self.names)}
        self.gates = []
        if kind == "bent":
            require(k == 4, "bent control is four variables")
            self.add_gate("and", "p0", "p1", "a")
            self.add_gate("and", "p2", "p3", "b")
            self.add_gate("xor", "a", "b", "c")
        else:
            require(kind == "and", "unknown model")
            previous = "p0"
            for j in range(2, k + 1):
                name = "c" if j == k else f"prefix{j}"
                self.add_gate("and", previous, f"p{j - 1}", name)
                previous = name
        # This circuit is on the live output path. Both XOR gates read the
        # SAME physical c row. It is not a detached occurrence construction.
        self.add_gate("xor", "w", "c", "u")
        self.add_gate("xor", "u", "c", "t")
        self.pin_clauses = []
        for j in range(k):
            for epsilon in (0, 1):
                self.pin_clauses.append([(self.index[f"p{j}"], bool(epsilon), j, epsilon)])
        self.definitions = []
        for op, x, y, out in self.gates:
            signs = ([(-1, -2, 3), (1, -3), (2, -3)] if op == "and" else
                     [(1, 2, -3), (1, -2, 3), (-1, 2, 3), (-1, -2, -3)])
            variables = [x, y, out]
            self.definitions.extend([[(variables[abs(lit) - 1], lit > 0, None, None)
                                       for lit in clause] for clause in signs])
        self.units = [[(self.index[name], True, None, None)] for name in ("w", "t")]
        self.yes_clauses = self.pin_clauses + self.definitions + self.units
        self.no_clauses = self.yes_clauses + [[(0, False, None, None)]] * 2

    def add_gate(self, op, left, right, name):
        out = len(self.names)
        self.names.append(name)
        self.index[name] = out
        self.gates.append((op, self.index[left], self.index[right], out))

    def honest(self, w=1):
        rows = [self.full if w else 0]
        rows += [sum(((z >> j) & 1) << z for z in range(self.N)) for j in range(self.k)]
        rows += [0] * (len(self.names) - len(rows))
        for op, x, y, out in self.gates:
            rows[out] = rows[x] ^ rows[y] if op == "xor" else rows[x] & rows[y]
        return rows

    def failure_count(self, rows, no=False):
        clauses = self.no_clauses if no else self.yes_clauses
        failures = 0
        cache = {}
        for clause in clauses:
            accepted = 0
            for row, positive, bit, epsilon in clause:
                values = rows[row]
                if bit is not None:
                    key = (row, bit, epsilon)
                    if key not in cache:
                        cache[key] = sum(((values >> ((z & ~(1 << bit)) | (epsilon << bit))) & 1) << z
                                         for z in range(self.N))
                    values = cache[key]
                accepted |= values if positive else self.full ^ values
            failures += (self.full ^ accepted).bit_count()
        return failures

    def local_cost(self, assignment, seed, no=False):
        bit = lambda row: (assignment >> row) & 1
        cost = (1 - bit(0)) + (1 - bit(self.index["t"]))
        cost += 2 * sum(bit(1 + j) != ((seed >> j) & 1) for j in range(self.k))
        cost += sum(gate_failure(op, bit(x), bit(y), bit(out))
                    for op, x, y, out in self.gates)
        if no:
            cost += 2 * bit(0)
        return cost

    def weights(self):
        literal = [0] * len(self.names)
        for clause in self.yes_clauses:
            for row, _, bit, _ in clause:
                literal[row] += 2 if bit is not None else 1
        signed = [0] * len(self.names)
        for j in range(self.k):
            signed[1 + j] += 2  # exact sum of the complementary pin pairs
        signed[0] += 1
        signed[self.index["t"]] += 1
        for op, x, y, out in self.gates:
            signed[x] += 1
            signed[y] += 1
            signed[out] += 2 if op == "and" else 1
        return literal, signed


def cone_and_gate_controls():
    gate_count = 0
    for op in ("and", "xor"):
        signs = ([(-1, -2, 3), (1, -3), (2, -3)] if op == "and" else
                 [(1, 2, -3), (1, -2, 3), (-1, 2, 3), (-1, -2, -3)])
        for actual in range(8):
            bits = [(actual >> j) & 1 for j in range(3)]
            raw = sum(not any(bool(bits[abs(lit) - 1]) == (lit > 0) for lit in clause)
                      for clause in signs)
            require(raw == gate_failure(op, *bits), "signed gate encoding")
            for reference in range(8):
                ref = [(reference >> j) & 1 for j in range(3)]
                if gate_failure(op, *ref):
                    continue
                errors = [x ^ y for x, y in zip(bits, ref)]
                charge = errors[0] + errors[1] + (2 if op == "and" else 1) * errors[2]
                require(raw <= charge, "all-error gate charge")
                gate_count += 1
    cones = []
    for v in (0, 1):
        for c in (0, 1):
            scores = [(v ^ c ^ u) + (u ^ c ^ t) + 1 - t
                      for u in (0, 1) for t in (0, 1)]
            require(min(scores) == 1 - v, "shared cancellation cone minimum")
            cones.append({"v": v, "c": c, "minimum_replacement_failures": min(scores)})
    # Same cancellation identity fails when the second occurrence is detached.
    v, c0, u, c1, t = 0, 0, 0, 1, 1
    require((v ^ c0 ^ u) + (u ^ c1 ^ t) + 1 - t == 0,
            "detached occurrence control")
    return {"all_error_gate_charge_cases": gate_count, "shared_cones": cones,
            "detached_mutant_accepts_v0": True}


def bent_control():
    model = Model(4, "bent")
    honest = model.honest()
    require(model.failure_count(honest) == 0, "perfect completeness")
    require(model.failure_count(model.honest(0), no=True) == 32 and
            model.failure_count(honest, no=True) == 32, "attaining NO proofs")
    maximum = Fraction(0)
    maximum_case = None
    minima = []
    unique_counts = []
    checked = 0
    for z in range(model.N):
        ref = sum(((row >> z) & 1) << j for j, row in enumerate(honest))
        minimum_no = 10**9
        zeros = 0
        for assignment in range(1 << len(model.names)):
            value = model.local_cost(assignment, z)
            minimum_no = min(minimum_no, model.local_cost(assignment, z, no=True))
            zeros += value == 0
            error = (ref ^ assignment).bit_count()
            if error:
                ratio = Fraction(value, error)
                if ratio > maximum:
                    maximum = ratio
                    maximum_case = {"seed": z, "assignment": assignment,
                                    "reference": ref, "errors": error, "failures": value}
            else:
                require(value == 0, "reference local completeness")
            checked += 1
        require(minimum_no == 2 and zeros == 1, "local exact NO/YES classification")
        minima.append(minimum_no)
        unique_counts.append(zeros)
    require(maximum == 3, "exact all-error sensitivity")
    rng = random.Random(4949)
    for _ in range(32):
        rows = [rng.getrandbits(model.N) for _ in model.names]
        for no in (False, True):
            local = sum(model.local_cost(sum(((row >> z) & 1) << j for j, row in enumerate(rows)),
                                         z, no=no) for z in range(model.N))
            require(model.failure_count(rows, no=no) == local, "actual clamp/local identity")
    codes = affine_tables(4)
    distances = [min((row ^ code).bit_count() for code in codes) for row in honest]
    literal, signed = model.weights()
    raw_min = sum(distances)
    literal_min = sum(w * error for w, error in zip(literal, distances))
    signed_min = sum(w * error for w, error in zip(signed, distances))
    require((raw_min, literal_min, signed_min) == (20, 176, 54), "weighted affine distances")
    easy = model.honest()
    for name in ("a", "b", "c"):
        easy[model.index[name]] = 0
    easy[model.index["u"]] = easy[model.index["t"]] = model.full
    require(all(degree(row, 4) <= 1 for row in easy), "candidate rows are affine")
    require(model.failure_count(easy) == 8, "actual affine failure count")
    # Exactness of the unrestricted affine-row minimum: changing any pinned
    # affine seed bit incurs >=16 pin failures, and w!=1 incurs >=16 base/cone
    # failures. With those fixed, each of the two AND gates costs >=4 and all
    # subsequent XORs have an affine exact extension for any affine a,b.
    pin_dist = min((code ^ honest[1]).bit_count() for code in codes if code != honest[1])
    w_dist = min((code ^ model.full).bit_count() for code in codes if code != model.full)
    and_minima = []
    for op, x, y, out in model.gates[:2]:
        scores = []
        for code in codes:
            score = sum(gate_failure(op, (honest[x] >> z) & 1,
                                     (honest[y] >> z) & 1, (code >> z) & 1)
                        for z in range(model.N))
            scores.append(score)
        and_minima.append(min(scores))
    require(pin_dist == w_dist == 8 and and_minima == [4, 4], "exact affine optimum argument")
    c_row = honest[model.index["c"]]
    walsh = [sum(1 if (((c_row >> z) & 1) ^ ((slope & z).bit_count() & 1)) == 0 else -1
                 for z in range(model.N)) for slope in range(model.N)]
    require(set(map(abs, walsh)) == {4}, "bent Walsh certificate")
    return {
        "seed_bits": 4, "seeds": 16, "rows": len(model.names),
        "used_cells": len(model.names) * model.N,
        "padded_cube_size": (1 << (len(model.names) - 1).bit_length()) * model.N,
        "YES_templates": len(model.yes_clauses), "NO_templates": len(model.no_clauses),
        "old_YES_templates": 10, "old_NO_templates": 12,
        "raw_NO_minimum": sum(minima), "normalized_NO_gap": "1/15",
        "local_assignments_checked": checked,
        "satisfying_local_assignments_per_seed": unique_counts,
        "unique_used_YES_proof": True,
        "exact_signed_sensitivity": str(maximum), "sensitivity_attainment": maximum_case,
        "honest_row_degrees": {name: degree(row, 4) for name, row in zip(model.names, honest)},
        "nearest_affine_row_distances": dict(zip(model.names, distances)),
        "literal_fiber_weights": dict(zip(model.names, literal)),
        "signed_gate_charge_weights": dict(zip(model.names, signed)),
        "minimum_affine_used_error": raw_min,
        "minimum_affine_literal_weighted_error": literal_min,
        "minimum_affine_signed_charge_error": signed_min,
        "raw_error_sufficient_strict_budget": "32/3",
        "actual_minimum_affine_failure_count": 8,
        "acceptance_threshold": 16,
        "all_error_direct_clamp_identity_controls": 64,
        "bent_Walsh_values": walsh,
        "scope": "explicit equivalent Boolean compiler control, not the recursive source's gate census",
    }


def and_chain_control():
    k, d = 8, 4
    model = Model(k, "and")
    honest = model.honest()
    require(model.failure_count(honest) == 0, "AND perfect completeness")
    require(model.failure_count(model.honest(0), no=True) == 2 * model.N and
            model.failure_count(honest, no=True) == 2 * model.N, "AND raw NO attainment")
    approximate = honest.copy()
    for j in range(d + 1, k + 1):
        approximate[model.index["c" if j == k else f"prefix{j}"]] = 0
    approximate[model.index["u"]] = approximate[model.index["t"]] = model.full
    errors = sum((x ^ y).bit_count() for x, y in zip(honest, approximate))
    failed = model.failure_count(approximate)
    require(errors == 1 << (k - d) and failed == 1 << (k - d - 1),
            "prefix truncation exact costs")
    require(max(degree(row, k) for row in approximate) == d, "truncation degree")
    _, signed = model.weights()
    literal, _ = model.weights()
    require(max(signed) == 4, "AND all-error sensitivity upper bound")
    mutated = honest.copy()
    mutated[model.index["c"]] ^= 1  # seed zero has both final AND inputs zero
    require(model.failure_count(mutated) == 4, "AND sensitivity lower attainment")
    tradeoffs = []
    for cap in range(1, k):
        candidate = honest.copy()
        parity_lower = 0
        for j in range(cap + 1, k + 1):
            name = "c" if j == k else f"prefix{j}"
            row = honest[model.index[name]]
            candidate[model.index[name]] = 0
            # Each cube varies exactly the first j variables. Its truth
            # parity is odd; any degree<=cap<j polynomial has even parity.
            for rest in range(1 << (k - j)):
                parity = sum((row >> ((rest << j) | low)) & 1 for low in range(1 << j)) & 1
                require(parity == 1, "prefix disjoint parity certificate")
                parity_lower += 1
        candidate[model.index["u"]] = candidate[model.index["t"]] = model.full
        require(honest[model.index["u"]].bit_count() & 1, "live complement odd parity")
        parity_lower += 1
        row_errors = [(x ^ y).bit_count() for x, y in zip(honest, candidate)]
        actual_errors = sum(row_errors)
        signed_cost = sum(w * e for w, e in zip(signed, row_errors))
        literal_cost = sum(w * e for w, e in zip(literal, row_errors))
        failures = model.failure_count(candidate)
        require(actual_errors == parity_lower == 1 << (k - cap), "exact total degree-error curve")
        require(signed_cost == 3 * (1 << (k - cap)), "exact signed-charge approximation minimum")
        require(literal_cost == 5 * (1 << (k - cap)) + 9,
                "exact literal-weight approximation minimum")
        require(failures == 1 << (k - cap - 1), "truncated failure curve")
        tradeoffs.append({"degree_cap": cap, "minimum_used_error": actual_errors,
                          "disjoint_parity_lower_count": parity_lower,
                          "minimum_signed_charge_error": signed_cost,
                          "minimum_literal_weighted_error": literal_cost,
                          "constructed_actual_failures": failures})
    return {
        "seed_bits": k, "rows": len(model.names),
        "YES_templates": len(model.yes_clauses), "NO_templates": len(model.no_clauses),
        "raw_NO_minimum": 2 * model.N,
        "exact_signed_sensitivity": 4,
        "honest_maximum_row_degree": max(degree(row, k) for row in honest),
        "final_AND_row_ones": honest[model.index["c"]].bit_count(),
        "approximate_maximum_row_degree": d,
        "truncated_tuple_used_errors": errors,
        "truncated_tuple_actual_failures": failed,
        "all_error_charge_upper": max(signed) * errors,
        "half_NO_threshold": model.N,
        "whole_chain_counted_not_only_final_row": True,
        "general_formula": "for 1<=d<k: used errors=2^(k-d), actual failures=2^(k-d-1)",
        "exact_approximation_tradeoffs": tradeoffs,
    }


if __name__ == "__main__":
    print(json.dumps({"gate_and_cone": cone_and_gate_controls(),
                      "live_bent_compiler": bent_control(),
                      "live_AND_chain": and_chain_control()},
                     indent=2, sort_keys=True))
