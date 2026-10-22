# Formal assumption ledger

## Current checkpoint: real mixtures and a scoped n12 obstruction

Approved2026-10-22 JST night; acceptance completed2026-10-23 JST just after
midnight. Existing numerical degree2 equalities n5..11, generic degree<=1
exclusion n>=7, balanced fibers and certified clique profiles remain unchanged.
Issue16 is complete. Issue17 selects the next substantive growing-degree lemma.

## Actual accepted execution and assumptions

Code9410fa952ad4b92f09237bfc09be5ad200413db3,
tree d71346655c0012faa1c6b70991322ddf6cd5052f.
Completed SUCCESS run39800322628/job119898840545:
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39800322628
Lean4.35.0-rc4, Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Root --wfail9054 jobs. Namespace axiom audit741 declarations. All24 new target
outputs and earlier targets stay within [propext,Classical.choice,Quot.sound].
No sorry/new axioms/native_decide or warning-policy relaxation was used.

The full decoded job log, completed job/steps, actual source and matching Git
commit/tree were re-fetched. The actual target transcript is preserved in
Expedition023/axiom-report.txt; ci-evidence.md records provenance and excerpts.
Source-generated reports and partial builds are not acceptance evidence.
Re-fetched source blobs match locally computed Git blobs:
- ProfileMixtures.lean:1a552897d03f8d20796bc3fdb5764baa63b05a39
- RestrictedCliqueObstruction.lean:505eef80ba592227c7f36cf02c3ad36629a364cc

## Faithful semantic chain

ProfileMixtures.layerAverage_mixture is finite REAL linearity for arbitrary
actual polynomial correctness values; it even permits signed coefficients.
q_mixture_profile/r_mixture_profile substitute accepted actual q/r evaluation
formulas. feasible_of_profiles requires actual-profile equality, a degree bound
for every row, nonnegative normalized real coefficients and sufficient layer
bounds for a symmetric target. It delegates to EXISTING full symmetrization,
not an assumption that the desired pointwise mixture is already feasible.

layerMass assigns each input in layer w mass1/choose(n,w). The expectation
identity applies to any real score and even empty layers, whose totalized
measure is zero. Probability normalization explicitly requires w<=n.

RestrictedCliqueObstruction.Allowed names precisely zero, every q_A of subset
size9 and every r_B of subset size8 at n12. Actual totalDegree<=2 is proved.
Total dual masses5/14 and9/14 go to uniform layers6 and10. Positivity and full
input normalization are proved. Deterministic scores9/14 for zero/q9 and241/462
for r8 are derived from actual correctness, not supplied as premises. Existing
real finite weak duality yields no_allowed_mixture and no_allowed_certificate.
The latter keeps Allowed inside its existential statement. Nonuniform subsets,
duplicate rows and irrational coefficients are permitted; negative weights are
not probabilities. The distribution is fixed BEFORE the universal input.

The accepted q8_dual_score and support_restriction_essential exhibit a genuine
degree2 polynomial scoring5/6 under the same dual. Therefore the support
restriction cannot be removed. This does not itself provide a pointwise2/3
quadratic approximation, and does not settle unrestricted n12 degree.

## Separate finite sharpness and source argument

At772b0eac, exact run39799669199/job119896456402 independently evaluates all716
candidate truth tables on4096 inputs and compares9308 actual layer means to
closed profiles. Normal/-O and saved/actual equality both pass. Its matching
primal has zero mass3/14 and each of220 q9 rows mass1/280; its pointwise minimum
is9/14. Thus the RESTRICTED finite game has value9/14. This primal is not a
compiled Lean sharpness theorem, nor a minimal support/denominator assertion.
Old n11 coefficient regression remains finite, not a new old/new polynomial
identity theorem. No unnecessary reproof of the n11 degree equality was made.

source-bridge.md reconstructs independent-majority and two-bit restriction
adapters to a specifically cited literature theorem. The difficult universal
lower bound is IMPORTED, not proved by this repository. Its known Omega(sqrt(n))
consequence is not novel and gives no numerical n12 threshold. Generic Lean
amplification and the source's hard low-degree agreement lemma are still absent.
Exact majority truth-table/ANF and padding tests do not fill those proof gaps.

## Failures, review, environment and history

Failed e1703205/run39797072216: an already-closed tactic goal plus unresolved
GF(2) numerals. Failed7f687ceb/run39798702853: only three ZMod.val1 reductions
remained. The successful repair used a definitional equality proved by rfl.
Graveyard034/035 retain these failures; graveyard033 retains countermodels.
No claim was weakened to get green CI.

Gemini Issue15 and its correction cover only old0e30b5b7. New-code independent
semantic review, external human review and second-kernel verification are not
claimed. Human review #8 remains a separate nonblocking track; novelty is
unknown. Local Lean is absent; actual execution used Actions. No write blocker
or unapplied patch remains. Production CI is not a second proof kernel.

The preceding COMPLETE ledger is preserved byte-identically at
reports/2026-10-22-pre-mixtures-ledger.md, blob
cbad8c2540cfb1a85a2f68b541f03e67ab731d16, including all older archive links.
No new unrestricted quadratic, circuit or P-versus-NP result, arbitrary-n
quadratic upper bound, novelty or proof-barrier escape is asserted.
