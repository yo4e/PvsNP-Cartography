# N8 recovery and sparse certificates

Two distinct results are recorded here:

1. The existing Hamming-layer bridge and complete n=8 degree equality were
   repaired and actually verified in Lean at e034962d3df395a4b82bc00d2ef78aa8d6cb25a4.
2. The prior explicit 939-polynomial certificate was recovered, and a new
   159-polynomial certificate was validated by two differently structured
   exact Python checkers. These explicit compact witnesses are NOT yet separate
   Lean-formalized witnesses. The degree value itself was already known.

## Reproduce without optimization dependencies

From this directory:

```bash
python recover_939.py > /tmp/recovered-939.json
python verify_compact.py --certificate /tmp/recovered-939.json
python audit_anf.py /tmp/recovered-939.json
python verify_compact.py --certificate certificate-159.json
python audit_anf.py certificate-159.json
```

Repeat with `python -O` to verify that checks do not disappear with assertions.
The actual CI does both and compares every pointwise-success digest. It also
checks seed provenance against the unchanged Expedition004 certificate.

The direct tuple validator does not import group construction or search code.
The second validator uses subset zeta/Mobius reconstruction and a Walsh dual.
The fixed JSON alone supplies the 159 actual degree-at-most-two coefficients
and positive integer probability tickets.

## Optional candidate discovery

```bash
python -m pip install -r requirements-search.txt
python reproduce.py --seed 2 --output /tmp/candidate.json
python verify_compact.py --certificate /tmp/candidate.json
python audit_anf.py /tmp/candidate.json
```

The optimizer only proposes an active set. Exact rational elimination and all
256 input inequalities decide acceptance. Pinned-version reproduction selected
159 rows with denominator100874688. A different solver may return a different
vertex; validate it rather than trusting a matching support count. Compare JSON
objects or canonical coefficient hashes, not pretty-printing bytes.

See conclusion.md, statement-audit.md, search-results.json, audit-results.json,
and ../../graveyard/009-rounded-probabilities.md. No novelty, minimal support,
all-n MOD3 degree bound, or P-vs-NP result is claimed.
