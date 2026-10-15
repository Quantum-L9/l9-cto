# L9 CTO - Cursor-Governance Deep Environment Recon

Date: 2026-10-14
Mode: Read-only source reconnaissance. No code mutation, test execution, runtime deployment, merge, or publication.
Status: SOURCE-INSPECTED / HOST-RUNTIME-UNVERIFIED / FILETREE-NOT-YET-APPROVED

## Exact reference baselines

- Quantum-L9/.github: `d4397e53f8f4c23458a80f87db9552463ad9e26f`
- Quantum-L9/Cursor-Governance: `4cc0d7dc858021bc8e2a95a904e2945fd3d3acba`
- Quantum-L9/l9-graphiti-memory: `441b741e31a7bb5a57849e5b49b97465b1c7ee58`

All read-only GitHub repository queries used immutable commit refs for file content. GitHub metadata and tree inspection were successful. The separate execution container could not resolve github.com, so there is no verified local clone, Mac checkout census, installed-package proof, runtime test result, or external-effect receipt.

## Operator objective and frozen architectural direction

Develop an autonomous L9 technical executive inside the existing Cursor-Governance implementation home. Python/LangGraph in Mac Docker Desktop initially; memory through l9-graphiti-memory; canonical identity and semantic authority from .github; preferred code execution via existing l9-coding-agent and Claude execution machinery. No Igorbot/OpenClaw dependency, second execution plane, new memory owner, new publisher, or autonomous merge grant. One campaign and one worker first.

The user's order is recon, then source-grounded filetree, then code. This document completes bounded source inspection, not the filetree or an implementation grant.

## Proposed interaction path, with source-based availability classification

1. Principal submits a complete campaign and existing grants to the CTO application. NEW executive reasoning/intake is planned, not implemented.
2. CTO resolves current authority and actor/surface/runtime identity. `.github/semantics/identity_model.yaml` and both identity registries exist, but no admitted CTO actor or CTO Docker surface is present at the pinned revision. CTO-specific operational binding is also absent from current `environment/agents/agent_registry.yaml`. BLOCKED for real consequential CTO execution.
3. LangGraph makes bounded decisions and checkpoints campaign progress. Existing `workflows/dags/_runtime/durable_checkpointer.py` implements workspace SQLite `SqliteSaver`, and `tests/workflows/test_langgraph_durable_resume.py` contains a two-instance resume fixture. REUSE CANDIDATE for checkpoint mechanics only; not evidence of remote-effect idempotency or Docker durability.
4. CTO submits a verified native coding contract and exact target to a host-owned execution boundary. `skills/l9-coding-agent/` already owns a contract schema, a structural validator, canonical-binding verifier, and an execution-receipt schema. REUSE. Schema validity does not establish a grant.
5. Host prepares a dedicated task worktree using `ops/scripts/agent_worktree_start.sh` and wired worktree support. REUSE only after host permission and exact task/repo authority.
6. Host starts an actual Claude SDK session. `environment/agents/adapters/claude-agent-sdk/l9_agent.py` is a concrete launcher: `ClaudeSDKClient`, `setting_sources=['project']`, `cwd`, turn/budget bounds, `query`, `receive_response`, `ResultMessage`, report writing. REUSE/EXTEND CANDIDATE, not a finished CTO remote execution port.
7. Claude Code loads the target project's `CLAUDE.md`, `.claude/settings.json`, and `.mcp.json`. Project hooks and permission settings own governance; SDK harness explicitly avoids re-authoring them. Verified source-level binding; runtime activation not observed.
8. Claude accesses canonical memory through project MCP configuration, `ops/memory/run_memory_mcp.sh`, signed per-agent assertions, and the bound `l9-graphite-memory` 2.6.0 service. REUSE. CTO identity and namespace grants remain unbound.
9. Host validates tool effects via existing gates and publishes through the existing `make pr` path only when appropriately authorized. Human-head-specific merge authorization remains separate. REUSE; not delegated to the CTO here.
10. CTO observes host operation state and independently reconciles results before advancing. NOT IMPLEMENTED as a coherent durable CTO `submit/observe/cancel` API. The SDK harness writes one default `reports/agent_sdk/latest.json` report; it does not yet establish stable operation IDs, a durable accepted/running/terminal journal, trusted immutable per-operation receipts, recovery after lost acknowledgements, or an independently authenticated remote host API.

## Key source-backed findings

### R01 - A real SDK launcher already exists

Observed: `environment/agents/adapters/claude-agent-sdk/l9_agent.py` calls `ClaudeSDKClient`, sends a task, receives the result, and stores a structured report. `README.md` identifies supported permission modes and project-owned policy. The code takes a working-directory target from `L9_REPO` and requires project governance files. It defaults the report to one `latest.json` path. Unit tests exist under the adapter.

Implication: do not invent a new generic Claude runner. The CTO-facing host interface must be derived from this actual SDK path and its native governance, after validating its target-binding and asynchronous-operation requirements. The existing harness is synchronous task-oriented, not a demonstrated multi-operation host service.

### R02 - Autonomy lease assignment is not worker launch

Observed: `autonomy/adapters/orchestrator.py::request_agent` selects a ready action, issues a lease, and returns a deployment description and contract. `autonomy/adapters/bridge.py` exposes JSON-line registration, lease, authorization, heartbeat, artifact, status, and sweep commands. Neither launches a Claude process. `autonomy/runtime/cli.py` deliberately disables its file-path CLI. The root `autonomy/runtime/engine.py` composes scheduler, leases, claims, authorization gateway, artifact validator, receipt chain, and store.

Implication: distinguish existing useful claims/lease primitives from a proven SDK launch integration. Do not make the retired Program Execution tree a CTO prerequisite. Root autonomy remains a reuse candidate where actual current support is demonstrated.

### R03 - Program Execution is being evicted

Observed: the later append-only amendments in `AGENTS.md` dated October 6-7 expressly forbid surviving autonomy, L4, publication, readiness, and adapter mechanisms from depending on `environment/program-execution/`, and retire live campaign/program routing. Earlier documents still name it as active. Later applicable amendments take precedence.

Implication: no new CTO dependency on the old PE runtime or campaign controller. Existing root autonomy capabilities may be inspected and reused only if independent of the evicted tree.

### R04 - CTO identity has not been admitted

Observed: `.github/semantics/actor_registry.yaml` includes cursor, claude-code, codex, gemini, manus, and human, but no CTO. `.github/semantics/surface_registry.yaml` contains no CTO Docker surface. The current operating-plane `environment/agents/agent_registry.yaml` defines active cursor, Claude Code, Manus, Codex and Gemini bindings, and no CTO binding. `ops/memory/agent_identity.py` reserves `l-cto` as a not-yet-wired adapter identity.

Implication: existing placeholder names are not execution authority. CTO actor admission and a legitimate runtime/surface/credential/grant binding must be resolved at the upstream/local owners. Never impersonate Claude or Cursor as the executive actor. The downstream Claude worker retains its own canonical actor identity.

### R05 - Native contract validation is structural, not authorization

Observed: `skills/l9-coding-agent/schemas/execution-contract.schema.json` and `scripts/validate_execution_contract.py` check required keys, array shapes, non-empty criteria and obligations. They do not prove current GAR authority, authorize the target repository, authenticate a delegation, or validate a remote execution effect. At this CG revision `skills/l9-coding-agent/integrations/L9_RUNTIME_BINDING.yaml` is version 1.2.0 and references the cursor-governance-operating-plane profile. It is not identical to the installed ChatGPT Coding Agent's newer 1.5.4-chatgpt runtime.

Implication: the CTO must consume the actual repository-native contract but must not confuse schema PASS with permission. The exact canonical projection and active consumer requirements need separate current admission proof; do not transplant the ChatGPT-installed skill's behavior into the Claude host as an assumption.

### R06 - Host permission, not model wording, is the security boundary

Observed: `.claude/settings.json` configures SessionStart/Stop hooks and PreToolUse gates for merge, local execution and memory. `ops/autonomy/merge_gate.py` recognizes merge effects; `authorize_merge.py` requires a human, repo/PR/head-specific expiring grant. Its own documentation explains that controlling-terminal interaction is forgeable by a deliberately hostile worker under the same OS account.

Implication: a long-running CTO process and its worker must not inherit writable grant stores, the grant-maker route, host-wide credentials, or unchecked repository paths. A host execution boundary must validate authenticated identity, native contract digest, exact revision, scope, allowed effect and idempotent operation identity; model-supplied fields alone are not authority. A Docker mount or localhost request is not automatically a secure boundary.

### R07 - Durable LangGraph mechanics already have a shared owner

Observed: `workflows/dags/_runtime/durable_checkpointer.py` creates a `SqliteSaver` scoped to `workspace/.l9/langgraph/<dag>.sqlite`. GMP and intelligence-harvest executors consume it. `tests/workflows/test_langgraph_durable_resume.py` tests a second process resuming the same thread after interruption without replaying the completed graph node. `skills/l9-dag-authoring/references/langgraph-runtime-contract.md` distinguishes graph checkpointing from domain side-effect idempotency and memory.

Implication: first evaluate extending/consuming this small helper before writing CTO-specific persistence plumbing. The CTO owns its node semantics and external-effect reconciliation. A checkpoint can say what the graph last saw, not what GitHub or Claude actually did after the checkpoint.

### R08 - Memory is bound to 2.6.0, with per-principal MCP identity

Observed: `ops/config/memory-binding.json` pins package `l9-graphite-memory` 2.6.0, commit `846f283f7dade101b324b87008ab4f5901f97074` and wheel digest. Main `l9-graphiti-memory/pyproject.toml` also declares version 2.6.0 at the inspected head. `ops/memory/runtime_binding.py` authenticates the actual installed interpreter/package binding rather than taking PATH. `.mcp.json` configures the existing stdio `l9-graphite-memory` server. `run_memory_mcp.sh` resolves per-agent identity, checks signed door values and fails closed without them. Memory SDK and service already own search, hydrate, writes, lineage and namespace authorization.

Implication: no separate CTO memory store/ontology. An authenticated CTO-specific principal and grants remain to be admitted and tested; code presence and a declared wheel pin do not prove live installed or server readiness.

### R09 - Existing worktree and publication mechanisms are real source owners

Observed: `ops/scripts/agent_worktree_start.sh` fetches/pins the starting base, creates isolated wired worktrees and saves task metadata. `ops/scripts/open_pr_after_gate.sh` is the existing publication leg, including base refresh. Later `AGENTS.md` governance requires one human merge grant bound to the live head, with `stack_safe_merge.py` doing rechecks. These should not be reimplemented inside LangGraph.

Implication: CTO should request an authorized bounded operation from the host and consume actual worktree/PR/CI results; it should not execute raw, model-invented Git commands or become a publisher.

### R10 - The repository contains an old `/lcto` persona command

Observed: `commands/lcto.md` describes a chat persona that makes strategic architectural recommendations. It is not an autonomous LangGraph executive, host worker transport, agent identity, or implementation of the requested CTO. The current repository also contains a generated `filetree.md` projection, not an ownership authority. These names must not bias the CTO's source placement.

## Existing tests worth binding during implementation (not executed here)

- `environment/agents/adapters/claude-agent-sdk/tests/test_l9_agent.py`: SDK option surface, shadow-policy rejection, report shape, bounds, dependency/governance checks and mocked behavior.
- `tests/workflows/test_langgraph_durable_resume.py`: genuine two-instance SQLite checkpoint resume fixture.
- `tests/ops/memory/test_agent_identity.py`: memory author identity resolution.
- `tests/ops/memory/test_cross_repo_lifecycle.py`: bound memory 2.6.0 lifecycle proof at the owning repo configuration.
- `autonomy/tests/test_cursor_host_bridge.py` and `autonomy/tests/test_cursor_admission_binding.py`: existing host admission on the Cursor Task surface, NOT automatically a Claude SDK launcher.
- `skills/l9-coding-agent/scripts/validate_execution_contract.py`: native coding contract structural validation.

No tests were run in this recon. A passing source fixture is not a runtime result, and a previously recorded run is not current proof.

## Required filetree-phase decisions and acceptance

1. Choose the exact existing Cursor-Governance ownership directory for CTO executive logic based on current owner contracts. New files only where no existing owner can lawfully satisfy the obligation.
2. Bind a concrete host execution invocation path to `l9_agent.py` (or another independently verified existing launcher) with a request->durable acceptance->observe->cancel/reconcile contract, without a new generic worker framework.
3. Map CTO identity and surface registration to `.github` source owners; map operating-plane actor bindings and memory principal grants to the existing Cursor-Governance owners. Treat admission as a separate, upstream authorized change.
4. Map LangGraph CTO-specific nodes/state to their domain owner and reuse the shared `durable_checkpointer.py` mechanics if the container/runtime import and storage boundary permit.
5. Preserve the existing coding agent contract, Claude settings/hooks, worktree owner, memory service, publisher and human merge gate. List all read-only dependencies separately from authorized write surfaces.
6. Design test seams for false target, missing actor, forged grant, invalid contract digest, missing host launch, lost ACK, duplicate operation ID, restarted executor, changed PR head, memory principal denial and attempted merge. Existing native test suites should carry the smallest required new negative cases.
7. Only after source-grounded file placement is accepted should implementation begin. No Docker/Mac transport selection, separate daemon, writable grant access or live worker execution is admitted by this recon.

## Current blockers / Unknowns

- No authenticated, host-owned Docker-to-Mac CTO execution ingress has been demonstrated.
- No existing complete CTO submit/observe/cancel path and durable host action journal has been demonstrated.
- CTO actor, surface, operational delegation and private/shared memory grants are not admitted at current pinned .github/CG sources.
- Real Mac machine checkout, Claude SDK installation, workspace trust, secret availability, network policy, Docker mounts, native sandbox separation and live MCP health were not observed.
- End-to-end launch, credential isolation, lost-ack recovery, independent evidence acceptance, real campaign completion and publication handoff have not been executed.
- Installed ChatGPT Coding Agent skill version and current Cursor-Governance repository Coding Agent version are different. Use each only in its verified execution context.

## Recommended next transition

Proceed to the requested FILETREE phase: a minimal, revision-bound responsibility/file map within Cursor-Governance, with explicit REUSE / EXTEND / NEW / DEFER and provenance for every proposed file. Keep all repo mutations disabled until that filetree is reviewed and accepted.

## Primary immutable source links

- Authority registry: https://github.com/Quantum-L9/.github/blob/d4397e53f8f4c23458a80f87db9552463ad9e26f/semantics/actor_registry.yaml
- Surface registry: https://github.com/Quantum-L9/.github/blob/d4397e53f8f4c23458a80f87db9552463ad9e26f/semantics/surface_registry.yaml
- Identity model: https://github.com/Quantum-L9/.github/blob/d4397e53f8f4c23458a80f87db9552463ad9e26f/semantics/identity_model.yaml
- Governance amendments: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/AGENTS.md
- SDK launcher: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/adapters/claude-agent-sdk/l9_agent.py
- SDK validator: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/adapters/claude-agent-sdk/validate_agent_sdk_env.py
- Native coding contract: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/skills/l9-coding-agent/contracts/EXECUTION_CONTRACT.yaml
- Autonomy orchestrator: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/autonomy/adapters/orchestrator.py
- Autonomy bridge: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/autonomy/adapters/bridge.py
- LangGraph persistence helper: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/workflows/dags/_runtime/durable_checkpointer.py
- LangGraph resume test: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/tests/workflows/test_langgraph_durable_resume.py
- Memory pin: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/ops/config/memory-binding.json
- Local agent bindings: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/environment/agents/agent_registry.yaml
- Human merge grant: https://github.com/Quantum-L9/Cursor-Governance/blob/4cc0d7dc858021bc8e2a95a904e2945fd3d3acba/ops/autonomy/authorize_merge.py
