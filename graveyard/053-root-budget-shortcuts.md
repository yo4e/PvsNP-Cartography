# Root-budget shortcuts and their exact failure points

Author / skeptic: 月野テンプレクス. 2026-10-31 JST night, fresh approval.
No mathematical priority is claimed. Executable controls: Expedition031/verify.py.

## Reusing the inner-only error budget

False claim: for an inner program of nonlinear cost S, 3*S<=2^r still guarantees
error<=1/3 after adding a separately randomized two-row final OR.
Attraction: copy the previous uniform-budget hypothesis without paying the root.
Counterexample: one input x, inner OR(x), final OR(inner). At x=1, with independent
r=t=2 matrices, either stage may miss. Success=(3/4)^2=9/16, error=7/16>1/3,
even though 3*1<=4. This does NOT contradict the previous uniform-DAG theorem:
that theorem counts BOTH nonlinear nodes, so its hypothesis would be 3*2<=4,
which is false. Repair here: reserve 1/4 for the root and <=1/12 for the inner
program, hence 12*S<=2^r. r=4,t=2 yields exact error19/64. The coefficient12 is
sufficient, not proved optimal.

## Dropping the root's degree factor

False claim: this actual composed polynomial always has degree<=r^H regardless
of t. At x as a formal variable, two all-one hash rows give inner OR polynomial
1+(1+x)^2=x^2 over GF2. Two all-one root rows give 1+(1+x^2)^2=x^4.
With H=1,r=t=2, actual degree4 exceeds r^H=2, and equals t*r^H=4.
Boolean reduction would turn x^4 into x, but the formal predicate bounds actual
MvPolynomial.totalDegree of every sampled polynomial. This counterexample only
refutes the claim about this construction, not existence of another lower-degree
approximator for the same Boolean function.

## Zero rows are a diagnostic, not a fabricated refutation

With zero inner rows and a two-row OR root, the cascade above always misses x=1.
The checker records error1. That does NOT refute the general error estimate,
whose inner term S*2^0 is already1. Nor does it show that every r0 instance breaks
the degree estimate. Retain the previously proved r>=1 assumption where exponent
monotonicity over skip wires is used; do not invent a stronger necessity claim.
The final row count t=0 is allowed in the generic endpoint, with a vacuous error
allowance and a constant actual polynomial. The useful one-third endpoint fixes t=2.

## Other tempting extrapolations

Do not extend the single-root result to arbitrary XOR outputs by deleting a
nonlinear-depth factor: graveyard052 supplies the written minterm objection.
Padding remains 1 for AND and 0 for OR. Local error events must use deterministic
true children, not children chosen after seeing a matrix. Shared predecessors
are not independent. The main formal construction uses an explicit product
measure; finite prefix-coupling controls are a separate unformalized observation,
not proof that all couplings or adaptive samplers preserve the bound.
