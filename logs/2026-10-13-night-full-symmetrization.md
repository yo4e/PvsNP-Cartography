# 2026-10-13 night: full symmetrization, checked applications and countermodels

One fresh approved session. Research lead: 月野テンプレクス.
Start: 59190b5b91e9a48e9e5f7930e1df5b0be641ec01. Mandatory orientation,
open Issue #8 and prior completed stages were read before substantive work.

## Result

Completed generic variable-permutation transport and full symmetrization with
actual GF(2) polynomial degree, normalized nonnegative REAL weights, and one
family before all inputs. Proved the exact success/orbit-average identity,
full success invariance, preservation of pointwise guarantees and equivalence
of orbit certificates with the original degree predicate. Applied this to the
already proved n=6/n=7 MOD3 feasibility without a new feasibility assumption.
Three mathematical counterexample components are also checked in Lean.

This is a general transformation theorem, not an all-n MOD3 degree bound.
The next Hamming-layer coverage and fiber-counting identity remains unproved
in Lean. Do not merge those two stages in future summaries.

## Verified evidence

Final code ac61ba1b2888de029b8fc567187ff3a4dbb263c0 passed formal run38414011388,
job115353465722: Lean4.35.0-rc4, Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8,
--wfail, 205-declaration namespace audit, 21 explicit symmetry target reports.
All new targets use only propext, Classical.choice and Quot.sound. Actual
completed logs and source/commit/tree were retrieved and hashes compared.

Core proof c1ff9c8639e9aef0a83f9492f087934085fd5c83 previously passed
run38412149245/job115346960273 with 188 declarations and 16 targets.
Semantic commit b2602bb5269bdbbda85cc1fc57610bd0208c2a72 passed
run38412385402/job115347783200. Its core source hashes are unchanged in the
final formal commit; normal and -O outputs match the local reproduction.

Finite checks: all 278 squarefree polynomials and score tables for n=0..3,
12,426 squarefree and 42,944 higher-exponent evaluations, 30 mixtures.
For n=7, all 90,720 polynomial/permutation pairs and 128 inputs are checked;
full symmetrization gives success 11/15 at weight three, otherwise 2/3.
No improved worst-case error or new finite degree value is obtained.

## Failures and repairs

Two failed builds are preserved: 75ce55dea40b176e83ed242eaf7b85a627e1cc60
(run38410870758/job115342534435), wrong sum_comp overload; and
7093b1070cc69b4746ad10f244a971e30e18db63 (run38412898572/job115349584281),
unresolved characteristic-two arithmetic. Repairs changed proof steps only.
No theorem, certificate threshold, --wfail setting or axiom policy was weakened.

Seven invalid mathematical shortcuts have exact countermodels in
 graveyard/007-symmetrization-hypotheses.md. Missing symmetry can lower success
from 1 to 1/2; a whole-cube average of 3/4 can coexist with an input of success
zero; cyclic averages need not agree at equal-weight inputs. Four malformed
probability/group inputs are also rejected, including under Python -O.
The exact coverage of the three Lean counterexample components is documented;
not all seven Python countermodels have separate Lean theorems.

## Continuity and remaining work

The generic transformation stage is complete. Next prove equal permutation
fiber counts and the uniform Hamming-layer average identity, then use it for
the existing n=8 finite certificate. Numerical Lean coverage remains n=5,6,7.
Issue #8 stays open for the next interface and independent human semantic review.

No GitHub write blocker or unapplied patch remains. Local Lean was unavailable;
actual formal checking was in Actions. Same-author tests and separate machines
are not independent human review or a second proof kernel. Novelty, support
optimality, all-n MOD3 degree bounds, barrier escape and P-vs-NP are unclaimed.

Records: expeditions/008-full-symmetrization/, claims/008-full-symmetrization.md,
formal/reports/2026-10-13-full-symmetrization-axioms.txt. The records commit adds
observed evidence and continuity without changing verified formal code.
