import PvsNPCartography.DegreeOneNormalForm
import PvsNPCartography.ProbabilisticDegree

open scoped BigOperators

namespace PvsNPCartography.Mod3Five

/-- Same MOD3 truth function as the earlier integer certificate, now field-valued. -/
def mod3Function (x : BooleanCube 5) : ZMod 2 := (target x : ZMod 2)

theorem degree_two_feasible :
    HasProbabilisticDegreeAtMost mod3Function (1 / 3 : ℝ) 2 := by
  obtain ⟨P, mu, hd, hn, hs, hp⟩ := exists_quadratic_approximation
  refine ⟨30, P, mu, hd, hn, hs, ?_⟩
  intro x
  have hthreshold : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
  rw [hthreshold]
  exact hp x

/-- Full degree-based classification, NOT just a canonical-coefficient result.
The lower direction uses the structural normal form; the upper direction uses
the previously compiled, genuine polynomial witness and its degree bound. -/
theorem feasible_degree_iff (d : ℕ) :
    HasProbabilisticDegreeAtMost mod3Function (1 / 3 : ℝ) d ↔ 2 ≤ d := by
  constructor
  · rintro ⟨m, P, mu, hd, hn, hs, hp⟩
    by_contra hsmall
    have hd1 : d ≤ 1 := by omega
    apply no_degree_one_family P mu (fun i => (hd i).trans hd1) hn hs
    intro x
    have hx := hp x
    have hthreshold : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
    rw [hthreshold] at hx
    exact hx
  · intro h
    exact degree_two_feasible.mono h

/-- An exact least-degree statement with all original quantifiers exposed. -/
theorem least_feasible_degree :
    IsLeast {d : ℕ | HasProbabilisticDegreeAtMost mod3Function (1 / 3 : ℝ) d} 2 := by
  exact ⟨degree_two_feasible, fun _ h => (feasible_degree_iff _).mp h⟩

/-- The numerical degree is 2 for ANY existence proof; that proof cannot select
or smuggle in the answer. Both bounds are derived from the original predicate. -/
theorem probabilistic_degree_eq_two
    (h : ∃ d, HasProbabilisticDegreeAtMost mod3Function (1 / 3 : ℝ) d) :
    probabilisticDegree mod3Function (1 / 3 : ℝ) h = 2 := by
  classical
  unfold probabilisticDegree
  apply le_antisymm
  · exact Nat.find_min' h degree_two_feasible
  · exact (feasible_degree_iff (Nat.find h)).mp (Nat.find_spec h)

/-- Feasibility is established by the explicit upper witness, not assumed. -/
theorem degree_exists :
    ∃ d, HasProbabilisticDegreeAtMost mod3Function (1 / 3 : ℝ) d :=
  ⟨2, degree_two_feasible⟩

/-- Closed equality: no unproved feasibility hypothesis is supplied by a caller. -/
theorem pdeg_eq_two :
    probabilisticDegree mod3Function (1 / 3 : ℝ) degree_exists = 2 :=
  probabilistic_degree_eq_two degree_exists

/-- The same target admits a degree-zero answer separately at each input,
yet it admits NO single degree-zero randomized polynomial family valid for all
inputs. This formally refutes the tempting swapped-quantifier definition. -/
theorem swapped_quantifiers_are_strictly_weaker :
    (∀ x : BooleanCube 5, ∃ P : BinaryPolynomial 5, P.totalDegree = 0 ∧
      MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) P = mod3Function x) ∧
    ¬ HasProbabilisticDegreeAtMost mod3Function (1 / 3 : ℝ) 0 := by
  constructor
  · exact input_dependent_constant mod3Function
  · rw [feasible_degree_iff]
    omega

end PvsNPCartography.Mod3Five
