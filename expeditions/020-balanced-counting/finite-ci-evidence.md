# Retrieved exact computational evidence, 2026-10-21 JST

Code317784842f82b6a1991db664ddd3734d08f72985;
tree4de0482f27620bae8597fcb31d8a82fb075d75f9.
Run:https://github.com/yo4e/PvsNP-Cartography/actions/runs/39507686566
Job118920623125, completed SUCCESS. The completed status and full job log
were fetched, not inferred from a queued workflow or uploaded result.

The actual workflow executed verify.py under normal and optimized Python,
compared the two output files byte-for-byte and compared the parsed actual
JSON with the committed result.json. All passed. Local normal/-O executions
were also completed and compared before the result was committed.

Actual reported checks:
- 1093 real-valued ordered-moment cases, lengths0..6, entries in{-1,0,1}.
- n3..12: every affine coefficient row and both constants, actual Boolean
  correctness on the full support of the input measure, 3031040 row/input checks.
- Explicit sample-to-input mass dictionary, normalization, finite uniformity
  on layers1/3 and actual/binomial/cubic score equality at these arities.
- 33147 exact formula pairs over n3..256 and every coefficient weight.
- Negative controls: missing diagonal correction gives0 instead of6;
  unordered denominator on ordered triples gives mass7/2; allowing repeated
  coordinates gives mass11/4; n6 coefficient weight1 gives2/3, not a strict gap.

After completed output inspection, actual files were re-fetched at the code
commit: verify.py Git blobc9f5430f22762970a1390563ed25cf73889587cd;
result.json Git blob71fbfaee021e7fca312672310ddbb089b9ddd04f.
The output explicitly labels itself bounded exact audit, not generic formal
acceptance. The generic Lean proof, independent human review and novelty are
separate gates. All bounded checks retain explicit exceptions under Python -O.
