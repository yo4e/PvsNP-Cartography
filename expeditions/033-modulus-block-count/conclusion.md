# Conclusion — exactness accepted, implementation cost made explicit

2026-11-05 JST. Research lead: 月野テンプレクス. Issue25 is completed at its bounded correctness milestone. Issue26 is the next mathematical frontier, requiring fresh approval in any later session.

The failed prior folding/zeta build was repaired without changing statements. At51a86b10cb0f493b0c093aa81dba734400cb0118, completed run42038613103/job127283180450 accepted the original-GF2-polynomial-to-exact-block-count chain. Strict build,1466-declaration unchanged axiom audit,43 named reports and7 explicit signatures were inspected. The accepted theorem is extensional, not an executable runtime guarantee.

We then continued beyond build repair: a deterministic sorted-coefficient implementation and shared-table transform were written and attacked. Existing checks reproduced75295 exact counts; new checks passed22719 counts,26616 signed modular tables and604 finite budget instances. Both scripts pass normal/-O byte-identity and compilation. Remote blobs were compared to executed bytes. This is finite same-author validation, not independent review.

The separate written derivation charges construction, sorting, coefficient bits, folding and table allocation. It reconstructs the known counting form2^(n-n/(200d))*poly(n) with a deliberately weak constant and explicit input conventions. In the large-degree b0 case the amplifier is F_1(Y)=Y, so construction has one multiplication by a constant and at most t products; it is O(t*poly(n)), NOT the loose t*M bound. Since t<=2^n, the remaining dense transform is at most2^n*poly(n). Degree0 total counts are handled directly. The Python-to-specification relation and asymptotic cost bound are not formally verified in Lean.

Dead shortcuts are retained in ../../graveyard/2026-11-05-zeta-cost-shortcuts.md: treating unshared recursion as memoized, repeating coordinates, overwriting head collisions, or dropping construction costs. Full new control stdout is runtime-audit.json. Actual source/commit/toolchain details and selected log excerpts are in execution-evidence.md; written reasoning is in cost-and-fidelity.md.

No local Lean/Lake or clone access was available, but GitHub writes and CI worked. No write-security blocker or unapplied patch remains. Independent semantic review, second-kernel checking and costed formal implementation refinement remain gaps. The next substantive question is the uniform counting-to-hierarchy/oracle bridge with its actual E^NP and infinitely-often quantifiers, not another round of generic infrastructure polishing.
