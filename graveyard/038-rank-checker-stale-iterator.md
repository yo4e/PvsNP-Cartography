# A green rank checker that read stale pivots

Discovered by author adversarial source audit during approved2026-10-23 session.
Affected checker: Expedition024/verify.py at de8913e7c1058844354f376ae8a72a2a2abddfa9.
Its exact run39964233049/job120449783272 succeeded, but that alone did NOT
validate the rank algorithm. Do not cite that run's rank checks as accepted evidence.

## Defect and concrete counterexamples

The loop `for j,c in enumerate(row)` kept iterating over the ORIGINAL list even
after elimination rebound `row` to a newly reduced list. Later c values were
therefore stale. Explicit execution showed:
- [[1,1],[1,0]] returned1 instead of2;
- [[1,1],[1,1]] returned2 instead of1.
Thus it could both lose real pivots and invent pivots for dependent rows.
The structured polynomial matrices happened to pass, hiding the defect.

## Repair and independent controls

Iterate over column indices and read c=row[j] from the current row after every
elimination. Add both counterexamples and exhaustively compare all256 GF4
2x2 matrices against the independent determinant/nonzero-entry rank formula.
The repaired checker again passes18020 polynomial-rank cases and53942 actual
compression evaluations. Normal/-O agree locally; remote acceptance must use
the NEW source and completed run, not transfer the old green status.

This was a verification-implementation defect. It changes neither the Lean
compression proof nor the written dimension proof. The binomial/majority
calculations are rerun too. It reinforces why tests, kernel acceptance,
statement fidelity and independent review are separate evidence classes.
