# Current checkpoint: actual agreement dimension and real-mixture obstruction

Approved2026-10-24 night; executed after midnight2026-10-25 JST and completion
record recovered in the same conversation on Oct25 morning after a failed final
response. Research lead 月野テンプレクス. **Issue18's mathematical milestone is
complete; Issue19 is the next bounded frontier.** Future nightly work requires
fresh approval. Dated README/direction snapshots do not restart completed work.

## Accepted mathematics

For arbitrary field K, nonzero a,b and actual polynomial R of total degree<=d,
the actual agreement set with product_i y_i on {a,b}^n has cardinality at most

 B(n,d)=sum_{j=0}^{min(n,floor((n+d)/2))}choose(n,j).

AgreementDimension derives this from explicit interpolation, degree-preserving
squarefree evaluation reduction, existing TwoPointCompression and dimension
counting, not an assumed surjectivity/rank bound. AgreementConsequences also
handles a=b by the singleton-grid case. Distinctness is needed for the2^n input
count, not for the cardinality inequality itself.

For any fixed finite nonnegative normalized REAL mixture of actual degree<=d
K-polynomials, total grid correctness<=B(n,d). With a!=b, pointwise success>=eta
therefore implies eta*2^n<=B(n,d). This accepted target is the coordinate PRODUCT,
not yet the original GF2 MOD3 predicate. Coefficients and probabilities live in
different fields; input-dependent selection and signed mass are excluded.

## Evidence

Accepted source8e5be8ce59b069c278ec32839552dad712de04e1,
tree474f4a9a18940dcba367416d3136ece1990af624. Completed SUCCESS
run40108908554/job120916298894: pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
whole-root --wfail9057 jobs,812 namespace declarations in unchanged
[propext,Classical.choice,Quot.sound],21 new target reports. Full actual output,
completed job/steps, both modules and matching Git commit/tree were re-fetched
and inspected during recovery. Expedition025 preserves conclusion, statement
and barrier audits, ci-evidence.md and timestamped axiom-report.txt excerpts.
This is the existing kernel, not a second kernel or independent semantic review.

Exact sourcea62add7e08387a4231f7092f108b59964a00feca passed completed
run40107805754/job120913025271. Normal/-O and actual/saved results match;
11,910 polynomial cases across GF3/GF4/GF5,971 independent rank controls and
22,230 reduction evaluations corroborate but do not prove the general result.
Graveyard039/040 preserve implementation failures, mathematical countercontrols
and the corrected distinctness wording. All earlier failure records remain.

## Next: Issue19, actual GF2-to-GF4 transport

Expedition025/next-bridge.md derives a same-index coupling of two residue
restrictions, linear GF4 encoding and affine input-grid transport, aiming to
preserve degree D and obtain success>=1-2delta. Formalize actual polynomials,
field/root existence, evaluation, degree and real probability bounds, then apply
the accepted product-mixture theorem. Do not merely assume its desired inputs.
No independence is needed BETWEEN THE TWO RESIDUES. Independent samples remain
necessary for the separate majority15 amplification, which is still unformalized.

The n>=299 degree2 exclusion remains an author-reconstructed candidate, not an
end-to-end Lean theorem, independent review or optimal-threshold claim. Numerical
exact degree2 n5..11 and generic affine exclusion n>=7 remain unchanged. General
n12 degree is unresolved. No novelty, new circuit result, barrier escape or
P-vs-NP conclusion follows. #8/#15 retain separate, older nonblocking review scopes.

No write blocker or unapplied patch remains. Local Lean is unavailable; accepted
execution used Actions. Source PDF parsed text was read; failed screenshot
requests are not visual inspection. Prior status is preserved byte-identically
at history/2026-10-25-pre-agreement-status.md, blob716952a1805128bfab88b630b32e632a8491e9bf.
Session log: ../logs/2026-10-24-night-agreement-dimension.md.
