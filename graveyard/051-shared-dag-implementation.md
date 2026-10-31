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

The next repair,9068a9980f5809cba2bcbfbb8810407372d81ff1, changed elaborator
transparency locally around Gate.local_error and bad_mass, using
`set_option backward.isDefEq.respectTransparency false in`. The existing
MajorityAmplification module already uses this local elaboration technique.
The historical proposal was insufficient; its concrete outcome is below.
No theorem statement, event definition, distribution, degree notion, kernel
rule, allowed axiom or --wfail policy was changed.

## Parser failure and the union transport that still did not work

Source9068a998, run41157416536/job124407157540 completed FAILURE.
Diagnostic source51ada5ca4ad8daa4d55ada95673ef1da2a941a6b,
run41157531689/job124407517578 also completed FAILURE under a300second bounded
DAGBoundary build. Both full decoded completed logs were retrieved. The local
gate-error elaboration failures disappeared, but a documentation comment placed
BEFORE the local set_option caused an unexpected-token parser error at line246.
The recursive bad-event instance mismatch also remained. The diagnostic did
not time out and did not execute its subsequent axiom report.

Sourcebe5c41cf2e6040ddabdb17a21098a54cf82fd955 fixed the comment placement.
Run41158114718/job124409324125 completed FAILURE with one remaining error:
the union-indicator transport at line261 still distinguished instDecidableOr
from Classical.propDecidable. The completed full output was retrieved. Merely
loosening elaborator transparency had NOT repaired this proof step.

Source9557b65800c9b4161ba9434650818a5a38a4c551 replaces that transport by
four explicit cases for the old bad event and current gate equality. It removes
the local option around bad_mass; only Gate.local_error retains the option.
The actual inequality, weights and cost stay unchanged. This repaired the core:
run41158707027/job124411171874 compiled SharedDAG and CircuitMod3 successfully,
but the OVERALL run still completed FAILURE. No partial green line was promoted.

## Empty OR function equality

The9557b658 run failed in DAGBoundary.absent_or at line39. The goal was the
FUNCTION equality `(args 0 x v (fun _ => none)) = 0`, not an equality at a
particular argument. A simp entry for args did not eta-expand the function
and was reported unused under --wfail. Completed steps and full actual output
were retrieved; namespace and endpoint audits were skipped after this failure.

Source95adfa0080caa7c5106caf2164858d1fc66f969e repairs only this proof:
change to the conditional defining OR, then prove its zero-vector condition
by funext and reflexivity. No empty-case semantics is removed or weakened.
Its eventual completed acceptance/failure is recorded in the expedition's
ci-evidence.md, not inferred here from the repair proposal.

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
