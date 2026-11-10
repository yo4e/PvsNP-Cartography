# How much does the true-literal certificate lose? A sharp factor four

2026-11-10 JST. Research lead: 月野テンプレクス. This is a continuation of capacity-and-transfer.md, not a Lean theorem or an independent review. General statements below have explicit author-written finite proofs; the finite checker is corroboration, not their basis. Novelty has not been established and is not claimed.

## Statement with its indispensable hypothesis

Retain a nonempty finite address set X, N=|X|, fixed binary proof pi, and normalized nonnegative REAL test weights nu. Every signed OR test has at most three occurrences and is satisfied by pi. Let A_t and B_t be its distinct true and false addresses under pi. Assume every positive-weight test is non-tautological, equivalently A_t intersect B_t is empty.

Let kappa_frac be the optimal fractional true-address congestion, and C_OR the optimal constant bounding actual weighted test failure by uniform proof error, over all binary global proofs. Their formulas were derived in capacity-and-transfer.md. Then

    C_OR <= kappa_frac <= 4*C_OR.

The factor four is sharp, even for constant query projections on a two-bit address cube, with a degree-one polynomial attaining the actual error ratio. This does not claim that the worst-case factor is attained by the specific projection-PCP in the external source.

## Proof, without finite-to-general extrapolation

The upper bound C_OR<=kappa_frac was already proved by the fractional allocation certificate. Choose a nonempty address set S attaining the finite maximum in the capacity formula, and write f(S)=sum_{t:A_t subset S} nu_t. Thus kappa_frac=N*f(S)/|S|.

Choose a random error set E contained in S by putting each element of S in E independently with probability1/2; leave every address outside S correct. For a test with A_t subset S, failure requires all A_t to enter E and all B_t intersect S to stay outside E. Non-tautology makes these requirements consistent. Their total number of distinct constrained addresses is at most3. The test therefore fails with probability

    2^(-|A_t|-|B_t intersect S|) >= 1/8.

By nonnegative weighted summation, the expected failure is at least f(S)/8. On the other hand, for every E, including E empty, the definition of C_OR gives failure(E)<=C_OR*|E|/N. The expectation of |E| is |S|/2, hence

    f(S)/8 <= C_OR*|S|/(2N).

Multiplying by8N/|S| gives kappa_frac<=4*C_OR. This argument uses a finite probability space and applies to arbitrary real test weights. It is not an assertion about efficient enumeration of E, finding pi, or computing a selector on a succinct verifier.

## Exact sharp example

Use X={0,1,2,3}, interpreted as the two-bit Boolean address cube, and pi identically1. For every nonempty A subset{0,1,2}, include one clause with a positive literal at each address in A and a negative literal at each address in {0,1,2} minus A. Give that clause weight |A|/12. These seven weights sum to1 because the sum of all nonempty subset sizes of a three-element set is12. All clauses have three distinct occurrences, are non-tautological, and are true under pi.

Allocate |A|/12 equally over its |A| true addresses. Each allowed test/address contribution is1/12. Each of the three addresses belongs to four subsets, so each receives load1/3, proving congestion4/3. The cut{0,1,2} forces all mass, so kappa_frac=4/3 exactly.

For an error set E, put U=E intersect{0,1,2}. If U is empty, no clause fails. Otherwise exactly the clause indexed by A=U fails, with weight |U|/12. An error at address3 adds uniform error but no failure. It follows that

    C_OR = 4/12 = 1/3,    kappa_frac/C_OR = 4.

The actual GF2 polynomial p(y0,y1)=y1 differs from pi at addresses0 and1. Its uniform error is1/2 and its weighted test failure is2/12=1/6, attaining the ratio1/3. Thus the example is not merely a hypothetical non-polynomial truth table.

## Adversarial boundary

Without the non-tautology premise there is no such multiplicative lower bound. On a one-address set, the test(v OR not-v OR v) has true-address congestion1 but actual failure constant0. Zero-weight tautologies can be ignored; positive-weight tautologies must not be counted as forced mass in an application of the factor-four proof. One may drop them and renormalize the remaining tests, explicitly accounting for the change of total mass; that is a different bookkeeping step, not an implicit assumption.

The deterministic-selector factor3 from capacity-and-transfer.md compares a different pair of quantities. It must not be confused with this factor4 between the fractional certificate and actual signed failures, and neither is a running-time speedup.

## Checks and next decision

verify_signed_gap.py separately evaluates actual signed literals, enumerates capacity cuts and all finite error sets, and checks the random-half-subset expectation. It exhausts3146 families with one or two tests on address sets of sizes1..3 and weights0,1,2 (nonzero total), plus200 seeded four-test families on sizes4 and5. The named seven-clause sharp example and the excluded tautology are separate controls. Normal/-O output agrees locally; remote evidence is recorded separately after completion.

This bounds the loss in a proposed average-error adapter but does not establish the needed capacity for the actual PCP construction. The next named use is to inspect that construction's query fibers and soundness-preserving modifications, not to grow an unrelated optimization library. Formal proof/runtime refinement, source-dependent query bounds, external hierarchy assumptions and independent semantic review remain separate.
