# What a row label can change, and what a general address circuit can hide

These are elementary written arguments and exact finite controls, not a new
formal proof or a novelty claim. Run `python check_layout_degree.py` from this
directory or by its repository-relative path. The geometry comes from the
public normalization; the bit assignment below is deliberately artificial and
is **not** asserted to pass an RS or outer residual test.

## 1. A short invertible description can have large substitution degree

The first two-level example has 64 normalized symbol rows and 256 root
coordinates. Write its whole 14-bit cube as `(r,z)`, where `r` has six bits and
`z` has eight. Define

    Phi(r,z) = (r XOR (AND(z_0,...,z_7),0,0,0,0,0), z).

This is a permutation of the entire cube, and its inverse is itself. Seven
binary ANDs and one XOR implement the displayed circuit. The degree-one new
proof polynomial `P(r,z)=r_0` pulls back to

    P(Phi(r,z)) = r_0 + z_0 z_1 ... z_7,

of degree eight. The actual `RR` offset query with fresh tape zero and offset
zero returns to the root; after normalization it is `(0,z)`. The pullback on
that genuine recursive query is exactly `AND_8`, still of degree eight.

The program checks all 16,384 inverse images and inverse identities, computes
the complete multilinear normal form, and evaluates that actual query on all
256 seeds. The same construction on `k` seed coordinates has an `O(k)`-gate
description and query degree `k`. This is an algebraic family argument; the
finite run is its concrete control. No hard counting problem is inferred for
this particular AND function: it is easy to count by its special form. The
counterexample only refutes the inference that a short circuit description
automatically meets the **low-degree polynomial** counter's hypothesis.

This map varies the row tag with the seed. The useful guessed maps in the
normalization result instead assign a **constant** tag to each complete row.
They preserve degree on every literal by construction. A general succinct map
is a different model and needs its own composition or structured-counting
algorithm.

## 2. A precise five-degree saving, with an unchanged row obstruction

Use one bit at each of the 16,384 canonical symbol positions. On row zero set

    f_0(z) = z_0 z_1 z_2 z_3,

and set all other 63 rows to zero. The final four seed bits are unused.
The ordinary six-bit dense row encoding is

    F(r,z) = (product_{j=0}^5 (1+r_j)) z_0 z_1 z_2 z_3,

with exact degree ten. There is no padding in this dense symbol-bit universe.

Relabel row zero by a seven-bit tag with low bit one and all other bits zero.
Relabel the 63 zero rows by distinct tags with low bit zero, using their
within-class rank for the remaining six bits. All rows remain distinct. The
completion

    P(c,z) = c_0 z_0 z_1 z_2 z_3

has degree five and agrees on every used cell. It uses twice as large an
ambient cube. This is an explicit, witness-dependent tag table for this known
artificial assignment, not a public encoding of unknown accepting witnesses.

### The same minima survive up to fifteen raw errors

For each fixed setting of the high four seed bits, let all six dense tag bits
and the low four seed bits vary. These sixteen disjoint ten-dimensional cubes
each have odd target parity. Every degree-at-most-nine polynomial has even
parity on each cube. Thus the public dense layout needs at least sixteen
errors at degree nine or below; its minimum degree at any raw budget
`0 <= E <= 15` is exactly ten.

For **any** injective tag-only relabeling, select the nonzero row and one zero
row. Their two distinct tags span an affine line. Cross that line with the four
low seed directions, fixing the high seed bits. Every resulting affine
five-cube uses only those two physical rows and has odd parity. A polynomial
of degree at most four remains of degree at most four under this affine
substitution and has even five-cube parity. The sixteen disjoint high-seed
sections force at least sixteen used-cell errors, regardless of unused
padding or the width of the tags.

The displayed degree-five completion attains zero used errors. Therefore the
minimum over **all injective tag-only layouts with free padding** is exactly
five for `E <= 15`. The minimum possible maximum degree of independent row
polynomials is four: the nonzero row itself contains sixteen disjoint
odd four-cubes, excluding degree three at those budgets. Sixteen errors let the all-zero polynomial fit in every
model, so this boundary is sharp. The enumeration checks all 8,128 unordered
pairs of seven-bit tags and their 130,048 sections; the argument above, rather
than that enumeration, covers arbitrary tag widths.

This illustrates the general comparison: tags can remove a degree cost of
selecting a row, while the actual seed function on the row still has to be
represented. In the fixed-rate source there are only polynomially many rows,
so the row-selection cost is `O(log k)`. The lead's finite control does not
establish a degree lower bound for any accepting source proof.

## 3. Free padding is a mathematical choice

The degree-five completion assigns values to unused tags. If those unused
positions are instead required to be zero, the same sparse layout's exact
degree is eleven. The degree-five polynomial makes 1,008 errors against that
zero-filled target, all on padding. The executable explicitly checks both
numbers.

Thus preservation of raw errors on physical cells does not imply preservation
of the error rate against an arbitrarily preassigned padded target. The row
sandwich is stated on used cells with free padding; the hierarchy simulation
evaluates those physical reads. Any claim about uniform approximation to one
fixed full-cube language must specify its padding and occupied-length encoding
separately. The five selected physical error sites in the executable transport
exactly through the injection, independently of padding.

## Evidence boundary

The checker uses exact Python integer/bit arithmetic, a complete Boolean
multilinear transform, and address routines from the pinned Expedition 038.
No sampling, floating-point optimization, heuristic fit, Lean proof, new
soundness constant, or complexity separation is hidden in these statements.
