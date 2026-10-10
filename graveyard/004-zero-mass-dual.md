# Graveyard 004: replacing a probability measure by zero mass

Date: 2026-10-10. Status: refuted semantic mutation / negative control.
This false variant was deliberately generated to test an assumption;
it was not previously believed or published as a true mathematical claim.

## Invalid claim

Remove sum_x q(x)=1 from finite_dual_obstruction while keeping q(x)>=0,
normalized nonnegative mu, and the bound on every deterministic row.
Claim that the same pointwise obstruction follows.

## Attraction and failure

Nonnegative weights suffice for several intermediate inequalities, making
normalization look cosmetic. It is essential when turning the pointwise
lower bound t into an average lower bound t rather than (sum_x q(x))*t.

## Complete counterexample

Take singleton types I=X={0}, payoff(0,0)=1, mu(0)=1, q(0)=0,
b=0 and t=2/3. Then mu is a probability distribution, q is nonnegative,
every deterministic q-average is 0<=b, and b<t. Yet the mixture has
pointwise payoff 1>=t. The proposed obstruction is false.
The only removed premise, sum(q)=1, fails.

The data auditor checks the exact inequalities. Mod3FiveBridge.lean also
contains zero_mass_is_not_probability as an explicit arithmetic countermodel;
its final build and axiom audit passed in run 38055370947.

## Salvage

Keep the original normalization premise. In the n=5 application it is
proved: mass_sum gives total integer mass 180, and inputProb_sum proves
that dividing by 180 gives probability one. The research direction survives;
only the weakened variant dies. See ../expeditions/005-formal-mod3-five/.
