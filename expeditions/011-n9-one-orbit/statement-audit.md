# Statement-fidelity and exact certificate audit: n=9 MOD3

2026-10-16 JST. Self-audit; independent expert statement review is pending.

## Exact quantifiers and field

f:{0,1}^9 -> GF(2) is 1 exactly when Hamming weight is divisible by three (including zero). The original `HasProbabilisticDegreeAtMost f (1/3) d` requires one fixed finite family of actual MvPolynomial objects of degree <=d, nonnegative **REAL** probabilities summing to one, and correctness >=2/3 for **EVERY** input. It does not let the polynomial depend on the input. Field arithmetic is mod2; probability arithmetic is real.

The final Lean module is `formal/PvsNPCartography/Mod3NineDegree.lean`. It proves `degree_two_feasible`, `degree_one_impossible`, `feasible_degree_iff`, `least_feasible_degree`, `pdeg_eq_two`, plus an explicit unsymmetrized-counterexample theorem. The general permutation and layer lemmas are reused from the previous pinned verified module; no new symmetry assumption is supplied by the caller.

## Upper witness: one seed, full orbit

Lexicographic pair order i<j for nine variables. Polynomial encoding (c,a,b) = **(1,127,36505001791)**. For a fixed unsymmetrized variable labeling A={0,1,5,6}, B={2,3,4}, C={7,8}, the polynomial is

`1 + sum(A) + sum(B) + choose(sum(A),2) + sum(A)*sum(B) + sum(B)*sum(C) + choose(sum(C),2) (mod 2)`,

where `sum` means the integer number of ones in that block and the binomial terms are reduced mod2. This is an ANF with 7 linear and 25 degree-two monomials. Group permutations within A,B,C leave it unchanged.

For Hamming weights 0..9, layer sizes are [1,9,36,84,126,126,84,36,9,1] and the numbers of inputs on which this seed agrees are **[1,7,27,59,85,85,59,27,7,1]**. Full permutation averaging therefore gives success

`[1,7/9,3/4,59/84,85/126,85/126,59/84,3/4,7/9,1]`.

Minimum **85/126 > 2/3**, with exact gap **1/126**. The formal upper theorem needs only >=2/3, and discharges its ten integer layer premises with `decide +kernel`. Uniform group sampling from 9!=362880 permutations gives the family independently of x. Each distinct polynomial appears exactly 4!*3!*2!=288 times; the distinct support is thus 1260 equally weighted polynomials indexed by labelled (4,3,2) partitions. The separate Python checker reconstructs all 1260 and verifies every one of 512 inputs, without taking the layer conclusion on trust.

## Lower certificate

Define integer input mass 28 at every input of weight1, 3 at every input of weight3, and zero elsewhere. Mass is 28*9+3*84=**504**. Every one of the 1024 binary affine polynomials c+a.x has weighted correctness <=**322**. The maximum is **322/504=23/36 < 2/3**, strict gap **1/36**. This can also be verified by the exact hypergeometric formula

`s(k)= (9-k)/18 + (choose(k,1)*choose(9-k,2)+choose(k,3))/168`

for zero constant and coefficient weight k, with invalid binomials interpreted as zero; constant1 complements the probability. The Lean proof covers all affine rows by permutation transport and 20 canonical kernel computations, then arbitrary finite real mixtures through the existing structural normal-form and finite-dual theorem.

## What is deliberately NOT asserted

The unsymmetrized one-seed family fails at input bit7=1, all other bits0; its success is exactly zero. It is invalid to call that singleton family pointwise-valid. The block scan tried exactly 7432 coefficient masks for one-orbit quadratic families invariant within <=3 nonempty blocks, and found only the (4,3,2) mask727 feasible; the 7431 failures are **not** a universal obstruction to other degree-two families or mixtures. Support minimality, best error, novelty and n>=10 remain unresolved.

The stronger strict upper guarantee 85/126 is checked by exact finite Python arithmetic, not separately claimed as a closed Lean theorem at epsilon=41/126. The closed Lean error parameter here is epsilon=1/3. No independent human mathematical review or second proof kernel was run.
