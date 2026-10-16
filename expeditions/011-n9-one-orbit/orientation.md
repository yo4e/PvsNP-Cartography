# Expedition 011: one-orbit MOD3 n=9 degree equality

Approved session: 2026-10-16 JST. Roles: explorer, experimentalist, formalist, skeptic, archivist (one author, not independent human review).

Start main: a5315840b06d4bad7d016d10ebf8b93a6d775639. Read AGENTS.md, README, all five mandatory documents, the current open Issues #8/#9, the latest commits, the n=8 conclusion and source. Do not rework the completed n=5..8 theorem chain.

## Bounded target

For MOD3 on the entire Boolean cube of dimension **nine**, with output in GF(2), establish or refute pointwise error <=1/3 via a single normalized finite REAL distribution on actual degree <=2 polynomials, fixed before quantification over inputs. Separately exclude all degree <=1 polynomials by a universal dual, not by sampled examples.

## Search path and acceptance

1. Use exploratory SciPy only to find candidate column mixtures, never for proof. Fixed seed: NumPy RNG 20261016, 17,578 candidate coefficient masks generated from old n=8 representatives, all 512 possible ninth-variable interactions for each, symmetric rows and random bit masks at seven densities; after equal layer profiles are merged, 8,618 profile rows. A ten-layer numerical LP proposed a four-seed mixture but revealed one constituent with a sufficient strict pointwise guarantee on its own.
2. That seed is (constant, linear mask, quadratic mask) = **(1,127,36505001791)**, with lexicographic unordered edges. Its single full permutation orbit is the certificate; the unsymmetrized polynomial is NOT pointwise valid.
3. Replace floating claims by exact per-layer counts and all-input validators, a symmetrized dual covering all 1024 binary affine polynomials, and reconstruction of the seed through a 4/3/2 coordinate partition.
4. Search ALL 7432 binary coefficient patterns invariant within at most three nonempty coordinate blocks, over every descending size partition of nine. This tests the *single uniform orbit* class only; no global certificate-optimality conclusion.
5. Connect the candidate to existing formally verified variable permutation, Hamming-layer and degree interfaces. A complete Lean --wfail build, namespace/target axiom audit and re-fetching of sources and actual logs are mandatory before formally-verified promotion.

## Reproduction

```sh
python3 expeditions/011-n9-one-orbit/verify.py --full
python3 -O expeditions/011-n9-one-orbit/verify.py --full
python3 expeditions/011-n9-one-orbit/scan_blocks.py
python3 -O expeditions/011-n9-one-orbit/scan_blocks.py
```

Both scripts require only the Python standard library. Their separate CI is under .github/workflows/n9-one-orbit.yml. The alternative partition loop does not assume the orbit-average identity and directly evaluates all 1260 distinct polynomials on all 512 inputs. Its source shares the certificate definition, so it is not independent human review.

The source and data are in this directory. Verification and limits are recorded in statement-audit.md, barrier-audit.md, conclusion.md and the session log.
