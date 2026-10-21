import PvsNPCartography.HammingProfiles
import PvsNPCartography.SmallSupportMod3

open scoped BigOperators

namespace PvsNPCartography.CliqueProfiles

open Symmetrization HammingProfiles

noncomputable section

/-- A genuine squarefree monomial, not a truth-table label. -/
def subsetMonomial {n : ℕ} (S : Finset (Fin n)) : BinaryPolynomial n :=
  ∏ i ∈ S, MvPolynomial.X i

/-- Elementary symmetric polynomial on A, including degrees zero and one. -/
def elementary {n : ℕ} (A : Finset (Fin n)) (d : ℕ) : BinaryPolynomial n :=
  ∑ S ∈ A.powersetCard d, subsetMonomial S

theorem subsetMonomial_degree {n : ℕ} (S : Finset (Fin n)) :
    (subsetMonomial S).totalDegree ≤ S.card := by
  classical
  induction S using Finset.induction_on with
  | empty => simp [subsetMonomial]
  | @insert i S hi ih =>
    have he : subsetMonomial (insert i S) = MvPolynomial.X i * subsetMonomial S := by
      simp only [subsetMonomial, Finset.prod_insert hi]
    rw [he, Finset.card_insert_of_notMem hi]
    calc
      _ ≤ (MvPolynomial.X i : BinaryPolynomial n).totalDegree +
        (subsetMonomial S).totalDegree := MvPolynomial.totalDegree_mul _ _
      _ ≤ S.card + 1 := by simpa only [MvPolynomial.totalDegree_X] using Nat.add_le_add_left ih 1

theorem elementary_degree {n : ℕ} (A : Finset (Fin n)) (d : ℕ) :
    (elementary A d).totalDegree ≤ d := by
  unfold elementary
  apply MvPolynomial.totalDegree_finsetSum_le
  intro S hS
  exact (subsetMonomial_degree S).trans_eq (Finset.mem_powersetCard.mp hS).2

private theorem bit_as_indicator {n : ℕ} (x : BooleanCube n) (i : Fin n) :
    ((x i).val : ZMod 2) = if i ∈ ones x then 1 else 0 := by
  classical
  by_cases hi : x i = 1
  · simp [ones, hi]
  · have hv : (x i).val = 0 := by
      have hlt := (x i).isLt
      have hne : (x i).val ≠ 1 := by
        intro h
        exact hi (Fin.ext h)
      omega
    simp [ones, hi, hv]

theorem subsetMonomial_eval {n : ℕ} (S : Finset (Fin n)) (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (subsetMonomial S) =
      if S ⊆ ones x then (1 : ZMod 2) else 0 := by
  classical
  simp only [subsetMonomial, map_prod, MvPolynomial.eval_X]
  by_cases hs : S ⊆ ones x
  · rw [ite_eq_left hs]
    apply Finset.prod_eq_one
    intro i hi
    rw [bit_as_indicator, ite_eq_left (hs hi)]
  · rw [ite_eq_right hs]
    obtain ⟨i, hi, hn⟩ := Finset.not_subset.mp hs
    apply Finset.prod_eq_zero hi
    rw [bit_as_indicator, ite_eq_right hn]

/-- Actual evaluation counts d-subsets of the active coordinates, in GF(2).
The binomial count is formed in the naturals BEFORE casting into the field. -/
theorem elementary_eval {n : ℕ} (A : Finset (Fin n)) (d : ℕ) (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (elementary A d) =
      ((overlap A x).choose d : ZMod 2) := by
  classical
  simp only [elementary, map_sum]
  simp_rw [subsetMonomial_eval]
  have hf : (A.powersetCard d).filter (fun S => S ⊆ ones x) =
      (A ∩ ones x).powersetCard d := by
    ext S
    simp only [Finset.mem_filter, Finset.mem_powersetCard, Finset.subset_inter_iff]
    tauto
  rw [← Finset.sum_filter, hf]
  simp only [Finset.sum_const, nsmul_eq_mul, mul_one, Finset.card_powersetCard]
  rw [Finset.inter_comm]
  rfl

theorem overlap_univ {n : ℕ} (x : BooleanCube n) :
    overlap Finset.univ x = hammingWeight x := by
  simp [overlap, ones_card]

theorem overlap_complement {n : ℕ} (A : Finset (Fin n)) (x : BooleanCube n) :
    overlap (Finset.univ \ A) x = hammingWeight x - overlap A x := by
  classical
  have he : ones x ∩ (Finset.univ \ A) = ones x \ A := by
    ext i
    simp
  have hc := Finset.card_sdiff_add_card_inter (ones x) A
  rw [ones_card] at hc
  unfold overlap
  rw [he]
  omega

/-- q_A = 1 + sum of all variables + the clique quadratic on A. -/
def q {n : ℕ} (A : Finset (Fin n)) : BinaryPolynomial n :=
  1 + elementary Finset.univ 1 + elementary A 2

/-- r_A = 1 + sum of variables outside A + the clique quadratic on A. -/
def r {n : ℕ} (A : Finset (Fin n)) : BinaryPolynomial n :=
  1 + elementary (Finset.univ \ A) 1 + elementary A 2

private theorem degree_template {n : ℕ} (A B : Finset (Fin n)) :
    (1 + elementary B 1 + elementary A 2).totalDegree ≤ 2 := by
  apply (MvPolynomial.totalDegree_add _ _).trans
  apply max_le
  · apply (MvPolynomial.totalDegree_add _ _).trans
    apply max_le
    · simp
    · exact (elementary_degree B 1).trans (by decide)
  · exact elementary_degree A 2

theorem q_degree {n : ℕ} (A : Finset (Fin n)) : (q A).totalDegree ≤ 2 :=
  degree_template A Finset.univ

theorem r_degree {n : ℕ} (A : Finset (Fin n)) : (r A).totalDegree ≤ 2 :=
  degree_template A (Finset.univ \ A)

theorem q_eval {n : ℕ} (A : Finset (Fin n)) (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (q A) =
      1 + (hammingWeight x : ZMod 2) + ((overlap A x).choose 2 : ZMod 2) := by
  simp only [q, map_add, map_one, elementary_eval, overlap_univ, Nat.choose_one_right]

theorem r_eval {n : ℕ} (A : Finset (Fin n)) (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (r A) =
      1 + ((hammingWeight x - overlap A x : ℕ) : ZMod 2) +
        ((overlap A x).choose 2 : ZMod 2) := by
  simp only [r, map_add, map_one, elementary_eval, overlap_complement, Nat.choose_one_right]

def qGood (w k : ℕ) : ℝ :=
  if (1 + (w : ZMod 2) + (k.choose 2 : ZMod 2)) =
    (if w % 3 = 0 then 1 else 0 : ZMod 2) then 1 else 0

def rGood (w k : ℕ) : ℝ :=
  if (1 + ((w-k : ℕ) : ZMod 2) + (k.choose 2 : ZMod 2)) =
    (if w % 3 = 0 then 1 else 0 : ZMod 2) then 1 else 0

theorem q_correct {n : ℕ} (A : Finset (Fin n)) (x : BooleanCube n) :
    correct SmallSupportMod3.target (q A) x = qGood (hammingWeight x) (overlap A x) := by
  unfold correct
  rw [q_eval]
  rfl

theorem r_correct {n : ℕ} (A : Finset (Fin n)) (x : BooleanCube n) :
    correct SmallSupportMod3.target (r A) x = rGood (hammingWeight x) (overlap A x) := by
  unfold correct
  rw [r_eval]
  rfl

/-- The actual polynomial's layer correctness, not an assumed profile. -/
theorem q_layer_sum {n : ℕ} (A : Finset (Fin n)) (w : ℕ) :
    (∑ x : Layer n w, correct SmallSupportMod3.target (q A) x.1) =
      ∑ k ∈ Finset.range (w+1),
        (A.card.choose k : ℝ) * ((n-A.card).choose (w-k) : ℝ) * qGood w k := by
  calc
    _ = ∑ x : Layer n w, qGood w (overlap A x.1) := by
      apply Finset.sum_congr rfl
      intro x _
      rw [q_correct, x.2]
    _ = _ := weighted_layer_sum A w (qGood w)

theorem r_layer_sum {n : ℕ} (A : Finset (Fin n)) (w : ℕ) :
    (∑ x : Layer n w, correct SmallSupportMod3.target (r A) x.1) =
      ∑ k ∈ Finset.range (w+1),
        (A.card.choose k : ℝ) * ((n-A.card).choose (w-k) : ℝ) * rGood w k := by
  calc
    _ = ∑ x : Layer n w, rGood w (overlap A x.1) := by
      apply Finset.sum_congr rfl
      intro x _
      rw [r_correct, x.2]
    _ = _ := weighted_layer_sum A w (rGood w)

theorem q_layer_mean {n : ℕ} (A : Finset (Fin n)) (w : ℕ) :
    layerAverage (correct SmallSupportMod3.target (q A)) w =
      (∑ k ∈ Finset.range (w+1),
        (A.card.choose k : ℝ) * ((n-A.card).choose (w-k) : ℝ) * qGood w k) /
      (n.choose w : ℝ) := by
  unfold layerAverage
  rw [q_layer_sum, layer_card]

theorem r_layer_mean {n : ℕ} (A : Finset (Fin n)) (w : ℕ) :
    layerAverage (correct SmallSupportMod3.target (r A)) w =
      (∑ k ∈ Finset.range (w+1),
        (A.card.choose k : ℝ) * ((n-A.card).choose (w-k) : ℝ) * rGood w k) /
      (n.choose w : ℝ) := by
  unfold layerAverage
  rw [r_layer_sum, layer_card]

end
end PvsNPCartography.CliqueProfiles
