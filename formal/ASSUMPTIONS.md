# Formal assumption ledger

## Checkpoint: actual randomized gates, 2026-10-29 JST night

Freshly approved session, research lead 月野テンプレクス. Issue22 remains OPEN.
The gate milestone is kernel accepted; the arbitrary shared-DAG endpoint is not.
This ledger does not authorize later nightly work. Complete preceding ledger,
including all older theorem chains and history links, is archived byte-identically
at reports/2026-10-29-pre-gates-ledger.md, blob9a605007af6e2a8869ffdfcc60edc8ed569a2e6f.

## Accepted source, execution and foundations

Mathematical source5e43c061544f2d56e924a03420c39d40ad5ecbc6,
tree9afbe56bae28fc6abed2cd67aade538f7e6b7132.
Completed SUCCESS formal run40884225246/job123483506622:
https://github.com/yo4e/PvsNP-Cartography/actions/runs/40884225246
Lean4.35.0-rc4, commitc29b6dda4f7c20e3eeaa717c4e565663c5cfa364;
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Whole-root --wfail9069 jobs,1083 namespace declarations, unchanged allowlist
[propext,Classical.choice,Quot.sound]. All22 explicit GatesAudit reports and
all previous target/transport/majority/growing-degree reports succeeded.

Full actual decoded output and completed steps were retrieved, as were the
actual source and matching Git commit/tree. RandomizedGates.lean blob
0b3c1ac0ecb64e6521af678e9532e6c9d3dfe55a matches local325-line source bytes.
No sorry, admit, new axiom, native_decide or warning waiver occurs in the module.
Finite two-element bit facts use kernel-reduced decide, not native_decide.
Actual lean-action resolvedfe408643ea7367d8c0404a8be3975bb145f5fb64;
axiom-audit v0.1.2 resolved46024e005996495c65ef609368e11ab39c4222e3.
Normal caching restored the previous74eca706 checkpoint. No clean-room build,
second kernel or independent semantic reviewer is inferred. Later record-only
commits are not new mathematical execution evidence.

## Statement fidelity and dependency inspection

Mask k is Fin k -> ZMod2. Each mask has real weight1/card(Mask k); the space is
inhabited even for k0. Matrix k r is Fin r -> Mask k with the ACTUAL product
weights from IndependentTrials.mass. Normalization and nonnegativity are proved.
The construction and probability distribution precede every input quantifier.

The proof of unbiasedness selects an active coordinate of a FIXED nonzero vector
and pairs ALL masks by translation with its unit vector. Weighted zero and one
fibers sum to1 and have equal mass. all_zero_mass inducts over the ACTUAL row
tuple, using sum_tuples and mass_cons; row independence is constructed rather
than assumed as a premise. The exact OR error law is0 at zero and2^-r elsewhere.
There is no conditioning on random child values, unproved hash bound or desired
success premise. AND follows by complementing both source values and output;
andValue_semantics verifies all-one semantics, including empty fan-in.

orPoly/andPoly are genuine MvPolynomial constructions. Their substitution degree
lemmas apply to arbitrary actual source polynomials of degree<=D, including
repeated variables and repeated source polynomials; bound<=rD uses actual
sum/product degree theorems. No Boolean multilinear reduction replaces degree.
Evaluation lemmas connect these constructions to the direct hash functions.
NOT/XOR/constants have exact evaluation and corresponding degree results.

or_feasible and and_feasible quantify over arbitrary natural k,r and return the
UNCHANGED HasProbabilisticDegreeAtMost at epsilon(1/2)^r, degree r. The actual
matrix family is reindexed by the accepted feasible_of_fintype adapter. Neither
the final predicate nor its finite REAL-mixture semantics was weakened.

shared_gate_union_bound quantifies over S deterministic vectors in one common
arity k and ONE common matrix distribution. It derives union mass<=S2^-r using
indicator domination, nonnegative weights and finite sum interchange. It needs
NO independence between gate failures. It is not a generic circuit-evaluation
lemma and does not prove correctness on sample-dependent input vectors.

## Adversarial and finite evidence

Two real implementation failures were repaired without changing the statements
or strict audit settings; graveyard048 records their source/run IDs. Graveyard049
contains exact witnesses against source-wire coefficient reuse, inter-gate
independence, adaptive-input quantifier exchange and omission of r>=1 in the
circuit depth conversion. These refute only the stated false shortcuts.

Finite source879f4a5c4bc1ae53e66ba5ef7f2a854b136480ec passed completed SUCCESS
run40883896389/job123482350566. Actual checker/result/workflow/commit and full
job output were re-fetched. Local Git blob hashes match: checker254ca41210132ec251bcb6121eca7b11c54de469,
JSONb42d0b3889e829feee9e8a547881fa27bb85c59e. Python3.12.15 normal/-O/saved
bytes agree. The6566 two-gate programs and8 deeper programs are bounded exact
controls by the same author; they are not a universal theorem or external review.

## Remaining obligations and scope

An actual topological DAG datatype/evaluator, recursive polynomial table,
nonlinear-depth induction, padding/reindexing, first-error inclusion and final
original-predicate/MOD3 composition remain UNFORMALIZED. The written derivation
in Expedition029 does not close them. In particular r>=1 is required for the
circuit r^h bound, while the accepted gate theorems legitimately include r0.

Earlier growing-degree, n>=299 quadratic, n>=7 affine and exact n5..11 results
remain unchanged, and their reports passed again. General n12 classification,
optimal constants, independent semantic review and the full circuit bridge
remain unresolved. #8/#15 retain their older review scopes. This is reconstruction
of a known approximation method, with novelty-unknown and no claimed general
P/poly lower bound, proof-barrier escape or P-versus-NP conclusion.

No write blocker or unapplied patch remains. Local Lean/lake were absent and
local Git read failed DNS; connected Actions supplied actual formal execution.
Expedition029/ci-evidence.md and axiom-report.txt record attributed output excerpts,
not complete raw log archives. The previous complete ledger is preserved above.
