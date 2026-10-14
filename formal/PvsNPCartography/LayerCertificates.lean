import PvsNPCartography.HammingLayers

open scoped BigOperators

namespace PvsNPCartography.Symmetrization

noncomputable section

/-- A subtype sum and its full-cube integer-checkable representation. -/
theorem sum_layer_eq_filter {n w : ℕ} {M : Type*} [AddCommMonoid M]
    (g : BooleanCube n → M) :
    (∑ y : Layer n w, g y.1) = ∑ x : BooleanCube n,
      if hammingWeight x = w then g x else 0 := by
  classical
  rw [← Finset.sum_filter]
  exact (Finset.sum_subtype (Finset.univ.filter (fun x => hammingWeight x = w))
    (by intro x; simp) g).symm

/-- Exact multiplicity, derived from the general mean identity on indicators.
The mean identity itself was proved without assuming this cardinality. -/
theorem permutation_fiber_card {n : ℕ} (x y : BooleanCube n)
    (h : hammingWeight x = hammingWeight y) :
    Fintype.card {e : Perm n // permuteInput e x = y} =
      (hammingWeight x).factorial * (n - hammingWeight x).factorial := by
  classical
  have hs : (∑ z : Layer n (hammingWeight x),
      if z.1 = y then (1 : ℝ) else 0) = 1 := by
    have he (z : Layer n (hammingWeight x)) :
        (z.1 = y) ↔ z = (⟨y, h.symm⟩ : Layer n (hammingWeight x)) :=
      ⟨fun hz => Subtype.ext hz, fun hz => congrArg Subtype.val hz⟩
    simp_rw [he]
    simp
  have hn : (∑ e : Perm n, if permuteInput e x = y then (1 : ℝ) else 0) =
      (Fintype.card {e : Perm n // permuteInput e x = y} : ℝ) := by
    simp [Fintype.card_subtype]
  have havg := permutation_mean_eq_layer_mean
    (fun z => if z = y then (1 : ℝ) else 0) x
  rw [hs, hn] at havg
  have hfac : (n.factorial : ℝ) ≠ 0 := by
    exact_mod_cast (Nat.factorial_ne_zero n)
  have hchoose : (n.choose (hammingWeight x) : ℝ) ≠ 0 := by
    exact_mod_cast (Nat.choose_ne_zero (hammingWeight_le x))
  have hprod := (div_eq_div_iff hfac hchoose).mp havg
  simp only [one_mul] at hprod
  have hcomb : (n.choose (hammingWeight x) : ℝ) *
      ((hammingWeight x).factorial * (n - hammingWeight x).factorial : ℕ) =
      (n.factorial : ℝ) := by
    have hh : n.choose (hammingWeight x) *
        ((hammingWeight x).factorial * (n - hammingWeight x).factorial) = n.factorial := by
      simpa only [Nat.mul_assoc] using
        Nat.choose_mul_factorial_mul_factorial (hammingWeight_le x)
    exact_mod_cast hh
  have hr : (Fintype.card {e : Perm n // permuteInput e x = y} : ℝ) =
      ((hammingWeight x).factorial * (n - hammingWeight x).factorial : ℕ) := by
    apply mul_right_cancel₀ hchoose
    calc
      _ = (n.factorial : ℝ) := hprod
      _ = _ := by simpa only [mul_comm] using hcomb.symm
  exact_mod_cast hr

/-- Bounds on all nonempty Hamming layers yield one fixed pointwise family.
The original unsymmetrized family need not itself satisfy pointwise bounds. -/
theorem feasible_of_layer_bounds {n : ℕ} {I : Type} [Fintype I]
    {f : BooleanCube n → ZMod 2} {epsilon : ℝ} {d : ℕ}
    (hf : IsSymmetric f) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1)
    (hl : ∀ w : ℕ, w ≤ n → 1 - epsilon ≤ layerAverage (success f P mu) w) :
    HasProbabilisticDegreeAtMost f epsilon d := by
  apply feasible_of_orbit_bounds hf P mu hd hn hs
  intro x
  rw [orbitAverage_eq_layerAverage]
  exact hl (hammingWeight x) (hammingWeight_le x)

/-- Precisely scoped equivalence, preserving field, degree and real weights. -/
theorem feasible_iff_layer_average {n : ℕ} {f : BooleanCube n → ZMod 2}
    {epsilon : ℝ} {d : ℕ} (hf : IsSymmetric f) :
    HasProbabilisticDegreeAtMost f epsilon d ↔
      ∃ (m : ℕ) (P : Fin m → BinaryPolynomial n) (mu : Fin m → ℝ),
        (∀ i, (P i).totalDegree ≤ d) ∧ (∀ i, 0 ≤ mu i) ∧ (∑ i, mu i = 1) ∧
        (∀ w : ℕ, w ≤ n → 1 - epsilon ≤ layerAverage (success f P mu) w) := by
  constructor
  · rintro ⟨m, P, mu, hd, hn, hs, hp⟩
    refine ⟨m, P, mu, hd, hn, hs, ?_⟩
    intro w hw
    have hc : 0 < Fintype.card (Layer n w) := by
      rw [layer_card]
      exact Nat.choose_pos hw
    obtain ⟨x⟩ := Fintype.card_pos_iff.mp hc
    rw [← x.2, ← orbitAverage_eq_layerAverage]
    exact orbitAverage_lower_bound (success f P mu) (1 - epsilon) hp x.1
  · rintro ⟨m, P, mu, hd, hn, hs, hl⟩
    exact feasible_of_layer_bounds hf P mu hd hn hs hl

end
end PvsNPCartography.Symmetrization
