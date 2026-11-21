# Adversarial review: local code space is not a soundness certificate

Reviewer role: same-model-lineage skeptic/experimentalist, separately tasked
from the research lead and theory/compiler workers. Base checkpoint:
`fa1dabd4f3a760832e78ca398d1ebedf68853ebe`. Read the operating contract and
required background, then Expedition 040's physical verifier/soundness and
Expedition 044's compiler and zero-error obstruction. The basis-derivative
predicate was independently selected by the theory worker and this worker,
then shared before experiments. The lead subsequently supplied the cross
construction and its proposed argument. This is an adversarial internal
review, not blind independent mathematical review, another proof kernel, or
a Lean execution.

## 1. What was attacked

Write `d(x)=A(x)+A(x+1)` over GF(128), represented with modulus `0x83`. For an
offset set D containing 0 and 1, the local membership predicate is

    A(x+delta) = A(x)+delta*d(x)  for every delta in D.

All additions in addresses are XOR. The same external A and B tables are
used at every center, with the original shared B root/row/column extension
cells. The NO arithmetic is unchanged. The initially tempting claim was that
the exact affine zero-error code space suffices to retain the old NO minimum
of 109. It does not.

The standalone [attack script](attack_sparse.py) evaluates the actual NO
residual with a separate shift/reduce GF(128) implementation. B leaves use
the pinned scalar absolute-point interpolation implementation from 040,
not the new Boolean compiler. Honest B auxiliary tables are constructed by
040's `honest_cells`; all sixteen rows and all thirty-two columns are then
checked. There is no detached parent or sibling copy.

## 2. Executed radius-one counterexamples

For D consisting of zero and the seven basis vectors, start with the old
honest sharp B polynomial interpolating 1/x at x=4,...,19. A=0 accepts
exactly seeds 1,...,19.

Set A(y)=100*y on the eight-point Hamming ball of radius one around 96,
and A(y)=0 elsewhere. The nonzero A entries are:

| y | A(y) |
|---:|---:|
| 32 | 43 |
| 64 | 86 |
| 96 | 125 |
| 97 | 25 |
| 98 | 54 |
| 100 | 104 |
| 104 | 87 |
| 112 | 41 |

The sparse verifier now accepts exactly 1,...,19 and 96: **108 NO
rejections**. Every old accepted center is Hamming distance at least three
from 96. Its local star is disjoint from the changed star, so its A and
residual reads remain zero. At 96, all local reads come from the single
affine polynomial 100*X and its residual is zero. Thus the gain is not an
aliasing defect.

Three disjoint local stars, centered at 96,117,122 with respective slopes
100,92,98 and zero constant, retain those nineteen old acceptances and add
all three centers. This gives **106 rejections**. The script records the
complete nonzero A table. A bounded enumeration of subsets of the thirteen
eligible centers found this three-star packing; no global optimum over A,
B, or auxiliary assignments is claimed.

## 3. Executed radius-two counterexample

For D consisting of the 29 offsets of Hamming weight at most two, take

    P = {5,6,7,9,10,11,15,17,18,19,23,27,33,34,35,39},
    U(X) = product_(p in P) (X+p),
    B(X) = (U(X)+U(0))/(X U(0)).

This is a polynomial of degree at most fifteen. Its ascending coefficient
list is

    [55,43,75,65,76,75,115,57,19,48,29,73,27,2,26,95].

Fill the single shared B table honestly. Define A(y)=1+121*y when the
Hamming distance from y to 124 is at most two, and A(y)=0 elsewhere. The
radius-two local predicate accepts thirty centers; the joined NO verifier
accepts exactly `{1,2,3} union P union {124}`, twenty centers. Thus it also
has **108 rejections**, disproving retention of 109 for this larger stencil.
The old nineteen centers are all distance at least five from 124, so their
radius-two stars avoid the patch. The local affine at 124 supplies its new
acceptance. This is an upper witness, not a proof that 108 is the minimum.

The surviving lower bound for radius two is handled in the theory artifact;
this attack does not upgrade it to an equality.

## 4. The cross repair: hostile checks of the proposed proof

The repaired stencil is

    L={0,...,7}, H={0,8,...,120}, D=L union H, |D|=23.

**No issue found in the accepted-site affine argument.** A passing center x
supplies one actual affine polynomial

    P_x(T)=A(x)+(T+x)*d(x)

on every point of x+D. For distinct x,y, put h=x+y=l+k with l in L and k in H.
The points x+l=y+k and x+k=y+l lie in both stars. They are distinct: l=k
would lie in L intersect H={0}, forcing h=0. This covers the cases l=0 or
k=0, as well as the case with both nonzero. Two affine polynomials agreeing
at these two field points are identical. Consequently **every passing
center uses one common affine polynomial**, even when A itself is a noncode
and rejected centers are arbitrarily corrupted. There is no connectedness,
majority, or small-error hypothesis.

The independent finite check enumerated every nonzero difference h. The
intersection-size distribution is 105 differences with two common points,
seven with eight, and fifteen with sixteen. This finite census checks the
GF(128) implementation; the direct-sum argument above supplies the general
two-intersection fact.

**Attempted quantifier objection: P need not describe A at rejected centers.**
That is harmless. The NO residual at a joined accepting center reads A only
at offsets 0,1,2, all of which are in L. Those three actual values equal P
at their corresponding field points. The later residual polynomial is only
required to match the real predicate at accepted centers.

**Attempted B objection: the root can be a noncode.** The old shared-cell
argument still applies. With at most one passing row or at most one wholly
passing column group, at most sixteen centers can accept. Otherwise two
passing rows and two groups determine a common bivariate polynomial on all
passing rows, and hence a degree-at-most-fifteen B* at every possibly
accepting physical root cell. The reasoning needs physical parent and
sibling aliases. It does not assume the whole B table is a codeword.

**Attempted nonzero-polynomial objection: 0 or 1 might reject locally.** The
root bound is nevertheless valid. Substitute the common affine P and B*
into the NO residual. Its degree is at most nineteen. If it were the zero
polynomial, its evaluations at 0 and 1 would respectively force P(0)=1 and
P(0)=0. This contradiction concerns the constructed polynomial, so neither
0 nor 1 needs to be an accepted center. A polynomial over the extension
field can still have at most nineteen distinct roots in the embedded base
field. Thus the written proof retains 109 NO rejections over arbitrary
field assignments. The unchanged A=0 sharp B witness attains 109.

**Compiler boundary.** This field argument does not by itself prove a
Boolean-clause minimum or sensitivity. Those require the separately checked
private gates, fixed query maps, complete public-pin charging, and actual
Q census. This worker supplied its fixtures to the compiler worker for
physical replay and did not treat the field rejection count as that replay.

## 5. Controls against overbroad cross claims

Removing the high 64 direction yields the restricted union
`L union {0,8,...,56}`. The nonaffine table A(x)=indicator(bit6(x)) passes all
128 restricted local membership tests: every allowed shift stays within
one half and d(x)=0. It fails the full cross test at all 128 centers. The
script verifies non-affineness by absolute-point interpolation. This is a
membership counterexample only, not a low-rejection joined NO witness.
The complementary spaces must span the entire physical address space.

In the actual cross schedule, the disjoint-star attack has no room: any two
passing stars share two field points. Distinct local affine pieces cannot
both pass. The explicit candidate witnesses were replayed without altering B:

| Field assignment | Radius one rejections | Radius two rejections | Cross rejections |
|---|---:|---:|---:|
| Old affine sharp witness | 109 | 109 | 109 |
| One radius-one star | 108 | 114 | 119 |
| Three radius-one stars | 106 | 118 | 128 |
| One radius-two star | 108 | 108 | 124 |

All B rows and columns pass in every row of this table. New failures come
from the A check or the unchanged residual, not inconsistent B storage.

## 6. Actual execution and limits

Executed `python attack_sparse.py` and `python -O attack_sparse.py`; outputs
are byte-identical. [Stored JSON](attack-results.json) SHA256:

    b26e7b12b9b33ee8d688afe450e593f86a10ceae4ab7fcd32cccbc441d700408

The script compares all 16,384 base-field products to the pinned arithmetic,
checks every center of every witness, every B row/column, and all 127 nonzero
cross-stencil differences. These are finite computations and a written
algebraic review. No Lean proof, human semantic review, mathematical novelty,
approximation construction, or P-vs-NP separation is asserted. A speculation
that the radius-two optimum might equal 108 was not pursued: the cross
repair dominates the current certificate and is the useful mathematical
decision from this attack pass.
