import PvsNPCartography.GF4Transport
import PvsNPCartography.FixedProofTransfer

open scoped BigOperators

namespace PvsNPCartography.SignedProjection
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Exactly the allowed 1-local coordinates; no unrestricted evaluation oracle. -/
inductive Coordinate (r : ℕ) where
  | constant (b : Fin 2)
  | positive (j : Fin r)
  | negative (j : Fin r)

def Coordinate.value {r : ℕ} : Coordinate r → BooleanCube r → Fin 2
  | .constant b, _ => b
  | .positive j, x => x j
  | .negative j, x => if (x j).val = 0 then 1 else 0

def Coordinate.polynomial {r : ℕ} : Coordinate r → BinaryPolynomial r
  | .constant b => MvPolynomial.C (b.val : ZMod 2)
  | .positive j => MvPolynomial.X j
  | .negative j => MvPolynomial.C 1 - MvPolynomial.X j

theorem Coordinate.degree {r : ℕ} (q : Coordinate r) :
    q.polynomial.totalDegree ≤ 1 := by
  cases q with
  | constant b => simp [Coordinate.polynomial]
  | positive j => simp [Coordinate.polynomial]
  | negative j =>
    simpa [Coordinate.polynomial] using
      (MvPolynomial.totalDegree_sub (MvPolynomial.C 1) (MvPolynomial.X j : BinaryPolynomial r))

theorem Coordinate.eval {r : ℕ} (q : Coordinate r) (x : BooleanCube r) :
    PointwiseCover.row q.polynomial x = ((q.value x).val : ZMod 2) := by
  cases q with
  | constant b => simp [PointwiseCover.row, Coordinate.polynomial, Coordinate.value]
  | positive j => simp [PointwiseCover.row, Coordinate.polynomial, Coordinate.value]
  | negative j =>
    have h : (x j).val = 0 ∨ (x j).val = 1 := by have := (x j).isLt; omega
    rcases h with h | h <;>
      simp [PointwiseCover.row, Coordinate.polynomial, Coordinate.value, h]

def query {n r : ℕ} (q : Fin n → Coordinate r) (x : BooleanCube r) : BooleanCube n :=
  fun j => (q j).value x

def substitute {n r : ℕ} (q : Fin n → Coordinate r) (P : BinaryPolynomial n) :
    BinaryPolynomial r :=
  MvPolynomial.eval₂ (MvPolynomial.C.comp (RingHom.id (ZMod 2)))
    (fun j => (q j).polynomial) P

theorem substitute_degree {n r : ℕ} (q : Fin n → Coordinate r) (P : BinaryPolynomial n) :
    (substitute q P).totalDegree ≤ P.totalDegree :=
  GF4Transport.affine_substitution_degree _ _ (fun j => Coordinate.degree (q j)) P

theorem substitute_eval {n r : ℕ} (q : Fin n → Coordinate r) (P : BinaryPolynomial n)
    (x : BooleanCube r) : PointwiseCover.row (substitute q P) x =
      PointwiseCover.row P (query q x) := by
  have hc : (MvPolynomial.eval (fun j => ((x j).val : ZMod 2))).comp
      (MvPolynomial.C.comp (RingHom.id (ZMod 2))) = RingHom.id (ZMod 2) := by
    ext c
    simp
  have hv : (fun j => MvPolynomial.eval (fun k => ((x k).val : ZMod 2))
      (q j).polynomial) = (fun j => ((query q x j).val : ZMod 2)) := by
    funext j
    exact Coordinate.eval (q j) x
  unfold PointwiseCover.row substitute
  rw [MvPolynomial.eval_eval₂, hc, hv, MvPolynomial.eval₂_id]

/-- A sign of one negates a bit over GF2. -/
def literal {n r : ℕ} (P : BinaryPolynomial n) (q : Fin n → Coordinate r)
    (s : ZMod 2) : BinaryPolynomial r := substitute q P + MvPolynomial.C s

theorem literal_degree {n r d : ℕ} (P : BinaryPolynomial n)
    (q : Fin n → Coordinate r) (s : ZMod 2) (hd : P.totalDegree ≤ d) :
    (literal P q s).totalDegree ≤ d := by
  have h := MvPolynomial.totalDegree_add (substitute q P) (MvPolynomial.C s)
  have hq := (substitute_degree q P).trans hd
  simp only [MvPolynomial.totalDegree_C, max_zero] at h
  exact h.trans hq

theorem literal_eval {n r : ℕ} (P : BinaryPolynomial n)
    (q : Fin n → Coordinate r) (s : ZMod 2) (x : BooleanCube r) :
    PointwiseCover.row (literal P q s) x = PointwiseCover.row P (query q x) + s := by
  simpa [literal, PointwiseCover.row] using congrArg (fun z : ZMod 2 => z + s)
    (substitute_eval q P x)

def clausePolynomial {n r : ℕ} (P : BinaryPolynomial n)
    (q : Fin 3 → Fin n → Coordinate r) (s : Fin 3 → ZMod 2) : BinaryPolynomial r :=
  MvPolynomial.C 1 - ∏ j : Fin 3, (MvPolynomial.C 1 - literal P (q j) (s j))

def clauseAt {n r : ℕ} (q : Fin 3 → Fin n → Coordinate r)
    (s : Fin 3 → ZMod 2) (x : BooleanCube r) : FixedProofTransfer.Clause (BooleanCube n) :=
  ⟨fun j => query (q j) x, s⟩

theorem or_eq_one (v : Fin 3 → ZMod 2) :
    (1 - ∏ j, (1-v j)) = 1 ↔ ∃ j, v j = 1 := by
  rw [sub_eq_self]
  simp [Finset.prod_eq_zero_iff, eq_comm]

theorem clause_eval {n r : ℕ} (P : BinaryPolynomial n)
    (q : Fin 3 → Fin n → Coordinate r) (s : Fin 3 → ZMod 2) (x : BooleanCube r) :
    PointwiseCover.row (clausePolynomial P q s) x =
      1 - ∏ j : Fin 3, (1 - (PointwiseCover.row P (query (q j) x) + s j)) := by
  simp only [clausePolynomial, PointwiseCover.row, map_sub, map_prod,
    MvPolynomial.eval_C]
  congr 1
  apply Finset.prod_congr rfl
  intro j _
  exact congrArg (fun z : ZMod 2 => 1-z) (literal_eval P (q j) (s j) x)

theorem clause_semantics {n r : ℕ} (P : BinaryPolynomial n)
    (q : Fin 3 → Fin n → Coordinate r) (s : Fin 3 → ZMod 2) (x : BooleanCube r) :
    PointwiseCover.row (clausePolynomial P q s) x = 1 ↔
      FixedProofTransfer.Accepts (clauseAt q s x) (PointwiseCover.row P) := by
  rw [clause_eval]
  exact or_eq_one _

theorem clause_degree {n r d : ℕ} (P : BinaryPolynomial n)
    (q : Fin 3 → Fin n → Coordinate r) (s : Fin 3 → ZMod 2)
    (hd : P.totalDegree ≤ d) : (clausePolynomial P q s).totalDegree ≤ 3*d := by
  have hl (j : Fin 3) :
      (MvPolynomial.C 1 - literal P (q j) (s j)).totalDegree ≤ d := by
    have h := MvPolynomial.totalDegree_sub (MvPolynomial.C 1) (literal P (q j) (s j))
    simp only [MvPolynomial.totalDegree_C, zero_max] at h
    exact h.trans (literal_degree P (q j) (s j) hd)
  calc
    _ ≤ max (MvPolynomial.C (1 : ZMod 2) : BinaryPolynomial r).totalDegree
        (∏ j : Fin 3, (MvPolynomial.C 1 - literal P (q j) (s j))).totalDegree :=
      MvPolynomial.totalDegree_sub _ _
    _ ≤ 3*d := by
      simp only [MvPolynomial.totalDegree_C, zero_max]
      calc
        _ ≤ ∑ j : Fin 3, (MvPolynomial.C 1 - literal P (q j) (s j)).totalDegree :=
          MvPolynomial.totalDegree_finsetProd _ _
        _ ≤ ∑ _j : Fin 3, d := Finset.sum_le_sum (fun j _ => hl j)
        _ = 3*d := by simp

end
end PvsNPCartography.SignedProjection
