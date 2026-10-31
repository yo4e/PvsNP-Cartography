#!/usr/bin/env python3
"""Exact controls for the concrete reverse-table DAG, not an all-circuit proof.
Two same-author implementations: unreduced sparse polynomials on reverse tables
and Boolean execution on chronological tables. All checks remain active with -O.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json

Wire = tuple[str, int]
Poly = frozenset[tuple[int, ...]]

@dataclass(frozen=True)
class Gate:
    op: str
    refs: tuple[Wire | None, ...] = ()
    bit: int = 0


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def one(n: int) -> Poly:
    return frozenset({(0,) * n})


def variable(n: int, i: int) -> Poly:
    return frozenset({tuple(int(j == i) for j in range(n))})


def mul(p: Poly, q: Poly) -> Poly:
    out: set[tuple[int, ...]] = set()
    for a in p:
        for b in q:
            c = tuple(u + v for u, v in zip(a, b))
            if c in out:
                out.remove(c)
            else:
                out.add(c)
    return frozenset(out)


def degree(p: Poly) -> int:
    return max((sum(m) for m in p), default=0)


def peval(p: Poly, x: tuple[int, ...]) -> int:
    # Exponents are kept for degree; Boolean evaluation separately uses 0^0=1.
    return sum(all(e == 0 or b == 1 for b, e in zip(x, m)) for m in p) % 2


def polys(n: int, gates: tuple[Gate, ...], A: tuple[tuple[int, ...], ...]):
    table: list[Poly] = []
    depths: list[int] = []
    r = len(A)
    O = one(n)
    for g in gates:
        def read(w):
            return variable(n, w[1]) if w[0] == 'i' else table[w[1]]
        def dep(w):
            return 0 if w is None or w[0] == 'i' else depths[w[1]]
        h = max((dep(w) for w in g.refs), default=0)
        if g.op == 'const':
            p, h = (O if g.bit else frozenset()), 0
        elif g.op == 'not':
            p = O ^ read(g.refs[0])
        elif g.op == 'xor':
            p = frozenset()
            for w in g.refs:
                if w is not None:
                    p = p ^ read(w)
        else:
            require(g.op in ('and', 'or'), 'unknown polynomial operation')
            args = [((O if g.op == 'and' else frozenset()) if w is None else read(w)) for w in g.refs]
            if g.op == 'and':
                args = [O ^ p for p in args]
            p = O
            for a in A:
                row = frozenset()
                for j, q in enumerate(args):
                    if a[j]:
                        row = row ^ q
                p = mul(p, O ^ row)
            if g.op == 'or':
                p = O ^ p
            h += 1
        require(degree(p) <= r**h, 'degree versus nonlinear output depth')
        table.insert(0, p)
        depths.insert(0, h)
    return table, depths


def values(gates: tuple[Gate, ...], x: tuple[int, ...], A=None):
    # Deliberately use chronological indexing, unlike the polynomial table.
    out: list[int] = []
    for g in gates:
        z = []
        for w in g.refs:
            if w is None:
                z.append(int(g.op == 'and'))
            elif w[0] == 'i':
                z.append(x[w[1]])
            else:
                z.append(out[len(out) - 1 - w[1]])
        out.append(bit_gate(g, tuple(z), A))
    return out


def bit_gate(g: Gate, z: tuple[int, ...], A=None) -> int:
    if g.op == 'const':
        return g.bit
    if g.op == 'not':
        return 1-z[0]
    if g.op == 'xor':
        return sum(z) % 2
    if A is None:
        return int(all(z)) if g.op == 'and' else int(any(z))
    if g.op == 'and':
        z = tuple(1-b for b in z)
    q = int(any(sum(c*b for c,b in zip(row,z)) % 2 for row in A))
    return 1-q if g.op == 'and' else q


def options(n: int, m: int, K: int):
    wires = tuple(('i', j) for j in range(n)) + tuple(('g', j) for j in range(m))
    yield Gate('const', bit=0)
    yield Gate('const', bit=1)
    for w in wires:
        yield Gate('not', (w,))
    for op in ('xor', 'or', 'and'):
        for refs in product((None,) + wires, repeat=K):
            yield Gate(op, refs)


def check(n: int, K: int, gates: tuple[Gate, ...], r: int, counts: Counter):
    require(r >= 1, 'circuit hypothesis r>=1')
    counts['program_parameter_pairs'] += 1
    S = sum(g.op in ('and','or') for g in gates)
    inputs = tuple(product((0,1), repeat=n))
    truth = [values(gates,x) for x in inputs]
    matrices = tuple(product(tuple(product((0,1),repeat=K)),repeat=r))
    local_counts = [[0]*len(gates) for _ in inputs]
    output_counts = [[0]*len(gates) for _ in inputs]
    union_counts = [0]*len(inputs)
    for A in matrices:
        ps, ds = polys(n,gates,A)
        counts['matrix_program_pairs'] += 1
        counts['actual_degree_checks'] += len(ps)
        for xi,x in enumerate(inputs):
            approx = values(gates,x,A)
            local = []
            for j,g in enumerate(gates):
                z = tuple(int(g.op=='and') if w is None else
                    (x[w[1]] if w[0]=='i' else truth[xi][j-1-w[1]]) for w in g.refs)
                bad = bit_gate(g,z,A) != truth[xi][j]
                local.append(bad)
                local_counts[xi][j] += bad
                wrong = approx[j] != truth[xi][j]
                output_counts[xi][j] += wrong
                require(not wrong or any(local), 'first-error inclusion')
                require(peval(ps[len(ps)-1-j],x)==approx[j], 'reverse/chronological evaluator mismatch')
                counts['node_input_checks'] += 1
            union_counts[xi] += any(local)
            for j in range(n):
                require(peval(variable(n,j),x)==x[j], 'direct external output')
                counts['external_output_checks'] += 1
    for xi,x in enumerate(inputs):
        require(union_counts[xi]*2**r <= S*len(matrices), 'original-node union bound')
        counts['union_checks'] += 1
        for j,g in enumerate(gates):
            z = tuple(int(g.op=='and') if w is None else
                (x[w[1]] if w[0]=='i' else truth[xi][j-1-w[1]]) for w in g.refs)
            active = (g.op=='or' and any(z)) or (g.op=='and' and not all(z))
            expected = Fraction(1,2**r) if active else Fraction(0)
            require(Fraction(local_counts[xi][j],len(matrices))==expected, 'exact padded local law')
            require(output_counts[xi][j]*2**r <= S*len(matrices), 'every chosen output bound')
            if 3*S <= 2**r:
                require(3*output_counts[xi][j] <= len(matrices), 'one-third endpoint')
                counts['one_third_checks'] += 1
            counts['pointwise_output_checks'] += 1


def attacks():
    # Wrong AND padding changes the Boolean target even before randomization.
    require(bit_gate(Gate('and'),(1,1)) == 1 and bit_gate(Gate('and'),(1,0)) == 0,
            'AND padding attack')
    # An exact output node does not erase a preceding randomized error.
    g=(Gate('or',(('i',0),)),Gate('not',(('g',0),)))
    wrong=sum(values(g,(1,),((a,),))[-1] != values(g,(1,))[-1] for a in (0,1))
    require(wrong==1, 'output-only error count attack')
    # Composition multiplies degrees, rather than adding a fixed r per level.
    p,_=polys(1,(Gate('or',(('i',0),)),Gate('or',(('g',0),))),((1,),)*3)
    require(degree(p[0])==9 and 9>3*2, 'flat degree attack')
    # Shared fan-out can have exponentially many formula occurrences but linear DAG count.
    dup=tuple([Gate('or',(('i',0),('i',0)))]+[Gate('or',(('g',0),('g',0)))]*5)
    dag_count=len(dup)
    occurrences=2**len(dup)-1
    require(dag_count==6 and occurrences==63, 'DAG/formula bookkeeping control')
    return {
        'and_zero_padding': {'input':1,'correct_target':1,'wrong_target':0},
        'output_only_gate_count': {'program':'NOT(OR(x))','x':1,'r':1,
                                   'actual_error':'1/2','false_bound':'0'},
        'linear_depth_degree': {'r':3,'h':2,'actual_degree':9,'false_bound':6},
        'unrolling_control': {'original_nonlinear_nodes':dag_count,'formula_occurrences':occurrences}
    }


def mod3_check():
    # n3 residue-zero is all-zero OR all-one. Gate references remain newest-first.
    gs=(Gate('and',(('i',0),('i',1),('i',2))),
        Gate('not',(('i',0),)), Gate('not',(('i',1),)),Gate('not',(('i',2),)),
        Gate('and',(('g',0),('g',1),('g',2))),
        Gate('or',(('g',0),('g',4),None)))
    inputs=tuple(product((0,1),repeat=3))
    for x in inputs:
        require(values(gs,x)[-1] == int(sum(x)%3==0),'original MOD3 polarity')
    r=4
    matrices=tuple(product(tuple(product((0,1),repeat=3)),repeat=r))
    errors=[]
    for x in inputs:
        bad=sum(values(gs,x,A)[-1] != int(sum(x)%3==0) for A in matrices)
        require(3*bad<=len(matrices),'MOD3 one-third actual error')
        require(bad*2**r<=3*len(matrices),'MOD3 gate-count budget')
        errors.append(str(Fraction(bad,len(matrices))))
    return {'n':3,'S':3,'h':2,'r':r,'matrices':len(matrices),'inputs':8,
            'errors_lex_order':errors,'scope':'Boolean execution; sparse degree checked separately at r1/2',
            'gates':gs}


def main():
    counts=Counter()
    programs=0
    for n in range(3):
        for K in range(3):
            for first in options(n,0,K):
                for second in options(n,1,K):
                    programs+=1
                    for r in (1,2):
                        check(n,K,(first,second),r,counts)
    curated=Counter()
    ms=mod3_check()
    mod3_gates=ms.pop('gates')
    for r in (1,2):
        check(3,3,mod3_gates,r,curated)
    check(3,3,(Gate('and',(('i',0),None,('i',2))),
               Gate('xor',(None,('g',0),('g',0))),Gate('or',(('g',1),None,('i',1)))),2,curated)
    check(1,1,(Gate('or',(('i',0),)),Gate('or',(('g',0),))),3,curated)
    print(json.dumps({'status':'PASS','scope':'same-author exact finite controls, not a generic proof',
        'exhaustive':{'programs':programs,'n':[0,1,2],'K':[0,1,2],'r':[1,2],**dict(counts)},
        'curated':dict(curated),'mod3':ms,'counterexamples':attacks()},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
