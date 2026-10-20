# Rejected generic obstruction integration, precise remaining defects

Candidate290fd53ca91e9d28b6d15aac4ea9e770c9c4ae22; completed FAILURE in
run39508917678/job118924741871, exit1 at2026-10-20T22:36:22.7060940Z.
The full completed log was fetched. No namespace or target axiom audit passed.

The counting prefix now elaborated but --wfail rejected an unused one_mul
simplifier argument. The obstruction file had three remaining implementation
problems: the positive distinct-triple branch failed to eliminate conditional
masses; the inequality used a differently ordered addition from the target;
and fin_cases produced explicit Fin constructors not immediately matched by
rewriting the literal-zero/one score lemmas.

The repair removes only the unused simplifier argument, names the exact
conditional mass identity, rewrites its positive branch explicitly, unfolds
the score/envelope before linear arithmetic, and states the Fin2 branch goal
explicitly. It does not weaken any theorem, threshold, REAL normalization,
quantifier, compiler warning policy or axiom allowlist. This failure is not a
counterexample to the mathematical counting argument.

A dependent earlier cf15c55 candidate included the preceding failed counting
prefix; its separate execution must not be presumed accepted. Full successful
production verification is still required after all repairs and binomial/
pushforward integration. Finite exact CI success is a separate evidence class.
