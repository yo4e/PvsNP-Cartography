# Conclusion: exact finite n=9 MOD3 degree equality verified in Lean

Date: 2026-10-16 JST. Research lead: 月野テンプレクス. Status: **formally-verified under listed Lean assumptions**. Numerical n=9 result is new to this repository; prior-art novelty UNKNOWN. Independent human semantic review pending.

## Result

The standard finite-support, real-probability, pointwise probabilistic degree of MOD3 on the nine-variable Boolean cube over GF(2), at error 1/3, is **exactly 2**. The n=9 closed theorems give feasibility iff 2<=d, IsLeast and the actual numerical `pdeg_eq_two`, with existence proved, not assumed. The complete Lean coverage is now n=5..9. This finite result does NOT extend to all n or P vs NP.

Upper: one quadratic seed (1,127,36505001791) uniformly permuted. Success on each weight layer is [1,7/9,3/4,59/84,85/126,85/126,59/84,3/4,7/9,1]. The **minimum is 85/126**, a strict 1/126 margin above 2/3. All 362880 permutations describe one real distribution; there are only 1260 distinct polynomial coefficient rows because of 288 within-block automorphisms.

Lower: integer input mass28 on weight1 and3 on weight3, total504. The universal affine maximum is322/504=**23/36**, strictly less than2/3. The Lean proof reduces ALL 1024 affine rows to20 canonical cases through a proved permutation identity and rules out any normalized finite real mixture of degree-one polynomials.

## Actual formal verification

Final audited source commit **807124110f0fc1861504f9ea0bd6fd971a78992e** (the preceding code candidate was 480fa2df). Actual successful [GitHub Actions formal run 38908696378](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38908696378), job 116998734457. Pinned Lean4.35.0-rc4 and Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8; `lake build --wfail` completed successfully (9041 jobs). Axiom audit covered **356 declarations** with only [propext, Classical.choice, Quot.sound]. All **14 printed n=9 targets**, including the final closed equality, depend only on those three. An attributed excerpt is in ../../formal/reports/2026-10-16-n9-axioms.txt.

The first formal commit 480fa2df8940adf6451d1a68ce7f44e26ea24332 compiled the new n=9 source, but the explicit axiom script failed because the new import was below declarations. The repaired commit moved the import to the start of the audit file, WITHOUT modifying the n=9 theorem statements, proof source or warning/axiom policy. Source blob of n=9 module: 32428657909833b00103c85f3656708a08c64678. Do not label the first failed full run verified.

## Independent-algorithm finite checks and attacks

[Test/certificate commit a529afed](https://github.com/yo4e/PvsNP-Cartography/commit/a529afedcca686757618b68ba6a328d5a229b654) passed the actual [semantic run 38909099839](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38909099839), job117000104346, under both Python3.13 normal and -O execution. The checker compares independent mask/expanded polynomial evaluation and Mobius ANF, all512 input truth values, full literal362880-permutation orbit over10 canonical inputs (3,628,800 orbit/input checks), and all1260 distinct partition polynomials at all512 inputs (645,120 checks). Dual results agree between exhaustive1024-affine enumeration, Walsh-Hadamard transform and exact hypergeometric formula. Seven corrupted source/model assertions were rejected in the CI checker.

The constrained block search exhausts **7432** binary coefficient patterns invariant within <=3 nonempty coordinate blocks, with one uniform orbit per pattern. Exactly one (the (4,3,2), mask727 construction) meets 2/3. This does not establish minimal support over all polynomial families. See graveyard/011 and statement-audit.md.

The raw unsymmetrized seed fails at a concrete input (formally checked), and naively ignoring one coordinate of the n=8 witness fails at n=9 all-one input. See graveyard/010. These attacks avoid upgrading mean-case bounds to pointwise claims and prevent unproved generalizations.

## Frontier / limits

No GitHub write blocker or unapplied patch from this session remains. The audited code and separate executable audit have successful completed actions and were re-fetched. Same-author independent algorithms and a CI runner are not independent expert review. No second proof kernel was used; novelty and global support optimality are unknown.

Next: test n=10 with fresh certificate / possible universal obstruction, and separately seek independent human review of the now n=5..9 formal chain. The single-orbit <=3-block search at n=10 is only a restricted exploration and cannot establish degree-three necessity. No asymptotic circuit lower bound, proof-barrier escape or P-vs-NP conclusion follows.
