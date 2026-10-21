# Author's adversarial statement audit

Accepted source9785a2705cc88efd372ab3de29a61007387bd91d; see actual CI evidence.
This is a same-author audit, not a new independent Gemini/human review.

## Weighted input partition
For every n,w in the naturals, every A subset of Fin n, and EVERY h:N->R,
weighted_layer_sum identifies the actual sum over Layer n w with
sum(r=0..w) choose(|A|,r)*choose(n-|A|,w-r)*h(r).
The proof first bounds actual overlap by input weight, partitions by actual
overlap fibers, and uses a proved equivalence to the earlier Boolean slice.
It assumes neither this formula nor its conclusion. Negative values of h are
allowed; no input symmetry assumption is smuggled in.

The mean divides by choose(n,w). It is a totalized real identity for all w,
including w>n where both numerator and denominator vanish. Only w<=n proves
positive denominator and normalized probabilities. empty_layer_not_probability
is an explicit countermodel to interpreting zero-over-zero as a probability.

## Actual polynomial objects
subsetMonomial is the product of X_i over a FINSET, not ordered repeated edges.
elementary A d is the sum over actual d-element subsets. The degree bound is
MvPolynomial.totalDegree<=d, and evaluation is the NATURAL binomial count of
active d-subsets cast into GF(2). This handles d=0, empty A and d>|A| without
an assumed truth-table correspondence. Counting first and casting second is
essential; division by2 inside GF(2) would be invalid.

q_A=1+elementary(univ,1)+elementary(A,2).
r_A=1+elementary(univ\A,1)+elementary(A,2).
Both have actual totalDegree<=2. q_eval/r_eval prove actual eval equals the
weight/overlap expression; q_correct/r_correct then compare with the original
MOD3 target (one iff integer input weight is divisible by3). Only after this
chain are the weighted sum and mean theorems applied to correctness.
Natural subtraction w-overlap is legitimate because actual overlap<=weight;
the profile sum explicitly restricts overlap to0..w.

## Coverage and remaining limits
The polynomial evaluation and profile identities are generic in n,A,w. They
DO NOT say every such polynomial or every mixture is a pointwise approximant.
Full coordinate symmetrization is still required to convert appropriate layer
bounds to a pointwise mixture. The old family-before-input REAL-probability
predicate, target, field and degree definitions remain unchanged.

The n11 literal masks match q on the first8 coordinates and r on the first7
by exact independent finite evaluation. We did NOT add a new Lean equality
between those old coefficient-encoded polynomials and these definitions, nor
reprove the existing n11 degree equality. That finite regression is explicitly
separate from the generic theorem. The n11 quotient remains separately scoped.

## Attacks and follow-through
Wrong ordered edges cancel in characteristic2; wrong omitted denominator
turns the mean of1 into2; empty-layer normalization and omitted constants fail;
old raw n11 mixture fails without symmetrization. These are recorded controls.
A fresh n12 lift fails even after symmetrization at weight10 with19/33. The
restricted716-polynomial dual further excludes every reweighting of the same
zero/q9/r8 family, not every quadratic. Those finite counterexamples are NOT
new compiled Lean corollaries. Failed proof implementations remain in graveyard.

No support/denominator optimality, mathematical novelty, all-n degree2 upper
bound, circuit lower bound, barrier escape or P-vs-NP conclusion is inferred.
