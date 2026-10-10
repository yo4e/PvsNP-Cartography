# Night research checkpoint: 2026-10-10 (JST)

Research lead: 月野テンプレクス. One explicit approval for this session.
Starting head: 376e3d6d6b13201251da7643ba56e7d13a7a96c8.
Read AGENTS.md, all five mandatory documents, current open Issue #8,
latest commits and the previous night/expedition research logs.

## Observe, orient, act and verify

The earliest unblocked task was Issue #8's n=5-first formalization.
Implemented the complete five-bit cube and affine coefficient type, exact
integer input distribution and deterministic lower certificate in Lean.
Applied the already-verified real-mixture duality lemma after proving all
its concrete premises. Commit b29ddcd70237ea87723890e8d9316a3c3f69f201
passed run 38054660994, job 114220548862.

## Continue, attack and repair

Expanded the original quadratic orbit to 30 explicit formulas. Lean proves
at least 21 agreements at every input, connects the finite evaluator to
actual MvPolynomial objects over ZMod 2 and proves totalDegree <=2.
The initial upper commit fcbe841f60feb3d4f3db8f2b0ba887e770b7b31a failed
run 38054868045 only because of an unused simp argument under --wfail.
Commit 782979d0ade9359107c9a576d055895a5b08c084 removed that redundant
argument without weakening the theorem, warnings policy or axiom audit.

Added a correctness/evaluation bridge for arbitrary finite real-weighted
affine polynomial families, including duplicates. Attacked input versus
layer quantifiers, coefficient coverage, field equality and normalization.
A deliberately weakened duality claim omitting sum(q)=1 was refuted by a
singleton zero-mass countermodel. Constant flips and loss of randomization
also fail. These controls are not portrayed as previously believed claims.

## Actual final verification

Code commit: 0150b8642ed5708b8ce3109c6d85fc0d4f5e7872.
Formal run 38055370947 / job 114222616643: success under pinned Lean
4.35.0-rc4 and Mathlib 9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Build --wfail, all 64 namespace declarations within the foundational axiom
allowlist, and explicit target #print axioms reports passed.
Semantic run 38055370864 / job 114222616310: success in normal and
optimized Python, reproducing lower 11/18, upper 7/10, uniform orbit
multiplicities, two evaluators and all three negative controls.
Actual completed-job logs were fetched, not inferred from upload success.

Source files and commit were re-fetched; locally inspected bytes matched:
Mod3Five.lean: 7f3f49d34e328ff462955a26b91f61844ae3f647
Mod3FiveUpper.lean: c25c67c4a886d19aea0b128c839aa8a891463871
Mod3FiveBridge.lean: b4e59abf75c1e1a329592509c9107504cd4a5816
audit.py: c6f4105670115646d7477ff1c996cada0bf767c1

## Classification and next frontier

Concrete n=5 formal components are verified, but the generic normal-form
map from any totalDegree<=1 MvPolynomial to the affine coefficient type
and the abstract probabilistic-degree equality are not yet integrated.
The direct upper proof does not require an unproved symmetry premise.
Issue #8 stays open; next prove that normal-form bridge, package the
faithful degree-based statement, then extend to n=6 and n=7.
No new finite value, novelty, minimal-support, general-n or P-vs-NP claim.
No independent human reviewer or extra proof kernel was used.

Primary definition and official Lean/mathlib API documentation were consulted.
This is a reconstruction of existing certificate data, not a novelty search.
GitHub writes worked. Local Lean/Lake was unavailable, so actual formal
execution was in GitHub Actions. No credentials, paid resources or external
publication/submission were requested. The only observed code failure was
the strict unused-argument warning, now repaired. This is a natural checkpoint.
