# Working Bibliography

This is a working source map, not yet a publication-ready bibliography.

Prefer primary papers and official project pages. Secondary summaries are useful for orientation but should not carry theorem-level claims when the original source is available.

## P vs NP: official problem statement

### Clay Mathematics Institute — P vs NP

https://www.claymath.org/millennium/p-vs-np/

Official Millennium Prize Problem page.

### Stephen Cook — The P versus NP Problem

Official Clay problem description:

https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf

Use this as a canonical source for the statement and historical framing of the problem.

## Core proof barriers

### Baker, Gill, Solovay — Relativizations of the P =? NP Question

Theodore Baker, John Gill, Robert Solovay. **“Relativizations of the P =? NP Question.”** *SIAM Journal on Computing* 4(4), 431–442, December 1975.

DOI: https://doi.org/10.1137/0204037

Primary facts used in `map/BARRIERS.md`:

- for oracle `X`, `P^X` and `NP^X` are polynomial-time deterministic/nondeterministic query-machine classes;
- there is a recursive oracle `A` with `P^A = NP^A`;
- there is a recursive oracle `B` with `P^B != NP^B`.

Research rule: the usual “relativizing methods cannot settle P vs NP” statement is a method-level consequence of these oracle worlds. Keep it distinct from the literal theorem/construction.

### Razborov, Rudich — Natural Proofs

Alexander A. Razborov, Steven Rudich. **“Natural Proofs.”** ECCC TR94-010, 12 December 1994. Conference version: STOC 1994. Journal version: *Journal of Computer and System Sciences* 55(1), 24–35 (1997).

Primary report: https://eccc.weizmann.ac.il/report/1994/010/

STOC DOI: https://doi.org/10.1145/195058.195134

JCSS DOI: https://doi.org/10.1006/jcss.1997.1494

Primary facts used in `map/BARRIERS.md`:

- natural lower-bound properties combine constructivity and largeness and must be useful against the target circuit class;
- the strong limitation on superpolynomial lower bounds for general circuits is conditional on a cryptographic hardness / pseudorandomness assumption;
- the paper separately proves unconditional limitations in narrower settings and analyzes weaker `AC^0`-natural proofs.

Research rule: audit constructivity in the full truth-table length `N = 2^n`, give a quantitative largeness bound, prove usefulness, and state the cryptographic assumption. Do not use “natural” colloquially.

### Aaronson, Wigderson — Algebrization: A New Barrier in Complexity Theory

Scott Aaronson, Avi Wigderson. **“Algebrization: A New Barrier in Complexity Theory.”** ECCC TR08-005 (2008); *ACM Transactions on Computation Theory* 1(1), Article 2 (2009).

Primary report: https://eccc.weizmann.ac.il/report/2008/005/

DOI: https://doi.org/10.1145/1490270.1490272

Primary facts used in `map/BARRIERS.md`:

- Definition 2.1 distinguishes unrestricted oracle access from polynomial-length oracle queries where needed;
- Definition 2.2 defines finite-field polynomial extension oracles agreeing with the Boolean oracle and having uniformly bounded multidegree;
- Definition 2.3 gives asymmetric notions of algebrizing inclusions and separations;
- Theorem 3.7 gives the algebrized interactive-proof containment `PSPACE^{A[poly]} subseteq IP^{A_tilde}`;
- the oracle/extension constructions in Section 5 show that resolving P versus NP requires non-algebrizing techniques in this framework.

Research rule: “uses algebra” and “non-relativizing” are not substitutes for the formal Definition 2.3 audit.

## Polynomial-method context for Expedition 001

### Smolensky — Algebraic methods in the theory of lower bounds for Boolean circuit complexity

Roman Smolensky. **“Algebraic methods in the theory of lower bounds for Boolean circuit complexity.”** Proceedings of the 19th Annual ACM Symposium on Theory of Computing (STOC 1987), 77–82.

DOI: https://doi.org/10.1145/28395.28404

Use for theorem-level Razborov–Smolensky claims, not an AI project's labels. The paper's approximation machinery carries explicit field, circuit, degree, and error conditions; a finite sequence named “approximate polynomial degree” does not by itself instantiate the lower-bound theorem.

## Restricted lower bounds / positive landmarks

### Håstad — switching-lemma / AC0 lower-bound work

Relevant for understanding what successful restricted circuit lower bounds look like.

Before relying on an exact formulation, retrieve the primary paper and record the precise random-restriction distribution, width/depth hypotheses, and quantitative bound.

### Razborov — monotone circuit lower bounds

Relevant restricted-model success.

Before relying on an exact formulation, retrieve the primary paper and separate monotone-circuit assumptions from unrestricted circuit claims.

### Smolensky — algebraic lower bounds for bounded-depth circuits

See the primary STOC 1987 entry above. Relevant for `AC^0[p]` / polynomial-method discussions.

### Ryan Williams — NEXP vs ACC0

A major modern lower-bound landmark connecting algorithms and circuit lower bounds.

Before relying on any exact formulation, fetch and cite the primary paper.

## Formal mathematics and AI

### AlphaProof

Nature:

https://www.nature.com/articles/s41586-025-09833-y

DeepMind overview:

https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/

### LeanDojo

https://arxiv.org/abs/2306.15626

### Gemini Deep Think / Aletheia

https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/

## AI-generated mathematical research

### OpenAI — Sharing AI progress in mathematics

https://openai.com/index/sharing-ai-progress-in-mathematics/

Important methodological details:

- broad portfolio of open research problems
- public manuscripts
- Lean formalization for many results
- reasoning summaries for selected results
- compute disclosure
- revision/citation protocol

### OpenAI — Unit-distance conjecture result

https://openai.com/index/model-disproves-discrete-geometry-conjecture/

Important methodological lesson:

Counterexample discovery can decisively resolve a conjectural direction without producing a giant proof.

### OpenAI — Navier–Stokes research announcement

OpenAI research listing:

https://openai.com/research/index/publication/

Treat any Millennium-level result as requiring independent expert verification beyond model-generated or formal artifacts.

### OpenAI — Advisory Group on Mathematics and AI

https://openai.com/index/advisory-group-on-mathematics-and-ai/

Relevant to publication ethics, disclosure, verification burden, and responsible release of machine-generated mathematics.

## Meta-rule

No citation should be included merely because an AI remembered it.

For theorem-level work:

1. retrieve the source
2. read the relevant statement
3. record the exact assumptions
4. distinguish the paper's theorem from our paraphrase
5. cite stable source information
