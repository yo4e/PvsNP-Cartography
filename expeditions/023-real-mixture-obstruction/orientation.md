# Expedition 023: real mixtures and the restricted n12 obstruction

Approved session: 2026-10-22 JST night. Research lead: 月野テンプレクス.
Starting main: 9dcd6e1268adf4251c2b76f53eb8ce38c085b811.

## Observe / orient

Read live AGENTS, its five required documents, research direction, current status,
open Issues #8/#15/#16, #14 completion and the preceding research log. Reuse the
accepted HammingProfiles/CliqueProfiles evaluator and existing finite real duality.
The earliest unblocked target is #16. This initial file is an actual write test
and a plan, not a claim of a completed proof or successful new Lean execution.

## Mathematical target

At n=12 restrict support to zero, q_A with |A|=9, and r_B with |B|=8,
where q_A=1+sum_all X_i+e_2(A), r_B=1+sum_outside_B X_i+e_2(B), over GF(2).
Use the input distribution that places total mass 5/14 on the uniform weight-6
layer and 9/14 on the uniform weight-10 layer. Derive from actual polynomial
profiles that zero/q9 have dual success 9/14 and r8 has success 241/462.
Apply finite real weak duality to exclude a fixed, normalized, nonnegative,
input-independent finite mixture supported in precisely that family from having
success >=2/3 at every input. The gap is 1/42. Neither an unrestricted quadratic
lower bound nor the n12 probabilistic degree is asserted.

## Loop and natural milestone

Derive a small actual-correctness mixture interface; instantiate the measure and
family; verify pinned Lean/axiom output if execution is available; attack support,
quantifiers, normalization and GF(2) evaluation. Preserve failed attempts rather
than weakening the theorem. After this bounded integration, assess a primary-source
bridge to a restricted lower bound instead of automatically advancing to n13.
If formal execution is blocked, preserve exact candidate files and the unverified
gap, then perform useful unblocked mathematical work without falsely closing #16.

## Environment observed so far

Local git clone failed because github.com DNS resolution is unavailable; no local
lean/lake/elan executable is installed. Connected GitHub reads work. Python exact
integer/rational computation is available. This write probes connected mutation;
its result must be re-fetched before reporting persistence. No paid resources or
external publication are authorized by this session.

Evidence and novelty are separate axes; novelty remains unknown. No independent
review of this expedition or second proof kernel is assumed.
