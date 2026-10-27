import PvsNPCartography.MajorityAmplification
import PvsNPCartography.MajorityNumerics
import PvsNPCartography.Mod3Restrictions

namespace PvsNPCartography.Mod3QuadraticObstruction

/-- Original-predicate exclusion at n299, with every missing bridge discharged. -/
theorem at_299 :
    ¬ HasProbabilisticDegreeAtMost (@SmallSupportMod3.target 299) (1/3 : ℝ) 2 := by
  intro h
  have ha := MajorityAmplification.amplify (@SmallSupportMod3.target 299) h
  rw [MajorityNumerics.tail15_exact] at ha
  exact Mod3ProductBound.no_mod3_approximation 297 16 MajorityNumerics.deltaStar
    MajorityNumerics.strict_gap ha

/-- All n>=299, actual GF2 total-degree<=2 and arbitrary fixed finite REAL
probability distributions. This is not an exact degree3 or optimal-threshold claim. -/
theorem degree_two_impossible (n : ℕ) (hn : 299 ≤ n) :
    ¬ HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) (1/3 : ℝ) 2 := by
  intro h
  exact at_299 (Mod3Restrictions.restrict_le 299 n hn h)

end PvsNPCartography.Mod3QuadraticObstruction
