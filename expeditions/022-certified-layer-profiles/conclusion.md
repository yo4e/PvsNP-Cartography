# Generic layer evaluation completed; a tempting lift and reweighting fail

Formal status: ACCEPTED generic weighted-layer and actual-polynomial interface.
Code9785a2705cc88efd372ab3de29a61007387bd91d passed completed
run39615053307/job119273743612, pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
--wfail9052 jobs,695 namespace declarations and26 new target reports within
[propext,Classical.choice,Quot.sound]. Complete actual log, full source files
and matching Git commit/tree were fetched. See ci-formal-evidence.md and
axiom-report.txt. This discharges Issue14's mathematical implementation target.

## Result
The actual Hamming-layer sum of ANY real function of overlap is a short
binomially weighted sum. Nonempty-layer normalization and empty-layer
zero totalization are distinguished. Actual elementary symmetric GF(2)
MvPolynomials have proved totalDegree bounds and evaluation by overlap choose d.
Two clique-quadratic families q_A/r_A have proved degree<=2, actual evaluation,
MOD3 correctness and generic closed layer-sum/mean formulas. No surrogate
truth-table label or assumed evaluation identity is used.

Independent exact code at d65bfec7 reproduces174762 polynomial evaluations,
1022 Mobius checks,4608 signed layer cases,41870 elementary counts and the
existing n11 masks/tickets with minimum158/231. Normal/-O and saved/actual JSON
match in completed CI39614264276/job119270959043. Re-fetched source/result
blobs agree with local bytes/canonical output. These tests remain bounded.

## Attack beyond implementation
Extending the n11 recipe to zero,q_{n-3},r_{n-4} with weights[1,4,2]/7 fails
already at n12. Weight10 success is19/33, below2/3 by1/11; weight7 also fails.
Direct evaluation of4096 inputs and independent binomial profiles agree.
The base failure passed completed CI39615642650/job119275791416 at56f8670f.

Changing only the probabilities does not salvage this candidate family.
A dual with per-input integer masses5 at weight6 and126 at weight10, total12936,
gives maximum8316/12936=9/14<2/3 over ALL716 declared zero/q9/r8 polynomials.
All708840 positive-mass polynomial/input comparisons and a separate profile
calculation agree locally in normal/-O. The separate finalized attack CI record
must be consulted for remote reproduction of this stronger certificate.
This excludes arbitrary finite REAL mixtures of the specified family by
linearity, not arbitrary degree-two polynomials. No dedicated Lean instance
of that restricted-family obstruction has been compiled here.

## Dead directions, salvage and scope
Graveyard028/030 preserve two inspected formal implementation failures;
029 records ordered-edge/normalization mistakes;031 the fixed-weight lift;
032 its failed probability-only repair. No theorem or axiom policy was weakened.

The next useful step is a faithful finite-mixture/certificate interface using
these accepted profiles, with the restricted dual as an adversarial application.
Prefer existing duality and symmetrization lemmas over redundant wrappers.
Changing the family, not merely probabilities, is necessary to escape the
specific n12 obstruction. Do not turn this into an unbounded n-by-n staircase.

Numerical exact degree2 coverage remains n5..11; generic degree-one exclusion
remains all n>=7. No n12 degree determination, arbitrary-n quadratic upper bound,
new asymptotic result, novelty or proof-barrier escape is claimed. Gemini's
independent review concerns the earlier checkpoint only. Human external review
and a second kernel remain separate, nonblocking gaps. No write blocker.
