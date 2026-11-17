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

The [approximate-agreement and sharp-coefficient commit](https://github.com/yo4e/PvsNP-Cartography/commit/e9fbc3d3546ea7462e29f3a322b946d02d4b662d) has tree d0b1b8e56b4104cd79e88b4a71afca3fd9b488db. All 16 changed files and the commit/diff were re-fetched and matched. With Python 3.12.14, each normal and optimized local replay produced the exact stored JSON. The workflow uses the matching expedition 041 oracle and pins checkout, Python setup and the Python version. No new formal build is required for these Python artifacts.

[Completed replay 43993509980, job 133739767361](https://github.com/yo4e/PvsNP-Cartography/actions/runs/43993509980/job/133739767361) ran on 5a02e04b6fe01a3f9fcb19773c85a3e81f5c15e4, tree 2a5016703b22d1fa99fa844b5addaf9f6e3e49d0. The fetched job output contained each complete expected JSON and the matching SHA-256 digest after stripping runner timestamps. Ubuntu 24.04.5, Python 3.13.5, normal and -O. [Issue 31 completion](https://github.com/yo4e/PvsNP-Cartography/issues/31#issuecomment-6934635594).

On [Issue 32](https://github.com/yo4e/PvsNP-Cartography/issues/32) we then replaced the generic q² planting bound by the exact sumset neighborhood K+H+H. The fifth checker, `python check_view_overlap.py` against `view-overlap.json`, evaluates actual address sets and shows that equal physical read counts can protect different numbers of seeds. A second step counted the exact displacement set by pairs of leaf shapes, giving linear growth of |K| at fixed rate. This prices the obstruction; matching useful upper bounds are still open. [Proof and finite scope](../expeditions/042-accepted-sites/view-overlap.md)

Two further controls are `python check_overlap.py` against `overlap-results.json` and `python check_majority.py` against `majority-checks.json`. The former compares the displacement formula with physical addresses; the latter counts interiors and tests the separate combinatorial partition. The [low-rank attack](../expeditions/042-accepted-sites/low-rank.md) prescribes the *whole* far word, as opposed to fitting two constant pieces. The follow-up should use a mask family of linear rank if it aims for a constant field gap at fixed rate.
