# Completion log for the previously started layer/n=8 expedition

Recorded2026-10-16 JST. The original orientation remains unchanged and identifies
the Oct14 starting work. Current session details are in ../010-n8-recovery/log.md.

The predecessor main contained HammingLayers, LayerCertificates and an n=8
formal candidate, plus finite audits and graveyard008. Its last inspected formal
run38585537578/job115926408709 at9bf6ad40 failed on a natural-sum/field-sum
mismatch and excessive concrete simplification. Earlier core compilation alone
was not treated as success for the complete n=8 chain.

Repair21f5b710 fixes sum transport and limits correctness simplification; its
actual run38816045819/job116700845599 still failed on Nat-to-real0/1 casts.
Final e034962d uses norm_num in those branches. The actual completed
run38816877083/job116703673137 succeeds through --wfail,305-declaration audit
and explicit target reports. No statements, coefficients, thresholds, resource
settings or axiom policy were weakened. Both failures remain in Git history.

A direct source/commit/result re-fetch confirms the final status. The original
Expedition004 seeds and probability definition are unchanged. This records
completion of a prior multi-session construction, not a claim that every source
file was newly written in the final repair session. See conclusion.md for scope.
