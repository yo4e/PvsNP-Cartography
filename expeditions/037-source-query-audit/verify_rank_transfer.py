#!/usr/bin/env python3
"""Finite rank-based repair controls; no source-PCP or independent validation."""
from collections import Counter
from fractions import Fraction as F
from random import Random
from pathlib import Path
import hashlib
import json
import verify_smoothing as base
from verify_smoothing import require, rank, affine, constants


def rank_transfer_controls() -> dict:
    """Check a computable sufficient bound against actual signed-clause errors.
    These are generic affine families, NOT generated from the BV14 PCP.
    """
    rng = Random(20261110)
    families = 0
    for r in range(4):
        for m in range(4):
            for _ in range(8):
                clauses, weights, bound = [], [], F(0)
                occurrences = Counter()
                for _i in range(3):
                    w = rng.randrange(1, 4)
                    maps = tuple((tuple(rng.randrange(1 << r) for _ in range(m)),
                                  rng.randrange(1 << m)) for _j in range(3))
                    signs = (0, rng.randrange(2), rng.randrange(2))
                    bound += w*sum(F(2)**(m-rank(rows)) for rows, _bias in maps)
                    for z in range(1 << r):
                        c = tuple((affine(rows, bias, z), sign)
                                  for (rows, bias), sign in zip(maps, signs))
                        clauses.append(c)
                        weights.append(w)
                        for x, _sign in c:
                            occurrences[x] += w
                total = sum(weights)
                density = F((1 << m)*max(occurrences.values()), total)
                bound /= F(total, 1 << r)
                kappa, actual = constants(1 << m, (1 << (1 << m))-1, clauses, weights)
                require(actual <= kappa <= density <= bound, 'rank-to-signed-error chain')
                families += 1
    return dict(families=families, seed=20261110,
                scope='synthetic affine three-query families, 0..3 bits, all error sets; not actual PCP')


def main() -> None:
    prerequisite = hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest()
    require(prerequisite == 'c994160443a1dbe828daa830772f61e3043a84587c07584f3ebc3b9522065e3a',
            'unchanged prerequisite')
    result = dict(status='PASS', checks=rank_transfer_controls(), prerequisite_sha256=prerequisite,
                  self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
