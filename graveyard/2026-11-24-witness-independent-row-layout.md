# Failed direction — witness-independent low-degree tags for unrestricted affine rows

Claim under attack: a public fixed tag assignment of polynomial storage can always encode a large collection of affine-in-seed rows by a polynomial of degree O(log k) at the growing cross's raw error radius.

Attraction: a coefficient tag for an affine row makes it a degree-two function of tag and seed variables; most rows of the named honest YES reference are affine.

Failure: coefficient labels depend on which row function the witness supplies. Fix t tag bits and R occupied tags, and vary R constant rows independently. At seed zero a degree d polynomial restricts to a degree d tag polynomial, giving at most 2^D distinct patterns, D=sum_{j<=d} binom(t,j). With <=e errors its cover has size <=2^D sum_{j<=e} binom(R,j). For t=O(k), d=O(log k), R exponential in k as in the compiler and e=O(s)=O(2^(k/2)), the log of this cover is o(R). Therefore there exist constant-row assignments outside all the balls. Mixtures do not evade an existential mean-error threshold. The finite t=3,R=8,d=1,e=1 check gives 16 affine tables, 144 covered, 112 uncovered (see results.json).

Scope: independent arbitrary constants, not a lower bound over constrained satisfying assignments. No conclusion about general PCP proof layouts follows without showing the needed independence or other obstruction among actual satisfying witnesses. Salvage: seek a public structural invariant specific to a nontrivial witness family.

Separate cost failure: the initial common-rank coefficient bank needed 2048x and 8192x the compact storage for a=3,4 because repeated constant rows forced a large rank field across all signatures. Separate banks recover much of that loss, with remaining overhead 16x/64x or 16x for the larger unequal-prefix variant. Equal-valued rows were not merged; such a merge would alter the proof space and requires fresh sensitivity/soundness accounting.

Do not use either the favorable finite examples or their explicit known YES reference as evidence for a uniform unknown-witness approximation theorem.

Follow-up in [Expedition047](../expeditions/047-witness-layouts/conclusion.md):
this remains a **fixed-layout** obstruction. A witness-dependent value/rank
map can encode arbitrary constant rows at degree one, but its explicit table
carries the witness information and costs too much in the growing compiler.
One shared guessed map preserves NO soundness. A separate scoped obstruction
now covers genuinely satisfying shared-RS code-only witnesses, without
claiming to refute existential completeness. These distinctions correct the
overbroad inference that witness dependence itself invalidates every route.
