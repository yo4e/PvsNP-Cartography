"""BV14 recursive RS geometry for a 128-point translated root and rate 1/8."""
from functools import reduce
from operator import xor

F_SIZE = 128
THETA = F_SIZE
C0, C1, C2 = (u * THETA for u in (2, 4, 8))


def _base_product(x, y):
    result = 0
    while y:
        if y & 1:
            result ^= x
        x <<= 1
        if x & 128:
            x ^= 0x83
        y >>= 1
    return result


BASE_MUL = tuple(tuple(_base_product(x, y) for y in range(F_SIZE)) for x in range(F_SIZE))


def mul(x, y):
    """Product in GF(128)[θ]/(θ²+θ+1); low seven bits are the base coefficient."""
    a, b = x & 127, x >> 7
    c, d = y & 127, y >> 7
    ac = BASE_MUL[a][c]
    bd = BASE_MUL[b][d]
    return (ac ^ bd) | ((BASE_MUL[a ^ b][c ^ d] ^ ac) << 7)


def inv(x):
    if not x:
        raise ZeroDivisionError("zero field element")
    a, b = x & 127, x >> 7
    norm = BASE_MUL[a][a ^ b] ^ BASE_MUL[b][b]
    scalar = BASE_MUL[norm].index(1)
    return BASE_MUL[scalar][a ^ b] | (BASE_MUL[scalar][b] << 7)


def eval_poly(coeffs, x):
    """Evaluate coefficients given in ascending order."""
    y = 0
    for coef in reversed(coeffs):
        y = mul(y, x) ^ coef
    return y


def times_linear(coeffs, root):
    result = [0] * (len(coeffs) + 1)
    for i, coef in enumerate(coeffs):
        result[i] ^= mul(root, coef)
        result[i + 1] ^= coef
    return result


def vanishing(points):
    coeffs = [1]
    for p in points:
        coeffs = times_linear(coeffs, p)
    return coeffs


Q_COEFFS = vanishing(range(8))
COL_POINTS = tuple(eval_poly(Q_COEFFS, THETA ^ (r << 3)) for r in range(16))


def row_point(row, w):
    origin = THETA ^ (row << 3)
    x = origin ^ (w & 7)
    if w & 8:
        x ^= C1
    if w & 16:
        x ^= C2
    if w & 32:
        x ^= C0 ^ origin
    return x


ROW_POINTS = tuple(tuple(row_point(r, w) for w in range(64)) for r in range(16))


def row_cell(row, w):
    """Canonical word address, with the parent occupying exactly [0,128)."""
    return ((w >> 3) << 7) | (row << 3) | (w & 7)


def col_cell(col, v):
    return row_cell(v, 32 + col)


def row_query(z, fresh, offset):
    inherited = (fresh << 3) | (z & 7)
    return row_cell(z >> 3, inherited ^ offset)


def col_query(z, fresh, offset):
    col = (fresh << 3) | (z & 7)
    return col_cell(col, (z >> 3) ^ offset)


def split_polynomial(coeffs):
    """Return R,S of degree <8 with P(X+θ)=R(X)+q(X)S(X)."""
    coeffs = list(coeffs)
    if len(coeffs) > 16 or any(not 0 <= c < F_SIZE for c in coeffs):
        raise ValueError("external polynomial must have 0..16 coefficients in GF(128)")
    translated = []
    for c in reversed(coeffs):
        translated = times_linear(translated, THETA) if translated else [0]
        translated[0] ^= c
    translated += [0] * (16 - len(translated))
    quotient = [0] * 8
    for i in reversed(range(8)):
        quotient[i] = lead = translated[i + 8]
        for j, qj in enumerate(Q_COEFFS):
            translated[i + j] ^= mul(lead, qj)
    return translated[:8], quotient


def honest_cells(coeffs):
    """Extend an external P of degree <16 to the 1,024 physical oracle symbols."""
    r_coeffs, s_coeffs = split_polynomial(coeffs)
    cells = [0] * 1024
    for r, points in enumerate(ROW_POINTS):
        y = COL_POINTS[r]
        for w, x in enumerate(points):
            cells[row_cell(r, w)] = eval_poly(r_coeffs, x) ^ mul(y, eval_poly(s_coeffs, x))
    return cells


def interpolation_weights(nodes, x):
    weights = []
    for i, node in enumerate(nodes):
        numerator = denominator = 1
        for j, other in enumerate(nodes):
            if j != i:
                numerator = mul(numerator, x ^ other)
                denominator = mul(denominator, node ^ other)
        weights.append(mul(numerator, inv(denominator)))
    return tuple(weights)


def _interpolation_checks(points, cutoff):
    nodes = points[:cutoff]
    return tuple(interpolation_weights(nodes, p) for p in points[cutoff:])


ROW_CHECKS = tuple(_interpolation_checks(points, 8) for points in ROW_POINTS)
COL_CHECKS = _interpolation_checks(COL_POINTS, 2)


def _valid_word(values, checks, cutoff):
    basis = values[:cutoff]
    return all(reduce(xor, (mul(y, w) for y, w in zip(basis, row)), 0) == expected
               for row, expected in zip(checks, values[cutoff:]))


def row_ok(cells, r):
    return _valid_word([cells[row_cell(r, w)] for w in range(64)], ROW_CHECKS[r], 8)


def col_ok(cells, c):
    return _valid_word([cells[col_cell(c, v)] for v in range(16)], COL_CHECKS, 2)
