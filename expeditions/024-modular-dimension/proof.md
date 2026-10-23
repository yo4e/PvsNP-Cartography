# Two-point compression, agreement dimension, and an explicit MOD3 consequence

Research lead: 月野テンプレクス. Approved 2026-10-23 JST session.
Evidence classes are deliberately separate: the Lean module targets the core
compression lemma; the dimension argument and MOD3 consequence below are an
author reconstruction, not an end-to-end Lean theorem or independent review.
Novelty is unknown. This reconstructs a known method, not a new lower-bound method.

## Source provenance and exact comparison

Oded Goldreich, *On teaching the approximation method for circuit lower bounds*,
ECCC TR23-034 revision 1, 2023-03-25:
https://eccc.weizmann.ac.il/report/2023/034/revision/1/download/
Section 3.1, proof of Lemma 4 (printed pp.11-13), and Section 3.2 (p.14).
The author's exposition, not the original Smolensky1987 paper, was retrieved.
Parsed text was inspected. PDF screenshot requests returned internal/cache errors;
visual inspection and a local PDF archive are NOT claimed.

The source uses extension-field root encoding and a dimension bound on an
agreement set. Its q<p statement must not be applied directly at p=2,q=3;
Section3.2 treats the larger output alphabet. Its deterministic average-input
error is distinct from our random-polynomial pointwise error. Below we derive
an exact degree-parameter version and a GF(4) adapter from the repository's
predicate, without importing its desired lower bound as a premise.

## A. Precise algebraic compression lemma

Let K be a field, a,b in K nonzero, R in K[Y_1,...,Y_m] of total degree<=D,
and H={y in {a,b}^m : R(y)=product_i y_i}. Let t be a natural number such that
m+D<=2t+1. For each S subset [m], a polynomial Q_S of total degree<=t exists,
chosen before y, such that Q_S(y)=product_{i in S} y_i for EVERY y in H.
Distinctness of a,b is not needed for this lemma, but is needed in B.

Define L(Y)=(a+b-Y)/(ab). Direct substitution gives aL(a)=bL(b)=1.
If |S|<=t, take Q_S=product_{i in S}Y_i. Otherwise take
Q_S=R times product_{i outside S}L(Y_i).
Its degree is <=D+m-|S|<=t: the strict integer inequality |S|>t means
|S|>=t+1, so D+m-|S|<=2t+1-(t+1)=t.
For y in H its evaluation is
(product_i y_i) times (product_{i outside S} y_i^(-1))=product_{i in S}y_i.
The polynomial Q_S itself is well defined on all K^m; equality is asserted
only on H. We use actual total degree, not the number of terms in R.

`TwoPointCompression.compress_monomial` encodes this statement and construction.
The premises do not assume compression, a rank inequality, or an agreement bound.
Its quantifiers are forall R,D,t,S, exists Q, forall y, not forall y, exists Q.
Taking t=floor((m+D)/2) meets the threshold for both parities.

## B. Complete author reconstruction of the dimension step

Assume additionally a!=b and put t=floor((m+D)/2). Then

    |H| <= B(m,D) := sum_{j=0}^{min(m,t)} choose(m,j).

Here is a proof, not an inference from the small-field tests.
For c in {a,b}, let ell_a(Y)=(Y-b)/(a-b), ell_b(Y)=(Y-a)/(b-a).
For each z in {a,b}^m, the product delta_z(Y)=product_i ell_{z_i}(Y_i)
is 1 at z and 0 at every other grid point. Thus every function f:H->K is
represented on H by sum_{z in H} f(z)delta_z(Y). Expanding it gives a linear
combination of squarefree monomials. Replace each by Q_S from A. This yields
one polynomial of total degree<=t representing f on H.

It remains essential to control the number of generators; a low-degree
polynomial need NOT already be multilinear. On the grid,
Y_i^2=(a+b)Y_i-ab. Repeatedly replacing a factor Y_i^k for k>=2 by
(a+b)Y_i^(k-1)-abY_i^(k-2) strictly decreases that exponent. This preserves
evaluation and never increases total degree. Termwise reduction terminates,
so f is represented by a linear combination of squarefree monomials with
support size<=t. There are B(m,D) such monomials.

The evaluation map from their K-linear span onto K^H is surjective by the
construction. The latter vector space has the |H| indicator functions as a
basis. Hence |H|=dim_K K^H <= B(m,D). This proof also covers H empty, m=0,
and D>=m; the last case only gives the trivial bound |H|<=2^m.

The Lean module does NOT yet encode this interpolation/reduction/surjectivity
chain. Finite-field row reduction corroborates it but is not its general proof.

## C. Degree-aware amplification for the repository predicate

Start with ANY finite normalized nonnegative REAL distribution on GF(2)
polynomials P of total degree<=d, fixed before x, with pointwise error<=1/3
for F_n(x)=1 iff |x|=0 mod3. Let n>=2 and m=n-2.

Sample 15 independent copies and compose with the elementary symmetric
polynomial e_8 on these 15 values. For a Boolean 15-tuple of weight w its value
is choose(w,8) mod2, equal to 1 exactly when w>=8. Indeed, in GF(2)[z],
(1+z)^w=product_{j: binary bit j of w is 1}(1+z^(2^j)); for 0<=w<=15 the
coefficient at z^8 is the bit of weight8. Thus this is exact majority15 with
degree8, not a degree15 or degree17 estimate. Each composite Q has degree<=8d.

A sample tuple has weight product of its original 15 masses. These real
weights are nonnegative and sum to (sum mu)^15=1, with no rationality premise.
At each fixed input the 15 error bits are independent with common probability
p(x)<=1/3. Their majority error is B15(p)=sum_{k=8}^{15}choose(15,k)p^k(1-p)^(15-k).
Differentiating and cancelling consecutive binomial terms gives
B15'(p)=51480 p^7(1-p)^7>=0 on [0,1]. Therefore error is at most

    delta=B15(1/3)=422009/4782969.

The checker verifies this polynomial derivative identity by exact integer
coefficients and the tail by rational arithmetic; no real-p sampling is used.
The Lean `majority15_binomial` checks only the finite binomial identity, NOT
this entire probability/distribution/composition argument.

## D. Two restrictions and root encoding, without extra degree cost

Let K=GF(2)[omega]/(omega^2+omega+1), a field of four elements because the
quadratic has no root in GF(2). Then omega^3=1 and omega!=1.
For each fixed sampled Q, put A0(x)=Q(x,0,0), A1(x)=Q(x,1,1).
They have degree<=8d. Their target indicators on m bits are respectively
f0=[|x|=0 mod3] and f1=[|x|=1 mod3]. Each pointwise error is<=delta.
The SAME sampled Q can be reused for these two restrictions: only the union
bound is needed here, not independence between the two resulting errors.

Embed the coefficients in K and set T=omega^2+omega A0+A1.
When both indicators are correct its values for residues0,1,2 are1,omega,omega^2.
Thus Pr_Q[T(x)=omega^|x|]>=1-2delta at every input, and degree(T)<=8d.
A single residue indicator cannot encode all three roots. Notice that T uses
a linear combination, not a product of A0 and A1, so the degree is not doubled.

Now y_i=1+(omega-1)x_i bijects {0,1}^m with {1,omega}^m. Its inverse is affine.
Substitute x_i=(y_i-1)/(omega-1) in T to obtain R, still degree<=8d. Correctness
becomes R(y)=product_i y_i. For each fixed sample, B bounds the fraction of
agreeing grid points. Averaging over the finite real sample distribution and
then interchanging two finite sums yields the necessary inequality

    1-2delta <= 2^(-m) sum_{j<=floor((m+8d)/2)} choose(m,j).

This is the exact pointwise-random to average-deterministic bridge. There is no
claim that a good layer average alone gives a fixed pointwise approximant.

## E. Explicit consequence candidate and its unverified boundary

For n=299, m=297, d=2, the transformed degree is<=16 and cutoff is156.
The exact numerator of the right-hand binomial sum is
209660394993883821947535023324611441185492248181130328034971979979928832110669599839817888,
with denominator 2^297. It is STRICTLY smaller than
1-2delta=3938951/4782969. The exact positive gap is in result.json; an independent
integer binomial recurrence reproduces the sum. Consequently A-D imply exclusion
of degree<=2 for the original n299 predicate. Fixing extra variables to0 then
implies the same exclusion for every n>=299, without assuming binomial monotonicity.

Classification: **author-reconstructed consequence candidate, not end-to-end
Lean acceptance and not independently reviewed**. The finite arithmetic is exact;
the generic chain A-D, rather than the arithmetic alone, carries the inference.
No optimal threshold, new lower-bound method, novelty, n12 result, circuit-size
bound, or P-versus-NP conclusion is asserted. The old 17-copy bridge remains valid;
this uses a different error target and sharper actual composition degree.

## Scientific decision

The previously imported hard ingredient now has an explicit reconstruction
and a generic formal core, with a concrete use: distinguishing bounded degree
from growing arity without enumerating all quadratics. The next missing formal
link is B's actual polynomial evaluation/rank bound, followed by C-D. Strengthen
that link or attack this candidate; do not open an automatic n13 search. A review
of the full chain would add independent semantics that today's checks do not supply.
