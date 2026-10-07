# Barrier Map

Status: **primary-source audit map**. This document is an operational guide, not a substitute for the cited papers.

A proof barrier is a theorem or oracle construction about a broad method class. It is not evidence that P vs NP is undecidable, hopeless, or likely to have one answer rather than the other. The practical question for a new proof sketch is narrower:

> Which exact step stops the argument from belonging to a method family already known to be insufficient?

For every barrier below, theorem-level statements are separated from this repository's explanatory paraphrase.

## 1. Relativization

### Primary source

Theodore Baker, John Gill, Robert Solovay, **“Relativizations of the P =? NP Question,”** *SIAM Journal on Computing* 4(4), 431–442 (December 1975). DOI: `10.1137/0204037`.

Stable source: https://doi.org/10.1137/0204037

### Technical definition needed for audits

For an oracle language/set `A`, `P^A` and `NP^A` are the languages decided in polynomial time by deterministic and nondeterministic oracle Turing machines, respectively, with access to the same oracle `A`.

A proof argument **relativizes** when the same reasoning continues to establish its claimed class relation after all relevant machines are supplied with an arbitrary common oracle `A`.

This is a property of a proof method, not merely of a theorem statement.

### Primary-source theorem / construction

Baker, Gill, and Solovay construct recursive oracles `A` and `B` such that

- `P^A = NP^A`, while
- `P^B != NP^B`.

They also construct oracle worlds realizing the consistent inclusion relations among relativized `P`, `NP`, and `coNP` considered in the paper.

### Consequence used by this repository

**Explanatory paraphrase:** a method that would prove `P = NP` or `P != NP` by reasoning valid relative to every common oracle cannot settle the unrelativized problem. The two BGS oracle worlds would force that uniformly relativizing argument to give incompatible conclusions.

This consequence is a meta-observation about proof techniques built from the oracle constructions. It is not itself a theorem that classifies every possible proof technique.

### Assumptions / scope

- Both sides receive the same oracle in the standard relativized setup.
- The barrier applies only to reasoning that survives arbitrary oracle substitution.
- The theorem is about relativized complexity classes and recursive oracle sets, not about an oracle believed to model ordinary computation.

### What it does **not** show

BGS does not show:

- `P = NP` or `P != NP` in the ordinary world;
- that every diagonalization argument relativizes;
- that every black-box-looking argument is formally relativizing;
- that a non-relativizing argument is correct;
- that escaping relativization escapes later barriers such as algebrization.

### Technique interaction example

The arithmetization behind `IP = PSPACE` is a canonical example of a major technique that does **not** relativize in the naive BGS sense. Aaronson–Wigderson later show that the interactive-proof argument nevertheless **algebrizes**, which is precisely why “non-relativizing” is not a sufficient stopping criterion.

### Expedition checklist

For a proposed proof route, answer with an explicit lemma or step, not “probably”:

1. Replace every relevant machine/class by its oracle version using the same arbitrary oracle `A`.
2. Which lemmas still go through verbatim?
3. If the claimed final separation/equality still goes through for every `A`, how is that compatible with both BGS oracle worlds?
4. If the proof does **not** relativize, identify the first exact step that fails under oracle substitution.
5. State whether that non-relativizing step may still algebrize.

**Graveyard trigger:** if a complete proposed P-vs-NP proof relativizes and provides no demonstrated flaw in the BGS analysis, archive the route as blocked.

---

## 2. Natural Proofs

### Primary sources

Alexander A. Razborov, Steven Rudich, **“Natural Proofs,”** ECCC TR94-010 (12 December 1994); conference version STOC 1994, DOI `10.1145/195058.195134`; journal version *Journal of Computer and System Sciences* 55(1), 24–35 (1997), DOI `10.1006/jcss.1997.1494`.

Stable sources:

- https://eccc.weizmann.ac.il/report/1994/010/
- https://doi.org/10.1145/195058.195134
- https://doi.org/10.1006/jcss.1997.1494

### Technical definition needed for audits

For each input length `n`, consider a combinatorial property `Gamma_n` of Boolean functions `f : {0,1}^n -> {0,1}`. Since such a function is represented by a truth table of length `N = 2^n`, the relevant efficiency scale is polynomial in `N`, not polynomial in `n`.

Operationally, the Razborov–Rudich framework asks whether the lower-bound property has the following features:

- **Constructive:** membership in `Gamma_n` can be recognized efficiently from the `N`-bit truth table, in the natural-proof setting typically `poly(N) = 2^{O(n)}` time.
- **Large:** `Gamma_n` contains a non-negligible fraction of all `n`-variable Boolean functions, conventionally density at least `1/poly(N) = 2^{-O(n)}` in the standard P-natural formulation.
- **Useful against a circuit class C:** a circuit family in `C` cannot satisfy the property at infinitely many input lengths; equivalently, the property separates the hard functions witnessed by the proof from all sufficiently large members of the target easy class.

Terminology warning: **naturalness is technical.** “Elegant,” “combinatorial,” “explicit,” or “humanly natural” are not substitutes for the constructivity and largeness tests.

### Primary-source theorem / consequence

Razborov and Rudich show, under a cryptographic hardness assumption, that natural proofs cannot establish superpolynomial lower bounds for general Boolean circuits. Their ECCC abstract states this conditional result explicitly and also gives unconditional limitations for particular settings, including the discrete-logarithm application and relationships among weaker `AC^0`-natural methods.

The commonly used P/poly form is:

> Under the existence of sufficiently hard pseudorandom function/generator families of the type assumed by Razborov–Rudich, there is no P-natural property useful against P/poly.

The cryptographic assumption is essential. Do not silently delete it when invoking the barrier.

### Assumptions / scope

- The lower-bound method yields a Boolean-function property satisfying the relevant constructivity and largeness conditions.
- The property is useful against the target circuit class.
- The strong general-circuit impossibility is conditional on the pseudorandomness / cryptographic hardness assumption in the paper.
- Parameterization is by truth-table length `N = 2^n`; confusing `poly(n)` with `poly(N)` changes the definition.

### What it does **not** show

Natural Proofs does not show:

- that strong circuit lower bounds are impossible;
- that the required pseudorandom functions definitely exist;
- that every combinatorial lower-bound argument is natural;
- that a property failing largeness or constructivity is blocked;
- that a method outside the natural-proof framework is correct;
- that “non-natural” in ordinary English has any relevance.

It also does not license the shortcut “this proof mentions algebra/geometry/learning, therefore it is non-natural.” The property induced by the proof must be extracted and tested.

### Technique interaction example

The original paper explicitly analyzes known lower-bound arguments through this lens. In particular, it states that a weaker `AC^0`-natural framework is sufficient for classical parity lower bounds such as the Furst–Saxe–Sipser / Yao / Håstad line, while also proving limitations on what such `AC^0`-natural proofs can obtain. This is an interaction example, not an escape certificate.

### Expedition checklist

If the proof seeks a circuit lower bound by identifying a property of truth tables:

1. Write the property `Gamma_n` explicitly.
2. **Constructivity:** given the full `2^n`-bit truth table, what algorithm decides membership, and what is its running time as a function of `N = 2^n`?
3. **Largeness:** give a quantitative lower bound on `Pr_f[f in Gamma_n]` for uniformly random Boolean `f`.
4. **Usefulness:** prove exactly which circuit families fail the property and from what input length onward.
5. State the target circuit class and lower-bound strength.
6. State the pseudorandomness assumption needed to turn naturalness into a barrier for that class.
7. If one condition fails, identify which one and prove the failure rather than merely naming the approach “non-natural.”

**Graveyard trigger:** if a claimed strong general-circuit lower bound is demonstrably constructive, large, and useful under the relevant cryptographic assumption, record the collision before spending effort polishing the proof.

---

## 3. Algebrization

### Primary source

Scott Aaronson, Avi Wigderson, **“Algebrization: A New Barrier in Complexity Theory,”** ECCC TR08-005 (2008); *ACM Transactions on Computation Theory* 1(1), Article 2 (2009). DOI: `10.1145/1490270.1490272`.

Stable sources:

- https://eccc.weizmann.ac.il/report/2008/005/
- https://doi.org/10.1145/1490270.1490272

### Technical definitions needed for audits

Aaronson–Wigderson distinguish a Boolean oracle `A` from a bounded-multidegree algebraic extension `A_tilde`.

For each Boolean oracle function `A_m : {0,1}^m -> {0,1}` and finite field `F`, an extension is a polynomial

`A_tilde_{m,F} : F^m -> F`

that agrees with `A_m` on the Boolean cube. Their extension oracle is a collection of such polynomials with a uniform constant bound on multidegree. The paper notes that many results would also tolerate linear or polynomial multidegree bounds, but the formal Definition 2.2 uses a constant bound.

The paper's Definition 2.3 is deliberately asymmetric:

- An inclusion `C subseteq D` **algebrizes** if `C^A subseteq D^{A_tilde}` for every Boolean oracle `A` and every allowed extension `A_tilde` of `A`.
- A separation `C not_subseteq D` **algebrizes** if `C^{A_tilde} not_subseteq D^A` for every `A, A_tilde`.

This asymmetry is part of the definition. Replacing it with “both sides get the algebraic oracle” is not the Aaronson–Wigderson barrier.

### Primary-source theorem / construction

Aaronson and Wigderson construct oracle/extension settings showing that resolving central questions including `P` versus `NP` requires **non-algebrizing** techniques in their sense. Their paper also proves that many celebrated arithmetization-based results do algebrize.

For example, their Theorem 3.7 states an algebrized form of the interactive-proof result:

`PSPACE^{A[poly]} subseteq IP^{A_tilde}`

for every oracle `A` and extension `A_tilde` in the paper's framework.

### Consequence used by this repository

**Explanatory paraphrase:** merely adding arithmetization or low-degree polynomial structure is not enough to escape the oracle-method barrier. A candidate P-vs-NP proof must identify a step that does not survive the Aaronson–Wigderson algebraic-oracle framework.

### Assumptions / scope

- The formal framework uses Boolean oracles and low-multidegree extensions over finite fields, with access conventions specified in Definitions 2.1–2.3.
- “Algebrizes” is a theorem-specific method property with asymmetric oracle access, not a synonym for “uses algebra.”
- The paper's barrier statements are oracle constructions about method families, not a claim that all conceivable algebraic reasoning fails.

### What it does **not** show

Algebrization does not show:

- `P = NP` or `P != NP`;
- that algebra is useless in complexity theory;
- that every arithmetization argument algebrizes;
- that every non-relativizing method is algebrizing;
- that escaping algebrization escapes Natural Proofs or ordinary logical errors.

### Technique interaction example

`IP = PSPACE` is the cleanest diagnostic example. It is famously non-relativizing in the ordinary sense, yet Aaronson–Wigderson prove that the arithmetized interactive-proof argument **does algebrize**. This demonstrates the strict methodological lesson:

> non-relativizing does not imply non-algebrizing.

### Expedition checklist

1. Identify every step that replaces Boolean computation by a low-degree polynomial or uses polynomial identity reasoning.
2. Replace the Boolean oracle by an arbitrary allowed extension `A_tilde` and apply the paper's asymmetric access convention for the claimed inclusion/separation.
3. Which lemmas still survive?
4. If the entire claimed P-vs-NP argument survives, compare it against the Aaronson–Wigderson oracle/extension constructions.
5. If it fails to algebrize, isolate the **first exact step** whose reasoning depends on structure not available through the extension oracle.
6. Separately re-run the relativization and Natural Proofs audits. Escaping one barrier is not transitive.

**Graveyard trigger:** a purported P-vs-NP proof whose decisive argument fully algebrizes, with no demonstrated flaw in the Aaronson–Wigderson construction, is blocked in that form.

---

## 4. Barrier interaction matrix

| Observation about a candidate method | What follows | What does **not** follow |
|---|---|---|
| It relativizes | A complete P-vs-NP resolution collides with BGS | The theorem being attempted is false |
| It is non-relativizing | It escapes the BGS filter at some step | It escapes algebrization or Natural Proofs |
| It is constructive + large + useful | Natural-Proofs analysis is mandatory | The barrier applies without its cryptographic assumptions |
| It fails constructivity or largeness | The standard naturalness test may fail | The lower bound is valid |
| It algebrizes | A complete P-vs-NP resolution collides with Aaronson–Wigderson | Algebraic techniques are useless |
| It is non-algebrizing | It passes that one filter | It is novel, correct, or non-natural |

Barriers are filters, not certificates.

## 5. Standard expedition barrier-audit template

Every broad proof route should include `barrier-audit.md` with evidence for each answer:

```text
Relativization
- Exact target class relation:
- Oracle-lifted form:
- First non-relativizing step, if any:
- Evidence / lemma:

Natural Proofs
- Candidate Boolean-function property:
- Constructivity bound in truth-table length N=2^n:
- Largeness bound:
- Usefulness against target class:
- Cryptographic assumption needed:
- First failed naturalness condition, if any:

Algebrization
- Boolean oracle / extension-oracle form:
- First non-algebrizing step, if any:
- Evidence / lemma:

Other restrictions / known lower-bound limits:
Unclear points:
Disposition: pass / collision / unknown
```

`unknown` is an acceptable answer. Ceremonial claims such as “our approach is geometric, therefore it avoids the barriers” are not.

## 6. Positive landmarks to reconstruct next

A barrier map should eventually be paired with successful restricted lower bounds, because the useful question is not only why proofs fail but what makes them work in limited models. Priority landmarks remain:

- `AC^0` lower bounds and switching-lemma methods;
- monotone circuit lower bounds;
- Razborov–Smolensky bounded-depth modular-circuit lower bounds;
- Williams' `NEXP not subseteq ACC^0` algorithms-to-lower-bounds program.

For each, the repository should reconstruct at least one precise theorem with its assumptions and identify which ingredients fail to scale to unrestricted circuits.
