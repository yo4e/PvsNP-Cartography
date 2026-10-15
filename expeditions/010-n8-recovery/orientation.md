# Expedition 010: complete the n=8 formal chain and recover the compact witness

Execution date: 2026-10-16 JST. One freshly approved session.
Research lead: 月野テンプレクス. Human steward: 山田佳江.
Starting main: b9b736e385ef91f87aefef328e0248da8d2a2513.
Roles: cartographer, formalist, experimentalist, skeptic, historian, archivist,
all performed by the same author. This is not independent human review.

## Orientation and selected work

Read AGENTS.md, all five mandatory documents, current open Issues, recent
commits, the preceding research log, the prior local handoff and the actual
formal source and failed CI. Issue #8 still described the Oct13 checkpoint,
but main already contained a later Hamming-layer/n=8 candidate. Do not overwrite
that work with an old patch or count completed generic symmetrization as new.

The earliest unblocked task was repairing and verifying that existing n=8
chain. In parallel, recover the Oct14 local-only 939-polynomial certificate,
validate its exact provenance, and explore a smaller explicit support.

Acceptance requires the original GF(2) target, actual polynomial totalDegree,
nonnegative REAL weights summing to one, and one fixed family before every
input. Numerical candidates are accepted only after exact all-input validation.
A smaller explicit witness and the existing full-symmetry Lean proof are
separate evidence objects and must not be conflated.

## Operational boundary

GitHub write tools were available again. The first proof repair was committed
and re-fetched successfully; the prior read-only blocker did not recur.
Local Python was available but Lean/lake and outbound GitHub DNS were not.
Actual formal checking used the existing GitHub Actions workflow. No paid
resource, new external credential, or publication/submission was requested.

The previous 22-file patch was NOT applied wholesale. Its mathematical witness
is recovered deterministically by recover_939.py, and verify_compact.py is
byte-identical to the prior direct validator. Original handoff filenames and
hash are recorded in prior-art.md. The old package remains a historical archive,
not a claim that every legacy file has been committed.
