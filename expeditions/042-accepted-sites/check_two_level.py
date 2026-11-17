"""Replay the rowwise accounting and split-parity witness, using only Python."""
import json
from collections import Counter


def require(condition, message):
    if not condition:
        raise ValueError(message)


def intersections(s, k, c):
    """Possible |K intersect C| for sets of the specified sizes."""
    return range(max(0, k + c - s), min(k, c) + 1)


def accounting(s):
    # For fixed K every intersection choice for C0 is compatible with every
    # choice for C1. Their overlap with each other has no role in the schedule.
    records = 0
    tight_regular_single = 0
    for k in range(s + 1):
        for c0 in range(s + 1):
            for c1 in range(s + 1):
                strong = tuple(p for p, c in enumerate((c0, c1)) if c >= 4)
                for u0 in intersections(s, k, c0):
                    for u1 in intersections(s, k, c1):
                        for g in range(4):
                            accepts = (u0 if g & 1 else 0) + (u1 if g & 2 else 0)
                            recovered = k >= 2 and g == 3
                            if strong:
                                credits = []
                                covered = 0
                                for p in strong:
                                    usable = k >= 2 and (g & (1 << p))
                                    credits.append((2*s if recovered else s) if usable else 0)
                                    if usable:
                                        covered += (u0, u1)[p]
                                if recovered:
                                    covered = accepts
                                twice_credit = (2 * sum(credits)) // len(strong)
                                cap = 2 if len(strong) == 2 else 3
                            else:
                                twice_credit = 4*s if recovered and c0+c1 >= 4 else 0
                                covered = 0
                                cap = 6
                            require(twice_credit >= 3*accepts - 2*s, "distance credit")
                            require(0 <= accepts-covered <= cap, "exceptional site cover")
                            if k >= 2 and g in (1, 2) and accepts == s:
                                tight_regular_single += twice_credit == 3*accepts - 2*s
                            records += 1
    require(tight_regular_single > 0, "missing tight single-parity pattern")
    return {"row_patterns": records, "tight_full_acceptance_single_parity_patterns":
            tight_regular_single}


def poly_mod(x, divisor):
    while x.bit_length() >= divisor.bit_length():
        x ^= divisor << (x.bit_length() - divisor.bit_length())
    return x


def is_irreducible(modulus):
    degree = modulus.bit_length() - 1
    # Any reducible binary polynomial has a monic factor of degree <= degree/2.
    return all(poly_mod(modulus, d) != 0 for d in range(2, 1 << (degree//2 + 1)))


def fsquare(x, modulus):
    square = sum(1 << (2*i) for i in range(x.bit_length()) if x >> i & 1)
    return poly_mod(square, modulus)


def split_witness(a, k, modulus):
    s, n = 1 << a, 1 << k
    m, dimension = n//(2*s), n//s
    require(k in (2*a+2, 2*a+3), "two-level shape")
    require(modulus.bit_length() == k+1 and is_irreducible(modulus), "field modulus")
    power = list(range(n))
    for _ in range(dimension.bit_length()-1):
        power = [fsquare(x, modulus) for x in power]
    require(len(set(power)) == n, "Frobenius permutation")
    root = [None] * n

    # Alias inner-parent cells directly onto the outer row; every non-parent
    # inner entry is d. No verdict for an unspecified leaf is assumed.
    statuses = Counter()
    for v in range(m):
        d = v % 2
        outer = [(w//s) % 2 for w in range(2*s*s)]
        for u in range(2*s):
            x = 2*s*v + u
            outer[u] = d if u//s == d else power[x]
            root[x] = outer[u]
        for u in range(2*s):
            p, b = divmod(u, s)
            # All outer common columns are constant by computing each shared
            # cell's parity. Repeating at every v verifies the whole column.
            for h in range(s//2):
                require(outer[s*s+2*s*h+u] == p, "outer column")
            # The entire inner common rectangle is outside the parent cells.
            for h in range(s//2):
                require(s*s//2 + s*h+b >= s, "inner common column alias")
            if p == d:
                for f in range(s):
                    j = p + 2*f
                    require(all(value == d for value in outer[s*j:s*(j+1)]),
                            "passing inner-row parents")
                statuses["accepted_by_constant_leaves"] += 1
            else:
                # One selected leaf suffices. Its other s*s-s cells equal d,
                # too many for a nonconstant polynomial of degree below s.
                j = p + 2
                require(s*s-s >= s and all(value != d for value in outer[s*j:s*(j+1)]),
                        "rejecting inner row")
                statuses["rejected_by_mixed_leaf"] += 1
    require(min(statuses.values()) == n//2 and len(statuses) == 2, "seed count")
    constants = max(Counter(root).values())
    require(constants == n//4, "constant agreement")
    cap = (dimension-1)*2 + dimension
    result = {"seeds": dict(statuses), "best_constant_agreements": constants,
              "nonconstant_agreement_upper_bound": cap,
              "distance_lower": n-max(cap, constants), "distance_upper": n-constants}
    if a >= 4:
        require(result["distance_lower"] == result["distance_upper"] == 3*n//4,
                "witness tightness")
    return result


if __name__ == "__main__":
    moduli = {8: 0x11B, 9: 0x211, 10: 0x409, 11: 0x805}
    outputs = {"accounting": {s: accounting(s) for s in (8, 16)},
               "witnesses": {f"a{a}_k{k}": split_witness(a, k, moduli[k])
                             for a in (3, 4) for k in (2*a+2, 2*a+3)}}
    print(json.dumps(outputs, indent=2, sort_keys=True))
