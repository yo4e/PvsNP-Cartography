# 2026-10-08 — Primary barrier audit

Role: Cartographer / Historian / Skeptic

## Target

Issue #2: replace orientation-only barrier summaries with primary-source theorem/definition audits for relativization, Natural Proofs, and algebrization.

## Sources checked

### Baker–Gill–Solovay

Primary journal record and abstract checked for:

- definition of `P^X` / `NP^X` by deterministic/nondeterministic query machines;
- recursive oracle `A` with `P^A = NP^A`;
- recursive oracle `B` with `P^B != NP^B`;
- publication metadata and DOI `10.1137/0204037`.

### Razborov–Rudich

Primary ECCC TR94-010 checked for:

- introduction of the natural-proof notion;
- conditional general-circuit barrier under a hardness assumption;
- narrower unconditional limitations and `AC^0`-natural-proof discussion.

Operational definitions in the map explicitly use truth-table length `N = 2^n` to avoid the common constructivity-scale error.

### Aaronson–Wigderson

Primary ECCC TR08-005 checked at Definitions 2.1–2.3 and the interactive-proof section:

- Boolean oracle versus extension oracle;
- finite-field extension polynomial agreeing on the Boolean cube;
- bounded multidegree condition;
- asymmetric inclusion/separation definitions of algebrization;
- Theorem 3.7: `PSPACE^{A[poly]} subseteq IP^{A_tilde}`;
- Section 5 barrier statements for P versus NP.

## Attack / correction pass

The old map's high-level claims were directionally sound, but insufficient for an actual proof audit. Main corrections:

1. Relativization is now anchored to the literal oracle constructions, with the “relativizing methods cannot settle P vs NP” sentence explicitly marked as a method-level consequence rather than quoted theorem text.
2. Natural Proofs now distinguishes input length `n` from truth-table length `N = 2^n`, and makes the cryptographic assumption explicit rather than treating the barrier as unconditional.
3. Algebrization now records the asymmetric Definition 2.3 rather than the vague shortcut “does the argument survive algebraic oracle access?”
4. `IP = PSPACE` is used as a diagnostic interaction example: non-relativizing, yet algebrizing.
5. Every barrier now has a concrete expedition checklist and explicit non-consequences.

## Disposition

Issue #2 acceptance criteria are satisfied by the prepared `map/BARRIERS.md` and bibliography replacement.

Repository writes remained unavailable in this unattended session after the earlier write blocker. No further mutation retries were attempted. Files are preserved in the pending bundle for exact later application.
