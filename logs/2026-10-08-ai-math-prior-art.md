# 2026-10-08 — AI mathematics prior-art audit

Role: Historian / Skeptic

Issue: #4

## Scope

Audited the seed research systems/programs against a common ten-field template:

- source
- problem class
- natural-language vs formal mode
- verifier / feedback
- search / revision loop
- human role
- evidence / publication protocol
- limitations
- method worth borrowing
- failure mode to avoid

## Primary / official sources checked

### OpenAI

- *Sharing AI progress in mathematics* (2026-10-06)
- *An OpenAI model has disproved a central conjecture in discrete geometry* (2026-05-20)
- *On the Navier–Stokes Millennium Prize Problem* (2026-09-08)
- *Advisory Group on Mathematics and Artificial Intelligence* (2026-09-21)

Important process observations:

- the October portfolio release publishes attempted-problem/compute information and many Lean formalizations;
- the unit-distance result provides a useful counterexample-first precedent but no kernel-level verifier is claimed in the overview;
- the Navier–Stokes run exposes unusually detailed multiagent mechanics: proof/disproof variants, adjacent easier Euler work, resource reallocation, cross-pollination, and final Lean verification;
- the advisory group is governance, not proof verification.

### Google DeepMind — AlphaProof

Checked the Nature paper *Olympiad-level formal mathematical reasoning with reinforcement learning* and DeepMind's public overview.

Important process observations:

- Lean is the search environment, not a post-hoc badge;
- tactic execution provides exact feedback;
- TTRL trains on generated variants for hard targets;
- manual statement formalization remained part of the live IMO protocol;
- huge bespoke training/inference compute is a material limitation.

### Google DeepMind — Gemini Deep Think / Aletheia

Checked the 2026-02-11 DeepMind research overview.

Important process observations:

- explicit generator → verifier → reviser/restart loop;
- natural-language verifier, not a proof-assistant kernel;
- web/literature tools;
- failure is an allowed output;
- balanced proof/refutation prompting is explicitly recommended;
- public taxonomy records AI contribution/significance and avoids claiming top levels for the summarized work.

### LeanDojo / ReProver

Checked the NeurIPS paper and current project state.

Important process observations:

- programmatic Lean proof-state interaction;
- retrieval over formal premises;
- open benchmark/code/data;
- original LeanDojo is now deprecated for new work in favor of LeanDojo-v2.

## Adversarial synthesis

Three recurring traps were added to the map:

1. **verification collapse:** model critique, code execution, expert review, and kernel checking are different evidence classes;
2. **parallelism illusion:** many same-lineage agents are not independent replication;
3. **formalization displacement:** correctness can fail at statement translation even when the proof term is valid.

## Result

`docs/PRIOR_ART.md` was upgraded from orientation notes to an operational audit map.

No claim of independent validation of the labs' headline mathematical results is made. The cited organizational pages are used as primary evidence for their reported workflow and release practices.
