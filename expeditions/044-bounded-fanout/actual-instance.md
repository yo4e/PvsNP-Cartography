# A private-copy compiler with a measured proof-bit precision gain

The actual GF(128) compiler of Expedition 040 admits a finite precision improvement through private copies. The chosen implementation caps nonphysical fanout at 126 and reads each distinct physical input map only into its own copy root. Its unrestricted signed sensitivity is exactly 128. On the existing honest YES reference the original sensitivity is exactly 288, certified by a true-literal allocation and an attaining single-bit error. The padded Boolean address cube stays at 4,194,304 bits and the NO minimum stays at 109 failed clause–seed pairs. Thus the sufficient uniform-bit error threshold increases by a factor 9/4 in this fixture comparison. [Original compiler](../040-recursive-verifier/compiler.md) · [NO minimum](../040-recursive-verifier/soundness.md) · [Precision being compared](../043-dispersed-shifts/compiled-cost.md)

The original YES reference uses A(X)=1+X, B(X)=X and the honest shared bivariate extension, with every public pin and computation gate filled truthfully. The signed-error quantity is sigma=max_(E nonempty) F(E)/|E| over arbitrary physical Boolean error sets. It counts every clause–seed occurrence with its multiplicity. The old value 288 applies to this specified reference. The new 128 bound applies to every satisfying reference for the new layout, because the local charging argument below is independent of the particular true gate values.

## The implemented transformation

Every old input key (block,page,bit,delta) still denotes the same physical bit at z XOR delta. Distinct wires with the same tag retain their original aliasing. Insert one private copy root for each used key. Its two clauses enforce v=u, with u the original physical read and v a fresh row at z. Only this copy definition reads u. Redirect every old use of this input to the root or one of its private copy descendants, preserving the sign of the literal.

For every original nonphysical driver, retain its defining gate and split its outgoing uses through private copies if its fanout exceeds the chosen cap f. Count the final output assertion as one outgoing use. The shared constant has its existing unit pin, and each public bit retains its two clamped unit templates. Their copy descendants receive ordinary private rows. All new rows are indexed by the unchanged public seed z. Their query maps are fixed signed projections, and a copy's physical input map is exactly the old map.

For d outgoing uses, a nonphysical driver needs max(0,ceil((d−f)/(f−1))) copies. A physical map needs one mandatory root plus that quantity. The implementation gives f−1 uses to the current node and one edge to the next copy until the final node can supply the remaining uses. It verifies the actual resulting fanout after rewriting. This construction preserves the original AND/XOR operations, including signed inputs and the final output literal. The circuits can be evaluated in a topological sequence.

## Rigorous sensitivity bound for all physical error sets

At an honest reference let e_u be one when physical bit u is flipped. For a gate whose output is a distinct private cell, direct Boolean equivalence gives these bounds on the number of failed definition clauses.

| Gate relation | Upper charge |
|---|---|
| v=u AND w | e_u+e_w+2e_v |
| v=u XOR w | e_u+e_w+e_v |
| v=u | e_u+e_v |

The input charges count occurrences, including repeated or oppositely signed aliases. Negating a literal preserves whether its underlying bit was flipped. An AND with reference inputs and output 000 changes to 001 when only the output is flipped, violating two clauses. The factor two on that output is necessary. A constant or final-output unit has charge one. The clamped public pins cause exactly two failures per erroneous public-bit cell over their two templates and all seeds.

For a new private driver the total charge is at most f+2, including its own definition or public pins. A physical input map feeds one copy definition, at charge at most one. Its XOR map is a bijection on the 128 seeds. At any one physical input cell the number of such incoming charges is the number mu of distinct used maps for its tag.

In this actual compiler, each A bit has all 128 XOR offsets. A B root bit has eight, each nonrectangle extension bit has eight, and each common-rectangle bit has 8+16−1=23 distinct offsets. The overlapping zero offset is counted once. Therefore the maximum physical input charge is mu=128. Padding cells contribute no failures. Summing the local inequalities proves

    F(E) ≤ max(128,f+2)|E|

for every error set, including mixed changes in field, gate, copy, constant, public and padding cells.

At either f=2 or f=126 this upper bound is 128. Flip one A bit while retaining every copy and private gate at its honest value. Its 128 distinct read maps each violate exactly one copy-equivalence clause at one seed. Every other clause retains its honest values. This attains 128 failures and proves exact sigma=128. The construction and proof do not assume errors are independent, or that an error pattern has low polynomial degree.

## The original 288 is also an exact finite certificate

For the original YES reference, the checker computes F({u}) at every used physical address. A clause contributes to that count precisely when the flipped address supplies all of its initially true literal occurrences. The original ordinary templates have distinct physical maps within each clause, which the checker verifies. The clamped public pin contribution is added with its exact multiplicity two. The maximum is 288 at A(126)'s least significant bit. Direct packed evaluation and a scalar evaluation of every clause–seed pair touched by that address both give 288.

For the matching upper certificate, assign every satisfied clause–seed pair to one physical address supporting an initially true literal. Begin with all sole-true-literal assignments. For each remaining pair, choose its currently least-loaded true address, with ties resolved by the original literal order. The checker verifies the truth of each selected literal at its actual physical address. The completed assignment has maximum load 288 and total mass 10,706,688, equal to every original clause–seed pair including constant, final-output and public-pin units.

If an arbitrary error set makes a clause false, the clause's assigned initially true literal must have been flipped. Consequently F(E) is at most the sum of the assigned loads on E, at most 288|E|. Combined with the attaining singleton this proves sigma=288 for this reference. The stored output contains the deterministic replay's mass, maximum load and SHA256 of its 2,458,096 greedy completion addresses. The entire allocation is regeneratable from the pinned source, reference and rule. Only the digest and replay code are stored; no full allocation file is asserted.

## Actual census and the selected cap

| Layout | YES copies | YES used rows | YES clause templates | NO used rows | NO clause templates | Padded address count Q |
|---|---:|---:|---:|---:|---:|---:|
| Original | 0 | 21,923 | 83,646 | 21,948 | 83,731 | 4,194,304 |
| Fanout cap 2 | 18,042 | 39,965 | 119,730 | 39,999 | 119,833 | 8,388,608 |
| Fanout cap 126 | 2,603 | 24,526 | 88,852 | 24,551 | 88,937 | 4,194,304 |

The unchanged original binary gate counts are 3,582 AND and 18,221 XOR on YES, and 3,597 AND and 18,231 XOR on NO. For cap 126, both circuits add 903 copies downstream of A maps, 1,680 downstream of B maps, four downstream of public bits, and sixteen downstream of original gate outputs. There are 2,576 used physical input maps, so the total includes their mandatory roots and 27 additional copies. The cap 2 NO circuit has 18,051 copies. All counts come from the generated circuit and final physical tag layout.

The cap 126 choice follows the physical A sensitivity 128. Reducing all fanouts to two already leaves that term dominant and crosses a padding boundary. Both versions are retained as controls. For these two choices and the specified reference, the precision values are

| Layout | V_NO | sigma_YES | V_NO/(Q sigma_YES) | Ratio to original |
|---|---:|---:|---|---|
| Original | 109 | 288 | 109/1,207,959,552 | 1 |
| Cap 2 | 109 | 128 | 109/1,073,741,824 | 9/8 |
| Cap 126 | 109 | 128 | 109/536,870,912 | 9/4 |

These are strict sufficient error thresholds, eta<V_NO/(Q sigma_YES). The decision functional is the raw number of failed clause–seed pairs, with common threshold 109 for this YES/NO fixture. YES and NO have different M; their normalized rejection probabilities are not compared against one identical normalized threshold. A normalized count must be multiplied by its own known MN first. This convention is why no unequal-M factor is silently dropped. It does not substitute a field rejection fraction for an arbitrary compiler's soundness count.

## Why the NO minimum remains 109

Fix any global field table. At a seed with correct public bits, correctness of every copy and original gate definition forces the original field verdict. A rejecting field seed therefore creates at least one ordinary failure at that seed, unless some public input there is wrong. Each wrong public-bit cell causes two failed pin-clause pairs. The original charging proof consequently bounds rejected field seeds by ordinary failures plus half the pin failures. All copy rows are private to the seed, so this implication remains pointwise and does not introduce the shared-decision-buffer failure of Expedition 043.

The unchanged field verifier rejects at least 109 seeds on every NO field proof. Thus every complete new Boolean assignment has at least 109 failures. The previous degree-15 reciprocal interpolant, with truthful copies and gates, attains 109. The executable evaluates its actual physical clauses for both caps and retains the exact count. This is the old all-assignment field argument transported through the new gate equivalences, plus an executed attaining assignment.

## Verification and scope

The checker covers all 1,152 combinations of local gate type, signed or aliased inputs, consistent reference input values, and all three-variable error subsets. A small signed circuit with a shared input is checked over every private assignment and gives optimum one failure for its false input and zero for its true input.

Both transformed YES and NO circuits were compared against the original output on all 128 seeds for all 142 inherited field-table fixtures. Selected actual field, gate, public and mixed bit errors were evaluated on the full packed physical CNF. Independent scalar DIMACS-address evaluation checks three singleton mutations each on the original and cap 126 layouts. The copied query keys and their physical aliases are checked directly. A normal run and Python -O produce identical expected JSON.

Two mutants retain the honest function but defeat the proposed sensitivity bound. Bypassing the mandatory copy root for A's zero-offset least-significant-bit map permits a single A-bit flip to create 250 failures. Bypassing a private split of original wire 5264 permits one gate-bit flip to create 199 failures. These controls identify the roles of the protected physical boundary and the private fanout cap. The separate AND 000→001 control kills an output-charge-one shortcut.

This finite result changes the sufficient threshold for approximating the new global Boolean proof function. An approximation of the old address encoding does not automatically approximate the new copy rows with the same error or polynomial degree. The new exact sigma ranges over unrestricted error sets, and its singleton witness can be a high-degree error pattern. Novelty, proof-kernel verification, a general-instance census, and an approximation construction for the new function remain open.
