# Expedition 006 research log

Approval night: 2026-10-11; execution crossed into 2026-10-12 JST.

Observe/orient: followed the single open Issue #8's n=5-first plan, after
reading the operating contract, mandatory documents, recent commits and log.
Starting head 845eceb717bc498f1bfe8cccaa0e9a4d7ea757b3.

Act: wrote a generic degree-one structural normal form using finite exponent
multisets and coefficient extensionality; connected actual ZMod 2 coefficients
to the canonical affine evaluator. Initial candidate commit 6178308d675737d4bcd8115786b5f9d2379734cb.

Verify/repair: run 38149625181, job 114500170820, failed on the initial code.
Actual errors concerned a multiline term's indentation, eta reduction of id,
zero-equality orientation, and an explicit coefficient-cast bridge; redundant
simp arguments also raised strict warnings. No failed candidate was called
verified. Corrected the proof terms without changing theorem targets or CI policy.

Continue: added a finite-support real-probability degree predicate, monotonicity,
a least-degree definition with explicit feasibility, the n=5 feasibility iff,
a closed equality theorem, and a formal swapped-quantifier countermodel.
Code commit 512aaf2745d2d8aab4bab76c1ac43ff6130d7de2.

Verify: run 38150083188 / job 114501532196 completed successfully at
2026-10-11T15:13:13Z (2026-10-12 00:13 JST). New modules built, the namespace
axiom audit covered 86 declarations, and every new printed target used only
propext, Classical.choice and Quot.sound. The actual completed logs were read.

Attack: alternate finite auditor recovers all 64 affine functions by Mobius
inversion and checks 2048 evaluations. Deliberate mutations drop the degree
premise or move the polynomial choice after the input. Both are exposed by
exact counterexamples; no probability grid is used to infer an all-real result.
Test/record commit 215f89efc3800ecc7c6af97f28c968685406b6b3.
Semantic run 38150257051 / job 114502054887 passed in normal Python and python -O.
Actual logs, remote auditor, formal sources and commits were re-fetched.

Record: conclusion, statement audit, actual axiom excerpt, semantic stdout,
gracefully retained first build failure and graveyard/005. No random seed or
numerical optimizer was needed: this session formalizes existing certificates.
The local auditor's output agrees with the separately executed CI output.

Classification: n=5 degree-based equality formally verified under audited
axioms; not independently human-reviewed, not new numerical or asymptotic work.
Natural milestone: the final n=5 interface gap is closed; leave Issue #8 open
for the larger finite cases and remaining general-purpose proof infrastructure.
