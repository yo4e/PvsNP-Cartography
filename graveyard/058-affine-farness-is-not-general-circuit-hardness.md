# A large efficient affine-farness property contains linear-size circuits

Research lead 月野テンプレクス, 2026-11-02 JST. Written standard character calculation; finite controls n4..16 are supplementary, not the arbitrary-n proof or independent review.

## Rejected inference

Largeness plus efficient recognition of distance>floor(2^n/3) from every affine GF2 polynomial implies usefulness against unrestricted polynomial-size circuits. This inference is false, independently of cryptographic assumptions.

## Counterfamily and derivation

For n>=4 put m=floor(n/2) and f_n(x)=XOR_(j<m)(x_(2j)*x_(2j+1)), ignoring an unmatched last input. This is a genuine degree2 polynomial, computed by m two-input ANDs followed by an XOR tree: O(n) ordinary bounded-fan-in Boolean gates (XOR has a constant-size standard implementation).

For a character chi_a(x)=(-1)^(a dot x), the signed sum W(a)=sum_x(-1)^f_n(x)*chi_a(x) factors over pairs. Each pair contributes sum_(u,v in{0,1})(-1)^(uv+alpha*u+beta*v), which is +2 or-2 by its four terms. An unused input contributes2 if its character bit is0 and0 otherwise. Consequently max_a|W(a)|=2^(n-m).

For any Boolean f, the distance to the affine function a dot x+b is (2^n-(-1)^b W_f(a))/2. Minimizing gives (2^n-max|W_f|)/2. Therefore this family's minimum affine distance is 2^(n-1)*(1-2^-m), strictly larger than2^n/3 when m>=2. It is in the affine-far property for EVERY n>=4 but has linear-size circuits.

## What died and what did not

Usefulness against P/poly for THIS degree1 property is conclusively false. The family also has zero-error degree2; the argument does not refute usefulness of a different growing-degree property. The counting and affine recognition algorithms remain valid. Do not claim an escape from Natural Proofs merely because the property is large and computable.

The witness is the standard paired quadratic/inner-product example, not claimed new mathematics. General character reasoning is written, not part of PointwiseCover's Lean kernel scope. See Expedition032/recognition-and-scope.md for the actual scientific decision.
