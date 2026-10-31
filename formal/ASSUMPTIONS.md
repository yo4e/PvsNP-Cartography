# Formal assumption ledger

## Checkpoint: actual shared-DAG approximation,2026-10-31 JST

Issue22 completed in one freshly approved session; Issue23 is the next target,
not standing authorization. This ledger separates kernel acceptance, faithful
statement inspection by the author, finite corroboration and independent review.
No previous theorem is weakened or historical review silently extended.

## Accepted execution and actual foundations

Source95adfa0080caa7c5106caf2164858d1fc66f969e,
treefda6de65aa480f1ba30b1b0832edcf27cc32f930.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/41159407778
Run41159407778/job124413377260 completed SUCCESS, including all old and new
explicit reports. Full decoded completed output and completed step states were
retrieved. The actual source files and matching Git commit/tree were re-fetched.

Lean4.35.0-rc4, commitc29b6dda4f7c20e3eeaa717c4e565663c5cfa364;
Lake5.0.0-src+c29b6dd; Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Whole-root --wfail9072 jobs; namespace audit1268 declarations within unchanged
[propext,Classical.choice,Quot.sound]. DAGAudit printed29 explicit theorem-axiom
reports and4 fully explicit endpoint signatures. negateOutput_cost and cost_step
use only[propext]; the other27 new reports use the full foundational allowlist.
The accepted endpoint signatures were inspected, not merely their names.

Local bytes match actual source blobs:
- SharedDAG.lean f301b113c398773aadbc7b97c72f4d1b2e311875,14242bytes;
- CircuitMod3.lean d854e2f40d597a9e01a884de165a1a087c3f2d5a,2138bytes;
- DAGBoundary.lean19ef084be2ba4973eee93ff64ae30f525e31196e,2710bytes.
No sorry/admit/new axiom/native_decide tokens occur in these modules. ONE local
backward.isDefEq.respectTransparency option remains at Gate.local_error; it
changes elaboration, not theorem assumptions, kernel rules or allowed axioms.
The recursive union proof instead uses explicit Boolean cases. No warnings were
waived. Earlier failed statements were not promoted by partial successful lines.

Normal project cache restored81619bb9ed6f216e7eeb9fba27784b07d6821218.
Actual lean-actionfe408643ea7367d8c0404a8be3975bb145f5fb64;
axiom-audit v0.1.2 at46024e005996495c65ef609368e11ab39c4222e3.
Runner2.338.2, Ubuntu24.04.5 image20261025.353.1. No clean-room execution,
independent semantic reviewer or second proof kernel is claimed. Actual output
excerpts, not the complete raw log, are archived in Expedition030/axiom-report.txt.

## Statement fidelity and dependency chain

Program n K m is a sequence with ONE stored prefix per new node. Wire permits
only external inputs or previous-table references; repeated references do not
copy a prefix in the model or increase cost. Slots indexes argument positions,
not source-wire identities, and None pads0 at OR/XOR and1 at AND. All arities
and capacities may be0. Constants, NOT and XOR are exact. Any chosen wire may
be output; unused nodes are conservatively counted. The theorem concerns this
concrete model, not a machine-verified importer for arbitrary graph formats.

values evaluates original gates. approximations is a separate randomized
evaluation; polynomials stores ACTUAL GF2 MvPolynomial objects. polynomial_eval
connects the latter two. The target is not redefined to equal the approximator.
No multilinear reduction or truth-table proxy changes the actual totalDegree.

cost counts original AND/OR nodes once, including empty ones. depths uses max
child depth (empty max0), plus1 exactly at AND/OR; inputs/constants0, NOT
inherits, XOR takes max. outputDepth refers to the selected output, not all
nodes. It counts nonlinear layers, not ALL layers as in the compared source.
For r>=1, exponent monotonicity plus actual gate substitution yields r^depth.
The r>=1 condition matters for exact skip wires and is retained.

The SAME normalized nonnegative REAL matrix distribution is chosen before all
Boolean inputs. Row independence comes from the accepted finite product mass.
Different gates may share the matrix and their bad events are not assumed
independent. Each local event evaluates the randomized gate on deterministic
TRUE predecessor values. good_values proves correctness of the whole table
outside their union by topological induction. bad_mass uses pointwise Boolean
indicator inequalities, nonnegative weights and additive original-node cost.
No desired error bound, correctness-of-approximation or degree lemma is assumed.

feasible returns the unchanged HasProbabilisticDegreeAtMost at errorcost*2^-r
and degree r^outputDepth. The finite-type adapter retains a single family before
all inputs and sums repeated polynomial outcomes legitimately. Particular real
weights in this upper witness do not restrict the arbitrary REAL mixtures in
the previously accepted lower obstruction.

feasible_third accepts conservative S,h bounds, r>=1 and3S<=2^r; it DERIVES
error<=1/3 and degree<=r^h. mod3_size_bound additionally assumes that the actual
original circuit computes residue-zero MOD3 for every input and derives
n<(16*r^h+2)^2+2 from the accepted growing-degree obstruction. There is no
polynomial-approximability endpoint premise. DAGBoundary adds an exact NOT,
proves cost/depth preservation and derives the complementary-polarity version.
Its empty-gate, external-output and cost-step endpoints retain zero cases.

## Corroboration, attacks and limits

Exact controls77e8bf049dfdc51a60c34fcfcf7723b7e233f722 passed
run41155876986/job124402435004. Python3.12.15 normal/-O/stored JSON bytes agree;
actual source/result/workflow/commit and completed output were retrieved and
local source hashes/reruns match.2694 small two-gate programs plus curated cases
compare newest-first unreduced sparse polynomials with chronological Boolean
execution. This is same-author finite evidence, not universal proof or independent
semantic review. Exact scope and all counts are in Expedition030/ci-evidence.md.

Graveyard050 retains wrong AND padding, final-local-only error and additive-degree
shortcuts; its6-versus63 unrolling example is a weaker-bound control, not a false
inequality. Graveyard051 preserves six failed whole-root candidates, two bounded
diagnostic failures, their repairs and actual cache-egress diagnosis. No semantic
condition or axiom policy was weakened. Graveyard052's XOR-of-minterms argument
rejects a size-independent h-1 improvement for arbitrary XOR outputs; the minterm
argument is written and NOT Lean-formalized by this session.

Next root-budget candidate is NOT accepted generically. Its local checker at
770197a1 passed on8curated circuits/36parameter cases with18792matrix pairs,
75144pointwise evaluations and36qualified1/3 bounds. It is NOT part of the completed
slot CI. See #23 and Expedition030/next-frontier.md. Earlier #8/#15 reviews keep
their old scopes. Novelty, optimal bounds, general n12 classification, unrestricted
circuit lower bounds, proof-barrier escape and P-versus-NP conclusions are unclaimed.

## History and environment

Previous complete ledger and all earlier history links are archived byte-identically
at reports/2026-10-31-pre-dag-ledger.md using original blob
95d49368d2056d0dce4b1e4efcf623f83a1eb87b. Previous status is similarly archived.
Local Git DNS failed and Lean/lake were absent. Connected writes and Actions
worked; a transient cache egress failure was diagnosed without paid resources
or weaker checks. Final execution succeeded. No unapplied patch/write blocker
remains. Later record-only commits are not new mathematical-source executions.
