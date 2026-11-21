# Barrier and statement audit

## Actual claim

For the specified GF(128) YES/NO field fixtures and the physically shared
one-level B extension, change only the A test to the 23-offset union of
complementary coordinate subspaces. Compile with mandatory physical read
buffers, private fanout cap21, the inherited signed gate clauses, and the
inherited clamped public pins. The resulting NO raw failure minimum is 109,
the uniform unrestricted signed sensitivity about every satisfying YES
reference is23, and both padded proof cubes have Q=4,194,304.

The derivation covers arbitrary A/B field words, extension symbols, Boolean
gate/copy/constant/public assignments and mixed physical error sets. It does
not assume that a cheating word is a codeword or that its errors are random.

## Relativization

This is an explicit finite verifier comparison, not a separation between
uniform complexity classes. No step is claimed to be non-relativizing.
The inherited source reduction does not supply a P-versus-NP separation
from the new constants. A future route to such a separation still needs a
specific non-relativizing step.

## Natural Proofs

No property of arbitrary Boolean truth tables is proved both large and
useful against unrestricted circuits. Low-degree approximants for the new
encoded proof functions are not constructed. The Razborov–Rudich barrier
therefore has not been bypassed or refuted. Any circuit-lower-bound use
requires its own constructivity, largeness, usefulness and hypothesis audit.

## Algebrization

The affine-overlap and residual-root arguments use finite-field algebra.
That observation supplies no evidence of a non-algebrizing step. There is
no new algebraic-oracle separation or claim of barrier escape.

## Quantifiers and cost

- A single A word and a single physically shared B extension precede every
  public seed. Neither a slope nor a fresh B proof is resampled per query.
- Recovery concerns the stars of passing centers and the B values on passing
  rows/groups. It does not claim global equality on rejected entries.
- The signed bound is F(E)<=23|E| for every physical error set E. Restricting
  to low-degree polynomial errors might improve a bound, but is not used.
- Raw clause–seed counts are compared. YES and NO have different numbers
  of templates; any normalized probability must retain its own denominator.
- The new proof truth function includes its own gates/copies/padding.
  Approximation of the old encoding is not transported for free.
- The family formula in theory-notes.md is a written field-level extension.
  The fully generated Q and gate census here are only for GF(128).

Disposition: the finite construction survives the stated audit. General
complexity consequences, mathematical novelty and new Lean checking remain
unclaimed. See [the repository barrier map](../../map/BARRIERS.md).
