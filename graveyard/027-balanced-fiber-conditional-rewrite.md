# Second rejected fiber candidate: explicit conjunction rewriting

Code2404af3d4b73e82f8f139d922db5a9b4bfa9bc40, completed FAILURE
run39547284945/job119048214934. Full completed log fetched and inspected.

The new independent HammingIntersections module built successfully in6.1s,
but the combined root build failed before namespace/target audits. Do not
promote that module based only on the partial green build line.

The point-indicator use of inputMass_mean repaired the previous dependent
conditional type mismatch. The remaining failure is one triple summand proof:
`simp only [hd,...]` did not eliminate the positive Distinct conjunction and
left `Distinct i j k ∧ True/False` in conditional expressions. Unused simp
arguments also violated --wfail. Actual excerpt:
```
2026-10-21T05:04:50.3590826Z ✔ [9047/9050] Built PvsNPCartography.HammingIntersections (6.1s)
2026-10-21T05:04:50.4612267Z error: PvsNPCartography/BalancedAffineFibers.lean:132:41: unsolved goals
2026-10-21T05:04:50.5920487Z ##[error]Process completed with exit code 1.
```

Repair candidate replaces only that tactic block with explicit ite_eq_left/
ite_eq_right applications, giving direct proofs of the conjunction or its
negation. No statement, range guard, count, probability, old definition or
axiom/warning policy changes. This is not a mathematical refutation. A completed
later root build and both audits are required before formal promotion.
