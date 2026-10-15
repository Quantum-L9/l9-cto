```yaml
repository_access:
  writable:
    - https://github.com/Quantum-L9/Cursor-Governance
  read_only:
    - https://github.com/Quantum-L9/.github
    - https://github.com/Quantum-L9/l9-graphiti-memory
  unlisted_repositories: no_access
```

# Claude Code | Bounded CTO implementation contract, F1 only

**Contract ID:** CTO-DEV-F1-2026-10-14  
**Status:** READY FOR OPERATOR REVIEW, NOT EXECUTION-AUTHORIZED  
**Delivery:** bounded implementation PR to the existing Cursor-Governance integration branch, subject to exact current repository authority and publication-gate checks.  
**Parent pack:** `CTO-DEV-PACK-001`.

## Objective

Implement the first **mock-only** executable CTO LangGraph vertical slice on the accepted file tree. It runs in restricted Docker, consumes or accurately reports current source/identity/permission/readiness, accepts one campaign, selects a bounded next action, uses an injected mock host operation protocol, stores checkpoint state, restores after loss of ACK without duplicate simulated effects, and never claims real host execution or independent acceptance. Do not attempt to implement all F2–F6 now.

## Governing locked decisions

Read `docs/00_EXECUTIVE_CONTRACT.md` through `docs/09_ACCEPTANCE_AND_NEGATIVE_TESTS.md`; read original source charter, pinned recon and filetree. Freeze CTO-BOOTSTRAP-001, CTO-READY-001 obligations and no shadow execution plane. Do not reinterpret the output as a new Node/ProductKind, permission authority, coding contract, MemoryService or general orchestration service.

## Source/head preflight

At work start resolve exact live GitHub `main` head, current open PR topology, native owner contracts and clean dedicated task worktree. The evidence baseline in the pack was `Cursor-Governance@4cc0d7dc...`, `.github@d4397e53...`, memory `@441b741e...`. They are **inspection coordinates**, not a license to implement against stale checkout state. If source currentness invalidates assumptions, report a bounded incompatibility; do not amend frozen architecture inside F1.

## Authorized read set

Current, relevant files in `workflows/dags/_runtime`, existing GMP graph/executor examples, root autonomy status/receipt readers, `environment/agents/adapters/claude-agent-sdk` options and tests, `skills/l9-coding-agent` native contract/schema, `ops/memory` runtime binding, Python test catalog, SDK optional lock entries, user-accepted CTO filetree, `AGENTS.md` current amendments. Upstream `.github` and memory are **strictly read-only**.

## Proposed mutation scope (not granted by this pack)

- `workflows/dags/cto/graph.py` (new, minimum source-proven)
- `workflows/dags/cto/executor.py` (new, minimum source-proven)
- `tests/workflows/test_cto_runtime.py` (new, minimum source-proven)
- `ops/cto/Dockerfile` (new, minimum source-proven)
- `ops/cto/compose.yaml` (new, minimum source-proven)

An explicit `__init__.py` is conditional and requires real import failure proof. `pyproject.toml`/lock changes are not approved by default; inspected baseline already declares LangGraph/sqlite saver. Do not mutate operational identity registry, root autonomy store, SDK launcher, Mac host bridge, memory config, publisher or merge gate during F1. No write to `.github` or `l9-graphiti-memory`.

## Acceptance criteria, mandatory

1. Existing LangGraph checkpoint helper is used, no new checkpoint system.
2. Graph builder has no compile call or effects; executor is the only compile/checkpointer site.
3. One campaign/thread, deterministic mock adapter, stable operation ID and target fingerprint.
4. Duplicate identical operations have one simulated effect; conflicting payload under same id is rejected.
5. After lost ACK and second executor instance, observe and recover without replaying simulated effect.
6. Startup with absent CTO actor, invalid source/identity/delegation and unavailable host reports blocked rather than READY.
7. No real SDK process, host shell, production repo mutation, remote GitHub write, merge or secret loading is reachable from the mock path.
8. Docker image is unprivileged, no host home/socket/grant mounts, and persisted checkpoint volume survives restart.
9. Unit/fixture tests cover BT-001, BT-002, BT-005, BT-008, BT-010, BT-014, CP-001–008, IO-001–004, RC-001–003, RC-005 and optional memory/false-READY cases applicable to F1. Report skipped live tests as NOT_RUN.
10. No legacy `environment/program-execution` import or Igorbot/OpenClaw dependency.
11. No new file beyond five proposed paths unless a concrete existing invariant cannot be satisfied and independent acceptance approves that conditional delta.
12. Produce exact test results/commit+diff, dependency and implementation evidence; do not report real execution ready.

## Forbidden actions

- Actor/surface registration or self-authorized memory principal activation.
- New CTO coding-execution schema, scheduling service, publisher, credentials/secret authority, API daemon, or generic process control.
- Attempts to run `authorize_merge.py`, auto-merge, write human grant files, bypass protected hooks or invoke remote effect with an in-container worker.
- Direct write to read-only dependencies; modifying unapproved files; resetting/cleaning foreign dirty work.
- Fabricating a compiler PASS, canonical actor/grant, host worker result or independent assessment.

## Validation and review procedure

Use exact target-verified test/validation commands from the *live* code owners (no Make command is inferred from this pack). A minimal local test, current DAG authoring package validator, source/permission review and Docker isolation probe must pass. Read-only proof should happen before any publication ceremony. Follow verified Cursor-Governance SSOT publication mechanism once on authorized scope; the contract alone is not a push/PR grant. Return CI checks/reviews as externally observed, not assumed.

## Done / not done declaration

Output the list of changed paths, exact source SHA, actual tests/proof, unrun host cases and a phase F1 verdict. State F2–F6 are **not implemented**. A passing F1 demonstrates mock-only viability; it cannot grant canonical CTO identity, host execution, memory namespaces or protected rights.

## v1.1 | Later architecture lock does not widen F1

Operator subsequently selected AgentPod Hub MCP/APN host transport, Cursor CLI ACP worker support and reuse of root `AutonomyRuntime` and `AdapterOrchestrator`. **F1 remains exactly mock-only with the same five planned new paths.** Do not install APN, add network ingress, change autonomy policies, touch `.github`, mutate AgentPod, create a host bridge, activate signed CTO principal, or launch real worker under F1. Upstream actor admission and AgentPod provider integration belong to separately authorized F2/F3 WPs in updated chapter 08. Refresh current CG head from the later v1.1 reviewed `0bb60d78...` and resolve any intervening changes before execution. The original `4cc0d7dc...` remains prior recon provenance, not today's target authority.
