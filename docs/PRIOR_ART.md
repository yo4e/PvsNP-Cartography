# Prior Art Map

Status: **living audit map**

This document maps earlier AI-assisted attempts relevant to P vs NP and the broader problem of AI-driven mathematical research.

The purpose is not to rank systems. It is to avoid duplicated work, inherit methods that are actually inspectable, and identify failure modes before importing them.

For external systems, claims below describe what the cited primary/official sources report. A vendor or lab report is not treated as independent verification merely because it is an official source.

## A. Direct P vs NP / complexity projects

### GISMO-1/p-vs-np-hunter

Primary project:

https://github.com/GISMO-1/p-vs-np-hunter

Closest known public project to this repository's intended direction.

Observed structure:

- multi-agent architecture
- circuit exploration
- SAT instance generation
- lower-bound hunting
- conjecture synthesis
- Lean formalization
- meta-learning / barrier tagging
- CI and known-result validation

Useful method:

- preserve finite computational findings as inspectable artifacts and expose formal files alongside them.

Failure mode to avoid:

- theorem-looking labels can outrun the implementation and formal layer.

PvsNP-Cartography Expedition 001 independently reproduced part of the public finite-degree output and found a definition mismatch: non-graph “approximate degree” values are formulas/extrapolations, while graph rows compute exact algebraic degree. See:

- `expeditions/001-audit-pvsnp-hunter/conclusion.md`
- `graveyard/001-approximate-degree-interpretation.md`

The current Lean lower-bound layer also contains axiomatized landmarks and placeholder propositions. A compiling formal file is therefore evidence only after statement and assumption audits.

### LLMDeveloperAiPNP autonomous solver

Primary project:

https://github.com/LLMDeveloperAiPNP/LLM-Developer-AiPNPvs-NP---Autonomous-Solver-Ai

Reported design:

- complexity theorist
- algebraist
- formalist
- literature watcher
- skeptic
- intuitionist
- metacognitive architect
- shared knowledge graph and strategy-pivot machinery

Useful method:

- explicit skeptic role and stagnation detection.

Failure mode to avoid:

- agent choreography becoming the deliverable. Roles, graphs, and orchestration are not mathematical evidence.

### MuchuCAT/p-vs-np-ai-quantum-research-notes

Primary project:

https://github.com/MuchuCAT/p-vs-np-ai-quantum-research-notes

Reported emphasis:

- formal P/NP definitions
- relativization
- Natural Proofs
- algebrization
- restricted lower bounds
- AI/LLM limitations
- quantum-complexity context

Useful method:

- barrier literacy before speculative proof search.

Failure mode to avoid:

- remaining forever at survey level without reconstructing a theorem or falsifiable subproblem.

### RenaudGL/Protocol_Cathedrale

Primary project:

https://github.com/RenaudGL/Protocol_Cathedrale

A multi-model research experiment exploring a thermodynamic route to `P != NP`.

Useful method:

- make conditional bridges explicit and preserve cross-model disagreement.

Failure mode to avoid:

- treating physical intuition or empirical thermodynamics as a complexity-class theorem without a formal mathematical bridge.

### chsahaka/llm-adversarial-theorem-prover

Primary project:

https://github.com/chsahaka/llm-adversarial-theorem-prover

Useful methodological precedent:

- multiple failed proof attempts remain visible.

Method worth borrowing:

- failed attempts are first-class research data.

This directly motivates this repository's `graveyard/`.

---

## B. AI mathematics systems and research programs

Each audit records the same fields:

1. source
2. problem class
3. natural-language vs formal mode
4. verifier / feedback
5. search / revision loop
6. human role
7. evidence / publication protocol
8. limitations for this repository
9. one method to borrow
10. one failure mode to avoid

### B1. OpenAI internal frontier-model mathematics portfolio — October 2026

Primary source:

https://openai.com/index/sharing-ai-progress-in-mathematics/

Publication date: 2026-10-06.

#### Problem class

A portfolio of open research problems across mathematics, rather than one benchmark family.

#### Natural-language vs formal mode

The public overview reports model-generated mathematical results and says many proofs are also being released with Lean formalizations.

The overview does **not** establish that Lean was the search environment for the original discoveries. Treat discovery and later formalization as separate stages unless a result's own record says otherwise.

#### Verifier / feedback mechanism

- Lean checks many released formalizations.
- mathematical papers remain subject to ordinary mathematical review and statement-fidelity checking.
- an independent Advisory Group on Mathematics and Artificial Intelligence informed release practices.

A Lean proof verifies its formal statement under its dependencies. It does not automatically prove that the formal statement matches the informal theorem.

#### Search / revision loop

The overview does not publicly specify one universal internal search loop.

What it does disclose is unusually useful for interpretation:

- statistics about attempted problems;
- estimates of compute spent;
- ten reasoning summaries;
- revision and citation protocols in the public GitHub release.

Unknown internal details should remain unknown rather than reconstructed from marketing prose.

#### Human role

Humans select research/release policy, curate the public release, improve exposition and citations, and coordinate with the mathematics community. The independent advisory group provides external guidance on review and communication.

#### Evidence / publication protocol

The release uses a public GitHub repository with:

- manuscripts/results;
- many Lean formalizations;
- revision and citation protocols;
- attempted-problem statistics;
- compute estimates;
- selected reasoning summaries.

#### Limitations relevant here

- the underlying frontier model is internal;
- end-to-end replication of discovery is therefore unavailable;
- a released portfolio creates selection effects, so successful papers should be read together with attempted-problem counts;
- formalization coverage is partial;
- public reasoning summaries are not a complete search trace.

#### Borrow

**Record the denominator.** Preserve attempted targets, compute, failures, and revision history, not only surviving results.

#### Avoid

A polished portfolio can create survivorship bias. Never infer a method's reliability from successful outputs without the search volume and failure record.

---

### B2. OpenAI unit-distance result — counterexample-first frontier search

Primary source:

https://openai.com/index/model-disproves-discrete-geometry-conjecture/

Publication date: 2026-05-20.

#### Problem class

A long-standing open problem in discrete/combinatorial geometry: the planar unit-distance problem and the conjectured `n^(1+o(1))` growth behavior.

#### Natural-language vs formal mode

The reported discovery was a natural-language mathematical proof from a general-purpose reasoning model. The release links the proof, companion remarks by external mathematicians, and an abridged reasoning trace.

No Lean or other kernel-level formalization is claimed on the overview page.

#### Verifier / feedback mechanism

The proof was checked by a group of external mathematicians. The external companion work provides mathematical context and further analysis.

That is expert review, not an executable formal verifier.

#### Search / revision loop

The source says the model was evaluated on a collection of Erdős problems and was not a mathematics-specific system scaffolded to search proof strategies for this target.

The exact internal retry/revision tree for this problem is not disclosed.

A notable qualitative feature of the released reasoning is heavy effort toward constructing a counterexample rather than proving the prevailing conjecture.

#### Human role

Humans:

- selected the broader evaluation portfolio;
- independently checked the result;
- wrote companion analysis;
- interpreted the significance and subsequent refinements.

#### Evidence / publication protocol

- public proof;
- companion paper by external mathematicians;
- abridged reasoning trace;
- discussion of later refinement and verification.

#### Limitations relevant here

- no machine-checkable proof is advertised;
- external review is strong evidence but not a substitute for reproducible formal checking where feasible;
- portfolio selection means the successful problem is one draw from a wider evaluation set;
- the full search history is unavailable.

#### Borrow

**Attack conjectures by construction before trying to prove them.** In PvsNP-Cartography, counterexample search should be an equal first-class branch for every candidate lemma.

#### Avoid

Do not let community confidence in a conjecture bias the attack direction. Also do not use “experts checked it” as a replacement for preserving an inspectable derivation when we can do better.

---

### B3. OpenAI Navier–Stokes multiagent research run

Primary source:

https://openai.com/index/navier-stokes-solution/

Publication date: 2026-09-08.

#### Problem class

Open Millennium-level PDE research, plus related Euler regularity questions.

#### Natural-language vs formal mode

The reported pipeline has both:

- analytical/natural-language discovery by a large coordinating multiagent system;
- a Lean formalization and verification stage, reported as an additional 17 hours using GPT-6 Astra.

#### Verifier / feedback mechanism

- code execution and cached-web access during research;
- cross-group consolidation of useful intermediate insights;
- final Lean formalization / verification.

The public overview still requires the same statement-fidelity caution as any formalization: kernel acceptance is not, by itself, proof that the encoded statement matches every informal claim.

#### Search / revision loop

This source exposes a concrete loop rather than only a final result:

1. separate groups received different problem variants;
2. proof-side variants A/B and disproof-side variants C/D were assigned separately;
3. easier related problems were attempted;
4. an Euler result changed resource allocation toward Navier–Stokes;
5. groups explored diverse approaches;
6. Codex consolidated useful intermediate results across groups;
7. follow-up groups were prompted with those consolidated insights;
8. the final result was formalized and checked in Lean.

The run reportedly used on the order of 10,000 concurrent agents for the Navier–Stokes resolution, 2.7 million messages, and roughly 130 billion output tokens for that problem.

#### Human role

Researchers:

- selected the high-impact evaluation portfolio;
- chose problem variants;
- allocated/reallocated compute;
- supplied the Euler result back into later prompts;
- managed release, priority, and provenance questions.

This is not “AI without humans”; it is a high-autonomy search process under substantial human experimental design.

#### Evidence / publication protocol

- public analytical paper;
- public Lean formalization;
- disclosed search architecture, rough message/token counts, and chronology;
- public discussion of concurrent work and provenance investigation;
- explicit statement that OpenAI did not intend to claim the Millennium Prize.

#### Limitations relevant here

- discovery is not reproducible without the internal model and enormous compute;
- brute-force breadth can hide correlated errors because agents share model lineage;
- cross-pollination improves search but reduces independence between branches;
- scale is not a proof-quality metric;
- a formalization still needs assumption and statement audits.

#### Borrow

Two methods are especially portable:

1. **balanced search:** send proof and refutation variants down independent branches;
2. **adjacent easier target:** use a nearby solvable/killable problem to reveal structure before returning to the hard target.

#### Avoid

Do not count thousands of agents as thousands of independent reviewers. Shared models, prompts, and cross-pollination can amplify one hidden mistake at industrial scale.

---

### B4. OpenAI / IAS Advisory Group on Mathematics and AI — release governance

Primary source:

https://openai.com/index/advisory-group-on-mathematics-and-ai/

Publication date: 2026-09-21.

This is not a theorem-proving system. It belongs in the map because publication governance becomes part of the research protocol once AI can generate many plausible mathematical claims.

#### Problem class

Review, communication, dissemination, and professional standards around AI-generated mathematical results.

#### Natural-language vs formal mode

Not applicable as a solver. The group advises on both mathematical significance and communication practices; it is not itself the proof verifier.

#### Verifier / feedback mechanism

Human expert criticism and community-facing governance.

#### Search / revision loop

Not applicable to theorem search. Its loop is institutional: emerging result → significance/review advice → dissemination guidance → public/community feedback → revised standards.

#### Human role

Central. The source states that the group operates independently, can offer unsolicited criticism, can publish its advice, is unpaid by OpenAI, and does not control the pace of OpenAI's internal mathematical progress.

#### Evidence / publication protocol

The group advises on:

- significance assessment;
- dissemination coordination;
- academic/professional standards;
- how AI tools can support research and learning.

#### Limitations relevant here

- advisory governance cannot certify correctness of individual proofs;
- independence of advice does not make the group a substitute for peer review;
- it explicitly does not govern the pace of internal capability development.

#### Borrow

For any high-stakes result, separate **research production** from **release judgment**. A reviewer should be empowered to say “do not publish this claim yet.”

#### Avoid

Do not outsource scientific responsibility to an advisory body. The repository still owns statement precision, provenance, replication, and correction.

---

### B5. Google DeepMind AlphaProof

Primary sources:

- Nature paper: https://www.nature.com/articles/s41586-025-09833-y
- DeepMind overview: https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/

Nature version of record: 2026.

#### Problem class

Formal theorem proving for competition mathematics, including historical IMO, miniF2F, and Putnam-level problems.

#### Natural-language vs formal mode

The proving environment is formal Lean.

Natural-language problems are auto-formalized into Lean at scale for training. For the 2024 IMO evaluation, non-geometry problems were manually formalized by experts after release; some “find all” answer candidates were generated using Gemini before AlphaProof proved/refuted formal candidates.

#### Verifier / feedback mechanism

Lean is the environment, not merely the final checker.

A state is the Lean tactic state; an action is a Lean tactic; Lean executes it and provides the next proof state. A completed proof must be accepted by Lean's kernel.

This gives search a grounded reward signal rather than relying on another language model to say whether a proof step “looks right.”

#### Search / revision loop

- policy/value network proposes tactics and estimates proof difficulty;
- specialized tree search explores tactic sequences;
- successful/failed interaction feeds reinforcement learning;
- millions of auto-formalized variants provide a curriculum;
- difficult target problems use test-time reinforcement learning (TTRL) on generated related variants.

#### Human role

Humans are still important:

- experts created the seed formalization data;
- 2024 IMO non-geometry statements were manually formalized;
- benchmark design and train/test separation were human research choices;
- geometry was delegated to a different specialized system because of formal-library limitations.

#### Evidence / publication protocol

- peer-reviewed Nature paper;
- benchmark methodology and held-out splits;
- public benchmark/formalization data for several evaluation sets;
- pseudocode and detailed methods/hyperparameters;
- Lean-checked proof artifacts.

#### Limitations relevant here

- formal search assumes a correct formal statement;
- auto-formalization is therefore its own correctness problem;
- the strongest runs use very large compute budgets, including problem-specific TTRL;
- bespoke training scale is explicitly noted as beyond most academic groups;
- library coverage shapes what can be formalized and solved.

#### Borrow

**Put the verifier inside the search loop.** Once a PvsNP-Cartography claim has a faithful Lean statement, proof-state feedback is preferable to free-form proof prose followed by a ceremonial final check.

Generated nearby variants are also attractive for testing whether a lemma is robust or accidentally tailored.

#### Avoid

Formal verification theater can move one layer earlier: a system may perfectly prove the wrong translation. Statement fidelity must be attacked independently of proof validity.

---

### B6. Google DeepMind Gemini Deep Think / Aletheia

Primary source:

https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/

Publication date: 2026-02-11.

#### Problem class

Research-level pure mathematics and broader scientific/theoretical work, not only formal or competition problems.

#### Natural-language vs formal mode

Primarily natural-language research.

Aletheia is described as a research agent around Gemini Deep Think with a natural-language verifier. It also uses web search/browsing and, in related workflows, code-assisted verification.

#### Verifier / feedback mechanism

The central verifier is another natural-language reasoning component, not a proof-assistant kernel.

The public diagram exposes three outcomes:

- correct → final output;
- minor fixes → reviser → candidate again;
- critically flawed → restart at generator.

The agent can also return failure rather than forcing a solution.

Human experts graded reported benchmark results.

#### Search / revision loop

Explicit:

`generator → candidate → verifier → revise/restart → final or failure`

The source also reports:

- literature navigation via Google Search/web browsing;
- balanced prompting that asks for proof **or refutation**;
- code-assisted verification;
- research runs over large portfolios, including 700 Erdős problems.

#### Human role

The work is described as operating under expert mathematician/scientist direction, with examples spanning autonomous, AI-guided collaboration, and human+AI research.

The release proposes a taxonomy recording both significance and degree of AI contribution, and publishes a Human-AI Interaction card for the associated work.

#### Evidence / publication protocol

The source links:

- research papers;
- prompts and model outputs;
- a contribution/significance taxonomy;
- human-expert grading;
- interaction documentation.

It explicitly states that it does not claim Level 3 “Major Advance” or Level 4 “Landmark Breakthrough” results for the body of work summarized there.

#### Limitations relevant here

- a natural-language verifier is fallible and may share correlated errors with the generator;
- some performance benchmarks are internal;
- web browsing reduces citation hallucination risk but does not establish theorem correctness;
- “autonomous” describes workflow contribution, not independent verification.

#### Borrow

Two immediately useful practices:

1. **failure is an allowed terminal state**;
2. **balanced prompting:** search for proof and refutation concurrently to reduce confirmation bias.

Its explicit generator/verifier/reviser state machine is also a useful model for our claim lifecycle.

#### Avoid

Do not call self-critique independent review. Generator and verifier can converge on the same hidden error, especially when built from closely related models.

---

### B7. LeanDojo / ReProver

Primary sources:

- paper: https://arxiv.org/abs/2306.15626
- current project: https://github.com/lean-dojo/LeanDojo-v2
- project site: https://leandojo.org/

The original LeanDojo repository now directs new users to LeanDojo-v2.

#### Problem class

Machine-learning-assisted **formal theorem proving in Lean**, with emphasis on programmatic proof-environment interaction, data extraction, premise selection, training, and evaluation.

#### Natural-language vs formal mode

Formal Lean theorem proving.

ReProver augments a language-model prover with retrieval over available formal premises.

#### Verifier / feedback mechanism

Lean executes proposed tactics and returns proof states/errors. LeanDojo exposes that interaction to external agents programmatically.

This turns the theorem prover into an environment with inspectable feedback rather than asking a model to judge its own prose.

#### Search / revision loop

A prover can repeatedly:

1. inspect the current tactic state;
2. retrieve relevant premises;
3. propose a tactic;
4. execute it in Lean;
5. continue from the resulting state or backtrack after failure.

The original paper's benchmark contains 98,734 Mathlib theorems/proofs and includes a split designed to test generalization to premises not used in training proofs.

#### Human role

Humans build the interface, datasets, retrieval/training machinery, benchmarks, and agents. The theorem prover supplies kernel checking; the system does not remove the need to choose faithful theorem statements.

#### Evidence / publication protocol

- NeurIPS 2023 paper;
- open code/data/models;
- public benchmark;
- permissive release;
- current v2 codebase for new projects.

#### Limitations relevant here

- LeanDojo is infrastructure, not an autonomous research mathematician;
- theorem-proving benchmarks can reward proof completion without testing research novelty;
- theorem-statement fidelity remains external;
- version compatibility is operationally significant, and the original codebase is now deprecated in favor of v2.

#### Borrow

Before inventing a bespoke Lean agent protocol, evaluate LeanDojo-v2 or an equivalent maintained proof-state interface.

Retrieval over *accessible* premises is especially relevant once our formal library grows beyond a handful of files.

#### Avoid

Do not optimize against a theorem benchmark and mistake higher solve rate for open-mathematics progress. Also do not freeze research tooling around a deprecated prover interface without checking current maintenance state.

---

## C. Cross-system lessons for PvsNP-Cartography

### C1. Verification is not one thing

There are at least four distinct verification modes in the systems above:

| Mode | Example | Strength | Main residual risk |
|---|---|---|---|
| model self-critique | Aletheia natural-language verifier | fast semantic criticism | correlated hallucination |
| executable computation | research agents with code | exact for the implemented computation | wrong quantity / wrong encoding |
| expert mathematical review | unit-distance external review | deep conceptual scrutiny | not mechanically reproducible |
| proof-assistant kernel | AlphaProof / Lean formalizations | exact formal derivation checking | wrong statement / hidden assumptions |

A serious claim may need more than one mode.

Expedition 001 already demonstrated why executable code is not enough: the code can faithfully compute the wrong named quantity.

### C2. Search diversity needs independence accounting

Parallel agents are useful, but “10,000 agents” does not imply 10,000 independent opinions.

Record:

- shared model lineage;
- shared prompt templates;
- cross-pollination points;
- common retrieved sources;
- verifier lineage.

Consensus after information sharing is evidence of convergence, not independent replication.

### C3. Counterexample and failure channels should be explicit

Two strong precedents converge here:

- the OpenAI unit-distance result emerged by attacking a prevailing conjectural direction with constructions;
- Aletheia explicitly permits failure and balanced proof/refutation prompting.

PvsNP-Cartography should continue treating refutation and graveyard entries as successful research outcomes.

### C4. Formalization should enter only after statement fidelity is explicit

AlphaProof shows the power of verifier-in-loop search.

Expedition 001 shows the danger of names outrunning definitions.

Therefore our order should be:

`informal target → exact definition → statement-fidelity attack → formal statement → proof search → axiom audit`

not:

`impressive theorem name → Lean file → compilation → celebration`.

### C5. Release process is part of epistemology

Once a system can attempt hundreds or thousands of open problems, the following affect how evidence should be interpreted:

- attempted-problem count;
- compute budget;
- selection criteria;
- revision history;
- external review;
- formalization coverage;
- human/AI contribution record.

These are not public-relations metadata. They are part of the denominator behind a claimed success.

---

## D. Methods adopted by this repository

From the audits above, PvsNP-Cartography adopts or reinforces:

1. **Attempt-volume accounting** — record the denominator, not only successes.
2. **Proof/refutation branching** — attack both directions where a claim permits it.
3. **Failure as terminal success** — a killed claim is useful output.
4. **Verifier-in-loop formal work** — once the statement is faithful enough to formalize.
5. **Independent statement audit** — a checked proof can still encode the wrong theorem.
6. **External release gate for exceptional claims** — production and publication judgment should be separate.
7. **Human-AI contribution disclosure** — record problem selection, steering, formalization, and interpretation.
8. **Tool-maintenance checks** — use maintained formal infrastructure rather than cloning stale interfaces.
9. **Cross-pollination logging** — distinguish diverse exploration from independent replication.
10. **Counterexample-first pressure** — constructions and tiny exact cases before asymptotic narrative.

## E. Immediate relevance to P vs NP

The strongest lesson is not “use more agents.”

For this repository, the high-value sequence is:

1. define the quantity;
2. reproduce a known result;
3. attack the definition and encoding;
4. run exact tiny counterexample searches;
5. map barrier collisions;
6. formalize surviving statements with audited assumptions;
7. only then scale search.

That ordering is slower than proof-shaped text generation and much faster than spending a month polishing a false lemma.
