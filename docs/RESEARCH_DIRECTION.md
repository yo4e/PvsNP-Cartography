# Research direction: exploration first, evidence kept precise

Policy update: 2026-10-22 JST. Research lead: 月野テンプレクス.
The steward authorized applying useful advice and left research choices to the
researcher. This is a direction update, not a new mathematical result or a
standing authorization to start nightly sessions.

## The objective remains research

P vs NP remains the long-horizon objective, including the possibility of a
substantial proof or counterexample. Curiosity, ambitious conjectures and
exploratory failure are welcome. Verification is how a claim earns trust;
it is not a substitute for choosing a worthwhile question. Neither avoid hard
problems to guarantee green builds nor invent significance for easy ones.

At a natural milestone, use the existing orientation and conclusion to say:
what mathematical uncertainty changed, and what would now be worth attempting,
changing or abandoning. No extra daily form, output quota, mandatory panel of
reviewers or new expedition solely to maintain this policy is needed. Additional
infrastructure should have a named mathematical use; useful reliability repairs
are allowed without pretending they are new mathematics.

## Immediate choice and exit from the current local loop

Keep [Issue #16](https://github.com/yo4e/PvsNP-Cartography/issues/16) as the next
bounded formal target: reuse the accepted profiles and real duality to finish
the precisely restricted n12 obstruction. This closes a real gap between an
exact finite certificate and its formal arbitrary-real-mixture statement.
It does not determine the degree of unrestricted n12 MOD3. Do not expand this
task into a general framework without a concrete need.

After that milestone, the default next direction is a **primary-source bridge
assessment**, not automatically n13, n14, or another counting wrapper. Choose
one precise restricted-lower-bound statement from the existing
[bibliography](BIBLIOGRAPHY.md) and [barrier map](../map/BARRIERS.md). Start by
examining the cited Smolensky polynomial-method source and the symmetric-function
probabilistic-degree source as candidates, not as assertions that our current
theorems instantiate either result.

Retrieve the primary statement, give its exact field, degree/error parameters,
input distribution/quantifiers and circuit restrictions, then compare it with
our definitions. Name the first missing implication or quantitative estimate
and reconstruct or attack that step. A useful result may be a faithful known
proof fragment, a specific mismatch, or a reason to change direction. An abstract
or a familiar theorem name is not enough. No exact external theorem statement
or newly established bridge is asserted by this policy document.

The researcher may choose a more promising structural conjecture instead,
with a brief reason in the existing log. A further finite-n experiment is
worth doing when it discriminates between stated hypotheses, tests a scaling
mechanism, or supplies a needed counterexample, not merely because n+1 exists.
If formal work stalls, retain the precise unfinished step and consider another
useful unblocked question; do not falsely close the issue or let sunk cost
force an unlimited repair loop.

## Conceptual dependency map at checkpoint caa83f30

This is a reading map of mathematical roles, NOT a generated import graph or
an exhaustive theorem/axiom dependency audit. Exact assumptions remain in the
source and [formal ledger](../formal/ASSUMPTIONS.md).

| Role | Main artifacts | What they supply and where the boundary is |
|---|---|---|
| Mathematical contract | [ProbabilisticDegree](../formal/PvsNPCartography/ProbabilisticDegree.lean), [DegreeOneNormalForm](../formal/PvsNPCartography/DegreeOneNormalForm.lean) | Actual total degree, a fixed normalized nonnegative real mixture before the input, and structural coverage of degree-one polynomials. |
| Lower-bound route | [FiniteDual](../formal/PvsNPCartography/FiniteDual.lean), [BalancedAffineObstruction](../formal/PvsNPCartography/BalancedAffineObstruction.lean), Expedition020 | Generic degree-one exclusion for n>=7; not exclusion of arbitrary quadratics or a growing-degree lower bound. |
| Pointwise upper-bound route | [FiniteSymmetrization](../formal/PvsNPCartography/FiniteSymmetrization.lean), [LayerCertificates](../formal/PvsNPCartography/LayerCertificates.lean), numerical Mod3*Degree modules | Full coordinate randomization connects layer inequalities to a fixed pointwise polynomial distribution. Existing exact degree-two results are n5..11. |
| Reusable evaluator | [HammingIntersections](../formal/PvsNPCartography/HammingIntersections.lean), [HammingProfiles](../formal/PvsNPCartography/HammingProfiles.lean), [CliqueProfiles](../formal/PvsNPCartography/CliqueProfiles.lean), Expedition021/022 | Actual overlap counts, signed weighted sums, polynomial degree/evaluation and short profiles. An evaluator does not itself guarantee approximation success. |
| Current negative application | [Restricted-family checker](../expeditions/022-certified-layer-profiles/restricted-family-dual.py), [result](../expeditions/022-certified-layer-profiles/restricted-dual-result.json), Issue #16 | Exact evidence for zero/all q9/all r8 at n12, including arbitrary reweighting within that family. Its dedicated Lean corollary is still pending. |
| Larger complexity objective | [Barrier map](../map/BARRIERS.md), [bibliography](BIBLIOGRAPHY.md) | Research leads and constraints. No completed deduction from the current MOD3 results to a general circuit lower bound or P-vs-NP separation is claimed. |

Keep four distinctions visible: definitions, general lemmas, finite applications,
and the presently unproved bridges. An import edge alone does not establish a
scientific implication, and a prose reading map does not replace an axiom audit.

## Describe the contribution, not only its verification status

In existing summaries distinguish **mathematical claim**, **formal reconstruction**,
**explicit computational certificate/counterexample**, and **research tooling**.
An artifact can contribute to more than one category. Preserve separate evidence
and novelty labels; this is not a retroactive claim-ledger schema migration.
A new machine-checkable encoding can be useful without a new mathematical theorem.
Retain `novelty-unknown` until a targeted literature comparison supports more.
Declaration counts, CI job counts and enumeration sizes describe verification
work, not a numerical distance to solving P vs NP.

## Independence and durable evidence, without a new bureaucracy

Gemini's corrected review in [Issue #15](https://github.com/yo4e/PvsNP-Cartography/issues/15)
applies to checkpoint0e30b5b7, not automatically to later profiles or obstructions.
It is an independent-AI semantic review with published finite tests, not a new
local Lean execution or a second proof kernel. Copilot's overview below is
process feedback, not another theorem-verification pass.

Request another reviewer when a concrete semantic blind spot or a materially
stronger claim warrants it. Independent problem reconstruction matters more
than collecting approvals. Changing the programming language or rerunning the
same Lean kernel elsewhere may improve replication, but neither automatically
creates independent semantics or an independent kernel. Human external academic
review (#8), additional kernel checking and publication decisions are separate;
they are not universal prerequisites for exploratory research.

For future substantive acceptance milestones, preserve the exact reviewed source
commit, resolved toolchain/library/workflow revisions, commands, completed status
and actual validation/axiom output. Prefer a durable, safely redacted full relevant
job log alongside the concise evidence summary; clearly label excerpts and missing
material. Record a runner-image identifier or container digest only when actually
available. Do not claim historical logs or a container digest have been archived
without retrieving them. This update adds no workflow, container migration or
blanket revalidation of previously accepted results.

## Provenance of this update

The steward pasted a GitHub Copilot repository overview in the conversation and
then authorized incorporating useful advice. It recommended distinguishing process
quality from mathematical reach, clarifying dependencies/contribution types,
strengthening genuinely independent checking and preserving execution evidence.
The overview did not provide a pinned reviewed commit, raw execution log or known
model version. It is therefore treated as attributed architectural advice only.
The researcher chose the changes above; this is not a claim that every suggestion
was implemented or independently verified. See the
[decision record](../logs/2026-10-22-research-direction.md).
