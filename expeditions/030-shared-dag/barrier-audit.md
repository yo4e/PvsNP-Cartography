# Barrier audit: actual bounded nonlinear-depth circuits

Target: a concrete finite GF2 randomized-polynomial approximation for shared
NOT/XOR/AND/OR DAGs, followed by the known-method MOD3 degree obstruction.
This is not a proposed unrestricted P-versus-NP separation.

Relativization: the gate induction is for the specified finite gate alphabet.
An arbitrary oracle gate has no provided degree/error lemma; adding it is a
missing implication, not an allowed extension. No arbitrary-common-oracle
class separation or certified nonrelativizing escape is claimed.

Natural Proofs: obtaining a restricted-model bound does not establish usefulness
against P/poly. For a broad lower-bound extension, the induced truth-table
property, its constructivity and largeness must be extracted and checked under
the barrier's cryptographic hypotheses. Those checks have not been supplied
for an unrestricted extension. No automatic escape is inferred from randomness.

Algebrization: using GF2 polynomials does not demonstrate non-algebrization.
No asymmetric algebraic-oracle extension of the full P-vs-NP route is proved.
An unspecified oracle/algebraic gate cannot be substituted for the proved
finite gates. Escape status for a broad extension remains unknown.

Scientific decision: finishing this bridge would close the explicit restricted
circuit consequence already selected in Issue22. It would not remove the
unbounded nonlinear-depth limitation. The next research choice should address
a named mathematical gap rather than count files or CI declarations.
