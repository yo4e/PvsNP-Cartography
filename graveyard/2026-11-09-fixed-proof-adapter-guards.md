# Fixed-proof adapter: failed scripts and necessary guards

2026-11-09 JST. Research lead: 月野テンプレクス. Same-author adversarial analysis; no novelty or independent review is claimed. These attacks refute altered interfaces, not the original fixed-proof OR argument.

## 1. Signed or unnormalized mixtures do not select a good positive row

On two addresses let the target be constant1, and let the three rows be (1,0), (0,1), (0,0), with weights1,1,-1. Total mass is1 and the signed success score at each address is1, yet each positive-mass row accepts only half of the equally weighted single-address tests (written as tripled literals). Thus dropping nonnegativity breaks the conclusion at epsilon0. Dropping the negative row instead gives total mass2 and still breaks it, showing why normalization cannot be omitted either. These rows are actual affine GF2 functions of one address bit.

Repair: retain nonnegative normalized REAL weights and require a positive-mass witness. Rational finite tests do not replace the arbitrary-real formal argument.

## 2. Sharp epsilon is specific to a satisfied OR clause

Take the constant-one target on two-bit addresses. Use three equiprobable degree<=2 polynomials, each wrong at one of00,01,10 and correct elsewhere. Every address has error<=1/3. An AND of the three queried bits fails for EVERY sample. Hence the sharp epsilon transfer cannot simply be relabeled a generic predicate lemma. A satisfied OR retains a true literal chosen before sampling; that is the actual implication.

## 3. Empty tests and zero denominators invalidate cross multiplication

With zero tests, the integer condition u*0<=v*0 always passes, while the totalized real acceptance is0 and can fail a positive threshold. With denominator0, totalized real division and cross multiplication are again inequivalent. The count identity itself permits an empty clause index type, but threshold equivalence requires nonempty tests and v>0. Zero variables do not mean zero assignments: the empty Boolean cube has one assignment.

## 4. Known coupling control retained

Tests(v,v,v) and(not-v,not-v,not-v) yield1/2 acceptance for every global proof or mixture of global proofs. Independent per-occurrence resampling yields7/8. This was already known in Expedition034 and is not reported as a new discovery. The same polynomial must be used for every query occurrence and test.

## 5. First formal candidate did not pass

Candidate40fc948826b1e64a6ab6c0391d4896d462455965, tree24b2c2304dffb0b6c22ce3431aa1e47913263369, failed completed run42569238374/job129002523550. Full decoded log was retrieved. FixedProofTransfer built, but SignedProjection failed: broad simplification obscured a constant-polynomial degree; equality orientation prevented the product-zero rewrite; and an implicit summand could not be inferred. A subsequent unused-simp warning also failed the unchanged strict policy. Target reports and namespace audit were skipped, so no new formal milestone was accepted from this run.

Repair candidateba3c08f4bea21495266ed6cddba48ada5b2e12f9 makes constant degree, product-zero reasoning and the summand proof explicit without changing any theorem statement, axiom or warning rule. Its execution status must be checked separately; this failure record does not declare it successful.

## Finite controls

Expedition035/verify_adapter.py preserves the countermodels and bounded exact checks. The checked ordinary exponent-vector polynomials retain unreduced degrees; a separate integer-residue amplifier/fold/transform path is compared with direct original-proof queries. The script uses explicit exceptions under both normal and optimized execution. Finite outcomes, formal acceptance, mathematical novelty and independent review remain separate.
