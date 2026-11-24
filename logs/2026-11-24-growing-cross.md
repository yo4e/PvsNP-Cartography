# November 24 JST — growing cross and coefficient-labelled proof rows

Fresh approval in the nightly conversation; parent 0bf3887f. #35 was the earliest unblocked substantive question.

The one-level family was priced with actual generated GF(128) and GF(512) Boolean circuits and a written general gate bound. The NO minima are 109 and 477; exact signed sensitivities 23 and 47; compact cubes 2^22 and 2^27, giving strict raw radii 4 and 10. The compact fixed named proof's exact and budgeted minimum over free padding is 17 and 20; 16 and 64 directly checked disjoint odd-parity cubes exclude the next lower degree. Reindexing rows by honest coefficients yields exact degrees 15 and 16 at a cost of 16x/64x compact storage, and an unequal-prefix alternative for GF(512) gives degree <=17 at 16x storage. The written basic scheme has O(log k) degree and polynomial-in-N storage for this known-reference family. It is not witness-independent.

The unrestricted fixed-layout extension is false by counting arbitrary independent constant rows, with an eight-row finite control. Shared B inverse and noncode attacks remain in the replay. See [conclusion](../expeditions/046-growing-cross/conclusion.md), [derivation](../expeditions/046-growing-cross/derivation.md), [graveyard](../graveyard/2026-11-24-witness-independent-row-layout.md).

Code 6d632a3e was retrieved at its immutable commit and rerun in V8; complete parsed JSON equals the retrieved results. [Execution evidence](../expeditions/046-growing-cross/execution-evidence.md). No new CI or Lean acceptance, independent external review or novelty claim. Next #36; #8/#15 retain their scopes. Fresh approval required for another night.
