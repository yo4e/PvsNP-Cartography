# Failed extension: the equal-half affine dual is strictly below2/3 for n>=5

Claim: the same dual placing half its probability on weight1 and half on
weight3 excludes all affine rows with a strict2/3 gap already for every n>=5.
Attraction: complete degree2 results exist for n5 onward, so the newer simpler
dual might be mistaken for a single certificate valid at all those arities.

Counterexamples, computed exactly by direct input sums and the cubic formula:
n5,k1,constant0 scores7/10>2/3; n6,k1,constant0 scores exactly2/3.
Thus the strict dual hypothesis fails. Equality is not a strict obstruction.

Failure point: substituting a different input distribution into a previously
verified lower bound and assuming its margin survives. This is a failure of
the particular dual, not evidence that an affine probabilistic family exists.
It does not refute the earlier n5/n6 degree equalities or their certificates.

Salvage: the derived algebraic score has a strict bound for n>=7. The generic
counting bridge must still be formalized; bounded n3..256 tests do not prove it.
The new Lean source includes six_is_tight, whose acceptance depends on the
actual completed build and axiom reports, not this source-level statement.
