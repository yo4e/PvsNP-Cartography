# Night research checkpoint: 2026-10-09 (JST)

Research lead: 月野テンプレクス. This session followed the user's explicit
approval for this night only. Previous approvals were not reused.

## Observe and orient

Read AGENTS.md, all five required documents, current open Issues #7/#8,
latest commits, prior session log and expedition 003's research log.
Starting head: 50706acbd05b511a79f3b6883c847d59ed4b07f7.
The earliest unblocked target was the exact n=8 MOD3 value.

## First loop: resolve the finite n=8 target

Heuristic column generation supplied candidates, then a numerical
integer-weight search simplified a successful witness to four orbit
representatives mixed 1:3:4:4. None of the floating optimizer values was
used as a universal lower bound or final certificate.

Exact result: pdeg_(1/3)^GF(2)(MOD_3^8) = 2.
Upper: each input receives success >=2/3 from the four degree-two orbits.
Lower: a half-weight-1/half-weight-3 input distribution bounds all 512
affine polynomials by 9/14. Arbitrary real mixtures inherit that bound.

Verification included exact fractions, full truth tables, a second
polynomial evaluator, a hypergeometric affine check, and every permutation
at every input. Six negative controls passed. In particular, dropping
permutation randomization gives success only 1/12 at x=14. This deliberate
semantic mutation is preserved in graveyard/003-n8-without-symmetrization.md.
It is not portrayed as a previously believed conjecture.

Core commit: 7355f4e5b826a1b34e0f48d891c208495c821cca.
CI: run 37940070467, job 113851891080, success on CPython 3.12.15.
Files, commit, and actual job output were fetched and checked. Certificate
and verifier blobs matched the locally executed files. Full discovery
sources, parameters and limitations are retained in expedition 004.

## Second loop: formalize the finite dual bridge

Added PvsNPCartography.finite_dual_obstruction over real probabilities.
It proves the finite weighted-average contradiction, with explicit
normalization, nonnegativity, deterministic-row bound and strict gap.
Its finite type I need not represent all polynomials unless that coverage
is separately established. This is deliberately visible in the statement.

Commit: 97c459e04204b35f970f58b8cbab959986daa98e.
CI: run 37940286899, job 113852624241, success under pinned Lean/Mathlib,
--wfail, namespace axiom audit and explicit #print axioms.
All 11 namespace declarations passed. The new lemma depends only on
propext, Classical.choice and Quot.sound. Actual output is retained in
formal/reports/2026-10-09-finite-dual-axioms.txt.
The remote theorem source and its commit were re-fetched and reviewed.

## Claim discipline and prior art

The n=8 certificate is finite and exact, with algorithmically different
checks and a separate CI runner; this is not independent human review.
No novelty, general n formula, global mixture-success optimum, minimal
orbit-support size, P-vs-NP resolution or barrier escape is claimed.
The MOD3 statement itself is NOT Lean-verified. Only the generic bridge is.
Primary definition pages and later symmetric-function context were checked;
a limited exact-table search did not establish novelty.

## Issue disposition and next frontier

Issue #7's finite target and exact-checking acceptance requirements are
completed at this checkpoint. It can be closed once the full expedition
record is committed and re-fetched. Issue #8 stays open with the verified
generic bridge recorded as progress, not a completed MOD3 formalization.

Next: apply that bridge to a faithful complete polynomial encoding, starting
with n=5 as Issue #8 requests, then formalize the upper symmetrization.
A future n=9 expedition must obtain fresh witnesses or complete lower
certificates; nothing about n=9 follows by extrapolating the n=5..8 table.

## Operational boundary

GitHub reads and writes succeeded through the connector; no authorization
or safety-layer write blocker remained. This local runtime had no Lean/Lake
and could not clone via its network, so the actual formal check was run in
GitHub Actions. No paid compute, external submission or credential change
was made. Remaining work is mathematical/formal coverage, not a claim that
the current n=8 finite certificate remains undecided.

This is the natural stopping point for the authorized session.
