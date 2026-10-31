import PvsNPCartography.CircuitMod3

#print axioms PvsNPCartography.SharedDAG.eval_read
#print axioms PvsNPCartography.SharedDAG.eval_args
#print axioms PvsNPCartography.SharedDAG.Gate.poly_eval
#print axioms PvsNPCartography.SharedDAG.polynomial_eval
#print axioms PvsNPCartography.SharedDAG.pow_mono
#print axioms PvsNPCartography.SharedDAG.read_degree
#print axioms PvsNPCartography.SharedDAG.args_degree
#print axioms PvsNPCartography.SharedDAG.Gate.poly_degree
#print axioms PvsNPCartography.SharedDAG.polynomial_degree
#print axioms PvsNPCartography.SharedDAG.Gate.local_error
#print axioms PvsNPCartography.SharedDAG.good_values
#print axioms PvsNPCartography.SharedDAG.union_indicator
#print axioms PvsNPCartography.SharedDAG.bad_mass
#print axioms PvsNPCartography.SharedDAG.output_degree
#print axioms PvsNPCartography.SharedDAG.output_error
#print axioms PvsNPCartography.SharedDAG.output_success
#print axioms PvsNPCartography.SharedDAG.feasible
#print axioms PvsNPCartography.SharedDAG.error_budget
#print axioms PvsNPCartography.SharedDAG.feasible_third
#print axioms PvsNPCartography.SharedDAG.mod3_size_bound

set_option pp.explicit true in
#check PvsNPCartography.SharedDAG.feasible
set_option pp.explicit true in
#check PvsNPCartography.SharedDAG.feasible_third
set_option pp.explicit true in
#check PvsNPCartography.SharedDAG.mod3_size_bound
