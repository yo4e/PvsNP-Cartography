# Barrier and scope audit

Target: an agreement bound for genuine total-degree-D polynomials on a two-point
nonzero field grid, and an author-reconstructed probabilistic-degree application.
This is reconstruction of the known algebraic approximation method, not a new
route claimed to separate unrestricted P and NP.

Relativization: no oracle simulation or non-relativizing step for a complexity-
class separation is supplied. The finite-field lemma is not an oracle barrier
escape certificate.

Natural Proofs: no constructive/large property useful against general circuits
has been extracted or proved. The restricted polynomial bound is not a general
circuit bound, and no cryptographic assumption is used or refuted here.

Algebrization: using extension fields does not prove non-algebrization. No
Aaronson-Wigderson oracle-extension analysis establishing an escape is claimed.

Actual scope boundaries: a,b must be nonzero; distinctness is needed for the
2^m input cube/interpolation. GF(2) itself has only one nonzero element; the
MOD3 adapter explicitly passes to GF(4). Degrees are total degrees of actual
polynomials. Probability weights live in R, not GF(4). Sampling is independent
across15 repeats and fixed before input. Union bounding the two residue errors
does not require their independence. An input-average lower bound alone cannot
be restricted to an arbitrary fixed subcube while retaining its error rate;
our restriction uses the original pointwise probabilistic guarantee instead.

A size/depth/error-preserving circuit-to-polynomial construction is still needed
for a circuit lower bound. No such new construction or P-vs-NP theorem is included.
Disposition: useful restricted known-method reconstruction, no barrier escape.
