# Failed shortcut — witness dependence as an automatic soundness objection

Session: approved November 24 JST night; completed November 25 JST. Role: quantifier skeptic.

## Claim

Any low-degree proof layout chosen using an unknown satisfying witness is mathematically invalid in a nondeterministic proof-counting algorithm; incompatible satisfying witnesses therefore refute the whole route.

## Attraction

The projection-PCP in Ben-Sasson–Viola Theorem 1.1 is publicly constructed from the instance before seeing a witness. A tag assignment computed from actual witness values is not that public construction.

## Failure

The public-compiler requirement is a model constraint, not a universal soundness theorem. A different nondeterministic algorithm may guess one bounded row-layout description and one polynomial. If each original query has a fixed row identity, and a single row map Lambda is reused for all aliases, then pi(i,z)=P(Lambda(i),z) is one original global proof. The original NO bound therefore applies for every branch. Injection is needed for arbitrary-proof transport and error-metric equivalence, not for this NO-only argument.

Completeness is existential: one qualifying witness/layout/polynomial is enough. A second satisfying witness requiring different labels does not defeat that existential statement. The public construction and a guessed-layout construction must be distinguished rather than conflated.

## Explicit control

For any R independent constant row values w_i, assign tag (w_i,rank_i) with unique ranks among equal values. The degree-one completion is simply the tag's value bit. This uses at most 1+ceil(log2 R) tag bits and polynomial storage. It evades the fixed-layout counting argument because the layout itself carries the independent row values.

There is no free algorithmic improvement: explicitly guessing the labels costs R*t bits. In the growing cross compiler R>=k(4s^2+s-1), N=2s^2; hence the layout description alone exceeds an o(N) decision budget. The large number of templates requires a separate charge too.

## A real unsound mutation

Let the old clauses be (v) and (not v). Every global old proof fails one clause. If the two occurrences of v are mapped independently to different cells, setting the first to 1 and the second to 0 satisfies both clauses. This breaks global alias consistency. Even an injective map on occurrence identities does not repair it.

## Salvage and lesson

Keep the fixed public layout as the current model, or explicitly study a new guessed-layout model with a short descriptor, validated consistency, degree-controlled query composition, and a fully charged time bound. Witness dependence alone does not kill that second branch. The present exponentially large explicit row-table branch is blocked by its actual cost.

Primary sources: Ben-Sasson–Viola, <https://eccc.weizmann.ac.il/report/2014/017/download/>, Theorem 1.1; Viola, <https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/>, §2.3. The conditional argument and examples above are our elementary deductions, not claims from those papers. No novelty, independent review, Lean acceptance, or complexity separation is claimed.
