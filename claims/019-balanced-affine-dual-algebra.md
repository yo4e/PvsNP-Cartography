---
id: balanced-affine-dual-algebra
status: formally-verified
statement: For all real n>=7 and 0<=k<=n, the explicitly defined cubic rational score lies strictly between1/3 and2/3; complement symmetry and score(6,1)=2/3 also hold.
dependencies: [formal/PvsNPCartography/BalancedAffineDualAlgebra.lean]
novelty: novelty-unknown
last_attacked: 2026-10-21
---

Let t=n-2k. The score is1/2+t*(n^2-t^2)/(4*n*(n-1)*(n-2)).
Its interval bound is proved by real polynomial inequalities, NOT inferred
from the33147 bounded formula checks. Code dde6151abd4a4a272a2bdcbbd277c7296487d2c5
passed formal39381768668/job118492254315, --wfail9044 jobs,518 namespace
allowlisted declarations and six explicitly reported algebra targets. Actual
full log, source blobef92fdecc80241481d9b4578dce596848733ff33 and commit/tree
were re-fetched. See Expedition019 conclusion, ci-evidence and axiom-report.

This claim remains the REAL ALGEBRA statement. Its actual generic Boolean-cube
affine correctness connection is now separately accepted in Expedition020,
claim020-balanced-affine-obstruction, codedc58ea7d/run39510465687. The generic
count/evaluation/duality proof was not inherited from the earlier algebra run.
The optional closed half-uniform point-mass formula remains separately open
in #13; the accepted actual pushforward and score proof do not assume it.

The n6 strict-bound extension is false, formally witnessed by score(6,1)=2/3;
n5 gives7/10 in the exact finite checker. Expedition020 also formally connects
n6 equality to an actual affine row. See graveyard018 and its preserved scope.
First build failure and faithful repair remain in graveyard019. No independent
human semantic review, second kernel, optimal support, mathematical novelty,
all-n degree2 upper bound, circuit lower bound or P-vs-NP claim is supplied.
