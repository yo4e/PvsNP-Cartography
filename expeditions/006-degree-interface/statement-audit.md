# Statement-fidelity audit: the n=5 degree interface

Research lead self-audit; independent human review has NOT occurred.
Approval night: 2026-10-11. Execution crosses midnight into 2026-10-12 JST.

## Exact intended statement

Let f(x) in GF(2) equal 1 exactly when the number of ones in x is divisible
by 3, for x in {0,1}^5. There exists a finite-support distribution on
polynomials over GF(2) of total degree at most d, with the SAME distribution
correct with probability at least 2/3 for EVERY x, if and only if d>=2.

## Definition correspondence

HasProbabilisticDegreeAtMost f epsilon d existentially quantifies m,
a family P indexed by Fin m, and real weights mu BEFORE the forall-input.
It requires mu>=0, sum(mu)=1, totalDegree(P_i)<=d for every row, and
sum_i mu_i * [eval(P_i,x)=f(x)] >= 1-epsilon for every Boolean input.

This is the finite-support definition in Srinivasan, Tripathi, Venkitesh,
FSTTCS 2019, Definition 1 (printed page 28:2):
https://doi.org/10.4230/LIPIcs.FSTTCS.2019.28 .

A finite distribution can be indexed by Fin m. Repeated rows only aggregate
probability and do not enlarge the class. A zero-weight row can be omitted;
requiring the degree bound on every indexed row therefore does not lose any
existentially feasible distribution. No restriction to rational weights is
made. The concrete epsilon is exactly 1/3 in the real numbers.

The numerical degree uses Nat.find only with an explicit existence proof.
The closed n=5 theorem provides that proof using the actual quadratic upper
witness. It does not assume the degree is 2 or use an empty-infimum default.
The stronger interface theorem classifies feasibility for EVERY natural d.

## Coverage audit

The old lower checker exhausts canonical affine coefficient rows. To extend
that to arbitrary degree-one Mathlib polynomial objects, the new structural
normal-form lemma shows actual polynomial equality with the constant term
plus all linear terms. An exponent vector of total mass <=1 is zero or a
single variable. Every other monomial has coefficient zero by the degree
hypothesis. This is not a test of only the zero and basis input vectors.

ZMod 2 coefficients are retracted through their finite representatives using
the actual nat-cast round trip. The lower theorem then applies to arbitrary
finite real mixtures of arbitrary degree<=1 polynomials, not just a hand-picked
sample or a list of favorable truth tables.

The upper bound reuses the previously accepted 30 actual polynomials. Their
total degrees, normalized weights, evaluated correctness and per-input success
were proved in Expedition 005. No orbit-transfer lemma is newly assumed.

## Deliberate adversarial mutations

1. Move the family choice after the input. Then P_x=C(f(x)) works with degree
   zero for every target. The combined n=5 theorem contrasts this with genuine
   degree-zero infeasibility. A separate exact two-input constant-class dual
   gives maximum 1/2, independently of the stronger affine certificate.
2. Drop totalDegree<=1 from normal-form reconstruction. The polynomial x0*x1
   has no constant or linear coefficients yet is nonzero at input mask 3. It
   even agrees with zero on all basis inputs. The executable control catches it.

These were intentionally false test variants, not previous research beliefs.

## Trust boundary

The finite semantic auditor uses a distinct Mobius/subset inversion algorithm
on all 64 affine functions (2048 evaluations). It cannot validate generic Lean
proof terms. Formal acceptance was separately observed in run 38150083188,
including actual compiled axiom reports. The author of code and self-audit is
the same research lead; a separate runner is not independent human peer review.

No numerical n=5 discovery, minimal-support result, general-n MOD3 upper bound,
novelty, proof-barrier escape, or P-vs-NP result follows.
