# Statement-fidelity audit: full permutation transport

Approval night: 2026-10-13 JST. Reviewer: 月野テンプレクス, same-author review.
Independent human semantic review is pending.

## Informal statement and proof

Let I be finite, P_i actual polynomials in GF(2)[x_0,...,x_(n-1)], and
mu_i nonnegative REAL weights with sum one, chosen before an input is known.
Let f be invariant under every variable permutation. For e in S_n define
P'_(i,e)=rename(e,P_i) and mu'_(i,e)=mu_i/|S_n|.

Polynomial evaluation obeys eval(P'_(i,e),x)=eval(P_i,x composed with e),
and actual totalDegree is unchanged because e is a bijection. Symmetry of
f identifies the corresponding correctness indicators. Swapping two finite
sums then gives the exact identity

    success(P',mu',x) = (1/|S_n|) sum_e success(P,mu,x composed with e).

Composition by a fixed permutation reindexes the same full finite group,
so this average is permutation invariant. Positivity and normalization of
mu' follow from |S_n|>0, including n=0. A lower bound at every input is
preserved. More generally a bound at every full input orbit is sufficient.

## Formal chain

PermutationTransport.lean proves permute_degree, permute_eval, permute_weight,
correct_permute and feasible_of_fintype. The last adapter reindexes an arbitrary
finite family to the original Fin m family without changing real weights or
quantifier order. It is not a change to HasProbabilisticDegreeAtMost.

FiniteSymmetrization.lean defines the exact product family and proves
sym_degree, sym_nonneg, sym_normalized, sym_success_eq_average,
sym_success_invariant, feasible_of_orbit_bounds, symmetrization_preserves
and feasible_iff_orbit_average. The latter is an equivalence with the original
degree predicate. The forward direction averages a genuine pointwise
certificate; the reverse constructs a single family from orbit bounds.

SymmetryApplications.lean proves MOD3 target symmetry for arbitrary n and
obtains a symmetric degree-two witness for n=6 or n=7 from the previously
proved feasibility result. The caller supplies only n=6 or n=7, not a desired
feasibility or deterministic bound. This is not a new degree equality.

## Important distinctions

- The input transformation is x composed with e, NOT e inverse. A 3-cycle
  distinguishes these. Checking only swaps would miss that error.
- The target is symmetric, but the individual input polynomials need not be.
- Probabilities are in R. Division by |S_n| inside GF(2) is not the construction.
- All degree premises concern actual MvPolynomial.totalDegree, including
  nonmultilinear polynomial objects, not their Boolean truth-table degree.
- Repeated and zero-weight rows are allowed. An empty family cannot satisfy
  normalization; no division by an empty permutation group is used.
- The algebraic success identity holds even for signed weights; its use as
  a probabilistic certificate separately requires nonnegativity and sum one.
- The proved invariant is success under permutations. We do not claim an
  additional, separately encoded equality of probability laws on polynomials.
- The generic theorem has arbitrary n because of a symbolic derivation.
  Its finite tests are not a proof of that quantification.

## Adversarial checks and coverage limits

The exact stdlib checker verifies all 278 squarefree polynomials and all 278
Boolean score tables for n=0,1,2,3; 12,426 squarefree and 42,944 higher-exponent
evaluations; and 30 nonuniform mixtures including zero weights and repeated
rows. Four deliberately invalid probability/group inputs are rejected with
assertions disabled as well. See audit-results.json for the actual output.

Seven mathematical countermodels are detailed in graveyard/007. The Lean
application file checks three components: the missing-symmetry correctness
identity, the AND2 global count plus a bad input, and the GF(2)/R arithmetic
distinction. The full nonsymmetric-target success drop from 1 to 1/2 and the
other countermodels are exact Python checks, not all separately Lean theorems.
In particular the AND2 component does not claim to prove nonexistence of every
randomized family; it disproves the proposed inference about a given witness.

The literal n=7 audit pushes all 18*5040 polynomial/permutation pairs into
2,524 distinct polynomials, keeping multiplicities. All 128 inputs agree with
an independently calculated layer mean: success is 11/15 at weight three and
2/3 at every other weight. This confirms the finite transformed certificate,
not a general orbit-to-Hamming-layer formula in Lean.

## Independent verification boundary

Actual pinned CI compilation and compiled axiom reports are recorded in the
conclusion and formal report, separately from semantic computation. Normal
and optimized Python outputs match. The finite checker is differently
structured code by the same author, not an independent human review or second
proof kernel. No novelty, all-n MOD3 degree-two result, asymptotic lower bound,
or proof-barrier escape is claimed. See prior-art.md and barrier-audit.md.
