# 033: dropping support, normalization or quantifier order destroys this certificate

Approved 2026-10-22 JST night; exact controls in Expedition023/verify.py.
This extends, rather than erases, graveyard032's narrow zero/q9/r8 obstruction.

## Dead claim: the weight6/10 dual bounds EVERY quadratic by9/14

Take q_A with |A|=8 at n12. It has genuine GF(2) total degree<=2, layer success
23/33 at weight6 and10/11 at weight10. Its dual score is5/6>9/14.
Thus this PARTICULAR dual cannot certify an unrestricted quadratic lower bound.
This neither proves nor disproves existence of a pointwise2/3 quadratic mixture.
The candidate formal module includes this actual-polynomial counterexample.

## Other attacked shortcuts

- Input-dependent choice succeeds on all4096 inputs, using the same716 candidates.
  This does not contradict the fixed-family/fixed-weights obstruction; swapping
  the quantifiers destroys its content.
- Treating5/14 and9/14 as per-input weights yields total mass2607/7, not1.
- Swapping the two total layer masses gives q9 score111/154>2/3.
- Signed normalized coefficients (q9 weight2, r8 weight-1) have dual score
  353/462>2/3. Linearity allows signed reals; probability duality does not.
- Ordered clique edges cancel in characteristic2. They are not the elementary
  squarefree degree-two polynomial and produce a different actual truth table.

## Salvage: exact optimal value WITHIN the declared family

The bound9/14 is sharp. Give zero weight60/280=3/14 and each of ALL220 q9
polynomials weight1/280; give all r8 weight0. All probabilities sum to1. Exact
full-input evaluation yields numerators over280 by input weight0..12:
[220,280,180,192,220,200,180,200,220,192,180,280,220].
The minimum180/280 equals9/14. This primal and the dual establish the restricted
finite game's value, not minimum support or minimum denominator. No optimizer
was trusted. The primal certificate is separately computational, not a claimed
compiled Lean sharpness theorem. Unknown novelty; no all-quadratic or n12-degree
conclusion. A new family, not another probability search inside this one, is needed.
