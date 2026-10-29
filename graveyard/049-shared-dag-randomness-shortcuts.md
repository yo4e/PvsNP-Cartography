# Four false shortcuts around shared-DAG approximation

Author: 月野テンプレクス, approved2026-10-29 JST session. Explicit exact witnesses in Expedition029/check_dag.py and dag-checks.json. Same-author computation, not independent semantic review. These refute the named shortcuts, not the gate construction or all circuit approximation.

## 1. Hash by source-wire identity

False: repeated arguments may share their coefficient merely because they read the same wire. OR(x,x), x=1: a*x+a*x=0 in GF2 for every coefficient a. Any number of such rows gives output0 with error1. Correct independent coefficients for the two argument POSITIONS give error1/4 for r2. Coordinate identities may coincide while random coordinates must remain separate. This is distinct from graveyard047's reused ROWS.

## 2. Multiply probabilities of different gates' failures

Two OR gates with true input11 and the same r2 matrix have identical failure events. Each marginal and their joint probability are1/4, not a joint1/16. Shared randomness remains legitimate: the needed UNION bound does not require event independence. Independence is constructed between rows within a gate, not assumed between nodes.

## 3. Apply fixed-input unbiasedness to a sample-dependent input

For one row a=(a0,a1), choose z=(a1,a0) when a is nonzero, and z=(1,0) when a=0. Every selected z is nonzero and a dot z=0; the failure probability is1 rather than1/2. A pointwise guarantee says forall fixed z, Pr_A[error(A,z)]<=1/2; it does not say the same for z=z(A). Thus the DAG proof must measure local failure on TRUE deterministic original values, not invoke the gate lemma directly on arbitrarily correlated child approximations.

## 4. Drop r>=1 from the circuit degree bound

Program OR(x,x) XOR x has nonlinear path-depth1. With r0 the OR approximator is0, so the output polynomial is x, actual degree1. The proposed bound r^h=0 is false. All-arity gate lemmas legitimately include r0, but the circuit depth conversion must assume r>=1. Exact skip wires matter.

## Retained historical control and repair boundary

The checker repeats x+x^2+x^3 from graveyard047 to ensure genuine polynomial degree is not replaced by Boolean reduced degree. New exact controls exhaust6566 two-node DAGs (two inputs, constants, fan-in0..2, NOT/XOR/AND/OR, r1/2), plus8 curated deeper shared DAGs at r1/2/3. These bounded successes do not prove the universal DAG endpoint. The generic gate formalization and the still-pending full DAG formalization have separate evidence states.
