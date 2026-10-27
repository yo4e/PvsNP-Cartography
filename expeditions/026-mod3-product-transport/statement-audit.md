# Statement audit: same author acting as adversarial reviewer

This is not an independent semantic review. Actual proof-kernel acceptance
and exact executed source are recorded in ci-evidence.md, not inferred here.

The final necessary_inequality has m,D,delta and exactly the ORIGINAL
HasProbabilisticDegreeAtMost predicate as inputs. It does not assume any
transport, agreement cardinality, probability bound on the new target, or
pre-existing MOD3 lower bound. no_mod3_approximation takes an explicit binomial
numerical gap, not an assumed semantic impossibility.

K is the defined GaloisField2,2; its cardinality4 is proved from Mathlib. A
nonbinary root exists by cardinality, not a caller-supplied existential premise.
Its polynomial relation is derived using finite-field Fermat and cancellation.
The code never substitutes ZMod4 for GF4. Characteristic-two coefficient algebra
is distinct from real arithmetic on probabilities.

The actual source degree is carried through coefficient embedding and affine
substitution by a monomial-support argument. No multilinear restriction on P
is assumed. The implementation prepends two fixed bits, not appends; its weight
identity proves the same residue targets. On all actual grid points decode
produces valid Boolean inputs, and forward/backward laws are checked separately.
The same polynomial index is used for both restrictions; nonnegative real linearity
and normalization establish the union bound. There is no resampling after y.

The source family is arbitrary finite, including duplicate polynomials and real
irrational weights; tests with rational probabilities merely corroborate that
universal statement. m=0,zero polynomial,D=0 and errors outside[0,1] do not hide
exclusions. The theorem is a necessary implication; impossible source premises
remain impossible rather than generating an approximation witness.

Seven-variable exclusion is explicitly ERROR1/12, not ERROR1/3. A bound at a
smaller error does not settle the old unrestricted n12 problem. The n299 route
still needs independent amplification. Correctness of this theorem does not
establish novelty, a circuit-size theorem, barrier escape, or P versus NP.

Counterexamples to invented independence and signed weights are genuine source
polynomial families, not just abstract coin tables. Their role is to falsify
extensions of this transport, not prove optimal degree/error tradeoffs. The
finite implementation is authored by the same investigator, despite different
arithmetic/evaluation implementations. Old Gemini review does not transfer.
