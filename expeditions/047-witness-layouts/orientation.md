# Orientation — which proof layouts may depend on the witness?

Approved November 24, 2026 JST night; work continued after midnight November 25.
Base commit: `ce66bdc08702922138dc77b93c6c2b4054873944`. Research lead:
月野テンプレクス. This is the fresh approval's single session, not authorization
for another night.

## Question and decision criterion

Issue 36 follows the coefficient-tag completion in Expedition 046. That
completion knows the named honest proof. The missing implication is whether
a layout usable without first finding an unknown witness has the same useful
degree/storage behavior. The finite compiler already prices its NO failures
and mixed-error sensitivity; another field size alone would not answer this.

We seek (a) an explicit public structural condition and a genuinely
multiple-witness control, or (b) a scoped obstruction over satisfying proofs.
We also audit whether witness dependence is intrinsically invalid in the
downstream nondeterministic algorithm, rather than merely outside the public
compiler model. The question is about quantifiers and cost, not a new claim
of a complexity separation.

## Reading and parallel roles

Read AGENTS.md and its five mandatory documents, RESEARCH_DIRECTION.md,
current status, open Issues 8/15/36, latest commits, and Expedition 046.
The frozen source, not earlier chat recollection, establishes the frontier.
Issues 8 and 15 remain separate review gates.

Three bounded same-model branches supplied a public-dictionary construction,
a satisfying-RS-witness attack, and a primary-source/quantifier audit. The
research lead inspected the scripts and arguments, supplied the shared-map
collision correction, wrote a separate guessed-layout checker, and integrated
the results. Shared lineage and context mean this is adversarial exploration,
not independent external review.

## What changed mathematically

The old YES fixture is unique on all used bits, so it cannot test two unknown
satisfying witnesses. A public symbolic dictionary gives an exact
witness-independent layout under a dimension/seed-degree hypothesis. The
shared RS checks alone do not imply that hypothesis: a code-only relaxation
has enough independent systematic bits to defeat an all-witness guarantee.
That obstruction does not defeat existential completeness.

Finally, one globally shared guessed row map can preserve NO soundness.
The problem with an explicit map in the current growing compiler is its
description/time cost, not witness dependence alone. This changes the next
research decision: stop trying to obtain a universal guarantee from these
RS checks, and inspect a succinct map in the actual fixed-rate recursive
projection setting, with all descriptor and counting costs included.
