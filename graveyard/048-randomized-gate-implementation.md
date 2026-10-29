# Randomized gate implementation failures, not counterexamples to the mathematics

Author: 月野テンプレクス, approved2026-10-29 JST session. Preserve failures before repair. No failed candidate is promoted to verified.

## First attempt

Source15d2dc2b144a54790334c4c9740bbf6ca735074c; formal run40881942065/job123475459692 completed FAILURE. Completed states and full decoded actual job log retrieved. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac, whole-root --wfail retained; axiom reports were skipped after the build failure.

Actual failures: the proof mixed Fin.val and ZMod.val in omega, leaving unrelated arithmetic atoms; arithmetic normalization did not close 1+1=0 in ZMod2 without an explicit characteristic-two fact; the dependent Fin.cons in an untyped universal binder did not elaborate. The run also rejected obsolete push_neg/if_neg and an unused simp argument under --wfail. The source does not yet establish the gate theorem by kernel acceptance.

Repair: kernel-decidable two-element facts only (not native_decide), an explicit Fin(r+1) binder, current push Not/ite_eq_right names, and removal of the unused argument. Preserve every original field, actual-degree, real-weight and pointwise quantifier. No warning or axiom policy is relaxed. Later outcomes are recorded in the expedition evidence and session log.
