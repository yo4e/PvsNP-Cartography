# Conclusion — growing one-level cross, exact compact degree and a priced layout pivot

The scoped milestone of #35 is met by a parameterized mathematical construction, actual generated GF(128)/GF(512) compiler and an explicit degree/cost tradeoff for the named reference. The important change is not merely that the arbitrary-error radius grows; a different tag arrangement lowers the exact degree of the encoded honest proof, but its witness dependence and address cost make the general transfer unresolved.

| a | instance | AND | XOR | copies | used rows | templates | compact Q |
|---|---|---:|---:|---:|---:|---:|---:|
| 3 | YES | 2847 | 16699 | 2179 | 21845 | 79711 | 4194304 |
| 3 | NO | 2862 | 16709 | 2178 | 21869 | 79794 | 4194304 |
| 4 | YES | 12567 | 189066 | 11669 | 213600 | 817323 | 134217728 |
| 4 | NO | 12595 | 189074 | 11669 | 213636 | 817439 | 134217728 |

The written cross/B-recovery and private gate arguments give V_NO=2s^2-2s-3 and sigma=3s-1 for the constructed family. The generated costs and field controls reproduce the previous GF(128) census exactly. At GF(512), V_NO=477, sigma=47, and the guaranteed integer error radius is 10 (versus 4). The strict compact eta thresholds are 109/96468992 and 477/6308233216. General compact Q bounds are Omega(s^4 k) and O(s^5 k^2); radius Theta(s) is not improved error rate.

| a | compact exact and budgeted minimum over padding | disjoint odd parity cubes | equal-bank exact completion degree | equal-bank Q | unequal-prefix degree upper | unequal-prefix Q |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 17 | 16 | 15 | 67108864 | 16 | 67108864 |
| 4 | 20 | 64 | 16 | 8589934592 | 17 | 2147483648 |

Compact minima concern the fixed used honest proof, not every satisfying assignment. Equal-bank precision thresholds are 109/1543503872 and 477/403726925824; the a=4 unequal-prefix threshold is 477/100931731456. The latter saves fourfold storage against its equal-bank counterpart, not against the compact compiler. Exact lower-degree completion is meaningful even though the allowed error fraction gets smaller.

The basic coefficient layout gives a written family upper bound O(log k) on exact completion degree for the known honest reference, at Q'=O(s^7 k^2). Its finite first version used 2048x and 8192x compact Q; the separated banks repair much of that padding blowup. The new layout is not a witness-independent construction. The fixed-layout counting attack on arbitrary independent constant rows explains why the unrestricted generalization is false.

Verification: [check.js](check.js), [results.json](results.json), [execution-evidence.md](execution-evidence.md). The script checks actual reader/fanout/census identities, field/circuit agreement on the named controls, honest witnesses, direct odd parities, all occupied reindexed tags, reindexed honest/singleton failure counts, 72 local gate charge controls and a finite counting counterexample. Arbitrary-assignment and asymptotic implications use the separate [written derivation](derivation.md), not finite extrapolation. The inverse root with independently interpolated rows still rejects every seed when siblings are physically shared, at both sizes.

Next [#36](https://github.com/yo4e/PvsNP-Cartography/issues/36): seek a syntax-determined, witness-independent structural condition for a nontrivial constrained proof family, or a precise obstruction. Retain #8 and #15 unchanged. No new Lean verification, independent mathematical review, novelty, general lower bound, or P-vs-NP theorem is claimed. The full recursive family remains unpriced.
