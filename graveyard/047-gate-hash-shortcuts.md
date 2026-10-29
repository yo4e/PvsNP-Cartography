# 047: false shortcuts in the next randomized gate bridge

Author/skeptic: 月野テンプレクス, approved2026-10-29 session.
These are local exact counterexamples for the NEXT frontier, not a claim that
a general gate/circuit theorem has already passed Lean. Reproducer:
expeditions/028-growing-degree/check_gate.py and gate-checks.json.

## Reuse a hash instead of independent rows

For input z=(1,1), a uniform binary two-coordinate mask has zero dot product
with probability1/2. Repeating that same row three times leaves the failure
probability1/2. It does not give the independent-row value1/8. All three
one-row marginals are correct; the joint law is not. Preserve actual product
sampling across rows in the future theorem.

## Add an affine constant without preserving the zero input

A one-row hash with constant1 returns1 at the zero input. The supposed OR
approximation then accepts an input that OR rejects. The one-sided error
argument relies on homogeneous linear hashes, not arbitrary affine forms.

## Confuse a Boolean function with its actual polynomial degree

With one variable and three all-one rows,
Q=1-(1-x)^3=x+x^2+x^3 in GF2. On Boolean inputs it agrees with x, but its
actual ordinary polynomial degree is3, not1. A future degree proof must bound
the composed genuine polynomial; it may not silently replace totalDegree by
the degree of an equivalent Boolean function or assume multilinearization.

The correct gate construction still has actual degree<=r and exact nonzero-input
error2^-r. The local exhaustive tests cover k0..4,r0..3 only, not arbitrary
k,r, circuits, sharing, depth or input-independent probability quantifiers.
All these generic obligations remain part of the next frontier. Normal/-O
local output agrees; no CI coverage or independent reviewer is claimed here.
