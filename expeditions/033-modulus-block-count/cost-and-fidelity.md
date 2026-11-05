# Exact counts are not yet a costed implementation

2026-11-05 JST. Research lead: 月野テンプレクス. This is an author-written mathematical/cost audit and known-method reconstruction, not a new lower bound, independent review, or Lean runtime theorem.

Primary context: Emanuele Viola, ECCC TR20-015 revision5, 2021-01-12, Section2.2, Theorem12/Lemmas13-14: https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/ . Relevant PDF images at zero-indexed pages12/13 were successfully inspected this session. The following explicit constants and implementation accounting are our expanded derivation, not a quotation or novelty claim.

## 1. What the accepted statement actually says

At source51a86b10cb0f493b0c093aa81dba734400cb0118, `SubsetZeta.exact_count` takes ANY actual GF2 polynomial P in a+b variables and ANY head subset T. Its conclusion equates the canonical integer remainder of the actual amplified/reduced/folded coefficient transform with `acceptingCount P (bits T)`. No equality-to-the-goal premise, positive head/tail requirement, or supplied coefficient oracle replaces P. The degree bound is a separate theorem about the actual polynomial, not a hypothesis needed for the count identity.

The chain is canonical integer lift -> integer amplifier -> Boolean evaluation-preserving reduction -> actual monomial tail summation -> duplicate-head coefficient aggregation -> subset transform -> strict no-wrap interval. `tail_sum` handles arbitrary nonnegative exponents; the tail factor depends on the NUMBER OF USED VARIABLES, not their exponent sum. The integer lift is not a ring homomorphism, and squarefree reduction is not equality of unreduced formal polynomials.

These source definitions are noncomputable/extensional specifications. The recursive scan is NOT a proved efficient array program. No asymptotic running time follows merely from its correctness theorem.

## 2. Refuting the free-sharing inference

Consider the literal unshared recursive evaluator, giving unit cost even to each original coefficient lookup. For an output subset S, each present processed coordinate branches and each absent one does not. Induction gives exactly 2^|S| coefficient-leaf reads. Computing all outputs independently therefore uses

    sum_{S subset [a]} 2^|S| = (1+2)^a = 3^a

reads. This is a written general counting argument. `runtime_audit.py` corroborates a=0..12; at a=12 it observes531441 leaves. It does NOT execute the Lean compiler or measure its runtime. The formal coefficient definition would itself cost additional work if evaluated literally.

In a shared table, after processing coordinate set I, the entry at S is

    sum_{U subset (S intersect I)} c((S minus I) union U) mod q.

Initially I is empty. Processing a fresh i replaces each entry with i present by itself plus its partner with i absent. Those two disjoint classes of U establish the next invariant. The lower partner is never modified during that stage, so in-place updates are safe. After all coordinates, this is the subset sum. Each coordinate has exactly2^(a-1) pairs: zero additions when a=0, otherwise a*2^(a-1) additions. At a=12 that is24576 modular additions. These are different counted operations, NOT a wall-clock speedup ratio.

Duplicate coordinates violate the invariant: c=[1,0] gives [1,1] after one pass and [1,2] after two. Coefficient folding must also aggregate: for P=x+y and one tail variable, the amplifier modulo4 is x+y+2xy. Correct head counts are [1,1]; overwriting colliding head coefficients instead of adding gives [1,3]. Neither is a counterexample to the accepted theorem, which already has the necessary guards and sums.

The old `verify.py:zeta_checked` deliberately enumerates subsets to verify every stage. It is a TEST ORACLE, not the fast production routine. The new `table_zeta` does not perform that exponential invariant check.

## 3. Construct the coefficient table without hiding its cost

Input convention for this bound: canonical squarefree GF2 ANF, encoded by t distinct n-bit monomial masks, each coefficient1; t<=M(n,d), where

    M(n,k) = sum_{j=0}^{min(n,k)} choose(n,j).

A redundant exponent-list input of length L has an additional explicit normalization/read cost polynomial in its encoding length. It is not legitimate to promise subexponential time independently of an arbitrarily large input encoding. General GF2 polynomial semantics survive Boolean normalization; the integer lift need only preserve parity, not exact integer values.

Choose b tail variables, a=n-b, s=b+1, h=2b+1, q=2^s, D=h*d. Expand the univariate amplifier in polynomial(s) bit work, then use h Horner multiplications. After j multiplications, each stored support has size at most j*d and coefficients are reduced modulo q. Every intermediate support count is at most M(n,D). Multiplication uses bitwise union, sorts product records by their mask, and aggregates equal keys modulo q. It does not assume disjoint supports or a field coefficient ring.

For one multiplication there are at most t*M(n,D) pair records. Across Horner there are at most h*t*M(n,D) records. Sorting costs O(K log(K+1)) comparisons for K records, each mask comparison costs O(n) bits; modular multiplication and reduction cost polynomial(s) bits. Construction, degree/support assertions, and coefficient generation thus fit

    (1 + t*M(n,D))*poly(n,b)

bit work in a word-RAM with polynomial-bit-cost arithmetic. Source duplicate validation can pessimistically cost t^2; this is still absorbed because t<=M(n,D). No favorable Python hash behavior is needed for the exponential bound. Sort-and-aggregate MATERIALIZES K pair records, so its peak space is not merely the number of surviving monomials.

The final polynomial is folded in O(M(n,D)*poly(n,b)) work by multiplying each coefficient by2^(b-tail_support_card), adding into the corresponding head cell modulo q. It does not enumerate2^b tail assignments. Dense allocation costs2^a; shared table transformation costs a*2^(a-1) modular additions. Summing the block counts to a total count costs O(2^a*n) bit work. The resulting bound is

    T <= (1 + t*M(n,D) + 2^(n-b))*poly(n,b).

For a conventional tape model, indexed records and each butterfly stage can instead be implemented by deterministic sorting/merging, with only additional polynomial(n) factors. This is a WRITTEN simulation argument, not a formally verified Python/Turing-machine compiler equivalence.

Every arithmetic operation is in the integer residue ring. s<=n+1, products before reduction have O(s) bits, masks have n bits, and final total counts have at most n+1 bits. The specification's integer no-wrap theorem explains why a residue at each block is its true count, not a merely congruent answer.

## 4. An explicit conservative uniform choice

For 1<=d<=n/100 take b=floor(n/(100d)). Then b>=n/(200d), b<=n/100, a>=99n/100, and D+d=(2b+2)d<=n/25.

For z=1/8, nonnegative binomial coefficients give

    M(n,k) <= (1+z)^n * z^(-k) = (9/8)^n * 8^k.

Since9^4=6561 <8192=2*8^4, (9/8)^4<2. Consequently

    t*M(n,D) <= M(n,d)*M(n,D)
                 <= (9/8)^(2n)*8^(D+d)
                 <= 2^(n/2 + 3n/25) = 2^(31n/50).

Thus construction is dominated by2^a up to polynomial factors, and

    T <= 2^(n-n/(200d))*poly(n).

This is a general inequality derivation, not an extrapolation from finite tests. The exact integer budget controls for100<=n<=400 merely corroborate604 instances. For d>n/100, choose b=0: 2^n differs from2^(n-n/(200d)) by less than a factor sqrt(2), so the same big-O form holds; no meaningful large saving is asserted in that regime. Degree0 and n=0 are constants and are handled separately (all-accepting count2^n or zero). Root counts are2^n minus the accepting count.

This reconstructs a known nontrivial counting exponent with a deliberately weak constant. It is not a new algorithm, optimal constant, practical performance claim, unrestricted circuit lower bound, or P-versus-NP conclusion.

## 5. Attack, tests, and the remaining boundary

Normal Python and python -O runs agree byte-for-byte. The counted implementation checked1747 source/block cases,22719 exact head counts, and26616 exhaustive signed modular tables. Inputs comprise all canonical ANFs at n<=3 plus explicitly seeded samples and constant/linear controls for n4..8; this is NOT exhaustive at n4..8. Same-author alternative implementations and brute force are not independent semantic review.

Construction cannot be omitted even on tiny instances: n=8, P=sum x_i, b=6 produces254 folded terms and17608 product-pair visits, despite only4 output cells and4 final zeta additions. These are operation counts, not timing comparisons. The conservative asymptotic choice would not select that large b for these parameters.

The missing formal refinement is the relation of the sorted-residue Horner/table implementation and its cost model to the accepted extensional integer-polynomial chain. Its Python test evidence and the written bit-cost derivation must not be relabeled as Lean cost theorems. The next mathematical bridge is to inspect what the counting algorithm actually supplies to the hierarchy/oracle lower-bound argument, keeping representation, uniformity, witness search and the E^NP/infinitely-often scope explicit.
