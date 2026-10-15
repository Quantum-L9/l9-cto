#!/usr/bin/env python3
"""Local integrity/consistency check for the CTO developer *plan*, not runtime admission."""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    raise SystemExit('yaml dependency missing; cannot validate pack')
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def getj(p): return json.loads((ROOT/p).read_text())
def check(cond, desc):
    if not cond: errors.append(desc)

src=getj('machine/source_baselines.json')
for name,obj in src['source_documents'].items():
    b=(ROOT/'sources'/name).read_bytes()
    check(len(b)==obj['size_bytes'] and hashlib.sha256(b).hexdigest()==obj['sha256'],f'original source digest mismatch: {name}')

items=getj('machine/work_items.json')['items']
assert isinstance(items,list)
workids=[w['id'] for w in items]
check(len(workids)==len(set(workids)),'duplicate WP identity')
tests=getj('machine/acceptance_tests.json')['cases']
testids=[t['id'] for t in tests]
check(len(testids)==len(set(testids)),'duplicate test identity')
check(all(t['status']=='NOT_RUN' and not t['evidence'] for t in tests),'plan contains claimed test success')
check(all(w['status']=='NOT_STARTED' for w in items),'plan contains claimed implementation success')

seen=set();active=set()
byid={x['id']:x for x in items}
def walk(i):
    if i in active:
        errors.append('DAG cycle: '+i);return
    if i in seen:return
    if i not in byid:
        errors.append('unknown work package '+i);return
    active.add(i)
    for d in byid[i]['dependencies']:walk(d)
    active.remove(i);seen.add(i)
for i in workids:walk(i)
for x in items:
    check(set(x['tests']).issubset(testids),'work item has nonexistent test '+x['id'])

matrix_doc=(ROOT/'docs/09_ACCEPTANCE_AND_NEGATIVE_TESTS.md').read_text()
parsed=set(re.findall(r'^\| ((?:BT|CP|IO|RC|MS|PB)-\d{3}) \|',matrix_doc,re.M))
check(parsed==set(testids),f'machine test IDs differ from document: {sorted(parsed^set(testids))}')

files=getj('machine/file_dispositions.json')['paths']
check(len(files)==len({x['path'] for x in files}),'duplicate file disposition')
check(all('/' not in x['path'][:1] for x in files),'absolute file path in plan')
check({x['path'] for x in files if x['disposition']=='NEW_F1'}=={
 'workflows/dags/cto/graph.py','workflows/dags/cto/executor.py','ops/cto/Dockerfile','ops/cto/compose.yaml','tests/workflows/test_cto_runtime.py'
},'F1 file tree grew beyond five committed new paths')

gates=yaml.safe_load((ROOT/'machine/readiness_gates.yaml').read_text())
for g in gates['gates']:
    check(set(g['tests']).issubset(testids),'readiness gate unbound test '+g['id'])
check(gates['mandatory_for_live_worker']==['G1','G2','G3','G4'],'mandatory readiness gate changed')
check(gates['conditional_required_for_memory_dependent_operation']==['G5'],'memory gate semantics changed')

cap=yaml.safe_load((ROOT/'capture.yaml').read_text())
check(cap['source']['completeness']=='partial' and cap['canonical']['resolution']=='partial','false source completeness or canonical resolution')
check(cap['independent_reconstruction']['status']=='not_run','faked independent reconstruction')
cp=(ROOT/cap['source']['path']).read_bytes()
check(hashlib.sha256(cp).hexdigest()==cap['source']['sha256'],'partial donor source digest mismatch')
msgs=[json.loads(l) for l in cp.decode().splitlines() if l.strip()]
check([x['id'] for x in msgs]==[x['message_id'] for x in cap['message_coverage']],'partial message coverage mismatch')
mt={m['id']:m['content'] for m in msgs}
for c in cap['claims']:
    for ev in c['evidence']:
        check(ev['quote'] in mt.get(ev['message_id'],''),'claim quoted text absent: '+c['id'])

for p in ['README.md','docs/00_EXECUTIVE_CONTRACT.md','docs/01_SOURCE_AUTHORITY_AND_FACTS.md','docs/02_SYSTEM_ARCHITECTURE.md','docs/03_BOOTSTRAP_AND_READINESS.md','docs/04_CAMPAIGN_AND_STATE_MACHINE.md','docs/05_HOST_WORKER_PORT_AND_EFFECTS.md','docs/06_MEMORY_SECURITY_AND_PERMISSIONS.md','docs/07_LOCKED_FILETREE.md','docs/08_WORK_PACKAGES_AND_DEPENDENCIES.md','docs/09_ACCEPTANCE_AND_NEGATIVE_TESTS.md','docs/10_OPERATOR_RUNBOOK.md','docs/11_REFERENCE_CAMPAIGN.md','docs/12_RISK_UNKNOWN_AND_DECISION_REGISTER.md','docs/13_TRACEABILITY_AND_COVERAGE.md','handoffs/CLAUDE_CODE_BOUND_DELEGATION.md']:
    check((ROOT/p).is_file() and (ROOT/p).stat().st_size>500,'mandatory document missing or empty: '+p)

# v1.1 locked decision integrity without claiming external admission
ledger=yaml.safe_load((ROOT/'machine/decision_register.yaml').read_text())
decs={d['id'] for d in ledger['decisions']}
check({f'CTO-D{i:03d}' for i in range(19,25)}.issubset(decs),'missing v1.1 operator decisions')
checks_v11={'WP-17','WP-18'}
check(checks_v11.issubset(set(workids)),'missing provider/host implementation WPs')
check({'IO-017','IO-018','IO-019','IO-020','IO-021','IO-022','IO-023','IO-024','IO-025','IO-026','BT-015','BT-016','BT-017','BT-018','PB-011','MS-013'}.issubset(set(testids)),'missing v1.1 negative tests')
check('AgentPod' in (ROOT/'README.md').read_text(),'AgentPod decision missing')
check('0bb60d78' in (ROOT/'machine/source_baselines.json').read_text(),'reviewed CG source head missing')
check(src.get('agentpod_host_principal_proven') is False and src.get('root_autonomy_cto_operational_binding_proven') is False,'fake host/actor proof claimed')
verdict={'status':'FAIL' if errors else 'PACK_CONSISTENCY_PASS_NOT_RUNTIME_PROOF',
         'errors':errors,'source_documents':len(src['source_documents']),
         'work_packages':len(items),'test_cases':len(tests),'file_dispositions':len(files),
         'readiness_gates':len(gates['gates']),
         'source_completeness':'PARTIAL','canonical_producer_receipt':'NOT_PROVEN',
         'runtime_tests_executed':False,'host_live_proof':False,
         'meaning':'Plan structure, source bytes, test refs, DAG and capture quotes checked only; no code installed or test run.'}
print(json.dumps(verdict,indent=2))
sys.exit(1 if errors else 0)
