# Executed research loop: 2026-10-13 JST

1. Observe/orient: read the operating contract, mandatory maps/literature,
   open Issue8, prior log, source and recent commits. Do not repeat completed
   n=5 normal-form/interface work. Select n=6/n=7 extension.
2. Act: inspect prior exact masses and orbit witnesses. Solve exploratory
   mixtures over cyclic suborbits of the n=7 seed (1,71,1887847).
3. Verify/attack: enumerate all5040 relabelings and360 cyclic suborbits.
   A single suborbit with fixed twelve-ticket masses has best minimum7/12,
   so it does not retain the required8/12 pointwise guarantee.
4. Repair: combine two cyclic orbits with the four symmetric polynomials,
   using24 tickets and18 distinct rows. Verify all128 inputs. Restrict x6=0
   and separately verify all64 inputs for n=6.
5. Act: build generic affine-coverage and real-mixture bridges, actual polynomial
   degree/evaluation lemmas, concrete kernel arithmetic and least-degree results.
   Create formal candidate92df9d85e2d0a6de7fac21c8c1807758b6415ec8.
6. Verify/attack: different polynomial evaluators, Mobius coefficient
   reconstruction, exhaustive affine scores and integer Walsh-Hadamard agree.
   Six corrupted certificate claims are rejected; normal and -O runs agree.
   Commit checker, fixed certificate, search and CI as
   6e2d8728cc367a9fc9b15f64e74e5252ff2ee779.
7. Verify/repair: actual Lean job115000959315 in run38306271041 rejects
   the first candidate at SmallSupportMod3.lean:130. The remaining goal is
   the totalDegree bound of a constant polynomial after broad simp rewrites.
   Apply totalDegree_C explicitly and Nat.zero_le2, preserving every theorem,
   certificate, threshold, --wfail and axiom allowlist. The proof-only repair
   also spells out an identity step in the dual calculation; no data changed.
   Repair commit8899e75646a443415d5a2346d3c8f48d62c7bb79 has source blob
   7f2e5ecdac08af19ba461d986c84711c13cd980a.
8. Verify: re-fetch remote sources and commits, compare local Git blob hashes,
   and inspect actual CI jobs. Semantic run38307092049/job115003655051
   reproduces the normal/-O exact output at the repaired source hash.
9. Record: retain the narrow failed compression in graveyard006 and all exact
   input numerators in audit-results.json. The conclusion and formal report
   provide the eventual observed Lean status, not an extrapolation from Python.

Roles were switched by the same author; independent human semantic review and
support novelty are not asserted. The next session must begin from the actual
conclusion and Issue8, not rerun an already-completed stage by habit.
