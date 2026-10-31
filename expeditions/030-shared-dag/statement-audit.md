# Same-author statement audit: concrete shared DAGs

Research lead and self-skeptic: 月野テンプレクス, fresh2026-10-31 JST session.
This is not an independent semantic review. Mechanical acceptance is recorded
separately with the exact source and completed run in ci-evidence.md.

## Formal-to-mathematical mapping

SharedDAG.Program stores a single prefix per node. Wire n m permits inputs and
previous-table indices only; the inductive index precludes forward references.
Gate has only constant, NOT, XOR, OR and AND constructors. No arbitrary-function
or oracle gate is silently admitted. Slots indexes ARGUMENT POSITIONS, not
source-wire identities. None is0 for OR/XOR and1 for AND. K and all arities may
be0. A sufficiently large finite K encodes any one finite fan-in instance, but
no translator from every external graph serialization is claimed verified.

values is the original deterministic evaluation. approximations and polynomials
are separate constructions. polynomial_eval equates genuine polynomial
evaluation to the approximate table; it does not redefine the target to make
correctness automatic. Tables are newest-first, while the separate finite
Boolean checker uses chronological order. Outputs may select earlier nodes or
external inputs. Unused internal nodes are permitted and conservatively counted.

cost adds1 exactly for every original OR/AND node. It is not formula-occurrence
count or wire count. outputDepth reads the selected wire's recursively computed
nonlinear depth: constant/input0, NOT inherits, XOR maximum, OR/AND maximum+1,
empty maximum0. It is NOT total gate-layer depth. The distinction is essential
in graveyard052; the stronger source theorem cannot simply be reparameterized.

polynomial_degree proves actual MvPolynomial.totalDegree<=r^depth for r>=1;
repeated wires and powers remain unreduced. There is no hidden multilinearity
assumption. r>=1 supplies exponent monotonicity when a gate reads a shallower
skip wire; the historical r0 counterexample remains relevant.

bad is the recursive union of local errors evaluated on TRUE predecessor values.
These vectors are independent of the sampled matrix by construction, not by an
assumption on random child outputs. good_values proves topological correctness
outside this union. bad_mass counts original gates and needs nonnegative weights,
not independence across gates. The accepted row-product construction supplies
local laws; no desired local bound is an endpoint premise.

feasible selects one finite matrix family with actual normalized real weights
BEFORE all Boolean inputs and returns the unchanged original degree predicate.
Its upper witness uses particular real weights, legitimately; the previously
accepted lower obstruction still quantifies over arbitrary real mixtures.
feasible_third derives the real error budget from3*S<=2^r and permits conservative
upper bounds S,h. mod3_size_bound additionally requires only genuine circuit
correctness for the residue-zero target, yielding n<(16*r^h+2)^2+2.

DAGBoundary negates the chosen output by an exact NOT node, preserving nonlinear
cost/depth. It supplies the complementary MOD3 polarity without confusing the
two targets. Its primary-source comment refers to Goldreich's nonzero convention;
Limaye et al.'s2025 source instead uses the residue-zero convention.

## Trust-boundary checks

Local lexical scans of the three new modules found no sorry, admit, axiom or
native_decide tokens. The two local backward.isDefEq.respectTransparency options
alter elaboration only, not the kernel, allowed axioms, theorem statements or
--wfail. Actual namespace/endpoint axiom outputs are required separately.
A successful finite test or another runner with the same Lean kernel does not
supply an independent semantic reviewer or a second proof kernel.

## Continued experiment, explicitly not a promoted theorem

check_root_budget.py uses the explicit Cartesian product of inner/root matrix
spaces on8curated circuits,36parameter cases,18792matrix pairs and75144pointwise
evaluations. Actual degree<=t*r^H, error<=S*2^-r+2^-t, and36qualifying one-third
bounds passed LOCAL normal/-O byte comparison and py_compile. Sparse arithmetic
is reused from check_slots.py. This check is NOT included in the completed
slot-control CI and NOT a generic root-budget proof. It tests the named next
frontier rather than silently broadening the currently accepted endpoint.
