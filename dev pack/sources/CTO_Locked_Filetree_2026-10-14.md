# L9 CTO | Locked Bootstrap Decision and Source-Grounded File Tree

**Decision:** CTO-BOOTSTRAP-001  
**Date:** 2026-10-14  
**Mode:** FILETREE / architecture-to-implementation boundary; **read-only**  
**Status:** BOOTSTRAP APPROACH LOCKED; FILE PLACEMENT PROPOSED AND SOURCE-GROUNDED; LIVE EXECUTION BLOCKED BY ADMISSION/TRANSPORT PROOF  
**Target repository:** `https://github.com/Quantum-L9/Cursor-Governance`  
**Target source baseline:** `4cc0d7dc858021bc8e2a95a904e2945fd3d3acba`  
**Canonical owner baseline:** `Quantum-L9/.github@d4397e53f8f4c23458a80f87db9552463ad9e26f`  
**Memory owner baseline:** `Quantum-L9/l9-graphiti-memory@441b741e31a7bb5a57849e5b49b97465b1c7ee58`  
**Supporting recon:** `cto_environment_recon_2026-10-14.md`  
**Source design:** `CTO Architecture(1).md` and `Cto!!!(1).md` (source documents; the subsequent exact-source recon corrects stale observations).

## 1. Locked architectural decisions

**D01. One governance foundation, three activation paths.** Cursor consumes Cursor-Governance through its IDE `sessionStart` hook; Claude Code consumes the same governance through its native `SessionStart`/project settings; the L9 CTO consumes canonical authority and existing Cursor-Governance capabilities through a **service-native start/recovery** path. The CTO does not call either interactive session hook as its primary bootstrap.

**D02. Different actor, different runtime.** The CTO must resolve independently admitted product/release/runtime/actor/surface identities from canonical upstream source/projection and actual runtime evidence. It does not borrow Cursor or Claude Code identity. The string `l-cto` is presently a **local reserved placeholder**, not a canonical admission. Do not preselect a canonical CTO actor ID, SurfaceIdentity spelling, local role, provider or permissions.

**D03. No parallel authority or execution plane.** `Quantum-L9/.github` owns canonical semantic and identity authority; Cursor-Governance owns existing operating-plane bindings, gates, worktree handling, Claude SDK integration and publication machinery. L9 Graphiti Memory owns memory service/authorization. The CTO owns executive judgment, campaign continuation and reconciliation, **not** their domains.

**D04. LangGraph is executive runtime only.** Use existing repository LangGraph `StateGraph` and `open_checkpointer()` rather than a new orchestrator/persistence framework. Persist CTO graph threads on an explicitly mounted Docker-owned volume. Checkpoints are not external-effect evidence and not shared memory.

**D05. Governed worker delegation.** The actual implementation worker remains Claude Code under its own project bootstrap and tool gates, launched via the existing Claude Agent SDK harness. CTO issues a bounded native coding contract/request; a host-owned boundary validates and observes it. Do not translate into new coding-contract semantics.

**D06. Convergence must be observed.** A stable operation identifier, durable host acceptance, independent observation and idempotent reconciliation are mandatory before real worker dispatch. The CTO cannot infer a successful effect from its own checkpoint or a worker's prose. The eventual host boundary supports `submit`, `observe`, `cancel` without becoming a generic platform.

**D07. No autonomous human-grant fabrication.** Publication uses the existing governed route only when explicitly authorized. Merge remains independently human-granted per repository/PR/exact head. The CTO must not possess the ability to mint human merge grants or write grant records, including through same-user OS account exposure.

**D08. Mac Docker first, no Igorbot/OpenClaw.** CTO Python/LangGraph lives in a container on Mac Docker Desktop. The native Claude execution path stays on the Mac. No host-home or Docker socket mounts, OpenClaw, Igorbot runtime, or Program Execution (`environment/program-execution/`) dependency.

**D09. Fail closed per capability.** Inability to authenticate semantic authority/actor or authorize a consequential effect blocks that effect. A mock-only graph may run and report `MOCK_ONLY` but must never report production `READY` or `VERIFIED`.

**D10. Freeze discipline.** Only necessary files are proposed. `NEW-CONDITIONAL` is not permission to create the file now; the stated missing capability, existing-owner insufficiency, transport choice and exact contract must be proved first. This decision does not authorize canonical registry mutation, Docker deployment, repository writes, PR creation or merge.

## 2. Source-grounded file tree

Legend: `=` existing `REUSE` unchanged, `~` existing `EXTEND` only for an established necessity, `+` justified `NEW` for the first safe vertical slice, `?` `NEW-CONDITIONAL` or conditional extension after proof, `x` `EXCLUDE`, `G` generated output (never hand-edit). The tree describes *intended source placement*, not files already created.

```text
Quantum-L9/Cursor-Governance/                          [implementation HOME]
|
|-- workflows/                                         [LangGraph/runtime owner]
|   |-- dags/
|   |   |-- _runtime/
|   |   |   `-- durable_checkpointer.py               = REUSE: SqliteSaver; stable thread ID
|   |   |-- gmp/                                      = REFERENCE exemplar, not CTO behavior
|   |   |-- intelligence_harvest/                     = REFERENCE exemplar, not CTO behavior
|   |   `-- cto/                                      + NEW CTO-specific graph domain
|   |       |-- graph.py                              + NEW: CTO state, decision routing,
|   |       |                                             mock effect state transitions
|   |       |-- executor.py                           + NEW: service-native startup,
|   |       |                                             readiness, checkpoint resume,
|   |       |                                             injected host port/CLI
|   |       `-- __init__.py                          ? NEW only if package/import proof requires
|   `-- README.md                                     ~ EXTEND: source-owner index only
|
|-- environment/
|   `-- agents/
|       |-- agent_registry.yaml                      ? EXTEND after canonical actor/surface admission
|       |-- PEER_RUNTIME_BINDINGS.yaml               ? EXTEND only if CTO is admitted as this kind of peer
|       `-- adapters/
|           |-- claude-code/
|           |   |-- README.md                         = REUSE: worker session/bootstrap law
|           |   `-- settings.template.json            = REUSE: worker permissions/hooks
|           `-- claude-agent-sdk/
|               |-- README.md                         ~ EXTEND usage with proven CTO host contract
|               |-- l9_agent.py                       ? EXTEND bounded per-operation launch/report
|               |-- validate_agent_sdk_env.py         = REUSE; EXTEND tests only if obligation changes
|               |-- host_bridge.py                    ? NEW-CONDITIONAL: authenticated Mac-host
|               |                                         submit/observe/cancel integration, only
|               |                                         if no current owner can supply it
|               `-- tests/
|                   |-- test_l9_agent.py               ~ EXTEND existing harness test suite
|                   `-- test_host_bridge.py            ? NEW-CONDITIONAL if new bridge exists
|
|-- autonomy/                                          [root policy / leases / claims]
|   |-- runtime/
|   |   |-- engine.py                                 = REUSE if independently verified applicable
|   |   |-- store.py                                  ? EXTEND existing host-side SQLite if
|   |   |                                             durable operation journal is required
|   |   |-- leases.py                                 = REUSE CANDIDATE
|   |   |-- claims.py                                 = REUSE CANDIDATE
|   |   `-- receipts.py                               = REUSE CANDIDATE
|   |-- adapters/
|   |   |-- orchestrator.py                           = REUSE contract/lease admission as applicable
|   |   |-- bridge.py                                 = REUSE JSON-line lease interface;
|   |   |                                             NOT the Claude worker launcher
|   |   |-- cursor/host_bridge.py                     = REFERENCE only (Cursor Task surface)
|   |   `-- claude_code/adapter.py                    = REUSE Claude task rendering, where applicable
|   `-- runtime/cli.py                                x DO NOT CALL: intentionally disabled CLI
|
|-- skills/
|   |-- l9-coding-agent/
|   |   |-- contracts/EXECUTION_CONTRACT.yaml         = REUSE native task fields and scope
|   |   |-- schemas/execution-contract.schema.json   = REUSE structural schema
|   |   |-- schemas/execution-receipt.schema.json    = REUSE native evidence shape
|   |   |-- scripts/validate_execution_contract.py   = REUSE; not permission grant
|   |   `-- scripts/verify_canonical_binding.py      = REUSE applicable invariant-binding check;
|   |                                                 not a CTO actor identity verifier
|   `-- l9-dag-authoring/                             = REUSE LangGraph validity requirements
|
|-- ops/
|   |-- config/
|   |   `-- memory-binding.json                      = REUSE pinned MemoryService release
|   |-- memory/
|   |   |-- runtime_binding.py                        = REUSE installed memory version/contract proof
|   |   |-- control_plane_client.py                  = REUSE bounded CLI/hook client only
|   |   |-- agent_identity.py                         ? CONSUME / review local CTO placeholder;
|   |   |                                             no self-admission by modifying code
|   |   |-- materialize_agent_authority.py           = REUSE approved per-principal grants
|   |   `-- run_memory_mcp.sh                         = REUSE signed stdio launch where applicable
|   |-- scripts/
|   |   |-- agent_worktree_start.sh                   = REUSE host-owned worktree creation
|   |   |-- worktree_add_wired.sh                     = REUSE host-owned worktree wiring
|   |   `-- open_pr_after_gate.sh                     = REUSE publication only after separate grant
|   |-- autonomy/
|   |   |-- authorize_merge.py                       = PROTECTED human-only; never CTO callable
|   |   |-- merge_gate.py                            = REUSE mandatory effect gate
|   |   `-- stack_safe_merge.py                      = REUSE human-granted merge path only
|   `-- cto/                                         + NEW CTO container deployment owner
|       |-- Dockerfile                               + NEW: isolated executive image, no SDK
|       |                                             worker/host secrets in image
|       `-- compose.yaml                             + NEW: bounded container, persisted
|                                                     checkpoint volume, no host-home/socket
|
|-- generated/
|   `-- governance/canonical_identity.yaml           G REGENERATE via current upstream owner;
|                                                     existing projection revision != current pin
|-- .claude/settings.json                            = REUSE worker gates; no CTO-owned hooks
|-- .mcp.json                                        = REUSE worker memory tool config;
|                                                     do not infer CTO container MCP connectivity
|-- AGENTS.md                                        = READ current authoritative amendments
|-- CANONICAL_LAW.md                                 = READ current governance law
|-- ARCHITECTURE.md                                  ~ EXTEND index if real source owner is added
|-- pyproject.toml                                   = REUSE LangGraph/sqlite dependencies;
|                                                     EXTEND only if a proven dependency is missing
|-- uv.lock                                          = REUSE; change only with approved dep delta
|-- filetree.md                                      G generated projection; never hand-edit
|-- tests/
|   |-- workflows/
|   |   |-- test_langgraph_durable_resume.py          = REUSE existing crash-resume proof
|   |   `-- test_cto_runtime.py                       + NEW: CTO domain/bootstrap/mock/restart
|   |-- ops/memory/test_agent_identity.py             ~ EXTEND if admitted CTO identity is bound
|   `-- ops/memory/test_cross_repo_lifecycle.py      = REUSE exact memory integration proof
|
`-- environment/program-execution/                   x EXCLUDE from new CTO imports/launch
```

### Upstream and external owners (not part of CTO write scope)

```text
Quantum-L9/.github@d4397e53...                    [CANONICAL; READ-ONLY in CTO campaign]
`-- semantics/
    |-- identity_model.yaml                         = REUSE canonical identity dimensions
    |-- actor_registry.yaml                         ? UPSTREAM admission of distinct CTO actor
    |-- surface_registry.yaml                       ? UPSTREAM admission of Docker service surface
    |-- canonical_sources.yaml                      = REUSE registered authority source catalog
    `-- projection_profiles.yaml                    ? OWNER admission/update if needed

Quantum-L9/l9-graphiti-memory@441b741e...            [MEMORY OWNER; READ-ONLY]
`-- src/l9_graphite_memory/
    |-- sdk.py                                      = REUSE authenticated typed MemorySDK
    |-- server.py                                   = REUSE MCP adapter
    `-- authz/signed_assertion.py                   = REUSE per-principal assertion validation

Mac host (runtime deployment, NOT tracked by Docker repo):
  Cursor-Governance checkout + governed Claude SDK + native worktrees +
  host-owned operation journal + existing permissions/merge gates.

Docker persistent runtime state (DATA, not git-tracked source):
  <named-volume>/.l9/langgraph/cto.sqlite             LangGraph thread checkpoints
  Note: actual path follows open_checkpointer(dag_id, workspace=...); this
  is an intended runtime volume mapping, not a newly admitted store contract.
```

## 3. Why each new file is justified

| New file/path | Why no existing file can lawfully own it | Acceptance boundary |
|---|---|---|
| `workflows/dags/cto/graph.py` | Existing graphs are GMP and intelligence-harvest domain flows; CTO decisions are a new domain. The LangGraph graph builder has a distinct responsibility from persistence/entrypoint. | Mock CTO state graph routes bootstrap, intake, action decision, observation, reconciliation and terminal/blocked states without runtime side effects. |
| `workflows/dags/cto/executor.py` | Existing executor files are tied to other domain graph types. The LangGraph runtime contract requires executable compile/checkpoint in the executor, not the graph builder. Service-native CTO startup is not an IDE/Claude session hook. | One graph run/resume/status/readiness entrypoint; uses existing `open_checkpointer`, injected worker port, no unverified authority fallbacks. |
| `ops/cto/Dockerfile` | No CTO container build surface exists in current source tree. It must isolate the executive from Mac worker privileges. | Reproducible Python image capable of running the mock executive; no embedded host secrets or SDK worker. |
| `ops/cto/compose.yaml` | Initial Mac Docker pilot requires an explicit durable named volume and reproducible least-privilege mount/network envelope, neither currently declared for CTO. | Restart preserves checkpoint volume; no home directory, Docker socket, GitHub credential, host grant directory, or production host-side write mount. |
| `tests/workflows/test_cto_runtime.py` | Existing test fixtures prove generic checkpoint mechanics, not CTO-specific campaign, bootstrap failure, effect idempotency and reconciliation behavior. | Positive mock and negative cases for lost ACK, duplicate submit, restart, stale authority and false VERIFIED. |
| `environment/agents/adapters/claude-agent-sdk/host_bridge.py` (`?`) | Only if authenticated, durable cross-process ingress is demonstrably absent from all applicable current host owners; the existing SDK harness runs a task but has no proven `submit/observe/cancel` service. | Not admitted now. Must retain existing owner of SDK worker launch and validate exact contract, repo revision, identity and permission independently. |
| `workflows/dags/cto/__init__.py` (`?`) | Only if packaging/import tests show the CTO subdirectory needs an explicit package marker. | Not admitted by consistency/style alone. |

Other obvious-looking files are intentionally absent: `cto/scheduler.py`, `cto/memory.py`, `cto/publisher.py`, `cto/merge.py`, `cto/identity_registry.yaml`, `cto/coding_agent.py`, `cto/permissions.py`, a new worker-control database and a second contract schema. Their responsibility already has another owner or is not yet justified.

## 4. Service-native CTO bootstrap, precise order

1. **START / TRUST.** Load a deployment-provided, independently authenticated authority revision and exact governance source identity. Inspect currentness without silently changing the source checkout. No hardcoded current `.github` main assumptions or unverified self-issued pin.
2. **CANONICAL.** Consume the producer-verified applicable upstream projection and identity assertion using existing authority/projection owners. An already generated projection is not automatically current. CTO lacks canonical actor/surface admission on this pinned baseline: record `BLOCKED_IDENTITY`, not an ad hoc actor.
3. **OPERATING BINDINGS.** Bind the appropriate local operating-plane identity and verified capability profile from existing `environment/agents/*` after upstream admission. A role or registry key alone does not grant action authority.
4. **RUNTIME READINESS.** Verify explicitly required dependencies, durable checkpoint path, memory service/package, and available Mac host capability. Preserve separate per-capability statuses `READY`, `UNAVAILABLE`, `UNKNOWN`, `BLOCKED`; do not collapse partial readiness into an overall execution READY.
5. **RECOVER.** Load checkpoint by stable campaign/thread identity. Before re-dispatch, query host-side operation identity and external evidence. For unresolved outcomes, suspend consequential retry; a checkpoint cannot attest GitHub effect completion.
6. **HYDRATE.** Use existing MemoryService identity-bound operations and retrieve relevant context. Distinguish memory unavailability from empty records; no new long-term memory DB.
7. **ACCEPT CAMPAIGN.** Validate frozen objective, target, native contract, delegated authority and all mandatory actor and worktree bounds. A campaign pack is not authorization.
8. **DECIDE / DISPATCH.** In the safe first slice, use a test-injected mock host that cannot mutate files or GitHub. Real host dispatch remains disabled until native host ingress, grant verification, operation journal and negative tests prove all required conditions.
9. **OBSERVE / RECONCILE / CHECKPOINT.** Emit honest `MOCK_ONLY`, `BLOCKED`, `RUNNING`, or evidence-linked terminal outcomes. Independent validation alone may establish verified completion, never LangGraph or worker prose.
10. **REVALIDATE.** Material changes in canonical revision, grants, target HEAD, host environment, or external observation invalidate affected assumptions; reevaluate before consequential continuation.

**Claude worker bootstrap is unchanged:** the SDK host invocation loads project `CLAUDE.md`, `.claude/settings.json`, `.mcp.json`, and Claude Code's own session hooks. It retains Claude actor identity; CTO executive does not impersonate or replace it.

## 5. Durable interaction contract (not yet a source API)

The architectural host boundary is the narrow **`submit → observe → cancel`** operation lifecycle; no transport/protocol/service is selected or deployed by this filetree.

- `submit`: immutable operation ID + campaign, exact native contract identity and digest, repository and pinned baseline, verified CTO identity assertion, delegated grant/ref. Host independently checks the contract bytes, resource claims, executable permissions, scope, workspace, and idempotency key *before* recording acceptance or executing a process.
- `observe`: host-observed operation state and immutable evidence refs. `ACCEPTED` is durable host admission; `RUNNING` is observed process execution; `SUCCEEDED` is observed terminal worker result, **not independently VERIFIED**.
- `cancel`: authorized termination request; return cancellation/termination evidence and reconcile whether an effect occurred. A cancellation request alone is not a confirmed clean rollback.

A lost acknowledgment followed by the identical operation ID must return the same host operation without a second worker. A reused operation ID with conflicting digest/contract must fail. Duplicate messages must not create duplicate PRs or code effects. On restart the CTO observes first and does not blindly resubmit.

**Existing host root `autonomy/runtime/store.py` is the preferred potential journal owner** because it already uses durable SQLite transactions; `autonomy/adapters/cursor/host_bridge.py` demonstrates an adapter extension table in that same store. This is a *reuse candidate*, not verified authorization to treat the root store as an arbitrary CTO command bus. If applicability fails, stop and resolve the real owner before adding any new database.

Transport choice (**authenticated loopback vs restricted spool**) remains deliberately **UNRESOLVED**, as in the source architecture. This filetree does not invent a port, token, localhost trust assumption, named pipe, API schema, background daemon or Docker mount. The existing remote host cannot be called directly from inside Docker merely because the SDK source exists in the same repository.

## 6. Sequence, authority and acceptance gates

| Phase | Allowed current scope | Requires before advancing | Outcome |
|---|---|---|---|
| **F0 - Source/file tree** | This document only; no repository mutations. | Exact source-head evidence; bootstrap locked; existing owners/negative spaces mapped. | **Completed as document**, not accepted code. |
| **F1 - Mock CTO vertical slice** | New graph/executor and one CTO test file; existing checkpointer/schema consumed. | Source tree remains current; no real host effects; startup must report unadmitted identity accurately. | Graph checkpoint + one campaign / one simulated host operation with crash/restart/lost ACK proof. |
| **F2 - Docker pilot shell** | Only Dockerfile + Compose and precise runtime source index changes. | Reproducible image; named checkpoint volume; hard isolation from host home and grant credentials. | Container restarts and resumes same mock operation; still `MOCK_ONLY`. |
| **F3 - CTO identity + memory admission** | **Separate** authorized upstream `.github` actor/surface/projection admission; downstream operating bindings after. | Independent canonical source/projection receipts and memory identity/grant proofs. | Distinct CTO principal proven, no aliasing to Claude/Cursor. |
| **F4 - Governed host call** | Extend exact Claude SDK owner and, only if necessary, add one narrow host bridge; reuse root autonomy store if appropriate. | Transport selected with threat model; authenticated host request, durable idempotency, isolation from grant issuance; source contracts fixed. | One authorized Claude worker launched and observed on Mac. |
| **F5 - Evidence and recovery close** | CTO graph/host integration and smallest existing-suite tests. | Full negative matrix + restart/duplicate/changed-head independent evidence check; existing `make pr` route enforced for any authorized publication. | One genuine campaign closes only on independently verified obligations; no merge. |

Parallel work is admissible for source/negative-test design and Docker mock packaging **after** F1's stable executive interface; upstream identity admission can proceed separately from the mock-only slice. Real host invocation requires F3 and F4, and final E2E requires all predecessors.

## 7. Test obligations, carried by existing test owners

| Scenario | Expected result | Proposed owning test |
|---|---|---|
| Unadmitted CTO actor or surface | No real execution, status `BLOCKED_IDENTITY` | `tests/workflows/test_cto_runtime.py`; upstream identity tests after admission |
| Missing/unauthenticated canonical revision or stale projection | No execution, preserve Unknown/STALE | CTO runtime test plus existing projection verifier |
| Mock-only path with valid test contract | Deterministic `MOCK_ONLY`, never production READY | CTO runtime test |
| LangGraph restart | Same thread resumes from durable checkpoint | Existing `tests/workflows/test_langgraph_durable_resume.py` + CTO runtime test |
| Effect occurred but acknowledgment lost | Observe existing operation, never duplicate effect | CTO runtime test with journal-backed fake host |
| Same operation ID, different contract digest | Explicit conflict, no new worker | CTO runtime + host test if bridge added |
| Host process missing / deadline expired | UNKNOWN/FAILED with reconciled evidence, not invented success | Host bridge test if added |
| Wrong repo/branch/worktree or mismatched baseline SHA | Host denies before launch | Existing worktree/gate suites + bridge test |
| Invalid native coding contract schema | Deny; no translation to new shape | Existing coding contract validator + CTO runtime test |
| Host permission lacking or forged merge grant | Deny; no protected action | Existing `ops/autonomy` gate tests; host privilege separation negative proof |
| Memory unavailable or namespace denied | Typed degraded/unauthorized state, no fake empty memory | Existing memory integration/identity suites |
| Worker returned SUCCEEDED but acceptance proof missing | Remain UNVERIFIED | CTO runtime/evidence test |
| Docker restarts while in-flight | Reconcile host operation first | Container E2E after F2 and F4 |

**Actual test execution:** NOT PERFORMED in this filetree phase. These are required proofs, not green receipts.

## 8. Repository access and mutation boundary for a later coding delegation

```yaml
repository_access:
  writable:
    - https://github.com/Quantum-L9/Cursor-Governance
  read_only:
    - https://github.com/Quantum-L9/.github
    - https://github.com/Quantum-L9/l9-graphiti-memory
  unlisted_repositories: no_access
```

This describes **F1/F2 only**, not permission to mutate .github for F3. Any upstream admission is a separate expressly authorized campaign with a different writable target. Future implementation should pin fresh immutable heads and preserve the accepted bootstrap and architectural boundaries. No merge, deploy or publication grant is conveyed by this filetree.

## 9. Important evidence/consistency notes

1. **Stale design assertion corrected.** `Cto!!!(1).md` says `environment/agents/agent_registry.yaml` contains `l-cto`. At current pinned CG HEAD, it **does not**. The `ops/memory/agent_identity.py` `l-cto` symbol is a reserved not-wired adapter identity, not an admitted actor or an active operating-plane binding.
2. **Generated identity projection is not current upstream.** `generated/governance/canonical_identity.yaml` declares `.github` source revision `9b27869dd893fcd28f76f99c9184a90435542c76`, whereas the independently inspected `.github` baseline is `d4397e53f8f4c23458a80f87db9552463ad9e26f`. This alone does not prove the older projection is invalid for every historic use; it **cannot** certify current CTO admission. Refresh via the authoritative producer and verify receipts, never hand-edit generated text.
3. **SDK presence is not host readiness.** The source exists and is exercised by tests; the Mac's actual installed SDK, workspace trust, credentials, concurrent execution behavior and security isolation were not observed.
4. **LangGraph persistence is narrower than external idempotency.** The checkpoint helper and crash-resume test exist, but the accepted terminal result of an external GitHub/Claude operation must be observed and independently reconciled.
5. **Root autonomy is not Program Execution.** The October 6–7 current CG amendments forbid new dependencies on `environment/program-execution/`; root `autonomy/` survives with its own code but each integration seam still requires proof.
6. **Code does not self-admit canonical authority.** Existing structural validators and skill configuration do not establish CTO actor registration, delegated execution authority or worker readiness.

## 10. Source anchors (immutable)

- [Canonical actor registry](https://github.com/Quantum-L9/.github/blob/d4397e53f8f4c23458a80f87db9552463ad9e26f/semantics/actor_registry.yaml)
- [Canonical surface registry](https://github.com/Quantum-L9/.github/blob/d4397e53f8f4c23458a80f87db9552463ad9e26f/semantics/surface_registry.yaml)
- [Canonical identity model](https://github.com/Quantum-L9/.github/blob/d4397e53f8f4c23458a80f87db9552463ad9e26f/semantics/identity_model.yaml)
- [Current CG amendments, including PE eviction and human merge](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/AGENTS.md)
- [Current operating-plane agent registry](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/agent_registry.yaml)
- [Current peer runtime bindings](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/PEER_RUNTIME_BINDINGS.yaml)
- [Current generated identity projection](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/generated/governance/canonical_identity.yaml)
- [Claude Agent SDK actual launcher](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/adapters/claude-agent-sdk/l9_agent.py)
- [Claude SDK environment validator](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/adapters/claude-agent-sdk/validate_agent_sdk_env.py)
- [Existing root autonomy store](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/autonomy/runtime/store.py)
- [Native Cursor host admission precedent](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/autonomy/adapters/cursor/host_bridge.py)
- [Existing LangGraph checkpointer](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/workflows/dags/_runtime/durable_checkpointer.py)
- [LangGraph two-instance recovery fixture](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/tests/workflows/test_langgraph_durable_resume.py)
- [LangGraph runtime authoring law](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/skills/l9-dag-authoring/references/langgraph-runtime-contract.md)
- [Native coding execution contract](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/skills/l9-coding-agent/contracts/EXECUTION_CONTRACT.yaml)
- [Pinned memory release/contract](https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/ops/config/memory-binding.json)
- [Memory SDK](https://github.com/Quantum-L9/l9-graphiti-memory/blob/441b741e31a7bb5a57849e5b49b97465b1c7ee58/src/l9_graphite_memory/sdk.py)

## 11. Handoff acceptance

This filetree locks **where the CTO's new responsibilities belong** and **what must remain owned elsewhere**. First mutating milestone may be a bounded mock-only LangGraph slice after operator authorization; it is **not** live autonomous CTO admission. Source-base movement, missing identity, false-grant risk or an invalidated architectural premise blocks only the affected later stage and must be reported, not silently repaired by broadening the file tree.

**Next executable engineering target:** F1: implement `workflows/dags/cto/graph.py`, `executor.py`, and `tests/workflows/test_cto_runtime.py` with real LangGraph and an injected mock-only `HostExecutionPort`. Consume the existing coding schema and checkpointer unchanged. Prove mock crash/restart and lost-ACK non-duplication before considering Docker or real host effects.
