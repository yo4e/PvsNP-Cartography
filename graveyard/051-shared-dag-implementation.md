# Shared-DAG implementation failures, not mathematical refutations

Author: 月野テンプレクス. Freshly approved session executed2026-10-31 JST.
Preserve failures before repair. No failed candidate is accepted as a theorem.

## First candidate

Source3c4d5ce1192ac44db831731a962f0d7cd748a6c4, tree7d1f490c42121f75ee7820d9f8ddfd989747a26a.
Run41155490365/job124401254735 completed FAILURE. The completed steps and full
decoded actual job log were retrieved. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac;
whole-root --wfail unchanged. The build failed in SharedDAG and later explicit
axiom reports were skipped. CircuitMod3 was not accepted by that run.

Errors: partial applications of eval_args/args_degree left slot capacity K
unconstrained; dependent empty Fin eliminations needed explicit arguments;
Fin.cons did not infer the motive in a standalone equality; unfolding gate
predicates left decidability instances that failed implicit-transparency
rewrites; the success-complement sum needed an explicit row count r.

First repair: specify existing K/r parameters, use pointwise Fin.cases for table
equalities and explicit empty indices, and transport standalone proved gate
and union indicator inequalities by simplification. This was not sufficient:
the three event-instance mismatches below remained. Do not interpret the
repair description as acceptance.

## Residual event-instance mismatch, independently reproduced as an execution

Core repaired source dc304d60832b257fa8175f848366a76efab26264:
run41156190207/job124403391357 completed FAILURE. The full actual completed log
was retrieved. SharedDAG failed at lines214/223/259. The first two messages
printed identical real inequalities but retained different hidden Decidable
instances; the third explicitly displayed instDecidableOr versus
Classical.propDecidable applied to the recursive bad predicate.

Boundary-extension source4dd55ef75eedc4b393873687b409155b15d704ea:
run41156858590/job124405450102 also completed FAILURE, with the SAME unchanged
SharedDAG blob fe4bb8eb8e2e59cc6d7f32bb5d987d903e4d72a9 and three diagnostics.
Full decoded actual output was retrieved. This run never accepted DAGBoundary.
It is not a separate mathematical counterexample.

Bounded diagnostic source1dd82d1b050e50f71c83645ab73ad55dfa3d29c3:
run41156992102/job124405856047 completed FAILURE under
`timeout 180s lake build --wfail PvsNPCartography.SharedDAG` without restoring
the project build cache. It reproduced the same errors in about4 seconds of
module compilation. This is same-kernel execution diagnosis, not independent
semantic review. Its full completed job log was retrieved.

The next repair,9068a9980f5809cba2bcbfbb8810407372d81ff1, changes only elaborator
transparency locally around Gate.local_error and bad_mass, using
`set_option backward.isDefEq.respectTransparency false in`. The existing
MajorityAmplification module already uses this local elaboration technique.
No theorem statement, event definition, probability distribution, degree notion,
kernel rule, allowed axiom or --wfail policy changes. Acceptance must still be
established by an actual completed strict build and axiom audit; see the
expedition's ci-evidence.md for the eventual outcome, not this repair proposal.

## Distinguish infrastructure delay from proof failure

The dc304d60 job's actual log records a failed3.52GB project-cache restoration:
`Failed to restore: Egress is over the account limit.` It then rebuilt the
repository, including older n10/n11 certificates, before reporting the already
encountered SharedDAG error. Hence the lengthy run did NOT show a mathematical
proof search stuck for that entire period. The later4dd55ef7 run restored the
cache successfully and failed on the same module in6.7seconds. The diagnostic
workflow isolates the target; it is not a substitute for whole-root acceptance.
No paid resource, credential change or weakened audit was used to work around
this transient execution problem.

The mathematical counterexamples are separately preserved in graveyard050/052.
The failure history remains visible even if a later candidate succeeds.
