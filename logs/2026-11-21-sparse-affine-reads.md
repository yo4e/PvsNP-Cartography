# November 21 JST evening — a sparse verifier and its degree obstruction

Fresh approval was received for this nightly PvsNP-Cartography session.
Starting main was fa1dabd4. The earliest unblocked issue was34; the older
human/AI review gates8 and15 were left within their separate scopes.

## What changed mathematically

Replacing full-A membership by23 XOR-translated reads retains the exact
109 raw NO failures while reducing uniform signed sensitivity to23.
Both padded cubes remain Q=4,194,304. The strict sufficient threshold is
109/96,468,992, a128/23 improvement over Expedition044, and guarantees any
four physical YES-bit errors.

The decisive argument uses complementary binary subspaces. Every pair of
passing A stars intersects in two points, forcing their affine polynomials
to coincide. The inherited B proof reconstructs one polynomial only where
its local tests pass. This supplies the residual root bound for arbitrary
global proofs, including noncodes. Truthful old auxiliaries attain109.

## Attacks and repair

Eight-read and29-read Hamming-ball alternatives keep the correct affine
zero-error code space but admit explicit noncode proofs with106 and108
rejections. Those globally shared witnesses, their exact field values and
their clause replays survive in graveyard and the expedition. The chosen
23-read schedule rejects those witnesses128 and124 times.

## Applicability check

For the actual honest YES assignment with zero padding, exact GF(2)
algebraic degree is18 on22 address variables. Every degree17-or-lower
polynomial differs in at least16 bits; a fixed mixture cannot reduce the
mean below that. Since16>109/23, the improved budget still requires degree18
for this specified function. Four-bit tolerance alone is not a useful
low-degree approximation construction.

The same session then settled free padding. The used prefix is a downset,
so ANF coefficients outside it can be deleted without changing any queried
bit. The executed completion has degree 17. Its fixed 21-cube also has
degree 17, forcing at least 16 used-bit errors against every degree 16-or-
lower competitor, regardless of padding or fixed mixture. Both exact and
budgeted minimum degree over padding are therefore 17 for this physical
proof. Other satisfying proof choices are not optimized. The next task is
to cost the designed growing one-level family, including actual Q and
degree/approximation behavior.

## Verification and persistence

[Execution evidence](../expeditions/045-sparse-affine-reads/execution-evidence.md)
records the completed local checks and actual remote commit/run readback.
Initial code 9483c577 and integrated code 47910b0a are published. Completed
[run 44912211021](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44912211021),
job 136870212842, ran all six scripts in normal and -O modes under Python
3.13.5, with exact equality to every stored output. The full replay-step
log, actual digests and immutable source readback manifest are archived.
All 39 added/changed files were re-fetched and matched their text and Git
blob hashes; all 834 untouched base files match. The lead also reproduced
the outputs locally, and separate NumPy calculations checked the completed
truth/ANF hashes and fixed-coordinate parities.

[Issue 34](https://github.com/yo4e/PvsNP-Cartography/issues/34) is closed as
completed. [Issue 35](https://github.com/yo4e/PvsNP-Cartography/issues/35)
records the next family/cost/degree target. Issues 8 and 15 are unchanged.
The final record commit changes evidence and logs only; source 47910b0a is
the executed mathematical/code checkpoint.

[Conclusion](../expeditions/045-sparse-affine-reads/conclusion.md) ·
[Primary argument](../expeditions/045-sparse-affine-reads/theory-notes.md) ·
[Degree audit](../expeditions/045-sparse-affine-reads/degree-notes.md).

No new Lean result, external review, novelty, general circuit lower bound
or P-versus-NP separation is claimed. This session ends at the integrated
construction/attack/degree-audit milestone. A later nightly session needs
fresh approval.
