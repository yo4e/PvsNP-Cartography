# Statement-fidelity audit: two different n=8 evidence objects

Date: 2026-10-16 JST. Skeptic: 月野テンプレクス, same-author audit.

## A. The formally verified result

Let f:{0,1}^8 -> GF(2) be one exactly when Hamming weight is divisible by3.
The standard pointwise, finite-support, real-probability probabilistic degree
at error1/3 is exactly2. The original HasProbabilisticDegreeAtMost definition
is unchanged: a single finite family of actual MvPolynomial objects with
nonnegative REAL weights summing to one is chosen before every-input quantification.

The upper proof uses the four unchanged Expedition004 seeds with masses
[1,3,4,4]/12, then ALL variable permutations. A proved arbitrary-n Hamming-layer
mean identity and exact fiber count connect nine layer inequalities to every
input. Layer cardinality, coverage, normalization and polynomial degree/evaluation
are proved, not supplied as unchecked hypotheses. Boundary cases n=0,w=0,w=n
are retained in the general counting theorem.

The lower proof uses full-cube mass7 at weight1 and mass1 at weight3, total112.
Only18 canonical affine cases are kernel-computed, but a structural normal form
and proved coefficient-permutation/score invariance cover ALL512 affine choices
and hence arbitrary finite real mixtures of all actual degree-at-most-one objects.
The score bound72/112=9/14 is strictly below2/3. This is not sampled coverage.

Mod3Eight.feasible_degree_iff, least_feasible_degree and pdeg_eq_two are closed
applications; no caller assumes the desired feasibility. The raw four-seed
mixture fails at input14 with success1/12, and that counterexample is formalized.

The successful pinned --wfail run and actual305-declaration axiom report are
recorded in formal/reports/2026-10-16-n8-axioms.txt. No project-specific axiom,
sorryAx, native_decide dependency or weakened threshold was accepted. No second
proof kernel or independent human statement reviewer was supplied.

## B. The explicit compact witnesses

recover_939.py reproduces the previous939 distinct rows and denominator2016,
including its canonical coefficient hash. It is a deterministic construction,
not a new uniform-group assertion. Direct per-input checks decide validity.

certificate-159.json has159 distinct actual binary quadratic coefficient rows,
positive integer tickets and denominator100874688. Two different exact evaluators
agree on all256 input probabilities. The minimum is2/3, attained at164 inputs.
All512 affine scores are separately checked by exhaustive tuples and Walsh
arithmetic. The tuple validator rejects5 damaged inputs and the ANF validator6;
normal and optimized execution agree.

The new witness has fewer distinct polynomials but a larger denominator. It
need not have equal success at equal-weight inputs: weights2,5,6 have multiple
success values. Do not reuse layer averages as a substitute for its every-input
checks. Neither minimal support nor minimal denominator nor optimal error has
been proved. This JSON witness itself is NOT encoded in the successful Lean
module. Formal proof A does not magically verify the coefficients of witness B.

## Quantifier and provenance attacks

Probabilities are real ratios, not elements of GF(2). No input-dependent family
is allowed. Floating-point normalization or a nearly2/3 bound is insufficient.
Direct fraction rounding of the selected LP vertex actually fails; exact
linear-system reconstruction repairs it without changing the required bound.
See graveyard009 for a concrete negative gap and normalization error.

The previous22-file patch was not blindly applied over a newer main. The useful
939-row mathematical object and unchanged direct checker were integrated with
explicit provenance. Historical claims and new formal/computational claims are
separate. These checks do not establish novelty or a result at n>=9.
