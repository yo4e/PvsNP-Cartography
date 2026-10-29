# Randomized gate implementation failures, not counterexamples to the mathematics

Author: 月野テンプレクス, approved2026-10-29 JST session. Preserve failures before repair. No failed candidate is promoted to verified.

## First attempt

Source15d2dc2b144a54790334c4c9740bbf6ca735074c; formal run40881942065/job123475459692 completed FAILURE. Completed states and full decoded actual job log retrieved. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac, whole-root --wfail retained; axiom reports were skipped after the build failure.

Actual failures: the proof mixed Fin.val and ZMod.val in omega, leaving unrelated arithmetic atoms; arithmetic normalization did not close 1+1=0 in ZMod2 without an explicit characteristic-two fact; the dependent Fin.cons in an untyped universal binder did not elaborate. The run also rejected obsolete push_neg/if_neg and an unused simp argument under --wfail. The source does not yet establish the gate theorem by kernel acceptance.

Repair: kernel-decidable two-element facts only (not native_decide), an explicit Fin(r+1) binder, current push Not/ite_eq_right names, and removal of the unused argument. Preserve every original field, actual-degree, real-weight and pointwise quantifier. No warning or axiom policy is relaxed. Later outcomes are recorded in the expedition evidence and session log.

## Second attempt

Source1ea3559ed9c10898dff62c00189d65e91e92a968; formal run40883125251/job123479644185 completed FAILURE. Actual completed states and full decoded output retrieved. Two errors remained: the inner Fin.cons still elaborated with an unconstrained dependent codomain despite the typed index; destructing the existential union witness before simplifying its indicator left an unsimplified existential on the inequality's left side.

Repair at5e43c061544f2d56e924a03420c39d40ad5ecbc6: annotate the inner tuple itself as Matrix k (r+1), and rewrite the existential indicator using the witness before destructing it. No lemma premise, field, error tolerance, degree definition or independence claim changed.

## Verified salvage

The third candidate completed SUCCESS in formal run40884225246/job123483506622: pinned whole-root --wfail9069 jobs,1083 declarations within the unchanged axiom allowlist, and all22 new gate reports plus prior reports. Actual source/commit/tree/completed output were retrieved before promotion. The lesson is to separate representation/elaboration failures from mathematical counterexamples; the latter are preserved independently in graveyard049. The generic gate theorem is accepted, not the still-unformalized full DAG endpoint.
