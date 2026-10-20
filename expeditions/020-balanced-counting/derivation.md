# Ordered samples: derivation and proof obligations

Let D=n(n-1)(n-2), n>=3. Use sample type Fin(n) + Fin(n)^3. A singleton has
probability1/(2n); a pairwise-distinct ordered triple has probability1/(2D);
all other triples have zero mass. Map a singleton to its one-hot Boolean input
and a valid triple to the input supported on its three coordinates.

For arbitrary real values z_i, S=sum z_i, Q=sum z_i^2 and R=sum z_i^3,
inclusion-exclusion gives sum_distinct z_i*z_j*z_k = S^3-3QS+2R.
The +2R correction is essential: all-equal triples were subtracted three times.
Taking z_i=1 gives exactly D ordered triples and normalization of sample mass.
No enumeration over a bounded n is needed by this proof strategy.

For affine coefficients b_i in{0,1}, take z_i=1-2b_i, so Q=n,R=S and
S=n-2k, where k is coefficient Hamming weight. Write csign=1-2c for the
constant coefficient. Singleton correctness is (1+csign*z_i)/2, because its
MOD3 target is0. Valid-triple correctness is(1-csign*z_i*z_j*z_k)/2, because
its target is1. These identities must be checked against actual GF(2)
affineValue, not used as a replacement definition.

Thus the actual sample score is
1/2 + csign*S*(n^2-S^2)/(4D).
Constant0 gives BalancedAffineDualAlgebra.score(n,k); constant1 gives its
complement, which also equals score(n,n-k). The proved cubic envelope gives
one common bound B(n)=1/2+n^2/(10(n-1)(n-2))<2/3 for n>=7. With a faithful
actual-evaluation bridge, finite real duality and structural degree-one normal
form exclude every finite REAL mixture of actual degree<=1 polynomials.

The ordered-sample measure is mathematically half-uniform on weight1/3: each
three-element support has exactly six orderings, and D=6*choose(n,3). However,
the formal obstruction can use the sample index type directly, as supported
by finite_dual_obstruction, without assuming that quotient theorem. Any
uncompiled pushforward/fiber or binomial statement remains a separate gate.

Novelty is unknown. This is a reusable explicit lower certificate, not a new
complexity-class separation. A small-arity obstruction also extends by a
properly proved restriction, so a generic affine exclusion is not itself a
new asymptotic research landmark. No degree-two upper bound is extrapolated.
