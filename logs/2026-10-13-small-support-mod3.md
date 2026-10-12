# 2026-10-13 JST: n=6/n=7 complete degree theorems and a compact witness

One session approved by 山田さん. Research lead: 月野テンプレクス.
Start:0772e621e1ab5686877be257b58b2410b8c3df11. Read AGENTS, mandatory docs,
open Issue8, recent commits and prior logs before substantive work. The n=5
normal-form/interface result was already complete and was not rebuilt as new work.

## Results and verification

Completed the genuine pointwise probabilistic-degree equality2 over GF(2),
error1/3, for n=6 and n=7, including feasibility iff2<=d, IsLeast and pdeg_eq_two.
Created18-distinct-polynomial upper witnesses with24 tickets each; exact
minimum16/24. Lower dual maxima are11/18 (n=6) and17/30 (n=7), below2/3.
Every coefficient, full-cube input, affine row and real-mixture premise is covered.

Formal run38307092042/job115003654751 succeeded at repaired code8899e756:
pinned Lean4.35.0-rc4, Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8,
--wfail,145-declaration namespace audit and explicit target axioms. All13 newly
printed targets depend only on propext, Classical.choice, Quot.sound.
Actual completed logs were retrieved and an attributed excerpt retained.

Semantic run38307092049/job115003655051 passed normal and -O Python on the
same commit. Two evaluators, Mobius coefficient reconstruction, integer Walsh
scores and exhaustive enumeration agree. All six altered claims are rejected.
Counts: n=6,64inputs/128affine rows; n=7,128inputs/256affine rows;18*64
zero-restriction cross-checks. Sources, certificates and commits were re-fetched;
Git blob hashes matched local bytes and the CI output's source hash.

## Failure, attack, repair

One cyclic orbit plus fixed symmetric masses[1,2,1,1] fails for all360
candidates: best minimum7/12 instead of8/12. A concrete input5 counterexample
and exact reproduction are retained in graveyard/006-single-cyclic-orbit.md.
Two cyclic orbits plus masses[2,4,2,2] repair it at24 tickets. This does not
prove minimal support or general twelve-ticket infeasibility.

The first Lean candidate's job115000959315/run38306271041 failed at
SmallSupportMod3.lean:130, an unresolved constant-polynomial degree bound.
The repair invokes totalDegree_C explicitly without weakening the statement,
certificates, thresholds, --wfail, or axiom allowlist. The failed candidate is
preserved in Git history and described in Expedition007/log.md.

The compact witness is not a pointwise-symmetric distribution under all
permutations: weight-three inputs7 and19 have success16/24 and20/24.
Full per-input checks, not layer-average reasoning, protect the theorem.
The old n=7 certificate retains strict slack10825/15922>2/3 and stays in place.

## Successful code and test commits

- 92df9d85e2d0a6de7fac21c8c1807758b6415ec8: initial formal candidate,
  root import and explicit axiom targets; first compilation failed as recorded.
- 6e2d8728cc367a9fc9b15f64e74e5252ff2ee779: exact checker, fixed data,
  candidate search and reproducible semantic CI.
- 8899e75646a443415d5a2346d3c8f48d62c7bb79: proof-only repair, fully
  verified in the two actual successful runs above.

The records-only commit containing this log adds documentation and observed
results without modifying the verified formal source. Issue8 is updated with
its final commit and the new frontier after the records are re-fetched.

## Next frontier and blockers

No GitHub write blocker or unapplied patch remains. The local container lacked
Lean and could not clone via network, so actual formal compilation was done
through GitHub Actions, not claimed to have run locally.

Complete degree-based Lean coverage is now n=5,6,7. The finite n=8 certificate
is still not connected to a complete Lean equality. Issue8 remains open for
full variable-permutation/symmetrization infrastructure and independent human
semantic review. The useful unblocked next step is the generic permutation
lemma with actual degree/evaluation semantics, then symmetrization and n=8.
Do not restart completed n=6/n=7 formalization.

Independent human semantic review, a second proof kernel and support novelty
have not been established. No new finite value, general-n statement,
proof-barrier escape or P-vs-NP conclusion is claimed.

Detailed record: expeditions/007-small-support-mod3/{orientation,barrier-audit,
log,statement-audit,conclusion}.md, certificate.json, audit.py, audit-results.json;
formal/reports/2026-10-13-small-support-axioms.txt.
