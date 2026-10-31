# A separately budgeted nonlinear root: derivation and scope

Author: 月野テンプレクス, 2026-10-31 JST night. Known-method reconstruction;
novelty unknown. Mechanical execution is recorded separately in ci-evidence.md.
This is an author statement audit, not independent semantic review.

## Exact mathematical contract

Retain SharedDAG.Program n K m, its deterministic values, nonlinear depths and
original AND/OR count. Let p have cost at most S, and ws have child height at
most H. Append ONE gate, OR if b=false and AND if b=true. target_is_circuit
identifies the new target with the old evaluator of this actual appended circuit.
No approximator is substituted into the definition of the target.

For inner r>=1 and final t>=0, select A:Matrix K r and B:Matrix K t with real
weight matrixWeight(A)*matrixWeight(B), before all Boolean inputs. poly is the
existing root gate's genuine polynomial applied to the existing inner polynomial
table. The finite product is normalized and nonnegative, including K=0.

Each selected child polynomial has actual totalDegree<=r^H. The existing OR/AND
substitution lemmas give totalDegree<=t*r^H. There is no Boolean quotient in
this assertion, even when two wires repeat or powers cancel only as functions.

For fixed input x, E_A is the inner program's union of TRUE-child local errors.
F_B is the root approximation's error on its deterministic TRUE child vector.
Outside E_A, the actual inner polynomial evaluations equal the true table.
Therefore root output error is contained in E_A union F_B. Product marginal
identities are proved for arbitrary real test functions, not assumed for these
events. Their masses are at most S*2^-r and 2^-t; summing indicators proves the
claimed bound. No conditioning on corrupted children or independence of gate
errors occurs. Independent product sampling is a sufficient construction, not
a claim that all other couplings fail.

feasible returns the ORIGINAL HasProbabilisticDegreeAtMost predicate. With t=2
and 12*S<=2^r, inner allowance<=1/12 and root allowance1/4 sum to1/3, yielding
degree2*r^H. If this original circuit computes residue-zero MOD3, the already
accepted obstruction gives n<(32*r^H+2)^2+2. The only target premise is actual
circuit correctness; approximation, normalization and degree are all derived.
The optional output-NOT version is not added by this expedition.

## Edge cases and parameter comparison

S=0, empty inner programs, K=0, None padding, repeated references, unused inner
nodes and exact NOT/XOR predecessors are retained. None is1 for AND,0 for OR.
The inner r>=1 hypothesis supports exponent monotonicity over skip wires. The
final t=0 is legitimate but its error bound is vacuous; it is not used for1/3.
A bound S may conservatively count unused inner nonlinear nodes. H is the max
nonlinear depth of SELECTED root children, not every node or total gate layers.

At the SAME r satisfying both hypotheses, the previous all-node construction
would give degree r^(H+1), whereas this root construction gives2*r^H. For r>2
this saves the factor r/2. Comparing the smallest separately admissible r values
is different: 12*S<=2^r is stronger than 3*(S+1)<=2^r. No pointwise dominance
for every small S,H, or optimum constant12, is claimed. Graveyard053 explicitly
refutes reusing the old inner-only hypothesis and omitting the root degree factor.

## Primary-source comparison

N. Limaye, A. Srinivasan, S. Srinivasan, MFCS2025 article67,
https://doi.org/10.4230/LIPIcs.MFCS.2025.67 . The official PDF was retrieved and
pages67:6 and67:8 visually inspected in this session. It measures circuit size
by wires and depth by all layers; Lemma10 records a more randomness-efficient
approximation bound, and Lemma11's argument budgets a final OR separately.
This motivates our root choice but does not certify our constants or model.
We do not reproduce that paper's full sampler or silently replace its parameters
by original nonlinear-node count and nonlinear depth.

## What is actually checked

The new module changes no old proof or definition. A lexical scan is a useful
sanity check, not a kernel result. Strict build, unchanged namespace axiom audit,
16 explicit new reports and3 explicit endpoint signatures are required for
acceptance. Finite exact controls compare separately written sparse-polynomial
and Boolean evaluators by the SAME author. The small domain is n,K0..2 with
zero/one inner node and one root, r1/2,t0/1/2, plus six deeper cases. None of
these finite counts proves the arbitrary-parameter theorem or its translation.

## Decision

At a successful root milestone, park constant-polishing and generic sampler
abstractions. The concrete next question is the gap between high probabilistic
degree as a large property and an efficiently recognizable useful property.
See next-frontier.md. This is a structural barrier audit, not an assertion that
this restricted-circuit reconstruction settles P versus NP.
