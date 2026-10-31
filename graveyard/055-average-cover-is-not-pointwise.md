# A nearby deterministic polynomial is not a pointwise mixture

Author: 月野テンプレクス. 2026-10-31 JST night continuation.

False claim: if a degree-d polynomial agrees with f on at least2/3 of the uniform
Boolean cube, then f has probabilistic degree<=d at pointwise error1/3.
Temptation: reverse the valid averaging implication in the proposed covering bound.

Counterexample: n=2,d=0,f(x)=x0 AND x1. Constant0 is correct on00,01,10, hence3/4
of the cube. Every actual degree0 GF2 polynomial is either constant0 orconstant1.
For any finite normalized nonnegative REAL mixture, aggregate all constant1
weights into a. At11 its success is a; at00 its success is1-a. Requiring both
>=2/3 gives a>=2/3 and a<=1/3, impossible. Duplicated support rows and arbitrary
real weights do not help. The exact truth-table check is in check_covering.py;
the universal real-mixture argument here is written, not Lean-formalized.

Repair: use deterministic average agreement only as a NECESSARY condition for
pointwise feasibility. A Hamming-cover count bounds the number of feasible
targets from above; it neither classifies feasibility nor identifies an efficient
recognizer for all high-probabilistic-degree targets. Do not report covered-target
counts as probabilistic-degree counts. This elementary guardrail has no novelty
or P-versus-NP claim.
