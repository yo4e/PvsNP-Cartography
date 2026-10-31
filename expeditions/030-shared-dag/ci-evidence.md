# Actual execution evidence: complete shared-DAG bridge

Research lead 月野テンプレクス. One fresh approval, executed2026-10-31 JST.
This record separates completed kernel execution, source persistence, finite
checks, same-author semantic inspection and independent review. No new independent
semantic reviewer or second kernel was used.

## Accepted mathematical source and completed output

Source95adfa0080caa7c5106caf2164858d1fc66f969e;
treefda6de65aa480f1ba30b1b0832edcf27cc32f930;
parent9557b65800c9b4161ba9434650818a5a38a4c551.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/41159407778
Run41159407778/job124413377260 completed SUCCESS. All completed step states and
the full decoded actual job log were retrieved AFTER completion. This was not
a queued-run report, truncated build line or inferred result. The output records
actual checkout95adfa0080caa7c5106caf2164858d1fc66f969e.

The whole-root --wfail build completed9072 jobs. It explicitly compiled
SharedDAG, CircuitMod3, DAGBoundary and the root. The namespace audit inspected
1268 declarations, all within[propext,Classical.choice,Quot.sound]. All previous
reports and the new DAGAudit step completed. DAGAudit printed29 theorem-axiom
reports and4 fully explicit endpoint signatures. negateOutput_cost/cost_step
use onlypropext; the remaining27 new reports use the full allowed foundations.
No sorry/admit/new axiom/native_decide or warning waiver was introduced.

Actual Lean4.35.0-rc4, commitc29b6dda4f7c20e3eeaa717c4e565663c5cfa364;
Lake5.0.0-src+c29b6dd; Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Resolved lean-actionfe408643ea7367d8c0404a8be3975bb145f5fb64;
axiom-audit v0.1.2,46024e005996495c65ef609368e11ab39c4222e3;
checkout11d5960a326750d5838078e36cf38b85af677262.
Runner2.338.2, Ubuntu24.04.5 image20261025.353.1. Normal project cache restored
81619bb9ed6f216e7eeb9fba27784b07d6821218. This is not a clean-room run or an
independent proof kernel. The complete raw log was fetched, but only labeled
actual excerpts are archived in axiom-report.txt; no complete raw archive is claimed.

## Source re-fetch and local comparison

The matching Git commit/tree was re-fetched. SharedDAG/CircuitMod3 were retrieved
at9557b658; the subsequent95adfa commit changes only DAGBoundary, whose complete
final source was retrieved at95adfa. DAGAudit was also retrieved at95adfa.
Local UTF-8 blob hashes match actual GitHub source:

SharedDAG.lean f301b113c398773aadbc7b97c72f4d1b2e311875,14242bytes.
CircuitMod3.lean d854e2f40d597a9e01a884de165a1a087c3f2d5a,2138bytes.
DAGBoundary.lean19ef084be2ba4973eee93ff64ae30f525e31196e,2710bytes.

A local lexical scan finds no forbidden proof placeholders/new axioms/native
computation tokens in these three modules. This scan complements, not replaces,
the completed kernel/axiom checks and the statement audit. ONE local elaboration
transparency option is used at Gate.local_error; it does not change the kernel
or mathematical premises. The final union proof uses direct Boolean cases.

## Separately completed exact controls

Source77e8bf049dfdc51a60c34fcfcf7723b7e233f722;
treec4139871d1cc93b1422b8cafdfb74fe1476c7f3a.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/41155876986
Run41155876986/job124402435004 completed SUCCESS. The actual checkout, full
completed output, Python3.12.15 and all step states were retrieved. Normal and
python -O outputs were compared byte-for-byte, then compared with stored JSON.
The checker uses explicit RuntimeError checks which remain active under -O.

Actual checker/result/workflow and matching Git commit/tree were re-fetched.
Local blob hashes agree:
check_slots.py1329a34a1d90e7ce82415ebf931299f5ff091c62,10114bytes;
slot-checks.json cd0dc75af3cd9e3029b5b840cc38eeeb645cf82c,1638bytes;
workflow8bd25836369a3e30c92602c2ac2c63a6361c431f.
Local normal/-O reruns and py_compile passed. Two same-author implementations
compare unreduced sparse GF2 polynomials/newest-first tables with chronological
Boolean evaluation. They are not an independent semantic reviewer.

All two-gate programs for n,K in0..2 at r1/2:2694 programs,5388 parameter cases,
46214 program-matrix pairs,92428 actual-degree checks,318388 node-input checks,
294556 external-output checks,36312 pointwise-output checks,18156 union bounds
and15996 qualified error1/3 bounds. Four curated parameter cases add144 matrix
pairs,640 degree checks,5024 node-input checks and26 union checks. A separate
MOD3 n3 circuit (S3,h2,r4) is checked on4096 matrices and all8 inputs; exact errors
are[1/16,15/256,15/128,15/128,15/128,15/256,15/128,1/16]. That r4 MOD3 check is
Boolean execution only; its actual sparse degree was checked separately at r1/2.
All finite counts corroborate, not prove, the generic theorem.

## Failure history and diagnosis

Six whole-root candidates completed FAILURE before acceptance:
3c4d5ce1/run41155490365/job124401254735;
dc304d60/run41156190207/job124403391357;
4dd55ef7/run41156858590/job124405450102;
9068a998/run41157416536/job124407157540;
be5c41cf/run41158114718/job124409324125;
9557b658/run41158707027/job124411171874.
Two bounded same-kernel diagnostics also completed FAILURE:
1dd82d1b/run41156992102/job124405856047;
51ada5ca/run41157531689/job124407517578.
Full completed logs were retrieved for all. None is promoted to accepted because
some modules compiled. Graveyard051 preserves exact faults and repairs.

The dc304d60 run recorded a3.52GB cache restoration failure with account egress
limit, then rebuilt old certificates. This explains its long runtime separately
from the three small SharedDAG errors. The final run restored the cache and
completed. No paid resources, credentials or audit relaxations were introduced.

## Local continuation is a distinct evidence class

Source770197a1955537f8bb6ce52ec0a17bcafb385660,
tree5ff51bf88a2bf9306c3385d2f5a7e8523fb23a8b, saves check_root_budget.py and
root-budget-checks.json. Actual files/commit were re-fetched; local hashes match:
017cfc1b81a1132c172b2cd59fa4acb79a8a3d32 (4469bytes),
7b3119b01a7ad1e2f98f4a760e5339442aa3b309 (461bytes).
Local normal/-O output bytes and py_compile agree:8circuits,36parameter cases,
18792matrix pairs/degree checks,75144pointwise evaluations,120error bounds and
36qualified1/3 bounds. These enumerate an explicit Cartesian product and reuse
same-author sparse arithmetic. NOT included in completed slot CI; NOT a generic
root-budget proof. The next formal target is Issue23, not a retroactive extension
of this session's accepted DAG theorem.

## Promotion boundary

Accepted: concrete shared-DAG semantics, actual degree/evaluation/pointwise
approximation, original epsilon1/3 conversion, both MOD3 polarities and boundary
lemmas under the stated foundations. Not accepted by implication: independent
semantics, second kernel, root-budget theorem, new mathematical priority, optimal
bounds, general n12 classification, unrestricted lower bounds, barrier escape or
P versus NP. Record-only commits are not mathematical-source execution evidence.
