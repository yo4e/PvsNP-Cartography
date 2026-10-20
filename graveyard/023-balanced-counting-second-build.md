# Second counting candidate: rejected implementation, precise repair

Candidate e96df58e2ee62589bbff4f6d5a809ca11200dc06, run39508191115,
job118922342254. Completed FAILURE, exit1 at2026-10-20T22:30:30Z. Full actual
log inspected. No generic theorem or axiom audit was accepted in that run.

Remaining errors were localized after the first repair:
- Factoring every constant out of every sum changed the full triple sum before
  its identity was rewritten. Stage the distribution/rewrites first, then
  pull the final factor2 outside.
- Unrestricted norm_num turned sums of indicators into filtered cardinalities
  only in the hypothesis, obscuring the matching target. Use a restricted
  simplifier on constant-one factors, then the polynomial identity.
- affineValue contains a cast of an entire natural sum. Move that cast through
  sum/product before applying the bit-indicator identity.
- norm_num left closed GF(2) equalities such as(2:ZMod2)=0. Finish those closed
  equality goals by ordinary kernel-checked decide, not a new axiom.
- A redundant sequence-focus warning is fatal under --wfail; remove the
  redundant syntax rather than disabling the linter.

The third source repair keeps target, degree, REAL mass, normalization and
pointwise quantifiers unchanged. The bound remains a candidate until a real
completed root build and both namespace/target audits are inspected. The
independent finite checker already passed separately; it cannot certify this
formal repair. Subsequent dependent candidates may fail transitively on the
same prefix, which must not be counted as fresh mathematical refutations.
