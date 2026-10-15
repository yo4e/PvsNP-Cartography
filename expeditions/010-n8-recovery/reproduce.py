#!/usr/bin/env python3
"""Candidate discovery and exact repair; never trust LP tolerance as a proof.

Optional dependencies: numpy, scipy, sympy. Final validation uses only the
standard-library checkers. Seed2 reproduced the retained 159-row witness in
numpy2.3.5/scipy1.17.0/sympy1.14.0. Different solvers may choose another vertex.
"""
import argparse
from fractions import Fraction
import json
from math import lcm
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
import sympy as sp
from recover_939 import recover, rename, LABELS, PAIRS, require


def run(seed):
    data = recover()
    rows = [tuple(r[:3]) for r in data['rows_c_a_b_tickets']]
    index = {r: i for i, r in enumerate(rows)}
    A = np.zeros((256, len(rows)), dtype=np.int64)
    for j, (c, a, b) in enumerate(rows):
        edges = [(1 << i) | (1 << k) for h, (i, k) in enumerate(PAIRS) if b >> h & 1]
        for x in range(256):
            v = (c + (a & x).bit_count() + sum(x & m == m for m in edges)) % 2
            A[x, j] = v == int(x.bit_count() % 3 == 0)
    translations = [tuple(LABELS[LABELS[i] ^ t] for i in range(8)) for t in range(8)]
    seen, orbits = set(), []
    for row in rows:
        if row in seen:
            continue
        orbit = sorted({rename(row, p) for p in translations})
        require(all(r in index for r in orbit), 'translation leaves the support')
        orbits.append(orbit)
        seen.update(orbit)
    B = np.array([A[:, [index[r] for r in orbit]].sum(axis=1) for orbit in orbits]).T
    mass = np.array([len(orbit) for orbit in orbits])
    C = B / mass
    objective = np.zeros(len(orbits)) if seed == 0 else np.random.default_rng(seed).random(len(orbits))
    result = linprog(objective, A_ub=-C, b_ub=np.full(256, -2/3),
                     A_eq=np.ones((1, len(orbits))), b_eq=[1], bounds=(0, None), method='highs')
    require(result.success, 'no LP candidate: ' + result.message)
    support = np.where(result.x > 1e-9)[0]
    # Record a failed tempting conversion, using exact arithmetic afterward.
    rounded = [Fraction(float(result.x[i])).limit_denominator(10**7) / int(mass[i]) for i in support]
    rounded_mass = sum(int(mass[i]) * f for i, f in zip(support, rounded))
    rounded_good = [sum(int(B[x, i]) * f for i, f in zip(support, rounded)) for x in range(256)]
    # Floating arithmetic selects equations only. Exact elimination and ALL
    # pointwise inequalities decide whether the candidate is accepted.
    alpha = result.x[support] / mass[support]
    active = np.where(abs(B[:, support] @ alpha - 2/3) < 1e-7)[0]
    M = sp.Matrix(np.vstack((mass[support], B[active][:, support])).tolist())
    rhs = sp.Matrix([3] + [2] * len(active))
    _, pivots = M.T.rref()
    require(len(pivots) == len(support), 'active constraints do not determine a vertex')
    v = M[list(pivots), :].inv() * rhs[list(pivots), :] / 3
    require(M * v == rhs / 3, 'exact equations inconsistent')
    D = lcm(*(int(s.q) for s in v))
    tickets = [int(s * D) for s in v]
    good = [sum(int(B[x, i]) * t for i, t in zip(support, tickets)) for x in range(256)]
    require(min(tickets) > 0, 'negative repaired probability')
    require(sum(int(mass[i]) * t for i, t in zip(support, tickets)) == D, 'exact mass failure')
    require(min(good) * 3 >= 2 * D, 'exact pointwise failure')
    expanded = sorted([list(r) + [t] for i, t in zip(support, tickets) for r in orbits[i]])
    certificate = dict(n=8, field='GF(2)', target='weight divisible by 3', degree_bound=2,
                       success_threshold='2/3', denominator=D, rows_c_a_b_tickets=expanded)
    report = {'seed': seed, 'numpy': np.__version__, 'scipy': scipy.__version__, 'sympy': sp.__version__,
              'translation_orbits': len(orbits), 'selected_orbits': len(support),
              'rows': len(expanded), 'denominator': D, 'active_inputs': active.tolist(),
              'independent_equations': list(pivots), 'support_indices': support.tolist(),
              'rounded_conversion': {'mass_error': str(rounded_mass - 1),
                   'worst_input': rounded_good.index(min(rounded_good)),
                   'worst_gap_from_two_thirds': str(min(rounded_good) - Fraction(2, 3)),
                   'accepted': rounded_mass == 1 and min(rounded_good) >= Fraction(2,3)},
              'exact_candidate_accepted': True}
    return certificate, report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int, default=2)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    certificate, report = run(args.seed)
    args.output.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps(report, indent=2))
