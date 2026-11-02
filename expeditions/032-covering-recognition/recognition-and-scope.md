# Largeness, recognition and usefulness are three different questions

Research lead 月野テンプレクス, 2026-11-02 JST. The following are WRITTEN mathematical derivations with same-author attacks and finite corroboration. They are not additional Lean theorems or independent review. The formal counting endpoint is separately recorded in proof-and-scope.md.

## 1. A genuinely quantified nonvacuous regime

Write N=2^n, R=floor(N/3), V=sum(j<=R,choose(N,j)). Since2^(N-j)>=2^(N-R) for j<=R, the binomial theorem gives

 V*2^(N-R) <= sum(j=0..N,choose(N,j)*2^(N-j)) = 3^N.

Cubing and using3R<=N yields (V/2^N)^3 <= (27/32)^N. For d<=1, M<=n+1. Put a_n=2^(3n+6)*(27/32)^(2^n). The exact integer base inequality2^27*27^128<32^128 gives a_7<1. Also a_(n+1)=2^(-3n-3)*a_n^2, so induction gives a_n<1 for EVERY n>=7. Therefore

 (2^M V / 2^(N-1))^3 <= a_n < 1,

hence2^M V<2^(N-1). The formally proved conditional large_of_bound then has its arithmetic premise discharged in ordinary written mathematics for n>=7,d<=1: more than half the Boolean targets are outside the cover.

This is not extrapolation from numerical cases. The exact checker separately scans n<=12,d<=4 and verifies the integer base. The scan finds first tested half-density bounds at n3,d0; n7,d1; n10,d2; n12,d3, and none for d4 in its range. Those latter finite thresholds are not promoted to all-n theorems. At n4,d1 the crude union bound220320 exceeds65536 and is vacuous, although direct enumeration finds896 far targets.

## 2. Efficient affine recognition

For f:{0,1}^n->{0,1}, let W_f(a)=sum_x (-1)^f(x) (-1)^(a dot x). For the affine row a dot x+b,

 distance(f,a dot x+b) = (N-(-1)^b W_f(a))/2.

Thus its minimum affine distance is (N-max_a|W_f(a)|)/2. Splitting the character sum by one input bit gives the ordinary Walsh butterfly recursion. The supplied integer implementation uses O(N log N) additions/subtractions on O(log N)-bit integers, or O(N log^2 N) bit operations with straightforward arithmetic. This is polynomial in truth-table length N, not in input dimension n. Direct enumeration and the transform agree for EVERY target at n0..4 (65814 targets total).

For general degree d, direct enumeration of2^M squarefree coefficient rows costs2^M*N*poly(n); at d2 this particular method is quasipolynomial in N. That is an upper bound for a named algorithm, not a lower bound for all possible recognition procedures.

## 3. The uniform detector misses the intended MOD3 target

Let (a_n,b_n,c_n) count inputs by weight modulo3. The last-bit recurrence is(a+c,b+a,c+b), initially(1,0,0). It gives a_(n+2)-a_(n+1)+a_n=2^n. Therefore u_n=3*a_n-2^n satisfies u_(n+2)=u_(n+1)-u_n with initial pair(2,1), and is six-periodic:2,1,-1,-2,-1,1.

The residue-zero target has a_n=(2^n+u_n)/3 ones. Constant0 lies within radius floor(2^n/3) exactly when n mod6 is2,3,4. Hence the uniform far-from-degree-d property misses this target at infinitely many lengths for EVERY d>=0. This does not contradict pointwise lower bounds. Other lengths can also be missed by nonconstant affine rows: at n7 the nearest affine distance is37 while the radius is42. We do not claim a complete affine-detection classification from the constant argument. Details and boundary attacks are preserved in graveyard056.

## 4. General-circuit usefulness is positively refuted for d1

For n>=4,m=floor(n/2), take f_n=XOR(j<m)(x_(2j)*x_(2j+1)). It has degree2 and O(n) ordinary bounded-fan-in Boolean gates. Each two-bit Walsh factor is+2 or-2; an unmatched last input contributes2 or0. Consequently max|W|=2^(n-m) and minimum affine distance=N/2*(1-2^-m)>N/3 for EVERY n>=4.

This easy circuit family is inside the affine-far property at all sufficiently large lengths. Thus THIS property's usefulness against P/poly is false, even though it is large and efficiently recognizable. No cryptographic hypothesis is needed for this concrete counterfamily. The argument does not refute a different growing-degree property. This is the standard paired quadratic/inner-product example, not new mathematics; graveyard058 preserves the full derivation.

## 5. A partial repair, deliberately not the next main project

For a nonconstant target with C ones, assign weight1/(2C) to each one-input and1/(2(N-C)) to each zero-input. Both target classes have mass1/2, so a constant's error becomes1/2. For a nonzero character of weight k, let A_(n,k) be its sum over the MOD3 one-inputs. It is the coefficient of z^0 in (1-z)^k(1+z)^(n-k) modulo z^3-1. The best sign of that affine row has balanced correlation N*|A|/(2C(N-C)).

With a primitive complex cube root omega, for k>0 the roots-of-unity filter gives A=(2/3)Re((1-omega)^k(1+omega)^(n-k)), so |A|<=(2/3)*3^(n/2). For n>=3,C/N lies in[1/4,1/2]. Thus balanced correlation<=(16/9)*(sqrt(3)/2)^n, which is<1/3 for n>=12 because(3/4)^12<9/256. Exact coefficient recurrences handle n8..11, with minimum errors1231/3230,1231/3230,191431/465806,227821/621530, all>1/3. This proves the balanced affine gap for n>=8 in written mathematics. At n7 the error1927/7310 is below1/3, so this measure is insufficient there.

This merely repairs one averaging blind spot and is weaker than the repository's already accepted n>=7 affine obstruction. It is not the default next formalization project. Higher-degree recognition, general-circuit usefulness and a new strong explicit lower bound do not follow.

## Decision

Keep the proved one-way counting tool and its explicit limitations. Park further uniform-cover detector polishing and the weaker balanced-affine reconstruction. Move to the concrete modulus-amplification/no-wrap counting bridge described in next-frontier.md, motivated by algorithms-to-lower-bounds literature. It changes the mathematical question rather than accumulating another local counting wrapper.
