# Expedition 037 log

The November 10 JST nightly session began at `b1f6825`. The operating contract, required reading, research direction, prior log and open Issues put #28 first among the unblocked mathematical tasks. #8 and #15 retain their independent-review scope.

1. Oriented the audit in `29e5df3`. Compared BV14's seed shifts, ACSP translations, tree queries and Cook–Levin auxiliary addresses with Viola's fixed-input counting argument.
2. Tested tagged permutations and the untagged two-address counterexample in `46efd23`. Formalized the written finite argument for fixed-degree XOR copies, extracted the conditional affine-rank budget, and attacked the hardwiring step in `cc7171a`.
3. Re-fetched the three result files and the completed [Actions job](https://github.com/yo4e/PvsNP-Cartography/actions/runs/42834963674/job/129894612862). The 5,054 affine maps and 33,792 polynomial-score evaluations are bounded corroboration. The [Issue 28 checkpoint](https://github.com/yo4e/PvsNP-Cartography/issues/28#issuecomment-6770130503) records the other test scopes.
4. In closing out that session, compared Eq. (9), Definition 6.2, Proposition 6.1 and the printed row test in BV14 §6.3. Direct substitution at β and c₀ exposed a reversed bit convention. Checked both origins and the one-level coordinate reconstruction. See the [post-mortem](../../graveyard/037-row-redirect-marker.md) and [saved finite output](rs-level-checks.json).

The recursive final-address bound and the per-input error budget remain open. Neither the named counterexamples nor the local coordinate repair received Lean verification or external mathematical review.

One-level reproduction: run `python3 verify_rs_level.py` in this directory and compare stdout with `rs-level-checks.json`. Run again with `python3 -O`. There is no random seed. Five (a,k) choices and both affine-origin conventions are exhaustively checked within a single level, including all occurrences at children of leaf dimension. At (3,7), reversing the intended bit misroutes 256 of 1,024 row states. The two conventions encode the same geometry, so their counts should not be pooled as independent evidence.
