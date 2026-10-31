# Next mathematical frontier: a separately budgeted nonlinear output gate

Selected during the freshly approved2026-10-31 JST session. This is a target,
not authorization for another session, and not an accepted Lean theorem.

## Decision enabled by the present bridge

The actual shared-DAG construction removes the missing approximation premise
from the MOD3 circuit consequence. Uniform rows spend the same error budget
at every nonlinear node. The next worthwhile question is whether a SINGLE
final AND/OR can be given a larger local error allowance, saving a factor of
log(size) in degree. Do not extend that conclusion to an arbitrary XOR output
or silently exchange nonlinear depth with total circuit depth.

## Precisely bounded target

Keep the concrete Program/Slots semantics. Let p be the inner shared DAG,
S>=cost(p), and H>=height(depths p,ws) for the selected children. Append one
AND or OR at the chosen output. Use r>=1 rows for the inner construction and
t>=1 separately sampled rows for the final gate. Construct actual finite
product weights before all inputs and prove

 degree <= t*r^H,
 pointwise error <= S*2^-r + 2^-t.

No child-approximator independence premise is allowed. For fixed x use the
old inner true-input bad union and the top gate's event on its TRUE child
vector. Product marginalization supplies the two bounds; their union supplies
correctness, even when child references repeat or share ancestors. The degree
proof uses actual substituted MvPolynomial objects and the selected-child
height, not all-node depth or formula size.

The explicit choice t=2 and12*S<=2^r gives error<=1/12+1/4=1/3 and degree<=2*r^H.
S0 and empty slots must be handled without taking log0. Combine with the
accepted growing-degree obstruction to obtain the corresponding restricted
MOD3 consequence. Optional exact output NOT should preserve the same bounds.
Do not expand this into a general nonuniform-resource framework first.

## Source comparison and a killed extrapolation

Limaye, A. Srinivasan and S. Srinivasan, MFCS2025, article67,
https://doi.org/10.4230/LIPIcs.MFCS.2025.67 . The official PDF pages67:6/67:8
were retrieved and VISUALLY inspected in this session (screenshots succeeded).
The HTML extraction omits many formulas, so it was not the sole source.
Page67:6 defines size by wires and depth by ALL layers. Lemma10 recalls a
known O((log s)^(d-1)*log(1/epsilon)) upper bound over F_p; the proof of Lemma11
explicitly gives the final OR constant error and degree while budgeting its
children more tightly. This supports the method choice but does not certify
our particular concrete DAG statement, constants, depth convention, or sampler.
The randomness-efficient construction in that paper is not claimed here.

Graveyard052 explains why replacing our general r^h by an absolute-constant
multiple of r^(h-1) for arbitrary XOR outputs is false. XOR of disjoint minterms
represents EVERY Boolean function with nonlinear depth1, though potentially
exponential size. A size-independent degree conclusion would contradict the
already accepted eventual MOD3 degree obstruction. The all-input minterm
argument is written, not Lean-formalized in this session. It is not a new
P-versus-NP result.

## Acceptance and exit

A natural milestone is the actual inner-DAG/top-gate composition with original
probability quantifiers, same-author statement attack, exact finite controls,
and completed pinned strict build/axiom evidence. Separately compare the
mathematical improvement against known methods; use novelty-unknown until a
proper priority audit. Independent semantic review and a second kernel remain
separate evidence classes. If the root condition is the only improvement,
say so and decide whether to park this reconstruction route rather than keep
polishing constants indefinitely.
