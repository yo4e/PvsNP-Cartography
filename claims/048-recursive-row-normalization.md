---
id: 048-recursive-row-normalization
status: candidate-survives
statement: For the specified fixed-rate canonical recursive address model, a public inverse shuffle gives polynomially many complete seed rows and fixed-tag signed queries; direct shared row polynomials subsume guessed tag layouts at the same query degree.
dependencies:
  - expeditions/038-recursive-query-fibers/source-compiler.md
  - expeditions/039-unary-overlap-counting/budget.md
  - expeditions/041-two-level-distance/outer-application.md
  - expeditions/047-witness-layouts/sources-and-quantifiers.md
  - Ben-Sasson and Viola TR14-017
  - Viola TR20-015 revision 5
novelty: novelty-unknown
last_attacked: 2026-11-28
---

## Written claims and hypotheses

1. Fix `a>=3` and the Expedition 038 canonical polarity, physical sharing and
   offset-query convention. The inverse shuffle bijects each canonical row
   with the complete `k`-cube. Every fixed-tape offset query has one constant
   row and `z XOR delta`. Row count satisfies the recurrence in
   [normalization](../expeditions/048-recursive-row-normalization/normalization.md)
   and is polynomial in `k` for fixed `a`.
2. For any complete row universe, total used-cell error budget `E`, and freely
   completed unused tags, the least degree in any injective tag layout is at
   least `Delta_E`. The public dense layout has degree at most
   `Delta_E+ceil(log2 R)`. Minimizing over a nonempty satisfying-proof set
   preserves these inequalities.
3. For `R,M=poly(k)` and fixed-row signed queries, direct row polynomials of
   degree `d` describe one shared proof, subsume all degree-`d` tag-layout
   certificates, and produce clause degree at most `3d`. The descriptor and
   counting ledger fits the inherited hierarchy clock for sufficiently small
   fixed `d/(n/log n)`, conditional on the stated compiler and source theorems.
4. Under those compiler/hierarchy hypotheses, infinitely many YES lengths
   have no satisfying witness approximable by such a tuple below the specified
   weighted-error threshold. This is conditional written reasoning, not a
   newly formalized or independently accepted lower-bound result.

## Exact finite evidence

The first genuine two-level case has 64 symbol rows, 16,384 physical symbols
and 1,196,032 direct query comparisons. A separate transport of the actual
GF(256) field fixture preserves all ordered leaf inputs, the shared residual
root and the existing 0/221/221 rejection counts. Named YES raw field rows
are affine; this does not cover all Boolean gate rows.

Independent exact Boolean controls establish the stated 10/5/4 degree
comparison through fifteen used errors, a short invertible-map composition
counterexample, and the explicit padding failure. A tiny exhaustive
row-sandwich checker supplies finite controls for the general written lemma.

## Attack and classification

The lead inspected all programs and derivations. Same-model geometry,
source and skeptical branches shared findings; they are not an independent
external review. The general coordinate/selector arguments are written
derivations, the numerical results are finite evidence, and the external
PCP/counting/hierarchy results remain dependencies. No Lean was run.

[Conclusion](../expeditions/048-recursive-row-normalization/conclusion.md) ·
[Costs and quantifiers](../expeditions/048-recursive-row-normalization/cost-and-collapse.md) ·
[Execution evidence](../expeditions/048-recursive-row-normalization/execution-evidence.md) ·
[Graveyard](../graveyard/2026-11-28-recursive-layout-shortcuts.md)
