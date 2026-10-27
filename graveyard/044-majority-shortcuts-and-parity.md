# 044: independence, signed mass, majority degree and a false all-n shortcut

Author: 月野テンプレクス, approved session executed2026-10-28 JST.
These are explicit mathematical negative controls, not compilation errors.
The exact verifier and output are in Expedition027. Finite controls do not
prove the general amplification or the all-arity obstruction.

## 1. Repeating one draw is not amplification

Use actual constant GF2 polynomials0 and1, target0, with weights2/3 and1/3.
Fifteen independent draws followed by majority have error422009/4782969.
Drawing once and repeating it15 times has error1/3. Both procedures have
correct marginals, but only the product measure supplies the claimed reduction.
Salvage: index by ALL functions Fin15->I and weight each by the product of the
original fifteen masses. The index family must be fixed before the input.
This is different from the valid same-index coupling for two residue restrictions.

## 2. Signed normalized mass destroys the bound

For the same constant-polynomial target, weights[2,-1] sum to1 and give apparent
source success2, hence formally satisfy the lower success inequality if positivity
is omitted. Their independent-product majority failure polynomial evaluates to
580865, not a number bounded by422009/4782969. The exact signed product identity
still holds; monotonic probability bounds need nonnegativity and p in[0,1].
Salvage: retain the original predicate's nonnegative REAL probability contract.

## 3. Fifteen-input majority is not degree<=7 over GF2

The independent Boolean Mobius transform of its complete32768-entry truth table
has6435 nonzero coefficients, exactly the degree8 subsets. In the unique
multilinear representation this is e8. Any degree<=7 polynomial would reduce on
the Boolean cube without increasing degree and have no degree8 coefficient.
This is an exact finite certificate and elementary reconstruction, not a new
Lean minimum-degree theorem. Salvage: the actual e8 composition has degree<=8*d.

## 4. The direct numerical gap is NOT monotone from n299 to n300

Write delta=422009/4782969 and G(n)=(1-2delta)*2^(n-2)-B(n-2,16).
The tempting claim is that G(299)>0 licenses G(n)>0 at every larger n.
It is false: changing parity changes the binomial cutoff.

G(299) =
173942218836028022567908624832604370947637296701413596332611277990970693974594993470985749600 / 4782969 > 0.

G(300) =
-34333774839145158628023571925093120480929917000923809155825198758114351048680211144059406722672 / 4782969 < 0.

For n300 the prefix is B(298,16)=
426571863385236290393334908741107301697730120595728745942257667473767182020143540901793264.
Its cutoff is157, versus156 in B(297,16). No rounded decimal is needed.

This refutes numerical monotonicity, NOT the n300 quadratic obstruction.
Correct salvage: any hypothetical n>=299 approximation restricts, by fixing
extra coordinates to zero, to a299-variable approximation with the same degree,
error guarantee and original real weights. Prove that actual polynomial
restriction and MOD3 target preservation separately. A failure of this numerical
criterion does not prove feasibility or establish the optimal threshold.
