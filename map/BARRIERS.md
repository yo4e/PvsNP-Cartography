# Barrier Map

Status: orientation document. Not a substitute for reading the primary papers.

## Why barriers matter

A proof barrier does not prove that P vs NP is impossible to resolve.

It demonstrates that a broad family of proof methods cannot resolve it **in that form**.

Barrier awareness is therefore a filter for research time.

## 1. Relativization

Classical source: Baker–Gill–Solovay.

Core phenomenon:

There are oracle worlds in which relativized P and NP coincide and oracle worlds in which they differ.

Consequence:

A proof method that remains valid under arbitrary common oracle access cannot settle ordinary P vs NP.

Research questions for every candidate route:

- Where exactly does the argument use non-black-box structure?
- Would the key lemma still hold relative to every oracle?
- If not, identify the non-relativizing step explicitly.

Graveyard trigger:

If the entire proof relativizes and claims to settle P vs NP, bury it unless a concrete error in the barrier analysis is demonstrated.

## 2. Natural Proofs

Classical source: Razborov–Rudich.

Rough orientation:

A large class of combinatorial circuit-lower-bound arguments can be characterized by properties that are:

- constructive
- large
- useful against the target circuit class

Under appropriate pseudorandomness / cryptographic assumptions, sufficiently strong natural proofs would imply distinguishers that should not exist.

Research questions:

- What Boolean-function property is being used?
- Is membership efficiently decidable from the truth table?
- Does the property hold for a large fraction of functions?
- Would the property exclude the circuit class strongly enough?
- Which exact pseudorandomness assumption invokes the barrier?

Important:

“Natural” in ordinary English is irrelevant. Use the technical definition.

## 3. Algebrization

Primary source:

Scott Aaronson and Avi Wigderson, *Algebrization: A New Barrier in Complexity Theory*.

https://www.scottaaronson.com/papers/alg.pdf

Motivation:

Some major techniques escaped ordinary relativization using arithmetization, yet still survived a richer algebraic-oracle framework.

Consequence:

Merely saying “our proof is non-relativizing because it uses algebra” is not enough.

Research questions:

- Does the argument algebrize?
- Is the algebraic structure used in a way that survives low-degree oracle extension?
- What step depends on representation-specific structure that the algebraic oracle model destroys?

## 4. Barrier interaction

A candidate proof does not become plausible merely because it escapes one barrier.

For example:

- non-relativizing does not imply non-algebrizing
- non-natural does not imply correct
- an approach outside all three famous barriers can still be wrong for ordinary reasons

Barriers are filters, not certificates.

## 5. Operational rule

Each expedition must include a `barrier-audit.md` answering:

```text
Relativization:
Natural Proofs:
Algebrization:
Other known restrictions:
Unclear points:
```

If the correct answer is “unknown,” record unknown.

Do not fill the box with ceremonial prose.

## 6. Positive landmarks

The long-term map should also explain techniques that successfully prove lower bounds in restricted settings, including:

- AC0 lower bounds
- monotone circuit lower bounds
- algebraic lower bounds for restricted circuit classes
- NEXP vs ACC0

The research question is not merely:

> Why do proofs fail?

It is also:

> What structural ingredients make restricted lower-bound proofs succeed, and which ingredients stop scaling?
