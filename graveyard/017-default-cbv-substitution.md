# Failed repair: blindly substitute decide_cbv with its default step budget

Attraction: proof-producing call-by-value evaluation may avoid expensive raw
kernel normalization without trusting a code generator. That does not imply
that a textual substitution works under its default100000-step budget.

Actual bounded experiment: run39137339446/job117704436981 on approved2026-10-18
session. Smoke test passes, but the lower prefix, layer-only and full n10 variants
all fail with maximum simplification steps exceeded. Source hashes and full
outputs are retained in artifact12140576819 and Expedition016's first diagnostic.

Axiom-report trap: after those errors, the failed full file prints sorryAx in
pdeg_eq_two and other dependent declarations. Those reports are failure evidence,
not theorem acceptance. A green diagnostic recorder workflow cannot override
individual nonzero exit codes or an unallowed axiom.

Salvage: preserve the kernel lower prefix, which actually passed, and test a
bounded increased cbv step budget or split closed layer computations. Accept no
native_decide, new project axiom, lowered success threshold or hidden assumed
feasibility. This failure says nothing about the truth of the n10 certificate,
and it does not identify the cause of the previous night's runner shutdowns.
