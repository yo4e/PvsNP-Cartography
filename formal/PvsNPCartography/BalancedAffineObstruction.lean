import PvsNPCartography.BalancedAffineCounting

open scoped BigOperators

namespace PvsNPCartography.BalancedAffineCounting

open Symmetrization SmallSupportMod3

noncomputable section

/-- Actual correctness, averaged with a fixed normalized input-sample measure. -/
def sampleScore {n : ℕ} (p : Affine n) : ℝ :=
  ∑ s : Sample n, sampleMass n s * (affineCorrect p (sampleInput s) : ℝ)

theorem sign_triple_moment {n : ℕ} (b : BooleanCube n) :
    (∑ i, ∑ j, ∑ k, if Distinct i j k then
      bitSign (b i) * bitSign (b j) * bitSign (b k) else 0) =
      (∑ i, bitSign (b i)) ^ 3 - (3 * (n : ℝ) - 2) * (∑ i, bitSign (b i)) := by
  have h := ordered_triple_moment (fun i : Fin n => bitSign (b i))
  simp only [bitSign_sq, bitSign_cube, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul, mul_one] at h
  rw [h]
  ring

/-- The actual GF(2) evaluation score, proved by structural finite summation.
The formula is not assumed as a hypothesis or extrapolated from bounded tests. -/
theorem sampleScore_formula {n : ℕ} (hn : 3 ≤ n) (p : Affine n) :
    sampleScore p = 1 / 2 + bitSign p.1 *
      (((n : ℝ) - 2 * hammingWeight p.2) *
        ((n : ℝ) ^ 2 - ((n : ℝ) - 2 * hammingWeight p.2) ^ 2)) /
      (4 * (n : ℝ) * (n - 1) * (n - 2)) := by
  classical
  have hnr : (3 : ℝ) ≤ n := by exact_mod_cast hn
  have hn0 : (n : ℝ) ≠ 0 := by linarith
  have hn1 : (n : ℝ) - 1 ≠ 0 := by linarith
  have hn2 : (n : ℝ) - 2 ≠ 0 := by linarith
  let T : ℝ := ∑ i, bitSign (p.2 i)
  let C : ℝ := bitSign p.1
  have hs : (∑ i : Fin n, sampleMass n (.inl i) *
      (affineCorrect p (sampleInput (.inl i)) : ℝ)) =
      ((n : ℝ) + C * T) / (4 * n) := by
    have he (i : Fin n) : sampleMass n (.inl i) *
        (affineCorrect p (sampleInput (.inl i)) : ℝ) =
        (1 + C * bitSign (p.2 i)) / (4 * n) := by
      rw [singleton_correct]
      dsimp [sampleMass, C]
      field_simp
      <;> ring
    simp_rw [he]
    rw [← Finset.sum_div, Finset.sum_add_distrib, ← Finset.mul_sum]
    simp [T]
  have he (i j k : Fin n) : sampleMass n (.inr (i,j,k)) *
      (affineCorrect p (sampleInput (.inr (i,j,k))) : ℝ) =
      ((if Distinct i j k then (1 : ℝ) else 0) -
        C * (if Distinct i j k then bitSign (p.2 i) * bitSign (p.2 j) * bitSign (p.2 k) else 0)) /
        (4 * (n : ℝ) * (n - 1) * (n - 2)) := by
    by_cases hd : Distinct i j k
    · rw [triple_correct p i j k hd]
      simp only [sampleMass, hd, if_true]
      dsimp [C]
      field_simp
      <;> ring
    · simp [sampleMass, hd]
  have ht : (∑ i : Fin n, ∑ j : Fin n, ∑ k : Fin n,
      sampleMass n (.inr (i,j,k)) * (affineCorrect p (sampleInput (.inr (i,j,k))) : ℝ)) =
      ((n : ℝ) * (n - 1) * (n - 2) - C * (T ^ 3 - (3 * (n : ℝ) - 2) * T)) /
        (4 * (n : ℝ) * (n - 1) * (n - 2)) := by
    simp_rw [he]
    simp only [← Finset.sum_div, Finset.sum_sub_distrib, ← Finset.mul_sum]
    rw [ordered_triple_count, sign_triple_moment]
  unfold sampleScore
  rw [Fintype.sum_sum_type]
  simp only [Fintype.sum_prod_type]
  rw [hs, ht]
  dsimp [T, C]
  rw [bitSign_sum]
  field_simp [hn0, hn1, hn2]
  <;> ring

theorem sampleScore_zero {n : ℕ} (hn : 3 ≤ n) (b : BooleanCube n) :
    sampleScore (0,b) = BalancedAffineDualAlgebra.score n (hammingWeight b) := by
  rw [sampleScore_formula hn]
  norm_num [bitSign, BalancedAffineDualAlgebra.score, pow_two]

theorem sampleScore_one {n : ℕ} (hn : 3 ≤ n) (b : BooleanCube n) :
    sampleScore (1,b) = BalancedAffineDualAlgebra.score n ((n : ℝ) - hammingWeight b) := by
  rw [BalancedAffineDualAlgebra.score_complement, sampleScore_formula hn]
  norm_num [bitSign, BalancedAffineDualAlgebra.score, pow_two]
  ring

/-- A common bound for all coefficient rows at the fixed arity. -/
def envelope (n : ℝ) : ℝ :=
  1 / 2 + ((2 / 5 : ℝ) * (n * n * n)) / (4 * n * (n - 1) * (n - 2))

theorem algebra_score_le_envelope {n k : ℝ} (hn : 7 ≤ n) (hk : 0 ≤ k) (hkn : k ≤ n) :
    BalancedAffineDualAlgebra.score n k ≤ envelope n := by
  have hn0 : 0 < n := by linarith
  have hn1 : 0 < n - 1 := by linarith
  have hn2 : 0 < n - 2 := by linarith
  have hd : 0 ≤ 4 * n * (n - 1) * (n - 2) := by positivity
  have he := BalancedAffineDualAlgebra.cubic_envelope (le_of_lt hn0)
    (show -n ≤ n - 2 * k by linarith) (show n - 2 * k ≤ n by linarith)
  exact add_le_add_left (div_le_div_of_nonneg_right he hd) (1 / 2)

theorem envelope_lt_two_thirds {n : ℝ} (hn : 7 ≤ n) : envelope n < (2 : ℝ) / 3 := by
  have hn0 : 0 < n := by linarith
  have hn1 : 0 < n - 1 := by linarith
  have hn2 : 0 < n - 2 := by linarith
  have hd : 0 < 4 * n * (n - 1) * (n - 2) := by positivity
  have hp := mul_nonneg (show 0 ≤ n - 7 by linarith) (show 0 ≤ 2 * n - 1 by linarith)
  have hg0 : 0 < 2 * n * n - 15 * n + 10 := by nlinarith
  have hg := mul_pos hn0 hg0
  have he : (2 / 5 : ℝ) * (n * n * n) <
      (1 / 6 : ℝ) * (4 * n * (n - 1) * (n - 2)) := by nlinarith
  have hr := (div_lt_iff₀ hd).mpr he
  unfold envelope
  linarith

theorem sampleScore_bound {n : ℕ} (hn : 7 ≤ n) (p : Affine n) :
    sampleScore p ≤ envelope n := by
  have hn3 : 3 ≤ n := by omega
  have hnr : (7 : ℝ) ≤ n := by exact_mod_cast hn
  have hk : (0 : ℝ) ≤ hammingWeight p.2 := by positivity
  have hkn : (hammingWeight p.2 : ℝ) ≤ n := by exact_mod_cast hammingWeight_le p.2
  rcases p with ⟨c,b⟩
  fin_cases c
  · rw [sampleScore_zero hn3]
    exact algebra_score_le_envelope hnr hk hkn
  · rw [sampleScore_one hn3]
    exact algebra_score_le_envelope hnr (by linarith) (by linarith)

/-- Generic obstruction for all actual degree-at-most-one polynomials and
arbitrary finite REAL probability distributions on them. -/
theorem no_degree_one_family {n : ℕ} (hn : 7 ≤ n)
    {I : Type} [Fintype I] (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ 1) (hm : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1) :
    ¬ (∀ x : BooleanCube n, (2 : ℝ) / 3 ≤ ∑ i, mu i *
      (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (P i) =
        target x then 1 else 0)) := by
  classical
  have hn3 : 3 ≤ n := by omega
  have h := finite_dual_obstruction
    (fun i s => (affineCorrect (coefficientRow (P i)) (sampleInput s) : ℝ))
    mu (sampleMass n) (envelope n) ((2 : ℝ) / 3) hm hs
    (sampleMass_nonneg hn3) (sampleMass_sum hn3)
    (fun i => sampleScore_bound hn (coefficientRow (P i)))
    (envelope_lt_two_thirds (by exact_mod_cast hn))
  intro hp
  apply h
  intro s
  have he (i : I) : (affineCorrect (coefficientRow (P i)) (sampleInput s) : ℝ) =
      if MvPolynomial.eval (fun j => (((sampleInput s) j).val : ZMod 2)) (P i) =
        target (sampleInput s) then 1 else 0 := by
    rw [affine_polynomial_correct, ← degree_one_eq_affine (P i) (hd i)]
  simp_rw [he]
  exact hp (sampleInput s)

theorem degree_one_impossible {n : ℕ} (hn : 7 ≤ n) :
    ¬ HasProbabilisticDegreeAtMost (@target n) (1 / 3 : ℝ) 1 := by
  rintro ⟨m,P,mu,hd,hm,hs,hp⟩
  apply no_degree_one_family hn P mu hd hm hs
  have ht : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
  simpa only [ht] using hp

end
end PvsNPCartography.BalancedAffineCounting
