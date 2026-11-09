import PvsNPCartography.SignedProjection
import PvsNPCartography.SubsetZeta

open scoped BigOperators

namespace PvsNPCartography.FixedProofCounting
open FixedProofTransfer SignedProjection
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Every head subset and every tail assignment is retained, including empty blocks. -/
def join {a b : ℕ} (x : BooleanCube a) (y : BooleanCube b) : BooleanCube (a+b) :=
  Fin.addCases x y

def blockOutput {a b : ℕ} (Q : BinaryPolynomial (a+b)) (T : Finset (Fin a)) : ℤ :=
  SubsetZeta.transform (FoldedBlockCount.coefficients (BooleanIntegerReduction.blockPolynomial b Q)) T %
    (2 : ℤ)^(b+1)

/-- Connect the ACTUAL signed clause polynomial to the original proof's queried bits. -/
theorem block_count {n a b : ℕ} (P : BinaryPolynomial n)
    (q : Fin 3 → Fin n → Coordinate (a+b)) (s : Fin 3 → ZMod 2) (T : Finset (Fin a)) :
    blockOutput (clausePolynomial P q s) T =
      ((Finset.univ.filter (fun y : BooleanCube b =>
        Accepts (clauseAt q s (join (FoldedBlockCount.bits T) y)) (PointwiseCover.row P))).card : ℤ) := by
  have he : IntegerPolynomialLift.acceptingCount (clausePolynomial P q s)
      (FoldedBlockCount.bits T) =
      (Finset.univ.filter (fun y : BooleanCube b =>
        Accepts (clauseAt q s (join (FoldedBlockCount.bits T) y)) (PointwiseCover.row P))).card := by
    unfold IntegerPolynomialLift.acceptingCount
    congr 1
    ext y
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    simpa only [PointwiseCover.row, IntegerPolynomialLift.joined, join, Int.cast_natCast] using
      clause_semantics P q s (join (FoldedBlockCount.bits T) y)
  unfold blockOutput
  rw [SubsetZeta.exact_count, he]

abbrev Test (I : Type*) (a b : ℕ) := I × (Finset (Fin a) × BooleanCube b)

def tests {I : Type*} {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2) :
    Test I a b → Clause (BooleanCube n) :=
  fun t => clauseAt (q t.1) (s t.1) (join (FoldedBlockCount.bits t.2.1) t.2.2)

def totalOutput {I : Type*} [Fintype I] {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (P : BinaryPolynomial n) : ℤ :=
  ∑ i, ∑ T : Finset (Fin a), blockOutput (clausePolynomial P (q i) (s i)) T

/-- Summation of actual block residues is the cardinality of the actual test set. -/
theorem total_count {I : Type*} [Fintype I] {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (P : BinaryPolynomial n) :
    totalOutput q s P =
      ((Finset.univ.filter (fun t : Test I a b => Accepts (tests q s t) (PointwiseCover.row P))).card : ℤ) := by
  unfold totalOutput
  simp_rw [block_count]
  calc
    _ = ∑ i : I, ∑ T : Finset (Fin a), ∑ y : BooleanCube b,
        if Accepts (tests q s (i,T,y)) (PointwiseCover.row P) then (1 : ℤ) else 0 := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro T _
      have h (pred : BooleanCube b → Prop) :
          ((Finset.univ.filter pred).card : ℤ) =
            ∑ y : BooleanCube b, if pred y then (1 : ℤ) else 0 := by simp
      exact h (fun y => Accepts (tests q s (i,T,y)) (PointwiseCover.row P))
    _ = ∑ t : Test I a b, if Accepts (tests q s t) (PointwiseCover.row P) then (1 : ℤ) else 0 := by
      simp only [Fintype.sum_prod_type]
    _ = _ := by simp

theorem test_card {I : Type*} [Fintype I] (a b : ℕ) :
    Fintype.card (Test I a b) = Fintype.card I * 2^(a+b) := by
  simp [Test, BooleanCube, pow_add]

def uniformWeight {T : Type*} [Fintype T] (_t : T) : ℝ := (Fintype.card T : ℝ)⁻¹

theorem uniform_nonneg {T : Type*} [Fintype T] (t : T) : 0 ≤ uniformWeight t := by
  unfold uniformWeight
  positivity

theorem uniform_sum {T : Type*} [Fintype T] [Nonempty T] :
    (∑ t : T, uniformWeight t) = 1 := by
  simp [uniformWeight, Fintype.card_ne_zero]

theorem uniform_acceptance {X T : Type*} [Fintype T]
    (c : T → Clause X) (p : X → ZMod 2) :
    acceptance c uniformWeight p =
      ((Finset.univ.filter (fun t => Accepts (c t) p)).card : ℝ) / (Fintype.card T : ℝ) := by
  unfold acceptance uniformWeight
  rw [← Finset.mul_sum]
  have he : (∑ t : T, if Accepts (c t) p then (1 : ℝ) else 0) =
      ((Finset.univ.filter (fun t => Accepts (c t) p)).card : ℝ) := by simp
  rw [he]
  ring

/-- Exact rational comparison by integer cross multiplication, not floating point. -/
theorem threshold_iff {I : Type*} [Fintype I] [Nonempty I] {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (P : BinaryPolynomial n) (u v : ℕ) (hv : 0 < v) :
    (u : ℝ) / v ≤ acceptance (tests q s) uniformWeight (PointwiseCover.row P) ↔
      (u : ℤ) * (Fintype.card (Test I a b) : ℤ) ≤ (v : ℤ) * totalOutput q s P := by
  have hvR : (0 : ℝ) < (v : ℝ) := by exact_mod_cast hv
  have hNR : (0 : ℝ) < (Fintype.card (Test I a b) : ℝ) := by
    exact_mod_cast Fintype.card_pos (α := Test I a b)
  rw [uniform_acceptance, div_le_div_iff₀ hvR hNR, total_count]
  constructor
  · intro h
    have hh : (u : ℤ) * (Fintype.card (Test I a b) : ℤ) ≤
        ((Finset.univ.filter (fun t : Test I a b => Accepts (tests q s t) (PointwiseCover.row P))).card : ℤ) * (v : ℤ) := by
      exact_mod_cast h
    simpa only [mul_comm] using hh
  · intro h
    have hh : (u : ℝ) * (Fintype.card (Test I a b) : ℝ) ≤
        (v : ℝ) * ((Finset.univ.filter (fun t : Test I a b => Accepts (tests q s t) (PointwiseCover.row P))).card : ℝ) := by
      exact_mod_cast h
    nlinarith

/-- Completeness starts at the original probabilistic-degree predicate and ends in a count test. -/
theorem exists_count_witness {I : Type*} [Fintype I] [Nonempty I] {n a b d : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (pi : BooleanCube n → ZMod 2) (epsilon : ℝ) (u v : ℕ) (hv : 0 < v)
    (hr : (u : ℝ) / v ≤ 1 - epsilon)
    (hc : ∀ t, Accepts (tests q s t) pi)
    (hp : HasProbabilisticDegreeAtMost pi epsilon d) :
    ∃ P : BinaryPolynomial n, P.totalDegree ≤ d ∧
      (∀ i, (clausePolynomial P (q i) (s i)).totalDegree ≤ 3*d) ∧
      (u : ℤ) * (Fintype.card (Test I a b) : ℤ) ≤ (v : ℤ) * totalOutput q s P := by
  obtain ⟨P, hd, ha⟩ := exists_good_polynomial pi epsilon (tests q s) uniformWeight
    uniform_nonneg uniform_sum hc hp
  exact ⟨P, hd, fun i => clause_degree P (q i) (s i) hd,
    (threshold_iff q s P u v hv).mp (hr.trans ha)⟩

/-- Global-proof soundness excludes EVERY guessed polynomial, not merely the support witness. -/
theorem rejects_all_polynomials {I : Type*} [Fintype I] [Nonempty I] {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (bound : ℝ) (u v : ℕ) (hv : 0 < v) (hg : bound < (u : ℝ) / v)
    (hs : ∀ pi : BooleanCube n → ZMod 2, acceptance (tests q s) uniformWeight pi ≤ bound)
    (P : BinaryPolynomial n) :
    (v : ℤ) * totalOutput q s P < (u : ℤ) * (Fintype.card (Test I a b) : ℤ) := by
  have ha := lt_of_le_of_lt (hs (PointwiseCover.row P)) hg
  apply lt_of_not_ge
  intro h
  exact (not_le_of_gt ha) ((threshold_iff q s P u v hv).mpr h)

end
end PvsNPCartography.FixedProofCounting
