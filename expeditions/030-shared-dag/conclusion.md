# Conclusion: the circuit-to-polynomial implication is no longer assumed

Session executed2026-10-31 JST with fresh approval. Research lead 月野テンプレクス.
Classification: known-method reconstruction; Lean kernel accepted under disclosed
foundations; same-author statement audit; independent semantic review pending;
novelty-unknown. Issue22 is completed; Issue23 is the next bounded target.

## What mathematical uncertainty changed

Previously the repository had actual randomized OR/AND gates and a MOD3
probabilistic-degree obstruction but no proved passage through an entire shared
circuit. This expedition closes that missing implication for the concrete
Program/Slots model. It does not assume circuit approximability as a premise.

For every encoded finite topological circuit, r>=1, original nonlinear-node
count<=S and selected-output nonlinear depth<=h, an input-independent finite
REAL distribution of genuine GF2 polynomials has degree<=r^h and pointwise
error<=S/2^r. Sharing and repeated references do not cause formula-size inflation.
Local errors are tested on TRUE predecessor values, so a first-error/topological
argument and union bound suffice despite correlations across gates. Constants,
NOT/XOR, empty fan-in and neutral padding are included; unused nodes may remain.

With3*S<=2^r the original error1/3 predicate follows. A circuit computing the
residue-zero MOD3 target therefore satisfies n<(16*r^h+2)^2+2, using the already
accepted growing-degree obstruction. Exact output NOT proves the same necessary
condition for complementary polarity without increasing nonlinear cost/depth.
The theorem is for the implemented model; no verified external graph importer
or unrestricted-circuit separation is claimed.

## Evidence that actually completed

Source95adfa0080caa7c5106caf2164858d1fc66f969e passed
run41159407778/job124413377260. Whole-root --wfail9072 jobs,1268 declarations
within unchanged[propext,Classical.choice,Quot.sound],29 new explicit reports,
4 explicit endpoint signatures and all old reports completed SUCCESS. Actual
full decoded output, completed states, source files and matching commit/tree
were re-fetched and inspected; source hashes match local bytes. This is kernel
acceptance, not independent semantic review or a second proof kernel.

Separate exact controls77e8bf04 passedrun41155876986/job124402435004:
2694two-gate programs plus curated cases; two same-author representations agree;
normal/-O/stored JSON bytes agree. These finite checks corroborate, not prove,
the generic theorem. ci-evidence.md records precise counts and source scope.
Six failed whole-root candidates and two diagnostic failures were inspected and
preserved rather than promoted by partial successful lines. The final source
retains all original semantic and audit conditions.

## Attacks and dead directions

Graveyard050 refutes zero padding for AND, counting only the output gate's local
error and adding r per nonlinear layer instead of multiplying degrees. Its
6-node/63-occurrence unrolling example is a weaker-bound control, not a false
inequality. Graveyard051 preserves implementation failures, repairs and the
actual cache-egress diagnosis. Graveyard052 gives a written counterargument to
blindly deleting one factor using nonlinear depth when the source counts all
layers: XOR of disjoint minterms represents every Boolean function at h1 with
possibly exponential size. A size-independent constant-degree conclusion then
contradicts the accepted MOD3 obstruction. That minterm argument is not newly
Lean-formalized here and does not refute the correctly stated source theorem.

## Continue, then stop at the natural milestone

The next question is a SINGLE final AND/OR with a separate error allocation,
not another numeric threshold or indefinite infrastructure expansion. Candidate:
degree<=t*r^H and error<=S*2^-r+2^-t for an inner shared DAG and selected root
children. With t2 and12S<=2^r this gives degree2*r^H at error1/3. The root condition
must not be dropped for arbitrary XOR outputs. #23 records the exact obligations.

Continuation770197a1 already tests8curated circuits/36parameter cases with explicit
Cartesian-product matrices;18792degree checks and75144pointwise evaluations pass
locally with normal/-O equality. This is NOT in the completed slot CI and NOT a
generic theorem. Its role is to test a named improvement before another formal
session. At that milestone reconsider whether the reconstruction route should
continue or be parked, rather than polishing constants for their own sake.

No write blocker or unapplied patch remains. A transient project-cache failure
was resolved without paid resources or relaxed checks. Independent semantic
review and second-kernel verification remain absent; #8/#15 retain older scopes.
No novelty, optimal constants, general n12 classification, unrestricted lower
bound, proof-barrier escape or P-versus-NP result is claimed. This approved
session ends at the connected shared-DAG milestone; later work needs fresh approval.
