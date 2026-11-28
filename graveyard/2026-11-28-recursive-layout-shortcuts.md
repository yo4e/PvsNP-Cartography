# Recursive-layout shortcuts that do not survive the costed model

Session: November 28, 2026 JST. Expedition 048. These records distinguish
repaired preliminary ideas from limitations of the surviving construction.

## 1. Exponentially many nodes force every useful layout table to be huge

**Attraction.** Even one all-row path shape has
`2^(k-2a+ah)` actual terminal nodes. Guessing a separate arbitrary label for
each node is too expensive for the unary hierarchy clock.

**Failure of the broader inference.** Rows need not be nodes. A public inverse
shuffle reconstructs the original seed across the edge labels and live point.
Only shape and fresh coordinates remain in the tag. The fixed-rate source
has polynomially many such transverse rows, each spanning many nodes.
The smallest depth-two example has 64 rows and 16,384 physical symbols.

**Salvage.** The per-node table objection remains valid for that model.
Expedition 046's growing-rate table obstruction is also unchanged. Neither
rules out the normalized fixed-rate construction.

## 2. A short invertible layout makes low-degree polynomial counting cheap

**Attraction.** A global map with a short circuit and cheap inverse can be
guessed without an exponential address table and preserves raw Hamming counts.

**Counterexample.** On normalized `(r,z)`, flip one row-tag bit by `AND(z)`.
The map is an involution with an `O(k)`-gate circuit. The linear output
polynomial selecting that tag bit becomes degree `k`, including on a genuine
full-rank recursive root query. At `k=8`, every input and inverse is checked.

**Lesson.** The relevant degree is after query composition. This does not
prove that this particular AND function is hard to count. A different
algorithm exploiting a factored high-degree representation remains possible;
the existing generic low-degree counter alone does not supply it.

## 3. Repeated tag search can remove the seed complexity of all witnesses

**Attraction.** Adaptive tags lower a concrete global proof's degree and the
normalized label table now costs only polynomially many bits.

**Failure point.** Fixing a tag in any degree-`d` polynomial gives a seed-row
polynomial of degree at most `d`. Guessing those row polynomials directly
already fits the same clock and defines one globally consistent proof.
No tag choice enlarges this direct certificate class. The public dense global
encoding differs from the optimum tag layout by at most `ceil(log2 R)` in
degree at the same used-cell error budget.

**Quantifier repair.** This statement survives minimization over all satisfying
witnesses. It is not derived from one bad member of a code-only family. Under
the full compiler/hierarchy hypotheses, infinitely many hard-family YES
instances must defeat every satisfying witness below the prescribed weighted
threshold. A universal low-degree layout there would contradict the very
hierarchy clock being used.

**Salvage.** Small-degree or constant-factor layout improvements may matter.
For an asymptotic change, investigate the actual seed functions, a different
precision model, or a stronger counting algorithm.

## 4. Low degree with free padding is low error against zero padding

**Counterexample.** One of 64 complete rows is `AND_4` on eight seed bits; the
others are zero. Value/rank tags give degree five with free padding at twice
the cube size. The same polynomial disagrees with the zero-filled enlarged
target at 1,008 padding cells, and that zero-filled target has exact degree
eleven. The dense original has degree ten. Disjoint affine cubes preserve
the used-cell degree minima through fifteen errors.

**Lesson.** Physical-cell error counts, full-cube error fractions, and chosen
padding completions are different quantities. State the target and denominator
before transporting an approximation claim.

## Reproduction

[Normalization and field transport](../expeditions/048-recursive-row-normalization/normalization.md),
[cost and row invariant](../expeditions/048-recursive-row-normalization/cost-and-collapse.md),
[exact degree controls](../expeditions/048-recursive-row-normalization/degree-controls.md).
No counterexample here asserts a new P-versus-NP result or defeats arbitrary
future counting algorithms.
