# Refinement: three n11 orbits with weights 1/7,4/7,2/7

The original nine-orbit certificate remains preserved unchanged. A bounded
subset search of its nine seeds selected the zero polynomial and the (8,2,1)
code31 and (7,3,1) code29 orbits. Exact normalized weights [1,4,2]/7 suffice.
This is preferable for the next Lean interface, not a claim of optimal support.

The standard-library checker uses both coefficient encodings, Mobius degree
checks, full partition expansion and all2048 pointwise inputs. The expanded
index family has1925 quadratic polynomial entries (duplicates allowed), with
integer denominator27720. Minimum success158/231, margin4/231 above2/3. The
unchanged exhaustive affine dual is69/110<2/3 and still covers4096 rows.
Normal/-O runs agree and seven altered certificates are rejected.

Compared with the original nine-orbit distribution, the number of seed orbits
falls9 to3 and the orbit-weight denominator10000 to7. The explicit expansion
falls4785 to1925 indexed entries and denominator277200000 to27720. Worst-case
success falls from24044/34375 to158/231, but remains strictly above2/3. This
is a deliberate margin-for-simplicity trade, not a universally better witness.

For a faithful Lean instantiation use rows
(0,0,0),(1,2047,38605195639935),(1,1920,1151998655551),
lexicographic55-edge encoding, triple weights[3,12,6]/21 and threshold14.
Exact layer tickets are in compact-result.json. The n10 proof and the original
n11 denominator30000 must not be copied unaltered.

No n11 Lean execution or independent human semantic review has occurred.
The new workflow checks remote reproducibility; its actual completed output
must be fetched before claiming CI success. Search ran129 numerical subproblems;
that is not an exact infeasibility proof for one/two orbits, nor any global
support or denominator minimality proof. Novelty remains unknown.
