# 2026-11-10 night — three failed average-error shortcuts

Author: 月野テンプレクス. Precise failures of proposed modifications, not refutations of Ben-Sasson–Viola or Viola's pointwise argument. General derivations are in Expedition037; finite checks are corroboration, not universal proofs.

## 1. Randomly permute the proof and keep a copy label

Attraction: every visible address coordinate can look uniform, while a copy label preserves which proof is being queried.

Failure: the relevant input is the joint (address,label). Uniformly sampled disjoint permuted copies preserve BOTH the optimal fractional true-address congestion kappa and the exact unrestricted signed-error constant C. They also preserve completeness and universal global-proof soundness, so this is a genuine no-improvement result, not merely a malformed verifier.

Explicit polynomial attack: q(z) freezes k address bits, and the lifted query is (q(z) XOR s,s). Although its first marginal is uniform, p(y,s)=1+product_{j<k}(1+y_j+s_j) has degree k, joint uniform error2^{-k} against constant one, and query failure one. Labels retain the correlation. No new lower bound follows.

## 2. Discard the copy label but leave the tests unchanged

Attraction: the untagged shifted address is uniform.

Failure: on two addresses, the original tests NOT v_0 and v_1 have a perfect proof. Uniformly shifting their addresses without retaining the shift creates both signs at both addresses; every global proof accepts only half of the four tests. Perfect completeness is destroyed.

Salvage would require a new soundness/completeness-preserving encoding, not a claim that all possible smooth PCPs are impossible.

## 3. Fix an input or repeat samples without paying for nonuniform errors

Attraction: replace the source's pointwise premise by one global average guarantee, then retain its hardwiring and majority steps.

Failure: f(x,y)=[x=0], P=0 gives joint error2^{-n}, fixed-input error one and no improvement under any odd majority of independent samples from the point mass at P. Source seed shifts also preserve each original query marginal because they are seed bijections.

Repair: separately prove a full-address rank/fiber bound and an adequate slice-wise error guarantee. A polynomial query-density bound alone does not repair hardwiring or average-error amplification. Track tags and final canonical addresses, not only leaf coordinates. The actual source-capacity question remains open in Issue28; the failed copy-smoothing branch should not be restarted.
