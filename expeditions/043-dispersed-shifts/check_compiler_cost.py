"""Exact controls for sharing decision gates and charging replicated verifiers.

These are small Boolean compilers, not the recursive RS predicate. The field
decision table is fixed before any auxiliary gate assignment is optimized.
"""

from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def failed_and_gate(left, right, output):
    clauses = [(not left, not right, output),
               (left, not output), (right, not output)]
    return sum(not any(clause) for clause in clauses)


def aggregate_cost(inputs):
    """Enumerate every gate truth assignment of a private left-associated AND."""
    if len(inputs) == 1:
        return int(not inputs[0])
    optimum = len(inputs) * 3 + 1
    for outputs in product((0, 1), repeat=len(inputs) - 1):
        previous, cost = inputs[0], 0
        for right, output in zip(inputs[1:], outputs):
            cost += failed_and_gate(previous, right, output)
            previous = output
        optimum = min(optimum, cost + int(not previous))
    return optimum


def sharing_controls():
    n, checked, extra_checked, buffer_errors = 4, 0, 0, 0
    aggregator_cache = {}
    for shift_bits in range(1 << n):
        if not shift_bits & 1:
            continue
        shifts = [h for h in range(n) if shift_bits >> h & 1]
        for wrong_buffers in range(1, 1 << n):
            # Fixed honest reference f=b=1, all AND gates=1. Flip only buffers.
            failure_count = wrong_buffers.bit_count()
            for z in range(n):
                inputs = [not (wrong_buffers >> (z ^ h) & 1) for h in shifts]
                if len(inputs) == 1:
                    failure_count += int(not inputs[0])
                else:
                    previous = inputs[0]
                    for right in inputs[1:]:
                        failure_count += failed_and_gate(previous, right, 1)
                        previous = 1
            require(failure_count == (len(shifts) + 1) * wrong_buffers.bit_count(),
                    "buffer sensitivity mismatch")
            buffer_errors += 1
        for failure in range(1 << n):
            best = n * 10
            for declared in range(1 << n):
                # Literal evaluation of the two clauses for b(z) <-> f(z).
                copy_cost = 0
                for z in range(n):
                    actual_pass = not (failure >> z & 1)
                    declared_pass = not (declared >> z & 1)
                    copy_cost += int(not (not declared_pass or actual_pass))
                    copy_cost += int(not (declared_pass or not actual_pass))
                and_cost = 0
                for z in range(n):
                    inputs = tuple(not (declared >> (z ^ h) & 1) for h in shifts)
                    if inputs not in aggregator_cache:
                        aggregator_cache[inputs] = aggregate_cost(inputs)
                    and_cost += aggregator_cache[inputs]
                best = min(best, copy_cost + and_cost)
            require(best == failure.bit_count(), "shared-copy optimum mismatch")
            checked += 1
            # Independent outer predicate, evaluated once at each center.
            for outer_failure in range(1 << n):
                optimum = min((failure ^ declared).bit_count()
                              + sum(bool(outer_failure >> z & 1)
                                    or any(declared >> (z ^ h) & 1 for h in shifts)
                                    for z in range(n))
                              for declared in range(1 << n))
                require(optimum <= failure.bit_count() + outer_failure.bit_count(),
                        "once-only outer upper bound failed")
                require(optimum >= (failure | outer_failure).bit_count(),
                        "unamplified lower bound failed")
                extra_checked += 1
    return {"cube_points": n, "base_table_mask_pairs": checked,
            "base_outer_table_mask_triples": extra_checked,
            "nonempty_buffer_error_sets": buffer_errors,
            "private_and_truth_tables": len(aggregator_cache),
            "extremal_all_masks": {"base_rejects": 1,
                                    "field_bundle_rejects": 4,
                                    "minimum_failed_clauses": 1}}


def full_error_sensitivity():
    """Flip every possible subset of all buffers AND all private gate cells."""
    n, assignments, mask_sets = 4, 0, 0
    results = []
    for mask_bits in range(1 << n):
        if not mask_bits & 1 or mask_bits.bit_count() > 3:
            continue
        shifts = [h for h in range(n) if mask_bits >> h & 1]
        gate_count = n * (len(shifts) - 1)
        variables = n + gate_count
        optimum = Fraction(0)
        for error in range(1, 1 << variables):
            buffers = [not (error >> z & 1) for z in range(n)]
            # On the honest all-one f, exactly the b-positive copy clause can fail.
            failures = sum(not value for value in buffers)
            for z in range(n):
                inputs = [buffers[z ^ h] for h in shifts]
                previous = inputs[0]
                for i, right in enumerate(inputs[1:]):
                    slot = n + z * (len(shifts) - 1) + i
                    output = not (error >> slot & 1)
                    failures += failed_and_gate(previous, right, output)
                    previous = output
                failures += int(not previous)
            optimum = max(optimum, Fraction(failures, error.bit_count()))
            assignments += 1
        require(optimum == len(shifts) + 1, "full signed sensitivity mismatch")
        mask_sets += 1
        results.append({"shifts": shifts, "variables": variables, "sigma": str(optimum)})
    return {"nonempty_full_error_sets": assignments, "mask_sets": mask_sets,
            "exact_maxima": results}


def rows_above(value):
    return 1 << (value - 1).bit_length()


def costing_controls():
    checked = 0
    for c, b, g, d, t in product(range(1, 6), repeat=5):
        difference = (t * c + b) * (t * g + d) - t * (c + b) * (g + d)
        require(difference == (t - 1) * (t * c * g - b * d),
                "product threshold mismatch")
        checked += 1
    examples = []
    for name, c, b, g, d, t in [("shared_overhead_gain", 10, 1000, 1, 1000, 4),
                                ("replica_dominated_loss", 1000, 10, 1000, 1, 4)]:
        clauses_one, clauses_t = c + b, t * c + b
        rows_one, rows_t = rows_above(g + d), rows_above(t * g + d)
        ratio = Fraction(t * clauses_one * rows_one, clauses_t * rows_t)
        examples.append({"case": name, "per_copy_clauses": c,
                         "shared_clauses": b, "per_copy_rows": g,
                         "shared_rows": d, "copies": t,
                         "cube_rows_before": rows_one, "cube_rows_after": rows_t,
                         "best_possible_precision_ratio": str(ratio)})
    return {"exact_product_comparisons": checked, "padded_examples": examples}


def main():
    print(json.dumps({"sharing": sharing_controls(), "costing": costing_controls(),
                      "all_gate_errors": full_error_sensitivity()},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
