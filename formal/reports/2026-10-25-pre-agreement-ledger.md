# Formal assumption ledger

## Current checkpoint: two-point monomial compression, 2026-10-23 JST night

The accepted new endpoint is TwoPointCompression.compress_monomial, not the
full agreement-dimension theorem or the n299 consequence. Previous accepted
n5..11 degree2 equalities, n>=7 affine exclusion, profiles and restricted n12
obstruction remain unchanged. #17's bounded first lemma is complete; #18 is next.

## Actual acceptance and trust boundary

Source de8913e7c1058844354f376ae8a72a2a2abddfa9;
tree5b9639c71fbcab3706fcb4780e390e3520b5bca4.
Completed SUCCESS run39964232854/job120449783214, pinned Lean4.35.0-rc4,
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Root --wfail9055 jobs;759 namespace declarations within unchanged
[propext,Classical.choice,Quot.sound]. Nine new target reports and all previous
reports completed. No sorry/admit/new axioms/native_decide or warning relaxation.
The full decoded output, completed state and actual source/commit/tree were
re-fetched. Module blob e22c7cffd1e893575301d13863e1703aeeafcd43 matches local5607
bytes. Expedition024/axiom-report.txt preserves actual timestamped excerpts,
not the full raw log; ci-evidence.md records resolved environment and commands.

This is the existing Lean kernel. No second kernel or independent semantic
review is inferred. Later record-only documentation is not a new formal execution.

## Statement fidelity

For any field K, n,d,t, a!=0,b!=0, actual R:MvPolynomial(Fin n)K with
R.totalDegree<=d and n+d<=2t+1, and any finite coordinate subset S, the theorem
constructs one actual Q with totalDegree<=t BEFORE quantifying over y.
At every y with each coordinate a or b AND R(y)=product y, evaluation of Q is
the squarefree monomial on S. This last premise defines the agreement set;
it does not assert its size, any compression or the desired lower bound.

Small supports use the monomial itself; large supports use R times factors
(a+b-X_i)/(ab) for complementary coordinates. Actual degree and evaluation
are proved. Nonzero hypotheses justify cancellation. Distinctness is NOT
needed here, but is introduced explicitly in the unformalized dimension step.
The theorem allows empty/full supports, arbitrary arities and fields, not only
GF4 or tested small dimensions. No finite computation supplies this generality.

Other accepted endpoints give squarefree/inverse-product degrees, the actual
inverse identity, complement evaluation/degree and a rational zero-grid
counterexample. majority15_binomial proves choose(w,8)%2=[w>=8] only for w<=15.
It does not formalize finite real product distributions or error reduction.

## Exact limits of nonformal mathematics

Expedition024/proof.md gives the author reconstruction of interpolation,
degree-preserving reduction and surjective evaluation yielding the full
agreement-dimension bound. It then gives a degree-aware majority15/residue/GF4
adapter and an explicit n>=299 degree<=2 exclusion candidate for the original
GF2 pointwise predicate. The dimension theorem, generic amplification and GF4
transport are NOT accepted Lean endpoints. Independent review is absent.
Exact binomial arithmetic and finite rank tests do not fill those formal gaps.
Novelty and threshold optimality are not asserted.

## Finite corroboration and corrected evidence

Accepted repaired checker531f3a86b602a7a1b272138e55e051279598f28f passed completed
run39965200654/job120453135024, with256 determinant-rank controls,18020 polynomial
rank cases and53942 compression evaluations, alongside majority/root/parameter
checks. Normal/-O and stored/actual output agree. Source/result/commit re-fetched;
verify.py blob3e06d549bc9c7d7295838a565e04665b09eaea0d matches local bytes.
The initial green run39964233049 is NOT accepted rank evidence because its
rank routine read stale pivots after rebinding a list. Graveyard038 preserves
the defect, counterexamples and repair. Lean did not depend on Python ranks.

Graveyard036 preserves mathematical shortcuts that fail, and037 the actual
formal implementation failures. Targets, hypotheses and axiom policy were
not weakened. A source typo revision has no claimed uninspected job verdict.

## History and review

The entire preceding ledger is archived byte-identically at
reports/2026-10-23-pre-compression-ledger.md, blob
dd47e070cf616c83fef28d7d48e8f0b47ae86193, including its earlier archive links.
Gemini #15 still covers only0e30b5b7; #8 human review is separate/nonblocking.
No new-code independent review, second kernel, n12 determination, new circuit
bound, novelty, proof-barrier escape or P-vs-NP conclusion is claimed.
Local Lean was unavailable; connected Actions supplied actual execution.
