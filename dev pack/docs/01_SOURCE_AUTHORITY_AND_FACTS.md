# 01 | Revision-bound evidence, authority ownership and provenance

## 1.1 Baseline and method

Exact `main` heads observed through the GitHub connector on 2026-10-14:

| Repository | Exact SHA | Inspected responsibility |
|---|---|---|
| `Quantum-L9/.github` | `d4397e53f8f4c23458a80f87db9552463ad9e26f` | Identity model, actor/surface registries, source and projection catalogs |
| `Quantum-L9/Cursor-Governance` | `4cc0d7dc858021bc8e2a95a904e2945fd3d3acba` | Runtime mechanics, worker adapter, native governance, memory and publisher |
| `Quantum-L9/l9-graphiti-memory` | `441b741e31a7bb5a57849e5b49b97465b1c7ee58` | MemorySDK, MemoryService, signed agent identity, MCP server |

**Important qualification:** This is directly observed source from exact GitHub refs. It is **not** a producer-validated AuthorityResolution receipt, verified canonical compiler artifact, signed projection proof, live Mac checkout, or runtime PASS. A later code implementer must first rebase source reality to its exact contemporaneous head without silently reinterpreting these design commitments.

## 1.2 Source findings and operational implications

| Finding | Source coordinate | Observation | Consequence |
|---|---|---|---|
| A01 | `.github/semantics/actor_registry.yaml` | No `l-cto` actor entry at pinned head; identity registry grants no permissions | Upstream actor decision is prerequisite for live CTO actions |
| A02 | `.github/semantics/surface_registry.yaml` | No CTO Docker service surface entry; surface registration does not bind a worker/actor | Resolve canonical service surface at correct owner; never hardcode |
| A03 | `.github/semantics/identity_model.yaml` | Product, release, runtime, actor, surface distinct; identity assertion does not grant new authority | CTO bootstrap is a consumer of identity proof, separate from delegation |
| A04 | `Cursor-Governance/environment/agents/agent_registry.yaml` | No active CTO operating binding; role grant composition belongs to operating plane | Do not promote `l-cto` from local memory placeholder |
| A05 | `ops/memory/agent_identity.py` | `l-cto` is explicitly labeled reserved/not wired | Reference name is not identity admission |
| A06 | `environment/agents/adapters/claude-agent-sdk/l9_agent.py` | Real `ClaudeSDKClient` path, project settings, turn/budget limits, structured ResultMessage report | Reuse worker launcher but bridge/replay semantics not yet present |
| A07 | `environment/agents/adapters/claude-agent-sdk/validate_agent_sdk_env.py` | Forbids policy shadowing; checks SDK pin, settings and import availability | CTO must not pass independent tool allowlists or bypass project settings |
| A08 | `autonomy/adapters/orchestrator.py` + `autonomy/adapters/bridge.py` | Produces leases and deployment descriptors but does not prove Claude OS process spawn | A deployment descriptor is not a worker execution receipt |
| A09 | `autonomy/runtime/store.py` | SQLite WAL, explicit transactions; campaigns, actions, leases, claims, artifacts, receipts, decisions | Candidate for host operation journal after exact ownership check; not automatically an RPC host |
| A10 | `autonomy/adapters/cursor/host_bridge.py` | Example of adapter extension data inside existing root autonomy DB | Reuse precedent, not Cursor-only transport implementation |
| A11 | `workflows/dags/_runtime/durable_checkpointer.py` | Workspace `.l9/langgraph/<dag>.sqlite` backed by SqliteSaver | Reuse checkpoint mechanics via persistent Docker volume |
| A12 | `tests/workflows/test_langgraph_durable_resume.py` | Contains two-instance checkpoint restore fixture | Existing *test source* shows intended proof, but no test was executed here |
| A13 | `skills/l9-coding-agent/contracts/EXECUTION_CONTRACT.yaml` | Existing bounded task contract and scope/authority fields | Do not create a CTO coding contract schema |
| A14 | `skills/l9-coding-agent/scripts/validate_execution_contract.py` | Checks structural minimum only | A valid JSON shape is not an effect grant |
| A15 | `ops/config/memory-binding.json` | Pins l9-graphite-memory 2.6.0 at immutable memory revision | Reuse existing package, runtime binding and namespace policy |
| A16 | `ops/memory/run_memory_mcp.sh`, `agent_assertion.py`, `materialize_agent_authority.py` | Signed per-principal memory door and active-binding requirement | Explicit CTO principal and authorized namespaces needed |
| A17 | `.claude/settings.json`, `.mcp.json`, Claude SessionStart shell | Worker governance is project-owned and host/session activated | CTO service cannot simply invoke Claude bootstrap as its own |
| A18 | `ops/scripts/agent_worktree_start.sh` | Dedicated wired agent worktree with pinned fetched base and task metadata | Use existing host-side isolated worktree protocol |
| A19 | `ops/scripts/open_pr_after_gate.sh`, `make pr` machinery | Existing guarded publication path | No second publisher or raw GitHub write shortcut |
| A20 | `ops/autonomy/authorize_merge.py`, `stack_safe_merge.py`, `merge_gate.py` | Human exact-PR/head grant; grant terminal challenge has same-account isolation limitation | CTO/worker never hold grant issuer privileges; separate host accounts/trust |
| A21 | `AGENTS.md` Oct 6–7 amendments | Program Execution is eviction target; surviving runtime cannot import it | No PE or legacy program campaign dependency |
| A22 | `ops/scripts/emit_claude_readiness.py`, `write_runtime_readiness_receipt.py` | Existing read-time status, source SHA and age-sensitive readiness patterns | Reuse predicates/semantics where applicable; no parallel validator |
| A23 | `environment/agents/deployment/receipts.py` | Digest/source-manifest validation is Cursor deployment-specific | Do not label Cursor receipt as CTO admission |
| A24 | `autonomy/validation/doctor.py` | CLI explicitly disabled; directs callers to `AdapterConformance.run()` | Don't put a disabled doctor command in build plan |
| A25 | `pyproject.toml` | Python >= 3.12, LangGraph/sqlite saver already dependency; Claude SDK pinned optional extra | Reuse locked Python stack, keep worker SDK host-only |
| A26 | `commands/lcto.md` | Legacy conversation mode, no durable worker control path | Do not pass off persona command as CTO implementation |

## 1.3 Immutable source URLs

Replace `{CG}` with `https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba` and `{ORG}` with `https://github.com/Quantum-L9/.github/blob/d4397e53f8f4c23458a80f87db9552463ad9e26f`.

Key files: `{ORG}/semantics/{identity_model,actor_registry,surface_registry,canonical_sources,projection_profiles}.yaml`; `{CG}/environment/agents/adapters/claude-agent-sdk/{l9_agent.py,validate_agent_sdk_env.py}`; `{CG}/autonomy/runtime/{engine,store,claims,leases}.py`; `{CG}/autonomy/adapters/{orchestrator,bridge}.py`; `{CG}/workflows/dags/_runtime/durable_checkpointer.py`; `{CG}/ops/memory/{runtime_binding,agent_identity,materialize_agent_authority}.py`; `{CG}/skills/l9-coding-agent/contracts/EXECUTION_CONTRACT.yaml`.

Direct immutable URL example: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/adapters/claude-agent-sdk/l9_agent.py

## 1.4 Required stage-specific rechecks

At implementation intake: resolve upstream owner, local repository HEAD, correct base branch, PRs and a clean isolated worktree; re-read each source file being edited; validate that locked design remains realizable. At integration: verify Mac-installed SDK interpreter, actual trust settings, a signed and scope-bound CTO actor, real process isolation and available memory. At acceptance: capture actual environment, target commit, host operation journal, independent GitHub/CI evidence and restart receipts.

A changed source revision invalidates affected source-derived assumptions only; it does not authorize spontaneous architecture revision.

## 1.5 Fidelity limits

Original donor files are supplied intact in `sources/`; an independent, complete original chat transcript was not available. `Cto!!!(1).md` includes speculative sketches and mock-only code, not installed modules. The Branch Consolidation reference references contract directories not attached here. Do not certify full original conversation coverage, reviewed missing contract contents or target-specific production readiness. The local machine files are an implementation projection with documented statuses, never a fabricated canonical L9 ProductManifest or WorkflowSpec.

## v1.1 | Additional exact source inspections and external support

Earlier source baselines in this chapter are immutable **historical reconnaissance**, not evidence that a host is running. The following later inspected sources inform CTO-D019 through CTO-D024:

| Owner / immutable revision | File or provider | Source-proven fact |
|---|---|---|
| `.github@d4397e53f8f4c23458a80f87db9552463ad9e26f` | `semantics/actor_registry.yaml`, `semantics/surface_registry.yaml`, `semantics/identity_model.yaml` | Neither registry has a CTO actor/surface; identity is not authorization |
| `Cursor-Governance@0bb60d78f8bdc22d09bd8464830cdfa62d61d0ed` | `autonomy/runtime/{engine.py,capability_gateway.py,store.py,leases.py,receipts.py}` | Campaign scope, leases, claims, receipts and per-capability denial checks exist as source code |
| Same CG revision | `autonomy/adapters/{orchestrator.py,conformance.py,bridge.py,protocol.py}` | Existing adapter request, grant acknowledgment, tool mediation, receipt and conformant peer registry mechanisms; bridge is a JSON-line *stdin* adapter, not a secure remote API |
| Same CG revision | `autonomy/policies/{role-capabilities.json,adapter-requirements.json}` | `coordinator` is read/schedule-only; `executor`/`remediator` have bounded mutations; `pr.merge`, `pr.admin_merge`, `git.force_push` are globally forbidden by root policy; adapter must enforce mediation |
| Same CG revision | `environment/agents/{agent_registry.yaml,PEER_RUNTIME_BINDINGS.yaml}` | CTO is not bound; peers depend on root-autonomy-control-plane; memory role bindings are a separate concern |
| `SuperJackfruitLabs/agentpod@e647ab22722819a23329e40152ff442977046705` | `apps/node-agent/cmd/agentpod-node/registry.go` | Node-agent registers Claude Code, Codex and others; **no Cursor descriptor appears** in this exact registry |
| Same AgentPod revision | `docs/OPERATING.md` | Node `apn` and fleet/operator `fleet` are distinct; agent principals use Hub MCP; native station terminal is an **unconfined host-user shell**, and must not be exposed as CTO fallback |
| Official Cursor CLI documentation (external live page, date observed 2026-10-14) | https://prod.cursor.com/docs/cli/acp | `agent acp` exposes stdio JSON-RPC; sessions, updates, permissions, cancel. This is a supported Cursor CLI interface, **not** proof of AgentPod support or an IDE-chat control API |

No live Mac, Hub, APN, Cursor CLI, SDK canary, signed projection receipt, principal/grants, delegated authority, operation journal or production acceptance was observed. Source links remain revision-specific. This pack does not claim a produced/validated `l9.authority-resolution/v1` receipt: only bounded source inspection and an explicitly selected resolver integration approach are established.
