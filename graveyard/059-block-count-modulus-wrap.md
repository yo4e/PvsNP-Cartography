# Exact block counting fails when the modulus equals the largest possible count

Research lead 月野テンプレクス, freshly approved2026-11-02 JST session.
Written counterexample valid for every natural ell, with finite controls ell0..6. Not a Lean-accepted endpoint.

## Rejected shortcut

A residue modulo2^ell suffices to recover the number of accepting assignments in a block of ell Boolean variables.

## Counterexample

The constant-one polynomial accepts ALL2^ell assignments, but its count is0 modulo2^ell. The constant-zero polynomial accepts none and has the same residue. This includes ell0: one possible assignment has count1, which is0 modulo1. No decoder of that residue alone can distinguish the two cases.

## Repair and scientific use

Use modulus2^(ell+1), strictly larger than every count in[0,2^ell]. The canonical residue then uniquely determines the integer count. The proposed amplifier F_(ell+1) has degree<=2ell+1 and supplies the needed parity-to-power-of-two congruence before block summation. See Expedition032/next-frontier.md.

The finite program checks actual unreduced modular composition, Boolean reduction, tail summation and subset-zeta evaluation against direct parity enumeration. This is a bounded correctness control, not a general proof, a running-time speedup or the larger algorithms-to-lower-bounds implication. Preserve the endpoint even if a later efficient implementation chooses a different amplifier.
