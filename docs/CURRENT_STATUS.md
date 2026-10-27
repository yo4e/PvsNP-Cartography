# Current checkpoint: original MOD3 quadratic exclusion for every n>=299

Freshly approved session executed2026-10-28 JST. Research lead 月野テンプレクス.
**Issue20 is CLOSED; Issue21 is the next bounded mathematical frontier.**
Fresh approval is required for later nightly work. Dated README/direction and
older Issue descriptions are history, not instructions to restart completed work.

## Accepted mathematical change

For EVERY n>=299, the ORIGINAL GF2 MOD3 predicate has no fixed finite distribution
of actual total-degree<=2 polynomials with nonnegative REAL weights summing to1
and success>=2/3 at each Boolean input. This covers arbitrary real weights and
all such polynomials, not a selected coefficient family or rational-ticket model.

Mod3QuadraticObstruction.degree_two_impossible has only n and299<=n as premises.
The formerly missing independent-majority chain is now discharged: actual product
weights and their exact real failure law, actual e8 majority composition with
degree8*d, exact error422009/4782969, the strict m297,D16 rational contradiction,
and actual zero-variable restriction to extend from299 to all larger arities.
The family is chosen before every input. No amplified-success or lower-bound
hypothesis is smuggled into the final theorem.

The generic failure law uses a threshold recurrence. A separate general
closed-binomial-form identity is not a compiled endpoint and is not needed by
the completed proof. The recurrence and its monotonicity/endpoint are proved.

## Actual evidence and adversarial findings

Accepted source79c52432c82406b0a692a079adab147402dbbbe0,
treeb7e508b227252cf0bac4b4d45fbac0706cc84ad9. Completed SUCCESS
run40536961983/job122304691322: Lean4.35.0-rc4/Mathlib9e6b3aac,
whole-root --wfail9065 jobs,984 namespace declarations within unchanged
[propext,Classical.choice,Quot.sound],27 new explicit reports plus earlier reports.
Completed steps, full decoded actual output, five source modules, actual Git
commit/tree and explicit endpoint statements were re-fetched and inspected.
No source sorry/admit/new axiom/native_decide or warning waiver was introduced.

Exact source80757ad411675e02aea96c426bc383619e7c9579 passed
run40535117682/job122298162510. Actual/saved JSON and normal/-O outputs agree,
including local reruns.32768 majority inputs,972 failure-law comparisons and
39 actual polynomial families corroborate rather than prove the generic result.
Expedition027 contains the derivation, same-author statement and barrier audits,
conclusion, actual output excerpts and resolved execution evidence.

The direct numerical gap is positive at n299 but NEGATIVE at n300 because of
parity. The all-n proof correctly uses actual restrictions, not numerical
monotonicity. Graveyard044 preserves this counterexample, correlated reuse,
signed-mass and degree-seven-majority failures. Graveyard043 preserves four
failed implementations and faithful repairs, including a warning-only failure.

## Next: Issue21, a growing-degree obstruction

The written candidate is exclusion of degree<=d at error1/3 whenever
n>=(16d+2)^2+2. It would connect the accepted generic amplification to a uniform
parity-aware binomial-prefix bound. Its new ingredients are a central-binomial
square invariant, symmetry/unimodality and the correct even/odd prefix estimate.
The precise derivation and local controls are in Expedition027/next-frontier.md.
This is NOT yet an accepted Lean theorem, independent review or sharp threshold.
The local frontier checker is NOT included in the completed main exact CI.

Earlier exact degree2 n5..11 and affine exclusion n>=7 remain. General n12 degree
is unresolved. The n>=299 exclusion is not exact degree3, an optimal299 threshold,
novel mathematics, a new unrestricted circuit lower bound, barrier escape or a
P-versus-NP result. #8/#15 keep their separate older review scopes. No new-code
independent semantic reviewer or second kernel was used. Normal caching was used;
full decoded logs were read but only labeled excerpts are committed.

No write blocker or unapplied patch remains. Local Lean/lake were absent; actual
formal execution used Actions. The previous complete status is archived by its
identical blobc6ca6ab73a68c90471ab1f2c9b7ca4cbe001477e at
history/2026-10-28-pre-majority-status.md.
Session log: ../logs/2026-10-28-independent-majority.md.
