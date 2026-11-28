# Research log — November 28 approved night

- Fresh approval verified against the 22:21 JST nightly request. This session
  began at 22:22 JST from clean main `2a546c3781d71cd159b388997bd5312a7ceb78e6`.
  Expedition 048 was the completed afternoon checkpoint; Issue #38 had no
  intervening comments or implementation changes.
- Rechecked AGENTS, current state, required document changes and the active
  source/quantifier frontier. The unchanged mandatory documents were reused
  from their previous full reading. No authorization was inferred for another
  night or for unrelated work.
- Split bounded work into source/degree analysis, a residual-constrained
  family and actual field extension, and adversarial signed-clause controls.
  The branches share one model and exchanged findings.
- Classified a new three-witness residual in the actual two-level oracle.
  The affine-A restriction forces quadratic B and is unsuitable as a growing
  arbitrary Boolean assignment model. Retained the complete classification
  and the masked-root/pointwise-division attacks.
- Reopened BV14 and Carlet. Separated univariate degree, Boolean degree and
  gate degree. Derived affine-selector and canonical-interpolation degree
  statements; retained the source's nonzero selector scale explicitly.
- The lead proposed the chi filtration for division by an affine-linearized
  polynomial. The source branch attacked the carries and ordinary-degree
  conditions. The honest source range yields a bound on B from A and a public
  controlled outer circuit. Independent GF(16)/GF(256) controls were written.
- The live compiler attack preserved exact raw NO soundness yet changed
  auxiliary degree. A bent control showed that failure of sufficient
  approximation budgets need not prevent low-degree clause counting. The
  full AND chain was priced with disjoint parity lower certificates.
- A fixed-node filtered basis led to the actual two-level all-polynomial
  honest-extension bound. Arbitrary recursive bases and Boolean leaf-gate
  arithmetic remain a separate obligation.
- The lead inspected code, proofs, source locations and recorded outputs.
  Local and immutable-source executions and saved hashes are recorded in
  `execution-evidence.md` and its JSON companions. Final commit and Issue
  readbacks are recorded in the top-level session log.

Scientific decision: continue with uniform recursive RS rows and the actual
Boolean failure predicate; park affine-toy enlargement and compiler-invariant
degree claims. No new Lean, CI, novelty or external acceptance was inferred.
