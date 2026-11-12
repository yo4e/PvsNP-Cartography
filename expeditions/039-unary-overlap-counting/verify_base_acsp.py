"""Generate two fixed signed-clause systems for a base-case BV14-shaped ACSP."""
from functools import reduce
from operator import xor
import argparse
import json
import random

Q, K = 32, 5
FIELD = range(Q)
BITS = range(K)
FULL = (1 << Q) - 1
SEED = [sum(1 << z for z in FIELD if z & (1 << i)) for i in BITS]


def check(ok):
    if not ok:
        raise ValueError("conformance check failed")


def mul(a, b):
    product = 0
    while b:
        if b & 1:
            product ^= a
        a <<= 1
        if a & Q:
            a ^= 0b100101  # X^5 + X^2 + 1
        b >>= 1
    return product


def inv(a):
    return next(b for b in FIELD if mul(a, b) == 1)


def product(seq):
    return reduce(mul, seq, 1)


def zero_set(points, x):
    return product(x ^ v for v in points)


def weights(nodes, x):
    return [mul(zero_set([w for w in nodes if w != v], x),
                inv(zero_set([w for w in nodes if w != v], v))) for v in nodes]


def interpolate(nodes, values, x):
    return reduce(xor, (mul(a, b) for a, b in zip(weights(nodes, x), values)), 0)


def residual(a, b, x, no):
    # H1={0}, H2=H0={0,1}, H={0,1,2,3}.
    shift = int(no)
    terms = [
        mul(zero_set([1, 2, 3], x), product([a[x] ^ 1, a[x] ^ 1, a[x ^ int(not no)] ^ 1])),
        mul(zero_set([0, 2, 3], x), product([a[x ^ shift]] * 3)),
        mul(zero_set([0, 1], x), mul(a[x ^ 2], a[x ^ 2] ^ 1)),
        mul(zero_set([0, 1, 2, 3], x), b[x]),
    ]
    return reduce(xor, terms)


def code_by_moments(word, cutoff):
    # sum x^j word(x)=0, 0<=j<q-1-(cutoff-1), on the full field
    powers = [1] * Q
    for _ in range(Q - cutoff):
        if reduce(xor, (mul(p, y) for p, y in zip(powers, word)), 0):
            return False
        powers = [mul(x, p) for x, p in enumerate(powers)]
    return True


def gate_clauses(op, a, b, c):
    if op == "and":
        return [(-c, a), (-c, b), (c, -a, -b)]
    return [(a, b, -c), (-a, -b, -c), (a, -b, c), (-a, b, c)]


class Circuit:
    """A cell (gate or input tag, z) is shared by all its uses at seed z."""

    def __init__(self):
        self.inputs = {}
        self.gates = []
        self.clauses = []
        self.size = 0
        self.zero = self.input(("constant", 0))
        self.one = self.input(("constant", 1))
        self.clauses.extend([(-self.zero,), (self.one,)])

    def new(self):
        self.size += 1
        return self.size

    def input(self, key):
        if key not in self.inputs:
            self.inputs[key] = self.new()
        return self.inputs[key]

    def gate(self, op, a, b):
        c = self.new()
        self.gates.append((op, a, b, c))
        self.clauses.extend(gate_clauses(op, a, b, c))
        return c

    def summation(self, terms):
        terms = list(terms)
        if not terms:
            return self.zero
        return reduce(lambda a,b: self.gate("xor", a, b), terms)

    def constant(self, value):
        return [self.one if value >> i & 1 else self.zero for i in BITS]

    def add(self, a, b):
        return [self.gate("xor", u, v) for u, v in zip(a, b)]

    def multiply(self, a, b):
        terms = [[] for _ in BITS]
        for i in BITS:
            for j in BITS:
                bit = self.gate("and", a[i], b[j])
                mask = mul(1 << i, 1 << j)
                for k in BITS:
                    if mask >> k & 1:
                        terms[k].append(bit)
        return list(map(self.summation, terms))

    def linear_check(self, table, cutoff):
        bad = []
        for w in range(cutoff, Q):
            coefs = weights(list(range(cutoff)), w)
            for i in BITS:
                terms = [table[w][i]]
                for j, coef in enumerate(coefs):
                    for k in BITS:
                        if mul(coef, 1 << k) >> i & 1:
                            terms.append(table[j][k])
                bad.append(self.summation(terms))
        return bad

    def evaluate(self, a, b):
        values = [0] * (self.size + 1)
        for key, wire in self.inputs.items():
            kind, index, *tail = key
            if kind == "constant":
                values[wire] = FULL if index else 0
            elif kind == "seed":
                values[wire] = SEED[index]
            else:
                table = a if kind == "A" else b
                values[wire] = sum(1 << z for z in FIELD if table[z ^ index] >> tail[0] & 1)
        for op, u, v, c in self.gates:
            values[c] = (values[u] ^ values[v]) if op == "xor" else (values[u] & values[v])
        return values

    def failures(self, values):
        # Also evaluate both physical half-cube pins for each seed bit.
        missed = 0
        for clause in self.clauses:
            covered = 0
            for lit in clause:
                val = values[abs(lit)]
                covered |= val if lit > 0 else FULL ^ val
            missed += Q - covered.bit_count()
        for i in BITS:
            word = values[self.inputs["seed", i]]
            for eps in (0, 1):
                for z in FIELD:
                    clamped = (z & ~(1 << i)) | (eps << i)
                    missed += int((word >> clamped & 1) != eps)
        return missed


def compile_case(no):
    c = Circuit()
    x = [c.input(("seed", i)) for i in BITS]
    a, b = [[[c.input((block, w, i)) for i in BITS] for w in FIELD] for block in ("A", "B")]

    def zero_at(subset):
        return reduce(c.multiply, (c.add(x, c.constant(t)) for t in subset))

    def cube(y):
        return c.multiply(c.multiply(y, y), y)

    first = c.add(a[0], c.constant(1))
    third = c.add(a[int(not no)], c.constant(1))
    terms = [
        c.multiply(zero_at([1, 2, 3]), c.multiply(c.multiply(first, first), third)),
        c.multiply(zero_at([0, 2, 3]), cube(a[int(no)])),
        c.multiply(zero_at([0, 1]), c.multiply(a[2], c.add(a[2], c.constant(1)))),
        c.multiply(zero_at([0, 1, 2, 3]), b[0]),
    ]
    bad = reduce(c.add, terms) + c.linear_check(a, 2) + c.linear_check(b, 4)
    passed = [c.gate("xor", wire, c.one) for wire in bad]
    accept = reduce(lambda u, v: c.gate("and", u, v), passed)
    c.clauses.append((accept,))
    return c, accept


class Layout:
    """Resolve every formal input or wire to one shared tag and a five-bit coordinate."""

    def __init__(self, c):
        self.cells = {}
        for key, wire in c.inputs.items():
            if key[0] in ("A", "B"):
                kind, delta, bit = key
                self.cells[wire] = (bit + (K if kind == "B" else 0), delta)
        tag = 2 * K
        for wire in range(1, c.size + 1):
            if wire not in self.cells:
                self.cells[wire] = (tag, 0)
                tag += 1
        self.tags = tag

    def address(self, lit, seed):
        tag, delta = self.cells[abs(lit)]
        var = 1 + (tag << K) + (seed ^ delta)  # DIMACS is one-indexed
        return var if lit > 0 else -var

    def clauses_at(self, c, z):
        for clause in c.clauses:
            yield tuple(self.address(lit, z) for lit in clause)
        for i in BITS:
            wire = c.inputs["seed", i]
            for eps in (0, 1):
                clamped = (z & ~(1 << i)) | (eps << i)
                yield (self.address(wire if eps else -wire, clamped),)

    def physical(self, c, values):
        bits = [None] * (self.tags * Q + 1)
        for wire in range(1, c.size + 1):
            for z in FIELD:
                cell = self.address(wire, z)
                bit = (values[wire] >> z) & 1
                check(bits[cell] in (None, bit))
                bits[cell] = bit
        return bits

    def verify_concrete(self, c, bits):
        total = 0
        for z in FIELD:
            for clause in self.clauses_at(c, z):
                total += int(not any(bits[abs(lit)] == (lit > 0) for lit in clause))
        return total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimacs", choices=["yes", "no"], help="emit the complete physical CNF to stdout")
    args = parser.parse_args()
    if args.dimacs:
        c, _ = compile_case(args.dimacs == "no")
        layout = Layout(c)
        print("p cnf", layout.tags * Q, (len(c.clauses) + 2*K) * Q)
        for z in FIELD:
            for clause in layout.clauses_at(c, z):
                print(*clause, 0)
        return
    check(all(mul(x, inv(x)) == 1 for x in range(1, Q)))
    # Exhaust all eight input/output triples of both gate templates.
    for op in ("xor", "and"):
        for pattern in range(8):
            val = [False] + [bool(pattern >> i & 1) for i in range(3)]
            ok = all(any(val[abs(l)] == (l > 0) for l in clause)
                     for clause in gate_clauses(op, 1, 2, 3))
            check(ok == (val[3] == ((val[1] ^ val[2]) if op == "xor" else val[1] and val[2])))

    a = [x ^ 1 for x in FIELD]
    zero = [0] * Q
    nodes = [4, 5, 6, 7]
    samples = [mul(residual(a, zero, x, False), inv(zero_set(range(4), x))) for x in nodes]
    b = [interpolate(nodes, samples, x) for x in FIELD]
    check(code_by_moments(a, 2) and code_by_moments(b, 4))
    check(all(residual(a, b, x, False) == 0 for x in FIELD))
    # Additional global assignments: flipped proof bits, random words and RS codeword pairs.
    rng = random.Random(1417)
    check(b == list(FIELD))
    sharp_b = [interpolate(nodes, [inv(v) for v in nodes], x) for x in FIELD]
    cases = [(a, b), (zero, sharp_b)]
    for block in (0, 1):
        for pos in FIELD:
            for i in BITS:
                pair = [a.copy(), b.copy()]
                pair[block][pos] ^= 1 << i
                cases.append(tuple(pair))
    for _ in range(8):
        cases.append(tuple([rng.randrange(Q) for _ in FIELD] for _ in range(2)))
        pair = []
        for dim in (2, 4):
            seeds = [rng.randrange(Q) for _ in range(dim)]
            pair.append([interpolate(list(range(dim)), seeds, x) for x in FIELD])
        cases.append(tuple(pair))

    results = {}
    for no in (False, True):
        c, output = compile_case(no)
        layout = Layout(c)
        for wire in layout.cells:
            check(len({layout.address(wire, z) for z in FIELD}) == Q)
        minimum = Q
        for index, (word_a, word_b) in enumerate(cases):
            canonical = c.evaluate(word_a, word_b)
            rejected = FULL ^ canonical[output]
            codes = code_by_moments(word_a, 2) and code_by_moments(word_b, 4)
            direct = sum(1 << x for x in FIELD if not codes or residual(word_a, word_b, x, no))
            check(rejected == direct)
            minimum = min(minimum, direct.bit_count())
            if no:
                check(direct.bit_count() >= 25)
            if index in (0, 1, len(cases)-1):
                count = c.failures(canonical)
                check(count == direct.bit_count())
                if index == int(no):
                    check(count == (25 if no else 0))
                    check(layout.verify_concrete(c, layout.physical(c, canonical)) == count)
                if not no and index == 0:
                    check(count == 0)
                    for wire in [c.one, c.inputs["seed", 0], c.gates[-1][-1]]:
                        canonical[wire] ^= 1
                        check(c.failures(canonical) > 0)
                        canonical[wire] ^= 1
        results["no" if no else "yes"] = {
            "witness_bit_count_AB": 2 * K * Q, "clause_templates_including_pins": len(c.clauses)+2*K,
            "physical_variables": layout.tags*Q, "actual_clauses": (len(c.clauses) + 2*K)*Q,
            "binary_gates": len(c.gates), "min_reject_seeds_sampled": minimum,
            "global_AB_pairs_tested": len(cases), "seeds_per_pair": Q,
        }
    # The selector value at a selected point is nonzero, but need not be 1.
    results["selector_at_zero"] = zero_set([1, 2, 3], 0)
    results["honest_B_samples_at_4_through_7"] = samples
    results["no_sharp_B_samples_at_4_through_7"] = [inv(v) for v in nodes]
    results["no_sharp_accepting_seeds"] = [z for z in FIELD if residual(zero, sharp_b, z, True) == 0]
    check(results["no_sharp_accepting_seeds"] == list(range(1, 8)))
    # A hard Boolean selector evaluated outside H would vanish at x=4.
    results["indicator_substitution_residual_at_4"] = mul(zero_set(range(4), 4), b[4])
    check(results["indicator_substitution_residual_at_4"] == 13)
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
