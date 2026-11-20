# Buffer actual maps, not raw path names

The input-buffer theorem requires a single read of each distinct physical map
at a center. The [canonical token argument](compiler.md) proves
`q_j(z) = tau_z(q_j(0))`, where each `tau_z` is a bijection on canonical storage.
Therefore equality at zero is equivalent to equality as maps; distinct keys
cannot collide only at later seeds. Tree identity and symbol-bit index remain
in the keys. Raw path labels before parent/sibling returns are not valid keys.

[check_query_maps.py](check_query_maps.py) fixes every leaf slot and fresh tape,
selects the symbolic canonical branch, substitutes all fresh positions, and
checks equality of the whole signed-projection signatures for equal zero keys.
Every original seed bit appears exactly once. Independent integer routing is
checked at four seeds per raw slot. Finally, every seed's deduplicated view is
compared to the separate physical-address representation in Expedition 042.

| Rate a | Seed bits k | Raw slots, including unused tape bits | Distinct maps | Maximum readers per physical symbol |
|---|---|---|---|---|
| 3 | 7 | 640 | 124 | 23 |
| 3 | 8 | 5,248 | 604 | 23 |

The two rows are bounded controls, not a proof for arbitrary depth. The general
proof is the token induction in compiler.md and the reader-set derivation in
[043](../043-dispersed-shifts/physical-cost.md). For one RS call at fixed rate
the latter bounds readers by `2^(2a)+2^a−1`. Additional outer queries and
translated calls must also be charged. In particular, the whole-field A test
in the actual 040 fixture reads each A bit from all 128 centers; its load is
128, even though the B geometry has maximum 23.
