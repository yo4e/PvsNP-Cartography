# The address problem ends at the seed rows

**Status: candidate-survives for the written normalization/cost derivations;
exact finite evidence for the stated fixtures; novelty-unknown.** This session
completes [Issue #37](https://github.com/yo4e/PvsNP-Cartography/issues/37) and
changes the next research target to [Issue #38](https://github.com/yo4e/PvsNP-Cartography/issues/38).

## 1. The fixed-rate source permits a cheap shared layout

A canonical recursive address contains the path shape, saved edge labels and
the live point. Those edge labels depend on the seed, so calling them constant
row identifiers was not valid. The repair is a public inverse shuffle:
reconstruct the root's coordinate order from **all** those fields, and extract
only the fresh auxiliary coordinates as the row tag.

For every fixed tape and leaf offset in the stated Expedition 038 variant,
the canonical query becomes

    (constant row identity, z XOR a constant mask).

It is a single map on physical cells, so root, parent and sibling aliases
remain shared. For fixed rate exponent `a`, the number of symbol rows satisfies

    R_a(k)=1                                      (k<=2a),
    R_a(k)=2^a R_a(floor(k/2)+a)
           +2^(a-1)(R_a(ceil(k/2))-1)             (k>2a),

and is polynomial in `k`. A later guessed injective row-label table therefore
costs polynomially many bits. This is a real difference from the growing
one-level fixture of Expedition 046, not a reversal of that fixture's scoped
cost calculation. [Coordinate argument and counts](normalization.md)

## 2. The first two-level geometry and actual residual agree after transport

At `a=3,k=8`, the canonical shapes root/R/RR give 1/7/56 rows, totaling
64 complete rows and 16,384 stored symbols. All 4,672 distinct fixed-tape
offset occurrences were checked on all 256 seeds: **1,196,032** direct query
comparisons, plus 16,384 separate column/sibling alias controls. Every physical
cell is reached. The symbolic controls also retain the exact root-coordinate
order on larger mixed paths through `k=33`.

The normalized indexing was then connected to the **actual** two-level
GF(256) residual fixture of Expedition 041, including its same shared root.
A bijection of all 16,384 symbols checks 18,432 names with aliases. Every
ordered leaf input and the residual agree before and after transport.

| Actual field fixture | Paired RS accepts | Joint accepts | Joint rejects |
|---|---:|---:|---:|
| Honest YES, `A=1+X,B=X` | 256 | 256 | 0 |
| Degree-31 NO extremizer | 256 | 35 | 221 |
| Same NO with root symbol 48 changed | 240 | 35 | 221 |

The field arithmetic and interpolation implementation are reused. The sharp
221 bound is inherited from Expedition 041's separate all-assignment argument;
it is **not** a Boolean-clause rejection count. This replay is not a generated
full source compiler. [Field replay output](recursive-field-bridge-results.json)

For this named YES proof, all 1,016 raw B bit rows have seed degree at most one:
536 are zero, 192 are nonzero constants and 288 have degree one. The eight raw
A rows are also affine. The NO extremizer has 504 B rows of degree four and
512 of degree five. These are actual finite row functions, not a bound on
arbitrary accepting proofs or on the Boolean compiler's auxiliary gate rows.

## 3. Direct row polynomials make further tag guessing unnecessary

Let `Delta_E(f)` be the minimum possible maximum seed degree of one polynomial
per row, subject to a total of at most `E` errors on used physical cells.
For every injective tag-only layout, restriction of a degree-`d` global
polynomial to each tag gives `Delta_E<=d`. Conversely, ordinary dense tags
and their selector polynomials give degree at most

    Delta_E + ceil(log2 R).

The same inequalities survive minimization over **all satisfying witnesses**.
They do not replace existential completeness by an all-witness hypothesis.
The error convention is used-cell error with free padding; whole-cube error
rates need their denominators and prescribed padding handled separately.

The stronger algorithmic statement is useful: directly guess the shared row
polynomials. This takes `R*sum_{j<=d} binom(k,j)=2^{o(k)}` bits when
`R=poly(k),d=O(k/log k)`. Each fixed literal still has degree at most `d`, so
the same counter sees clause degree at most `3d`. Every guessed tag layout
and degree-`d` polynomial already supplies such a tuple. Tag guessing adds
no accepting power to this certificate class at the same seed degree.

There is also full-row query coverage: follow the desired canonical shape,
then a zero-fresh all-R suffix and offset zero. The suffix returns to the
desired row. Consequently even a more general globally consistent recoding
whose **actual query values** are all low degree is covered by row polynomials;
pin-only rows cost at most one extra degree to glue their two halves.

The conditional unary hierarchy argument makes the limitation precise. Under
the stated polynomial-time compiler, computable gap, external hierarchy and
counting hypotheses, infinitely many YES lengths defeat the weighted
degree-`alpha*n/log n` approximation condition for **every** satisfying proof.
This is a written consequence of the existing method, with no new explicit
hard input or lower-bound theorem claimed. [Full costs and quantifiers](cost-and-collapse.md)

## 4. Attacks that survived into the record

- A global invertible map with seven ANDs and one XOR takes a degree-one
  polynomial to degree eight on an actual RR query. A short description
  does not supply the low-degree counting hypothesis.
- An artificial assignment on the same 64 physical rows has exact and
  `E<=15` degree ten in the dense layout, five under an explicit adaptive
  layout with free padding, and four for independent row polynomials.
  Disjoint affine parity cubes prove these minima in the stated models.
- The degree-five completion makes 1,008 errors if the enlarged padding is
  forced to zero. Free completion cannot be silently substituted for a
  predetermined full-cube target.
- A separate exhaustive tiny checker verifies the row sandwich on all
  256 two-row functions and nine error budgets, with sparse-tag, composition,
  precision and clamp-gluing controls.

[Degree certificates](degree-controls.md) ·
[Preserved failed shortcuts](../../graveyard/2026-11-28-recursive-layout-shortcuts.md)

## Research decision and limits

**Complete the layout-cost milestone and park additional tag search as the
route to an asymptotic improvement.** The actual unknown is the seed dependence
of residual-constrained accepting proofs and their Boolean gate rows under
the correctly weighted error budget. The next experiment must discriminate
that question, or a stronger counting method for structured high-degree row
functions, rather than generate another address layout.

All four suites passed normal Python and `-O` with identical stored output.
See [execution evidence](execution-evidence.md) for exact source/result hashes
and the 20 matching immutable GitHub files plus eight further successful
executions from the fetched implementation commit. No new Lean or CI acceptance,
independent external review, novelty, broad circuit lower bound or P-versus-NP
separation is claimed. Issues #8 and #15 remain separate.
