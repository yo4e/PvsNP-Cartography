# Current checkpoint — covering proved, recognition/usefulness shortcuts rejected

Freshly approved2026-11-02 JST session. Research lead 月野テンプレクス.
**Issue24 is CLOSED/completed; Issue25 is the next bounded mathematical target.** This checkpoint is not permission for later nightly work. Dated README/direction and old issue bodies do not restart completed tasks.

## Accepted formal change

PointwiseCover.feasible_count proves, for every natural n,d, that the number of targets admitting the ORIGINAL error1/3 finite REAL mixture of actual GF2 degree<=d polynomials is at most

 2^(sum(j<=min(n,d),choose(n,j))) * sum(j<=floor(2^n/3),choose(2^n,j)).

The proof derives a positive-mass close row from the pointwise hypothesis, reuses the accepted evaluation-preserving squarefree span, bounds its finite-field cardinality, counts binary error sets and takes a finite union. The actual totalDegree predicate and family-before-input quantifiers are unchanged. It does not identify covered targets with feasible targets.

large_of_bound formally proves more-than-half density under an explicit arithmetic bound. A SEPARATE written binomial/induction derivation supplies that bound for every n>=7,d<=1. The unconditional regime, Walsh runtime and following counterfamilies are written results with finite checks, not extra Lean endpoints.

## What changed scientifically

The affine-far property is efficiently recognizable in truth-table length, but the uniform detector misses MOD3 whenever n mod6 is2,3,4 because constant0 is already within the radius. Other lengths can also fail. Independently, the paired quadratic family has linear-size circuits and lies in the affine-far property for every n>=4. Therefore THIS degree-one property's usefulness against P/poly is FALSE, despite largeness and efficient recognition. Neither result refutes the correct one-way count or every possible growing-degree property.

Keep the counting tool; park uniform-cover polishing and the weaker balanced-affine salvage. Next is Issue25, an actual integer modulus amplifier and no-wrap exact accepting-assignment counts for GF2 polynomial blocks, motivated by a known algorithms-to-lower-bounds route. No complete faster algorithm or hierarchy consequence is yet established.

## Actual evidence

Formal source16de2eb187960c770e63114b3dadbb1690f08b3f, treecf6af1365290ec0de32ad25ef619ef2279affbc6; completed SUCCESS run41396234158/job125118052432. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac; --wfail9074 jobs,1347 declarations inside unchanged[propext,Classical.choice,Quot.sound],16 new reports and3 explicit signatures plus all older reports. Actual source/commit/tree, completed states and full decoded output were re-fetched; local source hashes match. No second kernel or independent semantic review is inferred.

Exact source9eb549897f5e227708ac9e7b73a3f72b0e2db237 passed completed SUCCESS run41396010959/job125117369329. Actual Python3.12.3 normal/-O/stored bytes and hashes agree, including exhaustive affine recognition checks on65814 tiny target tables. Actual code/results/workflow/commit and completed output were re-fetched. Finite tests are not general proofs. Full evidence boundaries: ../expeditions/032-covering-recognition/ci-evidence.md.

Continuation0ea0ec1fd5eb1550c457a2c451bf2f5c662bd830 saves scientific audits and LOCAL modulus/block-count checks.390 integer tests and3673 exact block counts pass local normal/-O/compile checks. They are not covered by covering CI or a generic Lean theorem. First next entry: ../expeditions/032-covering-recognition/next-frontier.md and Issue25.

Graveyard056/057/058/059 preserve false semantic shortcuts, both failed formal candidates, the easy-circuit counterfamily and modulus wraparound. No statement or strict audit was weakened. No write/security blocker or unapplied patch remains. Local execution limitations were handled through connected GitHub/Actions.

Previous root-budget/shared-DAG/growing-degree/n>=299 quadratic/n>=7 affine/exact n5..11 results remain intact. General n12 classification, novelty, optimality, independent semantic approval, second-kernel checking, unrestricted separation and barrier escape remain unclaimed. Issues8/15 retain their older scopes. Record-only commits are not new mathematical-source execution evidence.

Previous complete status: history/2026-11-02-pre-covering-status.md, original blobac21e13824a8b36b8ab04df4ec8c2dc5ac0f4c50. Session log: ../logs/2026-11-02-covering-recognition.md. Further work requires fresh approval.
