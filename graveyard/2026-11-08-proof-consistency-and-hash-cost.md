# 2026-11-08 — invalid proof interfaces and an actual validation-cost defect

Research lead: 月野テンプレクス. Specific refutations and repairs; no novelty claim. The original source's globally fixed-proof route survives these attacks.

## 1. Re-sampling each occurrence is not a single proof

Take one proof coordinate v and two equiprobable tests: v OR v OR v, and not-v OR not-v OR not-v. Every fixed proof, and every mixture of fixed proofs, accepts exactly1/2. Independently sampling a fair bit at each occurrence instead accepts7/8. Choosing a new proof after seeing the test accepts1. Thus a soundness hypothesis quantified over global proof functions does not cover either changed interface.

The attraction is to reuse a pointwise randomized predictor separately at every query. The failure is the coupling/quantifier change. Repair: average once over a family of global polynomials, select one polynomial, then use that fixed polynomial at all tests. `verify_transfer.py` retains the exact rational control. It is not a counterexample to Viola's fixed-proof argument.

## 2. Uniform-average agreement does not control concentrated queries

Let pi be constant1 on the two-bit address cube and p=x+y+xy. Agreement is3/4, but a verifier querying only00 always receives the wrong bit. Repair: retain pointwise approximation or explicitly prove a separate query-distribution/smoothness bound. Never infer the former from a uniform truth-table average.

## 3. Existence and guessing are not deterministic enumeration

At r=8,D=2, canonical coefficient description length is37 bits, but there are2^37=137438953472 descriptions. The nondeterministic branch guesses37 bits and checks them; enumerating every candidate is a different cost. This example does not prove an impossibility of efficient construction. It refutes charging enumeration as though it were merely one description.

## 4. A saving in the exponent may still lose to polynomial overhead

For a synthetic overhead n^12 and amplified degree lambda*n/log2 n, a1/200 counting constant with degree tripling leaves the power12-1/(600lambda). At lambda=1/6000 it is+2, not a speedup; at1/12000 it is-8. These are exact toy-budget calculations, NOT measured PCP constants. Repair: choose the small degree constant after all fixed construction, query, arithmetic and model-simulation overheads, as in source-bridge.md.

## 5. Actual repository defect: hash duplicate validation in the tail=0 branch

The old runtime_audit.py used len(set(masks)). Distinct masks j*sys.hash_info.modulus share the same ordinary-int hash. Instrumented1024-item validation makes646343 equality calls, whereas deterministic sorting needs9974 ordering comparisons and1023 adjacent checks in the recorded run. The generic t*M charge could cover t^2, but the tighter large-degree tail=0 argument could not.

Repair9afb67d1d1061558cea1a7a7d085236a59504087 introduces canonical_source with sorting and adjacent comparison. Its semantics and all earlier numerical outcomes are unchanged; completed exact CI reproduces them. The original cost document is archived, and the corrected entry point links the explicit erratum. No Lean theorem or count identity was weakened.

## Disposition

Reject the altered proof interfaces and uncharged hash assumption. Retain the known conditional PCP/counting route, with one fixed proof, explicit SAT-prefix oracle queries only in the E^NP language definition, and an oracle-free final tester. Mathematical identities, finite controls, source imports, implementation costs and independent review remain distinct evidence classes.
