import PvsNPCartography.CentralBinomialBound
import PvsNPCartography.AgreementConsequences

open scoped BigOperators

namespace PvsNPCartography.BinomialPrefixBound
open CentralBinomialBound
noncomputable section

/-- Unnormalized real prefix; no probability interpretation is needed here. -/
def prefix (m k : ℕ) : ℝ := ∑ j ∈ Finset.range k, (m.choose j : ℝ)

theorem prefix_mono (m a b : ℕ) (hab : a ≤ b) : prefix m a ≤ prefix m b := by
  apply Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_mono hab)
  intro j _ _
  positivity

theorem pascal_prefix (m s : ℕ) :
    (∑ j ∈ Finset.range (s+1), (m+1).choose j) =
      (∑ j ∈ Finset.range s, m.choose j) +
      (∑ j ∈ Finset.range (s+1), m.choose j) := by
  simp only [Finset.sum_range_succ', Nat.choose_succ_succ', Nat.choose_zero_right,
    Finset.sum_add_distrib]
  omega

/-- The even prefix contains half the central atom in addition to half the mass. -/
theorem even_half_exact (s : ℕ) :
    2 * (∑ j ∈ Finset.range (s+1), (2*s).choose j) =
      4^s + Nat.centralBinom s := by
  have hp := pascal_prefix (2*s) s
  have hh := Nat.sum_range_choose_halfway s
  have hs := Finset.sum_range_succ (fun j => (2*s).choose j) s
  change 2 * (∑ j ∈ Finset.range (s+1), (2*s).choose j) =
    4^s + (2*s).choose s
  omega

/-- Uniform parity-aware half-prefix upper bound, including m=0. -/
theorem half_prefix (m : ℕ) :
    prefix m (m/2+1) ≤ (2 : ℝ)^m/2 + (m.choose (m/2) : ℝ)/2 := by
  have hnat : 2 * (∑ j ∈ Finset.range (m/2+1), m.choose j) ≤
      2^m + m.choose (m/2) := by
    have he : m = 2*(m/2) ∨ m = 2*(m/2)+1 := by omega
    rcases he with he | he
    · have h := even_half_exact (m/2)
      rw [he]
      have hi : (2*(m/2))/2 = m/2 := by omega
      rw [hi]
      simpa [Nat.centralBinom, pow_mul] using le_of_eq h
    · rw [he]
      have hi : (2*(m/2)+1)/2 = m/2 := by omega
      rw [hi, Nat.sum_range_choose_halfway]
      have hp : (2 : ℕ)^(2*(m/2)+1) = 2*4^(m/2) := by
        rw [pow_succ, pow_mul]
        ring
      rw [hp]
      omega
  have hr : 2 * prefix m (m/2+1) ≤ (2 : ℝ)^m + (m.choose (m/2) : ℝ) := by
    unfold prefix
    exact_mod_cast hnat
  linarith

/-- Adding b coefficients costs at most b times the central coefficient. -/
theorem prefix_extension (m a b : ℕ) :
    prefix m (a+b) ≤ prefix m a + (b : ℝ)*(m.choose (m/2) : ℝ) := by
  unfold prefix
  rw [Finset.sum_range_add]
  apply add_le_add_left
  calc
    _ ≤ ∑ _j ∈ Finset.range b, (m.choose (m/2) : ℝ) := by
      apply Finset.sum_le_sum
      intro j _
      exact_mod_cast Nat.choose_le_middle (a+j) m
    _ = _ := by simp

/-- The ACTUAL capped bound from the agreement theorem, not a replacement definition. -/
theorem bound_le_peak (m d : ℕ) :
    (AgreementConsequences.bound m (8*d) : ℝ) ≤
      (1/2 + (4*(d : ℝ)+1/2)*peak m) * (2 : ℝ)^m := by
  have hk : min m ((m+8*d)/2)+1 ≤ (m/2+1)+4*d := by omega
  have hcast : (AgreementConsequences.bound m (8*d) : ℝ) =
      prefix m (min m ((m+8*d)/2)+1) := by
    simp [AgreementConsequences.bound, prefix]
  have hpeak : (m.choose (m/2) : ℝ) = peak m * (2 : ℝ)^m := by
    unfold peak
    exact (div_mul_cancel₀ _ (by positivity)).symm
  calc
    _ ≤ prefix m (m/2+1) + ((4*d : ℕ) : ℝ)*(m.choose (m/2) : ℝ) := by
      rw [hcast]
      exact (prefix_mono _ _ _ hk).trans (prefix_extension m (m/2+1) (4*d))
    _ ≤ (2 : ℝ)^m/2 + (m.choose (m/2) : ℝ)/2 +
        ((4*d : ℕ) : ℝ)*(m.choose (m/2) : ℝ) :=
      add_le_add_right (half_prefix m) _
    _ = _ := by rw [hpeak]; push_cast; ring

/-- No square root or limiting approximation is required for this explicit estimate. -/
theorem bound_three_quarters (m d : ℕ) (hm : (16*d+2)^2 ≤ m) :
    (AgreementConsequences.bound m (8*d) : ℝ) ≤ (3/4 : ℝ)*(2 : ℝ)^m := by
  have hmr : (16*(d : ℝ)+2)^2 ≤ (m : ℝ) := by exact_mod_cast hm
  have hs := peak_square m
  have hmul := mul_le_mul_of_nonneg_right hmr (sq_nonneg (peak m))
  have hsq : ((16*(d : ℝ)+2)*peak m)^2 ≤ 1 := by nlinarith [hmul]
  have hlinear : (16*(d : ℝ)+2)*peak m ≤ 1 := by
    nlinarith [sq_nonneg ((16*(d : ℝ)+2)*peak m - 1)]
  have hc : (1/2 : ℝ)+(4*(d : ℝ)+1/2)*peak m ≤ 3/4 := by nlinarith
  exact (bound_le_peak m d).trans
    (mul_le_mul_of_nonneg_right hc (by positivity))

/-- A tiny exact refutation of dropping the even central atom. -/
theorem even_atom_cannot_be_dropped :
    ¬ prefix 2 (2/2+1) ≤ (2 : ℝ)^2/2 := by
  norm_num [prefix, Finset.sum_range_succ, Nat.choose]

end
end PvsNPCartography.BinomialPrefixBound
