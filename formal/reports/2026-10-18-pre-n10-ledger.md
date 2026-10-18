# Formal assumption ledger

## Current formal checkpoint: 2026-10-16 JST, n=9 verified

n=9 closes the standard GF(2), error1/3 MOD3 probabilistic-degree equality with an actual fixed finite REAL distribution over totalDegree<=2 MvPolynomials, and universal exclusion of all degree<=1 real mixtures. The existing full variable-permutation/Hamming-layer identity (arbitrary finite arity) supplies the upper bridge. Lower normalization 504 and affine bound322 use 20 canonical kernel checks plus proved permutation coefficient transport and degree-one normal form.

Exact audited code807124110f0fc1861504f9ea0bd6fd971a78992e, source blob32428657909833b00103c85f3656708a08c64678; successful [formal run38908696378](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38908696378), job116998734457. Pinned Lean4.35.0-rc4, Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8, --wfail build,356 namespace declarations audited,14 explicit n9 #print axiom targets inside the unchanged [propext, Classical.choice, Quot.sound] allowlist. Attributed actual output in [2026-10-16-n9-axioms.txt](reports/2026-10-16-n9-axioms.txt). No project-specific axiom, sorryAx, admit or native_decide dependency introduced.

Numerical strict minimum85/126 and the alternative 1260-polynomial partition family were separately validated by normal/-O exact Python, test code a529afed, run38909099839. Those are not separate Lean encodings of the expanded compact coefficients. The restricted <=3-block single-orbit search of7432 candidates gives only ONE successful pattern in that class, without global support minimality. Independent human semantic review and second kernel remain outstanding.

Complete formal numerical degree equalities now cover n=5..9. n>=10 and any asymptotic P-vs-NP claim are UNPROVED. New result status: formally verified as stated, novelty unknown.


Current checkpoint: **2026-10-16 JST**. Complete degree-based MOD3 equalities
for n=5,6,7,8, generic full symmetrization, and the Hamming-layer mean/fiber-count
interface are verified under the recorded Lean assumptions. Independent human
semantic review remains pending. Compact939/159-row witnesses are separately
checked finite data, not yet separate Lean-formalized coefficient witnesses.

## Policy and reproduction

No project-specific extra axiom is accepted. The compiled namespace audit
permits only propext, Classical.choice and Quot.sound. Closed finite checks
use decide +kernel, not native_decide. The --wfail policy, heartbeat settings,
coefficient data, success thresholds and allowNonModules compatibility setting
were not weakened in the final repairs.

From formal/:

```bash
lake build --wfail
./scripts/axiom_report.sh
```

The script prints AxiomAudit.lean, SymmetryAxiomAudit.lean and LayerAxiomAudit.lean.
Axiom reports below are actual retrieved output, not source-string searches.

## Actual verified checkpoint

Code: e034962d3df395a4b82bc00d2ef78aa8d6cb25a4.
[Formal run38816877083](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38816877083),
job116703673137, completed successfully under pinned Lean4.35.0-rc4 and
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8. Actual output records --wfail,
305 namespace declarations inside the allowlist, and26 new layer/n8 printed
targets, all using only the same three foundational axioms.

[Actual target excerpt](reports/2026-10-16-n8-axioms.txt),
[statement audit](../expeditions/010-n8-recovery/statement-audit.md),
[layer conclusion](../expeditions/009-hamming-layer-bridge/conclusion.md),
[session conclusion](../expeditions/010-n8-recovery/conclusion.md).

HammingLayers proves the full permutation mean equals the uniform Hamming-layer
mean for arbitrary real scores, including empty variable sets and extreme weights.
LayerCertificates derives exact fiber cardinality and adapts layer bounds to the
unchanged pointwise degree predicate. The averaging theorem does not assume the
fiber count it is later used to derive.

Mod3EightDegree uses unchanged four seeds and full symmetrization for degree<=2.
The lower proof establishes arbitrary degree<=1 coverage via the structural
normal form and proved coefficient-permutation invariance, reducing512 affine
choices to18 canonical kernel computations. Its full-cube dual score is bounded
by72/112=9/14<2/3. Actual degree, GF(2) evaluation, real probability normalization
and family-before-input quantifiers are retained. Feasible_degree_iff, IsLeast
and pdeg_eq_two have proved existence, not assumed feasibility.

Re-fetched source blobs:
HammingLayers7261f29623c7c9fda84dbc7af9b89fc02c31fb49;
LayerCertificates1ab2fe1f542091fc85013d293694a5c3932c4e8a;
Mod3EightDegree ec288bf49be783ad6ab88954222019247389ce57.
The actual completed CI result and code commit/tree were retrieved separately.

## Failure and verification boundary

Prior candidate9bf6ad40 failed on a natural/field sum mismatch and excessive
concrete simplification. Repair21f5b710 still failed on indicator casts.
Final e034962d fixes proof steps only. Failed commits and actual failure IDs
are retained in the Expedition010 log; no failed build was called verified.

The159-row certificate is checked by two exact normal/-O Python validators in
run38817593904/job116706049239 at d197bc6e57f523dd69f8430a853ca1f32d85c9d4.
It is NOT the formal four-seed/full-permutation witness above. Its support is
smaller than the recovered939 rows but its probability denominator is larger.
No support minimality, denominator optimality or novelty is established.

Complete numerical Lean coverage is n=5,6,7,8. No n>=9 value, all-n MOD3 degree
bound, asymptotic circuit lower bound, barrier escape or P-vs-NP result follows.
Independent human semantic review and a second proof kernel were not supplied.
The local container lacked Lean; actual formal execution was in Actions.

## Preserved historical ledger

The previous ledger is preserved byte-identically as
[2026-10-16-pre-n8-ledger.md](reports/2026-10-16-pre-n8-ledger.md),
Git blobabbbc56fd87150e955f80f09e2671aa2d0aa0a08. Its pending statements describe
the Oct13 checkpoint, not the current state. It links the older pre-symmetrization
ledger and all original attributed reports. No historical proof artifact or
failed research direction was deleted by this update.
