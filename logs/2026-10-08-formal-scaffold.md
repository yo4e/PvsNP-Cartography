# 2026-10-08 — Initial Lean assumption-audit scaffold

Role: Formalist / Skeptic

Issue: #3

## Goal

Create a minimal Lean environment whose first job is exposing assumptions, not encoding ambitious complexity statements prematurely.

## Environment selected

Fresh Mathlib state inspected on 2026-10-08:

- Mathlib master commit: `9e6b3aac99b624d10c84653ab9c5357283b9b3b8`
- matching `lean-toolchain`: `leanprover/lean4:v4.35.0-rc4`

Both are pinned explicitly in `formal/`.

## Vocabulary boundary

The first formal layer intentionally stops before P, NP, machines, circuits, or polynomial-time reducibility.

It defines only:

- languages as predicates;
- semantic membership-preserving maps;
- fixed-length Boolean functions;
- finite disagreement counts.

This avoids giving a complexity-theoretic name to a definition that lacks the necessary resource bound.

## Sanity targets

Four small theorems test identity/composition and disagreement-zero behavior.

They are infrastructure checks, not complexity results.

## Assumption attack

Two complementary mechanisms are installed:

1. namespace-level compiled-environment axiom audit in CI;
2. explicit `#print axioms` commands for named theorem targets.

CI also builds with `--wfail`. A theorem that elaborates through `sorry` / `admit` must not be promoted merely because the file compiles.

## Verification caveat

The research runtime used to prepare this scaffold does not have Lean/Lake installed locally.

Therefore the commit itself is **not** evidence that the Lean files compile. The GitHub Actions run triggered by the commit is the verification step. Until it passes, status remains scaffold-pending-verification.
