# Barrier audit: finite n=8 certificate

Date: 2026-10-09. No general circuit lower bound is proposed.

Relativization: the statement concerns 256 Boolean inputs and explicit
GF(2) polynomials, not P/NP oracle classes. No non-relativizing step or
escape from Baker-Gill-Solovay is claimed.

Natural Proofs: no constructive, large property useful against a general
circuit class has been specified. The finite affine certificate is not
a Razborov-Rudich lower-bound method for P/poly. No cryptographic
assumption is silently invoked or defeated.

Algebrization: using GF(2) is not evidence of escaping the Aaronson-
Wigderson barrier. No algebraic-oracle class relation is established.

Immediate coverage audit: the upper bound is existential, so four valid
orbit representatives suffice. The lower bound is universal over the
ENTIRE affine class, and all 512 coefficient choices are checked. We
never generalize a sampled quadratic dual. That failed inference remains
in graveyard/002-n8-sampled-dual-extrapolation.md.

Degree preservation: variable permutations preserve degree; the encoded
representatives include only constant, linear and quadratic monomials.
The lower class covers every polynomial of degree at most 1 over GF(2).

Quantifiers: randomness chooses a polynomial before the input is tested;
pointwise success is required on every input, not an average input.

Disposition: finite certificate survives these scope checks. No broad
barrier escape, asymptotic theorem or novelty claim.
