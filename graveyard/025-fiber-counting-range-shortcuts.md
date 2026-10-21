# Three invalid counting shortcuts, 2026-10-21 JST

## Unguarded natural subtraction in a hypergeometric count

Claim: for all w,r, the number of w-subsets X with |X intersect A|=r is
choose(|A|,r)*choose(n-|A|,w-r), using natural-number subtraction unconditionally.
At n=1, A={0}, w=0, r=1, there are no such X. The expression nevertheless
returns choose(1,1)*choose(0,0)=1 because 0-1 truncates to0.
Repair: require r<=w, or explicitly return0 for r>w. The attraction is that
ordinary mathematical binomial conventions often implicitly set negative
lower indices to0, whereas the implementation has already erased the sign.

## Discard ordered triple multiplicity

Claim: keep one of the six ordered samples for each triple support, but retain
its original individual sample probability. Each weight-three input then has
mass1/(2*n*(n-1)*(n-2)), not the correct six times that. Total probability is
1/2+1/12=7/12. At n=3 the sole triple input has wrong mass1/12 instead of1/2.
Repair: ADD all fiber masses when pushing forward. Removing duplicate rows is
not the same operation as removing their probability mass.

## Extend normalization to n=2

There is no weight-three input at n=2. The closed singleton contribution sums
to1/2, not1. Thus n>=3 is needed for the probability/half-layer-mean interface.
Fiber counts themselves remain valid at n=0,1,2 and are tested separately.

Expedition021/verify.py checks all three exact counterexamples. These refute
only the stated shortcuts, not the accepted generic degree-one obstruction,
not the correct input measure and not any general complexity-class relation.
No novel-mathematics claim is made.
