#!/usr/bin/env python3
"""Independent exact bounded tests; not a substitute for generic Lean proofs."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json


def need(ok, message):
    if not ok:
        raise ValueError(message)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def subsets(mask):
    t = mask
    while True:
        yield t
        if t == 0:
            break
        t = (t - 1) & mask


def values(n, A):
    edges = [(1 << i) | (1 << j) for i, j in combinations(range(n), 2)
             if (A >> i) & 1 and (A >> j) & 1]
    outside = ((1 << n) - 1) ^ A
    q, r = [], []
    for x in range(1 << n):
        clique = sum((x & e) == e for e in edges) % 2
        q.append((1 + x.bit_count() + clique) % 2)
        r.append((1 + (x & outside).bit_count() + clique) % 2)
    return q, r


def mobius(v, n):
    a = v[:]
    for i in range(n):
        for x in range(1 << n):
            if x >> i & 1:
                a[x] ^= a[x ^ (1 << i)]
    return a


def profile(n, k, w, outside):
    result = 0
    for t in range(w + 1):
        multiplicity = choose(k, t) * choose(n-k, w-t)
        linear = w-t if outside else w
        result += multiplicity * (((1+linear+choose(t, 2)) % 2) == int(w % 3 == 0))
    return result


def main():
    evaluation_cases = degree_cases = weighted_cases = elementary_cases = 0
    for n in range(9):
        for A in range(1 << n):
            k = A.bit_count()
            q, r = values(n, A)
            for v in (q, r):
                anf = mobius(v, n)
                need(all(x.bit_count() <= 2 for x, a in enumerate(anf) if a), 'degree')
                degree_cases += 1
            actual_q = [0] * (n+2)
            actual_r = [0] * (n+2)
            # Signed h is represented at denominator 13, exactly.
            h = [(-1)**t * (t*t-3*t-5) for t in range(n+2)]
            sums = [0] * (n+2)
            for x in range(1 << n):
                w = x.bit_count(); t = (x & A).bit_count()
                need(q[x] == (1+w+choose(t, 2)) % 2, 'q evaluation')
                need(r[x] == (1+w-t+choose(t, 2)) % 2, 'r evaluation')
                evaluation_cases += 2
                sums[w] += h[t]
                actual_q[w] += int(q[x] == int(w % 3 == 0))
                actual_r[w] += int(r[x] == int(w % 3 == 0))
                if n <= 6:
                    by_degree = [0] * (n+2)
                    for S in subsets(A):
                        by_degree[S.bit_count()] += int((S & x) == S)
                    for d in range(n+2):
                        need(by_degree[d] == choose(t, d), 'actual elementary monomial count')
                        elementary_cases += 1
            for w in range(n+2):
                weights = [choose(k,t)*choose(n-k,w-t) for t in range(w+1)]
                need(sum(weights) == choose(n,w), 'coefficient normalization')
                expected = sum(c * h[t] for t,c in enumerate(weights))
                need(sums[w] == expected, 'signed weighted sum')
                denom = choose(n,w)
                mean = Q(sums[w],13*denom) if denom else Q(0)
                rhs = sum(Q(c,denom)*Q(h[t],13) for t,c in enumerate(weights)) if denom else Q(0)
                need(mean == rhs, 'exact mean')
                need(actual_q[w] == profile(n,k,w,False), 'q layer profile')
                need(actual_r[w] == profile(n,k,w,True), 'r layer profile')
                weighted_cases += 1
    n=11; A8=(1<<8)-1; A7=(1<<7)-1
    q,_=values(n,A8); _,r=values(n,A7)
    rows=[(1,2047,38605195639935),(1,1920,1151998655551)]
    pairs=list(combinations(range(n),2))
    for A,row,v in ((A8,rows[0],q),(A7,rows[1],r)):
        expected_mask=sum(1<<j for j,(a,b) in enumerate(pairs) if A>>a&1 and A>>b&1)
        need(row[2] == expected_mask, 'canonical quadratic mask')
        for x in range(1<<n):
            val=(row[0]+(x&row[1]).bit_count()+sum(1 for j,(a,b) in enumerate(pairs)
                 if row[2]>>j&1 and x>>a&1 and x>>b&1))%2
            need(val == v[x], 'canonical row evaluation')
    totals=[0]*12; raw=[]
    for x in range(1<<n):
        target=int(x.bit_count()%3==0)
        tickets=3*int(target==0)+12*int(q[x]==target)+6*int(r[x]==target)
        totals[x.bit_count()] += tickets; raw.append(tickets)
    expected=[18,189,795,2436,4938,6678,6636,4902,2547,918,171,21]
    need(totals==expected,'n11 regression')
    probabilities=[Q(t,21*comb(11,w)) for w,t in enumerate(totals)]
    need(min(probabilities)==Q(158,231),'n11 minimum')
    need(raw[63]==0,'raw counterexample')
    # Deliberate wrong alternatives, exact tiny witnesses.
    q2,_=values(2,3)
    duplicated=(1+2+2)%2
    need(q2[3]==0 and duplicated==1,'ordered edge cancellation control')
    need(sum(choose(0,t)*choose(2,1-t) for t in range(2))==2,'missing denominator control')
    controls={'ordered_edges_over_gf2':{'n':2,'A':3,'x':3,'correct_q':q2[3],'wrong_q':duplicated},
              'missing_layer_denominator':{'n':2,'w':1,'h':'constant 1','wrong':2,'correct':1},
              'empty_layer_not_probability':{'n':0,'w':1,'total_mass':0},
              'omitted_constant':{'n':0,'x':0,'correct_q':1,'wrong_q':0},
              'omitted_symmetrization':{'n':11,'mask':63,'success':'0'}}
    # Every single ANF-coefficient mutation has a low-weight distinguishing input.
    mutations=0
    basis=[0]+[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i,j in pairs]
    for row in rows:
        for monomial in basis:
            distinguishing=monomial
            def eval_encoded(row, x):
                c, lin, quad = row
                return (c+(lin&x).bit_count()+sum(1 for j,(a,b) in enumerate(pairs)
                        if quad>>j&1 and x>>a&1 and x>>b&1))%2
            changed=list(row)
            degree=monomial.bit_count()
            if degree==0:
                changed[0] ^= 1
            elif degree==1:
                changed[1] ^= monomial
            else:
                pair=tuple(i for i in range(n) if monomial>>i&1)
                changed[2] ^= 1<<pairs.index(pair)
            need(eval_encoded(row,distinguishing)!=eval_encoded(changed,distinguishing),
                 'mutated coefficient escaped actual evaluation')
            mutations+=1
    print(json.dumps({'state':'bounded exact evidence; generic Lean execution is separate',
      'n_range':[0,8],'q_r_input_evaluations':evaluation_cases,'mobius_degree_checks':degree_cases,
      'weighted_layer_cases':weighted_cases,'elementary_integer_cases_n0_to6':elementary_cases,
      'n11_canonical_input_comparisons':4096,'n11_layer_tickets':totals,
      'n11_probabilities':list(map(str,probabilities)),'n11_minimum':str(min(probabilities)),
      'single_coefficient_mutation_witnesses':mutations,'negative_controls':controls},sort_keys=True,indent=2))

if __name__=='__main__':
    main()
