# Failed direction — RS membership alone makes every satisfying proof easy

Claim: the shared RS code-check structure in the growing cross verifier
guarantees that every satisfying proof admits degree O(log k) at O(s) absolute
errors under one public polynomial-storage layout.

Attraction: each row belongs to a small univariate code, and the named
reference has low seed degree and a good coefficient-tag encoding.

Failure: a code-only relaxation, retaining actual shared row/column geometry,
admits every degree-less-than-2s root B. The first 2s field symbols give 2sk
independent systematic bits. Degree O(log k) polynomials on O(k) address bits,
even enlarged by radius O(s) Hamming balls, cover only a vanishing fraction
of these patterns for sufficiently large k. This supplies hard **satisfying
code-only witnesses**, not arbitrary unattested row assignments.

Explicit control: at GF(128), B=X^3 extends to the shared code geometry but
its first 112 used raw bits at the original tags have exact nearest affine
distance 42. The arbitrary-fixed-layout counting bound is a separate claim.
See [the derivation and data](../expeditions/047-witness-layouts/scoped-rs-obstruction.md).

Scope: the original designed YES proof is unique, and the relaxation removed
its outer residual constraint. No original NO gap, mixed-error coefficient,
or exact gate census is inherited. Easy code-only witnesses remain, so this
does not refute the existence of one useful witness per YES instance.

Lesson and salvage: use residual-constrained witness structure, a proved
small public symbolic dictionary, or a fully costed succinct guessed layout.
Do not infer a universal low-degree guarantee from code membership alone.
