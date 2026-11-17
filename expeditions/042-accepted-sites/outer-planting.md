# Extra accepted field constraints on the designed NO instance

Scale the four-selector NO constraint from [Expedition 041](../041-two-level-distance/outer-application.md) to $F=\mathbb F_{2^k}$. Choose $b\notin\{0,1\}$, put $J=\{0,1,b,b+1\}$, and write $Z_S(X)=\prod_{s\in S}(X-s)$. Set $T_0=Z_{J\setminus\{0\}}, T_1=Z_{J\setminus\{1\}}, T_r=Z_{\{0,1\}}, Z=Z_J=XT_0$. The designed residual is
$$
T_0(X)(A(X)+1)^3+T_1(X)A(X+1)^3
+T_r(X)A(X+b)(A(X+b)+1)+Z(X)B(X).
$$
Use the B-RS verifier and physical views $V_z$ of [the planting argument](planting.md). For a polynomial $A$ of degree at most one and polynomial $B$ of degree $<D$, the residual has degree at most $D+3$ when $D\ge3$. At $X=0$ its vanishing requires $A(0)=1$; at $X=1$ it requires $A(0)=0$. It is nonzero, so admits at most $D+3$ roots. For the counterexample fix $A=0$ publicly, eliminating the A test and preserving a polynomial field-symbol predicate budget. Equally, any separately tested all-honest zero A passes its perfect-completeness test. A direct all-field scan for affine A would cost $N$ reads and is unnecessary here. The residual becomes $T_0(X)(1+XB(X))$. It always vanishes on $J^*=\{1,b,b+1\}$, never at zero, and elsewhere precisely when $B(x)=1/x$.

Choose an integer $m$ with
$$
1\le m\le \min\{D,\ N-3q^2-1,\ \lfloor (N-D-4)/q^2\rfloor\}.
$$
Pick any $m$ centers $C$ outside $\{0\}\cup\bigcup_{u\in J^*}H(u)$. Symmetry keeps all three forced sites outside $\bigcup_{c\in C}H(c)$. Pick $D$ distinct points $T$ outside $J\cup\bigcup_{c\in C}H(c)$. The displayed bounds ensure both choices are possible. All sites in $C\cup T$ are nonzero, outside the forced sites, and $C\cap T=\varnothing$.

Interpolate $P_0$ of degree $<D$ to equal $1/x$ on $T$, and $P_1$ of degree $<D$ to equal $1/x$ on $C$. Explicitly, for either nonempty interpolation set $S$, take $P_S(X)=(1-Z_S(X)/Z_S(0))/X$. The numerator vanishes at zero, so this is a polynomial of degree $|S|-1$ with the required values. All sets can be chosen in increasing binary-coordinate order after excluding the indicated neighborhoods. Construct their two honest B-RS proofs using the actual field geometry. At each internal node use the bivariate decomposition of the input polynomial, restricting it to the row and column polynomials. The identities at shared sites give valid physical proofs, with perfect acceptance at every seed. [BV14, §6.1, equations (8)–(9) and Proposition 6.1](https://eccc.weizmann.ac.il/report/2014/017/download/)

Start with the $P_0$ proof and replace every physical cell in $\bigcup_{c\in C}V_c$ by the value at that address in the $P_1$ proof. An overlap between centers writes the same value, and locations where the two honest proofs already agree cause no problem. Each center sees the complete $P_1$ view and its reciprocal in the outer root. All points in $T\cup J^*$ see their complete $P_0$ views. Hence the RS and field constraint jointly accept on at least $D+3+m$ seeds. Counting additional mixed views is unnecessary. The $P_0$-only honest assignment attains exactly $D+3$, since $1+XP_0$ has its $D$ distinct roots on $T$, and value one at zero.

For sufficiently large $k$ and polynomially bounded $q$, the displayed choice allows $m=\Omega(N/q^2)$ at fixed rate. Thus the extra accepted sites can exceed the honest algebraic cap by an inverse-polynomial fraction of all seeds. For example at $a=3,k=64$ and the four fixed XOR masks $0,9,18,27$, the recurrence gives $L(64)=60{,}231{,}680$, $q=240{,}926{,}721$ and allows $m=278$. These are derived counts and an existence construction; no $2^{64}$-entry table was generated.

This obstructs using the honest residual root count as a sharp upper bound for arbitrary physically shared proofs under this extension of the designed NO test. It leaves open a constant gap for the field test, a list/approximate decoding argument, and the ordinary soundness of the published ACSP reduction. It changes neither the small-depth sharp counts nor the Boolean per-clause accounting.
