# Balanced affine score: counting sketch and a separate algebraic lemma

Evidence boundary: the counting argument below is an explicit self-authored
mathematical derivation, not yet a generic Lean Boolean-cube theorem or an
independently reviewed novelty claim. The Lean module covers only the algebra.

Let n>=3 be an integer. Put half the input probability uniformly on weight1
and half uniformly on weight3. MOD3 is0 on the first layer and1 on the second.
For a constant-zero affine parity with coefficient support size k:

S_n(k) = (n-k)/(2n)
       + [k*choose(n-k,2)+choose(k,3)]/[2*choose(n,3)].

Reason: a weight1 input succeeds exactly outside the coefficient support.
A weight3 input succeeds when its intersection with that support has size1
or3. Those two disjoint choices have the displayed counts. Adding constant1
complements the Boolean prediction on every input, so its score is1-S_n(k).
The family/input quantifier is unchanged by taking convex combinations.

Writing t=n-2k, expansion yields

S_n(k) = 1/2 + t*(n^2-t^2)/[4*n*(n-1)*(n-2)].

The polynomial numerator identity and the following SOS identity were checked
symbolically; reproducible exact bounded tests independently compare the
hypergeometric and cubic formulas for33147(n,k) pairs, n=3..256. Full cubes,
Walsh scores for all affine rows and direct canonical sums are checked n=3..12.
These bounded tests are NOT the proof of the generic identity.

## A rational envelope without square roots

For n>=0 and t>=0, t*(n^2-t^2) <= (2/5)*n^3.
If t<=2n/5, use n^2*(2n/5-t)>=0 and t^3>=0.
Otherwise use the exact nonnegative decomposition

2n^3-5n^2*t+5t^3
=5*(t-3n/5)^2*(t+6n/5)+(2/5)*n^2*(t-2n/5).

For -n<=t<0 the numerator is nonpositive. The same envelope therefore
holds on[-n,n]. When n>=7,

2n^2-15n+10 = (n-7)*(2n-1)+3 > 0,

so (2/5)*n^3 < [4*n*(n-1)*(n-2)]/6. Consequently the algebraic score is
strictly below2/3; complement symmetry makes it strictly above1/3 as well.
The separate Lean candidate proves these algebraic statements without finite
enumeration. Formal acceptance still requires actual completed build/axiom logs.

## Sharp domain warning and residual task

n=6,k=1 gives exactly2/3, and n=5,k=1 gives7/10. The equal-half dual therefore
does not give this strict obstruction at those arities. That does not overturn
the repository's n5/n6 degree equalities, which use different certificates,
or prove that an affine probabilistic family exists at either arity.

Remaining formal bridge: define the generic input distribution, prove layer
normalization and the combinatorial counts for actual affine polynomials, then
connect the already defined score through structural normal form and finite
duality. Do not label the pure real inequality itself a generic MOD3 theorem.
