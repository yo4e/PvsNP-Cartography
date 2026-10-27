# From the original MOD3 predicate to a product-agreement bound

Author reconstruction: 月野テンプレクス, approved session executed2026-10-27 JST.
Formal acceptance is recorded separately in ci-evidence.md. This is a known-
method specialization, not a mathematical-novelty claim.

## Exact input contract

Let m,D be natural numbers and delta a real number. Fix a finite index set I,
actual polynomials P_i in GF2[Z_0,...,Z_(m+1)] of total degree at most D, and
real weights mu_i>=0 summing to1, all BEFORE the input. At every binary input z,
assume the real probability that P_i(z) equals [|z|=0 mod3] is at least1-delta.
This is precisely the original HasProbabilisticDegreeAtMost predicate when
I=Fin k. No integer-ticket, uniformity, symmetry or multilinearity restriction
is imposed on the source polynomials. Repeated polynomials and real irrational
weights are permitted. The intermediate theorem accepts any finite index type.

## 1. An actual coefficient extension

Use K=GaloisField 2 2, Mathlib's actual splitting-field construction, and its
canonical GF2 ring embedding. Its cardinality is4. Therefore an element omega
outside{0,1} exists; choose one. Finite-field Fermat gives omega^3=1. Since
omega!=1, factoring omega^3-1 gives omega^2+omega+1=0. Characteristic two then
gives omega^2+omega=1 and omega^2+1=omega. The final theorem does not assume a
field or primitive root whose existence might be vacuous. Classical choice
selects the root; no additional axiom is introduced.

## 2. Two genuine restrictions and a linear encoding

Prepend00 and11 to x in {0,1}^m. (The earlier sketch appended the bits; prefixing
is an implementation choice, valid because the target only depends on weight.)
Write A0_i(x)=P_i(0,0,x) and A1_i(x)=P_i(1,1,x). The corresponding targets are
f0=[|x|=0 mod3] and f1=[|x|=1 mod3]. Both pointwise error guarantees remain delta:
we simply apply the hypothesis to those particular original inputs.

Over K form T_i=omega^2+omega*A0_i+A1_i. For the three residues of |x|, the target
pairs are(1,0),(0,1),(0,0), yielding respectively1,omega,omega^2. Thus the target
is omega^|x|. This is a LINEAR combination of the restrictions, so total degree
stays at most D, rather than2D. It is not a conversion of a truth table into
an unrestricted high-degree interpolating polynomial.

## 3. Affine input transport, including degree

For y in the ACTUAL grid{1,omega}^m set x_j=(y_j-1)/(omega-1). These values are
0 or1. The formal decoder returns the corresponding Fin2 bits; the separately
checked forward map sends0 to1 and1 toomega, and both inverse laws hold.
Consequently product_j y_j=omega^(sum_j x_j).

The implemented pulled polynomial performs coefficient embedding, constant
padding and inverse affine substitution in one eval2 operation. Its evaluation
is proved equal to embedding the ORIGINAL source evaluation at the padded
binary input. For each source monomial exponent e, the substituted product has
total degree at most sum e, by the degree bounds for powers and products.
Each nonzero coefficient exponent has sum e<=P.totalDegree. The finite sum bound
therefore proves actual total degree never increases. This covers arbitrary
powers, not only squarefree source polynomials. Apply it to both restrictions
and then to their linear combination to obtain the actual polynomial R_i(y).

## 4. Shared-index probability transport

At fixed y let c0_i,c1_i,cR_i be real correctness indicators. If both source
answers are right, root_encoding and the evaluation identity give cR_i=1.
In all four truth cases, cR_i>=c0_i+c1_i-1. Multiply by mu_i>=0 and sum:

 success(R,y) >= success(P,pad00(x))+success(P,pad11(x))-1 >= 1-2delta.

The same i supplies both answers, so independence is neither assumed nor needed.
A three-polynomial genuine MOD3 family in graveyard041 attains the loss2delta
at delta=1/3. An unjustified product-of-marginals estimate is false. Signed mass
one also fails, even when all apparent source correctness scores lie in[0,1].

## 5. Apply the already-derived agreement theorem

AgreementConsequences.pointwise_bound applies to the concrete field K, endpoints
1 and omega, actual R_i of degree<=D, and the unchanged real weights. It yields

 (1-2delta)*2^m <= B(m,D),
 B(m,D)=sum_{j=0}^{min(m,floor((m+D)/2))} choose(m,j).

The original-predicate endpoint necessary_inequality unpacks only the definition
of HasProbabilisticDegreeAtMost. It does not ask the caller for transported
success, a rank bound, or any conclusion-equivalent premise. The no-approximation
corollary uses only an explicit strict NUMERICAL inequality for B(m,D).

## A closed use, and the remaining mathematical question

At m=5,D=2, B=1+5+10+10=26. For delta=1/12 the left side is80/3>26. Therefore
seven_small_error_impossible excludes all fixed finite REAL quadratic mixtures
for seven-variable MOD3 at pointwise error at most1/12. This says neither that
1/12 is the optimal error threshold nor that the previously accepted degree2
success at error1/3 is invalid. No exhaustive enumeration of seven-variable
quadratic families is used in this proof.

At delta=1/3 the present inequality by itself is too weak: its left side is
2^m/3, whereas the binomial sum B(m,D) is at least2^(m-1) by symmetry (m>=1).
For m=0 the inequality is also automatic. This explains the named next use:
genuinely independent degree-aware majority amplification before transport.
It does not rule out every other possible lower-bound argument.

## Primary-source comparison (not an assertion of identical conventions)

Oded Goldreich, On teaching the approximation method for circuit lower bounds,
ECCC TR23-034 revision1,25March2023, Section3.2, printed pages13-14:
https://eccc.weizmann.ac.il/report/2023/034/revision/1/download
The author exposition uses the opposite MOD output convention and deterministic
uniform-input approximation. Its restriction error accounting therefore differs
from our pointwise random-family guarantee. It supplies the extension-field and
linear-input-map method. Here the specific GF2/GF4 answer encoding preserves D
and the real union bound loses2delta. This is a specialization/reconstruction;
no new circuit lower bound is inferred. Parsed text was read; screenshot calls
failed, so visual PDF inspection and a local PDF archive are not claimed.

Pinned primary formal-library sources: Mathlib9e6b3aac, FieldTheory/Finite/
GaloisField.lean, Algebra/MvPolynomial/Degrees.lean and Eval.lean. Those sources,
not a guessed API or current documentation alone, determine the compiled facts.
