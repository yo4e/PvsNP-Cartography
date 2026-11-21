# A difference-cover affine test retains the full NO gap

**Status and scope.** This is a written derivation for the fully shared
one-level verifier of Expedition 040 with a changed A-membership test.
It covers every assignment to the physical A and B roots and every shared
B extension symbol. The actual GF(128) implementation and census are
separate verification obligations. A symbolic extension is stated only for
the specially designed one-level family already defined in Expedition 040.
This is not a Lean result, a novelty claim, or a lower bound for unrestricted
circuits. Parent checkpoint: `fa1dabd4f3a760832e78ca398d1ebedf68853ebe`.

## 1. The fixed cross of physical offsets

Work in the existing polynomial-basis `F=GF(128)` with modulus `0x83`.
Define two complementary **binary vector subspaces**, not subfields,

    U = {0,1,...,7},
    V = {0,8,16,...,120},
    D = U union V.

There are exactly 23 elements in D. Every field element has a unique
decomposition `h=u+v`, `u in U`, `v in V`, where addition is XOR. Thus
`D+D=F`. The outer offsets 0, 1 and 2 already belong to D.

At public center x, replace the whole-A codeword test by the 21 equations

    A(x+d)+A(x) = d (A(x+1)+A(x)),    d in D \ {0,1}.   (1)

The omitted equations at d=0 and d=1 are identities. Each queried symbol
remains the original physical A cell at `x XOR d`. There is no separate
global slope table or repeated copy of the root. The slope is computed
from the same two physical reads at x and x+1; any Boolean arithmetic
gates and mandatory input buffers remain private to their center.

For a passing center x define

    P_x(T) = A(x)+(T+x)(A(x+1)+A(x)).                  (2)

This is a genuine degree-at-most-one polynomial over F. Equations (1)
mean exactly that it agrees with A on the entire star `x+D`.

## 2. Every pair of passing stars glues, however many centers fail

Let x and y be distinct passing centers, and decompose their nonzero
difference `h=x+y=u+v` in the complementary subspaces. Since h is nonzero,
u and v are distinct. The two distinct sites

    x+u = y+v,       x+v = y+u

belong to both stars. Hence `P_x` and `P_y` agree at two distinct field
points. Their difference is an affine polynomial with two roots, so it
is zero. Therefore **all passing centers share one affine polynomial P**.

This statement holds even when A is an arbitrary noncode word and only
two centers pass. If exactly one passes, choose its polynomial; if none
passes, the joint verifier accepts nowhere. At every passing center,
P agrees at all queried A offsets, in particular 0, 1 and 2. No claim
about A at an unqueried rejected site is needed.

The same argument proves that the exact zero-error space of (1) is the
original F-affine code: affine words pass, and when all centers pass
the recovered P agrees at every site. Unlike a bare binary-linearity
test, this does not admit arbitrary F2-additive maps.

This is the useful strengthening over the initial basis/radius tests.
Those tests required a bound on the number of failed centers to maintain
connectivity of an agreement graph. The difference cover makes that
agreement graph complete. The intermediate results and their explicit
path certificates are preserved in [ball-connectivity.md](ball-connectivity.md).

## 3. Recovery from the unchanged, shared B test

Retain exactly the original GF(128) B predicate and its physical aliases:
at each center, test the complete selected 64-symbol row and four complete
16-symbol columns. Let R be the number of passing rows and C the number
of passing four-column groups. At most RC centers can pass B. If at
least 20 joint centers accept, there must be at least two passing rows
and two passing column groups; otherwise at most 16 centers accept.

Choose two passing row polynomials and interpolate them in their true
distinct ordinates Y. There are at least eight passing common-column
abscissae. The complete passing column tests force the same interpolant
on every passing row at these eight points, and each row has degree
at most seven, so it agrees on its whole row. Substitution of the
degree-eight subspace vanisher yields one ambient-extension-field
polynomial `B_*` of degree at most 15. It agrees with the actual B
root value at every B-passing center. This is precisely the accepted-site
recovery step in [the original proof](../040-recursive-verifier/soundness.md).

Neither arbitrary B roots nor arbitrary extension symbols are assumed
to be codewords. The original physically shared parent and sibling cells
make the interpolation argument valid. Detached storage would break it;
the earlier counterexamples to that change remain applicable.

## 4. Exact 109 rejected seeds over all field assignments

Suppose there are at least 20 joint acceptances for a NO assignment.
Section 2 provides one affine P on all the accepted A stars, and Section 3
provides one degree-at-most-15 `B_*` on all accepted B root sites. At
every accepting seed the actual outer residual therefore agrees with

    H(X) = Z_{1,2,3}(X) (P(X)+1)^3
         + Z_{0,2,3}(X) P(X+1)^3
         + X(X+1) P(X+2)(P(X+2)+1)
         + Z_{0,1,2,3}(X) B_*(X).                    (3)

This single polynomial has degree at most 19. It is nonzero: its value
at zero can vanish only when P(0)=1, while its value at one can vanish
only when P(0)=0. At these two points the relevant singleton selector
equals the nonzero field element 6 and all other relevant terms vanish.
The argument also holds in the ambient extension containing `B_*`.

Every accepted seed is a root of (3), contradicting the assumed 20
acceptances. Thus there are at most 19 acceptances, or at least **109
rejections**, for every global field proof.

The lower bound is attained by the old sharp proof: take A=0 and the
degree-at-most-15 polynomial B interpolating `1/x` at x=4,...,19, with
its honest shared bivariate extension. Every new A test passes because
A is affine. The residual vanishes exactly at 1,...,19. Therefore the
field minimum remains exactly 109. This sharpness is special to the
cross test's universal two-point gluing; preserving the exact zero-error
code space alone would not justify importing the old minimum.

## 5. Boolean compiler and unrestricted error sensitivity

Use the private bounded-fanout construction of
[Expedition 044](../044-bounded-fanout/compiler.md). Put a mandatory private
copy root after each distinct physical input map; preserve all literal
signs and aliases; cap every private driver's outgoing use count at 21;
retain the local constant unit, the output assertion and both clamped
public pin templates per bit.

Each A bit is read at exactly 23 centers, once for each XOR offset in D.
The unchanged B part has maximum physical reader multiplicity 23 at
its common rectangle: eight row offsets plus sixteen column offsets,
with the coincident zero offset counted once. Root and nonrectangle
B cells have smaller loads. Thus the maximal physical load is 23.

The existing local charge inequalities, for arbitrary signed mixed errors,
are `e_a+e_b+2e_c` for AND, `e_a+e_b+e_c` for XOR and `e_a+e_c` for COPY.
The cap 21 bounds every private-cell charge by 23, including its own
definition or public pins. Summing proves `F(E)<=23|E|` over every error
set in the whole padded proof cube. Flipping one raw physical A bit and
holding every private buffer/gate at its honest value violates exactly
one copy clause at each of its 23 reading centers. Hence **sigma=23**.

At each field-rejecting center, correct public bits and all satisfied
local definitions would force the rejecting verdict, hence a failed
output assertion. Wrong public bits already create two failed clamped
pin pairs per wrong physical bit cell. The local clauses belong to
distinct centers. This transports the 109 field bound to **every**
Boolean assignment, with arbitrary gate, copy, constant and public-pin
values. Truthful auxiliaries on the attaining field proof have exactly
109 output failures. Therefore the complete Boolean minimum is also 109,
provided the implementation satisfies the stated layout conditions.

Consequently the fully priced threshold is

    eta < 109/(23 Q),                                (4)

where Q must be the actual padded address count of the new compilation.
The unrestricted strict integer error radius is four, since `23*4=92<109`
while `23*5=115>109`. The all-error bound does not assert that every
five-bit error causes failure. It specifies a uniform sufficient guarantee.

For the same Q as the previous cap-126 compilation, the sharp linear
budget is better by `128/23`. The actual census, scalar field-versus-circuit
comparisons, aliases and singleton witness must be checked separately;
this derivation does not infer Q from the reduced number of A queries.
The new encoded Boolean function is a different approximation target, and
no old approximating polynomial is reused without a separate argument.

## 6. Symbolic extension within the designed one-level family

Use the family already derived in
[Expedition 040](../040-recursive-verifier/soundness.md): `a>=3`, `s=2^a`,
`k=2a+1`, `N=2s^2`, A cutoff two and B cutoff `2s`. Choose U as the first
a binary basis coordinates and V as the other `a+1`; both are vector
subspaces of F. Their direct sum is F, and

    |D| = |U union V| = s+2s-1 = 3s-1.

The predicate (1), with this D, again yields one affine P on every passing
star, irrespective of the number or structure of failed centers. Offsets
0, 1 and 2 lie in U. When more than `2s+3` centers accept, the B schedule
has at least two passing rows and two passing column groups. Their common
points give one `B_*` of degree at most `2s-1`, agreeing on all accepted
sites. The residual (3) has degree at most `2s+3` and is nonzero by the
same evaluations at zero and one. Hence at most `2s+3` seeds accept.

For attainment choose any `2s` distinct nonzero points outside {0,1,2,3},
let W be their vanishing polynomial, take A=0 and

    B(X) = (W(X)+W(0))/(X W(0)).

The numerator has zero constant coefficient, so this is a genuine
polynomial of degree `2s-1`. Its residual is
`Z_{1,2,3}(X) W(X)/W(0)`, with exactly `2s+3` roots. Its honest
bivariate extension supplies every shared B cell. Thus the field minimum
is exactly

    V_NO = 2s^2-2s-3.                                (5)

The original one-level B query geometry has physical maximum `3s-1`:
the common rectangle combines s row offsets and 2s column offsets,
overlapping once. The cross A test matches that maximum. Conditional
on a private compiler with cap `3s-3`, the same argument gives exact
unrestricted `sigma=3s-1`. Therefore

    V_NO/sigma = (2s^2-2s-3)/(3s-1),

which grows on the order of s. This is a written result for that designed
family, using the existing one-level recovery argument. It is not a
family-wide implementation, gate count, padded-Q estimate, approximation
construction or extension to an arbitrary recursive source instance.

## 7. Reproducible geometry and attacks

[The finite difference-cover checker](check_difference_cover.py) verifies
the 23 actual offsets, every nonzero difference and both explicit overlap
sites. It additionally checks all 8,128 absolute star pairs in GF(128),
and analogous finite vector-group instances for a=4,5,6. In the actual
case, 105 mixed low/high differences have exactly two overlap points,
seven pure-low differences have eight, and fifteen pure-high differences
have sixteen. Removing high offset 8 destroys coverage at difference 9;
the checker preserves that failed repair. These finite checks illustrate
and check the implementation geometry; they do not replace Sections 2–6.

Adversarial boundaries:

- The two overlaps must be distinct; this uses `x!=y` and characteristic
  two, and is not a claim about arbitrary one-point star intersections.
- U and V need only be complementary binary subspaces; calling either a
  subfield would be incorrect and unnecessary.
- No global A-code assumption or global B-code assumption appears in
  the soundness argument. Only actual accepted-site agreement is used.
- The unchanged parent/sibling sharing, private copies and correct pin
  multiplicities are necessary for transporting the field bound.
- The result lowers the physical-read bottleneck to the remaining B
  maximum. Smaller A sets alone cannot lower this compiler's sigma
  below 23 while the B geometry remains unchanged.
- No proof-assistant acceptance, independent human review, novelty,
  unrestricted circuit lower bound or barrier escape is asserted.
