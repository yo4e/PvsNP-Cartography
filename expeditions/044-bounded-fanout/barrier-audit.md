# Prior art, assumptions, and barriers

The encoding starts from [Ben-Sasson and Viola, *Short PCPs with projection
queries*, ECCC TR14-017, Lemma 1.6 and Section 6](https://eccc.weizmann.ac.il/report/2014/017/download/).
Lemma 1.6 already stores the values of a computation in private queries `(z,i)`
to make the verifier's decision a 3CNF. We reuse that interface. The new copy
rows have the same form, and the old field queries retain their signed
projections. No claim is made that copying wires or bounding occurrences is new.

[Haviv, Regev and Ta-Shma, *On the Hardness of Satisfiability with Bounded
Occurrences in the Polynomial-Time Hierarchy*, Theory of Computing 3 (2007),
45–60](https://theoryofcomputing.org/articles/v003a003/v003a003.pdf) is a primary
comparison for bounded-occurrence reductions and their graph constructions.
Our private trees preserve one violated clause at each rejecting center. They
do not supply the expansion-based preservation of a constant fraction of all
original clauses. The proof here counts the actual raw violation minimum and
actual signed sensitivity, with its own hypotheses.

The targeted search checked the BV14 compiler step and this bounded-occurrence
paper. It does not establish priority or exhaustive novelty. All model-specific
deductions remain `novelty-unknown`. The weighted-buffer argument is an explicit
finite Boolean/minimum-cut derivation, not an imported PCP impossibility theorem.

The larger route still needs an adequately approximable encoded proof function
and a useful counting advantage at the resulting precision. Reducing the
compiler's error loss supplies neither. Relativization is not escaped: no
nonrelativizing separation step is supplied. No constructive large useful
property is established against general circuits, so no Natural Proofs escape
is claimed. Finite-field operations and projection substitutions do not by
themselves overcome algebrization. See the standing [barrier map](../../map/BARRIERS.md).

The exact GF(128) counts are finite computational evidence with explicit
replay. The general fanout and weighting statements have written mathematical
arguments and separate agent attacks. Neither is a new Lean result, independent
human semantic review, a general lower bound, or a P-versus-NP separation.
