# Statement-fidelity and adversarial audit: accepted checkpoint

Accepted source598d54ed0940a331650b7e7eb733d62c9b6e40ab completed pinned
production run39547776930/job119049747106: --wfail9050 jobs,639 namespace
declarations and12 explicit new targets within the unchanged foundational
allowlist. Full actual output, source statements and matching commit/tree
were fetched. This is an author audit, NOT fulfillment of human-review #8.

## Existing measure, not a replacement definition

The target is the existing BalancedAffineCounting.inputMass from Expedition020.
It sums sampleMass over every sampleInput fiber. The tagged sample type is a
singleton coordinate or an ordered triple of coordinates. Its sampleMass is
1/(2n) on singleton samples,1/(2n(n-1)(n-2)) on distinct triples,0 on repeated
triples. sampleInput uses bits of the coordinate SUPPORT, not GF(2) addition
with cancellation. No previous actual-degree obstruction statement is changed.

## Fiber proof dependency direction

bits_ones and ones_bits establish actual Boolean/subset correspondence. A
weight-one support has exactly one singleton sample. The existing generic
ordered_triple_moment applied to a set indicator counts distinct triples inside
that support by k(k-1)(k-2). At support size3, containment plus equal cardinality
forces equality, yielding six fibers. Other support sizes cannot equal the
support of three distinct coordinates. Uniform fibers are proved, not assumed.

Specializing the previously proved inputMass_mean to a point indicator
transports these counts to the actual existing inputMass. The cast identity
choose(n,3)=n(n-1)(n-2)/6 gives the closed mass. Explicit n>=3 discharges the
nonzero denominator conditions and supplies the normalized-probability setting.
For every real function g, expectation is half the layer1 mean plus half the
layer3 mean. No nonnegativity or symmetry assumption on g is smuggled in.

The singleton/triple fiber counts and decomposed totalized-division formula
hold at all n, including0,1,2. The final normalized probability interpretation
is stated for n>=3. The n2 counterexample refutes normalization, not necessarily
the bare algebraic layer-mean identity when empty-layer means are totalized.

## Generic intersection count

Slice A w r contains actual subsets X with X.card=w and |X intersect A|=r.
The proved splitEquiv sends X to its inside/outside parts; inverse is disjoint
union. Both inverse laws and size obligations are discharged. The resulting
cardinality is choose(A.card,r)*choose(n-A.card,w-r) if r<=w, and zero otherwise.
The Boolean-input version additionally uses the established bits/ones bijection.
No finite search or desired-count hypothesis replaces these proof obligations.

n=0, A empty/full, w=0/n, impossible cardinalities and r>w are included in the
total statement. Nat subtraction truncates, making omission of the guard false
at n1,A={0},w0,r1. The actual zero count and false expression1 are also accepted
as a formal counterexample in the same module.

## Attacks and preserved implementation failures

Discarding duplicate triple probability gives total7/12; extending normalized
probability to n2 gives1/2. These and the unguarded count are in graveyard025.
First and second formal candidates failed on conditional elaboration/rewrite
and warning checks. They are archived in graveyard026/027, not called
mathematical refutations. The final repair changes only proof implementation.

No prior definition, GF(2) field, polynomial degree, real probability,
quantifier order, warning policy or foundational axiom allowlist was relaxed.
These are standard exact counting interfaces. They do not establish novelty,
optimal support, arbitrary-n quadratic upper bounds or P-vs-NP conclusions.
