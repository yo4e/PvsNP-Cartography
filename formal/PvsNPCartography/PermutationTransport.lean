import PvsNPCartography.ProbabilisticDegree

open scoped BigOperators

namespace PvsNPCartography.Symmetrization

noncomputable section

abbrev Perm (n : ℕ) := Equiv.Perm (Fin n)

/-- Pull back an input along a permutation: coordinate i reads x (e i). -/
def permuteInput {n : ℕ} (e : Perm n) (x : BooleanCube n) : BooleanCube n :=
  fun i => x (e i)

/-- Rename polynomial variables in the matching, covariant direction. -/
def permutePolynomial {n : ℕ} (e : Perm n) (P : BinaryPolynomial n) :
    BinaryPolynomial n := MvPolynomial.rename e P

/-- Actual total degree, not the degree of a truth-table encoding. -/
theorem permute_degree {n : ℕ} (e : Perm n) (P : BinaryPolynomial n) :
    (permutePolynomial e P).totalDegree = P.totalDegree :=
  MvPolynomial.totalDegree_renameEquiv e P

/-- The input pullback uses e, not e inverse. -/
theorem permute_eval {n : ℕ} (e : Perm n) (P : BinaryPolynomial n)
    (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (permutePolynomial e P) =
      MvPolynomial.eval (fun i => ((permuteInput e x i).val : ZMod 2)) P :=
  MvPolynomial.eval_rename e _ P

theorem permute_weight {n : ℕ} (e : Perm n) (x : BooleanCube n) :
    (∑ i, (permuteInput e x i).val) = ∑ i, (x i).val :=
  e.sum_comp (fun i => (x i).val)

/-- Symmetry is a hypothesis on the TARGET, not on individual polynomials. -/
def IsSymmetric {n : ℕ} (f : BooleanCube n → ZMod 2) : Prop :=
  ∀ (e : Perm n) (x : BooleanCube n), f (permuteInput e x) = f x

/-- A real-valued correctness indicator, with the field still GF(2). -/
def correct {n : ℕ} (f : BooleanCube n → ZMod 2) (P : BinaryPolynomial n)
    (x : BooleanCube n) : ℝ :=
  if MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) P = f x then 1 else 0

def success {n : ℕ} {I : Type*} [Fintype I]
    (f : BooleanCube n → ZMod 2) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (x : BooleanCube n) : ℝ := ∑ i, mu i * correct f (P i) x

theorem correct_permute {n : ℕ} {f : BooleanCube n → ZMod 2}
    (hf : IsSymmetric f) (e : Perm n) (P : BinaryPolynomial n) (x : BooleanCube n) :
    correct f (permutePolynomial e P) x = correct f P (permuteInput e x) := by
  simp only [correct, permute_eval, hf e x]

/-- Reindex an arbitrary finite family by Fin without losing any real weights.
This is the adapter to the project's original degree predicate. -/
theorem feasible_of_fintype {n : ℕ} {I : Type} [Fintype I]
    {f : BooleanCube n → ZMod 2} {epsilon : ℝ} {d : ℕ}
    (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1)
    (hp : ∀ x, 1 - epsilon ≤ success f P mu x) :
    HasProbabilisticDegreeAtMost f epsilon d := by
  classical
  let e := (Fintype.equivFin I).symm
  refine ⟨Fintype.card I, (fun j => P (e j)), (fun j => mu (e j)),
    (fun j => hd (e j)), (fun j => hn (e j)), ?_, ?_⟩
  · exact (e.sum_comp mu).trans hs
  · intro x
    change 1 - epsilon ≤ ∑ j, mu (e j) * correct f (P (e j)) x
    rw [e.sum_comp (fun i => mu i * correct f (P i) x)]
    exact hp x

end
end PvsNPCartography.Symmetrization
