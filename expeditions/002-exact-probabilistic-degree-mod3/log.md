# Expedition 002 log

## 2026-10-08 — exact certificates through n=7

Role sequence: Experimentalist → Skeptic → Archivist

### Observe / orient

Issue #6 asks for the standard pointwise-error probabilistic degree of `MOD_3^n` over GF(2) at error 1/3.

The definition was fixed before computation and cross-checked against the symmetric Boolean-function probabilistic-degree literature.

### Act

Reconstructed the pilot n=5 and n=6 certificates independently.

Found simpler upper witnesses than the pilot mixture:

- n=5: one quadratic orbit, minimum success `7/10`;
- n=6: one quadratic orbit, minimum success `2/3`.

Pushed to n=7 instead of stopping at the requested boundary.

For n=7:

- found an adversarial layer distribution bounding every affine polynomial by `17/30`;
- found an eight-orbit rational quadratic mixture;
- exact combined success is `10825/15922` on every layer.

### Verify

A standard-library Python checker was run locally with exact `Fraction` arithmetic.

Observed output:

```text
n=5: affine max=11/18 (22 maximizers)
  upper layer success: 1, 4/5, 7/10, 7/10, 1, 1
  certified pdeg_1/3^GF(2)(MOD_3^5) = 2
n=6: affine max=11/18 (23 maximizers)
  upper layer success: 1, 5/6, 2/3, 7/10, 2/3, 5/6, 1
  certified pdeg_1/3^GF(2)(MOD_3^6) = 2
n=7: affine max=17/30 (51 maximizers)
  upper layer success: 10825/15922, 10825/15922, 10825/15922, 10825/15922, 10825/15922, 10825/15922, 10825/15922, 10825/15922
  certified pdeg_1/3^GF(2)(MOD_3^7) = 2
```

### Attack

A second implementation explicitly enumerated every variable permutation for every Boolean input rather than deriving pointwise correctness from layer symmetry alone.

Minimum pointwise success matched the certificate:

- n=5: `7/10`;
- n=6: `2/3`;
- n=7: `10825/15922`.

At n=7 all 128 inputs receive exactly the same success probability under the mixture.

The lower verifier enumerated all 64, 128, and 256 affine polynomials respectively.

### Literature check

Targeted search found the standard asymptotic literature but no exact n=5,6,7 table.

No novelty inference is drawn from search absence.

### Repository write state

Repository writes are available.

Successful commits during this expedition:

- `3a585dc44a4bffeef25f28b58c9e916c1998532b` — orientation / definition contract;
- `dd7589d85464ec161615bf541fef002cf895a07f` — barrier audit;
- `815afb5616c9c55b5a4f512b6bb4cb40c4028e41` — adversarial certificate-semantics attack;
- `e4f7939b135b401ed9ec3542f070d78cb0d17d45` — conclusion.

One write was unexpectedly blocked by the execution safety layer:

`expeditions/002-exact-probabilistic-degree-mod3/verify_certificates.py`.

The same blocked write was not repeatedly retried. The exact file contents remain prepared and locally executed for later application.

### Checkpoint

The requested n=7 attempt became a positive exact result rather than a scaling-barrier report.

Current classification: **exact finite result / novelty-unknown**.
