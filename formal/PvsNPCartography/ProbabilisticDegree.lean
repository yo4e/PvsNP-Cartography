import Mathlib

open scoped BigOperators

namespace PvsNPCartography

abbrev BooleanCube (n : ℕ) := Fin n → Fin 2
abbrev BinaryPolynomial (n : ℕ) := MvPolynomial (Fin n) (ZMod 2)

/-- Standard finite-support probabilistic polynomial definition, expressed by
success rather than error. Fin m indexes an arbitrary finite family, with
repetitions allowed; weights are REAL and the family is fixed BEFORE forall x.
All support polynomials have total degree <=d. This does not average over x. -/
def HasProbabilisticDegreeAtMost {n : ℕ} (f : BooleanCube n → ZMod 2)
    (epsilon : ℝ) (d : ℕ) : Prop :=
  ∃ (m : ℕ) (P : Fin m → BinaryPolynomial n) (mu : Fin m → ℝ),
    (∀ i, (P i).totalDegree ≤ d) ∧
    (∀ i, 0 ≤ mu i) ∧ (∑ i, mu i = 1) ∧
    (∀ x : BooleanCube n, 1 - epsilon ≤ ∑ i, mu i *
      (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (P i) = f x
        then 1 else 0))

theorem HasProbabilisticDegreeAtMost.mono {n : ℕ}
    {f : BooleanCube n → ZMod 2} {epsilon : ℝ} {d e : ℕ}
    (h : HasProbabilisticDegreeAtMost f epsilon d) (hde : d ≤ e) :
    HasProbabilisticDegreeAtMost f epsilon e := by
  obtain ⟨m, P, mu, hd, hn, hs, hp⟩ := h
  exact ⟨m, P, mu, fun i => (hd i).trans hde, hn, hs, hp⟩

/-- The least feasible degree, with an explicit existence witness. Requiring
existence prevents an empty-infimum convention from silently returning zero. -/
noncomputable def probabilisticDegree {n : ℕ} (f : BooleanCube n → ZMod 2)
    (epsilon : ℝ) (hexists : ∃ d, HasProbabilisticDegreeAtMost f epsilon d) : ℕ := by
  classical
  exact Nat.find hexists

/-- Negative-control boundary: swapping the existential family and the input
quantifier makes degree zero work for EVERY function. This is not the definition
above: the chosen constant depends on x. -/
theorem input_dependent_constant {n : ℕ} (f : BooleanCube n → ZMod 2)
    (x : BooleanCube n) :
    ∃ P : BinaryPolynomial n, P.totalDegree = 0 ∧
      MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) P = f x := by
  exact ⟨MvPolynomial.C (f x), by simp⟩

end PvsNPCartography
