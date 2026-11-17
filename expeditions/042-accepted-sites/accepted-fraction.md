# Approximate agreement conditional on acceptance

At fixed root rate r = D/N, the sparse interpolation observation and the centered sampler inequality together control the *conditional* fraction of accepted symbols that one polynomial misses. This is for the RS predicate itself, before the outer constraint. Use the explicit weighted mask schedule and base bound δ ≤ C p in [the sampler derivation](outer-and-sampler.md). Let S be the set of translated-test acceptances and write s = |S|/N. Fix any global physical proof before defining S.

If |S| ≤ D, interpolate its actual external values with a polynomial of degree < D (use zero if S is empty). Otherwise fix one polynomial nearest to the entire root. The fraction of all N sites that both accept and disagree with this polynomial is at most δ. Since no translate from S hits the base rejecting set, centered mixing gives

    Pr[mismatch | accepted] ≤ δ/s
        ≤ C λ² (1−s) / {s [s+λ²(1−s)]}
        ≤ C λ² (1−r) / r².

Choose λ² ≤ ε r² / [C (1−r)] for 0 < ε < 1. For every assignment there is then a single polynomial matching at least a 1−ε fraction of the sites which actually accept. The polynomial can depend on the proof. In the dense case it can be chosen once from the whole word. The statement concerns symbol mismatches conditional on acceptance, not the fraction of seed-query pairs that read a particular wrong cell. It does not provide an efficient decoding algorithm for the nearest polynomial. For the outer residual with translated neighbors one needs the separate joint-set argument, since those reads need not land in S.

## Cost and the remaining gap

Let L be the one-call raw slot count in [the recurrence](planting.md). The explicit schedule uses at most L·Q² raw reads plus the external site for the overlap count, with Q the next power of two above the requested bias threshold as specified in the sampler derivation. At fixed rate this is O(L k² C / ε) for the displayed bias choice. Signed projections survive each fixed shift. At inverse-polynomial ε the predicate too has polynomial size. This is an upper budget; deduplicating addresses may save reads.

Conversely, every scheme in the fixed-translation model with augmented slot bound q has some proof on which every polynomial misses at least floor((N−D+1)/(q²+1)) actually accepted symbols. This forces a conditional mismatch fraction at least that quantity divided by N. For a concrete finite lower bound, any uniform guarantee of conditional mismatch ≤ ε must therefore satisfy

    floor((N−D+1)/(q²+1)) ≤ ε N.

For fixed rate, inverse-polynomial ε and growing k this gives q = Ω(1/sqrt(ε)). It concerns total slots, not just the number of masks. The upper bound carries separate k-dependent factors L and C. Comparing identical values of k, rate, error and base checker is necessary before concluding any construction is best. The exact-agreement counterexample and the tunable approximation coexist because the schedule changes with ε. The finite two-level route uses a different source of agreement: it decodes a bounded list by parity from the original schedule.
