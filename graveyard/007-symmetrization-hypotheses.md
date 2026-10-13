# 007: seven invalid shortcuts in probabilistic-polynomial symmetrization

Date: 2026-10-13 approval night. Status: explicit countermodels, not new lower bounds.
Author in skeptic role: 月野テンプレクス. Same-author audit, not external review.
Reproducer: expeditions/008-full-symmetrization/audit.py (normal and python -O).

## Attraction and failure

Averaging sounds harmless, but several superficially similar operations have
different types or quantifiers. The following strengthened statements are
false. The repaired formal construction keeps the relevant hypotheses.

### 1. Remove target symmetry

For n=2, f(x)=x_0 and P=x_0, original success is one at every input.
Average the two renamed polynomials x_0 and x_1. At x=(1,0), success is only
1/2. Evaluation transports correctly, but the target value need not transport.
Lean target_symmetry_is_needed checks the underlying correctness-identity
failure; Python additionally evaluates the two-term distribution explicitly.

### 2. Replace every orbit bound by one whole-cube mean

For AND2 and the zero polynomial, global success is 3/4. At (1,1) it is zero,
and symmetrizing the zero polynomial does not change it. This input forms
its own permutation orbit. Lean checks the three good inputs and the bad
all-one input. This is a counterexample to the inference about this witness,
not a theorem excluding every possible randomized degree-zero family.

### 3. Use the inverse in the evaluation pullback

Let e=(1,2,0), P=x_0, x=(0,1,0). Renaming P by e gives x_1, whose value is one.
Evaluating P on x composed with e inverse gives zero. The correct evaluation
identity uses x composed with e. Swaps alone would conceal this error.

### 4. Replace the full symmetric group by a cyclic subgroup

Let n=4, P=x_0*x_1, target zero. Inputs (1,1,0,0) and (1,0,1,0) have the same
weight. Averaging the four cyclic shifts gives success 3/4 and 1 respectively;
averaging all 24 permutations gives 5/6 at both. Cyclic invariance is not
full permutation invariance, and does not make all equal-weight inputs
interchangeable. This is a smaller diagnostic than graveyard/006.

### 5. Replace a permutation by a variable-collapsing map

Over GF(2), rename both variables of x_0+x_1 to x_0. The result is zero:
actual degree drops from one to zero. The degree equality requires a bijection;
this counterexample says nothing against the usual nonincreasing-degree bound.

### 6. Replace actual polynomial degree by Boolean truth-table degree

The nonzero polynomial x_0^2+x_0 has actual degree two but evaluates to zero
on both Boolean inputs. Our rename theorem is about the polynomial object,
not an ANF reconstructed after evaluation on the cube.

### 7. Average coefficients in the characteristic-two field

Two is zero in GF(2), so uniform averaging by a group order divisible by two
cannot be interpreted as division by a nonzero field element. Lean's totalized
division makes 1/0=0; that convention does not turn it into a probability.
The actual weights are real, where 1/2 is positive. The construction is a
mixture over polynomials, not one polynomial formed by averaging coefficients.

## Repair, evidence and limits

Use the full finite group, a symmetric target, the correct input pullback,
actual polynomial degree and normalized nonnegative REAL weights. The formal
finite-sum identity then supplies the repaired implication. All seven examples
are checked exactly in Python. Only the three components identified above
are also encoded in SymmetryApplications.lean; do not claim all seven have
individual Lean formalizations. Four additional corrupted probability/group
inputs are rejected by the checker.

No small-support optimality, universal lower bound, new degree value or P-vs-NP
conclusion follows. The complete executed output is retained in Expedition008.
