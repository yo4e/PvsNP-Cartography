"""Exact Boolean and minimum-cut controls for weighted shared buffers.

No external packages.  Run `python check_weighted_copy.py --output checks.json`.
The finite checks test the written derivation, not an asymptotic theorem.
"""
from collections import deque
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse
import json
import random


def require(test, message):
    if not test:
        raise ValueError(message)


def points(mask, n):
    return [i for i in range(n) if mask >> i & 1]


def neighborhood(mask, h, n):
    result = 0
    for z in points(mask, n):
        for shift in h:
            result |= 1 << (z ^ shift)
    return result


def subsets(mask):
    current = mask
    while True:
        yield current
        if not current:
            return
        current = (current - 1) & mask


def failures(assignment, clauses):
    return sum(weight for weight, clause in clauses
               if not any(((assignment >> (abs(lit)-1)) & 1) == (lit > 0)
                          for lit in clause))


def private_clauses(inputs, gate_start, weights):
    """Left-fold AND with one final assertion; literals use one-based ids."""
    clauses = []
    output = inputs[0]
    j = 0
    for offset, right in enumerate(inputs[1:]):
        new = gate_start + offset
        definitions = ((-output, -right, new), (output, -new), (right, -new))
        clauses.extend((weights[j+i], clause) for i, clause in enumerate(definitions))
        j += 3
        output = new
    clauses.append((weights[j], (output,)))
    require(j + 1 == len(weights), "private weight count")
    return clauses


@lru_cache(None)
def local_minima(t, weights):
    clauses = private_clauses(list(range(1, t+1)), t+1, weights)
    return tuple(min(failures(inputs | (gate_values << t), clauses)
                     for gate_values in range(1 << (t-1)))
                 for inputs in range(1 << t))


def direct_minimum(n, h, e, u, v, private):
    """Enumerate buffers; minimize actual Boolean gates privately per center."""
    tables = [local_minima(len(h), tuple(weights)) for weights in private]
    costs = []
    for b in range(1 << n):
        cost = 0
        for z in range(n):
            fz, bz = 1 - ((e >> z) & 1), (b >> z) & 1
            cost += u[z] * (bz and not fz) + v[z] * (fz and not bz)
        for x in range(n):
            inputs = sum(((b >> (x ^ shift)) & 1) << i for i, shift in enumerate(h))
            cost += tables[x][inputs]
        costs.append(cost)
    return min(costs)


def formula_minimum(n, h, e, a, b):
    return min(sum(a[z] for z in points(e ^ zset, n)) +
               sum(b[x] for x in points(neighborhood(zset, h, n), n))
               for zset in subsets(e))


def min_cut(n, h, e, a, b):
    """Edmonds-Karp with exact rational capacities, independent of subset scan."""
    source, sink, size = 2*n, 2*n+1, 2*n+2
    capacity = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    infinite = sum(a) + sum(b) + 1
    for z in points(e, n):
        capacity[source][z] = a[z]
        for shift in h:
            capacity[z][n+(z ^ shift)] = infinite
    for x in range(n):
        capacity[n+x][sink] = b[x]
    flow = Fraction(0)
    while True:
        parent = [-1] * size
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] == -1:
            u = queue.popleft()
            for v, cap in enumerate(capacity[u]):
                if cap > 0 and parent[v] == -1:
                    parent[v] = u
                    queue.append(v)
        if parent[sink] == -1:
            return flow
        increment, v = infinite, sink
        while v != source:
            u = parent[v]
            increment = min(increment, capacity[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= increment
            capacity[v][u] += increment
            v = u
        flow += increment


def full_clauses(n, h, u, v, private):
    clauses = []
    for z in range(n):
        f, b = z+1, n+z+1
        clauses.extend(((u[z], (-b, f)), (v[z], (-f, b))))
    t = len(h)
    for x in range(n):
        inputs = [n+(x ^ shift)+1 for shift in h]
        clauses.extend(private_clauses(inputs, 2*n+x*(t-1)+1, private[x]))
    return n*(t+1), clauses


def singleton_certificate(nvars, clauses):
    """All-one reference: each present clause has exactly one true literal."""
    loads = [Fraction(0)] * nvars
    all_one = (1 << nvars) - 1
    require(failures(all_one, clauses) == 0, "all-one YES reference")
    for weight, clause in clauses:
        true = [lit for lit in clause if lit > 0]
        require(len(true) == 1, "unique true literal")
        require(-true[0] not in clause, "no tautological charged clause")
        loads[true[0]-1] += weight
    sigma = max(loads)
    for i, load in enumerate(loads):
        require(failures(all_one ^ (1 << i), clauses) == load, "singleton replay")
    return sigma


def exhaustive_sigma(nvars, clauses):
    all_one = (1 << nvars) - 1
    return max(Fraction(failures(all_one ^ error, clauses), error.bit_count())
               for error in range(1, 1 << nvars))


def constant_private(n, t, beta):
    return [(beta,) * (3*(t-1)+1)] * n


def run():
    checks = {"uniform_N4": 0, "nonuniform_N2": 0,
              "rational_nonuniform_N4": 0, "arbitrary_private_N2": 0,
              "all_error_assignments": 0, "repair_equalities": 0}
    weights = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1), (4, 1), (1, 3), (3, 2)]
    n = 4
    for hmask in range(1, 1 << n, 2):
        h = points(hmask, n)
        t = len(h)
        for e in range(1 << n):
            count = e.bit_count()
            expanded = neighborhood(e, h, n).bit_count()
            for alpha, beta in weights:
                a, b = [alpha]*n, [beta]*n
                private = constant_private(n, t, beta)
                direct = direct_minimum(n, h, e, a, a, private)
                value = formula_minimum(n, h, e, a, b)
                cut = min_cut(n, h, e, a, b)
                require(direct == value == cut, "uniform Boolean/subset/cut agreement")
                sigma = alpha + t*beta
                require(2*value <= count*sigma, "uniform no-netgain")
                if count:
                    require(value*(expanded+t*count) <= count*expanded*sigma,
                            "optimized endpoint envelope")
                checks["uniform_N4"] += 1
            repaired = direct_minimum(n, h, e, [t]*n, [t]*n, constant_private(n, t, 1))
            require(repaired == expanded, "alpha=t beta exactly restores numerator")
            checks["repair_equalities"] += 1

    n = 2
    for h in ([0], [0, 1]):
        t = len(h)
        for alpha, beta in weights:
            nv, clauses = full_clauses(n, h, [alpha]*n, [alpha]*n,
                                      constant_private(n, t, beta))
            require(exhaustive_sigma(nv, clauses) == alpha+t*beta, "uniform exact sigma")
            checks["all_error_assignments"] += (1 << nv)-1
        for seed_weights in product(range(3), repeat=4):
            a, b = list(seed_weights[:2]), list(seed_weights[2:])
            private = [tuple([bx]*(3*(t-1)+1)) for bx in b]
            nv, clauses = full_clauses(n, h, a, a, private)
            sigma = exhaustive_sigma(nv, clauses)
            expected = max(a[z]+sum(b[z ^ shift] for shift in h) for z in range(n))
            if t >= 2:
                expected = max(expected, 2*max(b))
            require(sigma == expected == singleton_certificate(nv, clauses),
                    "nonuniform exact mixed-error sensitivity")
            checks["all_error_assignments"] += (1 << nv)-1
            for e in range(1 << n):
                direct = direct_minimum(n, h, e, a, a, private)
                require(direct == formula_minimum(n, h, e, a, b) == min_cut(n, h, e, a, b),
                        "nonuniform Boolean/subset/cut agreement")
                require(2*direct <= e.bit_count()*sigma, "nonuniform no-netgain")
                checks["nonuniform_N2"] += 1

    rng = random.Random(21044)
    n = 4
    for _ in range(64):
        h = points(rng.randrange(1, 1 << n, 2), n)
        a = [Fraction(rng.randrange(7), rng.randrange(1, 5)) for _ in range(n)]
        b = [Fraction(rng.randrange(7), rng.randrange(1, 5)) for _ in range(n)]
        e = rng.randrange(1 << n)
        private = [tuple([bx]*(3*(len(h)-1)+1)) for bx in b]
        direct = direct_minimum(n, h, e, a, a, private)
        require(direct == formula_minimum(n, h, e, a, b) == min_cut(n, h, e, a, b),
                "rational Boolean/subset/cut agreement")
        nv, clauses = full_clauses(n, h, a, a, private)
        sigma = singleton_certificate(nv, clauses)
        require(2*direct <= e.bit_count()*sigma, "rational no-netgain")
        checks["rational_nonuniform_N4"] += 1

    n, h = 2, [0, 1]
    for _ in range(128):
        a = [rng.randrange(5) for _ in range(n)]
        private = [tuple(rng.randrange(5) for _ in range(4)) for _ in range(n)]
        nv, clauses = full_clauses(n, h, a, a, private)
        sigma = exhaustive_sigma(nv, clauses)
        require(sigma == singleton_certificate(nv, clauses), "arbitrary clause load certificate")
        checks["all_error_assignments"] += (1 << nv)-1
        for e in range(1 << n):
            value = direct_minimum(n, h, e, a, a, private)
            require(2*value <= e.bit_count()*sigma, "arbitrary private weighting obstruction")
            checks["arbitrary_private_N2"] += 1

    # A strict gap between the endpoint upper envelope and the true optimum.
    n, h, e = 4, [0, 1], 0b0111
    for alpha, beta in weights:
        value = direct_minimum(n, h, e, [alpha]*n, [alpha]*n,
                               constant_private(n, len(h), beta))
        require(value == min(3*alpha, alpha+2*beta, 4*beta), "proper-subset minimizer")
    # A positive-weight counterexample to dropping the copy-symmetry premise.
    n, h, e, u, v, beta = 4, [0, 1, 2, 3], 1, 5, 1, 1
    private = constant_private(n, len(h), beta)
    value = direct_minimum(n, h, e, [u]*n, [v]*n, private)
    nv, clauses = full_clauses(n, h, [u]*n, [v]*n, private)
    sigma = singleton_certificate(nv, clauses)
    require((value, sigma) == (4, 5), "positive asymmetric counterexample")
    require(Fraction(value, sigma) > Fraction(1, 2), "symmetry premise essential")
    asymmetry = {"N": n, "H": h, "E": [0], "weights_u_v_beta": [u, v, beta],
                 "V": value, "sigma": int(sigma), "ratio": str(Fraction(value, sigma))}
    # Fully enumerated asymmetric control, including arbitrary simultaneous errors.
    n, h, e, u, v, beta = 2, [0, 1], 1, 3, 1, 1
    nv, clauses = full_clauses(n, h, [u]*n, [v]*n, constant_private(n, 2, beta))
    require(exhaustive_sigma(nv, clauses) == 3, "asymmetric exact all-error control")
    require(direct_minimum(n, h, e, [u]*n, [v]*n, constant_private(n, 2, beta)) == 2,
            "asymmetric exact NO control")
    checks["all_error_assignments"] += (1 << nv)-1
    # Rational clause duplication changes both V and sigma by the common factor.
    n, h, e = 4, [0, 1], 0b0111
    alpha, beta = Fraction(1, 2), Fraction(1, 3)
    rational = direct_minimum(n, h, e, [alpha]*n, [alpha]*n, constant_private(n, 2, beta))
    integer = direct_minimum(n, h, e, [3]*n, [3]*n, constant_private(n, 2, 2))
    require(6*rational == integer, "integer clause replication")
    require(rational/(alpha+2*beta) == Fraction(integer, 7), "replication ratio unchanged")
    return {"status": "passed", "counts": checks,
            "intermediate_subset": {"N": 4, "H": [0, 1], "E": [0, 1, 2],
                                    "true_optimum_V_over_sigma": "1",
                                    "endpoint_envelope": "6/5",
                                    "unshifted_symmetric_optimum": "3/2"},
            "asymmetric_counterexample": asymmetry,
            "rational_replication": {"scale": 6, "V": str(rational),
                                     "replicated_V": integer, "Q_changed": False},
            "scope": "Exact finite Boolean checks plus written derivation; no Lean or novelty claim."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")
