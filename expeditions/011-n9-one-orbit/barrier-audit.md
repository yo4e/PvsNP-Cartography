# Expedition 011: proof-barrier and scope audit

Date: 2026-10-16 JST. Skeptic: same author, not independent review.

**Exact claim:** finite n=9 MOD3 over GF(2), pointwise error 1/3, probabilistic polynomial degree exactly two. This claim uses finite support and real mixing weights. The full permutation symmetrization theorem has arbitrary finite arity, but the MOD3 degree equality itself is ONLY established at the named n=9 (with earlier n=5..8 checkpoints).

- **Relativization:** No oracle classes P^A/NP^A, Turing-machine separation or uniform complexity-class claim is involved. The Baker–Gill–Solovay barrier is not claimed to be evaded.
- **Natural Proofs:** No constructive/large/useful property of truth tables for unrestricted circuits is derived. The Razborov–Rudich theorem is neither invoked as a proof of our finite bound nor claimed to be bypassed.
- **Algebrization:** Working with GF(2) polynomial objects does not establish non-algebrization. There is no oracle-extension step or circuit lower-bound consequence.
- **Sampling to infinity:** The finite n=9 upper bound enumerates all 512 inputs via a verified layer bridge; this says nothing about n>=10.
- **Probability quantifiers:** The polynomial distribution is uniform over the **full** coordinate permutation orbit chosen independently of each input. The seed alone fails at a concrete input. Never replace a worst-input bound with a global average.
- **Lower coverage:** All n=9 degree-one polynomials are reduced to affine masks via the existing structural theorem. Symmetry reduces 1024 possibilities to 20 exact canonical checks in Lean. Its proof does not assume a selected finite mixture can stand for all choices.
- **Numerical optimization:** The exploratory LP was only a candidate discovery tool. All accepted numerators, denominators and inequalities are integers/rationals. A previous failed fraction-rounding approach is preserved in graveyard/009.

The related main literature is Srinivasan, Tripathi and Venkitesh (2021), *On the Probabilistic Degrees of Symmetric Boolean Functions*, SIAM J. Discrete Math. 35, 2070–2092, DOI https://doi.org/10.1137/19M1294162. Its published abstract characterizes symmetric probabilistic degree up to polylogarithmic factors; this brief targeted check does not establish that this exact n=9 small-orbit witness is new. Novelty remains **unknown**.

Nothing here settles P vs NP, proves an all-n MOD3 bound, identifies minimal orbit size, or escapes any proof barrier.
