# Expedition 027: original MOD3 quadratic obstruction for every n>=299

Research lead: 月野テンプレクス. One fresh approval in the same conversation;
execution2026-10-28 JST. Issue20 is CLOSED as completed; Issue21 is the next
bounded frontier. This record does not authorize another nightly session.

## Mathematical milestone

For every natural n>=299, there is NO fixed finite probability distribution
on actual GF2 polynomials of total degree<=2 that computes the residue-zero
MOD3 target with success>=2/3 at every Boolean input. Weights are arbitrary
nonnegative REAL numbers summing to1. The family is chosen before the input.

This is now an end-to-end Lean-accepted statement of the ORIGINAL repository
predicate, not a restricted candidate-family obstruction or an assumption of
the formerly missing amplification. Mod3QuadraticObstruction.degree_two_impossible
has only n and299<=n as premises; its n299 endpoint has no premises.
It is a known-method reconstruction, not a novelty or optimal-threshold claim.

## What changed in the proof chain

IndependentTrials constructs the entire independent tuple family and product
weights and derives the exact failure recurrence. It proves monotonicity for
all real probabilities in[0,1], so smaller source errors and irrational weights
are covered. MajorityAmplification constructs the ACTUAL polynomial e8 of15
source polynomials, proves majority evaluation for both target bits and total
degree<=8d, and returns the original approximation predicate.

MajorityNumerics proves the exact error422009/4782969, a fast binomial evaluator's
equality with Nat.choose, and the strict rational gap at m297,D16. The previous
actual GF4 transport then contradicts a299-variable quadratic approximation.
Mod3Restrictions separately proves actual zero-substitution, degree/evaluation
and MOD3 preservation, extending the contradiction to all n>=299 with the same
original weights. No Python result supplies a formal hypothesis or axiom.

The implementation derives the exact law through a threshold recurrence, not
a separately compiled general closed-binomial-form theorem. This is sufficient
for the generic amplification and exact endpoint. The finite checker independently
compares recurrence, binomial formula and direct tuple sums; it is not the proof.

## Verification and refutation

Accepted source79c52432c82406b0a692a079adab147402dbbbe0,
treeb7e508b227252cf0bac4b4d45fbac0706cc84ad9. Completed SUCCESS formal
run40536961983/job122304691322. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac;
whole-root --wfail9065 jobs,984 namespace declarations within unchanged
[propext,Classical.choice,Quot.sound],27 new explicit reports plus all earlier
reports. Completed states, full decoded actual output, five actual source modules
and matching Git commit/tree were re-fetched and inspected. Local source blob
hashes match GitHub. The explicit printed endpoint confirms n,error1/3,degree2.
Evidence and actual timestamped excerpts are in ci-evidence.md and axiom-report.txt.

Exact source80757ad411675e02aea96c426bc383619e7c9579 passed completed
run40535117682/job122298162510. Full actual output and saved source/results were
re-fetched; normal/-O outputs and saved JSON match, as do local reruns. Controls
include32768 majority inputs,972 exact failure-law comparisons,39 genuine
polynomial families and45451 binomial coefficients checked by separate algorithms.
These are same-author finite corroboration, not an independent semantic reviewer
or a replacement for the universal probability and restriction proofs.

A significant failed shortcut: the direct numerical gap succeeds at n299 but
FAILS at n300 because of the parity-dependent cutoff. Therefore one cannot
extrapolate the finite inequality monotonically. The valid all-n proof uses
actual restrictions instead. Graveyard044 preserves exact fractions, diagonal
reuse and signed-mass counterexamples, and the degree<=7 majority failure.
Graveyard043 preserves four real implementation failures, including a warning-only
failure that had not reached its axiom audit. No target or warning policy was
weakened to obtain acceptance.

## Continue and choose the next question

The written continuation derives the candidate

 n >= (16d+2)^2 + 2  ->  no degree<=d approximation at error1/3.

A central-binomial invariant and parity-aware prefix estimate would connect the
accepted generic amplification to a growing-degree obstruction. Issue21 isolates
that estimate and its original-predicate application. This is not automatic
n300/n301 enumeration or a new general probability framework. The derivation in
next-frontier.md is NOT yet Lean accepted or independently reviewed. Its bounded
local checks are explicitly separate from the completed main exact CI.

## Remaining limits and environment

No independent new-code semantic review or second proof kernel was used. Normal
build/dependency caching was used; this is not clean-room replication. The
floating lean-action revision changed, and its actual resolved SHA is retained
in ci-evidence.md. Full decoded logs were read; committed files contain labeled
excerpts, not complete raw-log archives. Local Lean/lake were absent; Actions
provided the actual execution. No write blocker or unapplied patch remains.

The result does not establish exact degree3, an optimal299 threshold, general
n12 degree, a new unrestricted circuit lower bound, barrier escape or P versus NP.
Earlier exact degree2 n5..11 and affine exclusion n>=7 remain unchanged. #8/#15
retain separate older review scopes. New mathematical priority remains unknown.
This is the natural milestone ending the approved session.
