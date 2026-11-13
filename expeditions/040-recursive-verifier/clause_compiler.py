"""Generate a fixed signed-clause verifier. Bit i of a packed word is seed i."""
import importlib.util
from functools import reduce
from operator import xor
from pathlib import Path

from recursive_rs import C0, C1, C2, COL_CHECKS, F_SIZE, THETA, eval_poly, inv, mul, times_linear

# The preceding expedition's gate clauses are reused with signed input wires.
previous = Path(__file__).resolve().parents[1] / "039-unary-overlap-counting" / "verify_base_acsp.py"
spec = importlib.util.spec_from_file_location("base_case", previous)
base_case = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base_case)
gate_clauses = base_case.gate_clauses
SEEDS = range(F_SIZE)
FULL = (1 << F_SIZE) - 1
PUBLIC = tuple(sum(1 << z for z in SEEDS if z >> i & 1) for i in range(7))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def signed(bits, literal):
    value = bits[abs(literal)]
    return value if literal > 0 else value ^ FULL


def permute_seed(mask, offset):
    """Return the table z -> mask[z XOR offset] in seven butterfly steps."""
    for i, high in enumerate(PUBLIC):
        bit = 1 << i
        if offset & bit:
            mask = ((mask & high) >> bit) | ((mask & (FULL ^ high)) << bit)
    return mask


def lagrange_columns():
    # Ascending monomial coefficients of the eight Lagrange basis polynomials.
    columns = []
    for j in range(8):
        coeffs = [1]
        for h in range(8):
            if h != j:
                coeffs = times_linear(coeffs, h)
        scale = inv(eval_poly(coeffs, j))
        columns.append([mul(scale, w) for w in coeffs])
    return columns


class BitCircuit:
    """Constant-fold and share Boolean gates; read keys name physical symbol bits."""

    def __init__(self):
        self.one = 1
        self.zero = -1
        self.size = 1
        self.inputs = {("constant",): 1}
        self.gates = []
        self.memo = {}
        self.public = [self.input(("seed", i)) for i in range(7)]
        self.output = None

    def input(self, key):
        if key not in self.inputs:
            self.size += 1
            self.inputs[key] = self.size
        return self.inputs[key]

    def gate(self, op, a, b):
        if op == "and":
            if a == self.zero or b == self.zero or a == -b:
                return self.zero
            if a == self.one or a == b:
                return b
            if b == self.one:
                return a
        elif op == "xor":
            if a == b:
                return self.zero
            if a == -b:
                return self.one
            if abs(a) == 1:
                return b if a == self.zero else -b
            if abs(b) == 1:
                return a if b == self.zero else -a
        else:
            raise ValueError(op)
        key = (op, min(a, b), max(a, b))
        if key not in self.memo:
            self.size += 1
            self.memo[key] = self.size
            self.gates.append((*key, self.size))
        return self.memo[key]

    def parity(self, values):
        return reduce(lambda u, v: self.gate("xor", u, v), values, self.zero)

    def add(self, *words):
        return [self.parity(bits) for bits in zip(*words)]

    def read(self, block, page, delta, width):
        real_bits = 7 if block == "A" or page == 0 else 14
        return [self.input((block, page, i, delta)) if i < real_bits else self.zero
                for i in range(width)]

    def constant(self, value, width):
        return [self.one if value >> i & 1 else self.zero for i in range(width)]

    def scale(self, word, factor):
        images = [mul(1 << j, factor) for j in range(len(word))]
        return [self.parity(w for w, image in zip(word, images) if image >> i & 1)
                for i in range(len(word))]

    def product(self, left, right):
        width = len(left)
        terms = [[] for _ in range(width)]
        for i, u in enumerate(left):
            for j, v in enumerate(right):
                w = self.gate("and", u, v)
                image = mul(1 << i, 1 << j)
                for h in range(width):
                    if image >> h & 1:
                        terms[h].append(w)
        return [self.parity(row) for row in terms]

    def linear_combination(self, words, scalars):
        return self.add(*(self.scale(word, c) for word, c in zip(words, scalars)))

    def translate(self, coeffs, shift, guard=None):
        """Coefficients of P(X+shift), optionally selected by one public bit."""
        result = list(coeffs)
        power = shift
        for bit in (1, 2, 4):
            for i in range(8):
                if i & bit:
                    term = self.scale(result[i], power)
                    if guard is not None:
                        term = [self.gate("and", guard, u) for u in term]
                    result[i ^ bit] = self.add(result[i ^ bit], term)
            power = mul(power, power)
        return result

    def row_checks(self):
        # The fixed fresh=0 row schedule enumerates all 64 offsets. Changing
        # fresh only permutes the same field points; no row predicate is lost.
        parent = [self.read("B", 0, i, 14) for i in range(8)]
        basis = lagrange_columns()
        coeffs = [self.linear_combination(parent, weights) for weights in zip(*basis)]
        rectangle = self.translate(coeffs, C0 ^ THETA)
        for j in range(3, 7):
            rectangle = self.translate(rectangle, 1 << j, self.public[j])
        for w in range(8, 64):
            point = (w & 7) ^ (C1 if w & 8 else 0) ^ (C2 if w & 16 else 0)
            powers = [1]
            for _ in range(7):
                powers.append(mul(powers[-1], point))
            expected = self.linear_combination(rectangle if w & 32 else coeffs, powers)
            actual = self.read("B", w >> 3, w & 7, 14)
            yield from self.add(expected, actual)

    def column_checks(self):
        for fresh in range(4):
            page = 4 + fresh
            start = [self.read("B", page, v << 3, 14) for v in range(2)]
            for v, weights in enumerate(COL_CHECKS, start=2):
                # The actual ordinate is translated by the inherited high seed.
                # Column abscissa differences are unchanged by q's additivity.
                predicted = self.linear_combination(start, weights)
                yield from self.add(predicted, self.read("B", page, v << 3, 14))

    def compile(self, no):
        x = self.public
        a = [self.read("A", 0, u, 7) for u in SEEDS]
        b = self.read("B", 0, 0, 7)

        def vanisher(points):
            return reduce(self.product, (self.add(x, self.constant(t, 7)) for t in points))

        def triple(u, v, w):
            return self.product(self.product(u, v), w)

        first = self.add(a[0], self.constant(1, 7))
        third = self.add(a[int(not no)], self.constant(1, 7))
        other = a[int(no)]
        residual = self.add(
            self.product(vanisher((1, 2, 3)), triple(first, first, third)),
            self.product(vanisher((0, 2, 3)), triple(other, other, other)),
            self.product(vanisher((0, 1)), self.product(a[2], self.add(a[2], self.constant(1, 7)))),
            self.product(vanisher((0, 1, 2, 3)), b))
        bad = list(residual)
        slope = self.add(a[0], a[1])
        for w in range(2, F_SIZE):
            bad.extend(self.add(a[w], a[0], self.scale(slope, w)))
        bad.extend(self.row_checks())
        bad.extend(self.column_checks())
        self.output = reduce(lambda u, v: self.gate("and", u, -v), bad, self.one)
        return self

    def templates(self):
        yield (self.one,)
        for op, a, b, c in self.gates:
            yield from gate_clauses(op, a, b, c)
        yield (self.output,)

    def evaluate(self, a, cells):
        require(len(a) == 128 and len(cells) == 1024, "word lengths")
        require(all(0 <= x < 128 for x in [*a, *cells[:128]]), "external root alphabet")
        require(all(0 <= x < 16384 for x in cells[128:]), "extension alphabet")
        packed = {}
        for block, words in (("A", a), ("B", cells)):
            for page in range(len(words) // 128):
                for bit in range(7 if page == 0 else 14):
                    packed[block, page, bit] = sum(
                        ((words[128 * page + z] >> bit) & 1) << z for z in SEEDS)
        vals = [0] * (self.size + 1)
        for key, wire in self.inputs.items():
            if key[0] == "constant":
                vals[wire] = FULL
            elif key[0] == "seed":
                vals[wire] = PUBLIC[key[1]]
            else:
                vals[wire] = permute_seed(packed[key[:3]], key[3])
        for op, a, b, c in self.gates:
            u, v = signed(vals, a), signed(vals, b)
            vals[c] = u ^ v if op == "xor" else u & v
        return vals


class PhysicalCNF:
    """Compile cell tags and signed wires to one-address-cube DIMACS variables."""

    def __init__(self, circuit):
        self.circuit = circuit
        self.read = {}
        tags = {}
        self.num_tags = 0
        for key, wire in circuit.inputs.items():
            if key[0] in ("A", "B"):
                tag = tags.setdefault(key[:3], len(tags))
                self.read[wire] = (tag, key[3])
        self.num_tags = len(tags)
        for wire in range(1, circuit.size + 1):
            if wire not in self.read:
                self.read[wire] = (self.num_tags, 0)
                self.num_tags += 1
        self.templates = tuple(circuit.templates())
        self.template_count = len(self.templates) + 14

    def pack_assignment(self, vals):
        bits = [None] * self.num_tags
        for wire, (tag, delta) in self.read.items():
            table = permute_seed(vals[wire], delta)
            require(bits[tag] is None or bits[tag] == table, "inconsistent physical proof")
            bits[tag] = table
        return bits

    def failures(self, bits):
        # Re-read physical blocks using their final tag and public address.
        values = [0] * (self.circuit.size + 1)
        for wire, (tag, delta) in self.read.items():
            values[wire] = permute_seed(bits[tag], delta)
        missed = sum((FULL ^ reduce(int.__or__, (signed(values, w) for w in clause))).bit_count()
                     for clause in self.templates)
        for i, wire in enumerate(self.circuit.public):
            tag, _ = self.read[wire]
            missed += 2 * (bits[tag] ^ PUBLIC[i]).bit_count()
        return missed

    def address(self, lit, z):
        tag, delta = self.read[abs(lit)]
        cell = 1 + (tag << 7) + (z ^ delta)
        return cell if lit > 0 else -cell

    def clauses_at(self, z):
        for clause in self.templates:
            yield tuple(self.address(w, z) for w in clause)
        for i, wire in enumerate(self.circuit.public):
            for bit in (0, 1):
                clamped = (z & ~(1 << i)) | (bit << i)
                yield (self.address(wire if bit else -wire, clamped),)
