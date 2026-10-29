# Current checkpoint: actual randomized GF2 gates, with shared-error control

Freshly approved night session, 2026-10-29 JST. Research lead: 月野テンプレクス.
Issue22 remains OPEN: its generic gate milestone is accepted; the full shared-DAG
bridge remains the next mathematical target. This is not future-session authority.

## What changed mathematically

RandomizedGates constructs actual OR/AND polynomials from independent uniform
linear-hash rows, with one finite normalized nonnegative REAL distribution
chosen BEFORE every Boolean input. For every arity k and row count r, including
zero, original HasProbabilisticDegreeAtMost holds at error (1/2)^r and degree r.
The exact OR error is zero on the zero vector and (1/2)^r otherwise; AND is dual.
Substitution of arbitrary actual degree<=D polynomials gives genuine totalDegree
<=r*D. Repeated wires and non-multilinear powers are retained. NOT/XOR/constants
have exact evaluation and degree lemmas.

shared_gate_union_bound proves error-union mass<=S*(1/2)^r for S deterministic
true input vectors using ONE shared matrix. It assumes no independence between
gates. This is not yet a theorem about recursively evaluated arbitrary DAGs.
The missing universal DAG endpoint is now isolated from the accepted gate proof.

## Actual completed verification

Accepted mathematical source: 5e43c061544f2d56e924a03420c39d40ad5ecbc6.
Tree: 9afbe56bae28fc6abed2cd67aade538f7e6b7132.
Formal run40884225246/job123483506622 completed SUCCESS. Pinned Lean4.35.0-rc4,
Mathlib9e6b3aac; whole-root --wfail9069 jobs;1083 namespace declarations within
unchanged [propext,Classical.choice,Quot.sound]. All previous reports and22 new
explicit gate reports completed. Actual source, commit/tree, completed steps
and full decoded job output were re-fetched and inspected; source blob matches
local bytes. No sorry/admit/new axiom/native_decide or warning waiver was added.

Finite-control source879f4a5c4bc1ae53e66ba5ef7f2a854b136480ec passed exact
run40883896389/job123482350566 with Python3.12.15. Normal/-O output bytes and
committed JSON match, as do local reruns. Exhaustive6566 two-gate DAGs and8
curated deeper DAGs corroborate, but do not prove, the universal circuit result.
These are two implementations by the SAME author, not independent semantic review.
Expedition029/ci-evidence.md gives source hashes, actual runs and evidence limits.

## Refuted shortcuts and next frontier

Graveyard048 preserves two failed formal implementations and their repairs.
Graveyard049 refutes hashing by source-wire identity, multiplying correlated
gate-error probabilities, using the fixed-input bound for sample-dependent
inputs, and dropping r>=1 from the circuit degree bound. Graveyard047 remains.

Next: formalize a concrete topological shared DAG, its actual polynomial table,
nonlinear-depth induction and first-error inclusion using TRUE deterministic
wire values. For r>=1, S original AND/OR nodes and nonlinear depth h, derive
actual degree<=r^h and pointwise error<=S/2^r, without unrolling sharing.
With3S<=2^r, return the ORIGINAL error1/3 predicate, then apply accepted
Mod3GrowingDegree.feasible_size_bound to obtain n<(16*r^h+2)^2+2 for MOD3.
Written derivation and precise remaining obligations are in Expedition029.

Prior growing-degree exclusion (16*d+2)^2+2<=n, the stronger d2/n>=299 result,
exact degree2 at n5..11 and affine exclusion n>=7 remain unchanged and passed
this root build. General n12 classification remains unresolved. No novelty,
optimal constant, new unrestricted circuit bound, barrier escape or P-vs-NP
conclusion is claimed. No new independent reviewer or second kernel was used;
#8/#15 retain their older scopes.

No write blocker or unapplied patch remains at this checkpoint. Local Lean/lake
were absent and local Git failed DNS; connected Actions supplied execution.
Record-only later commits are not new mathematical execution evidence.
Previous complete status is archived byte-identically at
history/2026-10-29-pre-gates-status.md (blobca659b28ab9e12ec75200375ec38d6aad47394d7).
Session log: ../logs/2026-10-29-randomized-gates.md.
