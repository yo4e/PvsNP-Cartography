---
id: mod3-five-degree-interface
status: formally-verified
statement: "For MOD3 on five bits over GF(2), pointwise error 1/3 is feasible with finite-support real degree-d polynomial distributions iff 2 <= d; the least degree is 2."
dependencies: "Expedition 005 certificates; structural degree-one normal form; finite real-mixture duality; actual polynomial upper degree/evaluation."
novelty: unknown
last_attacked: 2026-10-12
---

Formal target: PvsNPCartography.Mod3Five.pdeg_eq_two.
Stronger threshold statement: PvsNPCartography.Mod3Five.feasible_degree_iff.
Definition: HasProbabilisticDegreeAtMost in formal/PvsNPCartography/ProbabilisticDegree.lean.

Verified code 512aaf2745d2d8aab4bab76c1ac43ff6130d7de2;
[actual CI](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38150083188),
job114501532196; target axioms propext, Classical.choice, Quot.sound.
The complete namespace audit covered86 declarations. Statement self-audit and
countermodels: ../expeditions/006-degree-interface/statement-audit.md.

No independent human review or second proof kernel. This is formalization
of the existing n=5 result, not novelty, larger-n verification or P-vs-NP progress
in the sense of a complexity-class separation. Exact scope and provenance:
../expeditions/006-degree-interface/conclusion.md.
