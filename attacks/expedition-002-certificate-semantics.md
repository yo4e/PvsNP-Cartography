# Attack — Expedition 002 certificate semantics

Date: 2026-10-08

Role: Skeptic

Target: exact claims for `pdeg_{1/3}^{GF(2)}(MOD_3^n)` at n=5,6,7.

## Attack 1 — Did the quantity silently become average-case error?

No.

The upper certificate is pointwise after symmetrization. For each fixed input x of Hamming weight w, uniformly permuting the variables of a representative polynomial maps x uniformly over the full weight-w layer. Therefore the success probability for that fixed x is exactly the representative's success fraction on that layer.

The mixture is then checked layer by layer against 2/3.

The lower certificate is also pointwise-safe: if a randomized affine polynomial had success at least 2/3 on every input, then under any input distribution q its average success would be at least 2/3. The explicit q distributions instead bound every deterministic affine polynomial strictly below 2/3; convex mixtures cannot exceed that deterministic maximum.

## Attack 2 — Did symmetry hide an invalid assumption?

The discovery calculation used layer summaries, so the symmetry argument was independently attacked by direct enumeration of **all variable permutations** for every fixed input.

Observed minimum pointwise success:

- n=5: `7/10`;
- n=6: `2/3`;
- n=7: `10825/15922`.

For each n, every input of the same Hamming weight had identical success under the symmetrized distribution, as required.

For n=7 the eight-orbit mixture gives the same exact value `10825/15922` on every one of the 128 Boolean inputs.

## Attack 3 — Could a degree-1 polynomial have been missed?

No reduction to affine symmetry classes is trusted in the final lower check.

All affine polynomials are enumerated explicitly:

- n=5: 2^(5+1)=64;
- n=6: 2^(6+1)=128;
- n=7: 2^(7+1)=256.

Maximum expected correctness under the explicit adversarial layer distributions is:

- n=5: `11/18`;
- n=6: `11/18`;
- n=7: `17/30`.

Each is strictly below `2/3`.

## Attack 4 — Are the “quadratic” representatives actually degree <= 2?

Yes.

Each representative is encoded only by:

- one constant bit;
- a linear-term bitmask;
- a quadratic-term bitmask indexed by unordered variable pairs.

There are no monomials of degree >2.

Some support elements have lower degree, which is allowed in a degree-at-most-2 distribution.

## Attack 5 — Could floating-point LP output be carrying the theorem?

No.

Floating-point LP/random search was used only to discover candidate certificates.

The accepted certificate uses rational weights and exact GF(2) evaluation. The decisive comparisons are rational:

- lower bounds: maxima strictly below `2/3`;
- upper bounds: minima at least `2/3`.

For n=7 the discovered floating weights rationalize to an exact mixture whose weights sum to 1 and whose success is exactly `10825/15922` on every layer.

## Attack 6 — Did the target function change?

Target is fixed throughout:

`MOD_3^n(x)=1` iff `|x| ≡ 0 (mod 3)`.

The checker evaluates this definition directly from the Boolean input tuple.

## Attack 7 — Does this support an asymptotic claim?

No.

Three exact finite values do not justify extrapolation.

The only promoted conclusion is the finite statement:

`pdeg_{1/3}^{GF(2)}(MOD_3^n)=2` for n in {5,6,7}.

Any asymptotic conjecture must be separately stated, attacked, compared to known theory, and proved.

## Residual risks

1. The standard-library checker file is currently pending repository application because its GitHub `create_file` write was blocked by the execution safety layer after the orientation write succeeded.
2. The exact values have not been proved novel. Targeted search found standard asymptotic theory, not an exact small-n table.
3. A Lean reconstruction has not yet been attempted.

## Verdict

The finite certificate semantics survive the current adversarial pass.

Status: **exact finite result, novelty-unknown**.
