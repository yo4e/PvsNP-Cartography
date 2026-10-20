# n11 MOD3 probabilistic degree equals two: formally verified

Approved2026-10-20 JST session. The exact GF(2), pointwise error1/3 n11 degree
equality is now accepted by pinned Lean and audited under the foundational
allowlist. Complete numerical formal coverage in this repository is n=5..11.
This is new to the repository, not asserted novel to mathematics.

## Faithful theorem

The formal target is one iff integer Hamming weight is divisible by3. Actual
MvPolynomial.totalDegree bounds each GF(2) polynomial. Nonnegative REAL masses
sum to one and the single finite family is chosen before EVERY input.

The upper witness uses the canonical three seeds with probabilities[1,4,2]/7
and ALL coordinate permutations. Split kernel computations discharge all12
layer sums with triple tickets[3,12,6]/21 and threshold14. The existing general
Hamming-layer/full-permutation theorem yields pointwise degree2 feasibility.

The lower dual assigns mass15 to weight1 and1 to weight3, total330. Proved
coefficient permutation coverage turns24 canonical computations into all4096
rows, with bound207/330=69/110<2/3. Structural normal form and finite real
duality then exclude ALL actual degree<=1 polynomial objects and all finite
REAL mixtures, not just sampled affine coefficients. feasible_degree_iff,
least_feasible_degree and pdeg_eq_two close the original degree interface.

## Actual verification

Code9733d800128ad6d92b1f1293e453a4c8d5188f34; completed SUCCESS
run39380310454/job118487684638. Lean4.35.0-rc4, pinned Mathlib9e6b3aac,
--wfail9043 jobs,508 audited namespace declarations and18 printed n11 targets,
all within[propext,Classical.choice,Quot.sound]. Full actual logs were fetched;
matching coefficient data, final theorem statements and commit/tree re-fetched.
See ci-evidence.md and axiom-report.txt for exact provenance.

Separate code9238f5a1 passed run39380579421/job118488536922. Full2048-input
subset/monomial/block agreement,4096 direct/Walsh affine scores,12 layers,
201 coefficient mutations and five source mutations pass normally and with-O.
Saved JSON equals actual output and the production Lean source hash. The496-row
quotient has min158/231 and agrees with all layer probabilities; no new formal
quotient transport theorem is claimed by the full-permutation implementation.

## Attack and next frontier

Raw canonical seeds without coordinate randomization have success0 atmask63.
Both the exact checker and the accepted Lean negative control prove this
specific shortcut fails. Earlier quotient/mass failures remain in graveyard016.
No false one/two-orbit impossibility or support-minimality claim is made.

Issue #11's mathematical formalization gate is complete; #8 remains open for
independent human semantic review. Expedition019 continues with a separately
scoped generic affine-dual algebra/counting question; its acceptance must be
read from its own logs, not inherited from this n11 success.

No second proof kernel, independent human review, mathematical novelty,
general-n degree2 upper bound, circuit lower bound, barrier escape or P-vs-NP
conclusion is supplied. n12 remains outside this numerical formal coverage.
