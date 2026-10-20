# Actual formal acceptance and source correspondence

Approved session: 2026-10-21 JST. Code dc58ea7dd4d3e2ed36ca5b7d8276de651d95aa08,
tree17bb48e8d3c1e44db10fa09cc30934ae7abd1355.

[Formal run39510465687](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39510465687),
job118929907745, completed SUCCESS. The completed job status and entire job log
were fetched. Pinned Lean4.35.0-rc4 and Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8,
--wfail root build9048 jobs,589 namespace declarations within the unchanged
[propext,Classical.choice,Quot.sound] allowlist, and all29 new explicit targets
completed. Previous numerical and algebra targets were printed successfully too.
Actual timestamped excerpts are in axiom-report.txt. No project-specific axiom,
sorryAx, unchecked native decision, weakened statement or relaxed audit was accepted.

After the successful log was inspected, the actual source statements and Git
commit/tree were re-fetched at that exact code commit. Git blob identities:

| Source in formal/PvsNPCartography/ | Git blob |
|---|---|
| BalancedAffineCounting.lean | 48ce5f97ed03856c17554d524bd4b23ec1a63442 |
| BalancedAffineObstruction.lean | 8384c6e245ef779a580ea9ceb3618d3a8fbd92c0 |
| BalancedAffineBinomial.lean | 4e30d4ea65187121efaf1857541409373e05d2d3 |
| BalancedAffineInputMeasure.lean | ff01e87a09444e9d8fdeca61c9cec27bb471fe62 |

The formal acceptance is for the generic sample/count/evaluation/duality chain,
including genuine-degree-one impossibility for all integer n>=7. It is not
limited to the bounded range of verify.py. The separately named closed point-mass
formula for half-uniform Hamming layers is not implemented; #13 records it.
The accepted pushforward and all-function expectation identity do not assume it.

Independent exact computational evidence is recorded in finite-ci-evidence.md:
code317784842f82b6a1991db664ddd3734d08f72985, SUCCESS run39507686566/job118920623125,
normal/-O and saved/actual JSON equality. Source and result were re-fetched.
The local exact result was also canonicalized and its Git blob matched the
re-fetched result blob71fbfaee021e7fca312672310ddbb089b9ddd04f. No claim is made
that the locally formatted Python source is byte-identical to GitHub's source.

Six formal candidate commits were executed in this session: five failed
(including one dependent candidate) and this final candidate succeeded.
Full logs were inspected for four primary failed runs and the final successful
run; the intermediate dependent cf15c55 run39508392914 was observed as failed
through run metadata, without claiming its full log was inspected. See the
preserved failure records022..024 and the chronological session log.

Local Lean is absent; formal execution occurred in Actions. Independent human
semantic review (#8), a second kernel and a novelty assessment were not supplied.
