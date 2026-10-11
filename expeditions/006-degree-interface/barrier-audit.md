# Barrier and scope audit

Target: connect a fixed n=5 certificate to a degree-based formal definition.

Relativization: no relation between oracle complexity classes is asserted.
The structural degree-one normal form is ordinary polynomial algebra, not a
non-relativizing ingredient in a P-vs-NP argument.

Natural Proofs: no large constructive property useful against a circuit class
is proposed. No cryptographic assumption is removed or circumvented.

Algebrization: using GF(2) and polynomial degree does not demonstrate a barrier
escape. No algebraic oracle framework or complexity-class separation is involved.

The immediate risks are instead representation coverage, quantifier order,
probability normalization, support degree, and confusing polynomial equality
with evaluation on too small a subset. These are attacked explicitly in the
source, semantic audit, and graveyard/005-input-dependent-polynomial.md.

The normal-form lemma ranges over arbitrary finite variable types and
commutative semirings by a structural proof. That is not an extrapolation of
the finite MOD3 data, which remains restricted to the stated input sizes.
No new finite value or novelty claim, and no P-vs-NP conclusion.
