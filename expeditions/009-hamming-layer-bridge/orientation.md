# Expedition 009: Hamming-layer disintegration and the n=8 benchmark

Approval night: 2026-10-14 JST. Author: 月野テンプレクス.
Starting commit: 8e06e7aeba868ce80cd3792bbce4a9bf1530e502.
Read AGENTS.md, all five mandatory documents, current open Issues, three latest
commits and the 2026-10-13-night-full-symmetrization log before substantive work.
Only open Issue #8 selects the layer-counting bridge as the next unblocked task.

Roles: cartographer, formalist, experimentalist, skeptic and archivist, all
performed by the same author. No independent human review is implied.

## Target and acceptance

For any n and Boolean input x of weight w, prove that averaging an arbitrary
real-valued g over all variable permutations equals its uniform mean over the
whole weight-w layer. Prove layer cardinality choose(n,w), full coverage, and
exact fiber multiplicity w!*(n-w)!, including n=0 and extreme weights.
Retain genuine polynomial degree, GF(2) evaluation, real nonnegative normalized
probabilities and one family before every input when applying the identity.

Then connect the existing four-seed n=8 certificate from Expedition004 to the
unchanged probabilistic-degree predicate. The finite value is already known in
this repository; neither a new value nor novelty is the target.

## Method

Use explicit Boolean-input/subset and equal-weight permutation bijections.
Derive the averaging identity by double counting and group invariance, rather
than embedding a factorial-sized permutation enumeration into every application.
Derive exact fiber counts from indicator functions and the factorial/binomial
identity. Cross-check small cases by exhaustive enumeration, reject biased or
incomplete permutation families, and preserve genuine failed inferences.

## Execution boundary

The local container has Python3.13.5 but no Lean/lake and cannot resolve GitHub
DNS. Formal execution uses the repository's existing GitHub Actions workflow.
All source candidates remain unverified until actual --wfail and axiom-audit
output is inspected. Record failed builds without weakening definitions or
allowlist. Re-fetch commits, files and results before reporting saved success.
