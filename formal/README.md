# Formal scaffold

Status: **infrastructure / sanity lemmas only**

This directory exists to make assumptions visible before theorem-level complexity claims are attempted.

It does **not** formalize P vs NP, a circuit lower bound, or polynomial-time reducibility.

## Pinned environment

The initial scaffold is pinned to the Mathlib state inspected on 2026-10-08:

- Lean: `leanprover/lean4:v4.35.0-rc4`
- Mathlib: `leanprover-community/mathlib4@9e6b3aac99b624d10c84653ab9c5357283b9b3b8`

The Mathlib revision is a commit SHA rather than a moving branch name.

## Current formal vocabulary

### `Language α`

An abbreviation for `α → Prop`.

The carrier type is explicit. No encoding size, decidability, machine model, or complexity bound is implied.

### `ReducesVia A B f`

Means only:

```text
∀ x, A x ↔ B (f x)
```

This is a semantic membership-preserving map. It is **not** a polynomial-time many-one reduction. Calling it one would hide exactly the assumption this scaffold is meant to expose.

A genuine complexity-theoretic reduction will require a formal machine/computation model and an explicit resource bound.

### `BitVec n` and `BoolFn n`

Small aliases for fixed-length Boolean inputs and Boolean functions.

### `disagreementCount f g`

Counts finite inputs on which two Boolean-valued functions differ.

It is not approximate degree, has no probability distribution, and has no built-in error threshold.

## Sanity theorem targets

`PvsNPCartography/Sanity.lean` currently proves only infrastructural facts:

- identity preserves language membership;
- membership-preserving maps compose;
- a Boolean function has zero self-disagreement;
- pointwise equal Boolean functions have zero disagreement.

These are theorem-level Lean declarations, but they are deliberately mathematically modest. Their purpose is to test the environment and assumption-audit pipeline, not to manufacture impressive theorem names.

## Assumption policy

Project-specific `axiom` declarations are not allowed in promoted formal claims.

The CI axiom audit uses the Lean action's standard foundational allowlist:

- `propext`
- `Classical.choice`
- `Quot.sound`

A target theorem depending on any additional axiom, including `sorryAx`, fails the axiom-audit job.

The explicit target list is also inspected with:

```bash
./scripts/axiom_report.sh
```

which runs Lean's `#print axioms` commands from `PvsNPCartography/AxiomAudit.lean`.

The actual initial axiom report is not claimed until CI has run successfully.

## CI checks

`.github/workflows/lean.yml`:

1. builds the pinned Lake project;
2. treats Lean warnings as failures via `--wfail`;
3. runs `leanprover/lean-action`'s compiled-environment axiom audit on the `PvsNPCartography` namespace;
4. runs the explicit `#print axioms` report.

This is stronger than grepping source text for `sorry`: it audits dependencies in the compiled environment and can detect hidden project axioms.

## Informal-to-formal mapping

| Informal phrase | Current formal object | Important omission |
|---|---|---|
| language | `Language α` | no encoding or decidability assumption |
| reduction via a function | `ReducesVia A B f` | no computability or polynomial-time bound |
| n-bit Boolean function | `BoolFn n` | no circuit representation or size measure |
| finite disagreement | `disagreementCount f g` | no distribution, error threshold, or polynomial approximation |

This table is part of the formal contract. If an informal research claim requires an omitted condition, the formal statement must be extended rather than silently reading the condition into the name.

## Promotion rule

A compiling file is not enough.

Before a formal result is promoted in this repository:

1. compare the formal statement to the informal claim;
2. inspect `#print axioms`;
3. require CI to pass;
4. identify any imported theorem carrying substantive assumptions;
5. record the correspondence in the relevant claim/expedition file.

The next complexity-theory definitions should be added only when a concrete theorem reconstruction requires them.
