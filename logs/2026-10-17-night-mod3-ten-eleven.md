# 2026-10-17 JST: n10 formal candidate, n11 three-orbit finite milestone

Research lead: 月野テンプレクス. One explicitly approved night session.
Starting commit783b4547812e15c6dc43106d2f1fe490d6389d60; read AGENTS, all its
required documents, open #8/#10, recent commits/logs and exact formal definitions.
GitHub connected writes succeeded. Local DNS prevented git clone; local Lean
was absent. No previous night's approval or future approval was assumed.

## Research result

n10: independently reconstruct eight real coefficient rows; full1024-input,
2048-affine-row, 11-layer and448-mutation checks pass, including actual Lean
literal alignment. Commit the genuine-degree candidate through pdeg_eq_two,
root import and15 target axiom reports. Exact finite minimum2123/3000 and dual
19/30 are unchanged. The formal build did NOT complete, so n10 is not promoted.

n11: generate and exactly replicate a nine-orbit witness, then reduce to THREE
seed orbits with fixed weights1/7,4/7,2/7. Preferred compact expansion has1925
indexed degree<=2 GF(2) polynomial entries, denominator27720. All2048 inputs
have success>=158/231>2/3. Exhaustive4096-row affine dual is69/110<2/3. The
original nine-orbit,4785-entry witness has the larger minimum24044/34375 and
is preserved unchanged. Compression trades margin for simpler probabilities.

## Verification, attacks and actual executions

All finite validators use independent exact encodings/algorithms; normal and
optimized Python outputs agree. Saved JSON equals actual output in completed
GitHub CI. The n11 checks include7 altered certificates, full pointwise
partition expansion, Mobius degree tests, direct/Walsh/hypergeometric duals.

- n10 semantic audit: run39037298636/job117409604280 SUCCESS, codebaa1d976.
- n11 original: run39037985386/job117411565884 SUCCESS, code81ca743a.
- n11 compact: run39038647497/job117413471238 SUCCESS, code402b1339.

Actual completed logs were fetched; source, certificates, output and matching
commits/trees were re-fetched rather than inferred from uploads. Compact
certificate blob2fed5a9a274f358deedf59879f4ba1160eb3214f; result blob
ad1f34fd3f814d11ad47a0052619f09db6dfc6d9. n10 source blob
6840ecfdd7786b583a7cc089e17da8c2f34e30e0.

## Blocker and dead directions

Formal run39037050907 at d25c6cd7: attempt1 job117408893626 and the single
rerun attempt2 job117411619247 both CANCELLED. Actual logs show shutdown
signals and exit143; both axiom audits did not complete. The shutdown cause
and n10 compilation verdict are unknown. No third identical retry, no weaker
axiom allowlist or weakened theorem. Complete formal coverage remains n5..9.

The raw n10 seeds without permutations fail at mask832 with success1/50:
graveyard/013-n10-unsymmetrized-mixture.md. The uniform coordinate-omission
lift to n11 fails at weight10 with success61/220: graveyard/014-n10-ignore-coordinate-lift.md.
Both execution failures are preserved separately in graveyard/015-n10-formal-runner-interruption.md;
those cancellations are not mathematical refutations.

## Successful commits and Issue state

edbdfdad67d95ba94b65a35c67e556d4ba869b72: orientation and actual write check.
d25c6cd777c7585d2765682baf34a94e38a9d6bc: candidate n10 Lean interface/audit targets.
baa1d976a45c4f74d10dcbb55f7195e7c0ae0744: independent n10 exact audit and CI.
81ca743a43b232b055de7849fa9a8782f913696c: original n11 certificate and counterexample.
8684f4f34d3168940c0f98c2af1ab4340bd5088e: attributed actual CI/interruption evidence.
402b13398af15add64961d4894b2a371beec3711: compact three-orbit n11 certificate/CI.
This log belongs to the final record-only commit, whose hash is not self-embedded.

#10 updated and remains OPEN for n10 execution/axiom gate. #11 created and
refined to the compact n11 frontier, remains OPEN. #8 unchanged and OPEN for
independent human semantic review. No new mathematical Issue was falsely closed.

## Next frontier and limits

First diagnose n10 interruption and complete the pinned --wfail build, namespace
allowlist and explicit target reports; inspect and re-fetch before promotion.
Then instantiate n11's compact witness in Lean with triple weights[3,12,6]/21,
threshold14, faithful degree and REAL-mixture quantifiers, full permutation
bridge and universal degree-one structural coverage. Do not blindly extrapolate.

No n11 Lean execution, second proof kernel or independent human review occurred.
Novelty, support/denominator minimality, exact LP optimality, general-n MOD3
bounds, barrier escapes and P-vs-NP conclusions are not claimed. All work is
committed, with no pending application patch or write-permission blocker. The
approved session ends at this finite replication/refinement and recorded
execution-blocker milestone; future research requires fresh approval.
