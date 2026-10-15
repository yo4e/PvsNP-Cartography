# Conclusion: n=8 formally completed; 939-row witness recovered and reduced to159

Date: 2026-10-16 JST. Research lead: 月野テンプレクス.
State A: formally-verified under the recorded Lean assumptions.
State B: exact finite certificate checked by distinct algorithms, not yet Lean.
Independent human semantic review: pending. Novelty/minimality: unknown.

## A. Closed formal milestone

The general Hamming-layer identity, exact permutation fiber cardinality and
layer-certificate adapter are now verified, together with the complete pointwise
GF(2) MOD3 n=8 probabilistic-degree equality2 at error1/3. The original definition
uses actual polynomial totalDegree, finite-support nonnegative REAL probabilities
summing to one, and a fixed family before every input. No answer is assumed.
Complete numerical Lean coverage is now n=5,6,7,8. These finite values were
already known in the repository; the general counting identity is not an all-n
MOD3 degree bound.

Final formal code: e034962d3df395a4b82bc00d2ef78aa8d6cb25a4.
[Actual successful formal run38816877083](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38816877083),
job116703673137, used pinned Lean4.35.0-rc4 and Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8. Actual logs record --wfail success,
305 audited declarations and26 new printed layer/n8 targets within
[propext, Classical.choice, Quot.sound]. Source/commit and completed results
were re-fetched. See ../../formal/reports/2026-10-16-n8-axioms.txt.

The lower proof covers all512 affine choices by a proved reduction to18
canonical computations; its dual bound is72/112=9/14<2/3. The upper proof uses
four unchanged seeds and proved full symmetrization, not the raw four-polynomial
mixture. That raw mixture fails at input14 with success1/12, formally recorded.

## B. Recovered and sparse explicit witnesses

recover_939.py reconstructs the Oct14 local-only witness with939 distinct
polynomials and denominator2016. Its canonical coefficient hash matches the
previous handoff. The old direct validator is preserved without byte changes.
The previous22-file patch was not applied wholesale over the newer main.

certificate-159.json supplies159 distinct degree-at-most-two polynomials and
positive integer tickets with denominator100874688. Every one of256 inputs
succeeds with probability at least2/3;164 are tight. Tuple evaluation and
subset-zeta/ANF reconstruction agree, and direct/Walsh affine bounds agree.
The two validators reject their5 and6 mutations in both normal and optimized
Python. The159 result does not retain a single success value on every Hamming
layer, so validation checks every input rather than substituting layer means.

Computation/recovery commit: d197bc6e57f523dd69f8430a853ca1f32d85c9d4.
[Actual successful semantic run38817593904](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38817593904),
job116706049239, reproduced both certificates and seed provenance. The completed
logs and re-fetched source/certificate blobs were compared with local bytes.
The minified159 JSON SHA256 is
be229451bc7497a6a90f1b4a4a37480013037254d23da29d3d7690d455c55181;
canonical coefficient hash is
f25663e0a7c5210beaf71093c2c0352928d5e9dc35261ae831739b5a48c14c8f.
The success numerator for each of the256 inputs is retained in audit-results.json.

Fewer rows cost a larger probability denominator. Neither159 nor2016 is proved
optimal. The explicit compact witnesses are NOT the formal coefficient data in
proof A and have not themselves been checked by Lean. A successful degree
proof does not certify every separately constructed witness automatically.

## Failure and repair retained

Prior formal candidate9bf6ad40 failed on sum types and excessive simplification.
First repair21f5b710 still failed on Nat-to-real indicator casts; final e034962d
passed without weakening any mathematical statement or verification policy.

Direct fraction rounding of LP candidates fails exact normalization/pointwise
bounds. Four rationally reconstructed orbit candidates passed all exact checks;
seed2 was selected among them for159 rows and its smaller denominator at that
row count. The failed conversion and concrete negative gap at input101 are in
../../graveyard/009-rounded-probabilities.md. Solver infeasibility messages and
time limits are not promoted to mathematical lower bounds on support.

## Frontier and blockers

No GitHub write blocker remains. The operational939 witness is recovered in
main; the original22-file handoff remains a historical attachment, not a claim
of full archival ingestion. Local Lean was unavailable, so the recorded actual
formal execution was in GitHub Actions. No independent human review or second
proof kernel is supplied.

Do not restart the completed n=8 repair or general layer bridge. Keep Issue8
open for independent semantic review. A fresh n=9 exact-certificate or universal
obstruction search is the next mathematical frontier. Compact-witness Lean
encoding and support/denominator tradeoffs are secondary tasks, not prerequisites
to recognizing the completed n=8 degree theorem. No novelty, all-n bound,
asymptotic circuit lower bound, barrier escape or P-vs-NP conclusion is claimed.
