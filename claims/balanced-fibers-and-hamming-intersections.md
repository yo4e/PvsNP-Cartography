---
id: balanced-fibers-and-hamming-intersections
status: formally-verified
statement: The existing balanced Boolean input measure has the closed half-uniform layer1/layer3 mass and arbitrary-real expectation formula for n>=3; guarded Hamming intersection counts hold at all natural arities.
dependencies: [formal/PvsNPCartography/BalancedAffineFibers.lean, formal/PvsNPCartography/HammingIntersections.lean]
novelty: novelty-unknown
last_attacked: 2026-10-21
---

Accepted source598d54ed0940a331650b7e7eb733d62c9b6e40ab, completed production
run39547776930/job119049747106. --wfail9050 jobs,639 namespace declarations,
12 explicit new targets, only propext/Classical.choice/Quot.sound. Actual
full log, source and matching commit/tree re-fetched. See Expedition021.

The exact point mass is1/(2n) at weight1 and1/(2 choose(n,3)) at weight3.
It is the existing pushforward, not a newly defined surrogate. Counts are
one singleton/six ordered-distinct-triple fibers. Every real score admits
the half-layer-mean formula; no symmetry or positivity restriction on the score.

The intersection count is choose(|A|,r)*choose(n-|A|,w-r) only when r<=w;
otherwise0. Explicit split/union and bits/ones bijections cover actual subsets
and Boolean inputs, including impossible cardinalities. The wrong unguarded
Nat formula is refuted in the accepted source. Three scoped attacks and two
failed implementations are retained in graveyard025..027.

These are standard counting results, not asserted novel mathematics. The
accepted generic obstruction and n5..11 degree equalities remain unchanged.
Independent human semantic review and a second proof kernel are absent.
No optimality, arbitrary-n quadratic upper bound or P-vs-NP claim.
