# Barrier and statement scope, n10 repair

The only new formal numerical target is MOD3 on exactly10 Boolean variables
over GF(2) at pointwise error1/3. Actual-degree polynomials, REAL probability
normalization and family-before-input quantifiers are retained. A repair to
closed finite proof evaluation is not a new lower-bound technique.

Relativization: no oracle-machine equality or separation is proposed.
Natural Proofs: no large constructive truth-table property useful against
unrestricted circuits is supplied. Algebrization: these finite polynomial
identities are not a non-algebrizing step. None of the three barriers is claimed
escaped. Formalizing a bounded instance does not establish an asymptotic result.

The Lean official reference was consulted to assess decide_cbv and cbv.maxSteps:
https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/
The default-budget CBV experiment failed, and the final proof keeps the original
kernel decision with finite case splitting. No theorem-level literature claim
or mathematical novelty is drawn from the documentation or this optimization.

Formal acceptance is now supported by actual production run39139432083 and its
420-declaration/15-target audits. Independent human semantic review and novelty
remain separate, unfulfilled gates; no P-vs-NP or all-n MOD3 claim is made.
