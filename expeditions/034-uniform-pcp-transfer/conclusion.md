# Conclusion — source bridge reconstructed, false interfaces rejected

2026-11-08 JST. Research lead: 月野テンプレクス. Bounded milestone for Issue26: a source-faithful **written conditional** map from exact GF2 counting to the known E^NP infinitely-often degree lower-bound route, with separately imported PCP and hierarchy theorems. No new lower bound or formal verification is claimed.

The argument now distinguishes two machines: an E^NP canonical proof-bit language defined through explicitly expanded SAT-prefix queries, and an oracle-free nondeterministic tester which guesses ONE polynomial. Its total input length is2n+O(log n), its amplified degree budget is integer-computable, and its coefficient description, projection expansion, signed-clause construction, exact count comparison and polynomial overhead are charged before choosing the small constant. The final clock contradicts the specifically named hierarchy bound only under those imported hypotheses.

Attack found an actual implementation-accounting defect: hash-based duplicate validation did not fit the tail=0 worst-case shortcut. Deterministic sorted validation repairs it without changing any counts. The previous complete cost document is archived and its entry point now exposes the correction.

The global-proof acceptance1/2 versus per-occurrence resampling7/8 countermodel kills an invalid interface, not the paper. Further controls reject average-only agreement for concentrated queries, description-length/enumeration confusion and insufficient savings after overhead. All are preserved in graveyard/2026-11-08-proof-consistency-and-hash-cost.md.

Code9afb67d1d1061558cea1a7a7d085236a59504087 passed completed run42437159862/job128598359545. Actual source/commit/results and full decoded output were re-fetched. New tests cover223522 projection-value comparisons and9120 composed-clause exact counts; both older suites also reproduce. Normal/-O/stored output hashes agree. Finite execution is not a general proof or independent review.

Next is Issue27: formalize the sharply bounded single-proof real-mixture/signed-projection/count adapter, reusing the existing exact-count endpoint. Full PCP construction, hierarchy, Python runtime refinement and independent semantic review remain separate gaps. No local Lean toolchain was available, but no persistence or security blocker remains. Further sessions require fresh approval.
