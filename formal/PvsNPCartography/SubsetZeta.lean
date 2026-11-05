import PvsNPCartography.FoldedBlockCount

open scoped BigOperators

namespace PvsNPCartography.SubsetZeta
noncomputable section
attribute [local instance] Classical.propDecidable
variable {α : Type*} [DecidableEq α]

/-- One Boolean-lattice butterfly. The recursive specification does not claim a runtime. -/
def step (i : α) (v : Finset α → ℤ) (S : Finset α) : ℤ :=
  v S + if i ∈ S then v (S.erase i) else 0

def scan : List α → (Finset α → ℤ) → (Finset α → ℤ)
  | [], c => c
  | i :: is, c => step i (scan is c)

/-- Sum over all subsets removed from the already-processed coordinates. -/
def partialSum (c : Finset α → ℤ) (T S : Finset α) : ℤ :=
  ∑ U ∈ T.powerset, if U ⊆ S then c (S \ U) else 0

theorem partial_insert (c : Finset α → ℤ) (T S : Finset α) (i : α) (hi : i ∉ T) :
    partialSum c (insert i T) S = step i (partialSum c T) S := by
  unfold partialSum step
  rw [Finset.sum_powerset_insert hi]
  congr 1
  by_cases his : i ∈ S
  · rw [ite_eq_left his]
    apply Finset.sum_congr rfl
    intro U hU
    have hiU : i ∉ U := fun h => hi (Finset.mem_powerset.mp hU h)
    have he : (insert i U ⊆ S) ↔ U ⊆ S.erase i := by
      simp only [Finset.insert_subset_iff, his, true_and]
      constructor
      · intro h j hj
        exact Finset.mem_erase.mpr ⟨(fun hji => hiU (hji ▸ hj)), h hj⟩
      · intro h j hj
        exact (Finset.mem_erase.mp (h hj)).2
    have hd : S \ insert i U = (S.erase i) \ U := by
      ext j
      simp only [Finset.mem_sdiff, Finset.mem_insert, Finset.mem_erase]
      tauto
    simp only [he, hd]
  · rw [ite_eq_right his]
    apply Finset.sum_eq_zero
    intro U _
    have hn : ¬ insert i U ⊆ S := fun h => his (h (Finset.mem_insert_self _ _))
    simp [hn]

/-- Duplicated coordinates are excluded by Nodup, not assumed harmless. -/
theorem scan_eq_partial (is : List α) (hn : is.Nodup) (c : Finset α → ℤ) :
    scan is c = partialSum c is.toFinset := by
  induction is with
  | nil => funext S; simp [scan, partialSum]
  | cons i is ih =>
    have hni : i ∉ is.toFinset := by simpa using (List.nodup_cons.mp hn).1
    have htail : is.Nodup := (List.nodup_cons.mp hn).2
    funext S
    simp only [scan, List.toFinset_cons]
    rw [ih htail]
    exact (partial_insert c is.toFinset S i hni).symm

theorem diff_involution (S U : Finset α) (hU : U ⊆ S) : S \ (S \ U) = U := by
  ext i
  have h := fun hi : i ∈ U => hU hi
  simp only [Finset.mem_sdiff]
  tauto

/-- Complementation permutes the subsets of the actual output set. -/
theorem sum_diff (c : Finset α → ℤ) (S : Finset α) :
    (∑ U ∈ S.powerset, c (S \ U)) = ∑ U ∈ S.powerset, c U := by
  apply Finset.sum_bij (fun U _ => S \ U)
  · intro U _
    exact Finset.mem_powerset.mpr Finset.sdiff_subset
  · intro U hU V hV he
    have h := congrArg (fun W => S \ W) he
    simpa only [diff_involution S U (Finset.mem_powerset.mp hU),
      diff_involution S V (Finset.mem_powerset.mp hV)] using h
  · intro U hU
    exact ⟨S \ U, Finset.mem_powerset.mpr Finset.sdiff_subset,
      diff_involution S U (Finset.mem_powerset.mp hU)⟩
  · intro U _
    rfl

theorem partial_univ [Fintype α] (c : Finset α → ℤ) (S : Finset α) :
    partialSum c Finset.univ S = ∑ U ∈ S.powerset, c U := by
  have he : (Finset.univ.powerset : Finset (Finset α)).filter (fun U => U ⊆ S) =
      S.powerset := by
    ext U
    simp
  unfold partialSum
  rw [← Finset.sum_filter, he]
  exact sum_diff c S

def transform [Fintype α] (c : Finset α → ℤ) : Finset α → ℤ :=
  scan (Finset.univ : Finset α).toList c

theorem transform_eq [Fintype α] (c : Finset α → ℤ) (S : Finset α) :
    transform c S = ∑ U ∈ S.powerset, c U := by
  unfold transform
  rw [scan_eq_partial _ (Finset.nodup_toList _)]
  simp only [Finset.toList_toFinset]
  exact partial_univ c S

/-- End-to-end original-polynomial endpoint. The conclusion is an exact integer count. -/
theorem exact_count {a b : ℕ} (P : BinaryPolynomial (a+b)) (T : Finset (Fin a)) :
    transform (FoldedBlockCount.coefficients (BooleanIntegerReduction.blockPolynomial b P)) T %
      (2 : ℤ)^(b+1) =
      (IntegerPolynomialLift.acceptingCount P (FoldedBlockCount.bits T) : ℤ) := by
  rw [transform_eq]
  exact FoldedBlockCount.exact_subset_count P T

end
end PvsNPCartography.SubsetZeta
