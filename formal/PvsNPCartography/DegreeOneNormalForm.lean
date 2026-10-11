import PvsNPCartography.Mod3FiveBridge

open scoped BigOperators

namespace PvsNPCartography

/-- A monomial of total exponent at most one is constant or a single variable.
This is a structural statement, not an enumeration truncated at a chosen degree. -/
theorem exponent_sum_le_one {σ : Type*} (s : σ →₀ ℕ)
    (h : s.sum (fun _ e => e) ≤ 1) :
    s = 0 ∨ ∃ i, s = Finsupp.single i 1 := by
  classical
  have hc : s.toMultiset.card ≤ 1 := by simpa [Function.id_def] using h
  have cases : s.toMultiset.card = 0 ∨ s.toMultiset.card = 1 := by omega
  rcases cases with hzero | hone
  · left
    have hm := Multiset.card_eq_zero.mp hzero
    simpa using congrArg (fun m : Multiset σ => Multiset.toFinsupp m) hm
  · obtain ⟨i, hi⟩ := Multiset.card_eq_one.mp hone
    right
    refine ⟨i, ?_⟩
    have hm := congrArg (fun m : Multiset σ => Multiset.toFinsupp m) hi
    simpa using hm

/-- Structural normal form for ANY degree-at-most-one multivariate polynomial.
The coefficient semiring and finite variable type are arbitrary. No MOD3 bound
or property of the truth table is assumed here. -/
theorem degree_one_normal_form {σ R : Type*} [Fintype σ] [CommSemiring R]
    (P : MvPolynomial σ R) (hP : P.totalDegree ≤ 1) :
    P = MvPolynomial.C (P.coeff 0) +
      ∑ i, MvPolynomial.C (P.coeff (Finsupp.single i 1)) * MvPolynomial.X i := by
  classical
  apply MvPolynomial.ext
  intro s
  by_cases hs0 : s = 0
  · subst s
    simp [MvPolynomial.coeff_X]
  · by_cases hs1 : ∃ i, s = Finsupp.single i 1
    · obtain ⟨i, rfl⟩ := hs1
      have hsingle : ∀ j : σ,
          (Finsupp.single j (1 : ℕ) = Finsupp.single i 1) ↔ j = i := by
        intro j
        constructor
        · intro heq
          have hm := congrArg Finsupp.toMultiset heq
          simpa using hm
        · intro heq
          subst j
          rfl
      simp [MvPolynomial.coeff_X, hsingle, Ne.symm hs0]
    · have hcoeff : P.coeff s = 0 := by
        by_contra hne
        have hexp := exponent_sum_le_one s
          ((MvPolynomial.le_totalDegree (MvPolynomial.mem_support_iff.mpr hne)).trans hP)
        exact hexp.elim hs0 hs1
      have hsingle : ∀ i : σ, Finsupp.single i (1 : ℕ) ≠ s := by
        intro i hi
        exact hs1 ⟨i, hi.symm⟩
      simp [MvPolynomial.coeff_X, Ne.symm hs0, hsingle, hcoeff]

namespace Mod3Five

/-- ZMod 2 is represented by Fin 2, so this keeps ALL binary coefficients. -/
noncomputable def coefficientRow (P : MvPolynomial (Fin 5) (ZMod 2)) : Affine :=
  (P.coeff 0, fun i => P.coeff (Finsupp.single i 1))

/-- The missing coverage bridge: actual polynomial equality, not just agreement
on sampled inputs. Every degree-one Mathlib object reaches the canonical class. -/
theorem degree_one_eq_affine (P : MvPolynomial (Fin 5) (ZMod 2))
    (hP : P.totalDegree ≤ 1) : P = affinePolynomial (coefficientRow P) := by
  change P = MvPolynomial.C (((P.coeff 0).val : ℕ) : ZMod 2) +
    ∑ i, MvPolynomial.C (((P.coeff (Finsupp.single i 1)).val : ℕ) : ZMod 2) *
      MvPolynomial.X i
  simp only [ZMod.natCast_zmod_val]
  exact degree_one_normal_form P hP

/-- No normalized REAL mixture of arbitrary degree-at-most-one polynomials
approximates MOD3 on every five-bit input. Degree and coverage are discharged. -/
theorem no_degree_one_family
    {I : Type} [Fintype I] (P : I → MvPolynomial (Fin 5) (ZMod 2))
    (mu : I → ℝ) (hdegree : ∀ i, (P i).totalDegree ≤ 1)
    (hnonneg : ∀ i, 0 ≤ mu i) (hsum : ∑ i, mu i = 1) :
    ¬ (∀ x : Cube, (2 : ℝ) / 3 ≤ ∑ i, mu i *
      (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (P i) =
        (target x : ZMod 2) then 1 else 0)) := by
  have h := no_affine_polynomial_family (fun i => coefficientRow (P i)) mu hnonneg hsum
  have heq : ∀ i, affinePolynomial (coefficientRow (P i)) = P i :=
    fun i => (degree_one_eq_affine (P i) (hdegree i)).symm
  simpa only [heq] using h

end Mod3Five
end PvsNPCartography
