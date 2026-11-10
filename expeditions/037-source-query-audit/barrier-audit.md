# Scope of the source-level calculation

The input here is a concrete finite verifier, an honest proof satisfying each signed test, and a specified distribution over complete proof addresses. The output is a bound or counterexample for passing uniform approximation error to test rejection. Mean error over language inputs can still concentrate on the single input later fixed by the counting algorithm.

- **Relativization.** The copy and fiber calculations use the verifier's finite maps and work for any fixed such maps. They provide no machine simulation or diagonalization separating oracle classes.
- **Natural Proofs.** There is no truth-table property with a largeness, constructivity and usefulness estimate against general small circuits. Enumerating small polynomials only tests the stated finite examples.
- **Algebrization.** Substitution and the local row calculation use characteristic two. Neither controls a verifier with algebraic-oracle access. No barrier-escape inference follows.

The relevant unresolved step for the original counting argument is quantitative: recover enough distinct random bits in the final full address and obtain sufficiently small error after hardwiring the input. The prior Lean checkpoint concerns a different, fixed-proof counting adapter.
