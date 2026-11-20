# A private bounded-fanout compiler and its exact error charge

This is an independent written audit of the proposed continuation of Issue 33.
Its input is a fixed-projection field verifier with the physical cell semantics
of Expeditions 038 and 043. The proof below supplies a compiler theorem with
explicit hypotheses. An implementation still needs to verify those hypotheses
for its actual query list and count its actual storage. Mathematical novelty
and proof-kernel acceptance are unassessed.

## Hypotheses and construction

Let the uniform public seed range over N = 2^k points. At one center z, a
deterministic Boolean DAG with G binary AND/XOR gates computes the original
field verdict from physical proof bits, a constant-one cell and k public-bit
cells. Every wire may occur positively or negatively. Constants can be folded.
Every gate, public-bit cell and constant cell is private to its center. Physical
field cells may be shared. The output assertion counts as a terminal use of its
wire. Count input ports with multiplicity, including two uses of the same wire
in one gate. The public bits are enforced by the two clamped pin templates per
coordinate from Expedition 038.

For the used physical input maps q_j, require an action tau_z by bijections on
canonical physical addresses such that q_j(z) = tau_z(q_j(0)). Bit index and
tree identity are part of the address. Deduplicate maps by their canonical
value at zero. Equality there implies equality at every seed. Inequality there
also implies inequality at every seed by injectivity of tau_z. Thus after this
deduplication a physical bit is read by at most one distinct input map at any
center. Let mu be the maximum number of centers reading any one physical bit.
This is a property of the query geometry and includes all outer reads.

The action is the original-token translation action proved in Expedition 042.
Raw strings before following parent/sibling aliases are insufficient keys.
Return guards, tree identities and bit indices must be retained. Root extension
bits known to be zero are constants, rather than physical inputs. Additional
fixed XOR calls still obey the action by replacing q_j(0) with q_j(h).

Fix a fanout cap f >= 2. Put one private copy buffer after each distinct used
physical input map at every center, even when that input has only one use.
Replace all its consumers by uses of this buffer. For every buffer and every
other driver, split its d downstream occurrences through a private copy tree
of fanout at most f. A source with d occurrences needs

    r_f(d) = max(0, ceil((d-f)/(f-1)))

additional copy nodes beyond its root. Each added copy uses one port and
supplies f new ports, increasing capacity by f-1. A chain or balanced tree
achieves the displayed count. All copies store the unsigned Boolean value.
Retain the original literal signs on the rewired uses. This avoids new NOT
gates. Treat the output assertion as one of these occurrences, or give it a
dedicated final private copy. Unused physical input declarations need no buffer.

Every new query reads a fixed gate row at z. Existing physical queries are
preserved. The construction has no conditional alias choices based on stored
proof values or untrusted public-bit copies.

## Why the actual canonical queries obey one action

Track each of the k original seed coordinates as a labeled token. A row step
saves the high live tokens in its edge label, retains the low ones in the child
and appends fresh constants. A column step saves the low ones and fresh
constants in its label and retains the high ones in the child. Thus the saved
labels and live point jointly contain every original token exactly once.
A fixed leaf XOR slot changes a fixed subset of these token bits and fresh
positions, without deleting or duplicating any token.

On a row return the membership guard examines only that edge's appended fresh
positions, possibly flipped by the fixed slot. Consequently its truth is fixed
across all seeds. A successful parent return drops those positions and restores
the saved high tokens to their original place. A column return redirects to a
row sibling, using its live high tuple for the sibling label and its saved low
tuple for the point, with constant auxiliary bits and rectangle marker. This
matches the token ordering reached by a genuine row edge to that same sibling.
Every return restores the canonical ordering appropriate to its physical owner.
The ultimate owner shape and stop depth therefore depend on the chosen slot,
fresh tape and shifts, while all its saved labels and point together still
contain each original token once.

For any canonical owner address, define tau_z by toggling its original-token
positions by the corresponding bits of z, preserving all fresh positions,
tree/shape headers and bit-of-symbol index. The same canonical cell receives
the same action from either of its possible raw routes. It is an involution
and tau_z tau_w = tau_(z XOR w). In particular it is a bijection. Replacing
the initial all-zero seed by z makes exactly these toggles, proving
q_j(z) = tau_z(q_j(0)) for every slot and every seed. This is a token and
canonical-address induction, independent of finite enumeration. The outer
field translations have the same action on the root addresses. Each address
bit is a constant or one possibly complemented seed bit, as required by the
signed-projection interface.

## All-error inequality

Fix any satisfying YES proof and its truthful new private gates and pins.
For any other global assignment, let e_u be the indicator that cell u differs
from this reference. Gate-equivalence clauses obey the following pointwise
inequalities, where F_gate counts actual failed clauses with multiplicity.

    XOR(a,b,c)       F_gate <= e_a + e_b + e_c.
    AND(a,b,c)       F_gate <= e_a + e_b + 2 e_c.
    COPY(a,c)        F_gate <= e_a + e_c.

They hold for every satisfying reference tuple and every replacement tuple,
including signed inputs. Complementing a literal preserves its error indicator.
An XOR definition has at most one failed clause. For AND, errors in inputs can
be charged once and an erroneous output at most twice. A copy constraint has
one failure exactly when its endpoints disagree. Equal addresses in different
ports may be counted twice on the right, consistent with the fanout definition.

Every physical field bit appears only in the input side of one copy constraint
per reading center. Its total coefficient is at most mu. An AND output has own
coefficient at most two and at most f consumer charges. XOR/copy outputs have
own coefficient at most one. A constant-one cell has one unit-pin charge. A
public-bit cell has exactly two clamped-pin failures per erroneous physical
cell, plus at most f local consumers. The output assertion is already a counted
use. Therefore, for every error set E in the entire padded proof cube,

    F(E) <= max(mu, f+2) |E|.

This includes simultaneous errors in physical inputs, private gates, copies,
constants and pins. Unused addresses can only increase |E|. It is an inequality
on one global proof replacement, with no independence assumption.

There is a matching physical-input attack when mu is attained. Flip one such
physical bit and leave every buffer and gate at its truthful value. Exactly
one copy clause fails per reading center, and no other constraint reads the
raw cell. Thus F(E) = mu for this one-bit E. If mu >= f+2, the unrestricted
signed sensitivity of the entire new compiler is exactly sigma = mu. This
conclusion uses the mandatory buffers and the absence of other raw physical
constraints. A directly pinned physical input would need its extra charge.

## NO minimum survives because copies remain private

Fix an arbitrary physical field proof, before choosing its auxiliary gates.
Let rN be the number of seeds on which the original public field predicate
rejects. At a rejected center with correct public pins, either a local
definition/copy clause, the constant-one unit, or the output assertion is false.
If the constant-one cell is wrong, its unit already provides the local charge.
If all local clauses were satisfied instead, the whole DAG would evaluate
truthfully and accept, a contradiction. These
violations use distinct clause-seed pairs at different centers. At centers
with wrong public bits, the clamped pins contribute twice the number of wrong
bit cells, at least the number of such centers. Hence all auxiliary choices
incur at least rN violations. Truthful copies, gates and pins attain exactly
rN, solely at the output assertions. Taking a minimum over the same physical
field-proof space proves

    V_NO = gamma_field N.

A cut of a private copy tree can excuse only its own center. Sharing a copy
tree across centers would invalidate this argument and is excluded here.
The claim also requires center-indexed public pins, with shifted public seed
values derived by fixed complements within each center's circuit.

## Storage and clause count

The original total downstream demand is U = 2G+1. For a physical source with
d >= 1 demands, its mandatory buffer plus its split nodes cost
1+r_f(d) <= d. All other split costs are at most their demands. Thus the total
number C of new private copy rows satisfies C <= 2G+1 for every f >= 2.
There are precisely two new equivalence clauses per copy, so M' = M+2C.
All quantities count real signed templates, with duplicates retained.

When the original storage is explicitly organized as S seed rows and includes
the constant row, S >= G+1 and S' = S+C <= 3S. Its enclosing power-of-two cube
then grows by at most a factor four.

The same Q' <= 4Q conclusion does not require repacking dynamic raw addresses.
Keep the entire old Q = 2^m cube under the new prefix 00. The old private gate
rows and constant row are disjoint N-cell sets, so (G+1)N <= Q. At most
(2G+1)N < 2Q cells are needed for the copies, each in a new row addressed by
its fixed identifier and z. Old storage plus new rows fits in the 4Q cube.
Old queries receive constant prefix bits and new queries are projections.
This proves a storage budget even when the old raw addresses interleave seed
tokens and fresh positions rather than using simple contiguous row tags.

## Geometry and scope of mu

For one unamplified RS call at rate a, the physical incidence theorem of
Expedition 043 gives B_a = 2^(2a)+2^a-1 reading centers per symbol. Each symbol
bit has the same incidence. With two distinct root trees and additional outer
read maps, one safe bound is max(B_aA,B_aB) plus the total number of outer read
maps. Duplicating coincident outer maps only overestimates it. Fixed rates make
the two B terms constant. The outer read count can still grow with k.

For t distinct translated calls the physical cell's reader set is S_y+H,
where S_y was its base reader set. Therefore mu_H is bounded by t times the
base RS incidence plus the once-only outer reads. It is also bounded by N.
Per-center map deduplication does not turn this into an H-independent bound.

## Precision comparison

For a fixed YES reference, let sigma be the largest F(E)/|E| over all nonempty
Boolean error sets. A distribution of degree-bounded global polynomials with
mean uniform bit error eta gives expected raw failures at most sigma Q eta.
One member stays below the NO minimum whenever

    eta < V_NO/(Q sigma).

This uses raw failed-pair counts and an identified common NO threshold.
If the YES and NO instances have different template counts M, do not compare
their normalized rejection fractions to one identical normalized threshold;
multiply each normalized count by its own known MN. For an instance family,
use a uniform YES sensitivity bound, a compatible common address cube and
the minimum NO raw count. A favorable pair alone gives no family-wide bound.

All queries after the transformation remain signed projections, so composing
a common degree-d polynomial with each three-literal clause retains degree at
most 3d. The number of templates increases by a constant factor. The input width
increases by at most two bits. These preserve the stated polynomial resource
form, while proving no new approximability hypothesis. The approximation must
target the new encoded proof function. An approximator of the old truth table
does not automatically approximate the new copy rows. The exact sensitivities
here allow arbitrary error sets; their singleton extremizers need not be
available under a separately imposed low polynomial degree.

The new compiler has a guaranteed threshold at least
gamma_field N/[4Q max(mu,f+2)]. The old fiber-only estimate was
gamma_field N/(6 M Q). This improves that sufficient estimate when
6M > 4 max(mu,f+2). To compare against the old actual linear threshold, use a
lower bound L on its actual sigma and the measured cube ratio R = Q'/Q.
The ratio of new to old thresholds is at least L/[R max(mu,f+2)]. If mu >= f+2,
the denominator's sensitivity term is exactly mu. There is no universal gain
claim when the numerical ratio is at most one or the geometry hypotheses fail.

At the Expedition 040 fixture, mu = 128. The old one-cell attack has 288
failures, and a separately replayed true-literal allocation supplies the
matching upper bound for the specified honest reference. Cap f = 126 gives
sigma' = 128 and fits the same cube on both instances, yielding exactly 9/4
improvement in this comparison. Cap two has the same exact sensitivity but
crosses one power-of-two storage boundary, giving 9/8. The [actual census and
finite allocation](actual-instance.md) supply these numbers; they are not
consequences of the generic fanout theorem alone.

## Adversarial boundaries

Omitting the mandatory physical buffer lets an input appear in several local
gate constraints and breaks the mu coefficient. Deduplicating raw path names
before aliases breaks the one-buffer-per-physical-map premise. Reusing a copy
at different centers breaks the per-center NO charge. Excluding the terminal
assertion from the fanout count can overcharge a public-bit output. Ignoring
literal multiplicity at a repeated input can also undercount fanout. Applying
the base B_a bound to a translated bundle ignores its union of reader sets.
All of these restrictions concern the construction being proved, rather than
external approval or a new research gate.
