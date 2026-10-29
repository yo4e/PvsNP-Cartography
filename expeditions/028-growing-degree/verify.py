#!/usr/bin/env python3
"""Exact finite corroboration and adversarial controls, not the universal proof.

Pascal addition, math.comb, multiplicative coefficients, direct prefix sums and
reflection-based prefix sums are separately compared. No assert disappears -O.
"""
from fractions import Fraction as F
from math import comb
import hashlib
import json


def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)


def reflected_prefix(m, cutoff):
    """Use symmetry and at most |cutoff-center| extra terms, not a full row."""
    cutoff = min(m, cutoff)
    if cutoff < 0:
        return 0
    if cutoff < m//2:
        return (1 << m) - reflected_prefix(m, m-cutoff-1)
    s = m//2
    half = (1 << (m-1)) if m % 2 else ((1 << m) + comb(m, s))//2
    return half + sum(comb(m, j) for j in range(s+1, cutoff+1))


def run():
    row = [1]
    coefficients = prefixes = saturated = quarter_checks = 0
    digest = hashlib.sha256()
    for m in range(385):
        require(row == [comb(m,j) for j in range(m+1)], 'Pascal vs library binomial')
        fast = [1]
        for j in range(m):
            top = fast[-1]*(m-j)
            require(top % (j+1) == 0, 'multiplicative divisibility')
            fast.append(top//(j+1))
        require(row == fast, 'Pascal vs multiplicative binomial')
        coefficients += len(row)
        denominator = 1 << m
        peak = F(row[m//2], denominator)
        require(m*peak*peak <= 1, 'uniform central maximum square bound')
        require(max(row) == row[m//2], 'actual maximum at center')
        c = F(comb(2*m,m), 4**m)
        cn = F(comb(2*m+2,m+1), 4**(m+1))
        require(cn*(2*m+2) == c*(2*m+1), 'normalized central recurrence')
        require((3*m+1)*c*c <= 1, 'all-s invariant, bounded check only')
        require((3*m+1)*(2*m+2)**2-(3*m+4)*(2*m+1)**2 == m,
                'coefficient polynomial identity')
        if m % 2:
            require(peak == F(comb(m+1,(m+1)//2), 1 << (m+1)), 'adjacent odd/even identity')
        half = F(sum(row[:m//2+1]), denominator)
        require(half == F(1,2) + (peak/2 if m % 2 == 0 else 0), 'exact parity-aware half')
        prefix = [0]
        for coefficient in row:
            prefix.append(prefix[-1] + coefficient)
        for d in range(33):
            cutoff = min(m,(m+8*d)//2)
            B = prefix[cutoff+1]
            require(B == reflected_prefix(m,cutoff), 'direct vs reflection-based prefix')
            normalized = F(B,denominator)
            require(normalized <= F(1,2)+(4*d+F(1,2))*peak, 'actual capped prefix envelope')
            if m >= (16*d+2)**2:
                require(normalized <= F(3,4), 'threshold three-quarter bound')
                quarter_checks += 1
            saturated += int(cutoff == m)
            prefixes += 1
            digest.update(f'{m},{d},{B}\n'.encode())
        row = [1]+[row[j-1]+row[j] for j in range(1,len(row))]+[1]

    # Boundary checks at larger arities. They use reflected prefixes and therefore
    # do not constitute independent full-row enumeration or general verification.
    boundaries = []
    for d in range(9):
        L = 16*d+2
        for m in (L*L,L*L+1,L*L+2):
            peak = F(comb(m,m//2),1 << m)
            B = F(reflected_prefix(m,(m+8*d)//2),1 << m)
            require(m*peak*peak <= 1 and L*peak <= 1, 'boundary central estimate')
            require(B <= F(3,4), 'boundary prefix estimate')
            boundaries.append({'d':d,'m':m,'quarter_bound':True})

    delta = F(422009,4782969)
    margin = 1-2*delta-F(3,4)
    require(margin == F(1406897,19131876)>0, 'exact amplification separation margin')
    bad_even = F(sum(comb(2,j) for j in range(2)),4)
    require(bad_even == F(3,4)>F(1,2), 'omitted even central atom is false')
    bad_invariant = 5*F(comb(2,1),4)**2
    require(bad_invariant == F(5,4)>1, 'coefficient four invariant is false')
    bad_linear = F(sum(comb(18,j) for j in range(14)),1 << 18)
    require(bad_linear > F(3,4), 'linear rather than square threshold fails')
    require(F(reflected_prefix(0,0),1) == 1, 'm0 is not within quarter-bound hypothesis')
    return {
        'scope':'finite exact corroboration; NOT a universal proof, independent review or novelty evidence',
        'm_range':[0,384], 'd_range':[0,32], 'randomness':'none',
        'coefficient_cross_checks':coefficients, 'central_invariant_checks':385,
        'prefix_checks':prefixes, 'saturated_prefixes':saturated,
        'quarter_checks_in_grid':quarter_checks, 'larger_boundary_checks':boundaries,
        'prefix_digest_sha256':digest.hexdigest(), 'delta':str(delta),
        'exact_margin':str(margin),
        'negative_controls':{
            'omit_even_central_atom':{'m':2,'d':0,'actual':str(bad_even),'false_upper':'1/2'},
            'replace_3s_plus_1_by_4s_plus_1':{'s':1,'lhs':str(bad_invariant),'false_upper':'1'},
            'replace_square_threshold_by_linear':{'m':18,'d':1,'actual':str(bad_linear),'false_upper':'3/4'},
            'drop_size_hypothesis':{'m':0,'d':0,'actual':'1','false_upper':'3/4'}}}


if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
