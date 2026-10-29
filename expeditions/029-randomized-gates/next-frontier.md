# Next mathematical entry: concrete shared-DAG approximation

This target is part of OPEN Issue22, not authorization for another session.
Read current AGENTS/status/ledger and obtain fresh nightly approval first.

## Starting point

Accepted RandomizedGates at5e43c061544f2d56e924a03420c39d40ad5ecbc6:
actual OR/AND constructors, degree<=rD, evaluation, exact fixed-input failure,
original finite REAL-mixture gate feasibility, exact NOT/XOR/constants, and the
shared_gate_union_bound for deterministic vectors under a single matrix.
Pinned completed evidence: ci-evidence.md. The accepted growing-degree theorem
is unchanged and has contrapositive Mod3GrowingDegree.feasible_size_bound.

## Bounded closed target

Define only the concrete topological DAG model required by Issue22: input and
constant wires plus NOT, finite XOR, finite AND and finite OR; repeated earlier
references and sharing allowed. Choose an output wire. Count S original AND/OR
nodes once each. Define nonlinear depth recursively as max child depth (empty
max0), adding1 exactly at AND/OR; input and constant depth0. This conservative
definition includes paths rooted at constants/empty gates, not only input wires.
Do not silently change it to a potentially smaller input-only path measure.

For r>=1 construct actual polynomial values by the same topological table using
one common r-by-K matrix, K at least maximum fan-in. Pad OR arguments by0 and
AND arguments by1 (so complemented padding is0), or prove equivalent restriction
marginals. Preserve argument-POSITION coordinates even with repeated references.

Prove actual degree<=r^(node depth) by induction, using monotonicity in depth
for r>=1, exact XOR/NOT degree lemmas and actual rD substitution bounds. For fixed
original input x, construct TRUE deterministic node values, define each local
bad event on those values, and prove by topological induction that no local bad
event implies equality of the actual approximate and true tables. Do not apply
a fixed-input lemma directly to a sample-dependent approximate child vector.

Use union bound over S original nodes, not unrolled formula occurrences, to get
pointwise error<=S/2^r. Return the ORIGINAL finite REAL-mixture predicate at
error1/3 when3S<=2^r. If the circuit computes residue-zero MOD3, derive
n<(16*r^h+2)^2+2 from the accepted lower-degree obstruction. The endpoint must
not assume circuit approximability or the desired failure bound as a premise.

## Attacks and stopping point

Attack constants, empty input/empty gate families, output equal to an original
input, skip wires, unused nodes, repeated references, AND complement padding,
shared randomness, depth accounting, original target polarity and quantifier
order. Retain graveyard047/049 counterexamples. Do not revive r0 as a circuit
hypothesis merely because the gate lemma permits it. The Python checker gives
finite controls only and supplies no formal axiom.

Natural milestone: the actual closed shared-DAG-to-original-predicate theorem
and MOD3 consequence, or a precise counterexample/post-mortem. Strict pinned
whole-root build, unchanged axiom audit, explicit endpoint reports and actual
source/commit/completed-output re-fetch precede promotion. No independent review
or novelty is implied by the previous kernel acceptance or by these instructions.
