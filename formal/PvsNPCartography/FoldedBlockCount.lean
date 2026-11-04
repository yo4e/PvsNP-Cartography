import PvsNPCartography.BooleanIntegerReduction

open scoped BigOperators

namespace PvsNPCartography.FoldedBlockCount
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Coordinates not used by a tail monomial, including the empty tail. -/
def zeroCoords {b : ℕ} (k : Fin b → ℕ) : Finset (Fin b) :=
  Finset.univ.filter (fun j => k j = 0)

/-- Exact sum of any monomial on a Boolean tail. No squarefree premise is needed. -/
theorem tail_sum {b : ℕ} (k : Fin b → ℕ) :
    (∑ y : BooleanCube b, ∏ j, ((y j).val : ℤ) ^ k j) =
      (2 : ℤ) ^ (zeroCoords k).card := by
  calc
    _ = ∏ j, ∑ v : Fin 2, (v.val : ℤ) ^ k j := (Fintype.prod_sum _).symm
    _ = ∏ j, if k j = 0 then (2 : ℤ) else 1 := by
      apply Finset.prod_congr rfl
      intro j _
      by_cases h : k j = 0 <;> simp [Fin.sum_univ_two, h]
    _ = _ := by simp [zeroCoords, Finset.prod_ite]

/-- This is the usual 2^(b-t) factor, with the range guard derived from an actual support. -/
theorem zeroCoords_card {b : ℕ} (k : Fin b → ℕ) :
    (zeroCoords k).card = b - (Finset.univ.filter (fun j => k j ≠ 0)).card := by
  have h := Finset.card_filter_add_card_filter_not (s := (Finset.univ : Finset (Fin b)))
    (p := fun j => k j = 0)
  have hcard : (zeroCoords k).card +
      (Finset.univ.filter (fun j => k j ≠ 0)).card = b := by
    simpa only [zeroCoords, Finset.card_univ, Fintype.card_fin] using h
  exact Nat.eq_sub_of_add_eq hcard

/-- Use finite total-coordinate products, retaining all actual exponents. -/
theorem eval_full {m : ℕ} (P : MvPolynomial (Fin m) ℤ) (x : Fin m → ℤ) :
    MvPolynomial.eval x P = ∑ e ∈ P.support, P.coeff e * ∏ i, x i ^ e i := by
  have he := MvPolynomial.eval₂_eq (RingHom.id ℤ) x P
  simp only [MvPolynomial.eval₂_id, RingHom.id_apply] at he
  rw [he]
  apply Finset.sum_congr rfl
  intro e _
  congr 1
  apply Finset.prod_subset (Finset.subset_univ _)
  intro i _ hi
  have hz : e i = 0 := Finsupp.notMem_support_iff.mp hi
  simp [hz]

def tailFactor {a b : ℕ} (e : Fin (a+b) →₀ ℕ) : ℤ :=
  2 ^ (zeroCoords (fun j : Fin b => e (Fin.natAdd a j))).card

def headProduct {a b : ℕ} (e : Fin (a+b) →₀ ℕ) : MvPolynomial (Fin a) ℤ :=
  ∏ i : Fin a, MvPolynomial.X i ^ e (Fin.castAdd b i)

/-- Formed by coefficient arithmetic, with no enumeration of Boolean tail assignments. -/
def fold {a b : ℕ} (P : MvPolynomial (Fin (a+b)) ℤ) : MvPolynomial (Fin a) ℤ :=
  ∑ e ∈ P.support, MvPolynomial.C (P.coeff e * tailFactor e) * headProduct e

theorem headProduct_eval {a b : ℕ} (e : Fin (a+b) →₀ ℕ) (x : Fin a → ℤ) :
    MvPolynomial.eval x (headProduct e) = ∏ i, x i ^ e (Fin.castAdd b i) := by
  simp [headProduct, map_prod]

theorem joined_product {a b : ℕ} (e : Fin (a+b) →₀ ℕ)
    (x : BooleanCube a) (y : BooleanCube b) :
    (∏ i : Fin (a+b), IntegerPolynomialLift.joined x y i ^ e i) =
      (∏ i : Fin a, ((x i).val : ℤ) ^ e (Fin.castAdd b i)) *
      (∏ j : Fin b, ((y j).val : ℤ) ^ e (Fin.natAdd a j)) := by
  rw [Fin.prod_univ_add]
  simp [IntegerPolynomialLift.joined]

/-- The actual coefficient-folded polynomial equals the original Boolean tail sum. -/
theorem fold_eval {a b : ℕ} (P : MvPolynomial (Fin (a+b)) ℤ) (x : BooleanCube a) :
    MvPolynomial.eval (fun i => ((x i).val : ℤ)) (fold P) =
      ∑ y : BooleanCube b, MvPolynomial.eval (IntegerPolynomialLift.joined x y) P := by
  calc
    _ = ∑ e ∈ P.support, (P.coeff e * tailFactor e) *
        ∏ i : Fin a, ((x i).val : ℤ) ^ e (Fin.castAdd b i) := by
      simp [fold, map_sum, headProduct_eval]
    _ = ∑ e ∈ P.support, ∑ y : BooleanCube b, P.coeff e *
        ((∏ i : Fin a, ((x i).val : ℤ) ^ e (Fin.castAdd b i)) *
        ∏ j : Fin b, ((y j).val : ℤ) ^ e (Fin.natAdd a j)) := by
      apply Finset.sum_congr rfl
      intro e _
      rw [← Finset.mul_sum, ← Finset.mul_sum, tail_sum]
      unfold tailFactor
      ring
    _ = ∑ y : BooleanCube b, ∑ e ∈ P.support, P.coeff e *
        ((∏ i : Fin a, ((x i).val : ℤ) ^ e (Fin.castAdd b i)) *
        ∏ j : Fin b, ((y j).val : ℤ) ^ e (Fin.natAdd a j)) := Finset.sum_comm
    _ = _ := by
      apply Finset.sum_congr rfl
      intro y _
      rw [eval_full]
      simp_rw [joined_product]

/-- No source polynomial, no acceptance count and no desired equality is assumed away. -/
theorem exact_folded_count {a b : ℕ} (P : BinaryPolynomial (a+b)) (x : BooleanCube a) :
    MvPolynomial.eval (fun i => ((x i).val : ℤ))
      (fold (BooleanIntegerReduction.blockPolynomial b P)) % (2 : ℤ)^(b+1) =
      (IntegerPolynomialLift.acceptingCount P x : ℤ) := by
  rw [fold_eval]
  exact BooleanIntegerReduction.blockPolynomial_count P x

/-- Boolean input encoded by its set of one-coordinates. -/
def bits {a : ℕ} (T : Finset (Fin a)) : BooleanCube a := fun i => if i ∈ T then 1 else 0

def headSet {a b : ℕ} (e : Fin (a+b) →₀ ℕ) : Finset (Fin a) :=
  Finset.univ.filter (fun i => e (Fin.castAdd b i) ≠ 0)

/-- Folded coefficient table aggregates duplicates instead of dropping multiplicities. -/
def coefficients {a b : ℕ} (P : MvPolynomial (Fin (a+b)) ℤ)
    (S : Finset (Fin a)) : ℤ :=
  ∑ e ∈ P.support, if headSet e = S then P.coeff e * tailFactor e else 0

theorem headProduct_bits {a b : ℕ} (e : Fin (a+b) →₀ ℕ) (T : Finset (Fin a)) :
    (∏ i : Fin a, (((bits T) i).val : ℤ) ^ e (Fin.castAdd b i)) =
      if headSet e ⊆ T then 1 else 0 := by
  by_cases h : headSet e ⊆ T
  · rw [ite_eq_left h]
    apply Finset.prod_eq_one
    intro i _
    by_cases hi : e (Fin.castAdd b i) = 0
    · simp [hi]
    · have ht : i ∈ T := h (by simp [headSet, hi])
      simp [bits, ht]
  · rw [ite_eq_right h]
    obtain ⟨i, hi, ht⟩ := Finset.not_subset.mp h
    have hn : e (Fin.castAdd b i) ≠ 0 := (Finset.mem_filter.mp hi).2
    apply Finset.prod_eq_zero (Finset.mem_univ i)
    simp [bits, ht, hn]

/-- The subset sum is tied to the actual polynomial, not an arbitrary supplied oracle. -/
theorem subset_sum_eval {a b : ℕ} (P : MvPolynomial (Fin (a+b)) ℤ)
    (T : Finset (Fin a)) :
    (∑ S ∈ T.powerset, coefficients P S) =
      MvPolynomial.eval (fun i => (((bits T) i).val : ℤ)) (fold P) := by
  simp only [coefficients]
  rw [Finset.sum_comm]
  simp only [fold, map_sum, map_mul, MvPolynomial.eval_C, headProduct_eval,
    headProduct_bits]
  apply Finset.sum_congr rfl
  intro e _
  simp [Finset.mem_powerset, eq_comm]

/-- Exact canonical block count after coefficient folding and subset summation. -/
theorem exact_subset_count {a b : ℕ} (P : BinaryPolynomial (a+b))
    (T : Finset (Fin a)) :
    (∑ S ∈ T.powerset, coefficients (BooleanIntegerReduction.blockPolynomial b P) S) %
      (2 : ℤ)^(b+1) = (IntegerPolynomialLift.acceptingCount P (bits T) : ℤ) := by
  rw [subset_sum_eval]
  exact exact_folded_count P (bits T)

end
end PvsNPCartography.FoldedBlockCount
