# Failed shortcut: ignore one n11 coordinate and reuse the n10 witness

Claim: select a uniformly random coordinate to omit, then use the existing
symmetrized n10 mixture on the remaining coordinates; this retains pointwise
success>=2/3 for n11 MOD3.

Counterexample: any n11 input of Hamming weight10. With probability1/11 the
omitted bit is zero and the old n10 weight10 success is71/100. With probability
10/11 the omitted bit is one, leaving weight9. The n10 target is then1 but the
n11 target is0, so success is1-383/500=117/500. The exact new success is
(71/100 + 10*(117/500))/11 = 61/220 < 2/3.

Failure point: omission changes the MOD3 target; a valid old success probability
must sometimes be complemented, not copied. Averaging omissions does not repair
that mismatch. All twelve lifted layer probabilities were checked exactly.

Salvage: a fresh nine-orbit n11 mixture in Expedition015 passes instead. This
counterexample kills only the specified coordinate-omission lift, not arbitrary
n11 quadratic distributions and not any general complexity-class claim.
