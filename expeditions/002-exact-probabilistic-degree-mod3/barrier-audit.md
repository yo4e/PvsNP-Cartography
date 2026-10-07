# Barrier audit — Expedition 002

Status: **finite restricted computation; no P-vs-NP transfer claimed**

## Relativization

This expedition proves only exact finite values of a Boolean-function complexity measure for three input lengths.

No oracle Turing-machine argument is used and no statement about P versus NP follows.

Therefore there is currently no proof route whose relativization behavior could settle P versus NP. Any future attempt to transfer these finite values into a class separation would require a separate theorem and a fresh Baker–Gill–Solovay audit.

## Natural Proofs

The current objects are explicit finite certificates for probabilistic degree.

They do not define a large constructive property useful against general circuit classes, and no superpolynomial circuit lower bound is claimed.

If a later route proposes turning a probabilistic-degree property into a general Boolean-circuit lower bound, the repository must explicitly test constructivity in truth-table length, largeness, usefulness, and the relevant cryptographic assumption.

## Algebrization

The certificates use polynomials over GF(2), but “uses algebra” is not the Aaronson–Wigderson notion of algebrization.

No oracle-extension argument or P-vs-NP separation is present here.

Any future transfer from probabilistic-degree bounds to a class separation must be audited against the asymmetric algebrization definitions rather than merely labeled nonrelativizing.

## Current conclusion

No barrier is “escaped.”

The expedition stays below the barrier layer: it establishes exact finite facts in a standard restricted measure and refuses to infer an asymptotic complexity-class consequence without a theorem-level bridge.
