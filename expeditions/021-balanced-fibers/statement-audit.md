# Statement-fidelity and adversarial audit

Checkpoint: candidates committed; formal acceptance remains pending until a
completed successful build plus both axiom audits are inspected. This is a
same-author semantic audit, not fulfillment of independent-human Issue #8.

## Existing measure, not a replacement definition

The target is the existing BalancedAffineCounting.inputMass from Expedition020.
It sums sampleMass over every sampleInput fiber. The tagged sample type is a
singleton coordinate or an ordered triple of coordinates. Its sampleMass is
1/(2n) on singleton samples,1/(2n(n-1)(n-2)) on distinct triples,0 on repeated
triples. sampleInput uses bits of the coordinate SUPPORT, not GF(2) addition
of coordinates with cancellation. The old actual-degree obstruction remains
unchanged and does not depend on this new closed formula.

## Fiber proof dependency direction

bits_ones and ones_bits establish actual Boolean/subset correspondence. A
weight-one support gives exactly one singleton sample. For triples, the existing
ordered_triple_moment applied to a set indicator counts distinct triples inside
that support by k(k-1)(k-2). At support size3, containment plus equal cardinality
forces equality, so the fiber has6 elements. Other support sizes cannot equal
three distinct coordinates. This proves the fibers instead of assuming uniformity.

The point-indicator specialization of the already proved inputMass_mean transports
these counts to inputMass. The cast choose(n,3)=n(n-1)(n-2)/6 then gives the
closed probability. Explicit n>=3 justifies nonzero denominators and the existing
normalization. Expected values are half the layer1 mean plus half the layer3
mean for EVERY real function, with no hidden nonnegative or symmetric-function
assumption. Exact tests include signed/nonsymmetric functions as controls.

## Generic intersection count

For an actual subset A of Fin n, Slice A w r contains exactly subsets X with
X.card=w and (X intersect A).card=r. The explicit split map sends X to its
inside/outside parts; inverse is disjoint union. Both inverse laws and sizes
are proof obligations. Cardinality is choose(A.card,r)*choose(n-A.card,w-r)
when r<=w. When r>w, the slice is empty. The Boolean-input form additionally
uses the proved bits/ones bijection. No finite enumeration or desired-count
hypothesis may replace these obligations.

n=0, A empty/full, w=0/n, impossible cardinalities and r>w are included by the
total guarded statement, not discarded. Natural subtraction makes omission
of the guard false at n1,A={0},w0,r1. That counterexample is also a formal target.

## Attack boundary

Dropping duplicate masses gives total7/12; pretending n2 is normalized gives
1/2. Both and the false unguarded count are in graveyard025. First formal
candidate failed implementation/type/warning checks; graveyard026 preserves
that distinct failure rather than presenting it as a mathematical refutation.

No previously accepted definitions, fields, degrees, real probabilities,
quantifier orders or axiom allowlists are changed. These standard exact counting
interfaces do not establish novelty, optimal support, arbitrary-n quadratic
upper bounds, new complexity-class results, barrier escape or P-vs-NP.
