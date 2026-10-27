import PvsNPCartography.SmallSupportMod3
import PvsNPCartography.AgreementConsequences

open scoped BigOperators

namespace PvsNPCartography.GF4Transport

noncomputable section
attribute [local instance] Classical.propDecidable

/-- A concrete, nonempty four-element field, not a hypothetical extension. -/
abbrev K := GaloisField 2 2
local instance : Fintype K := Fintype.ofFinite K

def embed : ZMod 2 →+* K := algebraMap (ZMod 2) K

theorem card_four : Fintype.card K = 4 := by
  simpa [Nat.card_eq_fintype_card] using GaloisField.card 2 2 (by decide)

theorem exists_nonbinary : ∃ w : K, w ≠ 0 ∧ w ≠ 1 := by
  classical
  by_contra h
  have hx (x : K) : x = 0 ∨ x = 1 := by
    by_cases h0 : x = 0
    · exact Or.inl h0
    by_cases h1 : x = 1
    · exact Or.inr h1
    exact False.elim (h ⟨x, h0, h1⟩)
  have hs : (Finset.univ : Finset K) ⊆ {0, 1} := by
    intro x _
    simpa using hx x
  have hc := Finset.card_le_card hs
  rw [Finset.card_univ, card_four] at hc
  have ht : ({0, 1} : Finset K).card ≤ 2 := Finset.card_pair_le _ _
  omega

def omega : K := Classical.choose exists_nonbinary

theorem omega_ne_zero : omega ≠ 0 := (Classical.choose_spec exists_nonbinary).1

theorem omega_ne_one : omega ≠ 1 := (Classical.choose_spec exists_nonbinary).2

theorem omega_cube : omega ^ 3 = 1 := by
  simpa [card_four] using FiniteField.pow_card_sub_one_eq_one omega omega_ne_zero

theorem omega_quadratic : omega ^ 2 + omega + 1 = 0 := by
  have hp : (omega - 1) * (omega ^ 2 + omega + 1) = 0 := by
    calc
      _ = omega ^ 3 - 1 := by ring
      _ = 0 := by rw [omega_cube]; ring
  exact (mul_eq_zero.mp hp).resolve_left (sub_ne_zero.mpr omega_ne_one)

theorem two_zero : (2 : K) = 0 := CharP.cast_eq_zero K 2

theorem omega_square_add : omega ^ 2 + omega = 1 := by
  linear_combination omega_quadratic - two_zero

theorem omega_square_add_one : omega ^ 2 + 1 = omega := by
  linear_combination omega_quadratic - omega * two_zero

/-- The two residue indicators encode the full three-valued root target. -/
theorem root_encoding (w : ℕ) :
    omega ^ 2 + omega * embed (if w % 3 = 0 then 1 else 0) +
      embed (if (w + 2) % 3 = 0 then 1 else 0) = omega ^ w := by
  have hp : omega ^ w = omega ^ (w % 3) := by
    conv_lhs => rw [← Nat.mod_add_div w 3]
    rw [pow_add, pow_mul, omega_cube, one_pow, mul_one]
  rw [hp]
  have hm : w % 3 = 0 ∨ w % 3 = 1 ∨ w % 3 = 2 := by omega
  rcases hm with h | h | h <;>
    simp [h, Nat.add_mod, omega_square_add, omega_square_add_one]

/-- Total degree is preserved under any affine substitution and coefficient map.
This lemma is used for constant padding and the actual inverse-grid variables. -/
theorem affine_substitution_degree {A B σ τ : Type*}
    [CommSemiring A] [CommSemiring B] (f : A →+* B)
    (v : σ → MvPolynomial τ B) (hv : ∀ i, (v i).totalDegree ≤ 1)
    (P : MvPolynomial σ A) :
    (MvPolynomial.eval₂ (MvPolynomial.C.comp f) v P).totalDegree ≤ P.totalDegree := by
  classical
  rw [MvPolynomial.eval₂_eq]
  apply MvPolynomial.totalDegree_finsetSum_le
  intro e he
  have hprod : (∏ i ∈ e.support, v i ^ e i).totalDegree ≤ e.sum (fun _ k => k) := by
    calc
      _ ≤ ∑ i ∈ e.support, (v i ^ e i).totalDegree :=
        MvPolynomial.totalDegree_finsetProd _ _
      _ ≤ ∑ i ∈ e.support, e i := by
        apply Finset.sum_le_sum
        intro i _
        exact (MvPolynomial.totalDegree_pow _ _).trans
          (by simpa using Nat.mul_le_mul_left (e i) (hv i))
      _ = e.sum (fun _ k => k) := rfl
  have hm := MvPolynomial.totalDegree_mul
    (MvPolynomial.C (f (P.coeff e))) (∏ i ∈ e.support, v i ^ e i)
  simp only [MvPolynomial.totalDegree_C, zero_add] at hm
  exact hm.trans (hprod.trans (MvPolynomial.le_totalDegree he))

/-- Two constant coordinates are prepended. MOD3 depends only on their sum. -/
def pad {m : ℕ} (b : Fin 2) (x : BooleanCube m) : BooleanCube (m + 2) :=
  Fin.cons b (Fin.cons b x)

theorem pad_weight {m : ℕ} (b : Fin 2) (x : BooleanCube m) :
    (∑ i, (pad b x i).val) = 2 * b.val + ∑ i, (x i).val := by
  simp only [pad, Fin.sum_univ_succ, Fin.cons_zero, Fin.cons_succ]
  omega

theorem encoded_targets {m : ℕ} (x : BooleanCube m) :
    omega ^ 2 + omega * embed (SmallSupportMod3.target (pad 0 x)) +
      embed (SmallSupportMod3.target (pad 1 x)) = omega ^ (∑ i, (x i).val) := by
  simpa [SmallSupportMod3.target, pad_weight, Nat.add_comm] using
    root_encoding (∑ i, (x i).val)

/-- Decode actual grid points, not a multiset of binary encodings. -/
def decode {m : ℕ} (y : Fin m → K) : BooleanCube m :=
  fun j => if y j = 1 then 0 else 1

def inverseVariable {m : ℕ} (j : Fin m) : MvPolynomial (Fin m) K :=
  (MvPolynomial.X j - MvPolynomial.C 1) * MvPolynomial.C ((omega - 1)⁻¹)

theorem inverseVariable_degree {m : ℕ} (j : Fin m) :
    (inverseVariable j).totalDegree ≤ 1 := by
  have hs := MvPolynomial.totalDegree_sub
    (MvPolynomial.X j : MvPolynomial (Fin m) K) (MvPolynomial.C 1)
  have hm := MvPolynomial.totalDegree_mul
    (MvPolynomial.X j - MvPolynomial.C 1 : MvPolynomial (Fin m) K)
    (MvPolynomial.C ((omega - 1)⁻¹))
  simp only [MvPolynomial.totalDegree_X, MvPolynomial.totalDegree_C] at hs hm
  unfold inverseVariable
  omega

theorem decode_coordinate {m : ℕ} (y : Fin m → K)
    (hy : ∀ j, y j = 1 ∨ y j = omega) (j : Fin m) :
    MvPolynomial.eval y (inverseVariable j) = ((decode y j).val : K) := by
  have hn : omega - 1 ≠ 0 := sub_ne_zero.mpr omega_ne_one
  rcases hy j with h | h
  · simp [inverseVariable, decode, h]
  · simp [inverseVariable, decode, h, omega_ne_one, hn]

theorem product_decode {m : ℕ} (y : Fin m → K)
    (hy : ∀ j, y j = 1 ∨ y j = omega) :
    (∏ j, y j) = omega ^ (∑ j, (decode y j).val) := by
  have hc (j : Fin m) : y j = omega ^ (decode y j).val := by
    rcases hy j with h | h <;> simp [decode, h, omega_ne_one]
  have hp (S : Finset (Fin m)) :
      (∏ j ∈ S, omega ^ (decode y j).val) = omega ^ (∑ j ∈ S, (decode y j).val) := by
    classical
    induction S using Finset.induction_on with
    | empty => simp
    | @insert i S hi ih => simp [hi, ih, pow_add]
  simp_rw [hc]
  exact hp Finset.univ

def paddedVariables {m : ℕ} (b : Fin 2) : Fin (m + 2) → MvPolynomial (Fin m) K :=
  Fin.cons (MvPolynomial.C (b.val : K))
    (Fin.cons (MvPolynomial.C (b.val : K)) inverseVariable)

def pulled {m : ℕ} (b : Fin 2) (P : BinaryPolynomial (m + 2)) :
    MvPolynomial (Fin m) K :=
  MvPolynomial.eval₂ (MvPolynomial.C.comp embed) (paddedVariables b) P

theorem pulled_degree {m : ℕ} (b : Fin 2) (P : BinaryPolynomial (m + 2)) :
    (pulled b P).totalDegree ≤ P.totalDegree := by
  apply affine_substitution_degree
  intro j
  refine Fin.cases ?_ (fun j => Fin.cases ?_ (fun k => ?_) j) j
  · simp [paddedVariables]
  · simp [paddedVariables]
  · simpa [paddedVariables] using inverseVariable_degree k

theorem pulled_eval {m : ℕ} (b : Fin 2) (P : BinaryPolynomial (m + 2))
    (y : Fin m → K) (hy : ∀ j, y j = 1 ∨ y j = omega) :
    MvPolynomial.eval y (pulled b P) = embed
      (MvPolynomial.eval (fun j => ((pad b (decode y) j).val : ZMod 2)) P) := by
  have hc : (MvPolynomial.eval y).comp (MvPolynomial.C.comp embed) = embed := by
    ext c
    simp
  have hv : (fun j => MvPolynomial.eval y (paddedVariables b j)) =
      (fun j => embed ((pad b (decode y) j).val : ZMod 2)) := by
    funext j
    refine Fin.cases ?_ (fun j => Fin.cases ?_ (fun k => ?_) j) j
    · simp [paddedVariables, pad]
    · simp [paddedVariables, pad]
    · simpa [paddedVariables, pad] using decode_coordinate y hy k
  rw [pulled, MvPolynomial.eval_eval₂, hc, hv,
    MvPolynomial.eval₂_eq, MvPolynomial.eval_eq]
  simp only [map_sum, map_mul, map_prod, map_pow]

/-- Linear root encoding. One original polynomial supplies BOTH restrictions. -/
def transported {m : ℕ} (P : BinaryPolynomial (m + 2)) : MvPolynomial (Fin m) K :=
  MvPolynomial.C (omega ^ 2) + MvPolynomial.C omega * pulled 0 P + pulled 1 P

theorem transported_degree {m : ℕ} (P : BinaryPolynomial (m + 2)) :
    (transported P).totalDegree ≤ P.totalDegree := by
  have h0 := pulled_degree 0 P
  have h1 := pulled_degree 1 P
  have hm := MvPolynomial.totalDegree_mul (MvPolynomial.C omega) (pulled 0 P)
  have ha := MvPolynomial.totalDegree_add (MvPolynomial.C (omega ^ 2))
    (MvPolynomial.C omega * pulled 0 P)
  have hb := MvPolynomial.totalDegree_add
    (MvPolynomial.C (omega ^ 2) + MvPolynomial.C omega * pulled 0 P) (pulled 1 P)
  simp only [MvPolynomial.totalDegree_C] at hm ha
  unfold transported
  omega

theorem transported_correct {m : ℕ} (P : BinaryPolynomial (m + 2))
    (y : Fin m → K) (hy : ∀ j, y j = 1 ∨ y j = omega)
    (h0 : MvPolynomial.eval (fun j => ((pad 0 (decode y) j).val : ZMod 2)) P =
      SmallSupportMod3.target (pad 0 (decode y)))
    (h1 : MvPolynomial.eval (fun j => ((pad 1 (decode y) j).val : ZMod 2)) P =
      SmallSupportMod3.target (pad 1 (decode y))) :
    MvPolynomial.eval y (transported P) = ∏ j, y j := by
  simp only [transported, map_add, map_mul, MvPolynomial.eval_C,
    pulled_eval _ _ y hy, h0, h1]
  rw [encoded_targets, product_decode y hy]

end
end PvsNPCartography.GF4Transport
