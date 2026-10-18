#!/usr/bin/env python3
"""Isolate n10 proof evaluation without modifying the production Lean source.
Every timeout/failure is recorded. A diagnostic success is not root validation.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / 'formal'
OUT = ROOT / 'n10-profile-output'
EXPECTED = 'bd998f8ad908a1622cac393dd3b68e62505f2bc01dd2ef9010b9cb7e5c948e93'


def run(name, text, seconds):
    path = FORMAL / 'N10Profile.lean'
    path.write_text(text)
    (OUT / (name + '.lean')).write_text(text)
    command = ['lake', 'env', 'lean', 'N10Profile.lean']
    print('START', name, 'limit_seconds', seconds, flush=True)
    started = time.monotonic()
    timed_out = False
    try:
        proc = subprocess.run(command, cwd=FORMAL, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=seconds)
        code, output = proc.returncode, proc.stdout
    except subprocess.TimeoutExpired as error:
        timed_out = True
        code, output = 124, error.stdout or b''
    output = output.decode('utf-8', errors='replace')
    elapsed = round(time.monotonic() - started, 3)
    (OUT / (name + '.log')).write_text(output)
    item = {'name': name, 'command': command, 'exit_code': code,
            'timed_out': timed_out, 'elapsed_seconds': elapsed,
            'source_sha256': hashlib.sha256(text.encode()).hexdigest()}
    print(json.dumps(item, sort_keys=True), flush=True)
    print(output, flush=True)
    return item


def main():
    OUT.mkdir(exist_ok=True)
    source = (FORMAL / 'PvsNPCartography/Mod3TenDegree.lean').read_text()
    if hashlib.sha256(source.encode()).hexdigest() != EXPECTED:
        raise ValueError('Production source changed; reconcile before profiling')
    close = '\nend PvsNPCartography.Mod3Ten\n'
    base = source.split('theorem weights_sum', 1)[0]
    prefix = source.split('/-- All eleven full-cube layer sums', 1)[0] + close
    layer = source.split('def layerTickets', 1)[1].split('theorem upper_layer_bound', 1)[0]
    targets = ['weights_sum','mass_sum','canonical_affine_bound','affine_bound',
               'layer_tickets_exact','upper_layer_bound','seed_correct','seed_success',
               'seed_layer_bound','degree_two_feasible','degree_one_impossible',
               'feasible_degree_iff','least_feasible_degree','pdeg_eq_two',
               'raw_seed_mixture_is_not_pointwise']
    reports = '\n'.join('#print axioms PvsNPCartography.Mod3Ten.' + t for t in targets) + '\n'
    results = []
    def save(item):
        results.append(item)
        (OUT / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    smoke = run('cbv-smoke', 'import Mathlib\nexample : (17 : Nat) * 3 = 51 := by decide_cbv\n', 30)
    save(smoke)
    save(run('kernel-mass', base + 'theorem diagnostic_mass : (∑ x, mass x) = 240 := by decide +kernel\n' + close, 45))
    save(run('kernel-lower-prefix', prefix, 75))
    if smoke['exit_code'] == 0:
        save(run('cbv-lower-prefix', prefix.replace('decide +kernel', 'decide_cbv'), 90))
        save(run('cbv-layer-only', (base + 'def layerTickets' + layer + close).replace('decide +kernel', 'decide_cbv'), 150))
        save(run('cbv-full-with-axioms', source.replace('decide +kernel', 'decide_cbv') + reports, 240))
    print('DIAGNOSTIC_RESULTS', json.dumps(results, sort_keys=True), flush=True)
    print('Diagnostics record failures; this exit status does not certify the production library.', flush=True)

if __name__ == '__main__':
    main()
