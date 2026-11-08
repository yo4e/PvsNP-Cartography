# Current checkpoint — exact block-count chain accepted; cost audited separately

Freshly approved2026-11-05 JST session. Research lead: 月野テンプレクス. **Issue25 is CLOSED/completed; Issue26 is the next bounded mathematical frontier.** Issues8/15 remain independent older review gates. This checkpoint grants no authority for later sessions; fresh approval remains required.

## Accepted formal result

For every actual GF2 polynomial P in a+b variables and every Boolean head assignment represented by a subset T, `SubsetZeta.exact_count` equates the canonical integer residue of the actual amplified/reduced/folded subset transform with the exact number of accepting tail assignments. The pipeline includes the actual integer coefficient lift, signed-integer modulus amplifier, genuine degree bound, ring-generic Boolean reduction, tail monomial sum, colliding-head coefficient aggregation, subset-zeta invariant and strict no-wrap interval. No supplied coefficient oracle or conclusion-as-premise replaces P. Empty head/tail and constants remain covered.

Accepted source **51a86b10cb0f493b0c093aa81dba734400cb0118**, treec04b4412f9426b633c6e8c1d57f29af737dc0e01. Completed SUCCESS run42038613103/job127283180450: pinned Lean4.35.0-rc4/Mathlib9e6b3aac, strict --wfail9079 jobs,1466 declarations within unchanged[propext,Classical.choice,Quot.sound],43 ModulusAudit reports and7 explicit signatures plus all older reports. Actual source/commit/tree, completed states and full decoded output were retrieved. This is not independent semantic review, a second-kernel check or a clean-room build.

## Written algorithmic result, not a Lean runtime theorem

The new deterministic sorted-coefficient construction and shared table cost `(1+t*M(n,(2b+1)d)+2^(n-b))*poly(n,b)` under the explicit canonical squarefree ANF encoding. Charging coefficient bits, sorting, construction, folding and table allocation gives a conservative known-method reconstruction `2^(n-n/(200d))*poly(n)` for d>=1, with a separate one-step b0 argument in the large-degree regime and constant handling for d0. Full derivation and representation qualifications: ../expeditions/033-modulus-block-count/cost-and-fidelity.md.

Literal unshared recursive evaluation needs3^a coefficient leaves; a shared table needs a*2^(a-1) additions (zero when a0). These count different operations, not wall-clock ratios. Construction can dominate: n8, linear source, b6 produces17608 pair visits and254 terms for only4 final additions. Thus neither the extensional Lean recursion nor a fast last stage proves a fast full program. The Python refinement and general bit-cost derivation remain outside the accepted formal theorem.

## Replication, failures, and persistence

Unchanged earlier controls reproduce75295 exact block counts and1548 signed integer tests. New counted code checks22719 exact head counts,26616 signed modular tables and604 finite budget instances. Normal/-O stdout files match byte-for-byte; both Python files compile. The actual remote code and stored results match executed Git blobs. Finite checks are not general proofs or independent review.

Code7eb2f25aa57b676f55f36a9648cd5212e9678ed4; written costsccc22bf79e6adde2af99d95c81a20f4959bd4db0; full new stdout0762832f6e5bf8c27c83ee63a7ff7ac68078209f. Evidence: ../expeditions/033-modulus-block-count/execution-evidence.md. Failure preservation: ../graveyard/2026-11-05-zeta-cost-shortcuts.md. It records the preceding failed build, false free-sharing inference, duplicate-coordinate corruption, overwritten coefficient collisions and omitted construction costs.

Connected GitHub writes and Actions worked despite local DNS failure and missing Lean/Lake. No write/security denial or unapplied patch remains. Record-only commits do not create new mathematical-source execution evidence.

## Next frontier and retained boundaries

Issue26: inspect the actual uniform counting-to-hierarchy/oracle transfer, representation and witness-search costs, and E^NP/infinitely-often quantifiers. First attack the written budget and then read the source's Section2.3 and cited hierarchy inputs. Do not substitute NP for E^NP or infer an unrestricted lower bound from counting alone. Costed formal implementation refinement remains a named gap, not an achieved theorem.

Previous covering/root-budget/shared-DAG/growing-degree/finite MOD3 results remain intact. The degree-one uniform-cover usefulness route stays refuted; don't restart it from stale README/direction text. Novelty, optimality, independent semantic approval, second-kernel checking, general n12 classification, unrestricted separation and barrier escape remain unclaimed.

Previous complete status preserved byte-identically at history/2026-11-05-pre-block-count-status.md (blob4dafb5620c9b5bf6ab5058ee76bbcc0fd3bdde3d). Complete previous ledger: ../reports/2026-11-05-pre-block-count-ledger.md. Session log: ../logs/2026-11-05-folding-audit.md.
