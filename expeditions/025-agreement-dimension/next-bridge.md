# Next concrete bridge: reuse the same random index for both residues

Author reconstruction, not a new accepted Lean endpoint or novelty claim.
Approved 2026-10-24 night session, executed 2026-10-25 JST.

## Contract

Let m,D be arbitrary naturals. Suppose a fixed finite family of actual GF(2)
polynomials P_i in m+2 variables has total degree <=D, with nonnegative REAL
weights mu_i summing to1. Assume pointwise error at most delta for the predicate
1 iff input Hamming weight is0 modulo3. No rationality or uniformity is assumed.
We seek a genuine degree<=D polynomial family on {1,omega}^m over a concrete
characteristic-two field with omega^2+omega+1=0, with pointwise success>=1-2delta
for the coordinate product. The field and root must actually exist, not be
asserted as a vacuous premise in the final MOD3 consequence.

## Two restrictions, one random index

Define A0_i(x)=P_i(x,0,0) and A1_i(x)=P_i(x,1,1). They approximate respectively
f0=[|x|=0 mod3] and f1=[|x|=1 mod3], each at error<=delta and degree<=D.
Use THE SAME i with the original weight mu_i for both. This is a fixed joint
coupling, independent of x. We do not need to choose two independent polynomials
or construct a new product distribution for this particular transport.

Embed GF2 into K=GF4 and form the actual polynomial

 T_i(x) = omega^2 + omega*A0_i(x) + A1_i(x).

Its degree is <=D, not 2D. The exact target is omega^{|x|}: the pairs (f0,f1)
are (1,0), (0,1), (0,0), giving1,omega,omega^2 respectively.
Indeed 1 and omega are GF2-linearly independent, so the encoded answer is right
if and only if BOTH binary residue answers are right. For the required lower
success bound, only the forward implication is needed.

For each i and fixed x, let c0,c1,cT be the real correctness indicators. Then
cT >= c0+c1-1. Multiply by mu_i>=0 and sum, using sum_i mu_i=1. Therefore
success(T,x) >= success(A0,x)+success(A1,x)-1 >= 1-2delta.
This union-bound argument needs no independence between the two residues.
The same-index coupling preserves the original finite support and real weights.

## Change the actual input grid without changing degree

Set y_j=1+(omega-1)*x_j. This is a bijection from Boolean inputs to the ACTUAL
set {1,omega}^m. Its inverse is x_j=(y_j-1)/(omega-1), since omega!=1.
Substitute these affine inverse polynomials into T_i to obtain genuine R_i(y).
Coefficient embedding, constant padding and affine substitution do not raise
actual total degree; their statements need to be proved for MvPolynomial, not
inferred from a truth-table conversion. On the grid,
product_j y_j=omega^{|x|}, so R_i approximates the coordinate-product target.

Apply the actual agreement-mixture endpoint from this expedition to get

 (1-2delta)*2^m <= B(m,D).

This eliminates the need for a second independent real product distribution in
the residue-to-root adapter. It does NOT eliminate independent draws in the
separate majority-amplification step. Repeating one sampled polynomial15 times
still does not reduce its error. A future proof should keep those distinct.

## Bounded implementation and acceptance target

Construct the GF4 coefficient embedding, two constant restrictions, linear root
encoding, affine input transport and same-index correctness inequality, then
instantiate AgreementConsequences.pointwise_bound. Preserve family-before-input
quantifiers, actual totalDegree and arbitrary finite REAL weights. Do not assume
the desired root-agreement guarantee or the MOD3 lower bound as a premise.

The n299 candidate separately uses genuine15-fold independent majority with
GF2 degree8 and delta=422009/4782969, hence D=16 from original degree2, m=297.
Generic amplification, this actual polynomial transport and full endpoint
integration remain unaccepted until their own pinned build and semantic audit.
The current deterministic agreement theorem alone does not decide n299 or n12.
This is a reconstruction/simplification for this proof chain, not novelty.
