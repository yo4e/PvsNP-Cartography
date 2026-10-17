#!/usr/bin/env python3
"""Recheck the three-orbit n11 certificate by all exact verifier algorithms.
This runs the full pointwise expansion; no numerical optimizer is imported.
"""
from pathlib import Path
import copy
import json
from verify import check


def main():
    d = json.loads(Path(__file__).with_name('compact-certificate.json').read_text())
    result = check(d, True)
    if d['probability_denominator'] != 7 or [s['weight'] for s in d['seeds']] != [1,4,2]:
        raise ValueError('unexpected compact normalization')
    triple = [3*s['weight'] for s in d['seeds']]
    result['triple_weights'] = triple
    result['triple_denominator'] = 21
    result['triple_layer_tickets'] = [sum(t*s['good'][w] for t,s in zip(triple,d['seeds'])) for w in range(12)]
    changes = [('coefficient',lambda q:q['seeds'][0].__setitem__('code',1)),
               ('layer',lambda q:q['seeds'][0]['good'].__setitem__(0,1)),
               ('normalization',lambda q:q.__setitem__('probability_denominator',6)),
               ('field',lambda q:q.__setitem__('field','GF(3)')),
               ('target',lambda q:q.__setitem__('target','parity')),
               ('quantifier',lambda q:q.__setitem__('distribution','choose seed after seeing input')),
               ('dual',lambda q:q['dual_mass_by_weight'].__setitem__('1',14))]
    rejected = []
    for name,change in changes:
        q = copy.deepcopy(d); change(q)
        try:
            check(q,False)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('bad negative control accepted: '+name)
    print(json.dumps({'result':result,'mutations_rejected':rejected},indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
