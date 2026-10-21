# Expedition 022: certified weighted Hamming-layer profiles

Research lead: 月野テンプレクス. Fresh user approval for one session, 2026-10-21 JST.
Starting main: 0e30b5b708931be5e6d181d63a684381ebe4ee58. Open Issues: #8, #14, #15.
Read live AGENTS.md, its five mandatory documents, current status, recent commits,
and logs/2026-10-21-balanced-fibers-and-intersections.md. Completed #9..#13 are
not to be repeated. Issue #14 is the earliest useful unblocked implementation.

## Target
Use the accepted Boolean intersection counts to prove arbitrary-real weighted
Hamming-layer sums and means, with exact normalization and empty-layer scope.
Then encode actual GF(2) clique-subset polynomials, prove totalDegree bounds and
evaluation identities, and connect their MOD3 correctness to short profiles.
Existing n11 seeds are regression cases, not a new degree theorem or a reason
to start an unbounded staircase of numerical certificates.

## Acceptance / attack
Keep the family-before-input quantifiers, integer overlap ranges and the full
permutation-to-pointwise bridge. Test signed functions, empty/full subsets,
impossible layers, constant terms, duplicated ordered edges in characteristic
two, and missing normalization. Formal acceptance requires an actual completed
pinned Lean --wfail build, unchanged axiom allowlist and explicit target reports.
Re-fetch source, commit and results before reporting success. Preserve failures.

## Review provenance
Gemini's Issue #15 report and addendum have been discussed with the steward.
They are an independent AI semantic review of the pinned PREVIOUS checkpoint,
not a local Lean rerun, second kernel, human review, or review of new code here.
Do not relabel the new work as independently reviewed merely by importing it.

## Environment
Local git network attempt failed: github.com cannot resolve. lean/lake are not
installed locally. Connected GitHub is the available repository/Actions route.
This orientation write is the actual write-capability check; its acceptance is
not mathematical evidence. No paid resources or new scheduled work requested.
