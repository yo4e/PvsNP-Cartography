# Two invalid promotions of a true-literal capacity certificate

2026-11-10 JST. Research lead: 月野テンプレクス. These counterexamples concern our proposed transfer interfaces, not a refutation of the original fixed-proof PCP argument. No novelty claim.

## Fractional feasibility does not give a deterministic selector at the same capacity

Attraction: the exact weighted cut condition looks like a complete selection criterion.
Failure: tests carry indivisible mass if one deterministic address must be chosen. On a four-address Boolean cube, one positive clause with three distinct true addresses has fractional congestion4/3 and deterministic congestion4. The factor3 loss is real and is also the general upper bound obtained by selecting each row's largest fractional share.
Repair: use the fractional allocation directly in the error inequality, without changing the sampled global proof, or explicitly charge the deterministic rounding loss. Do not conflate splitting test mass with independently sampling proof answers.

## Optimal allocation does not give the optimal actual signed-error constant

Attraction: minimizing congestion might seem to make the uniform-error transfer sharp for all signed OR verifiers.
Failure: the one-true-literal certificate discards the restrictions from literals that are FALSE under the target proof. With pi=1 on four addresses and the three equal-weight clauses(v0 OR v1 OR not v2), (v1 OR v2 OR not v0), (v2 OR v0 OR not v1), optimal congestion is4/3 but the exact failure/uniform-error constant is2/3. The latter is attained by the actual degree-one polynomial p(y0,y1)=y1. There are no tautological clauses in this example.
Repair: for each test retain both true addresses A_t and false addresses B_t. Failure under error set E is exactly A_t subset E and B_t intersect E empty. The exact unrestricted Boolean-function constant is the maximum weighted failure density over E, whereas capacity remains a valid but possibly nonsharp certificate. Enumerating E is not an efficient succinct algorithm.

## Verification and disposition

Expedition036 contains complete written finite real-weight derivations, an exact flow checker, two cut enumerations, deterministic selector enumeration, signed truth-table checks and both countermodels. Finite evidence is not a universal proof, and the written proof is not independently reviewed or Lean checked. Preserve the original pointwise method; only use average error with an explicitly justified loss and actual query-structure bound.
