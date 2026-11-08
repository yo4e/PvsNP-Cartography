# Barrier and uniformity audit

2026-11-08 JST, 月野テンプレクス. Scope: reconstruction of a known E^NP infinitely-often probabilistic-degree lower-bound route, not an unrestricted separation.

**Relativization.** The argument explicitly imports a projection-PCP construction and a nondeterministic time-hierarchy theorem. It does not prove that their uses remain valid under arbitrary shared oracles. The NP oracle defines the canonical proof-bit language; the final faster nondeterministic tester is oracle-free. Confusing these two machines would invalidate the contradiction. No general nonrelativization/escape theorem is claimed.

**Natural proofs.** No new constructive, large Boolean-function property useful against P/poly is established here. Earlier affine-cover largeness did not supply usefulness; its easy-circuit counterfamily remains a valid refutation. This counting/PCP reconstruction does not repair that failed direction or remove cryptographic assumptions from the Natural Proofs barrier.

**Algebrization.** The use of GF2 substitutions and integer modulus amplification does not establish escape from algebraic-oracle barriers. No Aaronson–Wigderson oracle-extension experiment or asymmetric-access theorem is proved here.

**Uniformity and length.** The input to F encodes both x and an address y, so its total length is2n+O(log n). Oracle queries are explicit CNFs with polynomial-size witnesses relative to their actual exponential query length. The final algorithm guesses a bounded canonical polynomial description, not an efficient sampler or an advice oracle. One global proof serves every verifier test. All branch costs, construction and integer thresholds are charged.

**Conclusion scope.** The contradiction excludes an eventual small-degree guarantee for a fixed E^NP language and therefore yields infinitely many hard lengths in the known result. It does not place the language in NP, make the lower bound almost-everywhere, produce a new unrestricted circuit lower bound, or settle P versus NP. External PCP/hierarchy proofs and the full costed implementation remain outside this repository's Lean acceptance.
