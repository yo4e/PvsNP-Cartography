# Exact counts and implementation costs — corrected entry point

Updated 2026-11-08 JST by 月野テンプレクス. The complete original November5 analysis is preserved **byte-identically** at [history/cost-and-fidelity-2026-11-05.md](history/cost-and-fidelity-2026-11-05.md), original Git blob52fd8fd45005f67a339bd64fa2c4cfd854daa7da. Its original evidence is historical, not an execution report for modified source.

## Correction that changes the implementation accounting

The old source used `len(set(masks))` for duplicate validation. The original analysis allowed a pessimistic quadratic t^2 charge, absorbed by t*M in its generic construction bound. But its later large-degree tail=0 branch invoked the tighter one-step construction and a 2^n*poly(n) bound. That branch cannot absorb arbitrary quadratic hash-collision work. Treat the old unqualified whole-implementation bound as needing this correction.

Source9afb67d1d1061558cea1a7a7d085236a59504087 replaces hash validation by sorting and adjacent comparison. The corrected cost is O(t log(t+1)*poly(n)), including the tail=0 branch. Polynomial values, finite test coverage and the earlier Lean sources are unchanged. A dedicated completed CI run reproduces both earlier suites and the new controls; it does not formalize the runtime.

Full attack, scope and repair: [Expedition034 cost correction](../034-uniform-pcp-transfer/cost-correction-2026-11-08.md). The old runtime-audit.json remains the November5 result; its numerical fields still match and only the executed source fingerprint changes. New output hashes and complete CI evidence are in [Expedition034](../034-uniform-pcp-transfer/execution-evidence.md).

## Current mathematical reading

Read the archived full derivation together with the correction. The nontrivial regime's generating-function budget and the modulus/folding/zeta identities are not refuted. With deterministic validation and charged coefficient construction, the written known-method bound remains

    (1+t*M(n,(2b+1)d)+2^(n-b))*poly(n,b),

and the conservative choice b=floor(n/(100d)) gives2^(n-n/(200d))*poly(n) in its nontrivial regime. For large d use the actual one-step tail=0 construction; degree0 total counts are direct. Redundant input encodings retain their explicit read/normalization cost.

Neither the earlier formal exact-count identity nor the new finite CI is a Lean runtime theorem. The conditional source-faithful use of this counting ingredient, with oracle and description costs kept explicit, is in [source-bridge.md](../034-uniform-pcp-transfer/source-bridge.md). No novelty, independent semantic review, unrestricted lower bound or P-versus-NP conclusion is claimed.
