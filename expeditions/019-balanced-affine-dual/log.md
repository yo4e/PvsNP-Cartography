# Running structural research log, approved2026-10-20

OBSERVE: n7..11 lower data use equal-half mass on layers1/3.
ORIENT: derive a coefficient-weight formula, separate counting from algebra.
ACT: derive S_n(k)=1/2+t(n^2-t^2)/(4n(n-1)(n-2)),t=n-2k.
VERIFY: symbolic numerator/SOS residuals are zero. Exact standard-library
checks cover33147 formula pairs n3..256 and all affine rows via Walsh on
full input cubes n3..12; normal/-O outputs match.
ATTACK: extending strictness to n6 fails at k1 with equality2/3; n5 gives7/10.
REPAIR: restrict the algebraic theorem to real n>=7 and0<=k<=n. Do not infer
an all-n counting theorem from the finite checks or a degree2 upper bound.
FORMALIZE: write the pure real algebra and six-is-tight counterexample in
BalancedAffineDualAlgebra.lean with six explicit axiom-report targets.
RECORD: preserve the false low-arity shortcut in graveyard018 and the precise
formal counting frontier. Actual Lean completion remains to be inspected.
