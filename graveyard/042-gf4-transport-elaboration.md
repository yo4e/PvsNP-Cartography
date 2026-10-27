# 042: first actual GF4 transport candidate failed compilation

Approved session2026-10-27 JST. Source73d562a7c2ffb49a1379e3e7513b04f475de4a70,
run40429493278, job121943428570, completed FAILURE. Full decoded job output and
completed step states were retrieved. No successful audit or endpoint report
ran for this source; they were skipped after the build failure.

Actual diagnostics at2026-10-27T00:59:52Z:
- GF4Transport.lean:34:44: Unknown constant Finset.card_pair_le.
- GF4Transport.lean:167:2 and168:2: unsolved degree goals for a natural-number
  cast into a polynomial, after broad simp had erased the C-constant form.

The repair270cf3773274c5e1455874c57f80166bbd1c6e07 proves the two-element finite
set count by simp and uses an explicit constant-polynomial goal followed by
MvPolynomial.totalDegree_C. No field, degree, quantifier, probability, target,
warning flag or axiom policy changed. Mathematical correctness is not inferred
from this repair: its own completed build and audit must be checked separately.

Failed source remains in Git history. These are implementation failures, not
counterexamples to the transport statement. This file records inspected errors,
not a claim that the entire raw CI log has been archived here.
