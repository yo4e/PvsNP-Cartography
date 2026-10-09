# Heuristic discovery replay, not the final verifier

These are the scripts actually executed to discover and simplify the witness.
Environment used: GNU C++, CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
Only the standard-library ../verify.py is used for certificate acceptance.

In a scratch copy of this directory:

```sh
g++ -std=c++17 -O3 -march=native search.cpp -o search
OPENBLAS_NUM_THREADS=1 python3 discover.py
OPENBLAS_NUM_THREADS=1 python3 simplify.py
```

Expected discovery trajectory in the recorded environment: 9 initial
profiles, numerical LP value about 0.623762376238; 2500 annealing restarts
with seed 20261009; combined 1391 profiles; numerical LP value about
0.685900547888; a four-row 1/12-grid witness from the simplification MIP.

A replay may choose different representatives because numerical LP tie
breaking, floating-point arithmetic, compiler and RNG distribution details
can vary. It does not change the independently exact-checkable certificate.
No heuristic stopping condition implies infeasibility. No pair found here
is NOT a proof that no pair in the full polynomial class can work.
The assertions in these exploratory scripts are convenience guards only;
the separate production verifier uses explicit exceptions under python -O.
