# First Bounded Research Target Selection

Status: **selected after comparative audit**

Date: 2026-10-08

Issue: #5

This memo compares four bounded targets that remain materially connected to circuit lower bounds or proof complexity without pretending to attack the full P vs NP question directly.

Selection rule:

- standard quantity with a theorem-level definition;
- falsifiable on finite instances;
- exact certificates are possible;
- useful even if the hoped-for pattern dies;
- limited overlap with Expedition 001;
- no novelty claim until literature and independent verification support one.

## Executive choice

**Select Candidate A: an exact finite probabilistic-degree atlas for modular Boolean functions, starting with `MOD_3` over `GF(2)` at error `1/3`.**

The first expedition should not ask for an asymptotic breakthrough.

It should ask:

> For small n, what is the exact pointwise-error probabilistic degree of `MOD_3^n` over `GF(2)`, and can every upper/lower value be accompanied by a machine-checkable rational certificate?

A pilot computation performed during target selection already produced exact certificate candidates showing

`pdeg_{1/3}^{GF(2)}(MOD_3^5) = 2`

and

`pdeg_{1/3}^{GF(2)}(MOD_3^6) = 2`.

These are **pilot finite results, not novelty claims**. They exist here to demonstrate tractability and to seed Expedition 002.

---

## Candidate A — Exact finite probabilistic degree of modular functions

### Exact target

For a Boolean function `f : {0,1}^n -> {0,1}`, field `F`, and `epsilon < 1/2`, define the probabilistic degree as the least `d` for which there is a distribution over degree-at-most-`d` polynomials `P` over `F` satisfying, for **every** Boolean input `x`,

`Pr_P[P(x) = f(x)] >= 1 - epsilon`.

Start with:

- `F = GF(2)`
- `f = MOD_3^n`
- `epsilon = 1/3`
- exact finite n, initially `n <= 6`, then push until exact certification becomes expensive.

This is deliberately different from the deterministic average-misclassification proxy attacked in Expedition 001.

### Why it matters

Probabilistic polynomials were introduced into circuit lower-bound work by Razborov and are central to the Razborov–Smolensky tradition. Modern work continues to use probabilistic degree as a standard Boolean-function complexity measure.

Primary/current context:

- Srinivasan, Tripathi, Venkitesh, *On the Probabilistic Degrees of Symmetric Boolean Functions*, ECCC TR19-138 / SIAM J. Discrete Math.
  https://eccc.weizmann.ac.il/report/2019/138/
- Srinivasan, *A Robust Version of Hegedűs's Lemma, with Applications*, ECCC TR20-046.
  https://eccc.weizmann.ac.il/report/2020/046/
- Srinivasan, Venkitesh, *On the Probabilistic Degree of an n-variate Boolean Function*, APPROX/RANDOM 2021.
  https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.42

### Known best result / context

The 2019–2021 line characterizes probabilistic degree of broad classes of symmetric Boolean functions up to polylogarithmic factors over fixed characteristic and develops tight lower bounds in positive characteristic.

That is asymptotic theory. This target asks instead for **exact finite values plus exact certificates**.

No exact `MOD_3^5` / `MOD_3^6` table was located in the initial search. That absence is not evidence of novelty.

### Finite experiment

Because the target is symmetric, any candidate distribution over polynomials can be symmetrized under variable permutations.

For a fixed degree, each polynomial can therefore be summarized by its success fraction on each Hamming-weight layer. The existence of a probabilistic polynomial becomes a finite linear program.

The dual is a finite zero-sum game:

- prover chooses a low-degree polynomial;
- adversary chooses a distribution over Hamming-weight layers;
- payoff is correctness probability.

This gives a natural route to exact rational upper witnesses and exact rational dual lower certificates.

### Pilot falsifiability check

The pilot did not merely return a floating-point optimum.

For `n=5`:

- every affine polynomial has expected success at most `11/18 < 2/3` against the exact layer distribution
  `(0, 1/3, 1/6, 7/18, 1/18, 1/18)`;
- an explicit rational mixture of symmetrized quadratic polynomials succeeds with probability exactly `2/3` on every weight layer.

For `n=6`:

- an exact layer distribution
  `(0, 11/36, 0, 7/18, 2/9, 1/12, 0)`
  again bounds every affine polynomial by `11/18`;
- an explicit four-orbit rational quadratic mixture succeeds with probability exactly `4/5` on every weight layer.

Thus degree 1 is impossible and degree 2 is possible in both cases.

The full representatives and exact verification belong in Expedition 002 rather than this selection memo.

### Formalization feasibility

**High.**

The final certificate can avoid trusting an LP solver:

- define Boolean cube and Hamming layers;
- evaluate a finite list of explicit polynomials;
- prove layerwise success counts;
- prove the affine lower certificate by finite binomial identities / enumeration;
- use rational arithmetic.

The solver discovers certificates; Lean or an independent exact checker verifies them.

### Barrier relevance

This is a restricted finite study connected to a known circuit-lower-bound method.

It is **not** a claimed escape from relativization, Natural Proofs, or algebrization, and no finite table will be promoted to a general circuit lower bound without an explicit transfer theorem.

### Novelty risk

**Medium.**

The quantity and asymptotic theory are well established. Exact small-n values may be folklore, mechanically derivable, or simply unpublished because they are small.

That is acceptable: the first genuinely new expedition should optimize for epistemic quality, not prestige.

### Estimated effort

**Low to medium** for n≤6 exact certificates; rising sharply for higher degree/n without symmetry/orbit reductions.

### Kill criteria

Archive or redirect if:

- the exact finite sequence is already tabulated/proved in the literature;
- values become immediate corollaries of a known exact theorem;
- the solver cannot produce independently checkable certificates beyond toy cases;
- no structural pattern survives adversarial checks;
- the work degenerates into numerical LP output without mathematical interpretation.

---

## Candidate B — Exact extremizers for Håstad-style switching probabilities

### Exact target

For small `n,w,t` and a fixed random-restriction distribution, enumerate width-`w` DNFs up to symmetry and determine which maximize

`Pr_rho[DTdepth(f|rho) >= t]`.

### Why it matters

The switching lemma is a core positive landmark behind `AC^0` lower bounds.

A finite extremal atlas could test intuitions about what makes a DNF resistant to random restriction.

### Known best result / context

Håstad's switching lemma gives exponentially decaying upper bounds such as `(C p w)^t` in standard formulations.

Tightness is already a serious literature topic. For example, Mehta's *Tree Tribes and Lower Bounds for Switching Lemmas* constructs functions giving matching lower behavior up to constants in a related framework:

https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2018.70

### Finite experiments

Possible but representation-heavy:

- canonicalize DNFs under variable/literal/clause symmetries;
- enumerate restrictions exactly;
- compute minimum decision-tree depth of the restricted function;
- compare extremizers with Tribes / tree-tribes structures.

### Formalization feasibility

**Medium.**

Finite probability and decision-tree depth are formalizable, but canonicalization and exhaustive formula enumeration add substantial machinery before any mathematical payoff.

### Barrier relevance

A positive restricted-model landmark, not a direct P-vs-NP route.

### Novelty risk

**High.**

Known tightness constructions make it easy to rediscover a finite shadow of existing work and mistake it for a new structural observation.

### Estimated effort

**Medium to high.**

### Kill criteria

Kill if small extremizers immediately collapse to known Tribes/tree-tribes constructions or if formula-representation choices dominate the result.

---

## Candidate C — Exact minimum Resolution width for bounded hard CNFs

### Exact target

Choose a tightly specified family such as small graph pigeonhole or Tseitin formulas and compute exact minimum Resolution refutation width for bounded instances.

### Why it matters

Resolution is a canonical proof system. Ben-Sasson–Wigderson connect refutation width to size, so exact width is a meaningful proof-complexity resource.

Primary source:

Eli Ben-Sasson, Avi Wigderson, *Short Proofs are Narrow — Resolution Made Simple*, ECCC TR99-022.
https://eccc.weizmann.ac.il/report/1999/022/

### Known best result / context

The width method already yields many exponential Resolution lower bounds.

The decision problem “does a CNF have a width-k refutation?” is itself computationally difficult when k is part of the input; work by Hertel–Urquhart and Berkholz establishes EXPTIME-completeness / strong parameterized lower bounds.

### Finite experiments

Very accessible via width-bounded closure / dynamic programming.

Potential outputs:

- exact width tables;
- minimal obstruction clauses;
- graph-structure correlations.

### Formalization feasibility

**Medium.**

Resolution syntax and a finite derivation checker are straightforward compared with probabilistic-polynomial theory.

### Barrier relevance

Closer to proof complexity and hence to the NP/coNP side of the landscape, but still a restricted proof system.

### Novelty risk

**High.**

Small exact Resolution instances have been studied for decades, and solver engineering can easily swamp the mathematical question.

### Estimated effort

**Medium.**

### Kill criteria

Kill if the chosen family's exact width follows directly from known expansion theorems or the finite table reproduces standard benchmark data without a new structural question.

---

## Candidate D — Exact Polynomial Calculus degree across fields for counting contradictions

### Exact target

Compute minimum Polynomial Calculus degree for a carefully bounded counting family while varying the field characteristic.

Candidates include PHP variants or mod-q Tseitin formulas.

### Why it matters

Polynomial Calculus is an algebraic proof system with direct field dependence, and degree lower bounds imply proof-size lower bounds in important settings.

### Known best result / context

For the ordinary pigeonhole principle, classical work gives a degree lower bound `ceil(n/2)+1` over arbitrary fields, with matching upper bounds in sufficiently large characteristic:

Impagliazzo, Pudlák, Sgall, *Lower Bounds for the Polynomial Calculus and the Gröbner Basis Algorithm*, ECCC TR97-042.
https://eccc.weizmann.ac.il/report/1997/042/

Modern expander-based work gives strong PC/PCR degree lower bounds for FPHP and Tseitin-style formulas.

The nearby parity-proof landscape is also moving quickly. In September 2026, Kamil Braun reported a DAG-like `Res(⊕)` lower bound for bit-PHP with Lean formalization:

https://arxiv.org/abs/2609.23015

### Finite experiments

Possible with degree-bounded polynomial consequence spaces / Gröbner-style linear algebra.

Field variation is exact and potentially informative.

### Formalization feasibility

**Medium to low** for a first expedition.

One must faithfully encode the proof system, Boolean axioms, degree measure, and field arithmetic before a finite certificate is meaningful.

### Barrier relevance

Strongly connected to algebraic proof complexity; still no direct general P-vs-NP implication.

### Novelty risk

**Medium to high.**

There is active and old literature on exactly these field-sensitive counting principles, including very fresh 2026 work nearby.

### Estimated effort

**High.**

### Kill criteria

Kill or postpone if a known theorem already fixes the selected exact values, or if encoding choices produce more uncertainty than the field-sensitivity question resolves.

---

## Comparison matrix

| Candidate | Standard quantity fidelity | Exact certificates | Connection | Novelty risk | Engineering load | Formalization | Verdict |
|---|---|---|---|---|---|---|---|
| A. probabilistic degree | very high | very high | circuit lower bounds | medium | low–medium | high feasibility | **select** |
| B. switching extremizers | high | high | AC0 lower bounds | high | medium–high | medium | defer |
| C. Resolution width | very high | high | proof complexity | high | medium | medium | reserve |
| D. PC degree / fields | very high | high | algebraic proof complexity | medium–high | high | medium–low initially | later expedition |

## Why Candidate A wins

It passes the most important lesson from Expedition 001:

> name the mathematical quantity first, then make the computation prove that quantity.

It also creates a clean three-layer verification stack:

1. numerical LP / search discovers a candidate;
2. exact rational Python verifies the finite certificate independently;
3. Lean can later verify the certificate and definition correspondence.

And if the sequence turns out boring, the expedition still produces a trustworthy exact benchmark for future AI-math systems.

## Selected next expedition

**Expedition 002: Exact finite probabilistic degree of `MOD_3` over `GF(2)`.**

Initial milestone:

- formal definition of pointwise-error probabilistic degree;
- exact table through at least n=6;
- rational upper and lower certificates;
- independent exact checker;
- adversarial definition/encoding audit;
- literature audit with no novelty claim;
- attempt to extend to n=7 or record the computational barrier precisely.
