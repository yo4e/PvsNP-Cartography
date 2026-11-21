"""Fixed-query GF(128) verifier with a sparse, field-linear A test.

The default schedule is the 23-offset cross. Integer radii 1, 2 and 3 name
earlier Hamming-ball trials. Only A membership changes from Expedition 040. The residual,
shared recursive B geometry, signed gate clauses, and clamped public pins
are inherited. This implementation does not assert a NO rejection minimum.
"""
from functools import cache, reduce
from pathlib import Path
import sys

EXPEDITIONS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXPEDITIONS / "040-recursive-verifier"))
sys.path.insert(0, str(EXPEDITIONS / "044-bounded-fanout"))
import clause_compiler as cc
import recursive_rs as rs
import verify_geometry as ref
import verify_verifier as inherited
import check_fanout as fanout

DIRECTIONS = (2, 4, 8, 16, 32, 64)
OFFSETS = (0, 1, *DIRECTIONS)


def offsets_for(radius):
    if radius == "cross":
        # Complementary binary subspaces U (low three bits) and V (high
        # four bits), sharing only zero. The union has 8+16-1 = 23 points.
        return tuple(sorted(set(range(8)) | set(range(0, 128, 8))))
    cc.require(radius in (1, 2, 3), "supported star schedule")
    return tuple(s for s in range(128) if s.bit_count() <= radius)


class SparseCircuit(cc.BitCircuit):
    """Require A(x+s)+A(x)=s D_1 A(x) for the selected fixed star."""

    def __init__(self, radius="cross"):
        super().__init__()
        self.radius = radius
        self.offsets = offsets_for(radius)

    def compile(self, no):
        x = self.public
        a = {u: self.read("A", 0, u, 7) for u in self.offsets}
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
        for s in self.offsets:
            if s in (0, 1):
                continue
            bad.extend(self.add(a[s], a[0], self.scale(slope, s)))
        bad.extend(self.row_checks())
        bad.extend(self.column_checks())
        self.output = reduce(lambda u, v: self.gate("and", u, -v), bad, self.one)
        return self


def affine_bad_seeds(a, radius="cross"):
    """Scalar membership only, using the independent reference field product."""
    return [x for x in range(128) if any(
        a[x ^ s] ^ a[x] ^ ref.mul(s, a[x ^ 1] ^ a[x])
        for s in offsets_for(radius) if s not in (0, 1))]


@cache
def leaf_membership(cells):
    """Absolute B interpolation, cached only by the entire immutable table."""
    rows = []
    for v, points in enumerate(ref.ROWS):
        word = [cells[(w // 8) * 128 + v * 8 + w % 8] for w in range(64)]
        rows.append(ref.degree_below(points, word, 8))
    cols = []
    for c in range(32):
        word = [cells[(4 + c // 8) * 128 + v * 8 + c % 8] for v in range(16)]
        cols.append(ref.degree_below(ref.COLUMNS, word, 2))
    return tuple(rows), tuple(cols)


def direct(a, cells, no, radius="cross"):
    """Absolute leaf interpolation and scalar residual; no Boolean gate reuse."""
    cc.require(len(a) == 128 and len(cells) == 1024, "scalar word lengths")
    cc.require(all(0 <= v < 128 for v in [*a, *cells[:128]]) and
               all(0 <= v < 16384 for v in cells[128:]), "scalar alphabet")
    rows, cols = leaf_membership(tuple(cells))
    bad_a = set(affine_bad_seeds(a, radius))
    passed = 0
    for x in range(128):
        if x in bad_a or not rows[x >> 3] or not all(
                cols[(x & 7) + 8 * f] for f in range(4)):
            continue
        first = ref.product([x ^ t for t in (1, 2, 3)] +
                            [a[x] ^ 1, a[x] ^ 1, a[x ^ int(not no)] ^ 1])
        second = ref.product([x ^ t for t in (0, 2, 3)] + [a[x ^ int(no)]] * 3)
        range_check = ref.product([x, x ^ 1, a[x ^ 2], a[x ^ 2] ^ 1])
        quotient = ref.product([x ^ t for t in (0, 1, 2, 3)] + [cells[x]])
        if first ^ second ^ range_check ^ quotient == 0:
            passed |= 1 << x
    return passed


def build(no=False, cap=21, radius="cross"):
    source = SparseCircuit(radius).compile(no)
    circuit = fanout.CopyCircuit(source, cap, cc)
    return circuit, cc.PhysicalCNF(circuit)
