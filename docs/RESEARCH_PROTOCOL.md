# Research Protocol

## Purpose

This protocol governs AI-assisted open mathematics in PvsNP-Cartography.

The central risk is not lack of ideas.

It is **mathematical self-deception at machine speed**.

## Research loop

Every expedition should follow:

> orient → state → derive → attack → compute → compare → formalize → attack again → classify

## 1. Orient

Before inventing a proof:

- identify the exact subproblem
- retrieve known results
- identify relevant proof barriers
- inspect prior AI attempts
- define what would count as progress

Output:

`expeditions/<id>/orientation.md`

## 2. State

Write the proposed claim precisely.

Bad:

> SAT seems fundamentally sequential.

Better:

> For model M under assumptions A, every circuit family computing function F requires resource R(n) ≥ ...

If the statement cannot be written precisely, it is not ready to prove.

Output:

`claims/<claim-id>.md`

with status `idea` or `candidate`.

## 3. Derive

Attempt a proof in small lemmas.

Each lemma should state:

- assumptions
- quantifiers
- dependencies
- target conclusion

Avoid prose transitions such as “clearly,” “therefore,” or “it follows” unless the implication is actually supplied.

## 4. Attack

Switch roles.

The attacking pass should assume the proof is wrong.

Search for:

- quantifier reversal
- hidden uniformity assumptions
- finite-to-asymptotic leaps
- average-case to worst-case leaps
- oracle/relativization issues
- natural-proof structure
- algebrization
- nonuniform vs uniform confusion
- circuit-size vs time-complexity confusion
- NP vs NP-complete confusion
- unproved hardness assumptions
- tautological reformulations
- circular dependence
- misuse of physical/computational intuition
- proof-assistant axioms or placeholders masquerading as proof

Output:

`attacks/<claim-id>-attack-XX.md`

## 5. Compute

Use computation primarily to:

- find counterexamples
- test boundaries
- compare restricted models
- generate candidate structure
- reproduce known finite results

Never promote finite evidence to asymptotic theorem status.

Every experiment must record:

- code
- parameters
- random seeds where relevant
- machine assumptions where relevant
- exact output
- interpretation
- what the experiment does **not** establish

## 6. Compare

Search prior literature after obtaining a candidate insight, not only before.

A model can independently rediscover known mathematics.

Novelty status must remain `novelty-unknown` until targeted search is completed.

## 7. Formalize

If a claim survives attack and is formalizable at reasonable cost:

- encode definitions explicitly
- minimize axioms
- audit imported assumptions
- avoid placeholder theorems
- record whether the formal statement actually matches the informal claim

A compiling Lean file is not sufficient evidence if the desired theorem was assumed as an axiom.

## 8. Attack again

Formalization often reveals that the original informal statement changed.

Re-run conceptual attack after the formal version exists.

## 9. Classify

End each expedition with one of:

- `refuted`
- `inconclusive`
- `finite-evidence`
- `known-result-reconstructed`
- `candidate-survives`
- `formally-verified`
- `novelty-unknown`
- `novelty-supported`

Anything refuted goes to `graveyard/` with a post-mortem.

## Barrier checklist

Every proposed P vs NP route should answer:

### Relativization

Does the argument remain valid if all relevant machines receive the same arbitrary oracle?

If yes, explain why this does not collide with Baker–Gill–Solovay.

### Natural Proofs

If the approach seeks strong circuit lower bounds using a property of Boolean functions:

- Is the property constructive?
- Is it large?
- Is it useful?

If so, state the cryptographic assumptions under which the Razborov–Rudich barrier applies.

### Algebrization

Would the argument survive algebraic oracle access in the Aaronson–Wigderson sense?

Do not use “non-relativizing” as a synonym for “barrier-free.”

## AI-specific failure modes

### Fluency bias

A smooth proof is not a correct proof.

### Citation hallucination

Never trust a remembered theorem statement when exact assumptions matter.

### Convergence illusion

Multiple agents can agree because they share training data, prompts, or the same hidden mistake.

Agreement is not independent verification.

### Formalization theater

Lean can verify the wrong theorem perfectly.

Always compare formal and informal statements.

### Benchmark contamination

Known competition or textbook proofs are not evidence of original research capability.

### Search overfitting

If thousands of conjectures are tried, a handful of apparently striking finite patterns will appear by chance.

Track search volume.

## Publication threshold

Do not publicly describe a result as new mathematics until:

1. statement is precise
2. attack record exists
3. relevant computation is reproducible
4. known literature has been searched
5. formal verification exists where feasible
6. assumptions are disclosed
7. an independent mathematical reviewer has had a chance to inspect it

For Millennium-level claims, formal verification is necessary but not sufficient.

## Research roles

The same model may alternate roles, but the roles must remain logically distinct:

- **Cartographer** — maps known territory
- **Explorer** — proposes routes
- **Skeptic** — attempts destruction
- **Experimentalist** — runs finite computation
- **Formalist** — translates to proof assistant
- **Historian** — checks literature and novelty
- **Archivist** — records both success and failure

The repository should make role transitions visible in artifacts rather than relying on internal intention.

## Success condition

A successful session does not require a positive theorem.

A session is successful if uncertainty decreases.
