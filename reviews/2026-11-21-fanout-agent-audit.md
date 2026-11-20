# Independent attack on the actual private-fanout continuation

This review checks the construction and the actual certificate code for the
Expedition 040 Boolean compiler. It does not replace the integration author's
rerun or the final GitHub read-back. The written compiler theorem is in the
companion bounded-fanout note. No novelty or proof-kernel acceptance is claimed.

## Mixed errors, literal signs and physical aliases

The copy transformation counts every gate input port and the output assertion
as uses. It leaves each original signed literal's sign intact. Every used raw
physical input map receives a mandatory private copy, including maps of demand
one. Its remaining consumers use that buffer. The private splitting routine
reserves one fanout slot for its next copy before assigning the other slots to
old consumers. Its recurrence is therefore exact even at the cap boundary.

The original physical key consists of tree/block, page, symbol-bit index and
XOR seed offset. The physical address map is (canonical tag, seed XOR offset).
Keeping the tag and offset keeps every alias. Per-center deduplication by the
seed-zero address is valid only under the common bijective translation action;
it must not be applied to unrelated pin maps or uncanonicalized path strings.
The current compiler keeps the original physical keys and independently checks
that their final reads are unchanged.

For arbitrary satisfying references and arbitrary simultaneous errors, the
local inequalities are

\[
F_{\rm AND}\le e_a+e_b+2e_c,\qquad
F_{\rm XOR}\le e_a+e_b+e_c,\qquad
F_{\rm copy}\le e_a+e_c.
\]

Signed inputs have the same error indicators. Repeated inputs require both
port charges; the implementation counts them. The XOR inequality is a local
truth-table fact: any invalid tuple violates exactly one of its four clauses.
It need not arise from a static one-true-literal allocation of all four clauses.
Confusing these two forms of certificate would incorrectly cost XOR outputs.

The mandatory buffer makes the physical coefficient exactly one per reading
center. A private AND output costs at most two for its definition and at most
the cap for its consumers. Pins cost two per wrong physical bit plus consumer
uses. Constants have their own unit cost, and the output assertion is already
a consumer. Thus cap 126 and maximum physical readership 128 give an all-error
upper bound 128. Flipping a physical A bit while retaining the old buffers
violates 128 copy clauses, attaining the bound. Padding cannot increase it.

## The exact old-reference sensitivity certificate

The actual old satisfying reference has a one-cell attack of weight 288. The
new allocation routine also certifies an upper bound of 288 for every error
set, without assuming that singleton maximization always suffices.

`singleton_loads` assigns every clause-seed pair with exactly one true literal
to that literal's actual physical address. It also includes both occurrences
of every clamped public pin. `greedy_true_certificate` then iterates all pairs
with at least two true literals and assigns one actually true physical literal.
Its local check verifies the stored reference bit and sign. It retains literal
and clause multiplicities; alias consistency is checked when the reference is
packed. A false clause after any set of flips must have lost its selected true
literal, so the maximum assigned load bounds the actual failure count per flip.

The reported mass is 10,706,688, precisely all old clause-seed pairs. The
completion visits 2,458,096 multiply satisfied pairs. The maximum final load
is 288, and a direct physical-address replay attains 288. Its regeneratable
completion-address stream has SHA-256
`becc1e2eeaf805be83f5e92cab6fbdbc92b7ec0315a22ea4bafed255bf39e81c`.
Consequently the old sigma is exactly 288 for this specified reference.
This is not a claim that the same number is the maximum over all possible
satisfying references or every member of an instance family.

## NO value, counts and the actual comparison

All added copies remain private to a seed. Holding the physical field proof
fixed, a rejected seed with correct public inputs needs a local clause or
output violation. Wrong public inputs have their independent clamped-pin
charge. This lower bound survives any combination of gate and copy errors,
because different seeds do not share those private rows. Truthful evaluation
attains one output violation per rejected seed. The proven field minimum 109
therefore remains the actual auxiliary/field minimum in this fixture.

At cap 126 the YES circuit has 24,526 used physical rows and the NO circuit
24,551. Both fit in 32,768 rows of 128 bits, giving the same
Q = 4,194,304 as their old encodings. Both use 2,603 new copy rows. Their
template counts differ: 88,852 for YES and 88,937 for NO. The new exact
sensitivity 128 gives 109/536,870,912 as the raw-count linear precision
threshold. Against the old exact 288 at the same Q, the ratio is exactly 9/4
for these specified references and instances. Cap two crosses a storage
boundary and gives ratio 9/8 instead.

The comparison uses raw failed clause-seed counts. One may normalize an
instance's counts and multiply by that same instance's MN; this removes M
from its sensitivity expression. If instead imposing a single normalized
rejection cutoff on circuits with unequal template counts, a factor involving
those counts must be retained. The raw-count convention and the chosen
YES/NO/family quantifiers should be explicit.

Two proposed shortcuts fail executable mutation controls: removing the
mandatory physical boundary copy gives a 250-failure singleton, and removing
one private fanout split gives 199. Both exceed 128. These controls distinguish
the actual construction from a functionally equivalent honest evaluator with
an incorrect error bound.

## Remaining scope

The result changes a compiler's sufficient linear precision requirement. It
does not supply a low-degree global approximant, bound the degree-restricted
signed optimum, amplify the field rejection, or prove a complexity separation.
For a family, retain the appropriate NO minimum and YES maximum and count each
member's padded cube. Translating multiple calls can increase physical reader
incidence; the unshifted readership bound must not be silently reused.
