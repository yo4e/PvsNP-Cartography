# Retrieved exact attack evidence: fixed lift and restricted family

Final code9673b20699753e5a7766986efa9c36e6f4e6b274,
tree32ae814bba42af597ea2fc90236f0df5db5de93d.
Completed SUCCESS run39616486615/job119278821696, CPython3.12.15.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39616486615

The full completed job log was fetched and inspected. Both independent scripts
run in normal and optimized Python, each pair matches byte-for-byte, and parsed
actual output equals the corresponding saved JSON. This run covers BOTH the
fixed-weight failure and the stronger restricted-family dual.

Actual attributed excerpts:
2026-10-21T14:24:03.7629572Z Scoped n12 lift refuted exactly; no universal quadratic impossibility claim.
2026-10-21T14:24:06.8566349Z   "actual_polynomial_input_comparisons": 708840,
2026-10-21T14:24:06.8566814Z   "candidate_polynomials": 716,
2026-10-21T14:24:06.8572296Z   "input_mass_total": 12936,
2026-10-21T14:24:06.8572597Z   "maximum_integer_score": 8316,
2026-10-21T14:24:06.8572919Z   "maximum_success": "9/14",
2026-10-21T14:24:06.8574938Z   "strict_gap": "1/42",
2026-10-21T14:24:06.8820483Z All716 declared polynomials have dual score <=9/14; this is not all quadratics.

Re-fetched exact scripts/results at the immutable code above, then the actual
Git commit/tree. Local source bytes and compact canonical saved JSON reproduce
these remote Git blobs:
- naive-lift-attack.py:6d55ee5f2b89f81749614cc1204f66cd860d1a0d
- naive-lift-result.json:36571c63d9e4176579e27f615eac56b4641f4e12
- restricted-family-dual.py:bb9e4e6a2fb66de4265b6ea3f2b0ae66e01520ac
- restricted-dual-result.json:15e1fbb8a2093e4e5f8f043a5b2af0a3496106fc

The initial fixed-lift-only run39615642650/job119275791416 at56f8670f also
completed SUCCESS and its full log was inspected. The final run repeats it
and adds the complete716-polynomial obstruction, not merely sampled orbits.

Scope: n12 only, candidates zero plus all q9 and all r8. The exact input dual
uses mass5 on weight6 and126 on weight10; total12936. Every declared candidate
has score<=9/14, so finite real convex mixtures cannot have pointwise success
>=2/3. This argument is elementary weak duality; its dedicated Lean instance
has NOT been compiled. Neither arbitrary quadratics nor n12 degree are decided.
See graveyard031/032 and Issue16 for the precise failed directions and next step.
