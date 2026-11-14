"""Independent schedule checks and a physical GF(512) cubic-column control.

The field control evaluates the first-level bivariate polynomial in a translated
quadratic extension. It does not instantiate an entire physical two-level tree.
"""
from functools import reduce
from fractions import Fraction
from operator import xor
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def schedule(low, a):
    """Recover labels from bit consumption rather than a verdict formula."""
    rows, inner_columns = set(), set()
    for extension in range(1 << a):
        child_seed = low | (extension << (a + 1))
        rows.add(child_seed >> a)
        for suffix in range(1 << (a - 1)):
            inner_columns.add((child_seed % (1 << a)) | (suffix << a))
    outer_columns = {low | (suffix << (a + 1)) for suffix in range(1 << (a - 1))}
    return rows, inner_columns, outer_columns


def count_schedule(a, k):
    s = 1 << a
    m = 1 << (k - a - 1)
    tables = [schedule(low, a) for low in range(2*s)]
    accepted = set()
    for seed in range(1 << k):
        v, low = divmod(seed, 2*s)
        rows, inner_cols, outer_cols = tables[low]
        require(len(rows) == s and len(inner_cols) == len(outer_cols) == s//2,
                "original fresh-tape schedule")
        if all(j % 2 == v % 2 for j in rows):
            accepted.add(seed)
        mates = tables[low ^ (s+1)]
        require(rows | mates[0] == set(range(2*s)), "paired row labels")
        require(len(inner_cols | mates[1]) == s and len(outer_cols | mates[2]) == s,
                "distinct column groups")
    require(len(accepted) == m*s, "template rejection")
    require(not any((seed ^ (s+1)) in accepted for seed in accepted), "paired template")
    return {"a":a, "k":k, "original_accepts_templates":len(accepted),
            "paired_accepts_templates":0, "all_seeds":1 << k}


def integer_bounds(a, k):
    s, n = 1 << a, 1 << k
    m = n // (2*s)
    d, c = n//s, m//s
    require(c in (2, 4) and d == 2*m, "family parameters")
    sparse = max(2*m, (c-1)*2*s)
    require(sparse == d and 4*(s//2) == 2*s, "two outer interpolation thresholds")
    require(2*s-1+(c-1)*(2*s) == d-1, "composed degree")
    max_agreement = max(n//4, 3*d-2)
    require(n-max_agreement > n//2, "strict original counterexample bound")
    return {"column_cutoff":c, "root_cutoff":d, "sparse_max":sparse,
            "template_ratio_upper":str(Fraction(n//2, n-max_agreement))}


# A primitive generator for F=GF(512); its full nonzero orbit certifies this
# quotient is a field. Addition uses bitwise XOR in its polynomial basis.
LOG = [-1] * 512
EXP = []
x = 1
for i in range(511):
    require(LOG[x] == -1, "early multiplicative cycle")
    LOG[x] = i
    EXP.append(x)
    x <<= 1
    if x & 512:
        x ^= 0x211
require(x == 1 and min(LOG[1:]) == 0, "incomplete GF(512) cycle")


def fm(x, y):
    return EXP[(LOG[x]+LOG[y]) % 511] if x and y else 0


def em(x, y):
    # E=F[theta]/(theta²+theta+1); 3 does not divide 511.
    a, b = x & 511, x >> 9
    c, d = y & 511, y >> 9
    low = fm(a,c) ^ fm(b,d)
    high = fm(a,d) ^ fm(b,c) ^ fm(b,d)
    return low | (high << 9)


def div(x, y):
    require(y != 0, "division by zero")
    a, b = y & 511, y >> 9
    norm = fm(a, a^b) ^ fm(b,b)
    return em(em(x, (a^b) | b << 9), EXP[(-LOG[norm]) % 511])


def power(x, e):
    result = 1
    while e:
        if e & 1:
            result = em(result, x)
        x = em(x, x)
        e >>= 1
    return result


def subspace(x):
    return reduce(em, (x ^ i for i in range(16)), 1)


def interp(points, values, x):
    value = 0
    for i, (xi, yi) in enumerate(zip(points, values)):
        others = [v for j,v in enumerate(points) if i != j]
        weight = div(reduce(em, (x^v for v in others), 1),
                     reduce(em, (xi^v for v in others), 1))
        value ^= em(weight, yi)
    return value


def odd_cubic_control():
    # q(X)=prod(X+u), u=0..15. Use the legal external P(x)=q(x)^3,
    # so on the translated root Y=q(theta+x) one has P(x)=(Y+q(theta))^3.
    theta = 512
    ordinates = [subspace(theta ^ (v<<4)) for v in range(32)]
    require(len(set(ordinates)) == 32, "outer row labels collapsed")
    oq = subspace(theta)
    row_table = []
    for v, y in enumerate(ordinates):
        row = [power(y ^ oq, 3)] * 128
        for u in range(16):
            root_index = 16*v + u
            require(row[u] == power(subspace(root_index),3),
                    "root/row overlap changed external legal value")
        row_table.append(row)
    columns = [[row[64+c] for row in row_table] for c in range(64)]
    cubic_accepted = 0
    quadratic_rejected = 0
    for col in columns:
        fits = {count: all(interp(ordinates[:count], col[:count], y) == value
                           for y, value in zip(ordinates, col)) for count in (3,4)}
        cubic_accepted += int(fits[4])
        quadratic_rejected += int(not fits[3])
    require(cubic_accepted == quadratic_rejected == 64, "incorrect odd branch column cutoff")
    return {"k":9, "a":3, "external_degree":48, "distinct_ordinates":len(set(ordinates)),
            "outer_root_overlaps":512, "column_sites":len(columns)*len(ordinates),
            "cubic_members":cubic_accepted, "quadratic_nonmembers":quadratic_rejected}


def main():
    trials = [count_schedule(a, k) for a in (3,4,5) for k in (2*a+2,2*a+3)]
    sizes = [3,4,5,8,16,32]
    bounds = {str(a): {str(k):integer_bounds(a,k) for k in (2*a+2,2*a+3)} for a in sizes}
    return {"enumerated_schedules":trials, "integer_bounds_only":bounds,
            "odd_external_field_control":odd_cubic_control()}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
