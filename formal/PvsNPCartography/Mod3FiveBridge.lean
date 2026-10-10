import PvsNPCartography.Mod3FiveUpper

open scoped BigOperators

namespace PvsNPCartography.Mod3Five

set_option maxRecDepth 100000
set_option maxHeartbeats 8000000

noncomputable def affinePolynomial (p : Affine) : MvPolynomial (Fin 5) (ZMod 2) :=
  MvPolynomial.C (p.1.val : ZMod 2) +
    ∑ i, MvPolynomial.C ((p.2 i).val : ZMod 2) * MvPolynomial.X i

/-- Checks the correctness bit, not just the value modulo two. -/
theorem affine_field_correct :
    ∀ (p : Affine) (x : Cube), affineCorrect p x =
      if (p.1.val : ZMod 2) + ∑ i, (p.2 i).val * (x i).val =
        (target x : ZMod 2) then 1 else 0 := by
  decide +kernel

theorem affine_polynomial_correct (p : Affine) (x : Cube) :
    payoff p x =
      if MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (affinePolynomial p) =
        (target x : ZMod 2) then 1 else 0 := by
  unfold payoff
  rw [affine_field_correct]
  simp [affinePolynomial]

/-- Arbitrary finite indexed families, including duplicated coefficient rows
and irrational real probabilities. No normalization of a sampled subfamily
is confused with exhaustive coverage of the coefficient type Affine. -/
theorem no_affine_polynomial_family
    {I : Type} [Fintype I] (a : I → Affine) (mu : I → ℝ)
    (hmu_nonneg : ∀ i, 0 ≤ mu i) (hmu_sum : ∑ i, mu i = 1) :
    ¬ (∀ x : Cube, (2 : ℝ) / 3 ≤ ∑ i, mu i *
      (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (affinePolynomial (a i)) =
        (target x : ZMod 2) then 1 else 0)) := by
  have h := PvsNPCartography.finite_dual_obstruction
    (fun i x => payoff (a i) x) mu inputProb ((11 : ℝ) / 18) ((2 : ℝ) / 3)
    hmu_nonneg hmu_sum inputProb_nonneg inputProb_sum
    (fun i => deterministic_bound (a i)) (by norm_num)
  simpa only [affine_polynomial_correct] using h

/-- A concrete countermodel to dropping the q-normalization hypothesis from
finite duality. The genuine theorem retains that hypothesis. -/
theorem zero_mass_is_not_probability :
    (∑ _ : Fin 1, (0 : ℝ)) = 0 ∧
    (∀ _ : Fin 1, (0 : ℝ) * 1 ≤ 0) ∧
    (0 : ℝ) < 2 / 3 ∧
    (∀ _ : Fin 1, (2 : ℝ) / 3 ≤ ∑ _ : Fin 1, (1 : ℝ) * 1) := by
  norm_num

end PvsNPCartography.Mod3Five
