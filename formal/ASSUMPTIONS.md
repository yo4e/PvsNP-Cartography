# Formal assumption ledger

## Checkpoint: actual polynomial to exact folded block count, 2026-11-05 JST

Research lead: 月野テンプレクス. Issue25 completed under one fresh approval. Issue26 records a next frontier, not permission for later work. This ledger separates kernel acceptance, author statement inspection, written mathematics, finite controls and independent review. Previous complete ledger is preserved byte-identically at ../reports/2026-11-05-pre-block-count-ledger.md, original blob5ea8a6ccb236c31e7bb9fc551f99ef36cde6cb7d. Its earlier history and review boundaries are retained.

## Accepted source and execution

Source51a86b10cb0f493b0c093aa81dba734400cb0118; treec04b4412f9426b633c6e8c1d57f29af737dc0e01. Run42038613103/job127283180450 completed SUCCESS. The actual commit/diff/source, audit source, completed job summaries and full decoded output were retrieved. Strict --wfail9079 jobs;1466 namespace declarations inside unchanged[propext,Classical.choice,Quot.sound];43 explicit ModulusAudit axiom reports and7 expanded endpoint signatures. All earlier reports also succeeded.

Lean4.35.0-rc4 c29b6dda4f7c20e3eeaa717c4e565663c5cfa364; Lake5.0.0-src+c29b6dd; Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8. Axiom-auditv0.1.2 at46024e005996495c65ef609368e11ab39c4222e3; lean-actionfe408643ea7367d8c0404a8be3975bb145f5fb64. Normal cache was used; no clean-room or second-kernel check is claimed. No additional axiom, sorry/admit, native_decide, warning waiver or statement weakening was introduced by this session's two-line repair.

Detailed source blobs, executable hashes, run/job links and selected message excerpts are in ../expeditions/033-modulus-block-count/execution-evidence.md. That file is not a full raw-job-log archive. Subsequent record-only commits are not additional Lean execution evidence.

## Statement fidelity

ModulusAmplification constructs the actual integer polynomial of degree at most2s-1, with parity congruence for every integer Y and s>=1, including negative values. The no-wrap theorem needs a modulus strictly greater than the maximum block count.

IntegerPolynomialLift uses canonical integer representatives of GF2 coefficients. It is NOT a ring homomorphism to integers. Mapping back to GF2 recovers the original polynomial, and the actual integer evaluation has the required parity. Its composed polynomial degree is bounded by(2b+1) times the original degree.

BooleanIntegerReduction is ring-generic and preserves evaluations on Boolean inputs while not increasing degree. It does not assert equality of unreduced polynomials or agreement at non-Boolean inputs. No field-only division is used over the residue ring.

FoldedBlockCount.tail_sum allows arbitrary nonnegative exponents and uses the number of used tail variables, not the exponent sum. The actual finite monomial fold includes the2^(b-usedTail) factor and adds all contributions with the same head support. No caller-supplied coefficient table or result equality is assumed.

SubsetZeta.scan_eq_partial requires a coordinate list with no duplicates. The full transform takes Finset.univ.toList. Its exact_count endpoint quantifies over every actual GF2 P in a+b variables and every head subset T, with no positive-head/tail premise, and concludes equality with the actual acceptingCount. Its canonical residue is an integer count because0<=count<=2^b<2^(b+1). The degree bound is a separate actual-polynomial theorem, not needed as a hypothesis for the count identity.

These are noncomputable/extensional definitions. The kernel-checked chain is NOT an efficient array implementation, a runtime theorem, a proof of Python correctness, or an algorithm-to-lower-bound transfer.

## Outside the formal boundary

The deterministic sorted-Horner/table code, the stage-invariant and bit-cost derivations, the explicit conservative exponent2^(n-n/(200d))*poly(n), and the3^a versus a*2^(a-1) cost comparison are WRITTEN arguments with finite corroboration. Input is canonical squarefree ANF; longer redundant encodings carry their own read/normalization cost. For large d use b0 and the actual one-step construction, not the loose t*M upper bound. Degree0 is separate. The count method is a known-method reconstruction, not a novelty claim.

Unchanged controls reproduce75295 exact head counts and1548 signed integer instances. New controls check22719 exact counts,26616 signed modular tables and604 finite parameter budgets. Normal/-O outputs are byte-identical; source/result blobs match re-fetched remote files. Canonical ANFs are exhaustive only at n<=3 in the new checker; higher inputs are deterministic samples and named controls. Same-author alternate implementations and brute force are NOT independent semantic review or universal proof.

The failed prior build and rejected shortcuts are preserved in ../graveyard/2026-11-05-zeta-cost-shortcuts.md. Wrong modulus, overwritten aggregation, duplicate coordinates and uncharged coefficient construction remain disallowed. These failures do not refute the repaired exact-count theorem.

## Retained scope and open gaps

Older covering, finite-field dimension, root-budget/shared-DAG and finite MOD3 statements are unchanged; their details remain in the archived complete ledger and earlier evidence. The affine-cover property's P/poly usefulness remains refuted by its easy quadratic counterfamily. No current counting result reverses that failure.

Independent older review gates8/15 remain open and are not discharged by this audit. No independent semantic approval, second kernel, clean-room build, optimality, unrestricted lower bound, P-versus-NP separation or proof-barrier escape is claimed. New frontier26 concerns the actual hierarchy/oracle bridge with E^NP and infinitely-often scope; costed implementation refinement remains unproved in Lean.

Local Lean/Lake were absent and git clone failed DNS; connected GitHub and Actions worked. No security-layer write denial or unapplied patch occurred. Later sessions require fresh approval.
