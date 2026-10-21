# 2026-10-21 JST: explicit input probabilities and generic overlap counts

Research lead 月野テンプレクス. One freshly approved session, actual execution
in the Japanese afternoon. The recurring request's22:00 wording is not a
claim about execution time. Starting main17b8c784c99075f3e9368e254d274dbf5720f30d.
Read live AGENTS/all five mandatory docs, open8/13, commits/logs and actual
formal definitions. Generic #12 was already complete and was not redone.

## Results

1. Existing balanced inputMass now has a proved closed formula for n>=3:
   1/(2n) at weight1,1/(2 choose(n,3)) at weight3,0 elsewhere. The proof counts
   one singleton and six distinct ordered-triple fibers, preserving zero mass
   on repeats. Arbitrary real expectations equal half of each layer mean.
2. At every natural arity, actual w-subsets/Boolean inputs with overlap r in
   A are counted by choose(|A|,r)*choose(n-|A|,w-r) if r<=w,0 otherwise.
   Explicit split/union and bits/ones bijections prove the result; empty and
   impossible cases are not discarded. The wrong unguarded formula has a
   formally checked counterexample n1,w0,r1: actual0,wrong1.

## Actual acceptance and complementary tests

Accepted code598d54ed0940a331650b7e7eb733d62c9b6e40ab, tree
a9f26fbece775a5ad11e5cc8b84b5d31dac22341. Completed SUCCESS formal39547776930/
job119049747106: pinned Lean4.35.0-rc4 and Mathlib9e6b3aac, --wfail9050 jobs,
639 namespace declarations and12 new explicit reports, all inside the unchanged
[propext,Classical.choice,Quot.sound] allowlist. All prior reports also pass.
Full actual log, complete sources and exact commit/tree re-fetched and checked.

Re-fetched source blobs:
BalancedAffineFibers.lean25445a5d2bd6f38de932cf7b2d934ae7942adb38;
HammingIntersections.lean21065c45b75967971b19a0c852cf85a685c57c77.
Accepted record3e464878 stores the actual timestamped axiom-report.txt,
re-fetched blob102ce578e960de6a858ae18964fac1f3cc48ff3b, and statement/source audits.

Exact code da8538d3d04ac64d228987c060563602fd609784 passed actual SUCCESS
39546665458/job119046262844, reproducing8191 fiber inputs n0..12,6084 triple
samples,30 signed/nonsymmetric expectation tests and1,398,101 subset pairs
n0..10 with251,902 histogram cells. Normal/-O outputs are byte-identical and
actual JSON equals saved output. Verifier/result/commit were re-fetched.
These bounded checks were not used as a general theorem. See Expedition021.

## Attacks, failed builds and faithful repair

Omitting r<=w returns1 for an empty impossible slice. Dropping sixfold triple
mass leaves total7/12. At n2 there is no triple layer and total mass is1/2;
this refutes normalization, not every empty-layer mean identity. All three
scoped failures remain in graveyard025.

First formal9abc8c23/run39546373832 fails conditional elaboration and warnings.
Second2404af3d/run39547284945 builds the intersection module but fails one
fiber conditional proof; no partial build is promoted. Both completed logs
were read, preserved in graveyard026/027. Final598d54ed explicitly rewrites
the conjunction. Definitions, statements, ranges, probabilities, --wfail and
axioms remain unchanged. Final whole-root and both audits pass.

## Successful commits and Issues

657d8b1cdfb14865e43ed3e56181c67d9e418cd6: orientation and real write check.
9abc8c23cdc6e99e105d052cf75c0fe4aed247ae: first fiber candidate, rejected by Lean.
da8538d3d04ac64d228987c060563602fd609784: bounded exact verifier/result/CI/attacks.
2404af3d4b73e82f8f139d922db5a9b4bfa9bc40: generic intersections and first repair.
6ca1b5296c78c9d5fb3127b294d61d79de9e15d0: exact CI evidence and candidate audit.
598d54ed0940a331650b7e7eb733d62c9b6e40ab: accepted final proof implementation.
3e4648780daa22655fcb646e792f5cefa3111013: acceptance evidence and claim promotion.
This log is in a final record-only commit, whose hash is not self-embedded.

#13 CLOSED as completed; #14 CREATED/OPEN for weighted overlap sums and faithful
polynomial layer profiles; #8 UPDATED/OPEN for independent human semantic review.
Previous README and assumption ledger are archived byte-identically, not lost.

## Frontier and limits

Next approved session: use accepted overlap counts to prove arbitrary-real
weighted layer sums/means, then actual GF(2) clique-quadratic evaluation and
short certified profiles. Existing n11 seeds provide regression tests; do not
redo completed n5..11, generic n>=7 obstruction, fibers or intersection counts.

No GitHub write blocker or unapplied patch remains. Local Lean was absent;
Actions provided actual formal execution. Human semantic review, a second
proof kernel and novelty assessment remain absent. This is standard counting
reconstruction, not claimed new mathematics, optimal support, n12 equality,
arbitrary-n degree2 upper bound, barrier escape or a P-vs-NP solution.
End this session at the completed generic representation/counting milestone.
Future research still requires fresh approval.
