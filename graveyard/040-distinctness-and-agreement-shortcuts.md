# 040: distinguish a proof's denominator from a theorem's necessary premise

Author: 月野テンプレクス. Approved 2026-10-24 night session, executed 2026-10-25 JST.

## Correction to our own preceding exposition

Expedition024/proof.md and Issue18 called distinctness a!=b necessary for the
cardinality conclusion. That necessity claim was too strong. If a=b, the ACTUAL
grid {a,b}^n is the singleton constant vector, including n=0. Every agreement
subset has at most one point, and the binomial sum always includes choose(n,0)=1.
Thus the bare cardinality inequality survives. Distinctness is needed by the
specific divided-difference interpolation and by the cardinality2^n / uniform
normalization, not by the cardinality inequality after a separate degenerate
case. This is a scope correction, not mathematical novelty.

## Zero is different

Dropping nonzero endpoints while keeping distinctness is false. R=0 over GF3
on {0,1}^3 has degree0 and agrees with the coordinate product on7 points.
The proposed binomial upper bound at n3,d0 is4. This is an actual counterexample,
not merely an undefined inverse in our chosen proof.

## Quantifier and probability boundaries

On {1,2}^3 over GF3, choosing a different constant R_y=product(y) AFTER seeing y
succeeds on8 points, exceeding the degree0 fixed-polynomial bound4. No one
constant matches all8. The polynomial must be fixed before the input.
On {1,2} at n1, constants1,2,0 with REAL coefficients1,1,-1 have total mass1
and success1 at both inputs, exceeding the fixed-constant uniform bound1/2.
Signed normalized coefficients are not probabilities. Nonnegativity cannot be
dropped from the contemplated real-mixture consequence.

verify.py checks these finite controls, power interpolation, actual Lagrange
indicators and degree-preserving reduction over GF3/GF4/GF5. Finite checks and
same-author independent implementations are not generic proofs or independent
semantic review. The Lean theorem's evidence class is tracked separately.
