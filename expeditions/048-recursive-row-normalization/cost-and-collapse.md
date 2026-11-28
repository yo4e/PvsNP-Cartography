# The invariant left after a short row layout

Approved November 28 session. Source checkpoint:
`ba1da266a3e51f4025b7ba4f00d305b94796cbff`.

Status: elementary written derivations and separate finite executable controls.
No Lean execution, independent external review, mathematical novelty, or new
complexity-class separation is claimed. This skeptical pass shared project
context and intermediate findings with the lead and the layout agent.

## 1. Scope and the correction from the growing fixture

The source recursion in Expedition 038 fixes its rate exponent `a`; its depth
is `O(log k)`, unlike the growing one-level fixture in Expedition 046.
Therefore the explicit-table lower bound from that fixture cannot simply be
reused. The constructive question is whether canonical physical addresses
admit one public normalization into rows

    (i,z),  i in [R],  z in {0,1}^k,

with `R=poly(k)`, such that every fixed query has a constant row `i` and a
signed seed projection `rho(z)`. Full-offset queries should have rank `k`;
public pin queries may clamp one bit and have rank `k-1`.

The companion layout work investigates exactly this normalization, including
column-to-row redirection and restoration of parent aliases. Everything
below that invokes the source compiler is **conditional on that single
canonical normalization**, rather than presuming an arbitrary table for
exponentially many recursive node names. The general row lemmas themselves
need only the displayed row universe.

Once such a normalization exists, an explicit `R*t`-bit row-label table with
`t=O(log k)` is polynomial size. The remaining obstacle is not writing that
table. The rows' dependence on the seed remains after every relabelling.

## 2. The row-degree invariant with an error budget

Let `R>=1`, `N=2^k`, and let a fixed physical proof be represented by Boolean
rows `f_i:{0,1}^k -> F2`. All degrees are total multilinear GF(2) degrees;
the zero and constant functions have degree zero for this bookkeeping.
Let `E>=0` be an absolute error budget on used cells.

Define

    Delta_E(f) = min over (G_0,...,G_{R-1}) of max_i deg(G_i),
    subject to sum_i |{z:G_i(z) != f_i(z)}| <= E.

The row polynomials are chosen once and reused. They are not resampled at
different occurrences. The feasible set is nonempty because exact truth
tables always have degree at most `k`. At zero error,

    Delta_0(f)=max_i deg(f_i).

For an injective row labelling `lambda:[R]->{0,1}^t`, let `d_E(f,lambda)` be
the least degree of a global polynomial `P(y,z)` making at most `E` errors
on the **used** cells `(lambda(i),z)`. No padding values are prescribed.
Equivalently, padding may be completed arbitrarily. This is not an error
fraction on the larger ambient cube.

### Restriction lower bound

For every such layout,

    Delta_E(f) <= d_E(f,lambda).

Indeed, from a feasible `P` set `G_i(z)=P(lambda(i),z)`. Fixing tag variables
cannot increase degree, and the sum of row errors is exactly the number of
used-cell errors of `P`. This proof allows the selected layout to depend on
the witness; it does not assume a public layout or universal completeness.

### Public dense upper bound

Let `b=ceil(log2 R)` and let `lambda_dense(i)` be the ordinary `b`-bit
encoding of the public row identity. For each row define its indicator

    I_i(y)=product_j (y_j if bit_j(i)=1 else 1+y_j).

For a tuple attaining `Delta_E(f)`, the explicit polynomial

    F(y,z)=sum_{i=0}^{R-1} I_i(y) G_i(z)

has degree at most `Delta_E(f)+b`, agrees with `G_i` on each used row, and is
zero at unused tags. Thus

    d_E(f,lambda_dense) <= Delta_E(f)+b.

For `R=1`, the empty indicator product is one and the bound has `b=0`.
An upper bound for every arbitrarily sparse labelling is unnecessary here;
the public dense layout is the witness to the upper bound.

### Sandwich and actual scope

Minimizing over all admissible injective tag widths and layouts gives

    Delta_E(f) <= inf_lambda d_E(f,lambda)
               <= d_E(f,lambda_dense)
               <= Delta_E(f)+ceil(log2 R).

In particular, adaptive row tags can save **at most `ceil(log2 R)` degrees**
compared with the public dense row encoding, when both are compared at the
same used-cell error budget. The bound is not an assertion that tags never
help. They can help substantially at small degree, and they can affect
constants and storage. It identifies what they cannot change at leading
order when `R=poly(k)` and the relevant degree scale is `k/log k`.

The upper bound is attained relative to the row invariant: take all `2^b`
rows, each constant in `z`, with exactly the all-one tag row having value
one. Then `Delta_0=0`, while the public dense function is the product of the
`b` tag bits and has degree `b`.

## 3. The existential satisfying-witness formulation

Let `W(I)` be the nonempty satisfying-proof set of a public YES instance.
Define

    Delta_E^exists(I)=min_{w in W(I)} Delta_E(f_w),
    d_dense,E^exists(I)=min_{w in W(I)} d_E(f_w,lambda_dense),
    d_adapt,E^exists(I)=min_{w in W(I),lambda} d_E(f_w,lambda).

The pointwise bounds above immediately give

    Delta_E^exists(I) <= d_adapt,E^exists(I)
                     <= d_dense,E^exists(I)
                     <= Delta_E^exists(I)+b.

This is the relevant quantifier order. One hard satisfying witness does not
lower-bound `Delta_E^exists`; every possible satisfying witness would have
to fail the target. The old code-only RS obstruction and the unique designed
YES example therefore do not supply such a lower bound for a hard source
language. The theorem also works for any fixed canonical chosen witness,
but choosing a canonical witness and minimizing over all satisfying ones
are distinct operations.

The same argument works with public nonnegative weights on the row error
counts. With partially used rows, replace each row's full seed cube in the
error objective by its specified used subset and minimize over seed-row
completions; the restriction/multiplex proofs are unchanged. For the clean
full-row model the exact formula is simply `max_i deg(f_i)`.

## 4. Direct row certificates subsume guessed row tags

There is a stronger algorithmic observation once queries have the normalized
fixed-row form. A nondeterministic simulator can guess one degree-`d`
polynomial `G_i` for each of the `R` rows, and decode one global old proof

    pi(i,z)=G_i(z).

All occurrences of a canonical physical cell use that same value. Every
NO-soundness theorem quantifying over all global old proofs therefore still
applies to every branch. No injection test or label map is needed for this
simulator.

Every certificate consisting of an injective guessed row map `lambda` and
a degree-`d` polynomial `P` yields such a tuple by restriction. Thus guessed
row tags add **no accepting power** over the direct row-polynomial certificate
class at the same seed degree. Conversely, a row tuple can be represented
as one public dense proof polynomial with the additive `b` overhead above.

Because each query fixes the row and composes only signed projections of
the seed, a literal `G_i(rho(z))` has degree at most `d`, and a width-three
clause has degree at most `3d`. The additive `b` is not needed in the
actual clause-counting call. It is needed only if one insists on representing
the entire proof by a single polynomial before fixing the queried tag.

The descriptor has

    R B(k,d) bits,   B(k,d)=sum_{j<=min(d,k)} binom(k,j).

For `R=poly(k)` and `d=O(k/log k)` this is `2^{o(k)}`. Signed substitution,
clause construction and parity cancellation have the same subexponential
bounds as Expedition 039, multiplied by polynomially many rows/templates.
The inherited polynomial counter uses degree `D<=3d` and runs in

    2^{k-Omega(k/(3d))+O(log k)}.

Constant polynomials (`d=0`) are evaluated directly. For positive degree,
with `k=n+O(log n)` and polynomially many calls, a sufficiently small fixed
coefficient in `d=alpha n/log n` pays the polynomial overhead and the chosen
hierarchy clock just as in the existing ledger. This is a conditional reuse
of that ledger, not a new unconditional counting algorithm or separation.

Do not confuse these independently **chosen deterministic rows** with
independent random samples per occurrence. The first choice always decodes
one shared proof; the second can detach two queries to the same cell.

## 5. Error precision and alias consistency still have to be paid

Suppose literal occurrence `ell` reads row `i_ell` through `rho_ell`, and
`nu_ell` bounds the largest seed fiber of this projection. For offsets
`nu_ell=1`; for a single clamped bit it is at most two. If a satisfying proof
has row errors `e_i`, the sum of failed clause–seed pairs after replacing it
by a row-polynomial tuple is at most

    sum_ell nu_ell e_{i_ell} = sum_i omega_i e_i,
    omega_i=sum_{ell:i_ell=i} nu_ell.

This is the ordinary literal union bound. It need not be the optimal signed
sensitivity, and repeated occurrences are deliberately counted. If the
source verifier's established raw NO lower bound is `gamma*2^k`, then

    sum_i omega_i e_i < gamma*2^k

is a sufficient completeness budget. It uses the fixed-rate compiler's own
gap and templates; it does not import the `109/23`, radius-four, or other
numbers from Expedition 046. The source implementation must still justify
its `gamma`, templates, physical aliases and normalization.

Injective relabelling preserves raw errors and the physical meaning of the
clause constraints. It does **not** preserve error fractions when it enlarges
the ambient address cube. If the old and new cubes have sizes `Q0,Q1`, a
uniform new-cube error bound `eta` implies only `eta*Q1` errors on queried
cells. Transport to the compact old cube can therefore cost `Q1/Q0` in
uniform fraction. At `t=O(log k)` this may be polynomial; a constant-factor
growth of the total `Theta(k)` address width can create exponential loss.

For a general recoding `Phi` and an old query `rho`, define

    lambda_rho=max_y |{z:Phi(rho(z))=y}|.

If a polynomial errs on an `eta` fraction of the new `2^m` cube, the query's
error probability is at most `lambda_rho * 2^{m-k} eta`, capped at one.
Bijections preserve the old query fibers; arbitrary small circuits need not.

The same globally fixed forward map suffices for NO soundness even if it
has collisions: `pi(x)=P(Phi(x))` is still a global old proof. An inverse is
needed for arbitrary-witness transport and exact preservation of the error
metric, not for this soundness argument. Occurrence-dependent maps are
different: they need not decode any one old proof.

## 6. Broader succinct recodings: a small circuit is not a low-degree map

Let one global recoding `Phi:{0,1}^{m0}->{0,1}^m` have coordinate degree at
most `q`, and let the guessed polynomial have degree `d`. Then

    deg(P o Phi) <= qd,

and original signed projection clauses have degree at most `3qd`. The
generic degree counter pays this product. With the existing fixed polynomial
overheads, the displayed sufficient hierarchy budget becomes

    qd <= alpha n/log n

for a suitable fixed small `alpha`. If `d` itself is a fixed positive
constant times `n/log n`, an unbounded `q` cannot be absorbed just by
choosing that constant once. This means the generic *upper bound no longer
establishes* the required speedup; it is not a lower bound on every possible
counting algorithm for the factored representation.

For bounded-degree global maps, the decoded proof is already an ordinary
degree-`qd` polynomial, whose direct coefficient description remains
`2^{o(n)}` in the same useful regime. The recoding gives a factorization,
not an enlarged class of decoded low-degree proofs for this generic counter.
Affine bijections are even more restrictive: composing with either direction
preserves degree, uniform error, and the minimum degree at any error budget.
The same correspondence holds when padding is free and both used sets are
transported by the bijection.

Short circuits can have large coordinate degree. For example,

    y0=x0+product_{j=1}^q xj,   yj=xj (j>=1)

is a bijection, is its own inverse, and has a circuit with `O(q)` gates.
The degree-one polynomial `P(y)=y0` pulls back to degree `q`. Disjoint
copies make the factor `qd` sharp: multiply `d` independently sheared output
bits. Hence even a succinct, efficiently invertible, metric-preserving map
does not ensure that the polynomial counter sees the new polynomial's degree.

Fixed header charts give a separate additive bound. If there are `2^b`
public charts, `b=O(log k)`, and the decoded function on each whole chart is
a degree-`D` polynomial in its payload variables, their indicator
multiplexing gives one degree-`D+b` polynomial. A polynomial number of
`B(payload_width,D)` coefficients suffices. More precisely, suppose each
canonical transverse row is an axis-aligned `k`-dimensional subcube in the
old `m0=k+O(log k)`-bit address cube. Its indicator `chi_i` fixes the other
`m0-k` bits, including old zero-padding bits. Suppose the recovered root
coordinates `root_i` are a permutation of the free payload coordinates.
Then

    F_old(a)=sum_i chi_i(a) P(lambda(i),root_i(a))

has degree at most `d+m0-k`, agrees on every used cell, and is zero outside
the canonical rows. This is the relevant collapse when the companion
normalization establishes those subcube and alias assumptions. It avoids
the much looser multiplicative composition estimate for this special map.

If low-degree composition is known only on separate query images, rather
than entire canonical charts, do not assert this multiplexing result without
a coverage argument. A direct occurrence representation must in general
keep or verify consistency on every physical overlap, as in Expedition 039.

For the source query types there is a particularly useful conditional
coverage lemma. Suppose a globally fixed recoding and polynomial give a
degree-`D` value on every actual query. If a normalized row is read by one
full-rank signed-permutation map `rho:{0,1}^k->{0,1}^k`, its whole native
row is `H(rho^{-1}(z))`, where `H` is that composed query polynomial. Its
degree is at most `D`. If a row is covered only by the two complementary
clamps of bit `j`, let their composed functions be `H0,H1`. They reconstruct
the row as

    G(z)=(1+z_j)H0(z)+z_j H1(z),

of degree at most `D+1`. The same globally fixed decoded proof guarantees
the necessary consistency; no independent sample or independent map is
introduced. Unqueried rows are irrelevant to soundness and may be zero.

Thus, under full-rank or complementary-clamp coverage, even globally
high-degree recodings whose actual query values are low degree are subsumed
by direct shared row polynomials, with at most one additional degree.

For the companion canonical normalization there is a written coverage
construction. A physical raw row is either the root or a canonical shape
`S` ending at a nonparent row-extension region, together with its fixed
auxiliary chunks. Follow the down path `S`, selecting those same fresh
chunks. From there choose only row descents until a leaf, with all new
fresh chunks zero, and query leaf offset zero. On climbing, every added
row edge returns. At the final row edge of `S`, its nonzero canonical fresh
chunk makes the query stop at precisely that extension row. The empty-root
case returns through every edge. The retained labels, including column
ancestry, recover the complete original root seed `z`. Hence this one
fixed-tape query addresses `(row,z)` for every `z`; each stored symbol bit
is included by the enumeration. This uses the stated canonical normalization
and enumeration of all paths, fresh tapes and leaf offsets, not merely the
finite `k=8` scan. Every private gate row has its identity query in its
definition clauses, and pin-only rows have the two complementary clamps.

A single partial query image, or arbitrary unrelated low-degree functions
on occurrences, does not establish the lemma in another verifier model.
A stronger counter for structured high-degree query functions would remain
a different possibility.

## 7. Probability mixtures

The row sandwich compares deterministic polynomial minima under a total
raw-error bound. If a fixed distribution over degree-`d` global polynomials
has expected total used-cell error at most `E`, some component has at most
`E` errors, because the total errors are integers. Consequently randomizing
does not enlarge this existential feasibility class. One may also restrict
or multiplex each component using one jointly shared random draw; the
degree bounds and expected-error transports then apply componentwise.

This is **not** an equivalence with pointwise probabilistic approximation,
which constrains each input's error probability separately. One valid joint distribution is the product coupling: sample one polynomial
for each disjoint row once, then reuse those sampled rows at every occurrence.
Independent resampling at each query is a different, invalid interpretation. Only the mean total-error
criterion used in the simulator's existence argument is being collapsed.

## 8. Exact finite controls and their meaning

`check_row_sandwich.py` is independent of the existing experiment generators.
Normal Python and `python3 -O` outputs were compared byte for byte.

1. **Complete tiny sandwich.** For two rows and two seed bits, it enumerates
   all 256 truth functions and all nine raw-error budgets, giving 2,304
   table/budget pairs. The exact row optimum and dense-layout optimum satisfy
   the sandwich in every pair. Three sparse two-row injections give the same
   punctured polynomial spaces. The maximum observed additive gap is one,
   equal to the one-bit header bound.
2. **Adaptive tags help, within the bound.** Sixteen constant seed rows have
   `Delta_0=0`. The all-one-row indicator has dense degree four, while an
   injective value/rank map yields exact degree one with an 80-bit label
   table. Four direct disjoint odd-parity cubes prove that every native
   degree-three polynomial has at least four errors on used cells; the zero
   polynomial attains four. This does not depend on padding.
3. **Composition product is real.** Two disjoint quadratic reversible shears
   on six address bits map a degree-two polynomial to exact degree four.
   All 64 points check bijectivity and the involutive inverse. This is a
   small instance of the written `qd` construction.
4. **Injectivity does not remove precision loss.** Embed a two-bit address
   cube into a codimension-three slice of a five-bit cube. The degree-three
   slice indicator has uniform error `4/32=1/8` against the zero function,
   but error one on every used query. The eightfold loss is exactly the
   ambient size ratio despite injectivity.
5. **Complementary clamp coverage costs a degree.** A three-bit row
   `x0*x1*x2` restricts to degrees zero and two on the `x0=0` and `x0=1`
   query halves. The displayed gluing formula reconstructs exact degree
   three. This checks the possible one-degree cost and why one half alone
   would not justify a whole-row claim.

None of these finite controls proves the general source normalization or
the external hierarchy/counting theorems. They test the stated algebraic
and metric claims and preserve explicit counterexamples to tempting shortcuts.

## 9. Conditional obstruction on the actual hard unary family

The following consequence sharpens the direction decision. Its hypotheses
are the fixed-rate source compiler and the external hierarchy/counting
results already used in Expedition 039. It does not assert that a complete
implementation or independent proof of that compiler has now been supplied.

Fix the one unary language `L` chosen there, in `NTIME(2^n)` but outside its
specified `2^n/n`-scale constructible clock. Assume that, on `1^n`, the
compiler provides the following templates, rows and maps in polynomial time in `n`:

- `R_n,M_n=poly(k)` canonical rows and fixed clauses, with
  `n<=k<=n+O(log n)`;
- the single shared row normalization above, with signed projection queries;
- perfect YES completeness and a raw NO failure lower bound
  `gamma_n * N`, where `N=2^k`;
- a positive, polynomial-bit, polynomial-time computable rational
  `gamma_n>=k^{-C}` for some fixed `C`, or such a constructible minorant of
  the soundness bound valid at all sufficiently large lengths.

Choose a sufficiently small fixed positive dyadic `alpha`, and a constructible
degree budget `d_n=floor(alpha*n/ceil(log2(n+2)))`. All fixed polynomial
overheads, including guessing `R_n` polynomial coefficient lists, are paid
by the counting ledger in Section 4. The exact choice of a numerical alpha
is not exported from an unspecified constant in the external theorem.

Suppose, towards contradiction, that all but finitely many YES lengths admit
some satisfying physical proof `pi` and some single tuple of seed-row
polynomials `G_i` of degree at most `d_n` with

    sum_i omega_i dist(pi_i,G_i) < gamma_n * N / 2.

No uniform method for selecting `pi` is assumed. The nondeterministic
simulator guesses **only** the tuple `G_i`, counts the exact raw failure total
of the resulting global old proof, and accepts precisely when that total
is less than the computable rational threshold `gamma_n*N/2`.

Every NO branch rejects, because its global proof has failure total at least
`gamma_n*N`. On every YES length with the displayed approximation, the
literal-error bound supplies an accepting branch. The finitely many YES
exceptions can be hardwired, along with small lengths; nonunary strings are
rejected directly. This would decide `L` in the forbidden clock, contrary
to the choice of `L`.

Consequently, under the stated compiler and external-theorem hypotheses,
there are **infinitely many occupied YES lengths** for which

    for every satisfying pi, and every tuple (G_i) with deg(G_i)<=d_n,
    sum_i omega_i dist(pi_i,G_i) >= gamma_n * N / 2.

This is the negation of existential completeness below the clock, not an
all-witness hypothesis silently inserted into its premise. It supplies no
explicit hard input or explicit offending row, and it does not imply an
almost-everywhere statement. It concerns the fixed hard unary family, not
every language, every PCP, or P versus NP. It is a written conditional
consequence of the existing method; no novelty promotion is made.

By restriction, every guessed-row-layout certificate below this weighted
error threshold also fails at these lengths. Fixed probability mixtures
with expected weighted total error strictly less than `gamma_n*N/2` would supply a good
component, so they do not evade this particular existential obstruction.
The pointwise approximation distinctions in Section 7 still apply.

## 10. Research decision

After a valid polynomial-row normalization, explicit row-label guessing is
feasible but mathematically secondary for the current asymptotic target.
It can be removed altogether from the nondeterministic certificate in favor
of a polynomial list of shared seed-row polynomials. Adaptive tags cannot
remove `Delta_E^exists`, and the dense public representation loses only
`O(log k)` in global degree.

The next substantive question is therefore about the **residual-constrained
satisfying seed-row functions**. One should identify which seed dependence
or approximation threshold causes failure, or prove a useful restricted
positive statement without demanding universal completeness below the
forbidden clock. Conditional on the source compiler, Section 9 shows that
some residual-constrained hard instances must defeat every satisfying
witness at that threshold; continuing to seek a universal layout that
removes this failure would chase a contradiction. A different globally
succinct recoding would need an explicitly stronger counting mechanism or a
useful query-image consistency interface, not just a low-degree polynomial
after renaming addresses.

This does not rule out constant-factor improvements, small-degree uses,
different time bounds, different approximation models, or stronger algorithms
for structured circuits. It settles which quantity the current approach
must confront rather than decorating the same seed dependence with tags.

## 11. Source dependencies

- `expeditions/038-recursive-query-fibers/source-compiler.md`: fixed-rate
  recursion, canonical physical sharing, source maps and rank bounds.
- `expeditions/039-unary-overlap-counting/budget.md`: unary hierarchy clock,
  coefficient/construction charges, polynomial counting and source caveats.
- `expeditions/047-witness-layouts/sources-and-quantifiers.md`: completeness
  quantifiers, global guessed-map soundness, and why the growing explicit
  node-table cost was scoped.
- Viola, *New lower bounds for probabilistic degree and AC0 with parity
  gates*, ECCC TR20-015 revision 5, Theorem 12 and Section 2.3:
  <https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/>.
  The source counter is for explicitly given GF(2) polynomials. It does not
  supply a generic small-circuit-recoding counter of the same strength.

The source-reading agent rechecked that primary statement during this
session. The row sandwich, multiplexing, degree composition and metric
calculations are supplied explicitly above, without claiming novelty.
