# Barrier and quantifier audit

- Target: cost and encoded degree of a designed one-level verifier family. No P/NP relation is established.
- Relativization: no class separation is inferred. The finite-field geometry and explicit known witness do not provide an oracle-lifted general proof. No barrier escape is claimed.
- Natural proofs: no Boolean-function property that is constructive, large and useful against a circuit class has been established. The counting obstruction below is about representational capacity of fixed tags for arbitrary row constants, not a circuit lower-bound property.
- Algebrization: no oracle extension analysis for a class relation is supplied. Use of finite-field algebra alone does not avoid the Aaronson-Wigderson barrier.
- Uniformity: the low-degree layout is computed from the explicit YES proof, then held fixed. A compiler for general instances cannot assume access to an unknown witness's row signatures. In addition, the gate counts here are polynomial in N=2^k, not automatically polynomial in a source instance's bit length. The public YES/NO fixtures are designed, so an exact low-degree representation does not imply a nontrivial decision algorithm.
- Soundness: one global physical assignment, arbitrary noncode roots and dishonest auxiliary cells; no resampling per query. Reindexing is injective and keeps all signed projections and clamped pins. The universal lower bound is a written argument, not a finite scan.
- Approximation: the strict raw-bit budget follows from an unrestricted signed sensitivity. Exact degree over free padding is established only for the named compact references at a=3,4; a different structured completion is an upper bound, not an optimum over all layouts or all witnesses.
- Review: no new Lean kernel run, external review or novelty assessment. The standard polynomial distance proof and counting obstruction are explicitly derived. The primary source BV14 is prior-art context, not certification of the changed compiler.

Disposition: scoped constructive result plus a failed unrestricted uniformity generalization. Next #36.
