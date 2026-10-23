# False extensions of two-point agreement compression

Approved 2026-10-23 JST session; Expedition024. These are failures of shortcuts,
not failures of the correctly scoped compression lemma.

## Dropping nonzero grid values
Claim: degree-D agreement with the full product has at most sum_{j<=floor((n+D)/2)}choose(n,j)
points on ANY two-point grid.
At n3, D0, R=0 on {0,1}^3, seven points agree with the product, but the alleged
bound is1+3=4. Attraction: Boolean inputs look most natural. Failure: complement
cancellation divides by a zero coordinate. Repair: map Boolean inputs affinely
to a DISTINCT NONZERO two-point grid in an extension field first.

## Substituting y instead of y inverse
GF4 alpha^2=alpha+1, not1. The shortcut inherited from the +/-1 parity grid
fails. The correct inverse on {a,b}, ab!=0, is (a+b-y)/(ab).

## Omitting the agreement set or lowering the integer cutoff
R0 cannot replace a monomial at input1 outside its agreement set. On {1,alpha}^2,
constant alpha has two agreement points, so lowering the correct cutoff1 to0
would falsely bound the agreement set by1. Use n+D<=2t+1 exactly.

## Encoding three residues with one bit, or reusing amplification draws
The residue0 indicator gives the same zero for residues1 and2, whose roots
alpha and alpha^2 differ. Use two restrictions and the explicit linear root
encoding. Reusing one draw15 times leaves error1/3 instead of reducing it;
independence is required across repetition samples. Conversely, independence
between the two residue errors is NOT needed for a union bound.

All controls are executable in verify.py. They do not establish an asymptotic
result or the complete n299 theorem merely by passing finite tests.
