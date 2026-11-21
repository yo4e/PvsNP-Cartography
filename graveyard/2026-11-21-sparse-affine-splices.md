# Correct affine kernel does not preserve the old NO minimum

## The tempting claim

Replace whole-field A membership by a few fixed-direction affine equations.
Because the zero-error A code remains exactly the affine field polynomials,
retain the old109-rejection NO lower bound.

## Why it was attractive and why it fails

The basis-direction test reads only eight symbols and has the right exact
kernel. Soundness, however, ranges over noncode A tables. Separate passing
stars can carry different affine polynomials while other centers reject.
The old residual-root bound cannot use one polynomial on all accepting
sites without an additional gluing argument.

## Executed physical counterexamples

All examples use one global A table and a single honest, physically shared
B extension. They do not detach recursive parent or sibling cells.

- Let B be the old degree 15 reciprocal interpolant at4,...,19. Put
  A(y)=100y on the radius-one star of96 and0 elsewhere, with multiplication
  in GF(128), modulus0x83. The eight-read NO test accepts1,...,19 and96:
 108 rejections.
- Patch three pairwise disjoint radius-one stars centered at96,117,122,
  with slopes100,92,98 respectively. The same B admits22 acceptances:
 106 rejections.
- For the radius-two test, put A(y)=1+121y when wt(y XOR124)<=2, and0
  otherwise. Interpolate B to1/x on
  {5,6,7,9,10,11,15,17,18,19,23,27,33,34,35,39}.
  The 20 accepting centers are those 16 points together with1,2,3,124:
 108 rejections.

Exact coefficients, nonzero A values, accepted sets and physical replays
are preserved in [attack_sparse.py](../expeditions/045-sparse-affine-reads/attack_sparse.py),
[results](../expeditions/045-sparse-affine-reads/attack-results.json) and
[compiler checks](../expeditions/045-sparse-affine-reads/compiler-checks.json).
The first trial's true minimum is only bounded between 28 and106 here;
the second is between 98 and108. These examples do not optimize either one.

## Repair and limit

Take D=U union V for complementary subspaces of sizes8 and16.
Every two translated stars share at least two points, forcing a common
affine polynomial at every passing center. This supplies the missing
accepted-site argument and restores exact109 rejection. The above splices
then reject119,128 and124 centers respectively.

Deleting a whole independent high-coordinate direction also destroys the
exact kernel: the indicator of bit6 passes every remaining local A test,
but no full-cross A test. That is a membership counterexample, not a
claimed joined NO witness.

Lesson: exact code-space characterization and soundness on arbitrary
global words are distinct obligations. The successful repair changes the
overlap geometry, not merely the number of queried symbols.
