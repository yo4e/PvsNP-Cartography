# Covering does not characterize pointwise approximation or recognize MOD3

Research lead 月野テンプレクス, freshly approved 2026-11-02 JST session.
Evidence: written derivations and exact finite controls in Expedition032. These attacks are not Lean-formalized here and do not refute the one-way counting theorem.

## False converse, retained

Graveyard055 already shows n2,d0,AND is close to zero on 3/4 of inputs yet no constant mixture gives pointwise success2/3. Do not relabel Hamming-covered target counts as probabilistic-degree feasibility counts.

## Target blindness at infinitely many arities

Let (a_n,b_n,c_n) count binary strings by Hamming weight modulo3, starting (1,0,0). Splitting by the last bit gives (a+c,b+a,c+b). Since a+b+c=2^n, direct substitution gives a_(n+2)-a_(n+1)+a_n=2^n. Put u_n=3*a_n-2^n. Then u_(n+2)=u_(n+1)-u_n, u_0=2,u_1=1. Six iterations return the pair to its starting value, so the exact periodic list is (2,1,-1,-2,-1,1). This is an induction/recurrence argument, not extrapolation from tests.

Thus the residue-zero MOD3 target has (2^n+u_n)/3 ones. Its distance to constant0 is at most floor(2^n/3) exactly when n mod6 is2,3,4. Constant0 has degree0 and belongs to every allowed degree class. Hence every uniform far-from-degree-d detector at radius floor(2^n/3) misses MOD3 at those infinitely many lengths, even when n is large enough for the accepted pointwise degree-d obstruction. The other residue classes need not always be detected: n7 is also missed by a nonconstant affine row. No claim of a complete detection classification is made.

At n8 the exact constant distance is85 and the radius is85. Strict versus non-strict inequality matters. Complementing target/output gives the corresponding constant1 witness for the opposite MOD3 polarity.

## Other assumptions genuinely needed

Signed weights (-1,2) on row values(3,1), threshold0, have total mass1 and mean-1, yet no positive-weight row has value<=0. Nonnegativity is essential to positive-support averaging. Zero weights without normalization can leave no positive support. Over a nonbinary alphabet, outputs1 and2 have the same error set against0, so the error-set injection used for binary Hamming-ball counting fails.

## Salvage

Keep the correct original-predicate-to-covering implication. A distribution balanced between the target's positive and negative inputs removes the trivial constant advantage but does not automatically yield a universal strong lower bound or efficient higher-degree recognizer. The correct converse in primary literature quantifies over EVERY input distribution, not just the uniform one. See Srinivasan, FSTTCS2013, Definition4/6 and Fact7, DOI10.4230/LIPIcs.FSTTCS.2013.201, printed page204 (visually inspected).
