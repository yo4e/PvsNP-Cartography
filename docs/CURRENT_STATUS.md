# Current checkpoint — recursive rejection versus distance

The November 14 JST session gives a positive-distance counterexample to the unmodified bundled verifier for two recursive levels. Over GF(256) it rejects 128 seeds, while every degree-31-or-lower polynomial differs on at least 162 of its 256 root symbols. A second fixed XOR-translated test on the same proof restores sharp rejection at least equal to distance. The general two-level derivation treats both affine and cubic outer columns. On the designed GF(256) field-constraint NO instance the resulting sharp minimum is 221 rejected seeds; a YES witness passes every seed. These counts concern symbol-level public seeds.

Four translated reads also give a written three-level result for rate exponent three and dimensions ten and eleven. The dimension-ten route enumeration covers every seed. For unbounded dimension, the cost of certifying a whole outer row from a single acceptance is exponential; the frontier is a polynomial-cost accepted-site argument. [Scope of this obstruction](../expeditions/041-two-level-distance/whole-row-limit.md)

[Expedition 041](../expeditions/041-two-level-distance/conclusion.md) · [Issue 30](https://github.com/yo4e/PvsNP-Cartography/issues/30) · [Chronological evidence](../logs/2026-11-14-two-level-distance.md)

## Previous checkpoint — a shared recursive verifier

The November 13 JST session generated and checked one recursive level over a translated GF(128) root. On a designed NO instance the sharp minimum is 109 failed physical clause–seed pairs out of 10,717,568. An honest YES witness has zero failures. The physical sharing of parent and sibling cells matters: either detached-copy mutant can accept 127 of 128 seeds on a proof that the joined verifier rejects everywhere. The exact finite witness replay is separate from the written lower-bound argument for arbitrary assignments.

[Issue 28](https://github.com/yo4e/PvsNP-Cartography/issues/28#issuecomment-6856525926) is complete in its scoped source-variant and conformance sense. [Issue 30](https://github.com/yo4e/PvsNP-Cartography/issues/30) asks for the two-level rejection–distance tradeoff. A single changed auxiliary cell already shows why the first-level row-wide verdict cannot be reused at the next depth. [Expedition 040](../expeditions/040-recursive-verifier/conclusion.md) · [Session evidence](../logs/2026-11-13-recursive-verifier.md)

## Previous checkpoint — unary counting and a generated base verifier

The November 12 night session produced two generated GF(32) base instances with exact minimum rejection counts 0 and 25 out of 469,056 clause–seed pairs. The occurrence and line-interpolation arguments give costed inverse-polynomial uniform-error implications on infinitely many occupied YES lengths for separately encoded E^NP proof functions. Their status is a written derivation using published theorems. The five finite suites passed on the pinned code; there is no new Lean result.

[Issue 29 is completed](https://github.com/yo4e/PvsNP-Cartography/issues/29#issuecomment-6828212368). [Issue 28 remains open](https://github.com/yo4e/PvsNP-Cartography/issues/28#issuecomment-6828211809) for the first end-to-end recursive child with shared parent and sibling cells. [Expedition 039](../expeditions/039-unary-overlap-counting/conclusion.md) · [Verification and session log](../logs/2026-11-12-unary-and-verifier.md)

## Previous checkpoint — recursive query fibers

## Expedition 038

The written BV14 variant retains every root seed bit for fixed XOR-offset leaf reads. Seed-pin clauses retain all but one. The remaining transfer compares the density and soundness losses to a sufficient approximation precision; the unary construction avoids conditioning on a general binary instance. The full compiler has not been executed. [Conclusion](../expeditions/038-recursive-query-fibers/conclusion.md) · [November 11 log](../logs/2026-11-11-recursive-query-fibers.md) · [Issue 28](https://github.com/yo4e/PvsNP-Cartography/issues/28) · [Issue 29](https://github.com/yo4e/PvsNP-Cartography/issues/29)

## Expedition 037

Full XOR-tagged copies preserve the fixed-degree error ratio. In the BV14 report, the parent-membership marker printed in §6.3 is reversed for the row origin displayed there. A one-level coordinate check resolves the convention; the final binary-address fiber bound and adequate fixed-input approximation remain open in [Issue 28](https://github.com/yo4e/PvsNP-Cartography/issues/28). See the [conclusion](../expeditions/037-source-query-audit/conclusion.md) and [nightly log](../logs/2026-11-10-source-query-audit.md).

## Previous checkpoint — fixed global proof and query capacity

Freshly approved 2026-11-10 JST session. Research lead: 月野テンプレクス. **Issue27 is CLOSED/completed; Issue28 is the next source-dependent research question.** Issues8/15 retain their older independent-review scopes. This checkpoint is not authorization for another session.

## Accepted formal result

The actual pointwise GF2 polynomial-mixture predicate now connects to one positive-mass polynomial shared across all signed three-query OR tests. Actual constant/variable/negated-variable substitutions preserve evaluation and degree; the signed OR has degree at most3D. Actual subset-zeta outputs equal the accepting counts, and proved inverse maps connect the head/tail enumeration to the ORIGINAL full randomness cube. The final rational threshold is an exact integer comparison. Soundness explicitly ranges over all global proof functions, not independently resampled answers.

Accepted source **443fc96147b8bd616f82250eeb14c1484510e694**, tree53d6b566eaa773c8b427e40179dbf152db1e74a8. Completed SUCCESS run42728862159/job129541435980: strict --wfail9083 jobs,1594 namespace declarations within unchanged[propext,Classical.choice,Quot.sound]. ModulusAudit has76 named reports/20 explicit signatures, of which33/13 concern the new adapter. Actual source/commit/diff/audit and full completed output were retrieved. This is kernel acceptance and author statement inspection, not independent semantic review, second-kernel checking or a costed executable proof.

The substantive November9 work was recovered from live history despite the missing final chat report. An inherited HTTP504 download failure was followed by actual proof-script diagnostics. Two repairs fixed representation/reindexing without weakening statements. See ../expeditions/035-fixed-proof-adapter/execution-evidence.md and ../../PvsNP-Cartography/graveyard/2026-11-10-fixed-proof-recovery.md (repository-local equivalent: ../graveyard/2026-11-10-fixed-proof-recovery.md).

## Written mathematical continuation, outside Lean scope

Expedition036 derives the finite real-weight capacity criterion for allocating each test's mass to its true addresses: kappa=N*max_S forced_true_mass(S)/|S|. It gives one-global-polynomial expected failure <=kappa*uniform-error. Deterministic selectors lose at most a sharp factor3.

The certificate optimum is NOT the actual signed-error optimum: false literals impose additional constraints. Writing C for the exact unrestricted global-proof error constant, C<=kappa always; for non-tautological width-three clauses the separate written argument gives **C<=kappa<=4C**, with factor4 attained by seven weighted clauses and an actual degree-one polynomial on a two-bit address cube. This quantifies certificate loss, not a runtime speedup or a guarantee for the external PCP construction.

These are author-written finite derivations and exact controls, not independently reviewed or Lean-verified theorems. No novelty promotion is made. Core arguments: ../expeditions/036-query-capacity/capacity-and-transfer.md and sharp-signed-gap.md. Countermodels: ../graveyard/2026-11-10-capacity-optimality.md. Arbitrary projection maps still allow concentrated queries that defeat uniform-average error.

## Completed finite evidence

Code checkpoint **b742079296f15da7790a2e9eb711b89031fea57e**, treefb71bdd7eea96de3bf39eacec5409275e8f70de6, passed completed SUCCESS run42730390055/job129546608938. All four normal/-O/stored-output comparisons and compilation checks succeeded. Inherited adapter controls include9984 exact head counts and25830 threshold comparisons. New capacity tests cover12037 graphs and2151 signed families; the sharp-gap checker covers3146 exhaustive plus200 seeded families and named countermodels. Exhaustive scope is explicitly bounded. Actual new code/results/commit, local hashes and completed remote output were compared. See both expeditions' execution-evidence.md files.

No write/security blocker or unapplied patch remains. Local Git DNS and missing Lean/Lake were bypassed only by the already-authorized connected GitHub/Actions route. No axiom policy or paid-resource setting was changed. Later record commits are not additional mathematical execution evidence.

## Next decision

Issue28 asks whether the ACTUAL projection-PCP construction, or a specified soundness/degree-compatible modification, has a useful query-congestion or signed-error bound. A max-flow on an explicit exponentially large graph is not an efficient succinct selector. True-address sets may depend on the unknown satisfying proof. A useful loss must beat the soundness gap; uniform-average error does not automatically admit pointwise amplification. Inspect source structure before adding generic infrastructure, and park the route if a source-level obstruction defeats it.

External PCP/hierarchy proofs, costed Python refinement, independent semantics and a second kernel remain separate gaps. Earlier MOD3/counting/circuit results and failed uniform-cover usefulness are retained. No E^NP-to-NP substitution, unrestricted separation, barrier escape or P-versus-NP result is claimed.

Previous complete status: history/2026-11-10-pre-fixed-proof-status.md, original blob8d5d6a05334e391bafdb92dcd276623874bc05ea. Previous complete formal ledger: ../reports/2026-11-10-pre-fixed-proof-ledger.md. Session log: ../logs/2026-11-10-fixed-proof-query-capacity.md. Further work requires fresh approval.
