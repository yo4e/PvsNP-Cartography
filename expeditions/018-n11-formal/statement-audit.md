# Statement fidelity: n11, completed 2026-10-20 JST

The source-submission checkpoint was a candidate. It is now accepted at
9733d800128ad6d92b1f1293e453a4c8d5188f34 by completed formal39380310454,
with --wfail, namespace allowlist and18 target reports. See ci-evidence.md and
axiom-report.txt. This self-authored audit does NOT fulfill human-review #8.

## Definition and quantifiers

Target is SmallSupportMod3.target on BooleanCube11, returning1 in GF(2) iff
integer Hamming weight is divisible by3. Actual BinaryPolynomial11 objects are
MvPolynomial(Fin11)(ZMod2), with totalDegree<=2. The unchanged feasibility
predicate quantifies a finite family P and nonnegative normalized REAL masses
before the universal input. No averaging over input replaces that pointwise demand.

## Exact encoding

Independent low-weight queries recover rows(0,0,0), (1,2047,38605195639935),
(1,1920,1151998655551) with55 lexicographic edges. All2048 input values match
explicit monomials, stored block codes and subset-count formulas. The latter
are external computational checks, not unproved premises of the Lean proof.
SmallSupportMod3.polynomial_eval and polynomial_degree handle the actual
polynomial objects. Weights[3,12,6]/21 equal[1,4,2]/7.

## Upper proof chain

layer_tickets_exact discharges all12 closed full-cube layer sums, splitting
weight cases but using kernel computation. upper_layer_bound proves threshold14.
seed_correct and seed_success connect genuine polynomial evaluation and real
probability. seed_layer_bound and feasible_of_layer_bounds supply a single
product distribution over seed choices and ALL coordinate permutations.

The separately reproduced496-row quotient is not claimed to have a new Lean
transport proof. The formal witness uses the existing full-permutation adapter.
Raw canonical seeds fail atmask63, success0, and the accepted source proves that
negative control rather than quietly dropping symmetry from the construction.

## Universal lower chain

Input mass15 on weight1 and1 on weight3 sums330. canonical_affine_bound computes
24 representatives with score<=207. Coefficient permutation, inverse-input
evaluation, dual symmetry and a full-cube bijection prove that these cover
all4096 affine rows. no_degree_one_family uses degree-one structural normal
form and finite real duality, excluding all actual totalDegree<=1 polynomials
and all normalized finite REAL mixtures. Strict207/330=69/110<2/3 is retained.

feasible_degree_iff, least_feasible_degree and pdeg_eq_two depend on proved
upper/lower statements, not assumed feasibility. The completed formal output
and final theorem statements were independently retrieved and compared with
this scope. Independent human semantic review and novelty remain unfulfilled.
No generic MOD3 degree2 upper bound or n12 degree equality is inferred.
