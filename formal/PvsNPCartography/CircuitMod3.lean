import PvsNPCartography.SharedDAG
import PvsNPCartography.Mod3GrowingDegree

open scoped BigOperators

namespace PvsNPCartography.SharedDAG
open RandomizedGates Symmetrization
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Real error budget derived from the natural size/row inequality. -/
theorem error_budget (S r : ℕ) (hb : 3*S ≤ 2^r) :
    (S : ℝ)*(1/2 : ℝ)^r ≤ 1/3 := by
  have hh : 3*(S : ℝ) ≤ (2 : ℝ)^r := by exact_mod_cast hb
  have hi : (2 : ℝ)^r * (1/2 : ℝ)^r = 1 := by
    rw [← mul_pow]
    norm_num
  have hm := mul_le_mul_of_nonneg_right hh
    (by positivity : (0 : ℝ) ≤ (1/2 : ℝ)^r)
  nlinarith

/-- Upper bounds S,h may exceed the actual original-node count and output depth. -/
theorem feasible_third {n m K r : ℕ} (p : Program n K m) (w : Wire n m)
    (S h : ℕ) (hr : 1 ≤ r) (hs : cost p ≤ S) (hd : outputDepth p w ≤ h)
    (hb : 3*S ≤ 2^r) : HasProbabilisticDegreeAtMost (target p w) (1/3 : ℝ) (r^h) := by
  apply feasible_of_fintype (outputPoly p w) (matrixWeight K (r := r))
  · intro A
    exact (output_degree p w A hr).trans (pow_mono hr hd)
  · exact matrixWeight_nonneg K r
  · exact matrixWeight_sum K r
  · intro x
    have hp := output_success (r := r) p w x
    have hsr : (cost p : ℝ) ≤ (S : ℝ) := by exact_mod_cast hs
    have he : (cost p : ℝ)*(1/2 : ℝ)^r ≤ 1/3 :=
      (mul_le_mul_of_nonneg_right hsr (by positivity)).trans (error_budget S r hb)
    linarith

/-- Actual shared-DAG MOD3 consequence. Circuit correctness is the only target
premise; polynomial approximability, error estimates and degree bounds are derived. -/
theorem mod3_size_bound {n m K r : ℕ} (p : Program n K m) (w : Wire n m)
    (S h : ℕ) (hr : 1 ≤ r) (hs : cost p ≤ S) (hd : outputDepth p w ≤ h)
    (hb : 3*S ≤ 2^r) (hc : ∀ x, target p w x = SmallSupportMod3.target x) :
    n < (16*r^h+2)^2+2 := by
  have hf := feasible_third p w S h hr hs hd hb
  have he : target p w = @SmallSupportMod3.target n := funext hc
  rw [he] at hf
  exact Mod3GrowingDegree.feasible_size_bound n (r^h) hf

end
end PvsNPCartography.SharedDAG
