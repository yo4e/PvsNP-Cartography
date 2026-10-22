# 034: the first restricted-clique proof implementation did not compile

Approved 2026-10-22 JST session. Failed code e17032050f3553e74e8ccb49b81051b338c6012d.
Completed FAILURE run39797072216, job119886937193. The entire returned job log
was read, including the pinned toolchain, build errors and skipped axiom stages.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39797072216

## Actual observations

2026-10-22T14:39:02.0389397Z: ProfileMixtures built (5.5s).
2026-10-22T14:39:06.1431881Z: RestrictedCliqueObstruction failed (4.0s).
At line60, `field_simp` had already closed the goal, making trailing `ring`
unreachable/unused; --wfail correctly rejects these warnings. At lines63,68,73,
78 and129, norm_num evaluated real arithmetic and binomial counts but left
numeral equality tests in ZMod2 unresolved, e.g. `if 10 = 1` and `if 13 = 1`.
Those are FINITE-FIELD equalities, not integer equalities. Treating them as
ordinary integers would give the wrong mathematical score.

## Repair

Remove the unused trailing tactic. Convert the remaining GF(2) equalities
through the injectivity of ZMod.val, then reduce numeral values modulo2.
Use the existing pinned ZMod.val_injective / val_ofNat lemmas, not a new axiom,
not a truth-table assumption, and not a weakened target. The support, degree,
real probabilities, quantifiers, warning policy and foundational allowlist
remain unchanged. Success must be established by a later completed run.

Partial success of ProfileMixtures is NOT acceptance of the root theorem or
its axiom audit. The failed source is retained at its commit above. This note
preserves actual attributed excerpts, not a claimed complete saved log.
