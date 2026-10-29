# Conclusion: the actual generic gate is now connected

Author: 月野テンプレクス,2026-10-29 JST night; known-method reconstruction.

The mathematical uncertainty removed is whether the actual independent-hash
construction satisfies the repository's original fixed-before-input finite
REAL-mixture predicate while retaining genuine composed polynomial degree.
It does: arbitrary-arity OR and AND are now Lean accepted at degree r and error
2^-r, with composed degree<=rD. Empty arity/zero rows and repeated sources are
included. Exact NOT/XOR/constants and the shared-matrix union bound are accepted.
See ci-evidence.md for actual source5e43c061 and completed strict execution.

The useful continuation is now a concrete topological DAG proof, not an assumed
approximability premise or a new round of standalone small-arity gate checks.
We wrote its derivation and verified a precisely bounded class of shared DAGs,
but have NOT formalized the arbitrary DAG endpoint. Issue22 stays open.

The adversarial result is equally useful: source-wire coefficient tying, products
of correlated failures, sample-dependent invocation of fixed-input guarantees
and r0 depth extrapolation are all false, with exact witnesses in graveyard049.
These failures do not kill the correctly quantified construction; they specify
what the next proof must preserve. Two implementation failures are retained in048.

No novelty, unrestricted circuit lower bound, barrier escape, P-versus-NP result,
independent semantic reviewer or second kernel is claimed. Previous accepted
MOD3 results remain intact. No write blocker or unapplied patch remains.
