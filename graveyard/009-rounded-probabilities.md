# 009: directly rounded LP probabilities are not an exact certificate

Date: 2026-10-16 JST. State: refuted for the recorded conversion, repaired.
Role: skeptic/experimentalist, same author. Not a global impossibility theorem.

## Temptation

A floating LP returns apparently normalized nonnegative probabilities and
success numerically equal to2/3. Replacing each float by a nearby fraction and
calling the result exact is tempting. Active constraints leave no slack to
absorb independent rounding errors.

## Concrete failed conversion

Use expeditions/010-n8-recovery/reproduce.py with seed2 and the pinned local
numpy2.3.5/scipy1.17.0/sympy1.14.0 environment. The search uses134 translation
orbits in the recovered939-row support. Convert selected LP weights using
Fraction(float(weight)).limit_denominator(10**7), then divide each orbit mass
uniformly among its members. The resulting exact total probability minus1 is:

```
-22131449544520134460945039411659928244709506854718173255305069093493 /
1270126618825184556452346715683942831564596162367622485088320323161352464268307536
```

At input integer101, the exact success minus2/3 is:

```
-318075497422635144633400357 /
7247745402695991991725630606240511074952
```

Both errors are nonzero, and the latter is negative. A tiny violation is still
a violation of the requested statement. Renormalization alone would require
another full inequality check; it is not a proof of repair.

## Repair

Floating arithmetic selects positive support and candidate tight constraints
only. Solve an independent subsystem of the integer normalization/correctness
matrix over exact rationals. Verify consistency of all selected equations,
strict positivity, exact normalization, and ALL256 pointwise inequalities.
Seed2 then yields26 selected orbits,159 rows, denominator100874688 and an exact
minimum2/3. Two separate standard-library validators and CI reproduce it.

Search accounting: five unrestricted LP objective probes and four orbit probes
failed naive rational conversion. All four orbit candidates survived exact
reconstruction. This records search volume, not independent discoveries.
Small-denominator MILP attempts at24 and48 returned infeasibility messages;
96 hit its time limit without a usable witness. These optimizer statuses are
NOT exact support/denominator impossibility certificates.

## Lesson and scope

Use numerical search to choose candidates, exact arithmetic to accept them.
The example refutes this conversion of this candidate, not every rounding
method, every LP solution, a159-row optimum, or every smaller-denominator
construction. Different solver versions can select different vertices.
No mathematical threshold, probability definition or Lean axiom policy was
weakened to retain the final candidate.
