# Completed production acceptance and source correspondence

Approved 2026-10-21 JST session. The actual execution took place during the
Japanese afternoon, not at the recurring prompt's nominal 22:00 hour.

Code598d54ed0940a331650b7e7eb733d62c9b6e40ab, tree
a9f26fbece775a5ad11e5cc8b84b5d31dac22341 passed completed SUCCESS
run39547776930/job119049747106. The complete actual job log was fetched;
its pinned Lean4.35.0-rc4, Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8,
--wfail9050-job build,639-declaration namespace allowlist and12 new explicit
target reports are recorded with original timestamps in axiom-report.txt.
Only propext, Classical.choice and Quot.sound occur in the audited dependencies.
Previous numerical and generic obstruction reports also completed. No source
warning, missing premise or unallowed axiom was waived to obtain acceptance.
The separate post-job Node.js action deprecation warning is not a Lean warning.

## Re-fetched exact source

Both complete source files were re-fetched at the accepted immutable commit.
The actual Git commit was then fetched and its tree/parent matched the write.
Local source bytes hash to these same Git blobs and SHA256 values:

| Source under formal/PvsNPCartography/ | Git blob | SHA256 |
|---|---|---|
| BalancedAffineFibers.lean | 25445a5d2bd6f38de932cf7b2d934ae7942adb38 | d72452628ac1ef133e4e69e61f79ce8bec30e1bd7298c1410b6e9f795e9b0374 |
| HammingIntersections.lean | 21065c45b75967971b19a0c852cf85a685c57c77 | e82185e0639a03e502cee7bb46d867e389027f7403441fda2ed0bfc9ca5a4500 |

The final statements were inspected for actual bits/ones representation,
existing inputMass rather than a substitute definition, full fiber sums,
nonzero denominator hypotheses, arbitrary real score functions and the r<=w
range guard. No desired-count assumption or finite enumeration supplies the
generic cardinality theorem. No sorry/admit or unchecked native decision is
present in either new source. See statement-audit.md for dependency direction.

## Separate finite evidence and failed candidates

Exact code da8538d3 passed run39546665458/job119046262844; actual normal/-O
output equals saved result.json. See ci-finite-evidence.md for its strictly
bounded scope, re-fetched verifier/result and actual execution excerpts.
Those numerical checks are complementary, not the source of the all-arity proof.

The initial code9abc8c23 failed run39546373832/job119045364935. The repair
2404af3d failed run39547284945/job119048214934 in one conditional proof; the
intersection module alone had built but was NOT promoted before the whole
root and both audits passed. Full logs of both failed attempts were inspected;
graveyard026/027 preserve the implementation failures and faithful repairs.

Independent human semantic review (#8), a second proof kernel and novelty
assessment remain absent. Another execution environment does not supply them.
