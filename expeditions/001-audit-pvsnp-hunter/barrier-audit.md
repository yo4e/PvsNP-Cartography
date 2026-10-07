# Expedition 001 — Barrier Audit

Status: **completed for the audited finite-degree claims**

This expedition audits a neighboring project's finite computations. It does not propose a route to P vs NP, so the three famous P vs NP barriers are mostly scope checks rather than obstacles to a new proof.

## Relativization

No separation of P and NP is claimed in this expedition.

The audited p-vs-np-hunter findings discuss restricted circuit classes and finite-field polynomial methods. Reproducing or refuting those finite tables neither yields nor assumes a relativizing P-vs-NP argument.

**Disposition:** not directly triggered.

## Natural Proofs

This expedition does not define a large, constructive, useful property of Boolean functions and does not infer a general circuit lower bound from one.

The target project's prose conditionally connects degree patterns to ACC0[p] hardness. That connection would require a precise lower-bound theorem with its own hypotheses; a finite table is not by itself a Natural-Proofs escape or collision analysis.

**Disposition:** not directly triggered by the audit; any future promotion from a property/degree measure to broad circuit lower bounds requires a separate Natural-Proofs check.

## Algebrization

The expedition studies a finite-field polynomial method, but it makes no P-vs-NP proof claim and therefore does not claim to escape algebrization.

Using algebra is not evidence of escaping the algebrization barrier.

**Disposition:** not directly triggered.

## Other restrictions that are directly relevant

### Quantity fidelity

The central barrier in this expedition is more elementary than the famous proof barriers: the implementation must compute the mathematical quantity named in the prose.

It does not do so uniformly:

- non-graph functions use hard-coded formulas and extrapolation;
- graph functions compute exact multilinear algebraic degree;
- an unused helper implements a separate average-misclassification search and truncates its monomial basis.

A mixed table cannot inherit one mathematical interpretation merely because all rows are integers called “degree.”

### Encoding fidelity

A complexity measure of PHP is meaningful only after a Boolean encoding is specified.

The audited degree estimator never constructs a PHP Boolean function. The only PHP-specific operation on its active path is a hand-written formula. The repository has a separate PHP CNF generator in its SAT component, but that encoding is not consumed by the degree estimator.

### Transfer-theorem fidelity

Smolensky's polynomial method proves lower bounds through an explicit chain relating bounded-depth circuits, finite-field polynomial approximations, approximation error, and a hard target function.

Primary source:

Roman Smolensky, *Algebraic methods in the theory of lower bounds for Boolean circuit complexity*, STOC 1987, DOI `10.1145/28395.28404`.

The audited code does not implement or verify a transfer theorem from its PHP sequence to an ACC0[p] size lower bound. The target project's public prose itself acknowledges that such a theorem-level transfer is still required.

## Expedition checklist result

```text
Relativization:      Not directly applicable; no P-vs-NP separation claim.
Natural Proofs:      Not directly applicable to the finite-table audit.
Algebrization:       Not directly applicable; algebraic technique != barrier escape.
Other restrictions:  Quantity mismatch, encoding mismatch, missing transfer theorem.
Unclear points:       Which precise approximation notion the original authors intended.
```

The barrier audit therefore does not rescue or kill the target findings. The decisive findings come earlier: provenance, definitions, exact tiny-instance counterchecks, and encoding.
