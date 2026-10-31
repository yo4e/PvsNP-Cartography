import PvsNPCartography.RootBudget

#print axioms PvsNPCartography.RootBudget.root_cost
#print axioms PvsNPCartography.RootBudget.weight_nonneg
#print axioms PvsNPCartography.RootBudget.fst_marginal
#print axioms PvsNPCartography.RootBudget.snd_marginal
#print axioms PvsNPCartography.RootBudget.weight_sum
#print axioms PvsNPCartography.RootBudget.target_is_circuit
#print axioms PvsNPCartography.RootBudget.poly_degree
#print axioms PvsNPCartography.RootBudget.poly_eval_true
#print axioms PvsNPCartography.RootBudget.root_local_error
#print axioms PvsNPCartography.RootBudget.error_indicator
#print axioms PvsNPCartography.RootBudget.error_bound
#print axioms PvsNPCartography.RootBudget.success_bound
#print axioms PvsNPCartography.RootBudget.feasible
#print axioms PvsNPCartography.RootBudget.third_budget
#print axioms PvsNPCartography.RootBudget.feasible_third
#print axioms PvsNPCartography.RootBudget.mod3_size_bound

set_option pp.explicit true in
#check PvsNPCartography.RootBudget.feasible
set_option pp.explicit true in
#check PvsNPCartography.RootBudget.feasible_third
set_option pp.explicit true in
#check PvsNPCartography.RootBudget.mod3_size_bound
