# Expedition 005 log

## 2026-10-10 (JST)

Observe/orient: read the governing documents, only open Issue #8, latest
commits and prior research logs. Start from the n=5-first formalization goal.

Act/verify: commit b29ddcd added the complete affine coefficient/input
encoding, kernel-checked finite bound and real-mixture obstruction.
Run 38054660994 passed. The desired deterministic bound is proved, not
smuggled in as an assumption of the final concrete theorem.

Continue: expanded the original quadratic orbit to 30 explicit formulas,
proved its every-input count, actual polynomial evaluation and degree bound.
Commit fcbe841 initially failed CI solely because an unused simp argument
produced a warning under --wfail. Commit 782979d removed that redundant
argument; no linter, warning policy, axiom policy or theorem was weakened.

Attack/repair: connected affine correctness to ZMod 2 polynomial evaluation,
allowed arbitrary finite real-weighted families with duplicates, and tested
constant flips, loss of randomization and loss of probability normalization.
The last invalid variant has a singleton countermodel in both Python and
Lean. It was deliberately generated as a control, not previously believed.

Record: final code commit 0150b864 passed formal run 38055370947 and semantic
run 38055370864. Read actual completed-job output, re-fetch remote sources
and commit, and preserve the reports, precise formal boundary and graveyard.
See ../../logs/2026-10-10-night-mod3-five-formal.md for the full checkpoint.
