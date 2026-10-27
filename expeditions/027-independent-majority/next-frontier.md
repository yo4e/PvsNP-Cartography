# Next frontier: an explicit growing-degree obstruction

Author reconstruction by 月野テンプレクス, approved session executed2026-10-28 JST.
This is a written continuation, NOT an accepted Lean theorem, independent
semantic review, novelty claim or optimal bound. The bounded checks in
check_frontier.py are additional local evidence, not the completed majority CI.
Tracked by Issue21; that issue does not authorize another session.

## Proposed endpoint and why it matters

For every natural d and n with

  n >= (16*d+2)^2 + 2,

exclude HasProbabilisticDegreeAtMost(MOD3_n, error1/3, degree d).
This is an explicit square-root-scale lower obstruction, rather than one more
finite n certificate. At d2 it is weaker than the separate299 threshold; the
point is degree growth, not replacing a sharper small-degree result.

The only new mathematical estimate needed after the independent amplification
chain is a uniform binomial-prefix bound. The construction below avoids a CLT,
Stirling asymptotic, numerical fit, or unproved monotonicity in n.

## 1. A central-binomial invariant

Set C_s=choose(2s,s)/4^s. The factorial or multiplicative binomial identities give

  C_0=1,  C_(s+1)=C_s*(2s+1)/(2s+2).

We claim (3s+1)*C_s^2<=1 for every s. The base case is equality. To propagate
an existing bound, use the exact identity

 (3s+1)*(2s+2)^2 - (3s+4)*(2s+1)^2 = s >= 0.

All denominators are positive. Multiplying the old inequality by the square of
the displayed ratio and using this polynomial difference proves the next case.
This is an all-s induction, not an inference from checked rows.

## 2. Both parities, with the central atom retained

For m>=1 put c_m=choose(m,floor(m/2))/2^m. If m=2s, c_m=C_s. If m=2s+1,

 c_m=((2s+1)/(2s+2))*C_s <= C_s.

Since m<=3s+1 in either case, m*c_m^2<=1. Each normalized binomial coefficient
is at most c_m: the adjacent-coefficient ratio (m-j)/(j+1) is >=1 up to the
center and <=1 afterwards. This is the required unimodality argument.

Let B(m,8d) be the actual prefix through min(m,floor((m+8d)/2)). If m=2s,
symmetry puts the prefix through s at1/2+c_m/2, followed by at most4d terms,
each at most c_m. If m=2s+1, the prefix through s is exactly1/2, again followed
by at most4d terms. Capping at m only removes extra terms. Hence uniformly

  B(m,8d)/2^m <= 1/2 + (4d+1/2)*c_m.

The half-central-atom term cannot be dropped in the even case. The failed
n299-to-n300 direct-gap monotonicity is preserved in graveyard044; this proof
does not assume it.

## 3. Exact contradiction, no square-root formal machinery needed

Suppose m >= (16d+2)^2. Write L=16d+2, so L>0 and4d+1/2=L/4.
From m*c_m^2<=1 and nonnegativity, (L*c_m)^2<=1, so L*c_m<=1.
Consequently B(m,8d)/2^m<=3/4.

On the other hand, the original degree-d,error1/3 approximation amplifies to
degree<=8d and error delta*=422009/4782969. The actual MOD3-to-product bridge
then requires B(m,8d)/2^m >= 1-2delta*. But

  (1-2delta*) - 3/4 = 1406897/19131876 > 0.

This contradicts the prefix bound. With m=n-2 the proposed endpoint follows.
No equality to an optimal degree or threshold follows. The candidate remains
unformalized until the invariant, parity split, actual prefix estimate and final
original-predicate application all pass their own checks.

## Attack plan and current limits

Check m=0 separately rather than dividing by it; the target threshold excludes
it. Include d=0, both parities, saturated prefixes and all natural casts. Do not
silently replace arbitrary real probabilities by rational tickets, or infer a
circuit lower bound from a polynomial-degree statement. Retain the fixed
family-before-input quantifier order. Independent semantic review and a second
proof kernel are separate evidence classes, neither supplied by these notes.

Local check_frontier.py confirms151 recurrence/invariant controls,150 central
mass controls and2400 prefixes (m1..150,d0..15), using exact fractions. It also
checks the rational margin. These checks corroborate and attack the written
argument only. They do not establish its universal conclusion.

Primary-method context remains Goldreich ECCC TR23-034 revision1, Sections3.1-3.2,
and the repository's prior source comparison. The growing-degree behavior is
known-method territory. This explicit loose constant is our reconstruction;
priority, novelty and sharpness are not claimed.
