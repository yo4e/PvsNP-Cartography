---
id: balanced-affine-dual-algebra
status: formally-verified
statement: For all real n>=7 and 0<=k<=n, the explicitly defined cubic rational score lies strictly between1/3 and2/3; complement symmetry and score(6,1)=2/3 also hold.
dependencies: [formal/PvsNPCartography/BalancedAffineDualAlgebra.lean]
novelty: novelty-unknown
last_attacked: 2026-10-20
---

Let t=n-2k. The score is1/2+t*(n^2-t^2)/(4*n*(n-1)*(n-2)).
Its interval bound is proved by real polynomial inequalities, NOT inferred
from the33147 bounded formula checks. Code dde6151abd4a4a272a2bdcbbd277c7296487d2c5
passed formal39381768668/job118492254315, --wfail9044 jobs,518 namespace
allowlisted declarations and six explicitly reported algebra targets. Actual
full log, source blobef92fdecc80241481d9b4578dce596848733ff33 and commit/tree
were re-fetched. See Expedition019 conclusion, ci-evidence and axiom-report.

This is ONLY the real algebra statement. Identifying the score with an actual
generic Boolean-cube affine correctness probability requires the uncompleted
counting bridge in #12. No generic MOD3 theorem is silently assumed here.
The n6 strict-bound extension is false, formally witnessed by score(6,1)=2/3;
n5 gives7/10 in the exact finite checker. See graveyard018.

First build failure and faithful repair are preserved in graveyard019. No
human independent semantic review, second kernel, support minimality, novelty,
all-n degree2 upper bound, circuit lower bound or P-vs-NP claim is supplied.
