# Cost correction — hash validation was not free in the tail=0 branch

2026-11-08 JST, 月野テンプレクス. Status: specific implementation-cost defect and repair, NOT a wrong-count counterexample or a refutation of the known counting method.

## Failure and affected claims

The old code at7eb2f25aa57b676f55f36a9648cd5212e9678ed4 used `len(set(masks))` before sorted multiplication. The old cost analysis explicitly tolerated t^2 duplicate checks because t^2<=t*M(n,D). That is sufficient for its coarse construction budget, but not for the separate large-degree b=0 argument, whose intended actual construction cost is only O(t*poly(n)). The coarse t*M budget can be as large as4^n and cannot establish the claimed2^n*poly(n) branch. The previous final summary omitted this validation interaction.

Python's numeric hash rule reduces nonnegative integers modulo a fixed prime P exposed as sys.hash_info.modulus. Thus the distinct valid masks0,P,2P,...,(t-1)P all hash to0, provided n is large enough to encode them. This is ordinary integer input, not a malicious user-defined hash function. Official references inspected: https://docs.python.org/3.13/library/stdtypes.html#hashing-of-numeric-types and https://docs.python.org/3.13/library/sys.html#sys.hash_info . The currently served3.13 documentation has a later patch label; actual execution here is CPython3.13.5.

`verify_transfer.py` uses ordinary-int hashes and an int subclass solely to count comparisons. At t=1024, n=71, the old set path makes646343 equality calls; the repaired path makes9974 sorting comparisons plus1023 adjacent equality checks. All six tested sizes32..1024 have the expected collision property. No huge2^71 output table is allocated. These are finite instrumented comparison counts, NOT a wall-clock benchmark or an asymptotic estimate inferred from six observations. The general objection is the unjustified worst-case hash-table bound; sorting removes that assumption.

## Repair and renewed bound

`canonical_source` checks arity and mask range, sorts masks, rejects equal adjacent masks and emits canonical source records. For t n-bit masks, deterministic comparison sorting costs O(t log(t+1)*poly(n)); adjacent checking is linear. The product code already used sorted aggregation. This establishes the required validation cost without favorable hash behavior.

When b=0, F_1(Y)=Y. Horner has one multiplication by a constant; it visits at most t pairs. Folding and a dense subset transform cost2^n*poly(n), and t<=2^n for canonical ANF. Validation therefore fits this bound. Since d>n/100 implies n/(200d)<1/2, the stated2^(n-n/(200d))*poly(n) form differs only by a bounded factor. The degree0 total-count case is direct, after reading/validating its encoding.

In the nontrivial regime1<=d<=n/100, the old generating-function argument remains intact: b=floor(n/(100d)), D=(2b+1)d, D+d<=n/25, M(n,d)M(n,D)<=2^(31n/50), and b>=n/(200d). The repaired validation is absorbed there as well. This is written complexity analysis, not Lean cost verification.

## Evidence and boundaries

Repair source9afb67d1d1061558cea1a7a7d085236a59504087 passed completed run42437159862/job128598359545. Both old suites reproduce every numerical field, normal/-O outputs agree, and new malformed-input checks reject all five controls. Historical runtime stdout is retained unchanged; its self hash describes the historical source. The new output fingerprint is explicit in replication-manifest.json and the actual completed job output.

The repair does not alter any Lean file, modulus, count definition, input polynomial semantics or theorem claim. Prior exactness evidence stays at its own immutable source. The stronger claim that the executed Python program had a fully justified worst-case bound before this repair is withdrawn.
