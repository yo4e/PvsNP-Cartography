# Current research checkpoint: approved2026-10-20 JST session

## Completed formal frontier

**n=5..11** standard GF(2), pointwise error1/3 MOD3 probabilistic-degree equalities
are formally verified. n11 source9733d800128ad6d92b1f1293e453a4c8d5188f34 passed
formal39380310454/job118487684638: --wfail9043 jobs,508 namespace declarations,
18 explicit n11 reports. Independent exact audit9238f5a1 passed39380579421,
all2048 inputs and source-data alignment. #11 is CLOSED completed. #10 and older
numerical stages were already completed; do not redo stale pending records.

The accepted n11 witness uses the three canonical seeds, REAL weights[1,4,2]/7,
ALL coordinate permutations and the proved Hamming-layer bridge. The496-row
quotient remains separately verified finite data, not a new formal transport.

The auxiliary BalancedAffineDualAlgebra at dde6151abd4a4a272a2bdcbbd277c7296487d2c5
also passed production39381768668/job118492254315: --wfail9044 jobs,518 namespace
declarations, six algebra targets plus18 n11 reports. Both runs use pinned
Lean4.35.0-rc4/Mathlib9e6b3aac and only propext,Classical.choice,Quot.sound.
Actual complete logs, source statements and matching commits were re-fetched.

## Next unblocked structural task: #12

The pure real score S(n,k)=1/2+t*(n^2-t^2)/(4*n*(n-1)*(n-2)),t=n-2k,
is formally proved strictly between1/3 and2/3 for n>=7,0<=k<=n. It still needs
a GENERIC Boolean-cube counting/evaluation bridge. Prove half-mass input
normalization on layers1/3, odd-intersection counts, the binomial/cubic identity,
actual affine polynomial coverage and the finite REAL duality connection.
Do not mistake the33147 bounded formula tests for that generic proof.

The degree-one obstruction at larger arities can alternatively be transported
by correctly proved zero-coordinate restriction. This target is an explicit
reusable dual/counting proof, not a claimed new asymptotic lower bound.
The numerical degree2 frontier beyond11, including n12, remains unresolved here.

## Review and dead directions

#8 stays OPEN for independent human semantic review. A second proof kernel and
novelty assessment remain absent. Self-audits and a second CI runner do not
supply independent human review.

The equal-half strict dual fails at n6,k1 with exactly2/3 and at n5,k1 with7/10;
graveyard018 records only that distribution's failed extension. Earlier n5/n6
degree equalities are not refuted. The auxiliary first build failed on real
computability and an unused-hypothesis warning; repaired without weakened
statements or audits, recorded in graveyard019. Old n10 shutdown/CBV failures
remain historical, not current blockers.

Read Expeditions018/019 conclusions and actual reports, formal/ASSUMPTIONS.md,
and logs/2026-10-20-mod3-eleven-and-balanced-dual.md. No GitHub write blocker or
unapplied patch remains. All this session's claims have exact evidence scopes.
No support/denominator optimum, all-n degree2 upper bound, barrier escape or
P-vs-NP resolution is claimed. Any future session needs its own approval.
