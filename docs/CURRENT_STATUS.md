# Current checkpoint: the actual shared-DAG bridge is connected

Freshly approved session executed2026-10-31 JST. Research lead 月野テンプレクス.
**Issue22 is CLOSED/completed; Issue23 is the next bounded mathematical frontier.**
This checkpoint is not authority for a later session. Dated README/direction and
old Issue bodies are history, not instructions to restart completed work.

## Mathematical change

For the concrete finite topological SharedDAG.Program/Slots representation,
r>=1 gives one fixed-before-input finite distribution of actual GF2 polynomials
with genuine totalDegree<=r^h and pointwise error<=S/2^r. Here S bounds ORIGINAL
AND/OR node count and h bounds the selected output's recursive AND/OR depth,
not total gate-layer depth or formula-occurrence count. Inputs/constants/NOT/XOR,
repeated references, sharing, neutral padding, empty fan-in, unused nodes and
arbitrary chosen outputs are retained. No verified external graph translator
is claimed; finite slot capacity K can be chosen for each finite fan-in instance.

Local bad events use deterministic TRUE predecessor values. Topological
correctness outside their union and nonnegative real-weight summation prove
the bound without independence across gates. Actual polynomial evaluation and
degree induction are supplied, not assumed. One shared matrix is sampled before
all inputs; only its rows need the already constructed independence.

Under3*S<=2^r, feasible_third returns the ORIGINAL error1/3 probabilistic-degree
predicate. If the circuit computes residue-zero MOD3, mod3_size_bound derives

 n < (16*r^h+2)^2+2.

Exact output NOT preserves nonlinear cost/depth and supplies the complementary
MOD3 version. This closes the missing circuit-approximability implication in
Issue22; it is known-method reconstruction, not a new unrestricted circuit lower
bound or P-versus-NP separation. Earlier accepted MOD3 results remain intact.

## Actual completed verification

Mathematical source95adfa0080caa7c5106caf2164858d1fc66f969e,
treefda6de65aa480f1ba30b1b0832edcf27cc32f930.
SUCCESS run41159407778/job124413377260: pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
whole-root --wfail9072 jobs,1268 namespace declarations within unchanged
[propext,Classical.choice,Quot.sound],29 new explicit axiom reports plus4 explicit
endpoint signatures and all old reports. Actual completed states/full decoded
output, source modules and matching Git commit/tree were retrieved and inspected.
Source blob hashes match local bytes; no sorry/admit/new axiom/native_decide or
warning waiver. Normal caching was used, not an independent proof kernel.
Expedition030/ci-evidence.md and axiom-report.txt separate full-log retrieval
from the labeled excerpts actually archived. No new independent semantic review
was performed; #8/#15 retain their older scopes.

Exact-control source77e8bf049dfdc51a60c34fcfcf7723b7e233f722 passed
run41155876986/job124402435004. Python3.12.15 normal/-O/committed JSON bytes
agree.2694 two-gate programs plus curated cases compare unreduced polynomial
and chronological Boolean implementations. This same-author finite corroboration
is not the universal proof. Graveyard050/051/052 retain mathematical shortcuts,
all implementation failures and the nonlinear-versus-total-depth mismatch.

## Next: Issue23, one separately budgeted final AND/OR

Construct actual product weights for inner r-row and final t-row matrices,
then prove degree<=t*r^H and pointwise error<=S*2^-r+2^-t. With t2 and12S<=2^r,
obtain original error1/3 and degree2*r^H. Do not extend this root condition to
arbitrary XOR outputs; graveyard052 refutes that blind depth-factor deletion.

Continuation770197a1955537f8bb6ce52ec0a17bcafb385660 saves local exact tests:
8 circuits,36 parameter cases,18792 matrix pairs and75144 pointwise evaluations.
Normal/-O bytes and local compilation agree. This root-budget check is NOT
covered by the completed slot-control CI and NOT a generic Lean theorem.
The precise next entry is expeditions/030-shared-dag/next-frontier.md and #23.

No write blocker or unapplied patch remains. Local Git DNS failed and Lean/lake
were absent; connected GitHub/Actions worked. One earlier project-cache egress
failure caused rebuilding, but the final run restored the cache and completed.
Novelty, independent semantic approval, second-kernel checking, optimal constants,
general n12 classification and proof-barrier escape remain unclaimed.

Previous complete status is archived byte-identically at
history/2026-10-31-pre-dag-status.md using blobaf5409fbd9711a743e5879fe621b3964d815c4eb.
Session: ../logs/2026-10-31-shared-dag.md. Later work requires fresh approval.
