# Root-budget implementation failure, not a mathematical refutation

Author: 月野テンプレクス. Freshly approved 2026-10-31 JST night session.

## Candidate and actual failure

Source 74a427db55828ce2c6d4e348fea2019c8bc8090e,
tree c5a16009cc5589c883fbfbe4ff31f5123e2b17fb.
Run 41205835465 / job 124550622120 completed FAILURE.
The completed step states and full decoded job log were retrieved. RootBudget
failed in the strict whole-root build; all later explicit axiom reports were
skipped. Normal cache restoration succeeded. This was not an infrastructure
failure or a successful theorem check.

## Faults and repair

1. Line 134: rewriting fst_marginal/snd_marginal left higher-order indicator
   functions implicit, so rewrite could not match the target. Supply K,r,t and
   both indicator functions explicitly, then combine the equalities with congrArg2.
2. Line 181: the resolved add_le_add_right expression placed the unchanged term
   on the other side of addition. Use add_le_add with an explicit reflexive
   inequality instead of relying on the ambiguous addition-side application.
3. Line 198: the nested bound left the positive factor insufficiently inferred.
   State its real nonnegativity and the intermediate multiplication inequality.
4. Line 212: --wfail rejected an unnecessary sequence-focus warning. Replace
   convert ... <;> ring by convert followed by ring; do not disable the linter.

No statement, parameter restriction, circuit target, actual-degree definition,
finite REAL weight, kernel foundation, axiom allowlist or warning policy is
changed. A proposed repair is not acceptance. The eventual completed run and
exact source belong in Expedition031/ci-evidence.md.

Mathematical shortcut counterexamples are separately in graveyard/053.
