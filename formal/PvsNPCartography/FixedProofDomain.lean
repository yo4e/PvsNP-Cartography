import PvsNPCartography.FixedProofCounting
import PvsNPCartography.HammingLayers

open scoped BigOperators

namespace PvsNPCartography.FixedProofDomain
open FixedProofTransfer SignedProjection FixedProofCounting
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Actual inverse laws, not just equality of domain cardinalities. -/
def assignmentEquiv (a b : ℕ) :
    (Finset (Fin a) × BooleanCube b) ≃ BooleanCube (a+b) where
  toFun t := join (FoldedBlockCount.bits t.1) t.2
  invFun z := (Symmetrization.ones (fun i => z (Fin.castAdd b i)),
    fun j => z (Fin.natAdd a j))
  left_inv := by
    rintro ⟨T, y⟩
    apply Prod.ext
    · simpa only [join, Fin.addCases_left, FoldedBlockCount.bits, Symmetrization.bits] using
        Symmetrization.ones_bits T
    · funext j
      simp [join]
  right_inv := by
    intro z
    funext i
    refine Fin.addCases (fun j => ?_) (fun j => ?_) i
    · simpa only [join, Fin.addCases_left, FoldedBlockCount.bits, Symmetrization.bits] using
        congrFun (Symmetrization.bits_ones (fun j : Fin a => z (Fin.castAdd b j))) j
    · simp [join]

def testEquiv (I : Type*) (a b : ℕ) : Test I a b ≃ (I × BooleanCube (a+b)) :=
  Equiv.prodCongr (Equiv.refl I) (assignmentEquiv a b)

def cubeTests {I : Type*} {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2) :
    (I × BooleanCube (a+b)) → Clause (BooleanCube n) :=
  fun t => clauseAt (q t.1) (s t.1) t.2

/-- Uniform acceptance is invariant under a proved bijection, even on empty domains. -/
theorem uniform_reindex {A B X : Type*} [Fintype A] [Fintype B]
    (e : A ≃ B) (c : B → Clause X) (pi : X → ZMod 2) :
    acceptance (fun t => c (e t)) uniformWeight pi = acceptance c uniformWeight pi := by
  unfold acceptance uniformWeight
  rw [Fintype.card_congr e]
  exact e.sum_comp (fun t : B => (Fintype.card B : ℝ)⁻¹ *
    (if Accepts (c t) pi then (1 : ℝ) else 0))

theorem cube_acceptance {I : Type*} [Fintype I] {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (pi : BooleanCube n → ZMod 2) :
    acceptance (tests q s) uniformWeight pi = acceptance (cubeTests q s) uniformWeight pi :=
  uniform_reindex (testEquiv I a b) (cubeTests q s) pi

/-- The integer endpoint is for the ORIGINAL full randomness cube, with no multiplicities. -/
theorem cube_threshold {I : Type*} [Fintype I] [Nonempty I] {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (P : BinaryPolynomial n) (u v : ℕ) (hv : 0 < v) :
    (u : ℝ) / v ≤ acceptance (cubeTests q s) uniformWeight (PointwiseCover.row P) ↔
      (u : ℤ) * ((Fintype.card I * 2^(a+b) : ℕ) : ℤ) ≤ (v : ℤ) * totalOutput q s P := by
  rw [← cube_acceptance]
  simpa only [test_card] using threshold_iff q s P u v hv

/-- One original polynomial simultaneously supplies all signed clause/count tests. -/
theorem cube_count_witness {I : Type*} [Fintype I] [Nonempty I] {n a b d : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (pi : BooleanCube n → ZMod 2) (epsilon : ℝ) (u v : ℕ) (hv : 0 < v)
    (hr : (u : ℝ) / v ≤ 1 - epsilon)
    (hc : ∀ i z, Accepts (clauseAt (q i) (s i) z) pi)
    (hp : HasProbabilisticDegreeAtMost pi epsilon d) :
    ∃ P : BinaryPolynomial n, P.totalDegree ≤ d ∧
      (∀ i, (clausePolynomial P (q i) (s i)).totalDegree ≤ 3*d) ∧
      (u : ℤ) * ((Fintype.card I * 2^(a+b) : ℕ) : ℤ) ≤ (v : ℤ) * totalOutput q s P := by
  obtain ⟨P, hd, hq, ht⟩ := exists_count_witness q s pi epsilon u v hv hr
    (fun t => hc t.1 _) hp
  exact ⟨P, hd, hq, by simpa only [test_card] using ht⟩

/-- The soundness premise ranges over global proofs on the original queried address cube. -/
theorem cube_rejects_all {I : Type*} [Fintype I] [Nonempty I] {n a b : ℕ}
    (q : I → Fin 3 → Fin n → Coordinate (a+b)) (s : I → Fin 3 → ZMod 2)
    (bound : ℝ) (u v : ℕ) (hv : 0 < v) (hg : bound < (u : ℝ) / v)
    (hs : ∀ pi : BooleanCube n → ZMod 2,
      acceptance (cubeTests q s) uniformWeight pi ≤ bound)
    (P : BinaryPolynomial n) :
    (v : ℤ) * totalOutput q s P < (u : ℤ) * ((Fintype.card I * 2^(a+b) : ℕ) : ℤ) := by
  have he (pi : BooleanCube n → ZMod 2) : acceptance (tests q s) uniformWeight pi ≤ bound := by
    rw [cube_acceptance]
    exact hs pi
  simpa only [test_card] using rejects_all_polynomials q s bound u v hv hg he P

end
end PvsNPCartography.FixedProofDomain
