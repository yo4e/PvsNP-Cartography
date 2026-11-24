# Scoped obstruction: fixed layouts for satisfying Reed–Solomon witnesses

Status: written derivation with exact finite controls; not a new Lean result,
external mathematical review, or novelty claim. The authoring and attacking
agents share model lineage and project context. This is a bounded adversarial
pass, not the independent review requested by Issues 8 or 15.

## 1. The quantifiers that a public compiler needs

Let `C(x)` be a compiler computed from public instance `x`, including an
injective physical row layout and all signed projection queries. It must be
chosen before, and without access to, an unknown satisfying witness. At a
minimum, a completeness route would need

    for every YES x, there exist a satisfying w and a degree-d polynomial P
    whose error against Enc_{C(x)}(w) is below the stated threshold.

`P` may depend on `w`. Asking that the same polynomial work for every witness
would be an unnecessary extra restriction. However, the stronger assertion

    for every YES x and every satisfying w, such a polynomial P exists

is also not needed by existential completeness. A counting obstruction to
this stronger assertion must not silently be reported as an obstruction to
the first statement. Allowing the compiler/layout itself to depend on `w`
is a different quantifier change: the coefficient signatures in Expedition
046 are computed after the named reference is known.

## 2. The original designed YES fixture has one used proof

Use the notation of Expedition 046, `s=2^a`, `k=2a+1`, `N=2s^2`, `a>=3`.
Suppose every physical clause is satisfied. The constant and public pins are
correct, every private gate and copy has its intended value, and all field
tests accept. Full cross acceptance forces an affine root
`A(X)=alpha+beta X`. The shared row/column argument gives a single root
polynomial `B_*(X)` of degree at most `2s-1`, with the actual root table as its
values.

In the YES residual in `046-growing-cross/check.js`, evaluation at `X=1`
has just the nonzero selector times `A(1)^3`, so `A(1)=0`. At `X=0`, the
remaining expression is the nonzero selector times

    (A(0)+1)^2 (A(1)+1).

Thus `A(0)=1`, and `A(X)=1+X` is forced. Substitution into the residual gives

    Z_{0,1,2,3}(X) (B_*(X)+X).

Consequently `B_*(X)=X` at all `N-4` points outside `{0,1,2,3}`.
Since `N-4>2s-1`, the polynomial root bound forces `B_*(X)=X` everywhere.
Every complete row is uniquely determined by its `s` parent samples,
so every nonroot B page is forced as well. The Boolean gates and copies then
force all remaining used rows. Padding is unconstrained.

Therefore an incompatible pair of satisfying witnesses cannot be obtained
inside this exact fixture. The known-reference layout is computable there
because public syntax already determines the unique used witness. This says
nothing about an unknown-witness source problem. It also explains why simply
replaying the existing YES fixture cannot demonstrate uniform completeness
over a nontrivial witness family.

## 3. A code-only relation with genuinely satisfying variable witnesses

Define an explicit relaxation: keep the physically shared A-star tests,
B-row tests, B-column tests, constant and public pins, and the ordinary
Boolean gate/copy definitions, but remove the *outer residual acceptance
assertion*. At the circuit level this means asserting a new final conjunction
of the code-test bits only; the old final conjunction containing the residual
must no longer be asserted. One can retain the residual gates and old
conjunction as unused, correctly evaluated private rows; they impose no
further restriction on the roots. This is a specified changed verifier, not
deletion of an independent unit clause that happens to exist in the old
compiler. No old exact gate census or NO soundness bound is inherited.

Fix `A(X)=1+X`. For every `B(X)` over `F=GF(2^k)` with `deg B<2s`, divide

    B(X)=R(X)+q(X) S(X),   deg R,deg S<s,
    q(X)=product_{u in U}(X+u).

For row index `v`, write `y_v=q(sv)` and fill its physical page cells at their
actual abscissae with

    Q_v(T)=R(T)+y_v S(T).

Each row is a genuine degree-`<s` polynomial. At a common column abscissa `T`,
the values are affine in `y_v`. At the root cell `z=sv+u`,
`q(z)=q(sv)=y_v`, so `Q_v(z)=B(z)`. These are the same shared cells in both
checks, not detached copies. Every such root therefore extends to a satisfying
code-only proof, with private rows obtained by actual gate evaluation.

At any `2s` distinct root points, the evaluation map from degree-`<2s`
polynomials is bijective: Lagrange interpolation supplies existence and the
root bound supplies uniqueness. Reading the `k` coordinate bits at those
points gives

    R0=2sk

systematic physical bits ranging independently over *all* `2^R0` patterns
among genuinely satisfying code-only witnesses. This is not the unrestricted
constant-row assumption in Expedition 046's original counting attack.

## 4. Arbitrary fixed-layout counting obstruction

Fix any witness-independent injective layout into an `m`-bit address cube.
Restrict each degree-`<=d` GF(2) polynomial to the `R0` systematic addresses
from Section 3. There are at most

    2^D restrictions,   D=sum_{j=0}^{min(d,m)} binom(m,j),

because this is the total number of multilinear polynomials before
restriction. Distinct polynomials may give the same restriction, which only
makes the upper bound smaller. The union of Hamming balls of radius `e`
around all restrictions has cardinality at most

    2^D V(R0,e),   V(R0,e)=sum_{j=0}^{min(e,R0)} binom(R0,j).

If this is less than `2^R0`, at least one *satisfying code-only witness* is
more than `e` errors away from every such polynomial already on the used
systematic cells. Adding private rows or choosing arbitrary unused padding
cannot repair these errors. For this fixed witness every polynomial has at
least `e+1` errors, so a fixed probability mixture has expected errors at
least `e+1` too.

For polynomial-in-`N` storage, `m=O(k)`. For `d=O(log k)`,
`D=2^{O((log k)^2)}=o(sk)`. If `e=O(s)`, then eventually `e<R0/2` and

    log2 V(R0,e)=O(e log2(R0/e))=O(s log k)=o(sk).

For `e=0`, the ball term is zero in the logarithm. Thus for all sufficiently
large `a` the covering bound is strictly below `2^R0`. This is a written
asymptotic deduction for the specified family, not a finite-data fit.

**Disposition.** Shared RS code-check structure alone cannot give an
`O(log k)` degree guarantee at `O(s)` absolute errors for *every* satisfying
witness under a public polynomial-storage layout. This is a scoped dead
direction. The existential completeness target survives: for example the
zero B root is still an available satisfying witness in this relaxation.
No hard language was encoded, and removing the residual discarded the
original NO gap. The obstruction neither refutes all possible proof layouts
for NP nor separates complexity classes.

## 5. Exact finite controls

Run `python3 check_scoped_rs.py`; its deterministic output is `scoped-rs-results.json`.
Normal and `python3 -O` outputs were compared byte for byte. The checker does
not import or modify the earlier compiler.

### GF(8) toy

All 4096 degree-`<4` polynomials over `GF(8)` were enumerated. Four distinct
evaluation points give all 4096 systematic patterns (12 bits). With three
coordinate tags and eight root points, the 24 raw cells live in a five-bit
address cube. All 64 affine restrictions were enumerated. Distances to the
nearest affine table have histogram

| Minimum distance | Codewords |
|---|---:|
| 0 | 8 |
| 4 | 168 |
| 6 | 3584 |
| 8 | 336 |

In particular `B(X)=X^3` has exact nearest affine distance 6 on used raw
cells. For an *arbitrary* fixed five-bit layout, the systematic covering
upper bound at radius 1 is `2^6 (1+12)=832<4096`. The latter is an existence
obstruction for every layout; the explicit `X^3` distance concerns the named
coordinate-tag layout. This toy is not an instance of the `a>=3` NO theorem.

### Shared GF(128) geometry (`a=3`)

The checker independently constructs the exact shared row/column geometry
and replays the roots `0`, `X`, `X^3`, plus an interpolated polynomial with
arbitrary prescribed values on the first 16 root points. For each, its
degree-`<8` row certificates match 1024 physical row cells and its affine
column certificates match 512 physical column cells. Root samples agree
with the intended degree-`<16` polynomial.

For `B(X)=X^3`, the first 16 root points in the original contiguous B-bit
tags 7 through 13 supply 112 used cells. On this slice, a polynomial of total
degree at most one on the whole 22-bit original address cube restricts to
one of exactly 512 tables: four varying seed bits, four varying tag bits,
and a constant. All 512 were enumerated. Its exact nearest distance is
**42**; the full distance histogram is in the JSON. This lower bound assumes
no padding values and concerns genuine satisfying code-only roots, though
`X^3` does not satisfy the original outer residual.

Separately, for *any* injective 22-bit layout, `d=1`, and target radius 4,

    2^23 sum_{j=0}^4 binom(112,j) = 54,065,157,373,952
    < 2^112 = 5,192,296,858,534,827,628,530,496,329,220,096.

Radius 4 is a target scale comparable with the earlier compiler; it is not
a new soundness guarantee for the relaxed relation. The arbitrary-layout
bound and the particular-layout `X^3` distance are distinct claims.

## 6. What a salvage condition would have to supply

A valid next target must use structure of the *residual-constrained*
satisfying family, or aim only at existence of one easy satisfying proof.
Neither finite row seed degree nor the fact that all rows belong to a linear
code is sufficient to obtain the stronger all-witness conclusion.

A simple positive algebraic condition illustrates the real cost. Suppose
each affine seed row has coefficients of the form

    c_ij(w)=sum_{ell=1}^r a_ijell phi_ell(w),

where every `a_ijell` is public and `r` is fixed. A public tag can store the
`(k+1)r` coefficients `a_ijell`, together with an injectivity rank. For each
witness the polynomial

    P_w(tag,z)=sum_ell phi_ell(w)
                   (tag_0ell + sum_{j=1}^k tag_jell z_j)

has degree at most two and matches all these affine rows. The layout is
witness-independent while polynomial coefficients depend on the witness.
Storage is exponential in `r(k+1)`, so it is polynomial in `N` only for
bounded `r` in this direct construction. Nonaffine rows and actual verifier
costs still require their own accounting. This is a scoped symbolic-basis
salvage, not a claim that the earlier compiler satisfies that hypothesis or
that a growing unknown witness can be reduced to constant dimension.

## Source map and limitations

- `expeditions/046-growing-cross/check.js`: original residual, physical tag
  order, common-column geometry, and known-reference coefficient layout.
- `expeditions/046-growing-cross/derivation.md`, Sections 1, 2, 4, 5: inherited
  shared B recovery, Boolean compiler semantics, and unrestricted-row attack.
- `graveyard/2026-11-24-witness-independent-row-layout.md`: predecessor failure
  whose arbitrary-row limitation this scoped construction addresses.

The interpolation and polynomial-counting arguments are given explicitly
above. No claim of new mathematics or independent proof-kernel checking is
made. A targeted literature audit remains needed for any novelty statement.
