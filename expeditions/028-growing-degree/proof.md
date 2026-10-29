# A uniform growing-degree obstruction

Author reconstruction by 月野テンプレクス,2026-10-29. Execution acceptance is
recorded separately in ci-evidence.md; the text is not a replacement for it.
Known-method context: Goldreich ECCC TR23-034 revision1, Sections3.1-3.2 and
Footnote9. This explicit constant is our reconstruction, not a quoted theorem.

## Original mathematical statement

For all natural n,d, if n>=(16d+2)^2+2, no finite family of genuine GF2
polynomials of total degree<=d, with arbitrary nonnegative real weights summing
to1 chosen before the input, achieves success>=2/3 at every Boolean input for
the residue-zero MOD3 target. This is the existing HasProbabilisticDegreeAtMost
predicate, with no imported lower-bound or amplified-success hypothesis.

## Central coefficient, proved by induction

Set C_s=choose(2s,s)/4^s. The exact recurrence is
C_(s+1)*(2s+2)=C_s*(2s+1). The invariant (3s+1)*C_s^2<=1 starts at s0 with
equality. Its inductive coefficient comparison follows from
(3s+1)*(2s+2)^2-(3s+4)*(2s+1)^2=s>=0.
Multiplication uses nonnegative squares; cancellation uses a strictly positive
(2s+2)^2. No Stirling formula, limit, numerical fit or central-limit theorem.

Let c_m=choose(m,floor(m/2))/2^m. For even m=2s, c_m=C_s. For odd m=2s+1,
c_m=C_(s+1), by Pascal symmetry and the normalizing factor. Consequently
m*c_m^2<=1 for both parities, including m0. The center is a maximum coefficient
by the pinned Mathlib choose_le_middle theorem, whose proof is imported normally.

## The actual capped prefix

B(m,D) is exactly AgreementConsequences.bound, namely the sum through
min(m,floor((m+D)/2)). No surrogate prefix is substituted in the theorem.
The odd center prefix is2^(m-1); the even prefix is
(2^m+choose(m,m/2))/2. The latter follows from the odd identity and Pascal's
recurrence, including m0. For D=8d the cutoff adds at most4d terms beyond that
center. Each term is bounded by the central coefficient; a saturated cutoff
only shortens the sum. Thus for every m,d,

 B(m,8d) <= [1/2+(4d+1/2)*c_m]*2^m.

Write L=16d+2. If L^2<=m then (L*c_m)^2<=1, whence L*c_m<=1. Since
4d+1/2=L/4, the bracket is<=3/4. All denominators2^m are positive; the proof
does not divide by m or assume m is even. d0 is retained rather than discarded.

## Reconnect the original predicate

An original error1/3, degree<=d approximation, if it existed at m+2, gives
by the accepted actual majority15 construction an error<=deltaStar,
degree<=8d approximation on the same inputs. deltaStar=422009/4782969.
The accepted actual GF4 transport and agreement theorem then require

 (1-2*deltaStar)*2^m <= B(m,8d).

But (1-2*deltaStar)-3/4=1406897/19131876>0, contradicting the new prefix
estimate. To obtain every n above the threshold, restrict its extra variables
to zero and use the already-proved same-distribution degree-preserving MOD3
restriction. There is no reliance on monotonicity of a parity-sensitive numeric
gap. The endpoint is also expressed contrapositively as feasible degree d
implies n<(16d+2)^2+2, and as exclusion of each fixed degree beyond an explicit N.

## Attacks and scope

Graveyard046 gives exact counterexamples to deleting the even central atom,
using4s+1 instead of3s+1, replacing the square size condition by a linear one,
and deleting the size hypothesis. These refute those auxiliary estimates, not
all stronger possible MOD3 bounds. The finite checker compares distinct
algorithms, but the universal theorem does not read or trust its output.
This is not an optimal threshold: at d2 the prior299 theorem is stronger.
Unrestricted n12 degree, novelty and unrestricted circuit complexity stay open.
