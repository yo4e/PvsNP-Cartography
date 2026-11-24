# Expedition 046 — costed growing cross and coefficient-labelled rows

Approved 2026-11-24 JST session. Parent main 0bf3887f354d65a917eac02db7f50b492bde233a.
Earliest unblocked target: #35. Review gates #8 and #15 are not being taken over.

The previous construction at a=3 established the exact NO minimum 109 and signed sensitivity 23, but positive bit tolerance did not lower its degree over free padding. The target is the designed one-level family, not a generic PCP or recursive compiler: a>=3, s=2^a, k=2a+1, N=2^k. Price actual Boolean gates, copies, physical aliases, Q and approximation budget. Reproduce a=3 and generate a=4. Do not infer a family theorem from the two runs.

A candidate pivot is to exploit the low degree in the *seed variables* of most honest intermediate rows. Arrange these rows by coefficient labels, rather than sequential tag numbers. Keep each physical row distinct, even if its honest truth table coincides with another's. Compare degree against the real cost of padding. Attack the resulting layout for witness dependence and address-space inflation. A positive result for a deliberately known witness is not an approximation theorem about unknown witnesses.

Dependencies: Expedition 040 shared geometry; Expedition 044 private fanout and pin charging; Expedition 045 cross overlap and downset completion. Prior-art context: Ben-Sasson–Viola, Short PCPs with projection queries, ECCC TR14-017, https://eccc.weizmann.ac.il/eccc-reports/2014/TR14-017/. The elementary Boolean polynomial distance argument is included below rather than assuming it from a finite run. Novelty unknown.
