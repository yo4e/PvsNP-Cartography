# Expedition030: close the actual shared-DAG approximation bridge

Research lead: 月野テンプレクス. Fresh approval in the current conversation; executed 2026-10-31 JST. No earlier approval is reused. Starting checkpoint81619bb9ed6f216e7eeb9fba27784b07d6821218. Read live AGENTS, open Issues8/15/22, current status and assumptions, recent commits and the Expedition029 handoff/log. Mandatory README/protocol/barriers/prior-art/bibliography and direction are available in the current conversation; their live blob hashes were checked against those full texts before reuse. Old dated checkpoints are not instructions to restart completed issues.

## Mathematical choice

Issue22's first three gate tasks are complete. The earliest unblocked target is the missing actual shared-DAG theorem, not another gate check or numeric threshold. Construct a finite topological program with input and constant wires, NOT/XOR/AND/OR, finite fan-in, repeated references and sharing. Preserve actual GF2 MvPolynomial totalDegree and a fixed-before-input distribution. Count each original AND/OR node once, and use the documented recursive nonlinear depth (empty maximum zero, plus one at AND/OR). For r>=1 derive degree<=r^h and pointwise error<=S/2^r, then the original error1/3 predicate and the accepted MOD3 consequence.

A concrete representation may use a list-like inductive program with references to its already-built wire table, not an expression tree with one recursively copied child per edge. A common finite slot capacity K represents every finite fan-in by neutral padding, indexed by argument POSITION. One r-by-K matrix is sampled before every input and reused at every gate. Local bad events are evaluated on deterministic TRUE wire values; induction and a union bound need no independence across gates.

## Roles and attacks

Explorer/Formalist: implement the closed construction and proofs. Skeptic: attack padding, empty arities, skip wires, unused nodes, source-wire coefficient tying, adaptive input, output polarity, recursive depth and quantifier order. Experimentalist: compare genuine unreduced sparse polynomials with an independently implemented Boolean evaluator on finite circuits. Such same-author checks are not independent semantic review or universal proof. Archivist: preserve implementation failures and mathematical counterexamples in graveyard/; record actual completed execution before any promotion.

Primary context retrieved: Goldreich, ECCC TR23-034 revision1, Section2.2.1, Lemma2/Claim2.1, https://eccc.weizmann.ac.il/report/2023/034/revision/1/download . Parsed text was read; PDF screenshots for pages5/6 failed with cache miss. Do not claim visual inspection. The source averages to a deterministic polynomial; our target retains the randomized pointwise construction. This is known-method reconstruction, novelty-unknown, not a new unrestricted-circuit bound or P-versus-NP result.

## Environment

A fresh local git ls-remote failed DNS resolution for github.com. Local lean/lake are absent. Connected GitHub reads work. Creating this useful orientation is the actual write probe; use connected Actions for pinned formal execution, preserving --wfail and the existing axiom policy. No write success, completed proof, new independent reviewer or second kernel is inferred in advance. Later work still requires fresh approval.
