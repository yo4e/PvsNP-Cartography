# Field amplification, gate sharing and fixed-input bit precision

Status is a written derivation with small exact compiler controls. All statements
below hold for one fixed physical field proof. When a minimum over field proofs
is taken, the argument identifies that step. Novelty and formal verification
remain unassessed. The setting is the compiler in Expedition 038 and the
once-evaluated residual in Expedition 042.

## The quantity required by the existing transfer

Let N = 2^k be the number of public seeds, Q = 2^m the full Boolean address cube,
M the number of signed clauses, and gamma the minimum field rejection fraction
at the fixed NO instance. Private per-seed computation gates, one output-true
clause and the prescribed public seed pins give minimum clause rejection
gamma/M. Every clause occurrence map has fibers of size at most two, so the
current union-bound transfer suffices when the fixed-input uniform proof-bit
error eta satisfies

    eta < beta = gamma N / (6 M Q).

Both the number of clauses and every padded address count belong in this
quantity. Increasing field rejection alone does not decide whether beta grew.
This is a sufficient precision threshold of this particular transfer, rather
than an optimal approximation theorem. [Compiler](../038-recursive-query-fibers/source-compiler.md)

Let H contain zero and t = |H|. At a fixed field proof, the original predicate
is the conjunction of the outer constraint and its two proximity predicates.
The new predicate repeats only proximity predicates at x+h and evaluates the
outer constraint once at x. Its failure set is contained in the union of the
t translates of the original failure set. Consequently r_H <= t r_1 on every
field proof, and gamma_H <= t gamma_1 by evaluating the new verifier on a
minimizer of the old rejection. The field-proof space is the same, with every
physical alias retained. Thus

    beta_H / beta_1 <= t M_1 Q_1 / (M_H Q_H),

when gamma_1 > 0. If gamma_1 = 0, a zero-rejection proof passes every translated
call as well, so gamma_H = 0. A proof of no improvement follows whenever
M_H Q_H >= t M_1 Q_1. This criterion can be used before selecting a sampler.

For an unpadded seed-row model, write M_t = t c+b and S_t = t g+d. Here c and g
are the incremental clause and gate-row costs per copy, and b and d count
shared work, including a once-evaluated outer constraint, proof storage and
pins. Connector costs must be included explicitly. If they are affine in t,
their slope and intercept can be absorbed in these symbols. The identity

    (tc+b)(tg+d) - t(c+b)(g+d) = (t-1)(t c g-b d)

gives the exact product-cost threshold. Under positive c,g and nonnegative
b,d, the upper envelope t/((tc+b)(tg+d)) is maximized at
sqrt(bd/(cg)) when that value is at least one. Shared overhead can therefore
allow a bounded gain from amortization. It prevents a blanket theorem saying
every replicated compiler loses. With exact cube padding use
Q_t = N times 2^ceil(log2 S_t) and the preceding product criterion directly.
No hypothetical counts replace a census of an implemented compiler.

Full independent copies that also duplicate the whole old address block have
M_H >= t M_1 and Q_H >= t Q_1, including output constraints and pins in each
copy. Their sufficient bit-error threshold is at most beta_1/t. One may save
shared overhead, but that is a different layout with its own count.

## Independently scored copies do not use the expansion of H

If each copy has its own output-true constraint instead of a final shared
AND output, the sum of its truthful output failures over all copies and seeds
is exactly t r_1 N for copies of the complete base predicate. Translation
is a permutation of the seed cube, so this count is independent of H.
With private computation tables, honest pins and a fixed field proof, the
minimum over gate tables is exactly this count. Every rejecting copy needs a
local clause failure, and correct computation attains it at its output unit.
For replicas sharing public seed pins, that equality requires additional
care: one corrupted pin can influence several copies while its unit checks
are only paid once. Retaining honest pins gives the stated upper bound;
the lower bound then needs the pin weights or a public-input treatment.

In the once-only outer-constraint variant, separate scoring gives the sum
of the outer rejection count and t times each proximity rejection count.
Its dependence on masks is again absent. Any improvement obtained merely by
changing t comes from the clause/address accounting, not from small bias.

## Sharing translated computation tables loses the amplified numerator

Consider an exact finite decision-table variant. Supply f(z) through one
physical input row queried at the unmodified seed address, and hold that row
fixed while minimizing over auxiliary tables. Thus this interface uses fixed
projection queries even when the values of f vary arbitrarily with z. Let
E = {z : f(z)=0}. Introduce one shared decision
buffer b(z), constrain b(z)=f(z) by the two ordinary copy clauses, and at every
center x use a private AND circuit requiring every b(x+h) to be true. Use one
output-true clause at that center. Every copy and private AND circuit has the
usual gate-equivalence clauses. Their queries are fixed XOR translates.

If Z = {z : b(z)=0}, the copy clauses fail exactly |E symmetric-difference Z|
times. The minimum over private AND gates and output tables is |Z+H|. Each
center touching Z either computes false and violates its output unit, or
violates a definition clause. Correct computation realizes one failure there.
Therefore the optimum total number of failed clause-seed pairs is

    min_Z (|E symmetric-difference Z| + |Z+H|) = |E|.

For the lower bound, zero belongs to H, so |Z+H| >= |Z| and
|E symmetric-difference Z|+|Z| >= |E|. For attainment, store b=1 everywhere and
compute every private AND truthfully. Each originally rejected seed violates
exactly one copy clause, and all final outputs pass. The enlarged field test
can reject every center although this compiler still has only |E| violations.
For example, one failed point on the four-point cube and all four shifts give
four field rejections but a one-clause optimum.

The same upper bound extends when f is computed by a shared base circuit.
Store its actual internal values and put a copy buffer after its actual output.
Changing the buffer at each rejected seed costs exactly one copy clause.
The matching lower bound holds when the shared base circuit is checked once
at its own seed z, each private aggregate is a literal AND of the fixed
addresses b(z+h), and every base/public pin is indexed by that same base seed.
At an originally rejected seed z with all its public inputs correct, either
some base definition/copy clause fails at z, or b(z)=0. Because zero belongs
to H, the latter forces one aggregate/output failure at the distinct center z.
These clause-seed pairs are disjoint across z and across the base/aggregate
categories. If the public inputs at z are wrong, charge that seed instead to
a wrong pin. In the exact clamped-pin construction each erroneous bit at its
physical seed is read by two pin-clause seeds, so the total pin failure count
is twice the number of erroneous bit cells, at least the number of bad seeds.
This proves the same lower bound |E|. Every pin in the attaining assignment is
truthful. The extension does not assert this property for arbitrary table
sharing, shared aggregates or adaptive address calculations.

For a fixed, once-evaluated outer predicate with failure set A, the simple
one-RS-buffer model has the exact optimum

    min_Z (|E symmetric-difference Z| + |A union (Z+H)|).

It lies between |A union E| and |A|+|E|. The lower bound follows by charging
every point of A, and every E-point outside A either to the copy or to the
aggregate. The upper bound uses Z empty. For two shared proximity computations
and one separately scored outer predicate, truthful base gates and falsified
RS buffers give an upper bound |A|+|E_1|+|E_2|, at most three times the old joint
failure count. This is enough to defeat a claim that table sharing inherits
the amplified field numerator at the same consistency cost.

## A cost that can distinguish a useful continuation

The exact signed-error constant C_OR from Expedition 036 gives sufficient
eta < (gamma/M)/C_OR. Define Lambda = M C_OR. The threshold becomes gamma/Lambda,
so the clause normalization cancels if actual signed sensitivity is used.
Repeated reads of one physical cell and the literal signs both affect that
sensitivity.

For a fixed satisfying canonical proof and an error set E in its Q Boolean
addresses, let F(E) be the actual count of failed clause-seed pairs after
flipping exactly E, with duplicate clauses counted. Define

    sigma = max over nonempty E of F(E)/|E|.
    C_OR = Q sigma / (M N),   Lambda = Q sigma/N.
    eta < gamma N/(Q sigma).

These identities follow directly by dividing failure density F(E)/(MN) by
uniform error |E|/Q. A single output-cell flip gives sigma >= 1. The crude
fiber accounting gives sigma <= 6M, since a clause has at most three occurrence
slots and each physical address has at most two preimages in a slot. Removing
M from the numerator of this estimate requires a bound on the total physical
load, not merely its maximum fiber in each individual slot. The exact sigma
supremum can use a high-degree error pattern, so it is not asserted to equal
its degree-restricted counterpart. [Signed-error characterization](../036-query-capacity/capacity-and-transfer.md)

Gate sharing has an additional cost visible in sigma. On a satisfying all-one
base-decision table, flip a single shared copy buffer b(z) from one to zero
while keeping all private AND gates at their honest value one. Its copy
constraint fails once. At each of the t centers which reads this buffer,
exactly one AND input-implication clause fails. For the decision-table variant, sigma = t+1 over **all** private AND-gate and
buffer error sets for this all-one reference. This equality also holds if
errors may change its physical input row f, as the extra charging below shows. Assign every gate-equivalence clause to a distinct true literal as
follows. An AND clause with its output positive is charged to that output;
its two input-positive clauses are charged to their respective inputs. Charge
the buffer-positive copy clause to its buffer and the output unit to its
output. If the input row f is included among the changeable addresses, charge
the other copy clause to its sole true literal f(z). Each input cell is
charged once, each buffer t+1 times and each private AND gate twice.
A false clause requires an error at its charged address, giving the upper
bound t+1. The one-buffer flip attains it. Errors at unused addresses only
increase the denominator. For a full translation of all-one inputs these
counts are independent of the mask geometry.

These exact sensitivity and cost conclusions apply to the decision-table
variant. Conditional on a fixed NO decision table with rejection r_1 and the
all-one YES reference, its auxiliary optimum is r_1/M and its signed-transfer
threshold is r_1 N/(Q_t(t+1)). Relative to its t=1 version the threshold ratio
is 2 Q_1/(Q_t(t+1)), at most 2/(t+1) when storage is nondecreasing. The table
variant alone does not enforce a NO restriction on f, so this is a conditional
compiler comparison, not standalone soundness for arbitrary input rows.

When f is produced by a shared base circuit, the earlier auxiliary cheating
assignment still applies and the same buffer flip proves sigma >= t+1. Errors
in the base circuit's gates, pins and physical inputs may make sigma larger.
Equality sigma = t+1 is not asserted for that extension or for the entire RS
compiler. The decision-table calculation identifies a cost which the richer
compiler must include.

More generally take full translated replicas of all base clauses, with a
shared physical-input address region but separate gate tables. For an error
set E confined to the shared physical-input region, with all gate and pin
cells kept at their honest values, translated copies have exactly the same
failure count. Thus F_t(E) = t F_1(E), and the maximum physical-input-only
ratio sigma_t_phys equals t sigma_1_phys. This is an exact counting identity
from translation invariance. It can force amplification costs even when
shared-gate fanout is avoided. For a once-only outer predicate the identity
becomes F_t(E) = F_outer(E)+t F_RS(E). A general conclusion about sigma_t
requires also checking errors in gate/pin cells and mixed error sets.

The concrete next objective is to determine gamma/sigma, including the
actual address ratio N/Q, for a compiler choice. This distinguishes a useful
improvement from merely increasing field rejection. It preserves the earlier
uniform-error problem, the one-global-polynomial requirement and the finite
Boolean occurrence semantics. It also exposes exactly where a better code
or weighted consistency scheme would have to change the analysis.

For a changed compiler, use its actual minimum V_NO of failed clause–seed
pairs over all global tables at a specified NO instance. At a satisfying YES
reference pi, use sigma_YES from its actual signed clauses. The corresponding
sufficient precision is V_NO/(Q sigma_YES), with the appropriate min/max
quantifiers retained for a family of instances. Only the established private
single-output encoding justifies substituting V_NO=gamma_field N. A shared
encoding cannot assume this equality after the cheating assignment above.
This is the exact next target in [Issue 33](https://github.com/yo4e/PvsNP-Cartography/issues/33).

## Finite verification

The checker enumerates all 128 choices of base failure table and zero-containing
mask set on a four-point cube. It directly evaluates the two copy clauses and
all assignments to private AND gates and verifies the exact |E| optimum.
It checks all 120 nonempty buffer-error sets against the t+1 sensitivity count.
For every zero-containing mask set of size at most three, it also evaluates
all 13,065 nonempty subsets of both buffer and private AND-gate cells, obtaining
the exact sigma = t+1 maximum each time.
It also checks all 2,048 choices with a separate outer failure table, and 3,125
integer cost-model parameters for the product identity. The padded count
examples illustrate possible amortization and replica-dominated loss; they
are accounting models rather than actual recursive RS gate counts.

The code uses explicit checks which remain active under Python -O.
All general claims above are proved in the text; bounded enumeration checks
the formulas and the gate semantics. [Checker](check_compiler_cost.py)
