# 035: the first numeral repair still left the GF(2) unit opaque

Approved2026-10-22 JST night. Failed code7f687cebc807faf8b34f560aaef5b28a54e9109c,
completed FAILURE run39798702853/job119892916030. Full decoded job log inspected.
This is an implementation failure, not a counterexample to the intended theorem.

The earlier failure and its first repair are preserved in graveyard034. The
first repair removed an unused closed-goal tactic and converted finite-field
numeral equalities using ZMod.val_injective and ZMod.val_ofNat. It solved the
weight10 goals, but q9_layer_six, r8_layer_six and q8_dual_score still contained
conditions of the form `0 = ZMod.val 1` or `1 = ZMod.val 1`. The actual unit
value had not been simplified. Treating these as ordinary unreduced integer
identities, or assuming the profile score, would not be a valid repair.

Repair: in exactly those three proofs add
`have h1 : (1 : ZMod 2).val = 1 := rfl` and include h1 in the final norm_num.
No new axiom, target relaxation, input restriction, coefficient restriction or
warning suppression is involved. ProfileMixtures itself had already built,
but that partial success was not treated as whole-root acceptance.

Accepted repair9410fa952ad4b92f09237bfc09be5ad200413db3 passed the completed
run39800322628/job119898840545: --wfail9054 jobs,741 declarations in the unchanged
axiom allowlist and all24 explicit new target reports. Actual source, commit,
completed steps and log were re-fetched. The exact failed sources remain at
their commits; this note is not a claim that the full failed log is saved here.
