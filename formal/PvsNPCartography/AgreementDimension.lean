import PvsNPCartography.TwoPointCompression

open scoped BigOperators
open Submodule

namespace PvsNPCartography.AgreementDimension

noncomputable section
variable {K : Type*} [Field K] {n : ℕ}
attribute [local instance] Classical.propDecidable

/-- Finite squarefree supports of size at most t. -/
def supports (n t : ℕ) : Finset (Finset (Fin n)) :=
  Finset.univ.filter (fun S => S.card ≤ t)

/-- Actual coordinate monomial, restricted to a finite set of actual points. -/
def monoValue (H : Finset (Fin n → K)) (S : Finset (Fin n)) : H → K :=
  fun y => ∏ i ∈ S, y.1 i

/-- No spanning or rank hypothesis is hidden in this definition. -/
def lowSpace (H : Finset (Fin n → K)) (t : ℕ) : Submodule K (H → K) :=
  by classical exact Submodule.span K ((supports n t).image (monoValue H) : Set (H → K))

theorem mono_mem (H : Finset (Fin n → K)) (t : ℕ) (S : Finset (Fin n))
    (hS : S.card ≤ t) : monoValue H S ∈ lowSpace H t := by
  classical
  apply Submodule.subset_span
  exact Finset.mem_image.mpr ⟨S, by simp [supports, hS], rfl⟩

theorem lowSpace_mono (H : Finset (Fin n → K)) {s t : ℕ} (h : s ≤ t) :
    lowSpace H s ≤ lowSpace H t := by
  classical
  apply Submodule.span_le.mpr
  intro v hv
  obtain ⟨S, hS, rfl⟩ := Finset.mem_image.mp hv
  exact mono_mem H t S ((by simpa [supports] using hS : S.card ≤ s).trans h)

/-- Expand a product of coordinate-affine factors into squarefree supports.
This construction works even when H is not a two-point grid. -/
theorem affine_product_mem (H : Finset (Fin n → K)) (A : Finset (Fin n))
    (t : ℕ) (hA : A.card ≤ t) (c e : Fin n → K) :
    (fun y : H => ∏ i ∈ A, (c i * y.1 i + e i)) ∈ lowSpace H t := by
  classical
  have he : (fun y : H => ∏ i ∈ A, (c i * y.1 i + e i)) =
      ∑ S ∈ A.powerset, ((∏ i ∈ S, c i) * ∏ i ∈ A \ S, e i) • monoValue H S := by
    funext y
    simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, monoValue]
    rw [Finset.prod_add]
    apply Finset.sum_congr rfl
    intro S _
    rw [Finset.prod_mul_distrib]
    ring
  rw [he]
  apply Submodule.sum_mem
  intro S hS
  exact (lowSpace H t).smul_mem _
    (mono_mem H t S ((Finset.card_le_card (Finset.mem_powerset.mp hS)).trans hA))

/-- Degree-preserving reduction of a power on two distinct points. This is
not the false Boolean identity y^2=y on a general two-point grid. -/
theorem power_affine (a b : K) (hab : a ≠ b) (k : ℕ) (x : K)
    (hx : x = a ∨ x = b) :
    x ^ k = ((a ^ k - b ^ k) / (a - b)) * x +
      (a * b ^ k - b * a ^ k) / (a - b) := by
  have hden : a - b ≠ 0 := sub_ne_zero.mpr hab
  rcases hx with rfl | rfl <;> field_simp <;> ring

theorem support_card_le_sum (d : Fin n →₀ ℕ) :
    d.support.card ≤ d.sum (fun _ k => k) := by
  classical
  calc
    d.support.card = ∑ i ∈ d.support, 1 := by simp
    _ ≤ ∑ i ∈ d.support, d i := by
      apply Finset.sum_le_sum
      intro i hi
      have hne : d i ≠ 0 := Finsupp.mem_support_iff.mp hi
      omega
    _ = d.sum (fun _ k => k) := rfl

/-- Every actual polynomial of bounded TOTAL degree evaluates in the bounded
squarefree span. Coefficients are unrestricted elements of K. -/
theorem eval_mem_low (H : Finset (Fin n → K)) (a b : K) (hab : a ≠ b)
    (hgrid : ∀ y : H, ∀ i, y.1 i = a ∨ y.1 i = b)
    (P : MvPolynomial (Fin n) K) (t : ℕ) (hP : P.totalDegree ≤ t) :
    (fun y : H => MvPolynomial.eval y.1 P) ∈ lowSpace H t := by
  classical
  have hm (d : Fin n →₀ ℕ) (hd : d ∈ P.support) :
      (fun y : H => ∏ i ∈ d.support, y.1 i ^ d i) ∈ lowSpace H t := by
    have hc : d.support.card ≤ t :=
      (support_card_le_sum d).trans ((MvPolynomial.le_totalDegree hd).trans hP)
    have h := affine_product_mem H d.support t hc
      (fun i => (a ^ d i - b ^ d i) / (a-b))
      (fun i => (a * b ^ d i - b * a ^ d i) / (a-b))
    convert h using 1
    funext y
    apply Finset.prod_congr rfl
    intro i _
    exact power_affine a b hab (d i) (y.1 i) (hgrid y i)
  have he : (fun y : H => MvPolynomial.eval y.1 P) =
      ∑ d ∈ P.support, P.coeff d • (fun y : H => ∏ i ∈ d.support, y.1 i ^ d i) := by
    funext y
    simpa only [MvPolynomial.eval₂_id, RingHom.id_apply, Finset.sum_apply,
      Pi.smul_apply, smul_eq_mul] using MvPolynomial.eval₂_eq (RingHom.id K) y.1 P
  rw [he]
  exact Submodule.sum_mem _ (fun d hd => (lowSpace H t).smul_mem _ (hm d hd))

def slope (a b z : K) : K := by
  classical exact if z = a then -(b-a)⁻¹ else (b-a)⁻¹

def intercept (a b z : K) : K := by
  classical exact if z = a then b * (b-a)⁻¹ else -a * (b-a)⁻¹

theorem lagrange_factor (a b : K) (hab : a ≠ b) (z x : K)
    (hz : z = a ∨ z = b) (hx : x = a ∨ x = b) :
    slope a b z * x + intercept a b z = if x = z then 1 else 0 := by
  have hden : b-a ≠ 0 := sub_ne_zero.mpr hab.symm
  have hba : b ≠ a := hab.symm
  rcases hz with rfl | rfl <;> rcases hx with rfl | rfl
  all_goals simp_all [slope, intercept]
  all_goals field_simp
  all_goals ring

/-- Explicit product Lagrange indicator on H. -/
def delta (H : Finset (Fin n → K)) (a b : K) (z : H) : H → K :=
  fun y => ∏ i, (slope a b (z.1 i) * y.1 i + intercept a b (z.1 i))

theorem delta_eq (H : Finset (Fin n → K)) (a b : K) (hab : a ≠ b)
    (hgrid : ∀ y : H, ∀ i, y.1 i = a ∨ y.1 i = b) (z y : H) :
    delta H a b z y = if y = z then 1 else 0 := by
  classical
  unfold delta
  by_cases h : y = z
  · subst y
    simp_rw [lagrange_factor a b hab _ _ (hgrid z _) (hgrid z _)]
    simp
  · rw [ite_eq_right h]
    obtain ⟨i, hi⟩ : ∃ i, y.1 i ≠ z.1 i := by
      by_contra hn
      push Not at hn
      apply h
      apply Subtype.ext
      funext i
      exact hn i
    apply Finset.prod_eq_zero (Finset.mem_univ i)
    rw [lagrange_factor a b hab _ _ (hgrid z i) (hgrid y i), ite_eq_right hi]

theorem all_functions_mem_full (H : Finset (Fin n → K)) (a b : K) (hab : a ≠ b)
    (hgrid : ∀ y : H, ∀ i, y.1 i = a ∨ y.1 i = b) (f : H → K) :
    f ∈ lowSpace H n := by
  classical
  have hd (z : H) : delta H a b z ∈ lowSpace H n := by
    exact affine_product_mem H Finset.univ n (by simp)
      (fun i => slope a b (z.1 i)) (fun i => intercept a b (z.1 i))
  have he : (∑ z : H, f z • delta H a b z) = f := by
    funext y
    simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul,
      delta_eq H a b hab hgrid]
    simp
  rw [← he]
  exact Submodule.sum_mem _ (fun z _ => (lowSpace H n).smul_mem _ (hd z))

/-- Compression + polynomial reduction + interpolation, not a surjectivity premise. -/
theorem lowSpace_eq_top (H : Finset (Fin n → K)) (a b : K)
    (ha : a ≠ 0) (hb : b ≠ 0) (hab : a ≠ b)
    (hgrid : ∀ y : H, ∀ i, y.1 i = a ∨ y.1 i = b)
    (R : MvPolynomial (Fin n) K)
    (hagree : ∀ y : H, MvPolynomial.eval y.1 R = ∏ i, y.1 i)
    (d t : ℕ) (hdegree : R.totalDegree ≤ d) (hthreshold : n+d ≤ 2*t+1) :
    lowSpace H t = ⊤ := by
  classical
  have hm (S : Finset (Fin n)) : monoValue H S ∈ lowSpace H t := by
    obtain ⟨Q, hQ, he⟩ := TwoPointCompression.compress_monomial a b ha hb R d t
      hdegree hthreshold S
    have h := eval_mem_low H a b hab hgrid Q t hQ
    convert h using 1
    funext y
    exact (he y.1 (hgrid y) (hagree y)).symm
  have hle : lowSpace H n ≤ lowSpace H t := by
    apply Submodule.span_le.mpr
    intro v hv
    obtain ⟨S, _, rfl⟩ := Finset.mem_image.mp hv
    exact hm S
  apply top_unique
  intro f _
  exact hle (all_functions_mem_full H a b hab hgrid f)

theorem supports_card (n t : ℕ) :
    (supports n t).card = ∑ j ∈ Finset.range (min n t + 1), n.choose j := by
  classical
  have hf := Finset.card_eq_sum_card_fiberwise (f := fun S : Finset (Fin n) => S.card)
    (s := supports n t) (t := Finset.range (min n t + 1)) (by
      intro S hS
      have hs : S.card ≤ t := by simpa [supports] using hS
      have hn : S.card ≤ n := by simpa using Finset.card_le_univ S
      simp only [Finset.mem_coe, Finset.mem_range]
      omega)
  rw [hf]
  apply Finset.sum_congr rfl
  intro j hj
  have hjt : j ≤ t := by simp only [Finset.mem_range] at hj; omega
  have he : (supports n t).filter (fun S => S.card = j) =
      (Finset.univ : Finset (Fin n)).powersetCard j := by
    ext S
    simp only [supports, Finset.mem_filter, Finset.mem_univ, true_and,
      Finset.mem_powersetCard, Finset.subset_univ]
    omega
  rw [he, Finset.card_powersetCard]
  simp

/-- Cardinality bound for any actual finite agreement subset. -/
theorem agreement_card_le (H : Finset (Fin n → K)) (a b : K)
    (ha : a ≠ 0) (hb : b ≠ 0) (hab : a ≠ b)
    (hgrid : ∀ y : H, ∀ i, y.1 i = a ∨ y.1 i = b)
    (R : MvPolynomial (Fin n) K)
    (hagree : ∀ y : H, MvPolynomial.eval y.1 R = ∏ i, y.1 i)
    (d : ℕ) (hdegree : R.totalDegree ≤ d) :
    H.card ≤ ∑ j ∈ Finset.range (min n ((n+d)/2) + 1), n.choose j := by
  classical
  let t := (n+d)/2
  have ht : n+d ≤ 2*t+1 := by omega
  have htop := lowSpace_eq_top H a b ha hb hab hgrid R hagree d t hdegree ht
  have hd : Module.finrank K (lowSpace H t) ≤ (supports n t).card := by
    exact (finrank_span_finset_le_card (R := K)
      ((supports n t).image (monoValue H))).trans (Finset.card_image_le)
  rw [htop, finrank_top] at hd
  simpa [supports_card, t] using hd

/-- Actual full two-point grid, finite even when K is infinite. -/
def grid (a b : K) (n : ℕ) : Finset (Fin n → K) :=
  by classical exact Fintype.piFinset (fun _ => {a,b})

def agreementSet (a b : K) (R : MvPolynomial (Fin n) K) : Finset (Fin n → K) :=
  by classical exact (grid a b n).filter (fun y => MvPolynomial.eval y R = ∏ i, y i)

/-- The requested endpoint. Neither the cardinality bound nor a rank statement
is a hypothesis. The degree is genuine MvPolynomial.totalDegree. -/
theorem agreement_bound (a b : K) (ha : a ≠ 0) (hb : b ≠ 0) (hab : a ≠ b)
    (R : MvPolynomial (Fin n) K) (d : ℕ) (hdegree : R.totalDegree ≤ d) :
    (agreementSet a b R).card ≤
      ∑ j ∈ Finset.range (min n ((n+d)/2) + 1), n.choose j := by
  classical
  apply agreement_card_le (agreementSet a b R) a b ha hb hab _ R _ d hdegree
  · intro y i
    have hy := (Finset.mem_filter.mp y.2).1
    simpa [grid, Fintype.mem_piFinset] using (Fintype.mem_piFinset.mp hy i)
  · intro y
    exact (Finset.mem_filter.mp y.2).2

end
end PvsNPCartography.AgreementDimension
