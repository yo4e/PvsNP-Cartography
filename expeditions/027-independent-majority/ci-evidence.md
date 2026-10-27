# Actual execution and source evidence

Approved session executed2026-10-28 JST. Research lead 月野テンプレクス.
Persistence, finite computation, kernel acceptance and independent semantic
review are separate evidence classes. The final record-only commit is not the
source of a new formal execution; use the exact source below.

## Accepted formal execution

Source:79c52432c82406b0a692a079adab147402dbbbe0
Tree:b7e508b227252cf0bac4b4d45fbac0706cc84ad9
Run:https://github.com/yo4e/PvsNP-Cartography/actions/runs/40536961983
Job:122304691322, completed SUCCESS.

All required steps completed successfully: checkout, Elan, pinned dependency
resolution, whole-root build and namespace axiom audit, existing axiom reports,
TransportAudit.lean, and MajorityAudit.lean. The completed job/steps and full
decoded actual output were retrieved and read after completion. The job's actual
checked-out SHA equals the re-fetched Git commit and tree. All five new source
modules at that SHA were re-fetched completely and compared with local Git blob
hashes. This is not a claim inferred from a green icon or a partial build line.

Actual execution:
- lake build --wfail:9065 jobs, successful.
- namespace axiom audit:984 declarations under PvsNPCartography, all within
  [propext,Classical.choice,Quot.sound].
- all27 new explicit #print axioms reports completed, plus all earlier reports.
- pp.explicit=true output confirms the final target's arity n, original
  HasProbabilisticDegreeAtMost, epsilon1/3 and total-degree bound2.
- no source sorry/admit/new axiom/native_decide, no warning-policy relaxation.
  Local resource and definitional-transparency settings do not bypass the kernel.

## Resolved environment, not assumed current tags

Lean4.35.0-rc4, commitc29b6dda4f7c20e3eeaa717c4e565663c5cfa364.
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Lake5.0.0-src+c29b6dd.
Ubuntu24.04.5, runner imageubuntu-24.04 version20261012.334.1.
Runner2.338.0; provisioner20261021.618; git2.55.0.
checkout@v4 resolved11d5960a326750d5838078e36cf38b85af677262.
lean-action@v1 resolvedfe408643ea7367d8c0404a8be3975bb145f5fb64.
cache action resolvedcaa296126883cff596d87d8935842f9db880ef25.
axiom-audit v0.1.2 resolved46024e005996495c65ef609368e11ab39c4222e3.
The floating lean-action revision differs from the preceding session; its actual
output still uses the unchanged --wfail and foundational axiom policy.

Dependency revisions printed in the actual manifest:
plausible aef59637faa9e85fa2486acaaf906ce3f572af7c;
LeanSearchClient234d9e074fbd6e911b920baf32db5291c3125be0;
importGraph579f558774c4ac6840e715ba60dabf3030619349;
proofwidgets d5ad4a0b79fa7f9818fe1380d05a3f6143823c09;
aesop04879b1e1de744d5c9777c8cf63fa55a8f652e5e;
Qq e7c4cdd2f1bf9df361ef7f621b4d6867012ab65e;
batteries b71aaf60877e673fdb921f06f20987d12ee8a290;
Cli82c11b9717083154aefc5fe8d4cba4bbf046298f.

Normal .lake caching restored from the preceding checkpoint9437b373. This is
not a clean-cache or clean-room execution. No container digest is claimed.
leanchecker, lean4checker and nanoda were disabled; no second kernel ran.

## Exact retrieved source fingerprints

IndependentTrials.lean:7280 bytes, blobbf85bda8cb8d22750a5cb60c0e68e18f95591212.
MajorityAmplification.lean:7340 bytes, blob24ca75b46d3dd5a988cb06fa669b6ef43362cc7e.
MajorityNumerics.lean:2533 bytes, blob4bc6f941e521b1845e68cf29f0ae7fd68615260b.
Mod3Restrictions.lean:2911 bytes, blobe8b2b5e56a836bdfca8d5d3ffd1897c3a70c1b4d.
Mod3QuadraticObstruction.lean:1035 bytes, blob3ae81b68e2f7d00747bcc3302bfa7af350cd3d9f.

A supplementary naive lexical screen initially matched the word axiom in a
comment explicitly denying a numerical axiom. A comment-aware screen and direct
source inspection found no proof-hole declarations. This screening false positive
is not a mathematical or Lean defect, and the real namespace axiom audit above
is the stronger evidence. Source hashes were checked again at record time.

## Exact finite controls

Source80757ad411675e02aea96c426bc383619e7c9579,
treea2567e66b07844f44e879eb3497ccd65c9a995a0.
Run:https://github.com/yo4e/PvsNP-Cartography/actions/runs/40535117682
Job122298162510, completed SUCCESS. Full decoded actual output was retrieved.
Python3.12.3; python verify.py and python -O verify.py outputs are byte-identical;
parsed actual output equals the committed result.json. Local reruns also match.
Checker blob07ed082062d8c97a8fa0703dfe536c6c32b143f4;
result bloba5c801a329104aeded16393144a71303104da0db.
The actual commit, checker and saved result were re-fetched and inspected.

Controls:27916 tuple evaluations;972 three-way failure-law comparisons;
3800 tail comparisons;32768 majority truth inputs and6435 degree8 ANF terms;
39 actual polynomial families,147 composition input checks,1035 zero-restriction
checks;45451 Pascal/multiplicative binomial coefficients. The degree24 example
comes from an explicitly included degree3 source, consistent with degree8*d.
Finite exact tests corroborate and refute variants, but are not the universal
formal argument. The formal proof imports none of their results.

The added check_frontier.py and frontier-checks.json were run locally in normal
and -O modes with matching output, with a further local rerun at record time.
They are NOT covered by the completed exact CI above, nor by the accepted Lean
source. Their candidate growing-degree argument remains unformalized.

## Failures, archives and trust boundary

Four completed formal failures were fully retrieved and inspected:
f3a5599d/run40531874680/job122286578853;
d2cede2c/run40533297666/job122291663655;
088bd61c/run40534788715/job122296987803;
eb8e503c/run40536001033/job122301279401.
The last had only warnings but did NOT reach its axiom audit; it is not acceptance.
Graveyard043 records their causes and faithful repairs. Graveyard044 records
mathematical counterexamples, including the nonmonotone n299-to-n300 gap.

axiom-report.txt and exact-output.txt are attributed ACTUAL OUTPUT EXCERPTS.
The full decoded logs were read but are not committed as full raw archives.
No independent semantic reviewer was available; statement-audit.md is explicitly
same-author adversarial analysis. Existing older reviews do not cover this code.
No novelty, optimal threshold, exact degree3, n12 resolution, unrestricted circuit
bound, barrier escape or P-versus-NP conclusion follows from this acceptance.
