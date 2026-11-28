# Auxiliary seed degree depends on the Boolean compiler

Approved November 28 night session. Repository reference:
`2a546c3781d71cd159b388997bd5312a7ceb78e6`.

Status: written elementary lemmas with exact signed-clause controls; no
novelty, Lean acceptance, external independent review, or complexity-class
separation is claimed. The control is a specified Boolean verifier with
complete shared seed rows, not the source recursive compiler's missing
gate census. The family, source, and skeptical agents exchanged findings.

## 1. What this attack distinguishes

Low seed degree of a raw accepting field witness does not by itself bound
the degree of the gate-value rows used by a Boolean clause compiler. A
compiler may create high-degree intermediate functions that cancel before
the decision. This can happen on a syntactically live output path, so
unreachable-code deletion alone is not a sufficient repair.

There are two further distinctions:

1. High **exact** auxiliary degree may still allow a low-degree approximation
   at the available error budget. The whole gate tuple must be counted, not
   only its sparsest final row.
2. Even a genuine lower bound on distance from every low-degree tuple to
   every satisfying compiled proof can fail to obstruct the counting
   algorithm. The usual distance/weight bound is sufficient, not necessary,
   for a guessed tuple to have acceptance above the NO threshold.

The following examples establish both distinctions with real gate-equivalence
clauses, explicit public-pin checks, all-assignment NO bounds, and actual
failure counts. They do not manufacture a success flag or use a difficult
NO witness to infer anything about YES proofs.

The checker assigns degree zero to both the zero function and nonzero
constants as a bookkeeping convention. Some algebra libraries assign the
zero polynomial degree minus infinity (or a sentinel such as minus one).
Every degree cutoff and lower-bound comparison here uses `d>=1`, so this
convention changes no feasibility, distance, or counting statement.

## 2. Equivalent extension by public computation

Consider a verifier made of unweighted signed Boolean clauses, with complete
proof rows indexed by a public seed `z`. Public seed bits are supplied by
pin rows; their correctness is enforced by the two usual complementary
clamp clauses. The same physical row is reused at every occurrence.

Let `C` be any uniformly specified acyclic XOR/AND circuit whose inputs are
the old public-pin rows at the same seed. Append a separate row for each
gate and its ordinary equivalence clauses. Do not assert its output.

For **every** old proof assignment, including one with incorrect public
pins, evaluating the new gates on the actual old pin values supplies a
unique extension satisfying all the new definitions. Conversely new
clauses have nonnegative violation counts and all old clauses remain.
Therefore

    min_new_proof raw_failures = min_old_proof raw_failures.

Perfect completeness is preserved, and every satisfying old proof has a
unique satisfying extension. In a satisfying proof the pins equal the
actual seed, so the new output row is forced to be `C(z)` regardless of
which old satisfying witness is chosen.

The **raw** minimum is invariant. The number of templates, address storage,
normalized rejection probability and error sensitivity are not invariant.
They must be recomputed. This extension alone can force any public circuit's
seed function into the proof without changing the relation on raw witnesses.

## 3. A live cancellation extension with the same exact raw minimum

The example can be strengthened so that the inserted computation is on the
syntactic output path. Suppose the old verifier has one positive output
unit clause `(v)`. Remove that one clause and introduce

    u = v XOR c,
    t = u XOR c,
    unit clause (t),

where `c` is the output of the public circuit `C`. Both XORs read the **same**
physical `c` row. Add all of `C`'s gate definitions.

For fixed old values `v,c` at a seed, the minimum number of violations among
the two XOR definitions and the new output unit is exactly `1-v`:

- If every definition holds, cancellation gives `t=v`, so `v=0` forces
  at least one failure.
- Set `u=v XOR c` and `t=v`; both definitions hold and exactly the new unit
  fails when `v=0`.

Evaluating `C` on the actual old pins satisfies all of its definitions, even
if the old pins are wrong. Thus for each fixed old proof, minimizing over
the new rows reproduces exactly the old output-unit contribution. All other
old clauses are retained. The exact raw global minimum is consequently
unchanged, not merely lower-bounded.

Satisfying proofs correspond bijectively: the new equations and `(t)` imply
`v=1`, while every old satisfying proof has the evaluated extension. The
`C -> u -> t` dependency is live. An algebraic cancellation rewrite followed
by deletion of the now unused `C` cone returns the old verifier, but ordinary
pruning of initially unreachable nodes would not do so.

Sharing is essential. If the second XOR reads an unrelated `c1`, the values
`v=0,c0=0,u=0,c1=1,t=1` satisfy both new XORs and the output unit, although
the old output unit fails. Such a detached mutant is not an equivalent
compiler.

This lemma concerns replacement of one unit of weight one using the stated
unit-weight gate clauses. Arbitrary weighted clause systems require their
own replacement costs; it is not a weight-oblivious claim.

## 4. Fully costed live bent control

Take four seed bits and `N=16`. The original proof has a raw row `w` and
four public pin rows `p0,...,p3`. The two variants are:

    YES: two copies of unit (w), plus all public pins;
    NO:  two copies of (w), two copies of (not w), plus all public pins.

The YES raw row is constantly one. The public rows are affine. Every NO
proof has exactly two base-unit failures at each seed, hence at least
`2N=32` failures globally; correct pins attain that bound.

Replace one of the positive `(w)` units by the live cone of Section 3 with

    a=p0 AND p1,   b=p2 AND p3,
    c=a XOR b,    u=w XOR c,    t=u XOR c.

The rows are `w,p0,p1,p2,p3,a,b,c,u,t`, all complete and physically shared.
Queries are identity projections except for the ordinary complementary pin
clamps. The gate clauses are the explicit standard three-clause AND and
four-clause XOR equivalences, and their literal truth tables are checked.

| Quantity | Original | Live extension |
|---|---:|---:|
| Used rows | 5 | 10 |
| YES clause templates | 10 | 28 |
| NO clause templates | 12 | 30 |
| Exact raw NO minimum | 32 | 32 |
| Normalized NO rejection minimum | 1/6 | 1/15 |
| Padded address cube | 128 | 256 |
| Maximum exact seed degree of a satisfying row | 1 | 2 |
| Exact all-error signed sensitivity | 2 | 3 |

The used extended cube contains 160 cells; padding is not used in any lower
bound below. All satisfying used rows are uniquely determined: pins force
their seed bits, the remaining positive `(w)` forces `w=1`, and the gate
definitions force the displayed evaluations. In particular this does not
select one hard member while ignoring easier satisfying proofs.

### Exact all-assignment soundness and sensitivity

For a public pin row `p_j`, the aggregate number of failures of its two
clamped units is exactly twice the number of cells where `p_j(z)!=z_j`.
All other clauses read the same seed. Thus the full raw objective is the
sum of local objectives

    (1-w)+(1-t)
    +2 sum_j [p_j != z_j]
    + sum_gate gate_failure,

with an additional `2w` in the NO variant. For an AND `(x,y,o)`,

    gate_failure=o(2-x-y)+(1-o)xy;

for XOR it is `x XOR y XOR o`. These are counts of failed signed clauses,
not merely Boolean checks that collapse multiple violations.

At every seed the NO local minimum is two; the YES local minimum is zero
at exactly one local assignment. The checker exhausts all `16*2^10=16,384`
seed/local-assignment pairs. The separate written replacement argument is
the general reason for the unchanged NO minimum.

For errors relative to the honest satisfying assignment, AND failures are
at most `e_x+e_y+2e_o`, XOR failures at most `e_x+e_y+e_o`, and the pin pair
cost is exactly `2e_p`. The resulting row charges are

| Rows | Signed gate-charge weight |
|---|---:|
| `w` | 2 |
| `p0,p1,p2,p3` | 3 each |
| `a,b,c` | 3 each |
| `u,t` | 2 each |

So every mixed error pattern causes at most three failures per erroneous
physical bit. This is sharp: at seed zero, flip only `a` from zero to one.
Its AND contributes two failures and `c=a XOR b` contributes one. The full
global sensitivity is therefore exactly `sigma=3`. The exhaustive local
ratios agree with this argument and a separate direct clamp implementation.

### Exact approximation costs, not just exact degree

The honest rows `a,b` are two-variable ANDs extended over the four-bit seed
cube. Their exact nearest-affine distance is four each. The row

    c=z0*z1 + z2*z3

has Walsh coefficients of absolute value four at every linear character.
This also follows by factoring the character sum into two two-bit sums,
each of absolute value two. Hence every affine function has distance six
or ten from `c`, and the minimum is six. Its complement `u=1+c` has the
same minimum. The other honest rows are already affine.

The nearest-affine row distances are therefore

| Row | Distance |
|---|---:|
| `a` | 4 |
| `b` | 4 |
| `c` | 6 |
| `u` | 6 |
| Other six rows | 0 |

Since row polynomials may be chosen independently once and then shared,
the **minimum total used-cell error** among all affine tuples is exactly
`20`. This exceeds the strict scalar sufficient budget

    V_NO/sigma = 32/3.

The exact minimum signed gate-charge error is

    3*4 + 3*4 + 3*6 + 2*6 = 54 > 32.

The literal-occurrence/fiber weights are `w:5`, each pin `6`, `a,b:7`,
`c:12`, `u:8`, `t:5`. They are read from the actual clause templates, with
fiber two for a pin clamp. Their exact minimum weighted affine error is

    7*4 + 7*4 + 12*6 + 8*6 = 176 > 32.

Thus the approximation obstruction is genuine at these stated sufficient
budgets, survives free padding, and applies to the unique satisfying used
proof. It is not based only on an exact-degree observation. Fixed mixtures
of affine tuples cannot beat the minimum expected total weighted error
either.

### Yet the actual affine certificate succeeds

Use the single shared affine tuple

    w=1,  p_j=z_j,  a=b=c=0,  u=t=1.

Both ANDs fail on four seeds each, for a total of eight clause–seed
violations. Every XOR, output unit and pin is satisfied. Thus

    actual failures = 8 < 16 = V_NO/2.

It is a valid low-degree certificate for the usual strict half-gap counting
test, despite failing every approximation budget above.

Eight is also the **minimum actual failure count among all affine tuples**.
An incorrect affine pin row differs from its prescribed bit at at least
eight seeds, already causing sixteen pin failures. An affine `w` other
than one differs at at least eight seeds; the unchanged positive unit and
the cancellation cone together cost at least two per such seed. Otherwise
pins and `w` are correct, and each AND has at least four failures against
any affine output. The XOR cone has a zero-failure affine extension for
any affine choices of `a,b`. The displayed tuple attains the lower bound.

The meaningful failure is therefore the inference

    no sufficiently close low-degree satisfying-proof approximation
    => no successful low-degree counting certificate.

Only the forward sufficient implication was justified by the weight/sigma
argument. Treating it as an equivalence would create artificial hardness.

This is a degree-two bounded example. It is not an obstruction at the
`alpha*k/log k` asymptotic degree scale and does not locate a hard witness
in the unary hierarchy family.

## 5. A high-degree live chain and its exact error curve

Use the same original YES/NO base, now with `k>=2` seed bits, and take

    g_j(z)=product_{i=0}^{j-1} z_i,   2<=j<=k,
    c=g_k,   u=w XOR c,   t=u XOR c.

Build the prefix AND chain with actual gate definitions and the same live
output replacement. The raw NO minimum remains `2N`, `N=2^k`. Every
satisfying proof contains a seed row of exact degree `k`, although the raw
witness and public pin rows are affine.

The final `g_k` differs from zero at one seed. That fact alone does not
price approximation of the preceding gate rows. Here the whole tuple can
be analyzed exactly.

For any `1<=d<k`, keep the honest prefixes with `j<=d`, set all later
prefixes to zero, and use `u=t=w=1`. Every row now has degree at most `d`.
The total used-cell error is

    sum_{j=d+1}^k 2^(k-j) + 1 = 2^(k-d),

where the final `+1` is the error in the live row `u=1+g_k`.
This is the **exact minimum** total error at degree at most `d`. For each
prefix with `j>d`, partition its seed cube into the `2^(k-j)` disjoint
subcubes obtained by fixing the remaining coordinates. Each has odd truth
parity, whereas every degree-`<=d` polynomial has even parity on a full
`j`-dimensional cube. At least one error is necessary per subcube. The
`u` row likewise has odd parity on the full seed cube and needs at least
one error. These are different physical rows, so their errors add. The
truncation attains every lower bound simultaneously.

For the actual signed compiler, an internal prefix has gate-charge weight
three, the final `c` weight four, and `u` weight two. The exact minimum
signed-charge error is `3*2^(k-d)`. The literal/fiber weights give the exact
minimum `5*2^(k-d)+9`. No approximation to the pin or constant rows helps,
because their minimum error is already zero and all weights are nonnegative.

The constructed tuple's **actual** violations are much smaller:

    2^(k-d-1).

Only the first truncated AND can fail, when its input prefix and next seed
bit are all one. Every later AND and both cancellation XORs are satisfied.

The all-error sensitivity is exactly four. Local gate charging proves the
upper bound. Flipping only the final `c` bit at seed zero causes two AND
failures and one failure at each XOR, attaining four.

At `k=8,d=4`, the checker gives:

| Quantity | Value |
|---|---:|
| Rows | 18 |
| YES / NO templates | 47 / 49 |
| Exact raw NO minimum | 512 |
| Maximum honest row degree | 8 |
| Exact minimum used error at degree≤4 | 16 |
| Exact minimum used error at degree≤3 | 32 |
| Constructed actual failure count at degree 4 | 8 |
| Scalar all-error upper bound | 64 |
| Half-NO acceptance threshold | 256 |

The entire gate tuple therefore has exact budgeted row degree four at a
used-error allowance of sixteen, despite exact degree eight. More generally,
an inverse-polynomial budget `E=N/poly(k)` needs only `d=O(log k)` for this
whole chain and its live cancellation rows, with the stated constant row
weights. These examples cannot explain a degree `alpha*k/log k` obstruction.

## 6. Consequence for the source-derived investigation

The actual raw A/B and recursive field-extension rows must first be separated
from public arithmetic and Boolean gate-value rows. The companion accepting
family investigation does that at the field level. The examples above show
why a degree claim about its gate rows has to name the Boolean implementation
and the error objective.

The source generator in `expeditions/046-growing-cross/check.js` stores each
created XOR/AND gate, performs local constant folding and memoization, and
emits definitions for its stored gates. General cancellation such as
`(v XOR c) XOR c=v` is not one of its displayed local rules. This does not
assert that the current source graph contains the exact inserted cone; it
identifies a real implementation dependence that cannot be ignored when
transporting raw-field degree to full proof degree.

Conversely, the source-reading branch has identified a constructive reason
to optimize before claiming a barrier: characteristic-two Frobenius squaring
is linear in field coordinates, and affine-subspace selector quotients can
be evaluated from a small-codimension linearized polynomial identity. A
large univariate selector degree is therefore not automatically a large
Boolean seed degree. The exact source lemma and its hypotheses belong in
that branch's derivation, not in these independent compiler controls.

The useful decision is to examine an explicit, semantically appropriate
source circuit and its actual countable predicate. An unavoidable weighted
approximation obstruction in one bloated equivalent compiler is not enough
to identify semantic witness hardness, and an exact-degree spike is weaker
still. The next structural result should survive the relevant field
identities and be connected to the actual failure objective, or it should
provide a counting method for a specified structured high-degree predicate.
No claim that every auxiliary degree spike is removable is made here.

## 7. Reproduction and evidence limits

Run `python3 check_auxiliary_artifacts.py`. `auxiliary-artifact-results.json` is its deterministic
output. The same script under `python3 -O` produced byte-identical output.
The checker uses no earlier experiment generator or inherited rejection
number. Its explicit clauses, pin maps, local all-error objective, affine
codewords, Walsh sums and odd-parity cubes are inspectable.

The 16,384 local assignments prove the finite bent objective after the
separate exact pin-pair decomposition. The general equivalent-extension and
chain error statements use the written derivations above. No finite test
is promoted into an asymptotic lower bound. The controls are standalone
compiler counterexamples, not a generated full recursive PCP compiler.
