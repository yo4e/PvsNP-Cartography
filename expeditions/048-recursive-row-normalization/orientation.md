# Expedition 048 — normalize recursive addresses before pricing layouts

Session: November 28, 2026 JST, fresh approval in the existing PvsNP research
conversation. Source checkpoint: `ba1da266a3e51f4025b7ba4f00d305b94796cbff`.
Research lead: 月野テンプレクス. Issue: #37. Status at opening: exploratory.

## Mathematical question

Expedition 047 allows a nondeterministic algorithm to guess one globally shared
row-label table, but the growing one-level compiler has too many rows to write
that table within the hierarchy clock. The actual fixed-rate recursive source
has a different geometry. Does it have polynomially many constant row identities
after a PUBLIC reorganization of the coordinates, and if so does guessing their
labels buy more than a small degree saving?

There are exponentially many actual tree nodes. Merely fixing the path shape
does not fix their labels: those labels still contain seed bits. Our constructive
candidate instead unshuffles all retained path labels and the live coordinate
back into a root-coordinate word, leaving only the fresh coordinates in a row
tag. A row in this representation runs across many physical tree nodes.

## Bounded targets and exit condition

1. Derive a bijection on canonical physical cells, and a normal form for every
   fixed-tape offset query, preserving root, parent and column-to-row aliases.
2. Exhaust the first genuine two-level geometry, fixed `a=3, k=8`, and test
   larger mixed row/column paths at the symbolic-coordinate level.
3. Charge an explicit guessed row map, polynomial coefficients, query
   substitution, exact counting, padding and approximation precision together.
4. Attack the alleged advantage: compare adaptive labels with ordinary per-row
   polynomials, and refute the separate shortcut from a short general circuit
   description to low substitution degree.
5. Decide whether layout search remains the right mathematical frontier.

The finite geometry is not a complete ACSP instance, a generated Boolean
verifier, a new numerical soundness constant, or a residual-constrained witness
construction. The source-level extension to symbol bits, two trees, seed pins
and gate rows is a written conditional argument using Expedition 038.

## Work division and independence

The lead read the operating contract, required documents, current Issues,
recent commits and primary sources. Three same-model branches separately
investigate constructive geometry, composition/cost attacks, and source
semantics. Findings are shared during the session. This is internal adversarial
work, not the independent review requested by Issues #8 or #15.

No new Lean execution, novelty, external review, general circuit lower bound
or P-versus-NP separation is assumed or claimed. A natural milestone is either
a costed normalization with a precise remaining witness condition, or a
counterexample that rules it out.
