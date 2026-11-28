# Canonical recursive addresses become fixed tags and translated seeds

Status: written coordinate induction and finite executable controls for the
specified Expedition038 variant. No novel theorem, Lean result, complete
recursive Boolean compiler, or approximation theorem is asserted.

## The apparent obstacle and the exact object being normalized

The actual source-style oracle address has a tree identifier, a path shape,
edge labels, a within-node point, and a symbol-bit index. The edge labels
depend on the seed. It would be false to call the entire path label a fixed
row tag, or to discard it. Nevertheless a *public permutation of these
coordinate positions*, chosen from the canonical path shape, separates the
seed from the fresh coordinates.

This construction acts on a canonical physical address, after parent and
sibling aliases have been resolved. It never uses the route that happened
to request that address. Consequently, aliases remain aliases even when
different recursive leaves or tapes request the same underlying cell.

The source objects inspected are:

- `expeditions/038-recursive-query-fibers/source-compiler.md` and
  `verify_recursive.py`: the specified row-return polarity, path encoding,
  concrete routing and symbolic signed-coordinate model.
- `expeditions/040-recursive-verifier/geometry.md` and `recursive_rs.py`:
  actual parent/row/column sharing in the first recursive level.
- `expeditions/041-two-level-distance/two_level_oracle.py` and
  `check_outer_application.py`: actual GF(256) two-level physical symbols,
  interpolation tests and residual-constrained fixtures.

These are implementations/derivations of a stated variant in the context
of Ben-Sasson--Viola, ECCC TR14-017, Sections6.1--6.3. This note does not
reverify that paper's ACSP or agreement theorems.

## Public inverse shuffle

At a node of dimension d, put l=floor(d/2). An R descent stores V (d-l bits)
and changes the live word (U,V) into (U,A), where A has a bits. A C descent
stores (U,A'), where A' has a-1 bits, and changes the live word into V.

Given a final canonical shape S and its payload, reverse its edges:

    R: (stored V, live (U,A)) -> live (U,V), extracted A.
    C: (stored (U,A'), live V) -> live (U,V), extracted A'.

Keep extracted chunks in their original root-to-leaf edge order. The result
is (S, aux, x), with x having k coordinates and

    e(S) = a #R(S) + (a-1) #C(S)

auxiliary coordinates. The original edge-plus-point payload has exactly
k+e(S) coordinates. Both transformations are coordinate permutations for a
fixed shape; the forward descent is the explicit inverse. Bit-of-symbol
and tree identifiers are retained without modification.

Root addresses have no auxiliary chunk. A stored nonroot address ends in R,
and the last a-bit fresh chunk is nonzero. A terminal C name is redirected
to its row sibling; a terminal R name with fresh chunk zero is redirected
to its parent. **Earlier fresh chunks need not be nonzero.** Removing such
addresses would incorrectly delete valid descendant oracle cells.

## Why every fixed-tape offset query becomes (constant tag, z XOR delta)

Before any offset substitution, reversing the entire down path restores the
root seed z in its original order and extracts only the fixed fresh tape.
Replacing the leaf word by itself XOR a fixed offset complements whichever
coordinate tokens occur in that leaf word. It never mixes two tokens.

A successful R return with fresh chunk zero reinstates the original parent
coordinate order and drops only fixed fresh coordinates. The return/stop
decision is independent of z because those fresh coordinates are fixed once
the tape and offset are fixed.

A C return uses the row sibling, whose edge label is the returned V' and
whose local word is (U,A',1). The reverse R rule restores (U,V') and extracts
(A',1). Thus it restores the same root-coordinate tokens as reversing the
old C frame, while producing a constant nonzero fresh chunk.

Induction through these returns proves that, for each fixed complete tape
and offset slot, there are a fixed canonical shape S, a fixed auxiliary
integer b, and a fixed XOR mask delta such that

    normalize(query(z)) = (S,b,z XOR delta)     for every z in {0,1}^k.

This is stronger than a rank claim: the final root-coordinate order is the
original order. The tag does not contain a remaining seed-dependent path
label. The symbolic checker tests this exact ordering, and the scalar
checker separately checks the concrete routed addresses.

## Literal-row census and compact storage

Enumerate every valid (S,b) pair once, giving a public dense row number.
Canonical physical cells are exactly row times {0,1}^k. Let R_a(k) denote
their number of rows, excluding bit-of-symbol and other region headers.

    R_a(k) = 1,                                       if k <= 2a;
    R_a(k) = 2^a R_a(floor(k/2)+a)
             + 2^(a-1) (R_a(ceil(k/2))-1),            otherwise.

Derivation: all row-child proofs contribute 2^(k+a) R_a(floor(k/2)+a)
symbols, including each parent symbol once. Each column child has its root
already stored in those row cells; its extra proof contributes
2^(k+a-1)(R_a(ceil(k/2))-1). Divide by the 2^k original seed coordinates.
This counts physical storage, not occurrences or recursion-node labels.

With maximum depth h, induction gives R_a(k) <= (3*2^(a-1))^h. For fixed
a and h=O(log k), this is polynomial in k. A direct list of (S,b) pairs and
their ranks therefore also has polynomial construction time and size.
Normalizing one explicit address uses polynomial time in its O(k+ah)
bits; no enumeration of all 2^k seeds or all node labels is needed.

Packed storage has Q=2^k * 2^ceil(log2 R_a(k)), with free unused rows if
R_a(k) is not a power of two. For a root alphabet of k bits and internal
alphabet of 2k bits, one tree has k(2R_a(k)-1) raw bit rows. Two constant-rate
trees, fixed region/symbol headers, public seed rows and polynomially many
gate rows retain a polynomial row count under the separately stated source
compiler size bounds. This note does not generate that full Boolean circuit.

## One globally shared later row map

After this public normalization, an arbitrary injective row map
Lambda:[R]->{0,1}^t may be publicly constructed or guessed once, independent
of the verifier seed and every individual occurrence. A new global proof
Pi' decodes the old proof by

    Pi(old_cell) = Pi'(Lambda(row(old_cell)), root_coordinate(old_cell)).

Each actual fixed query now uses (constant Lambda(row), z XOR delta).
Therefore composition with a degree-d GF(2) proof polynomial has degree at
most d, and a signed width-three clause has degree at most 3d. Public seed
pins that clamp one seed coordinate retain their existing degree and
two-to-one-fiber behavior.

An explicit row-map descriptor costs Rt bits, plus polynomial-time
construction/injectivity checks; R is polynomial in k for fixed a. This
cost is entirely different from the growing-a one-level compiler, whose
row count grows like a power of N=2^k. An exponential table of recursion-node
labels is not required: normalized rows pass through many such nodes.

No low-degree completeness claim follows just from cheap maps. The full
Boolean proof, its satisfying witnesses, error sensitivity, soundness and
approximation precision remain separate obligations. Injective reindexing
preserves raw failure counts for every assignment, but changing ambient
padding changes the required uniform-error denominator. The transformed
proof approximation hypothesis must refer to the actual transformed truth
function. Any claim of asymptotic advantage must also compare direct
polynomial descriptions after the finite header variables are eliminated.

## First genuine two-level calculation: k=8, a=3

The down shapes are RR (leaf dimension6), RC (dimension4), and C (dimension4).
The stored canonical shapes are root, R and RR, with respectively 1,7,56
literal rows. Thus there are 64 rows and 16,384 physical symbols.

The old padded shape/payload cube has 2^18=262,144 symbol addresses. The
dense row packing has exactly 2^14=16,384 symbols. With 8-bit root symbols
and 16-bit internal symbols there are 1,016 raw bit rows, padded to1,024;
the raw bit cube consequently has 262,144 bits. These are geometry/storage
counts, not a Boolean gate or clause census.

The exhaustive check enumerates every distinct tape and every offset:

| Down shape | Unique tapes | Leaf slots | Occurrences |
|---|---:|---:|---:|
| RR | 64 | 64 | 4,096 |
| RC | 32 | 16 | 512 |
| C | 4 | 16 | 64 |

All4,672 occurrences and all256 seeds are checked, giving1,196,032 direct
query comparisons. Every normalized row is fixed across its seed, and its
low coordinate is exactly seed XOR a fixed delta. Every physical symbol is
reached. An additional16,384 direct C/sibling-R alias checks agree. All
16,384 physical addresses satisfy both inverse laws without collisions.

For example, RR with tape0 and offset8 has normalized row8 and delta0;
offsets9 through15 use the same row and deltas1 through7. Two distinct
R-extension cells at auxiliary chunks1 and2 with root-coordinate0 remain
distinct; dropping their auxiliary tag would merge them.

Symbolic controls cover (k,a)=(7,3),(8,3),(10,3),(15,3),(21,3),(17,4),(33,3).
These controls include internal column ancestry and compare shape-counting
against the separate physical-subtree recurrence. They supplement the
coordinate induction; they do not turn a finite scan into a general theorem.

## Actual field/residual transport

`check_recursive_field_bridge.py` links the normalized coordinates to the
different dense integer indexing in Expedition041. It constructs a bijection
of all16,384 physical symbols and checks all parent/row aliases. Old outer
cells retain their indices; inner extension cells are regrouped across node
labels into literal rows.

Every leaf receives precisely its original ordered list of field symbols,
and its field abscissas/cutoff are unchanged. The actual root used by the
residual is still the same root used by the proximity test. Therefore the
field predicate is identical on every global proof under this bijection.
The finite replay checks the existing honest YES, degree31 NO extremizer,
and NO extremizer with a changed root symbol at48. The actual field
implementation is reused, and the previous all-assignment field rejection
argument is not advertised as newly proved here. No Boolean denominator or
signed bit-error sensitivity is inferred from field-level acceptance counts.

The field bridge also computes exact ANFs of the1,016 normalized raw B bit
rows and the8 raw A rows of each named proof. Low span or degree on one known
reference must not be mistaken for a public symbolic dictionary uniform over
unknown satisfying witnesses or for the full compiler's auxiliary gate rows.

The measured B rows are:

| Actual field fixture | Seed-degree histogram | Distinct ANF vectors | GF(2) row-span dimension |
|---|---|---:|---:|
| Honest YES B=X | 536 zero;192 nonzero constant;288 degree1 | 10 | 9 |
| Degree31 NO extremizer | 504 degree4;512 degree5 | 1,016 | 177 |
| Same NO with root48 toggled | 504 degree4;511 degree5;1 degree8 | 1,016 | 178 |

The YES A=1+X has eight degree-one bit rows, of span dimension eight.
Both NO A words are zero. All three fixtures preserve their original
residual and paired-RS verdicts: YES accepts256 seeds, both NO fixtures
accept35 and reject221; the changed-root NO has paired-RS acceptance240.
The bridge compares76,800 ordered field values and2,496 actual leaf verdicts
across the three fixtures, along with the18,432 physical names including
aliases. These values are exact finite observations, not a guessed
asymptotic law for compiler gate rows.
