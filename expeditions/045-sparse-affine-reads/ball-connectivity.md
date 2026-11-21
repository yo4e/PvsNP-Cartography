# Sparse affine stars: recovery where the verifier accepts

**Intermediate route.** These ball predicates and connectivity certificates
are retained as research evidence. The [difference-cover cross](theory-notes.md)
is the stronger final construction: it uses fewer A offsets than radius 2,
glues every pair of passing stars without a deletion bound, and retains the
exact original NO minimum.

**Scope.** This is a written finite derivation for the existing GF(128)
one-level NO fixture, with a changed A predicate and the unchanged, physically
shared B root/extension. It proves all-assignment field rejection bounds from
explicit finite graph certificates. It is not a Lean/kernel result or a claim
of mathematical novelty. Parent checkpoint: `fa1dabd4f3a760832e78ca398d1ebedf68853ebe`.

## 1. Predicates and physical reads

Keep the polynomial-basis model `F = GF(2^7)` with modulus `0x83`, one physical
F-symbol `A(x)` at each binary address `x`, and the original outer NO residual.
Addition of field elements is XOR of their seven coordinate bits. For
`r in {1,2,3}`, let

    D_r = {d in F : binary Hamming weight(d) <= r}.

At center x, require for every `d in D_r \ {0,1}`

    A(x+d) + A(x) = d (A(x+1) + A(x)).                 (A_r)

The two omitted equations are identities. No new shared slope oracle is
introduced. The slope on the right is computed from the same physical A
cells; any Boolean computation rows belong privately to their center. Every
read is the fixed XOR map `x -> x+d` on the original A page. The outer
residual reads offsets `0,1,2`, already in every `D_r`.

| Radius r | Distinct A offsets | Equations per center | Agreement graph |
|---:|---:|---:|---|
| 1 | 8 | 6 | Hamming distance 1 or 2 |
| 2 | 29 | 27 | Hamming distance 1 through 4 |
| 3 | 64 | 62 | Hamming distance 1 through 6 |

The query counts in this table refer to distinct physical symbol maps. Gate,
copy, pin and padding costs are separate and must be measured by the actual
compiler. They are not inferred from this table.

For a passing center define the genuine affine field polynomial

    P_x(T) = A(x) + (T+x)(A(x+1)+A(x)).

Condition `(A_r)` says precisely that `P_x` agrees with the physical word
on every site of the translated star `x+D_r`.

## 2. Exact code space and local gluing

Every affine A word passes every test. Conversely, if all centers pass,
adjacent centers have two common star sites. Their polynomials agree at
those two distinct F-points, so they are the same degree-at-most-one
polynomial. The ordinary seven-cube is connected, yielding one affine
polynomial on all centers. Thus the exact zero-error space is the original
F-affine code, rather than the larger class of arbitrary binary-additive maps.

More generally, let x and y be passing centers and put `h=x+y`. If the
Hamming weight of h is between 1 and `2r`, choose u consisting of
`floor(weight(h)/2)` of the nonzero coordinates of h. Both u and `u+h`
have weight at most r. The distinct sites `x+u` and `x+u+h` therefore lie
in both `x+D_r` and `y+D_r`. They force `P_x=P_y`.

If `weight(h)>2r`, the two stars are disjoint by the Hamming triangle
inequality. Consequently the graph whose edges are star intersections in
at least two points is exactly the `2r`-th power of the seven-cube.

For an arbitrary noncode A, every connected component of passing centers in
this graph carries a single affine polynomial. Crucially that polynomial
agrees on the *entire star* of each passing center, including the outer
offsets 0, 1 and 2. The conclusion does not require A to be affine at rejected
centers and does not silently replace A everywhere.

## 3. Finite connectivity certificate, with its strict endpoint

[The saved certificate](connectivity-paths.json) contains internally
vertex-disjoint paths between 0 and the canonical point `(1<<d)-1` at each
nonadjacent Hamming distance d. The path counts are

    kappa_1 = 7 + 21 = 28,
    kappa_2 = 7 + 21 + 35 + 35 = 98,
    kappa_3 = 127 - 1 = 126.

Translation and permutation of the seven coordinates are graph automorphisms.
They carry any two distinct nonadjacent points to one canonical pair.
Adjacent endpoints already have their direct edge. For nonadjacent endpoints,
deleting at most `kappa_r-1` other vertices destroys at most that many of the
internally disjoint paths, so at least one remains. The surviving graph is
therefore connected after strictly fewer than `kappa_r` deletions.

Deleting all neighbors of 0 is an attaining cut: it has size `kappa_r`,
leaves 0 and the point 127, and isolates 0. Thus the certified vertex
connectivities are exact. This upper cut is a graph boundary example, not
an attaining NO-verifier assignment.

[The checker](check_connectivity.py) verifies every path's endpoints,
vertex range, simplicity, Hamming adjacency and disjoint interior directly.
It then transforms and rechecks all 8,128 unordered pairs for each of the
three graphs. It also checks the star-overlap relation for every nonzero
translation. Its normal acceptance path does not invoke max flow. The
optional deterministic integral-flow generator is only a way to discover
the explicit paths. Four invalid certificates are rejected: one missing
path, a repeated interior, a nonedge and a wrong endpoint.

Normal and `python -O` runs produced byte-identical
[saved output](connectivity-checks.json). The direct certificate check is
finite computation; the path/deletion implication above is its written
mathematical interpretation. No independent proof kernel is involved.

In particular, if fewer than `kappa_r` A centers fail, **all passing centers
share one affine polynomial P**, with agreement at all of their outer reads.
The strict inequality matters: connectivity at exactly `kappa_r` deletions
is false.

## 4. Coupling to the actual shared B oracle

Retain precisely the original B predicate: one complete 64-symbol row and
the selected group of four complete 16-symbol columns at each center, with
the genuine parent/sibling aliases. The following is the recovery step of
[Expedition 040's soundness derivation](../040-recursive-verifier/soundness.md),
not a new assumption that arbitrary B words are codewords.

Let R_B be the number of passing rows and C_B the number of passing
four-column groups. There are at most `R_B C_B` B-passing centers. If at
least 20 joint centers accept, then `R_B>=2` and `C_B>=2`: otherwise there
are at most 16 such centers. Choose two passing row polynomials and
interpolate them in the true ordinate Y. The at least eight common passing
column abscissae force this same bivariate polynomial on every passing row.
Composition with the degree-eight subspace vanisher gives one polynomial
`B_*` over the ambient extension field of degree at most 15, agreeing with
the actual B value at every B-passing center. B may differ elsewhere.

The physical shared cells are indispensable. Detached parent or sibling
storage would invalidate the preceding statement, exactly as the existing
Expedition 040 counterexamples demonstrate.

Now suppose a fixed global NO field proof has rho rejecting joint centers
and

    rho < min(kappa_r, 109).                          (1)

At most rho A centers fail. By Section 3, every A-passing center carries
the same P, which agrees with A at all three outer offsets. There are at
least 20 joint acceptances, so the single `B_*` above applies to all of them.
At every accepted center, the actual outer residual therefore equals the
same polynomial

    H(X) = Z_{1,2,3}(X) (P(X)+1)^3
         + Z_{0,2,3}(X) P(X+1)^3
         + X(X+1) P(X+2)(P(X+2)+1)
         + Z_{0,1,2,3}(X) B_*(X).

This polynomial has degree at most 19. It cannot be the zero polynomial:
at X=0 its vanishing forces P(0)=1, while at X=1 its vanishing forces
P(0)=0. The relevant singleton selector is 6, a nonzero field element,
and the other terms vanish at those points. This argument remains valid
over the ambient extension containing `B_*`.

A nonzero polynomial of degree at most 19 has at most 19 distinct roots.
Every joint accepting seed is one of them, contradicting (1). Therefore,
for **every** global field assignment, including arbitrary noncode A and
B roots and all shared extension assignments,

    rho >= min(kappa_r,109).

| Radius | Certified NO rejection lower bound | Known attained upper bound |
|---:|---:|---:|
| 1 | 28 | at most 106, attained by the three-star attack |
| 2 | 98 | at most 108, attained by the customized one-star attack |
| 3 | 109 | 109 |

The radius 1 and 2 upper bounds use the explicit noncode-A witnesses in
[attack-results.json](attack-results.json), with honest shared B extensions.
They disprove retaining 109 automatically. Radius 3's upper bound 109 uses
the existing A=0 reciprocal-interpolant B witness, which passes every
affine-star test. Thus radius 3 has an exact field minimum of 109.
For radii 1 and 2, the table does **not** claim sharpness.
The lower bound is a consequence of the algebraic derivation and finite
connectivity certificate, not an exhaustive search of all field assignments.

## 5. Boolean transport and the precision implication

For the new predicate, use only private gate/copy rows at each seed and
the same two clamped public pin templates per bit. At a field-rejecting
center with correct public bits, either an ordinary local clause fails or
every local definition is true, which forces the rejecting output and hence
a failed final assertion. If a public bit is wrong, its clamped pins produce
two failures per wrong physical bit cell. Distinct centers have distinct
local clause-seed occurrences. Therefore the complete Boolean assignment
has at least as many failed pairs as the field rejection lower bound, even
when all gate, copy, public and constant cells are chosen adversarially.

This is the existing [private-copy argument](../044-bounded-fanout/compiler.md)
with a changed field predicate. It is valid only after the actual compiler
is checked to implement `(A_r)`, retain the physical aliases and preserve
private center ownership. Truthful auxiliaries realize exactly one output
failure per rejected seed; thus field upper witnesses also transfer.

The B component retains maximum reader load 23. Mandatory input buffers
and private fanout at most `f` give

    sigma <= max(|D_r|,23,f+2).

When `f+2` is no larger than the physical maximum, a single physical input
bit at a maximal-load address, with every private buffer/gate held honest,
attains that maximum. This is an unrestricted signed error statement for
all mixed physical error sets, not an assertion about degree-restricted
polynomial error sets.

With appropriate caps, the mathematical candidates are

| Radius | Physical sigma | Certified `V_NO/sigma` lower bound | Strict guaranteed integer error radius |
|---:|---:|---:|---:|
| 1 | 23 | 28/23 | 1 |
| 2 | 29 | 98/29 | 3 |
| 3 | 64 | 109/64 | 1 |

These implications are conditional on the compiled layout and census.
The uniform error threshold is `eta < V_NO/(Q sigma)`, with its **actual**
padded Q. Query-count improvement by itself supplies no Q comparison.
The newly encoded Boolean proof function is a different approximation
target; no old approximating polynomial is transported for free. This
argument also establishes neither a low-degree approximant for the new
function nor a P-vs-NP separation.

## 6. Attacks and surviving boundary

- Exact affine zero-error space alone is inadequate; Section 4 explicitly
  handles noncode A using recovery only at the accepting stars.
- Fewer than `kappa_r` failures is essential. The cut of all neighbors of
  zero disproves any unqualified connectivity claim at the boundary.
- B recovery is invoked only after at least 20 joint acceptances; no
  global-code claim is made for arbitrary B assignments.
- The recovered affine P need not agree with rejected A entries, and the
  recovered `B_*` need not agree at rejected B sites. The residual bound
  uses agreement exactly where acceptance requires it.
- The graph theorem is a finite seven-dimensional statement. A claim for
  a growing source family requires its own quantitative proof and costs.
- Radius 3 can retain the exact gap but lose precision to radius 2 through
  reader sensitivity. Increasing the neighborhood is not monotonic progress.

**Contribution.** The unresolved question changes from whether sparse
affine tests have the correct exact code space to whether their local
agreement graph remains connected after the number of failures that would
be needed to defeat the NO bound. In this fixture, explicit connectivity
certificates give a positive, fully quantified answer and cross the old
zero-integer-error obstruction. Mathematical novelty remains unknown.
