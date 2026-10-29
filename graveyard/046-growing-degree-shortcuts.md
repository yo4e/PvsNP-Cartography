# 046: false shortcuts in the growing-degree estimate

Author/skeptic: 月野テンプレクス, approved2026-10-29 session. These are explicit
mathematical counterexamples to auxiliary shortcuts, not counterexamples to
MOD3 lower bounds or claims of new discoveries. Exact controls: Expedition028.

## Omit the even central atom

False claim: the binomial prefix through floor(m/2) is at most half the mass.
At m2,d0 the actual prefix is3/4, not<=1/2. The even row needs half its central
atom in addition to1/2; an odd row has exactly half. Salvage: the parity-aware
bound1/2+(4d+1/2)*peak(m), retaining the actual capped cutoff. A matching formal
negative-control statement is included but needs actual Lean acceptance.

## Strengthen the invariant without checking the base

Replacing(3s+1)*C_s^2<=1 with(4s+1)*C_s^2<=1 is false at s1:
C_1=1/2 and the latter left side is5/4. A bigger coefficient would improve the
threshold, but this shortcut already fails in the first nontrivial case.
The valid induction uses the exact difference
(3s+1)(2s+2)^2-(3s+4)(2s+1)^2=s.

## Delete the square on the required size

The assertion m>=16d+2 -> B(m,8d)/2^m<=3/4 is false. At m18,d1, the cutoff13
prefix has mass16131/16384. This refutes that prefix estimate, not every possible
linear-size MOD3 obstruction. Salvage: retain m>=(16d+2)^2 for this derivation.

## Omit the size hypothesis altogether

At m0,d0 the capped prefix is1. The3/4 bound fails, while peak_square is still
valid because0*peak(0)^2=0. A valid auxiliary lemma does not license deleting
the distinct size hypothesis of its application.

The prior n299->n300 numerical monotonicity failure remains in graveyard044.
No finite table proves the universal new estimate. The proof must use induction,
exact parity/symmetry, actual coefficient maximum and the original predicate.
