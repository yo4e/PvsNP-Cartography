import PvsNPCartography.BinomialPrefixBound
import PvsNPCartography.Mod3QuadraticObstruction

namespace PvsNPCartography.Mod3GrowingDegree

/-- The original predicate, with no assumed prefix bound or amplified success. -/
theorem obstruction (m d : ℕ) (hm : (16*d+2)^2 ≤ m) :
    ¬ HasProbabilisticDegreeAtMost (@SmallSupportMod3.target (m+2)) (1/3 : ℝ) d := by
  intro h
  have ha := MajorityAmplification.amplify (@SmallSupportMod3.target (m+2)) h
  rw [MajorityNumerics.tail15_exact] at ha
  have hn := Mod3ProductBound.necessary_inequality m (8*d) MajorityNumerics.deltaStar ha
  have hu := BinomialPrefixBound.bound_three_quarters m d hm
  have hg : (3/4 : ℝ) < 1-2*MajorityNumerics.deltaStar := by
    norm_num [MajorityNumerics.deltaStar]
  have hp : (0 : ℝ) < (2 : ℝ)^m := by positivity
  nlinarith [mul_pos (sub_pos.mpr hg) hp]

/-- A uniform growing-degree obstruction for every natural n,d.
Actual GF2 polynomials and arbitrary fixed finite REAL distributions are retained. -/
theorem degree_impossible (n d : ℕ) (hn : (16*d+2)^2+2 ≤ n) :
    ¬ HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) (1/3 : ℝ) d := by
  intro h
  exact obstruction ((16*d+2)^2) d le_rfl
    (Mod3Restrictions.restrict_le ((16*d+2)^2+2) n hn h)

/-- Equivalent necessary size constraint for any feasible degree. -/
theorem feasible_size_bound (n d : ℕ)
    (h : HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) (1/3 : ℝ) d) :
    n < (16*d+2)^2+2 :=
  lt_of_not_ge (fun hn => degree_impossible n d hn h)

/-- No fixed finite degree works at all large arities. -/
theorem excludes_every_fixed_degree (d : ℕ) :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
      ¬ HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) (1/3 : ℝ) d :=
  ⟨(16*d+2)^2+2, fun n hn => degree_impossible n d hn⟩

end PvsNPCartography.Mod3GrowingDegree
