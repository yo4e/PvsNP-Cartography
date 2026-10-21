# Accepted generic profiles and actual polynomial application

Code9785a2705cc88efd372ab3de29a61007387bd91d, tree290f6b6e8196d2898d8612b0e1bbd0d2820462c7.
Completed SUCCESS run39615053307/job119273743612. Full actual log was retrieved
and inspected. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac; whole-root --wfail9052 jobs,
695 namespace declarations,26 new explicit target reports plus all old reports
within [propext,Classical.choice,Quot.sound]. See axiom-report.txt for actual
attributed timestamped excerpts, not a source-generated report.

Both complete source files were re-fetched at the accepted immutable commit:
HammingProfiles.lean blobbd1be55aa6605d53cbee78313af662dab5e10f60;
CliqueProfiles.lean blob22634fba45b6bf3089354a261fd9515ed33bc232.
The actual Git commit/tree was then fetched. Source assertions, queued runs,
finite Python checks and partial builds were not treated as acceptance.

The signed-real weighted sum uses a genuine partition of actual Hamming-layer
inputs through the previously proved overlap cardinality. Elementary symmetric
polynomials are actual MvPolynomial sums/products; their totalDegree and GF(2)
evaluation are proved before the q/r correctness formulas are used. See the
statement audit for precise quantifiers and empty-layer interpretation.

Rejected candidates e6fd5ff3 (extra tactic after a closed goal) and d65bfec7
(addition-order mismatch) had full completed logs inspected; graveyard028/030
preserve details. Candidate fd41fdf7 contains the same rejected profile prefix;
its own run was not inspected and no separate execution verdict is asserted.
The final repair changes only proof implementation, not any theorem or policy.

No local Lean, second proof kernel or independent external review of THESE new
modules occurred. Gemini #15 concerns the preceding pinned checkpoint only.
No all-n quadratic approximation, n12 degree result or novelty follows.
