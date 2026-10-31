# Actual shared-DAG bridge: derivation and statement audit

Author/explorer/formalist: 月野テンプレクス. Same-author skeptic pass; not independent review.
Formal candidates are SharedDAG.lean and CircuitMod3.lean. Only ci-evidence.md and
conclusion.md may promote a specific completed run; this derivation does not
claim kernel acceptance in advance.

## Exact model

Program n K m is an inductively constructed sequence of m nodes. A step stores
ONE prefix program and ONE gate, rather than copying a subprogram for every edge.
Each wire is either an external Fin n input or a Fin m reference into the previous
table. Tables are newest-first: adding a gate creates index0 and shifts old entries
by Fin.succ. The separate Python Boolean interpreter uses chronological tables
and converts these references, to attack ordering mistakes.

Constants and NOT have their usual semantics. A K-slot vector of optional wire
references specifies XOR/OR/AND. Every position has its own matrix coefficient,
even when two positions reference one wire. None means neutral padding:0 for
XOR/OR and1 for AND. All K are allowed, including0. Every finite fan-in can be
encoded with a sufficiently large K; the theorem concerns this concrete model,
not a proved translator from every external graph format. An output may be an
external input, an earlier node or the newest node. Unused nodes are allowed.

S is an upper bound on cost p, which counts original OR/AND nodes once each,
including empty gates. h is an upper bound on the recursively defined OUTPUT
depth: inputs/constants0, NOT inherits, XOR takes max, OR/AND take max+1,
with an empty maximum0. This retains Issue22's documented conservative convention.
A bound using the maximum depth of all nodes is safe but weaker; no silent
substitution of formula size or total node count for nonlinear depth occurs.

## Construct the distribution before the input

Fix r>=1 and sample ONE uniform r-by-K GF2 matrix A. Its rows have the accepted
product real weights. This nonnegative normalized finite distribution does not
depend on x; polynomial repetitions remain legitimate indexed outcomes. Reuse A
at every nonlinear gate. No independence between different gates is asserted.

Build actual MvPolynomial table entries: constants C b, external X j, NOT1+P,
XOR finite sum, OR orPoly and AND andPoly. Genuine exponents are retained.
The accepted gate evaluation lemma and topological induction identify polynomial
evaluation with the randomized table evaluator. The separate deterministic
values table evaluates the ORIGINAL gates, not their approximations.

## Degree argument

For every matrix, every wire of depth d has actual totalDegree<=r^d. External
variables have degree1=r^0, constants have degree0, and neutral padding has
degree0. For r>=1, r^d is monotone in d. NOT and XOR do not raise the maximum
child degree; OR/AND multiply that bound by r using the accepted substitution
lemma. Hence r*r^d=r^(d+1). Repeated wires do not invalidate the generic degree
inequality. The historical r0 counterexample explains the hypothesis.

## Error argument without conditioning on corrupted children

Fix x only AFTER fixing the distribution. At node g define E_g(A) by comparing
g's random gate on its deterministic TRUE predecessor vector against g's true
output. Accepted gate exact laws give Pr(E_g)<=2^-r for OR/AND and0 otherwise.
Those true vectors do not depend on A, even though randomized predecessor values do.

If no E_g occurs, induction in topological order gives equality of the two full
value tables: when predecessors agree, the actual randomized gate sees the true
vector, and absence of its local event supplies the current equality. Therefore
any incorrect chosen output implies some E_g. Weight the Boolean indicator
inequality by nonnegative real matrix weights and sum. The recursive union adds
one cost per original nonlinear node, giving output error<=cost(p)*2^-r<=S*2^-r.
Independence across gates is nowhere needed; row independence is constructed in
the accepted gate module. An exact output node can still inherit earlier errors.

## Original predicate and MOD3 consequence

The finite-type adapter constructs the same input-independent family in the
original HasProbabilisticDegreeAtMost predicate. It is not an average over inputs,
a truth-table proxy, a rational-grid assumption, or an assumed approximability
lemma. Under3S<=2^r the pointwise error is<=1/3, and degree is<=r^h. If the encoded
circuit computes the repository's residue-zero MOD3 target at EVERY input, the
already accepted Mod3GrowingDegree.feasible_size_bound yields

 n < (16*r^h+2)^2+2.

The final premises are a concrete program/output, r>=1, the actual cost/depth
upper bounds, the natural error budget and circuit correctness. None is the
desired polynomial approximation, local failure law or degree induction.
This is a restricted-model consequence; unrestricted depth can make it weak.

## Primary-source comparison and limitations

Goldreich, ECCC TR23-034 revision1, Section2.2.1/Lemma2/Claim2.1:
https://eccc.weizmann.ac.il/report/2023/034/revision/1/download .
Retrieved parsed text in this session; screenshot requests for pages5/6 failed
with cache miss. No visual inspection is claimed. The detailed proof multiplies
local degrees along depth and union-bounds gate replacements. We specialize to
GF2, for which XOR has degree1, and retain a randomized pointwise construction
instead of the source's final averaging step. The paper defines MODq as nonzero
residue, while the repository target is zero residue; the endpoint explicitly
uses the latter. No identification of these two functions without NOT is valid.

The known approximation method is reconstructed, not a novelty claim. No new
independent semantic reviewer or second kernel is used. Finite controls and
same-author proof inspection are separate evidence classes. No P/poly lower
bound, proof-barrier escape, general n12 classification or P-versus-NP conclusion
follows merely from completing this bridge.
