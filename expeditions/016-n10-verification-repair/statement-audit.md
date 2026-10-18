# Post-repair statement audit: preserve the theorem, change only evaluation

Evidence: production code1739ccfa2ebe5997e568135cdfacf06e9f6d1f87 and completed
formal run39139432083/job117710608870; separate exact semantic run39139432110/
job117710608842. Actual full logs and production statements/commit re-fetched.

The only Lean diff from the old n10 candidate is one proof body:
`decide +kernel` becomes `intro w; fin_cases w <;> decide +kernel` for
layer_tickets_exact. Every declaration's statement and all data are unchanged.
The separate finite-result file changes only the source-hash field, not its
expected numerical output. The diagnostic candidate SHA256 equals production.

The target remains the GF(2) indicator of weight divisible by3 on the entire
Boolean cube, including weight0 and10. Fin11 accounts for ALL possible weights;
fin_cases is exhaustive case elimination, not a sampled list of layers.

Upper chain: actual MvPolynomial degree/evaluation -> seed_correct/seed_success
-> all11 layer_tickets_exact -> seed_layer_bound -> full-permutation layer
adapter -> degree_two_feasible. The REAL mixture is fixed before every input;
the old raw seed mixture is formally refuted at mask832, success1/50.

Lower chain: normalized full-cube input mass ->22 canonical checks -> proved
coefficient-permutation coverage of2048 affine rows -> structural normal form
for arbitrary totalDegree<=1 polynomials -> no_degree_one_family for arbitrary
finite REAL mixtures. Strict bound19/30<2/3 is proved, not an optimizer estimate.

Endpoints: feasible_degree_iff, least_feasible_degree and pdeg_eq_two have actual
upper and lower proofs. No existence assumption merely restates feasibility.
The root build and all420 namespace declarations passed the unchanged
[propext,Classical.choice,Quot.sound] allowlist; all15 explicit n10 reports also
passed. No accepted sorryAx, project axiom or native_decide is hidden by naming.

The prior shutdown cause is NOT established by this successful repair. The
failed CBV alternative is kept separate in graveyard017. This same-author
semantic audit is not independent human review and does not establish novelty.
