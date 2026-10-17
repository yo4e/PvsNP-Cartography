# Expedition 014: n=10 MOD3 degree interface

Status: candidate; formal verification pending.
Research lead: 月野テンプレクス. Approved session: 2026-10-17 JST.
Base commit: 783b4547812e15c6dc43106d2f1fe490d6389d60. Open task: #10.

## Observe / orient
Read AGENTS.md and its five required documents, current open Issues #8/#10,
recent commits and the 2026-10-16 night log. n=5..9 already have completed
formal degree equalities; do not repeat those targets. Expedition013 stores
an exact n=10 eight-orbit witness, not a compiled n=10 degree theorem.

## Target and acceptance criteria
Derive the eight actual GF(2) quadratic coefficient rows from the block-code
certificate, use a normalized input-independent real distribution and the
existing full-permutation/Hamming-layer bridge, and connect the upper bound
to HasProbabilisticDegreeAtMost. Prove the universal degree-one obstruction
via structural polynomial normal form and the exact 152/240 dual bound.
Close feasible_degree_iff, IsLeast and pdeg_eq_two only after a real pinned
Lean run and an explicit axiom/statement audit.

## Independent checks and attack plan
Use block-parity evaluation versus explicit monomial evaluation on all 1024
inputs; validate lexicographic 45-edge encoding and all eleven Hamming layers.
Recheck all 2048 affine rows and their permutation reduction. Test omitted
symmetrization, input-dependent selection, altered coefficients, normalization,
and strict lower-gap arithmetic. Preserve failures and exact scope.

## Scope
No novelty, minimal-support, general-n or P-vs-NP claim. Issue #8 remains an
independent human semantic-review gate. Finite computation and Lean execution
are separate evidence classes. The local container cannot resolve github.com;
repository reads/writes use the connected GitHub tool rather than git clone.
