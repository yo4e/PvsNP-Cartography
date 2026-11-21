---
id: 045-sparse-affine-reads
status: written-derivation-and-finite-evidence
statement: "The specified23-offset GF(128) verifier has exact NO minimum 109, exact uniform signed sensitivity 23 and Q4194304, guaranteeing any 4 physical YES-bit errors."
dependencies: "040 shared B recovery and residual;044 private copy charge;045 source, all-assignment argument and executable checks"
novelty: novelty-unknown
last_attacked: 2026-11-21
---

The minimum ranges over every global physical field/gate/copy/constant/public
assignment for the specified NO instance. The signed sensitivity ranges over
all mixed bit-error sets about every satisfying YES reference. The matching
NO witness and sensitivity singleton are executed; universal bounds are the
written arguments, not finite sampling.

The strict sufficient uniform-error threshold is 109/96,468,992, a128/23
factor over the preceding full-A private compiler at the same Q. The
guaranteed integer error radius is 4. The encoded approximation target has
changed; no low-degree approximating family is supplied.

For the named honest YES proof with zero-filled padding, exact GF(2)
degree 18 on 22 variables and the elementary minimum-weight bound imply
at least 16 errors for every degree 17-or-lower competitor. The existential
uniform-average approximation degree at this threshold is therefore18
for that function. A subsequent downset completion reduces the exact degree
to 17 while preserving all used physical bits. This is optimal over free
padding even under the new error budget: the fixed 21-dimensional subcube
x21=0 has degree 17, forcing at least 16 used-bit errors for every degree
16-or-lower polynomial or fixed mixture. Other satisfying physical proofs
are not optimized. [Completion and bound](../expeditions/045-sparse-affine-reads/padding-bound-notes.md).

[Conclusion](../expeditions/045-sparse-affine-reads/conclusion.md) ·
[Derivation](../expeditions/045-sparse-affine-reads/theory-notes.md) ·
[Attacks](../expeditions/045-sparse-affine-reads/attack-notes.md) ·
[Execution](../expeditions/045-sparse-affine-reads/execution-evidence.md).

The one-level family extension is a written field argument, with only
GF(128) fully compiled here. No new Lean verification, external semantic
review, novelty, barrier escape, unrestricted circuit lower bound or
P-versus-NP result is claimed.
