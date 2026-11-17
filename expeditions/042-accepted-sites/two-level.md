# Sharp two-level distance and a short cover of accepting sites

**Scope and status.** This is a written derivation for the original, single-seed, all-fresh-tapes RS predicate of Expedition 041 on one fixed, fully shared proof. Set \(s=2^a\), \(a\ge3\). The two root dimensions \(k=2a+2,2a+3\) have \(m=2s,4s\) outer rows respectively, outer-column strict degree cutoff \(t=m/s\), root dimension \(D=2m=2st\), and \(N=2sm\) external sites. The result applies to both cutoffs \(t=2,4\). The three results below concern this topology, in which growing \(a\) costs exponentially many reads in \(k\). No unbounded-depth or Lean result follows. See [family and geometry](../041-two-level-distance/family.md) and [outer application](../041-two-level-distance/outer-application.md).

## From a successful parity to an actual row polynomial

A seed has outer row \(v\) and low label \(u=sp+b\), where \(p\in\{0,1\}\) and \(0\le b<s\). Define three sets by the full-leaf verdicts on the fixed proof.

- \(C_p\) comprises the residues \(b\) for which all \(s/2\) outer columns of label \(sp+b\) pass. It is global because each such column test reads every outer ordinate.
- \(K_v\) comprises the residues whose \(s/2\) inner common columns all pass in \(v\).
- \(G_v\) comprises parities such that all \(s\) inner rows \(j=p+2f\) for \(0\le f<s\) pass in \(v\).

The seed accepts exactly if \(p\in G_v\) and \(b\in C_p\cap K_v\). Call a row regular when \(|K_v|\ge2\). A row outside this set has at most two accepting seeds.

In a regular row choose any two passing residue groups. Their disjoint inner-column groups supply \(s\) common abscissae. For a passing parity choose two of its passing inner rows and interpolate their degree-\(<s\) polynomials in their two distinct ordinates. This gives bidegrees \((<s,<2)\). At every chosen abscissa the true affine column agrees at both ordinates, hence at every ordinate. At each passing inner row all \(s\) common abscissae agree, determining its entire row polynomial. Substituting the local degree-\(s\) subspace vanisher yields one degree-\(<2s\) polynomial \(H_v(X)\) on the underlying outer-row sites belonging to every passing parity. If both pass, the same interpolation agrees on the entire outer row. All inner nodes use their actual field geometry.

For clarity about the outer interface, in an outer row the index of an inner parent cell is \(w=sj+i\) for \(0\le i<s\). Its bit \(a\) is exactly the parity of \(j\). An external site at low label \(sp+b\) has this bit \(p\). An outer common column of the group \(u=sp+b\) has within-row index \(w=s^2+2sh+u\) for \(0\le h<s/2\), also with bit \(p\). Its physical field abscissa is common across the outer rows, while its outer ordinate varies with \(v\). Consequently \(H_v\) matches both the \(s\) external sites and the common columns of its passing parity. This step uses the fixed coordinate order and parent/column aliases of Expedition 041.

## Gluing the parity classes

Call \(p\) strong if \(|C_p|\ge4\). Its globally passing groups supply at least \(2s\) distinct abscissae of that parity. Take the regular rows with \(p\in G_v\). If there are at least \(t\), interpolate their \(H_v\) on any \(t\) distinct outer ordinates to get \(Q_p(X,Y)\) of bidegrees \((<2s,<t)\). For every one of these common abscissae, its entire passing column and the column of \(Q_p\) coincide on the \(t\) ordinates and hence everywhere. For each selected regular row, its recovered \(H_v\) then coincides with \(Q_p\) at \(2s\) abscissae, forcing identity as polynomials in \(X\). This includes the regular rows beyond the original interpolation rows. If there are fewer than \(t\), interpolate their row polynomials directly in \(Y\), taking zero if there are no such rows. The degree bound still holds.

Compose with the outer subspace vanisher of degree \(2s\), translate the root back to \(F\), and apply an \(F\)-linear coefficient projection from the ambient extension to \(F\) which fixes \(F\). The result is one actual external codeword \(P_p\) of degree at most \((2s-1)+2s(t-1)=D-1\). It matches all \(2s\) external entries on **every** regular row where both parities pass, and \(s\) on regular rows of its sole passing parity. This is stronger than checking individual accepting sites with unrelated polynomials.

If neither parity is strong and \(|C_0|+|C_1|\ge4\), use the same interpolation on regular rows where both pass, using the union of the two parities' passing columns. This supplies one polynomial on all these full rows. For total below four no row has more than three successful seeds.

## Sharp uniform rejection constant

Write \(n_v\) for the number of accepting seeds in row \(v\). We give a distribution supported on at most two actual external polynomials for which expected agreements in every row are at least \(3n_v/2-s\).

| Global column groups | Choice | Rowwise check |
|---|---|---|
| Both parities strong | Equiprobable \(P_0,P_1\) | Regular full rows contribute \(2s\). A regular row with exactly one passing parity contributes at least \(s/2\), and \(n_v\le s\). |
| Exactly one strong | Its \(P_p\) | Regular full rows contribute \(2s\), and strong-only regular rows at least \(s\). Weak-only rows have \(n_v\le3\). |
| Neither strong | Full-row polynomial above if the total is at least four, or zero otherwise | A full regular row is recovered in the former case. Every other regular row then accepts at most three seeds. In the latter case all rows accept at most three. |

In each case a nonregular row has \(n_v\le2\), and a row with no passing parity has zero. Whenever \(n_v\le3\), the required credit is nonpositive since \(s\ge8\). A row with full credit satisfies the inequality even when it accepts all \(2s\) seeds.

If \(A=\sum_v n_v\) and \(M\) is the maximum agreement of any external codeword, averaging gives \(M\ge3A/2-sm=3A/2-N/2\). Thus the original rejection fraction obeys

\[
   (N-A)/N\ \ge\ (2/3)(N-M)/N.
\]

The [existing split-parity assignment](../041-two-level-distance/family.md) attains equality for every \(a\ge4\) in both dimensions. Its two forced values each occupy \(N/4\) external sites. The remainder evaluate \(X^D\), with \(D\) a power of two. Constant candidates attain at most \(N/4\) because the preimages of 0 and 1 both occur in the forced region for the stated polynomial-basis labeling, and every other constant has at most one agreement. Each nonconstant polynomial of degree \(<D\) has at most \((D-1)+(D-1)+D=3D-2\) agreements, using the three disjoint parts and the nonzero difference polynomials. For \(a\ge4\), \(N/4\ge4D\), so the nearest distance is exactly \(3/4\). Its acceptance and rejection both equal \(1/2\). For \(a=3,k=8\) the same count gives only \(162/256\le\delta\le192/256\); equality of the ratio on this particular witness is unverified. The coefficient is optimal uniformly over the two-level family.

## Agreement on the sites where an outer constraint actually accepts

A list of at most three external codewords covers every single-seed RS acceptance. With both parities strong, \(P_0,P_1\) cover regular acceptances. Nonregular rows contribute at most two sites per row and hence at most \(2m=D\) sites altogether. Interpolate one extra polynomial there. With exactly one strong parity, its polynomial covers the regular full rows and its own regular single-parity rows. On every remaining row at most three sites remain, at most \(3m\) in all, covered by two degree-\(<D\) interpolants. With neither strong, the total number of accepting sites is at most \(6m=3D\); divide them into three interpolation sets. Thus for **every** subset of the accepting sites some member of a fixed list for that proof matches at least a third of that subset. The polynomial selected from this list can depend on the subset. The case analysis also prices the exceptional sites without interpolation.

For the GF(256) NO residual of Expedition 041, the direct A test either rejects every seed or fixes an affine A. For any genuine degree-\(<32\) replacement for B the published fixture argument gives a nonzero residual of degree at most 35, so at most 35 joint acceptances can be charged to that replacement. Here \((m,D)=(16,32)\). If both parities are strong, the joint acceptance count is at most \(2\cdot35+32=102\); with one strong it is at most \(35+3\cdot16=83\); with neither it is at most \(6\cdot16=96\). The original joint verifier therefore rejects at least \(154/256\) on every assignment to this designed NO instance. This is a lower bound. Sharpness for this unpaired joint predicate remains open; the earlier sharp count of 221 uses a different, paired RS predicate.
