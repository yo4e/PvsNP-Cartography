import PvsNPCartography.CircuitMod3

namespace PvsNPCartography.SharedDAG
open RandomizedGates
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Negating the chosen output adds one exact gate, not a nonlinear gate. -/
def negateOutput {n m K : ℕ} (p : Program n K m) (w : Wire n m) :
    Program n K (m+1) := p.step (.negate w)

@[simp] theorem negateOutput_cost {n m K : ℕ} (p : Program n K m) (w : Wire n m) :
    cost (negateOutput p w) = cost p := by
  simp [negateOutput, cost, Gate.cost]

@[simp] theorem negateOutput_depth {n m K : ℕ} (p : Program n K m) (w : Wire n m) :
    outputDepth (negateOutput p w) (.inr 0) = outputDepth p w := rfl

@[simp] theorem negateOutput_target {n m K : ℕ} (p : Program n K m) (w : Wire n m)
    (x : BooleanCube n) : target (negateOutput p w) (.inr 0) x = 1 + target p w x := rfl

@[simp] theorem negateOutput_polynomial {n m K r : ℕ} (p : Program n K m)
    (w : Wire n m) (A : Matrix K r) :
    outputPoly (negateOutput p w) (.inr 0) A = 1 + outputPoly p w A := rfl

/-- The primary source uses nonzero-residue polarity. Exact NOT bridges it
without paying another nonlinear gate or increasing nonlinear depth. -/
theorem mod3_complement_size_bound {n m K r : ℕ} (p : Program n K m) (w : Wire n m)
    (S h : ℕ) (hr : 1 ≤ r) (hs : cost p ≤ S) (hd : outputDepth p w ≤ h)
    (hb : 3*S ≤ 2^r) (hc : ∀ x, target p w x = 1 + SmallSupportMod3.target x) :
    n < (16*r^h+2)^2+2 := by
  apply mod3_size_bound (negateOutput p w) (.inr 0) S h hr
    (by simpa using hs) (by simpa using hd) hb
  intro x
  rw [negateOutput_target, hc, ← add_assoc, bit_one_add_one, zero_add]

/-- All absent OR slots have the neutral zero value for any capacity. -/
theorem absent_or {n m K : ℕ} (x : Fin n → ZMod 2) (v : Fin m → ZMod 2) :
    (Gate.disj (fun _ : Fin K => none)).eval x v = 0 := by
  simp [Gate.eval, args, orValue]

/-- All absent AND slots have the neutral one value, including K=0. -/
theorem absent_and {n m K : ℕ} (x : Fin n → ZMod 2) (v : Fin m → ZMod 2) :
    (Gate.conj (fun _ : Fin K => none)).eval x v = 1 := by
  simp [Gate.eval, andValue_semantics, args]

/-- Choosing an external input ignores all internal nodes, including unused ones. -/
theorem external_output {n m K : ℕ} (p : Program n K m) (j : Fin n)
    (x : Fin n → ZMod 2) : output p (.inl j) x = x j := rfl

/-- Original gate count is exactly additive, independent of fan-out multiplicity. -/
theorem cost_step {n m K : ℕ} (p : Program n K m) (g : Gate n m K) :
    cost (p.step g) = cost p + g.cost := rfl

end
end PvsNPCartography.SharedDAG
