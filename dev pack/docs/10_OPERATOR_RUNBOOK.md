# 10 | Developer/operator runbook, failure recovery and operational transition

## 10.1 Environments and trust

**Development:** isolated checkout at exact owner head, mock CTO in a restricted Docker container, local persisted test volume, no live host access. Run only current target-proven test commands; the pack does not authorize arbitrary shell commands or personal tokens.

**Host integration lab:** operator Mac, separate least-privilege host worker OS identity, installed project-governed Claude SDK with valid account trust, dedicated disposable test worktree/remote. Authenticated selected bridge and durable journal, no human merge-grant file access.

**Operational pilot:** explicitly granted CTO actor/surface plus scoped delegations and memory namespaces, documented exact release digest and rollback; at most one active campaign and worker.

## 10.2 Boot sequence checklist

1. Pin exact image/checkout/authority revisions and record them in operator-visible receipt.
2. Inspect compose for forbidden host mounts, Docker socket, elevated capabilities, ambient credentials and unrestricted shell ingress.
3. Confirm checkpoint named volume and backup/restore ability; exercise write/read across container restart before accepting live work.
4. Resolve verified identity and applicable operating-plane permissions; if absent, run read-only diagnostics only.
5. Load existing memory package and principal bindings without borrowing Claude credentials; verify direct authorization on allowed namespace.
6. Observe host authenticated interface and journal health; execute read-only canary through existing SDK; record actual SDK session and host journal.
7. Resume prior campaign/thread, inspect all pending IDs and verify external effect facts before new submission.
8. Check campaign native contract completeness, target SHA and protected-effects list.
9. Report eligible capabilities separately from blocked/unknown ones; no magic READY boolean.
10. Permit only the exact action the host independently authorizes now.

## 10.3 Routine campaign operating loop

For each stage: inspect latest source/PR state; bind exact frozen objective and authorized next action; check root autonomy claims; submit stable id; observe host execution; independently validate effect; handle bounded remediation/next stage; persist checkpoint; write governed memory only after evidence. Any pending human grant is reported with exact repo/PR/head and remains `MERGE_PENDING` until genuinely issued by a human under the existing mechanism.

A CTO should produce a compact status containing: campaign and target ref, last accepted stage, active operation id, last actual host observation, source/permission revision, pending verification, next lawful action, and precise operator decision requested, if any. Status must say `UNKNOWN` where observation was not possible.

## 10.4 Incident playbooks

### Lost submit acknowledgment

Stop submitting new operation IDs. Query `observe` using the stable original id. If accepted/running/terminal, continue with that record. If not found but possibility of an effect remains, inspect worktree, GitHub and process ledger; do not guess non-occurrence. Only a verified safe no-effect condition or provider-idempotent contract can justify a new launch.

### Host process unavailable

Freeze consequential dispatch. Keep Docker service inspectable if possible. When host returns, validate its identity/key, journal and worker environment, then reconcile every in-flight operation. Restarting container cannot justify duplicate work.

### Canonical authority changed

Invalidate affected source/profile/actor projections and current grants, rebind from a verified single revision through owners. Existing completed external effects remain historical facts, but future operation authorization must be re-evaluated; stale binding is not silently repaired from memory.

### Memory degraded

Determine whether affected work requires memory. For optional hydration, preserve unavailable context and continue only independently provable read-only work. For mandatory memory-dependent stage, halt that stage. Do not pull an unscoped memory DB, swap principal, or promote worker notes as shared truth.

### Worktree/PR divergence

Observe current remote head, read task metadata, compare with exact contract base. Cancel/stop only as authorized and preserve all foreign local changes. Do not use `git reset --hard`, `clean`, forced rewrite or wide `git add` as recovery. New staged source amendments require fresh owner/grant and relevant test evidence.

### Merge required

Report `MERGE_PENDING` with exact current PR head, checks, review and stack order, plus governing human-only grant route. CTO must not invoke `authorize_merge.py`, write grant file, use autonomous merge or reuse old head's grant. Worker OS principal must lack ability to access human issuer data.

### Checkpoint corruption / volume unavailable

Mark continuity failed and consequential work suspended. Restore from verified backup if one exists, then reconcile host journal and remote effects before resuming. An apparently empty checkpoint is not a new campaign if prior host ops exist; preserve their identities.

### Budget exhaustion / repeated remediations

Stop after bounded budget/turn/attempt caps specified by accepted campaign. Escalate smallest specific missing decision/evidence; do not recursively spawn workers to hide failure or introduce a new scheduler.

## 10.5 Rollback and clean shutdown

- **Code rollback:** Use existing repo/PR safety path with exact scope and authorized operation; do not self-authorize destructive clean/force-push.
- **Deployment rollback:** Stop accepting new campaigns, terminate/cancel authorized host work only after observing effects, preserve journal and checkpoints, run earlier verified image with compatible persistence after source-bound review.
- **Memory rollback:** Never delete governed memory to conceal erroneous work; record corrected/superseded evidence using MemoryService owner semantics.
- **Emergency stop:** A host-enforced disable must halt new executable admissions while preserving observational status and durable effect records. Do not rely on a model agreeing to stop.

## 10.6 Performance/operability measures

Measure: operator relays per accepted campaign, time from valid pack to first lawful action, percentage with exact acceptance, false-READY incidents, unauthorized actions actually denied, duplicate external effects (target zero), mean time to reconcile lost ACK, time and cost per delegated task, memory-fact provenance fidelity and number of new cross-cutting components. No arbitrary SLO is invented before observing pilot baseline.

## 10.7 Promotion checklist

**Do not promote** until source/identity current, host transport independently secured, actual worker invocation proven, effect journal durable, corrupt/reboot/lost-ACK cases passed, qualified review supported, memory access correct, protected merge blocked without real grant and operator understands the stop/restore procedures. Release status report must clearly identify what is proven live vs what remains mock or unexecuted.

## v1.1 | AgentPod operating checks (not yet executed)

- Confirm CTO canonical actor/surface and exact source revision; require scoped agent Hub MCP authorization before attempting service dispatch. `apn` is the Mac machine daemon, `fleet` is the separate operator/fleet client; CTO must not reuse operator token or node secrets.
- Independently verify the enrolled Mac station and restricted worker account; APN local service online is insufficient for CTO READY. Deny `terminal` and generic `fs.write` for the CTO principal; test denied routes before enabling any real worker.
- Confirm Cursor ACP station descriptor is present and audited, and that actual CLI `agent acp` can start a read-only session with current repository rules. Confirm Claude station project hooks and native coding contract parity separately.
- For each action, inspect root-autonomy lease/campaign/scope/capability receipt **and** host-side acceptance journal. Force revoke and stale SHA negatives. On disconnect: restore CTO checkpoint, query host by operation id, preserve UNKNOWN until independently reconciled; never blindly resend.
- Never use successful AgentPod Hub connectivity or `fleet agents` inventory as effect/completion/merge proof. Protected exact-head merge authority stays human-issued.
