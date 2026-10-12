# Statement-fidelity and barrier audit: finite MOD3, n=6 and n=7

Date: 2026-10-13 JST. Reviewer: 月野テンプレクス (same-author self-audit).
Independent human semantic review is still outstanding.

## What is actually asserted

For n equal to 6 or 7, over GF(2), with pointwise error at most 1/3,
the finite-support probabilistic degree of MOD3 is exactly 2.
MOD3 returns field element 1 exactly when the Boolean Hamming weight is
0 modulo 3, and returns 0 otherwise. The zero input is included.

`SmallSupportMod3.feasible_degree_iff` gives feasibility iff 2 <= d;
`least_feasible_degree` gives the IsLeast statement; `pdeg_eq_two` gives the
numerical equality using a proved existence witness, not a caller's assumption.
The explicit premise n=6 or n=7 is part of the statement, not an observation
silently generalized to arbitrary n.

## Coverage and quantifiers

`HasProbabilisticDegreeAtMost` fixes a finite indexed polynomial family and
nonnegative REAL probabilities summing to one before quantifying over every
Boolean input. Repeated polynomials and irrational mixture weights are allowed.
The lower proof covers arbitrary `MvPolynomial` objects of actual totalDegree
at most one, not merely a convenient selected list. The existing structural
normal-form theorem proves equality with the corresponding affine polynomial.
All 128 affine choices for n=6 and all 256 for n=7 are then exhausted.

The upper proof constructs actual quadratic GF(2) MvPolynomials and proves
both their totalDegree bound and evaluation semantics. Eighteen distinct
coefficient rows have weights [2,4,2,2,1,...,1]/24, fixed independently of x.
Each complete Boolean cube is checked directly. No unchecked orbit-coverage,
layer-average-to-pointwise, restriction, or symmetrization premise is used.
The n=6 data were obtained by setting x6=0 in n=7, but their Lean application
has its own complete arithmetic proof; the derivation is checked separately
at all 18*64 polynomial/input pairs by Python.

## Lower and upper arithmetic

n=6 input masses by weight are [0,55,0,21,16,15,0]. Their full-cube sum is
1080 and every affine row has weighted correctness <=660, giving 11/18<2/3.
n=7 masses are [0,20,5,13,1,15,0,0]; sum1050, affine bound595,
giving 17/30<2/3. These are the previous dual certificates in integer units.
The generic real-mixture bridge has mass/bound hypotheses, but the concrete
applications discharge them by `decide +kernel` rather than assume them.

Both upper witnesses have at least sixteen correct tickets out of24 at each
input. Exact success is 16/24 or20/24. Histograms are {16:56,20:8} for n=6
and {16:114,20:14} for n=7. In particular the new witness has no uniform
strict slack above2/3. The older n=7 eight-orbit witness has strict slack
10825/15922>2/3 and is not superseded for stricter error thresholds.

## Attacks and verification separation

The stdlib audit reads the actual Lean arrays and compares saved JSON data.
Two polynomial evaluators agree; a Mobius transform reconstructs the ANF;
integer Walsh-Hadamard and exhaustive enumeration agree on every affine score.
Normal and optimized Python give identical output and reject flipped constant,
unnormalized or negative probabilities, reversed pair order, corrupt dual mass,
and a false strict-slack claim. See audit-results.json for all input numerators.

All360 single-cyclic-orbit compression candidates fail; their best minimum is
7/12. See graveyard/006. The 24-ticket repair uses two orbits, but neither
support minimality nor global twelve-ticket infeasibility has been established.
Exploratory SciPy optimization finds candidates only; no optimizer is trusted
by either the stdlib checker or the Lean proof.

The first Lean candidate failed an ordinary constant-degree proof obligation.
That failure is distinct from mathematical refutation of the data, and neither
--wfail nor the axiom allowlist was weakened to repair it. The conclusion and
actual axiom report record only the eventually observed verification status.
A second algorithm or a separate CI runner does not constitute independent
human mathematical review.

## Prior art and proof barriers

The numerical n=6/n=7 degree values were already established by the finite
certificates in Expedition002. This expedition contributes a compact witness
and a degree-faithful formal connection, not a newly discovered numerical value.
The standard pointwise definition is consistent with the primary literature
linked in docs/BIBLIOGRAPHY.md, including the symmetric probabilistic-degree
literature and arXiv:2107.03171. No novelty search sufficient for a novelty
claim has been completed for this small-support presentation.

Nothing here supplies a uniform construction, asymptotic degree lower bound,
or circuit-size lower bound. It makes no relativization, Natural Proofs, or
algebrization escape claim. Those barriers are not bypassed by checking a finite
truth table in Lean. See map/BARRIERS.md for the actual barrier statements.
The next scaling questions remain n=8 formalization and reusable symmetry or
restriction infrastructure, with explicit field and degree semantics.
