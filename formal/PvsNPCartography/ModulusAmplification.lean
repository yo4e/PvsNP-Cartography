import PvsNPCartography.ProbabilisticDegree

open scoped BigOperators

namespace PvsNPCartography.ModulusAmplification
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Bernstein term, over an actual ring rather than a probability space. -/
def term {R : Type*} [CommRing R] (s j : ℕ) (y : R) : R :=
  y^j * (1-y)^(2*s-1-j) * ((2*s-1).choose j : R)

/-- Explicit integer-coefficient modulus amplifier; also used on actual polynomials. -/
def amplify {R : Type*} [CommRing R] (s : ℕ) (y : R) : R :=
  ∑ j ∈ Finset.range (2*s), if s ≤ j then term s j y else 0

def remainder {R : Type*} [CommRing R] (s : ℕ) (y : R) : R :=
  ∑ j ∈ Finset.range (2*s), if j < s then term s j y else 0

theorem split_one {R : Type*} [CommRing R] (s : ℕ) (hs : 1 ≤ s) (y : R) :
    amplify s y + remainder s y = 1 := by
  have hk : 2*s-1+1 = 2*s := by omega
  calc
    _ = ∑ j ∈ Finset.range (2*s), term s j y := by
      unfold amplify remainder
      rw [← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro j _
      by_cases hj : j < s
      · simp [hj, Nat.not_le_of_lt hj]
      · simp [hj, Nat.le_of_not_gt hj]
    _ = (y+(1-y))^(2*s-1) := by
      simpa only [term, hk] using (add_pow y (1-y) (2*s-1)).symm
    _ = 1 := by simp

/-- Divisibility proof includes negative integer y and does not assume y is a bit. -/
theorem two_pow_dvd {s j : ℕ} (y : ℤ) (hy : 2 ∣ y) (hj : s ≤ j) :
    (2 : ℤ)^s ∣ y^j := by
  obtain ⟨z, rfl⟩ := hy
  refine ⟨2^(j-s)*z^j, ?_⟩
  rw [mul_pow, ← mul_assoc, ← pow_add]
  have he : s + (j-s) = j := by omega
  rw [he]

theorem even_divisible (s : ℕ) (y : ℤ) (hy : 2 ∣ y) :
    (2 : ℤ)^s ∣ amplify s y := by
  apply Finset.dvd_sum
  intro j _
  by_cases hj : s ≤ j
  · simp only [ite_eq_left hj, term]
    exact dvd_mul_of_dvd_left (dvd_mul_of_dvd_left (two_pow_dvd y hy hj) _) _
  · simp [hj]

theorem odd_complement_divisible (s : ℕ) (hs : 1 ≤ s) (y : ℤ)
    (hy : 2 ∣ 1-y) : (2 : ℤ)^s ∣ 1-amplify s y := by
  have hr : (2 : ℤ)^s ∣ remainder s y := by
    apply Finset.dvd_sum
    intro j hj
    have hjr : j < 2*s := Finset.mem_range.mp hj
    by_cases hjs : j < s
    · simp only [ite_eq_left hjs, term]
      exact dvd_mul_of_dvd_left (dvd_mul_of_dvd_right
        (two_pow_dvd (1-y) hy (by omega : s ≤ 2*s-1-j)) _) _
    · simp [hjs]
  have he := split_one s hs y
  have : 1-amplify s y = remainder s y := by linarith
  rw [this]
  exact hr

/-- ALL integers, with the original parity interpreted as its canonical 0/1 value. -/
theorem parity_congruence (s : ℕ) (hs : 1 ≤ s) (y : ℤ) :
    amplify s y ≡ y % 2 [ZMOD (2 : ℤ)^s] := by
  have h0 : 0 ≤ y % 2 := Int.emod_nonneg y (by norm_num)
  have h1 : y % 2 < 2 := Int.emod_lt_of_pos y (by norm_num)
  have hy : y % 2 = 0 ∨ y % 2 = 1 := by omega
  rcases hy with hy | hy
  · rw [hy]
    exact Int.modEq_zero_iff_dvd.mpr
      (even_divisible s y (Int.dvd_iff_emod_eq_zero.mpr hy))
  · rw [hy]
    apply Int.modEq_iff_dvd.mpr
    apply odd_complement_divisible s hs y
    apply Int.dvd_iff_emod_eq_zero.mpr
    omega

/-- Ring homomorphisms commute with the actual algebraic construction. -/
theorem map_amplify {R S : Type*} [CommRing R] [CommRing S]
    (f : R →+* S) (s : ℕ) (y : R) : f (amplify s y) = amplify s (f y) := by
  unfold amplify
  rw [map_sum]
  apply Finset.sum_congr rfl
  intro j _
  by_cases hj : s ≤ j <;> simp [hj, term]

theorem polynomial_degree {σ : Type*} (P : MvPolynomial σ ℤ) (s d : ℕ)
    (hs : 1 ≤ s) (hd : P.totalDegree ≤ d) :
    (amplify s P).totalDegree ≤ (2*s-1)*d := by
  have hc : (1-P).totalDegree ≤ d := by
    have he : (1-P) = MvPolynomial.C (-1) * P + MvPolynomial.C 1 := by simp [sub_eq_add_neg, add_comm]
    rw [he]
    exact (MvPolynomial.totalDegree_add _ _).trans (by
      have h := (MvPolynomial.totalDegree_mul (MvPolynomial.C (-1)) P).trans
        (by simpa using hd)
      simpa using h)
  apply MvPolynomial.totalDegree_finsetSum_le
  intro j hj
  have hjr : j < 2*s := Finset.mem_range.mp hj
  by_cases hjs : s ≤ j
  · simp only [ite_eq_left hjs, term]
    have hn : (((2*s-1).choose j : ℕ) : MvPolynomial σ ℤ).totalDegree = 0 := by
      have he : (((2*s-1).choose j : ℕ) : MvPolynomial σ ℤ) =
          MvPolynomial.C ((2*s-1).choose j : ℤ) := by simp
      rw [he, MvPolynomial.totalDegree_C]
    calc
      _ ≤ (P^j * (1-P)^(2*s-1-j)).totalDegree + 0 := by
        simpa only [hn] using MvPolynomial.totalDegree_mul
          (P^j * (1-P)^(2*s-1-j)) (((2*s-1).choose j : ℕ) : MvPolynomial σ ℤ)
      _ ≤ j*d + (2*s-1-j)*d := by
        have hp := (MvPolynomial.totalDegree_pow P j).trans (Nat.mul_le_mul_left j hd)
        have hq := (MvPolynomial.totalDegree_pow (1-P) (2*s-1-j)).trans
          (Nat.mul_le_mul_left (2*s-1-j) hc)
        have h := MvPolynomial.totalDegree_mul (P^j) ((1-P)^(2*s-1-j))
        omega
      _ = (2*s-1)*d := by
        rw [← Nat.add_mul]
        congr 1
        omega
  · simp [hjs]

/-- An actual univariate integer polynomial (encoded with one variable). -/
def amplifier (s : ℕ) : MvPolynomial (Fin 1) ℤ := amplify s (MvPolynomial.X 0)

theorem amplifier_degree (s : ℕ) (hs : 1 ≤ s) :
    (amplifier s).totalDegree ≤ 2*s-1 := by
  simpa [amplifier] using polynomial_degree (MvPolynomial.X (0 : Fin 1)) s 1 hs (by simp)

theorem amplifier_eval (s : ℕ) (y : ℤ) :
    MvPolynomial.eval (fun _ : Fin 1 => y) (amplifier s) = amplify s y := by
  simp [amplifier, map_amplify]

def oddCount {X : Type*} [Fintype X] (v : X → ℤ) : ℕ :=
  (Finset.univ.filter (fun x => v x % 2 = 1)).card

theorem parity_sum {X : Type*} [Fintype X] (v : X → ℤ) :
    (∑ x, v x % 2) = (oddCount v : ℤ) := by
  have he (x : X) : v x % 2 = if v x % 2 = 1 then (1 : ℤ) else 0 := by
    have h0 := Int.emod_nonneg (v x) (by norm_num : (2 : ℤ) ≠ 0)
    have h1 := Int.emod_lt_of_pos (v x) (by norm_num : (0 : ℤ) < 2)
    split_ifs <;> omega
  calc
    _ = ∑ x, if v x % 2 = 1 then (1 : ℤ) else 0 :=
      Finset.sum_congr rfl (fun x _ => he x)
    _ = (oddCount v : ℤ) := by simp [oddCount]

/-- No hidden no-wrap premise: only a bound on the actual finite domain size. -/
theorem sum_no_wrap {X : Type*} [Fintype X] (v : X → ℤ) (s : ℕ) (hs : 1 ≤ s)
    (hX : (Fintype.card X : ℤ) < (2 : ℤ)^s) :
    (∑ x, amplify s (v x)) % (2 : ℤ)^s = (oddCount v : ℤ) := by
  have hcon : (∑ x, amplify s (v x)) ≡ (∑ x, v x % 2) [ZMOD (2 : ℤ)^s] := by
    apply Int.modEq_iff_dvd.mpr
    rw [← Finset.sum_sub_distrib]
    exact Finset.dvd_sum (fun x _ => (parity_congruence s hs (v x)).dvd)
  rw [parity_sum] at hcon
  have hc : oddCount v ≤ Fintype.card X := Finset.card_filter_le _ _
  have hb : (oddCount v : ℤ) < (2 : ℤ)^s := lt_of_le_of_lt (by exact_mod_cast hc) hX
  exact hcon.eq.trans (Int.emod_eq_of_lt (by positivity) hb)

/-- Summing over ell Boolean bits requires modulus 2^(ell+1), including ell=0. -/
theorem boolean_block_no_wrap (ell : ℕ) (v : BooleanCube ell → ℤ) :
    (∑ x, amplify (ell+1) (v x)) % (2 : ℤ)^(ell+1) = (oddCount v : ℤ) := by
  apply sum_no_wrap v (ell+1) (by omega)
  have hp : (0 : ℤ) < 2^ell := by positivity
  have hc : Fintype.card (BooleanCube ell) = 2^ell := by simp [BooleanCube]
  rw [hc]
  push_cast
  rw [pow_succ]
  linarith

end
end PvsNPCartography.ModulusAmplification
