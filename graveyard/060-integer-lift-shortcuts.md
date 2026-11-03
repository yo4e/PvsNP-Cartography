# Four invalid shortcuts in the integer counting bridge

Research lead 月野テンプレクス. Freshly approved 2026-11-03 JST session, Expedition033/#25. These are elementary counterexamples, not claims of mathematical novelty. Written reasoning and exact finite controls are distinct from any accepted Lean endpoint.

## 1. Canonical GF2-to-integer lift is not a ring homomorphism

Claim: lift addition/multiplication before evaluating by treating the canonical coefficient section as a ring map.
Attraction: this would make all transports automatic.
Failure: lift(1+1)=lift(0)=0 in GF2, but lift(1)+lift(1)=2 in the integers. No unital ring homomorphism GF2 -> Z can exist, since it would send 0=1+1 to2. The actual repair is coefficientwise lifting followed by the honest ring map Z -> GF2; prove that this reduction recovers the original polynomial. Integer evaluation agrees only modulo2, not as an integer equality.

## 2. Boolean reduction is not unrestricted polynomial equality

Claim: x^2=x as integer polynomials, or at arbitrary integer inputs.
Failure: evaluation at2 gives4 versus2. The reduction is valid on coordinates in{0,1}; that hypothesis must be explicit. Replacing positive exponents by1 cannot increase total degree. The argument works over a commutative ring, without pretending Z/(2^s) is a field. Salvage: evaluation equality on Boolean points only.

## 3. The unreduced amplifier value is not a nonnegative count

Claim: F_s(Y) is already the parity bit as an integer, or summing its raw integer values produces the accepting count without a final remainder.
Failure: F_2(Y)=3Y^2-2Y^3, hence F_2(2)=-4 while the parity bit is0. This occurs in an actual source lift such as P=x+y on the input11. The correct guarantee is congruence modulo2^s. Nonnegativity and the range below the modulus belong to the TRUE count; they need not hold for the algebraic sum. Recover the count by its canonical remainder only after proving no wraparound.

## 4. Overlap cannot be discarded in squarefree multiplication

Claim: multiply squarefree coefficient rows with disjoint-only subset convolution.
Failure: x*x reduces to x, not0; its value at1 is1. The Boolean quotient-ring product combines supports by UNION, allowing overlap. A disjoint-only operation is a different algebra. The prototype checks unreduced exponent-vector multiplication against union-mask multiplication.

The previously known modulus2^ell wraparound failure remains in graveyard059: count2^ell and count0 have the same residue0. Rechecking it at ell0..8 is a regression control, not another discovery.

Lesson: keep the three levels separate: formal polynomial identity, equality of Boolean evaluations, and integer congruence. Moving between them silently destroys the counting argument. The false shortcuts are dead; the guarded constructions remain viable. These observations do not establish a runtime speedup or unrestricted circuit lower bound.
