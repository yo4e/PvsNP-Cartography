#!/usr/bin/env python3
"""Targeted repair experiment after inspecting the first diagnostic failures.

Keep the already successful kernel lower proof. Change only the upper layer
proof, not its statement or data. Temporary successes require later production
root compilation and namespace audit before promotion.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import signal
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / 'formal'
OUT = ROOT / 'n10-profile-output'
EXPECTED = 'bd998f8ad908a1622cac393dd3b68e62505f2bc01dd2ef9010b9cb7e5c948e93'
TARGETS = ['weights_sum','mass_sum','canonical_affine_bound','affine_bound',
           'layer_tickets_exact','upper_layer_bound','seed_correct','seed_success',
           'seed_layer_bound','degree_two_feasible','degree_one_impossible',
           'feasible_degree_iff','least_feasible_degree','pdeg_eq_two',
           'raw_seed_mixture_is_not_pointwise']
ALLOW = {'propext','Classical.choice','Quot.sound'}


def execute(name, source, seconds, expect_reports):
    file = FORMAL / 'N10RepairProbe.lean'
    file.write_text(source)
    (OUT / (name + '.lean')).write_text(source)
    started = time.monotonic()
    print('START', name, 'timeout_seconds', seconds, flush=True)
    process = subprocess.Popen(['lake','env','lean','N10RepairProbe.lean'],
        cwd=FORMAL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True)
    timed_out = False
    try:
        output, _ = process.communicate(timeout=seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(process.pid, signal.SIGKILL)
        output, _ = process.communicate()
    output = output.decode('utf-8', errors='replace')
    code = 124 if timed_out else process.returncode
    reports = re.findall(r"'PvsNPCartography\.Mod3Ten\.([A-Za-z0-9_]+)' depends on axioms: \[([^]]*)\]", output)
    audited = all(set(a.replace(' ','').split(',')) <= ALLOW for _,a in reports)
    complete = not expect_reports or (set(t for t,_ in reports)==set(TARGETS) and audited)
    success = code==0 and complete and 'sorryAx' not in output and 'error:' not in output
    item = {'name':name,'exit_code':code,'timed_out':timed_out,
            'elapsed_seconds':round(time.monotonic()-started,3),'accepted_diagnostic':success,
            'target_reports':len(reports),'reports_allowlisted':audited,
            'source_sha256':hashlib.sha256(source.encode()).hexdigest()}
    (OUT / (name + '.log')).write_text(output)
    print(json.dumps(item,sort_keys=True),flush=True)
    print(output,flush=True)
    return item


def main():
    OUT.mkdir(exist_ok=True)
    source=(FORMAL/'PvsNPCartography/Mod3TenDegree.lean').read_text()
    if hashlib.sha256(source.encode()).hexdigest()!=EXPECTED:
        raise ValueError('production changed; reconcile before applying a repair')
    before, rest=source.split('theorem layer_tickets_exact',1)
    declaration, after=rest.split('theorem upper_layer_bound',1)
    statement, old_proof=declaration.split(':= by',1)
    if old_proof.strip()!='decide +kernel':
        raise ValueError('unexpected proof shape')
    base=source.split('theorem weights_sum',1)[0]
    layer_table='def layerTickets'+before.split('def layerTickets',1)[1]
    close='\nend PvsNPCartography.Mod3Ten\n'
    reports='\n'+ '\n'.join('#print axioms PvsNPCartography.Mod3Ten.'+t for t in TARGETS)+'\n'
    candidates=[('split-kernel','\n  intro w\n  fin_cases w <;> decide +kernel\n\n'),
                ('bounded-cbv','\n  set_option cbv.maxSteps 6000000 in\n    decide_cbv\n\n'),
                ('split-bounded-cbv','\n  intro w\n  fin_cases w <;> (set_option cbv.maxSteps 2000000 in decide_cbv)\n\n')]
    results=[]
    for name, proof in candidates:
        replacement='theorem layer_tickets_exact'+statement+':= by'+proof
        layer_source=base+layer_table+replacement+close
        item=execute(name+'-layer',layer_source,180,False)
        results.append(item)
        (OUT/'repair-results.json').write_text(json.dumps(results,indent=2)+'\n')
        if not item['accepted_diagnostic']:
            continue
        candidate=before+replacement+'theorem upper_layer_bound'+after
        full=execute(name+'-full',candidate+reports,270,True)
        results.append(full)
        (OUT/'repair-results.json').write_text(json.dumps(results,indent=2)+'\n')
        if full['accepted_diagnostic']:
            (OUT/'candidate-production.lean').write_text(candidate)
            print('CANDIDATE_PRODUCTION_SHA256',hashlib.sha256(candidate.encode()).hexdigest(),flush=True)
            break
    print('REPAIR_RESULTS',json.dumps(results,sort_keys=True),flush=True)
    if not any(i['accepted_diagnostic'] and i['name'].endswith('-full') for i in results):
        raise SystemExit('No fully checked diagnostic candidate. Production remains unchanged.')
    print('Diagnostic full target PASS; production root/namespace audit still required.',flush=True)

if __name__=='__main__':
    main()
