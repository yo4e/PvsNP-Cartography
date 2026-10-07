# Lean formalization candidate — Expedition 002

Status: **candidate only; not yet formalized**

## Scope

Formalize the certificate checker, not a general theory of probabilistic degree.

The first Lean target should prove the three finite statements for n=5,6,7 from explicit data.

## Minimal objects

1. Boolean vectors of fixed length.
2. Hamming weight.
3. `MOD_3^n` as a Boolean-valued function.
4. GF(2) degree-at-most-2 polynomials represented by:
   - constant bit;
   - finite set / bitmask of linear variables;
   - finite set / bitmask of unordered quadratic pairs.
5. Evaluation of that representation.
6. Exact rational distributions over:
   - Hamming-weight layers for lower certificates;
   - finite polynomial representatives for upper certificates.
7. Variable permutation action.

## Lemmas

### Lower certificate lemma

For an explicit layer distribution q, if every affine polynomial P satisfies

`E_{x~q}[1(P(x)=MOD_3(x))] < 2/3`,

then no distribution over affine polynomials can achieve pointwise success at least 2/3.

This is a finite convexity/averaging lemma and should be proved generically once.

### Symmetrization lemma

For a fixed representative P and fixed input x of weight w, if a variable permutation is chosen uniformly, then

`Pr_sigma[P(sigma x)=MOD_3(x)]`

equals the fraction of weight-w inputs y on which P(y)=MOD_3(y).

The key combinatorial fact is that every y of the same weight as x has the same number `w!(n-w)!` of preimage permutations.

### Mixture lemma

A rational mixture of symmetrized representatives inherits the corresponding weighted layer-success vector.

If every coordinate is at least 2/3, the mixture is a degree-at-most-2 probabilistic polynomial under the finite definition.

## Concrete theorem targets

Do not use grand names. Suggested targets:

- `mod3_n5_pdeg_one_third_eq_two`
- `mod3_n6_pdeg_one_third_eq_two`
- `mod3_n7_pdeg_one_third_eq_two`

Each theorem should expand to the exact finite definition used in the expedition, not assume an abstract `ProbabilisticDegree` API until that API has itself been audited.

## Assumption audit

Before promotion:

- no `sorry` / `admit`;
- no project-specific axioms;
- inspect `#print axioms`;
- compare the Lean pointwise probability statement to the expedition definition;
- ensure the finite distribution support and weights are explicit;
- ensure the theorem is not weakened to average-case success.

## Why this candidate is compact

The lower side requires at most 256 affine polynomials at n=7.

The upper side uses one orbit representative for n=5, one for n=6, and eight for n=7.

This is small enough that a formal certificate can remain transparent rather than outsourcing correctness to an optimizer.
