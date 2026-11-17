# November 17 JST • actual accepted-site agreement

Fresh one-session approval. The starting main was 6bbe8f03db2e2468929a999197d4cc20b9849d07. [Issue 31](https://github.com/yo4e/PvsNP-Cartography/issues/31) was the first unblocked mathematical task, alongside the separately scoped external review gates #8 and #15.

The [physical-splice commit](https://github.com/yo4e/PvsNP-Cartography/commit/af5f8ab7a61a2d66153b1509a06e3b9916943ce5) has tree 72643daf707b14e2c9190d779a6bbe6d0e989cf5. Its parent, changed paths and nine files were re-fetched and matched. The second iteration gives approximate agreement using fixed masks and sharpens the unmodified two-level coefficient. [Results and open cost question](../expeditions/042-accepted-sites/conclusion.md) · [Failure record](../graveyard/2026-11-17-exact-accepted-sites.md)

| Run from expeditions/042-accepted-sites | Output | Meaning |
|---|---|---|
| python physical_patch.py | physical-patch.json | New shared GF(256) proofs, actual leaf/outer residual checks and separate k=64 integer budget. |
| python check_mixing.py | mixing-checks.json | All failure subsets at dimensions 3/4, weighted sampler and translated toy residual. |
| python check_two_level.py | two-level-checks.json | Row-credit inequalities, field/alias split witnesses in the four listed parameter cases. |
| python check_parity_recovery.py | parity-recovery-checks.json | Reconstruct two nonconstant polynomials from the shared GF(256) physical checker. |

These checks are deterministic. Python's normal and optimized interpreters must produce the exact committed JSON. The general arguments use polynomial interpolation and a published bivariate agreement lemma. They have no Lean execution, independent human review or novelty assessment.
