import Mathlib

open scoped BigOperators

namespace PvsNPCartography

universe u v

/-- Finite weak duality for a pointwise success matrix, over real probabilities.

This is a certificate-conversion lemma, not a MOD3 theorem. `hdual` bounds
EVERY deterministic row of the chosen type I. A later application must prove
that I covers every allowed polynomial and must discharge hdual from the
actual certificate. Taking I to be a sample only excludes that sample.
No rational-probability restriction is imposed on the mixture.
-/
theorem finite_dual_obstruction
    {I : Type u} {X : Type v} [Fintype I] [Fintype X]
    (payoff : I → X → ℝ) (mu : I → ℝ) (q : X → ℝ) (b t : ℝ)
    (hmu_nonneg : ∀ i, 0 ≤ mu i) (hmu_sum : ∑ i, mu i = 1)
    (hq_nonneg : ∀ x, 0 ≤ q x) (hq_sum : ∑ x, q x = 1)
    (hdual : ∀ i, ∑ x, q x * payoff i x ≤ b) (hgap : b < t) :
    ¬ (∀ x, t ≤ ∑ i, mu i * payoff i x) := by
  intro hpoint
  have hlower : t ≤ ∑ x, q x * (∑ i, mu i * payoff i x) := by
    calc
      t = (∑ x, q x) * t := by rw [hq_sum]; simp
      _ = ∑ x, q x * t := by rw [Finset.sum_mul]
      _ ≤ ∑ x, q x * (∑ i, mu i * payoff i x) := by
        exact Finset.sum_le_sum fun x _ =>
          mul_le_mul_of_nonneg_left (hpoint x) (hq_nonneg x)
  have hupper : (∑ i, mu i * (∑ x, q x * payoff i x)) ≤ b := by
    calc
      (∑ i, mu i * (∑ x, q x * payoff i x)) ≤ ∑ i, mu i * b := by
        exact Finset.sum_le_sum fun i _ =>
          mul_le_mul_of_nonneg_left (hdual i) (hmu_nonneg i)
      _ = b := by rw [← Finset.sum_mul, hmu_sum]; simp
  have hexchange :
      (∑ x, q x * (∑ i, mu i * payoff i x)) =
        ∑ i, mu i * (∑ x, q x * payoff i x) := by
    calc
      (∑ x, q x * (∑ i, mu i * payoff i x)) =
          ∑ x, ∑ i, mu i * (q x * payoff i x) := by
        apply Finset.sum_congr rfl
        intro x _
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro i _
        ring
      _ = ∑ i, ∑ x, mu i * (q x * payoff i x) := Finset.sum_comm
      _ = ∑ i, mu i * (∑ x, q x * payoff i x) := by
        apply Finset.sum_congr rfl
        intro i _
        rw [Finset.mul_sum]
  rw [hexchange] at hlower
  exact (not_le_of_gt hgap) (le_trans hlower hupper)

end PvsNPCartography
