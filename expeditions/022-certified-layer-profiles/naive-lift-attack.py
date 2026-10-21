#!/usr/bin/env python3
"""Exact counterexample to ONE naive dimension lift, not a quadratic lower bound."""
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    n = 12
    A = set(range(9))
    B = set(range(8))
    q_edges = tuple(combinations(sorted(A), 2))
    r_edges = tuple(combinations(sorted(B), 2))
    q_counts = [0] * (n+1)
    r_counts = [0] * (n+1)
    layer_sizes = [0] * (n+1)
    for x in range(1 << n):
        bit = [(x >> i) & 1 for i in range(n)]
        w = sum(bit)
        target = int(w % 3 == 0)
        q_value = (1 + sum(bit) + sum(bit[i]*bit[j] for i,j in q_edges)) % 2
        r_value = (1 + sum(bit[i] for i in range(n) if i not in B)
                   + sum(bit[i]*bit[j] for i,j in r_edges)) % 2
        q_counts[w] += int(q_value == target)
        r_counts[w] += int(r_value == target)
        layer_sizes[w] += 1
    probabilities = []
    tickets = []
    for w in range(n+1):
        q_formula = sum(choose(9,t)*choose(3,w-t)
                        * int((1+w+choose(t,2)) % 2 == int(w%3==0))
                        for t in range(w+1))
        r_formula = sum(choose(8,t)*choose(4,w-t)
                        * int((1+w-t+choose(t,2)) % 2 == int(w%3==0))
                        for t in range(w+1))
        require(q_counts[w] == q_formula and r_counts[w] == r_formula,
                'direct polynomial evaluation differs from binomial profile')
        require(layer_sizes[w] == comb(n,w), 'layer size')
        ticket = int(w%3 != 0)*layer_sizes[w] + 4*q_counts[w] + 2*r_counts[w]
        tickets.append(ticket)
        probabilities.append(Fraction(ticket, 7*layer_sizes[w]))
    bad = [w for w,p in enumerate(probabilities) if p < Fraction(2,3)]
    require(bad == [7,10], 'unexpected failing layers')
    require(probabilities[10] == Fraction(19,33), 'wrong counterexample value')
    require(min(probabilities) == Fraction(19,33), 'wrong minimum')
    print(json.dumps({
        'scope':'only the lift zero,q_[n-3],r_[n-4] with weights [1,4,2]/7 at n12',
        'inputs_evaluated':1<<n,
        'q_subset_size':9,'r_subset_size':8,
        'q_correct_by_layer':q_counts,'r_correct_by_layer':r_counts,
        'weighted_layer_tickets':tickets,
        'success_by_layer':list(map(str,probabilities)),
        'failing_layers':bad,'minimum':'19/33','minimum_layer':10,
        'gap_below_two_thirds':str(Fraction(2,3)-min(probabilities)),
        'meaning':'layer mean refutes a raw pointwise guarantee; full uniform permutation makes this the actual pointwise success on the whole layer',
        'not_claimed':'no impossibility for other n12 quadratic mixtures and no n12 degree equality'
    },sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
