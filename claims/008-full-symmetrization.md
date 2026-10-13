---
id: 008-full-symmetrization
status: formally-verified
statement: >-
  For every finite arity n and permutation-invariant GF(2)-valued Boolean target,
  full permutation symmetrization preserves actual polynomial degree and
  normalized finite real probabilities, produces invariant success, and
  converts a bound on every input orbit into the original pointwise certificate.
dependencies:
  - formal/PvsNPCartography/ProbabilisticDegree.lean
  - formal/PvsNPCartography/PermutationTransport.lean
  - formal/PvsNPCartography/FiniteSymmetrization.lean
novelty: novelty-unknown; standard averaging and existing Mathlib identities reconstructed
last_attacked: 2026-10-13
---

Verified code: ac61ba1b2888de029b8fc567187ff3a4dbb263c0.
Formal run38414011388/job115353465722 passed --wfail, the 205-declaration
allowlist audit and 21 explicit target reports. Source and completed output
were re-fetched. Foundational dependencies: propext, Classical.choice, Quot.sound.

Closed n=6/n=7 MOD3 application and three counterexample components are in
SymmetryApplications.lean. Independent human semantic review remains pending.
Finite executable audits are separate evidence, not the proof for arbitrary n.

Not claimed: a general orbit-to-Hamming-layer counting formula in Lean,
a new MOD3 degree value, support optimality, an all-n degree bound, or a
complexity-class result. The next formal frontier is fiber counting.

See Expedition008 conclusion, statement audit, prior-art audit and graveyard007.
