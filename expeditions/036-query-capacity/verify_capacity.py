#!/usr/bin/env python3
"""Exact finite controls for true-literal allocation and signed-OR transfer.

Standard library, Python >=3.10; no disabled assertions under -O. This checks
finite instances, not the general real-weight theorem or a succinct PCP solver.
The integer max-flow implementation is separate from both cut enumerations.
"""
from __future__ import annotations
from collections import Counter, deque
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import hashlib
import json


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def validate(n: int, allowed: tuple[int, ...], weights: tuple[int, ...]) -> None:
    require(n > 0 and len(allowed) == len(weights), 'domain/length')
    require(all(0 < a < 1 << n and a.bit_count() <= 3 for a in allowed),
            'nonempty true-address sets of size at most three')
    require(all(isinstance(w, int) and w >= 0 for w in weights) and sum(weights) > 0,
            'nonnegative integer weights with positive total')


def address_cut(n: int, allowed: tuple[int, ...], weights: tuple[int, ...]) -> tuple[F, int]:
    """Unnormalized optimal maximum load, conjectured by the cut formula."""
    best, witness = F(-1), 0
    for s in range(1, 1 << n):
        forced = sum(w for a, w in zip(allowed, weights) if a & s == a)
        ratio = F(forced, s.bit_count())
        if ratio > best:
            best, witness = ratio, s
    return best, witness


def test_cut(allowed: tuple[int, ...], weights: tuple[int, ...]) -> F:
    best = F(0)
    for u in range(1, 1 << len(allowed)):
        neighbor = total = 0
        for j, (a, w) in enumerate(zip(allowed, weights)):
            if u >> j & 1:
                neighbor |= a
                total += w
        best = max(best, F(total, neighbor.bit_count()))
    return best


def flow(n: int, allowed: tuple[int, ...], weights: tuple[int, ...], cap: F):
    """Edmonds-Karp on scaled INTEGER capacities; returns primal and cut evidence."""
    m, scale = len(allowed), cap.denominator
    sink, size = 1 + m + n, 2 + m + n
    capacity = [[0] * size for _ in range(size)]
    demand = sum(weights) * scale
    for t, (a, w) in enumerate(zip(allowed, weights)):
        capacity[0][1 + t] = w * scale
        for x in range(n):
            if a >> x & 1:
                capacity[1 + t][1 + m + x] = demand + 1
    for x in range(n):
        capacity[1 + m + x][sink] = cap.numerator
    residual = [row[:] for row in capacity]
    value = augmentations = 0
    while True:
        parent = [-1] * size
        parent[0] = 0
        queue = deque([0])
        while queue and parent[sink] == -1:
            u = queue.popleft()
            for v in range(size):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
        if parent[sink] == -1:
            break
        amount, v = demand + 1, sink
        while v:
            u = parent[v]
            amount = min(amount, residual[u][v])
            v = u
        v = sink
        while v:
            u = parent[v]
            residual[u][v] -= amount
            residual[v][u] += amount
            v = u
        value += amount
        augmentations += 1
    reachable = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in range(size):
            if residual[u][v] > 0 and v not in reachable:
                reachable.add(v)
                queue.append(v)
    require(sink not in reachable, 'augmenting path remained')
    cut = sum(capacity[u][v] for u in reachable for v in range(size) if v not in reachable)
    require(cut == value, 'flow/cut certificate mismatch')
    alloc = [[F(capacity[1+t][1+m+x] - residual[1+t][1+m+x], scale)
              for x in range(n)] for t in range(m)]
    for t, a in enumerate(allowed):
        require(all(z >= 0 and (z == 0 or a >> x & 1) for x, z in enumerate(alloc[t])),
                'negative or forbidden allocation')
        require(sum(alloc[t]) <= weights[t], 'row exceeds demand')
    require(all(sum(alloc[t][x] for t in range(m)) <= cap for x in range(n)),
            'address capacity exceeded')
    require(sum(map(sum, alloc)) == F(value, scale), 'flow allocation value')
    return F(value, scale), alloc, augmentations


def deterministic_load(n: int, allowed: tuple[int, ...], weights: tuple[int, ...]) -> F:
    choices = [tuple(x for x in range(n) if a >> x & 1) for a in allowed]
    best = F(sum(weights))
    for assignment in product(*choices):
        loads = [0] * n
        for x, w in zip(assignment, weights):
            loads[x] += w
        best = min(best, F(max(loads)))
    return best


def check_graph(n: int, allowed: tuple[int, ...], weights: tuple[int, ...], stats: Counter):
    validate(n, allowed, weights)
    cap, witness = address_cut(n, allowed, weights)
    require(cap == test_cut(allowed, weights), 'two cut characterizations disagree')
    total = sum(weights)
    require(F(total, n) <= cap <= total, 'normalization bounds')
    value, alloc, rounds = flow(n, allowed, weights, cap)
    require(value == total and all(sum(row) == w for row, w in zip(alloc, weights)),
            'proposed cut optimum not feasible')
    lower, _, _ = flow(n, allowed, weights, cap / 2)
    require(lower < total, 'strictly suboptimal capacity accepted')
    forced = sum(w for a, w in zip(allowed, weights) if a & witness == a)
    require(F(forced, witness.bit_count()) == cap, 'binding cut witness')
    det = deterministic_load(n, allowed, weights)
    require(cap <= det <= 3 * cap, 'deterministic integrality-gap bound')
    rounded = [F(0)] * n
    for row, w, a in zip(alloc, weights, allowed):
        x = max((x for x in range(n) if a >> x & 1), key=lambda x: row[x])
        require(3 * row[x] >= w, 'largest-share rounding')
        rounded[x] += w
    require(max(rounded) <= 3 * cap, 'rounded congestion')
    for errors in range(1 << n):
        fail = sum(w for a, w in zip(allowed, weights) if a & errors == a)
        allocation_error = sum(alloc[t][x] for t in range(len(allowed))
                               for x in range(n) if errors >> x & 1)
        require(fail <= allocation_error <= cap * errors.bit_count(), 'positive-OR transfer')
        stats['positive_error_sets'] += 1
    stats['graphs'] += 1
    stats['flow_runs'] += 2
    stats['feasible_augmentations'] += rounds
    stats['strict_fractional_advantages'] += det > cap
    return F(n, total) * cap, F(n, total) * det


def accepts(table: int, clause: tuple[tuple[int, int], ...]) -> bool:
    return any(((table >> x) & 1) ^ sign for x, sign in clause)


def true_false_sets(pi: int, clause: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    a = b = 0
    for x, sign in clause:
        if ((pi >> x) & 1) ^ sign:
            a |= 1 << x
        else:
            b |= 1 << x
    return a, b


def signed_constant(n: int, pi: int, clauses, weights, stats: Counter):
    pairs = tuple(true_false_sets(pi, c) for c in clauses)
    allowed = tuple(a for a, _ in pairs)
    validate(n, allowed, weights)
    total = sum(weights)
    cap, _ = address_cut(n, allowed, weights)
    _, alloc, _ = flow(n, allowed, weights, cap)
    exact, witness = F(0), 0
    failures = []
    for errors in range(1 << n):
        predicted = pi ^ errors
        failure = sum(w for c, w in zip(clauses, weights) if not accepts(predicted, c))
        formula = sum(w for (a, b), w in zip(pairs, weights)
                      if a & errors == a and b & errors == 0)
        require(failure == formula, 'signed failure characterization')
        bound = sum(alloc[t][x] for t in range(len(clauses))
                    for x in range(n) if errors >> x & 1)
        require(failure <= bound <= cap * errors.bit_count(), 'fractional signed bound')
        failures.append(F(failure, total))
        if errors:
            ratio = F(n * failure, total * errors.bit_count())
            if ratio > exact:
                exact, witness = ratio, errors
        stats['signed_error_sets'] += 1
    kappa = F(n, total) * cap
    require(exact <= kappa, 'actual signed constant exceeds certificate constant')
    # One fixed normalized mixture, including zero-mass rows; no resampling per occurrence.
    mu = [(7 * e + 2) % 5 for e in range(1 << n)]
    mass = sum(mu)
    require(mass > 0, 'mixture normalization')
    err = [F(sum(w for e, w in enumerate(mu) if e >> x & 1), mass) for x in range(n)]
    mean_err = sum(err) / n
    expected_fail = sum(F(w, mass) * failures[e] for e, w in enumerate(mu))
    require(expected_fail <= exact * mean_err <= kappa * mean_err, 'mixture bound')
    require(any(w > 0 and failures[e] <= kappa * mean_err for e, w in enumerate(mu)),
            'positive-mass global witness absent')
    stats['signed_families'] += 1
    stats['mixture_checks'] += 1
    stats['strict_signed_improvements'] += exact < kappa
    return kappa, exact, witness


def main() -> None:
    graph_stats, signed_stats = Counter(), Counter()
    exhaustive = seeded = 0
    for n in range(1, 5):
        choices = tuple(a for a in range(1, 1 << n) if a.bit_count() <= 3)
        for m in range(1, (3 if n <= 3 else 2) + 1):
            for allowed in product(choices, repeat=m):
                for weights in product(range(3), repeat=m):
                    if not sum(weights):
                        continue
                    check_graph(n, allowed, weights, graph_stats)
                    exhaustive += 1
    rng = Random(20261110)
    for n in (4, 5, 6):
        choices = tuple(a for a in range(1, 1 << n) if a.bit_count() <= 3)
        for _ in range(100):
            m = rng.randrange(1, 5)
            allowed = tuple(rng.choice(choices) for _ in range(m))
            weights = tuple(rng.randrange(4) for _ in range(m))
            if not sum(weights):
                weights = (1,) + weights[1:]
            check_graph(n, allowed, weights, graph_stats)
            seeded += 1
    # Exhaustive single signed three-occurrence clauses, including duplicates and tautologies.
    for n in range(1, 4):
        occurrences = tuple(product(range(n), range(2)))
        for pi in range(1 << n):
            for clause in product(occurrences, repeat=3):
                if accepts(pi, clause):
                    signed_constant(n, pi, (clause,), (1,), signed_stats)
    # Seeded weighted families of satisfied clauses on the finite address set.
    for n in range(1, 5):
        for _ in range(100):
            pi = rng.randrange(1 << n)
            occurrences = tuple(product(range(n), range(2)))
            pool = [c for c in product(occurrences, repeat=3) if accepts(pi, c)]
            clauses = tuple(rng.choice(pool) for _ in range(3))
            weights = tuple(rng.randrange(4) for _ in range(3))
            if not sum(weights):
                weights = (1, 0, 0)
            signed_constant(n, pi, clauses, weights, signed_stats)
    frac, det = check_graph(4, (0b0111,), (1,), graph_stats)
    require((frac, det) == (F(4, 3), F(4)), 'sharp factor-three countermodel')
    clauses = (((0, 0), (1, 0), (2, 1)),
               ((1, 0), (2, 0), (0, 1)),
               ((2, 0), (0, 0), (1, 1)))
    kappa, exact, error_witness = signed_constant(4, 15, clauses, (1, 1, 1), signed_stats)
    require((kappa, exact) == (F(4, 3), F(2, 3)), 'signed certificate optimality countermodel')
    # On the two-bit address cube, p(y)=y_1 is an actual degree-one witness.
    table = sum(((y >> 1) & 1) << y for y in range(4))
    mean_error = F((15 ^ table).bit_count(), 4)
    failure = F(sum(not accepts(table, c) for c in clauses), 3)
    require(mean_error == F(1, 2) and failure == F(1, 3) and failure / mean_error == exact,
            'actual linear polynomial attains signed constant')
    invalid = 0
    for args in ((0, (1,), (1,)), (2, (0,), (1,)), (2, (4,), (1,)),
                 (2, (1,), (-1,)), (2, (1,), (0,)), (2, (1,), (1, 1))):
        try:
            validate(*args)
        except RuntimeError:
            invalid += 1
        else:
            raise RuntimeError('invalid input accepted')
    result = dict(status='PASS', scope='exact finite same-author controls, not Lean or independent review',
        seed=20261110, exhaustive_graph_cases=exhaustive, seeded_graph_cases=seeded,
        graph=dict(graph_stats), signed=dict(signed_stats), invalid_inputs_rejected=invalid,
        examples=dict(fractional_vs_deterministic=dict(addresses=4, true_addresses=[0, 1, 2],
            fractional=str(frac), deterministic=str(det), ratio=str(det / frac)),
            signed_optimality=dict(addresses=4, target_bits=[1, 1, 1, 1],
                clauses=clauses, certificate_constant=str(kappa), actual_constant=str(exact),
                maximizing_error_set=[x for x in range(4) if error_witness >> x & 1],
                linear_witness='p(y0,y1)=y1', uniform_error=str(mean_error), clause_failure=str(failure))),
        self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
