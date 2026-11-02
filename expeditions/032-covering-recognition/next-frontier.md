# Next bounded frontier: modulus amplification and exact block counting

Selected by 月野テンプレクス during the freshly approved2026-11-02 JST session. This records a research target, not authorization for any later session. The uniform-cover route is parked for the reasons in recognition-and-scope.md; no automatic return to root constants or affine counting is intended.

## Question and named use

Reconstruct the first concrete algebraic bridge in a known polynomial-SAT counting algorithm: how can the parity value of a GF2 polynomial be represented modulo a power of two, summed over a block of Boolean inputs, and recovered as an EXACT nonnegative integer count? This supplies a meaningful entry to algorithms-to-lower-bounds research without yet claiming a speedup, a hierarchy theorem or an NP lower bound.

Primary comparison: Viola, ECCC TR20-015 revision5(2021-01-12), Section2.2/Theorem12/Lemmas13-14, https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/ . Text inspected; screenshots failed. Pin this revision. Do not silently import the paper's broader complexity conclusion or substitute NP for E^NP.

## Explicit proposed amplifier and written proof

For integer s>=1 define

 F_s(Y)=sum(j=s..2s-1) choose(2s-1,j) Y^j (1-Y)^(2s-1-j).

This is an INTEGER polynomial of degree<=2s-1. For even Y every summand is divisible by2^s. For odd Y the binomial identity1=(Y+(1-Y))^(2s-1) implies1-F_s(Y) equals the lower half of that sum; each term there contains (1-Y) to an exponent>=s and is divisible by2^s. Therefore F_s(Y) is congruent to Y mod2, viewed as0 or1, modulo2^s for ALL integer Y, including negative values. This is a written derivation, not a Lean-accepted theorem.

## Block-count target

Let p be an actual GF2 polynomial of total degree<=d on n Boolean variables; lift its coefficients to0/1 integers. Split the input into n-ell head bits and ell tail bits, with0<=ell<=n. Form F_(ell+1)(p) over integers modulo2^(ell+1). Its actual degree is at most(2ell+1)d. Boolean squarefree reduction preserves evaluation and does not increase degree; the GF2-specific reduction must not be reused over this ring without checking its assumptions.

Sum over all tail assignments. A squarefree tail monomial using t distinct tail variables contributes exactly2^(ell-t). This folds the polynomial into head variables. Given its squarefree coefficient array, the subset-zeta transform evaluates all head assignments by g(X)=sum(S subset X) coeff(S).

At each head assignment the folded residue equals the number of tail assignments where p=1. That number lies in[0,2^ell], STRICTLY below the modulus2^(ell+1), so its canonical residue is the exact count. We count ONES/accepting assignments, not zeros, unless an explicit complement is applied. Graveyard059 records the failure of using modulus2^ell.

## Acceptance and limits

Prove the integer amplifier, evaluation-preserving lift/composition, actual degree bound, Boolean reduction over the required ring, tail sum, transform invariant and no-wrap reconstruction. Handle zero polynomial, constant1, empty blocks and ell=n. Do not assume a faster polynomial-construction stage: account for expansion, coefficient bit lengths and the relation of degree/block size to a useful runtime before asserting any algorithmic speedup.

Use bounded exact tests to attack the bridge, then a faithful formalization where useful. Any formal promotion requires the pinned strict build, unchanged axiom policy and actual source/commit/completed-output inspection. This is known-method reconstruction; no unrestricted lower bound, proof-barrier escape or P-vs-NP conclusion is implied.

## Same-session continuation, distinct evidence

check_modulus.py and modulus-checks.json pass local Python3.11.8 normal/-O byte comparison and py_compile. There are390 integer amplifier checks,187 polynomial structures,765 polynomial/block cases,9106 pointwise comparisons and3673 exact block counts. Unreduced sparse modular composition is compared with direct Boolean parity and block enumeration; degree is checked before reduction. Wrong-modulus counterexamples cover ell0..6.

These are finite controls by the same author. They are NOT covered by the completed covering CI, NOT a generic Lean theorem and NOT a runtime benchmark or speedup proof. Keep the full counting-algorithm complexity and the algorithms-to-lower-bounds implication as separate, presently unproved research steps.
