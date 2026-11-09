import PvsNPCartography.PointwiseCover

open scoped BigOperators

namespace PvsNPCartography.FixedProofTransfer
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Three signed occurrences may query the same address. A proof is a GLOBAL function. -/
structure Clause (X : Type*) where
  address : Fin 3 → X
  sign : Fin 3 → ZMod 2

def Accepts {X : Type*} (c : Clause X) (p : X → ZMod 2) : Prop :=
  ∃ j, p (c.address j) + c.sign j = 1

def failure {X : Type*} (c : Clause X) (p : X → ZMod 2) : ℝ :=
  if Accepts c p then 0 else 1

def acceptance {X T : Type*} [Fintype T] (c : T → Clause X)
    (nu : T → ℝ) (p : X → ZMod 2) : ℝ :=
  ∑ t, nu t * (if Accepts (c t) p then 1 else 0)

def errorRate {X T : Type*} [Fintype T] (c : T → Clause X)
    (nu : T → ℝ) (p : X → ZMod 2) : ℝ :=
  ∑ t, nu t * failure (c t) p

theorem acceptance_add_error {X T : Type*} [Fintype T]
    (c : T → Clause X) (nu : T → ℝ) (p : X → ZMod 2)
    (hs : ∑ t, nu t = 1) : acceptance c nu p + errorRate c nu p = 1 := by
  unfold acceptance errorRate failure
  rw [← Finset.sum_add_distrib]
  convert hs using 1
  apply Finset.sum_congr rfl
  intro t _
  by_cases h : Accepts (c t) p <;> simp [h]

/-- Fix a true literal BEFORE sampling. No independence among occurrences is required. -/
theorem one_true_literal {X : Type*} (c : Clause X) (p pi : X → ZMod 2)
    (j : Fin 3) (hj : pi (c.address j) + c.sign j = 1) :
    failure c p ≤ if p (c.address j) = pi (c.address j) then 0 else 1 := by
  by_cases he : p (c.address j) = pi (c.address j)
  · have ha : Accepts c p := ⟨j, by rw [he]; exact hj⟩
    simp [failure, he, ha]
  · simp only [he, ite_false]
    unfold failure
    split_ifs <;> norm_num

/-- Success-to-error conversion retains the ORIGINAL normalized finite real measure. -/
theorem pointwise_error {X I : Type*} [Fintype I]
    (pi : X → ZMod 2) (p : I → X → ZMod 2) (mu : I → ℝ) (epsilon : ℝ)
    (hs : ∑ i, mu i = 1)
    (hp : ∀ x, 1 - epsilon ≤ ∑ i, mu i * (if p i x = pi x then 1 else 0))
    (x : X) : (∑ i, mu i * (if p i x = pi x then (0 : ℝ) else 1)) ≤ epsilon := by
  have hc :
      (∑ i, mu i * (if p i x = pi x then (0 : ℝ) else 1)) +
      (∑ i, mu i * (if p i x = pi x then (1 : ℝ) else 0)) = 1 := by
    rw [← Finset.sum_add_distrib]
    convert hs using 1
    apply Finset.sum_congr rfl
    intro i _
    by_cases h : p i x = pi x <;> simp [h]
  linarith [hp x]

/-- The sharp epsilon bound, rather than a three-epsilon union bound. -/
theorem clause_error {X I : Type*} [Fintype I]
    (pi : X → ZMod 2) (p : I → X → ZMod 2) (mu : I → ℝ) (epsilon : ℝ)
    (hn : ∀ i, 0 ≤ mu i)
    (hp : ∀ x, (∑ i, mu i * (if p i x = pi x then (0 : ℝ) else 1)) ≤ epsilon)
    (c : Clause X) (hc : Accepts c pi) :
    (∑ i, mu i * failure c (p i)) ≤ epsilon := by
  obtain ⟨j, hj⟩ := hc
  calc
    _ ≤ ∑ i, mu i * (if p i (c.address j) = pi (c.address j) then 0 else 1) := by
      apply Finset.sum_le_sum
      intro i _
      exact mul_le_mul_of_nonneg_left (one_true_literal c (p i) pi j hj) (hn i)
    _ ≤ epsilon := hp (c.address j)

/-- Arbitrary nonnegative normalized TEST weights; one sample still precedes all tests. -/
theorem average_error {X I T : Type*} [Fintype I] [Fintype T]
    (pi : X → ZMod 2) (p : I → X → ZMod 2)
    (mu : I → ℝ) (nu : T → ℝ) (epsilon : ℝ) (c : T → Clause X)
    (hm : ∀ i, 0 ≤ mu i) (hn : ∀ t, 0 ≤ nu t) (hs : ∑ t, nu t = 1)
    (hp : ∀ x, (∑ i, mu i * (if p i x = pi x then (0 : ℝ) else 1)) ≤ epsilon)
    (hc : ∀ t, Accepts (c t) pi) :
    (∑ i, mu i * errorRate c nu (p i)) ≤ epsilon := by
  calc
    _ = ∑ t, nu t * (∑ i, mu i * failure (c t) (p i)) := by
      simp only [errorRate, Finset.mul_sum]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro t _
      apply Finset.sum_congr rfl
      intro i _
      ring
    _ ≤ ∑ t, nu t * epsilon := by
      apply Finset.sum_le_sum
      intro t _
      exact mul_le_mul_of_nonneg_left (clause_error pi p mu epsilon hm hp (c t) (hc t)) (hn t)
    _ = epsilon := by rw [← Finset.sum_mul, hs, one_mul]

/-- Zero-mass rows cannot witness the conclusion. Repeated queries and zero test weights survive. -/
theorem fixed_positive_sample {X I T : Type*} [Fintype I] [Fintype T]
    (pi : X → ZMod 2) (p : I → X → ZMod 2)
    (mu : I → ℝ) (nu : T → ℝ) (epsilon : ℝ) (c : T → Clause X)
    (hm : ∀ i, 0 ≤ mu i) (hms : ∑ i, mu i = 1)
    (hn : ∀ t, 0 ≤ nu t) (hns : ∑ t, nu t = 1)
    (hp : ∀ x, 1 - epsilon ≤ ∑ i, mu i * (if p i x = pi x then 1 else 0))
    (hc : ∀ t, Accepts (c t) pi) :
    ∃ i, 0 < mu i ∧ 1 - epsilon ≤ acceptance c nu (p i) := by
  have he := average_error pi p mu nu epsilon c hm hn hns
    (pointwise_error pi p mu epsilon hms hp) hc
  obtain ⟨i, hi, hh⟩ := PointwiseCover.positive_support_le mu
    (fun i => errorRate c nu (p i)) epsilon hm hms he
  refine ⟨i, hi, ?_⟩
  have ha := acceptance_add_error c nu (p i) hns
  linarith

/-- The original actual-polynomial/REAL-mixture predicate supplies the SINGLE polynomial. -/
theorem exists_good_polynomial {n d : ℕ} {T : Type*} [Fintype T]
    (pi : BooleanCube n → ZMod 2) (epsilon : ℝ)
    (c : T → Clause (BooleanCube n)) (nu : T → ℝ)
    (hn : ∀ t, 0 ≤ nu t) (hs : ∑ t, nu t = 1)
    (hc : ∀ t, Accepts (c t) pi)
    (hp : HasProbabilisticDegreeAtMost pi epsilon d) :
    ∃ P : BinaryPolynomial n, P.totalDegree ≤ d ∧
      1 - epsilon ≤ acceptance c nu (PointwiseCover.row P) := by
  obtain ⟨m, P, mu, hd, hm, hms, hx⟩ := hp
  obtain ⟨i, _hi, ha⟩ := fixed_positive_sample pi (fun i => PointwiseCover.row (P i))
    mu nu epsilon c hm hms hn hs hx hc
  exact ⟨P i, hd i, ha⟩

/-- Soundness applies to ALL global proof functions, hence every guessed polynomial. -/
theorem polynomial_soundness {n : ℕ} {T : Type*} [Fintype T]
    (c : T → Clause (BooleanCube n)) (nu : T → ℝ) (delta epsilon : ℝ)
    (hs : ∀ pi : BooleanCube n → ZMod 2, acceptance c nu pi ≤ 1 - delta)
    (hgap : epsilon < delta) (P : BinaryPolynomial n) :
    acceptance c nu (PointwiseCover.row P) < 1 - epsilon := by
  have h := hs (PointwiseCover.row P)
  linarith

end
end PvsNPCartography.FixedProofTransfer
