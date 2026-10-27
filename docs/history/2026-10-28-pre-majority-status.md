# Current checkpoint: actual MOD3 transport and a closed small-error application

Freshly approved session executed2026-10-27 JST. Research lead 月野テンプレクス.
**Issue19 is CLOSED; Issue20 is the earliest useful unblocked mathematical target.**
Further nightly work requires fresh approval. Dated README/direction snapshots
are history, not instructions to restart completed Issues17/18/19.

## Accepted mathematical change

The original GF2 MOD3 probabilistic-degree predicate on m+2 inputs now implies

 (1-2delta)*2^m <= B(m,D),
 B(m,D)=sum_{j=0}^{min(m,floor((m+D)/2))} choose(m,j).

GF4Transport constructs an actual GaloisField2,2, nonbinary root and embedding,
two constant restrictions and degree-preserving affine input substitution.
Mod3ProductBound derives product success by a SAME-index real union bound and
applies the accepted agreement theorem. Its final necessary_inequality assumes
only the original approximation predicate, not transported success or a rank bound.
Arbitrary finite nonnegative normalized REAL weights are fixed before all inputs.
Source polynomials need not be multilinear or symmetrized. Grid inverse laws
are explicit, and actual totalDegree never increases.

TransportExamples additionally proves no degree<=2 approximation of seven-variable
MOD3 at pointwise ERROR1/12, using26<80/3. This is NOT error1/3, optimality or a
new exact degree classification. Old n5..11 degree2 equalities at1/3 are unchanged.

## Actual evidence and attacks

Accepted source5acf085fa43f1fa4578252c1653033d3f523e753,
tree12c1e9ab938e823a15566c7921fdc6550217d1e6. Completed SUCCESS formal
run40430504329/job121946718143, pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
whole-root --wfail9060 jobs,875 namespace declarations within unchanged
[propext,Classical.choice,Quot.sound],23 new explicit reports and all old reports.
Completed steps, full actual output, actual source modules and commit/tree were
re-fetched and inspected; local source blob hashes match GitHub.

Exact run40430504271/job121946717619 at the same source also completed SUCCESS.
Normal/-O byte equality and actual/saved JSON equality, plus local reruns, pass.
3680 polynomials and18304 input evaluations corroborate, not prove, the generic
statement. Graveyard041 contains real polynomial counterexamples to false
independence and signed normalized weights;042 preserves the inspected failed
first build and faithful repair. No statement or verification policy was weakened.

Expedition026 contains full derivation, statement/barrier audits, actual output
excerpts, ci-evidence.md and conclusion. Existing Lean kernel only; no independent
semantic reviewer or second kernel. Old review #15 does not cover this new code.

## Next: Issue20, independent majority and the original n299 endpoint

The current inequality alone at error1/3 is too weak. Construct genuine15-fold
independent product weights and the actual GF2 majority15=e8 polynomial; prove
degree<=8d and error<=422009/4782969 for arbitrary real source weights. Apply the
accepted transport at m297,D16 and kernel-check the exact numerical gap. Prove
zero-padding restriction to extend exclusion from299 to all n>=299.
Do not assume amplified success as a premise or repeat one sampled index15 times.
The residue coupling and the majority independence are different operations.

The original n>=299,error1/3 degree2 exclusion remains an AUTHOR-RECONSTRUCTED
CANDIDATE until this chain is accepted. Unrestricted n12 remains unresolved.
No novelty, optimal threshold, new circuit lower bound, barrier escape or P-vs-NP
result is asserted. #8 and #15 remain separate nonblocking older review tracks.
No permission blocker or unapplied patch remains. Local Lean is absent; Actions
supplied actual execution. Prior status is archived byte-identically at
history/2026-10-27-pre-transport-status.md, blobb7ee38e060b7b8ea6525d13b6160b6fd10ec0980.
Session log: ../logs/2026-10-27-mod3-product-transport.md.
