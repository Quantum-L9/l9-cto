Very little. I think we’ve made enough architectural decisions to start building.

We should resist turning this into another prolonged design exercise. The CTO’s mission, core stack, authority structure, execution path and reference workload are established.

What remains is mostly integration discovery and proof, not product design.

What’s already decided

Architecture baseline selected

Concern	Decision
Mission	Replace you as the day-to-day technical operator
Runtime	Python + LangGraph
Hosting	Docker on Mac initially
Source home	Cursor-Governance
Canonical authority	.github
Identity	Upstream-derived bootstrap; no hardcoding
Memory	Existing L9 Graphiti Memory, private and shared
Coding execution	l9-coding-agent preferred
Program Execution	Unproven; not a dependency
First workload	Branch Consolidation campaign pack
Development discipline	CO-Pilot with independent architecture challenge

Only five integration questions remain

These should be resolved from actual source and runtime evidence—not by sending more architectural preferences back to you.

Question	What must be established
1. Bootstrap	How does the CTO obtain its valid upstream identity, governance context and standing operational delegation? Is a new canonical identity registration needed?
2. Execution interface	What’s the smallest reliable, governed interface from Docker to the existing l9-coding-agent on the host?
3. Recovery	How do LangGraph checkpoints correlate with real external operations so a restart never blindly repeats a consequential effect?
4. Memory integration	How does the resolved CTO principal access private and shared MemoryService namespaces using existing APIs and policies?
5. Admission and proof	Which existing owner admits the CTO integration, and how do we independently prove host isolation, execution effects and campaign completion?

These are meaningful engineering questions. None requires us to reconsider LangGraph, introduce another orchestrator or redesign memory.

Things I would deliberately defer

* Telegram versus another operator interface. Start with the smallest functioning campaign intake.
* DeepSeek versus another reasoning model. Keep the model adapter configurable.
* PostgreSQL versus SQLite for initial checkpoints. Choose from actual concurrency and reliability needs.
* Five-worker parallel orchestration. First prove one correctly supervised coding-agent execution.
* An always-on cloud host, LangSmith platform, new scheduler or elaborate dashboard.

We can add them when they solve an observed problem.

The remaining plan

01

One bounded source reconnaissance

Inspect the current .github, Cursor-Governance and Graphiti Memory contracts. Identify exact reusable APIs, identity requirements, execution paths and minimal gaps.

02

One independent CO-Pilot architecture break-test

Challenge ownership, authorization, recovery, memory isolation and container-to-host execution. Resolve material findings before freezing the implementation contract.

03

One bounded Claude Code implementation campaign

Build a running LangGraph CTO in Docker that bootstraps correctly, accesses memory, receives a campaign pack, selects an authorized next action and invokes a verified control-plane capability.

04

One real end-to-end operator test

Give the CTO a bounded campaign, let it supervise l9-coding-agent, interrupt it mid-operation, restore it and independently verify that it finishes or stops for a legitimate grant.

What I would build first

Not the complete CTO.

A thin, real CTO vertical slice with all the foundational boundaries present:

Verified bootstrap → LangGraph → MemoryService → Campaign intake → CTO decision → Governed coding-agent invocation → Evidence → Checkpoint → Resume

The first version can operate just one campaign and one worker. That’s enough to validate the architecture while keeping the implementation small.

My conclusion

We are past the point where additional general architecture planning is likely to pay off.

The only design work I would insist on before code is the bounded source-owner resolution and CO-Pilot adversarial break-test. Those protect us from accidentally creating a parallel execution plane or weakening existing authority.

After that, the next deliverable should be a CTO that actually runs, not another proposal.

The principle from here should be: prove the smallest working operator, then expand its delegated capability.


L9 CTO — Source-code microscope audit

October 14, 2026 · Source reconnaissance · Read-only

I’ve located the three public repositories behind the CTO architecture:

* Quantum-L9/.github⁠￼ — canonical semantic authority.
* Quantum-L9/Cursor-Governance⁠￼ — existing execution and governance runtime.
* Quantum-L9/l9-graphiti-memory⁠￼ — long-term memory subsystem.

The central architectural finding is already clear: the CTO should be a thin executive runtime over existing L9 capabilities, not another execution platform.

The live repositories confirm several important reuse boundaries, including canonical identity contracts, execution infrastructure, and a memory service with its own authorization and persistence architecture.

There is a verification limitation: GitHub’s publicly rendered files are accessible, but recursive directory listing, full repository cloning, and local tests are not available through this session’s tools. Consequently, this is a source-inspected, partial audit, not a complete commit-pinned code audit. I will distinguish confirmed paths from candidates requiring inspection rather than invent precision.

1. Critical findings that change the implementation plan

Program Execution is being retired, not integrated.

The October 6–7 amendments in Cursor-Governance/AGENTS.md explicitly identify Program Execution as an eviction target. The surviving autonomy, L4, publication and adapter paths must not depend on environment/program-execution/.

This strengthens CTO-004: do not build a CTO adapter around PE simply because the source directories still exist.

Merge requires a genuine human grant.

The October 12 amendment supersedes earlier instructions that treated /l9-pr-remediation as merge authorization.

The CTO may prepare PRs, supervise remediation, and reach MERGE_PENDING. It cannot authorize its own merge. Existing code paths include ops/autonomy/authorize_merge.py, merge_gate.py, and stack_safe_merge.py.

The coding-agent implementation contract already exists.

skills/l9-coding-agent/SKILL.md identifies the active implementation workflow, structured contract schema, validator, and execution-receipt schema.

We should map the CTO to those native contracts rather than inventing a competing CTOExecutionContract.

The memory system owns much more than storage.

MemoryService already defines authorization, canonical writes, operation identity, idempotency, receipts and projection handling. LangGraph should retain workflow checkpoints, not reproduce the memory subsystem’s lifecycle.

These are particularly important because some older repository instructions still describe PE as active or permit broader merge behavior. For this audit, the later explicit amendments take precedence.

2. Canonical identity: the CTO is not yet registered

I inspected these actual files in .github:

File	Finding
semantics/canonical_sources.yaml	Registers canonical identity and governance source coordinates
semantics/identity_model.yaml	Separates Actor, Runtime, Surface, Product and Release identities
semantics/actor_registry.yaml	Lists admitted human and agent actors
semantics/surface_registry.yaml	Lists admitted execution and interaction surfaces
semantics/identity_assertion.schema.yaml	Defines downstream identity assertions

The actor registry currently lists cursor, claude-code, codex, gemini, manus, and human. It does not list cto.

The surface registry likewise has no CTO-specific Docker surface.

Disposition: EXTEND upstream canonical identity, not NEW local identity.

This means the standalone CTO cannot simply boot as claude-code or invent a local cto identity and treat it as authorized. A narrowly scoped upstream admission is needed unless another current canonical binding legitimately covers the CTO’s intended identity.

Importantly, the actor registry itself grants no permissions. Operational delegation remains a separate, enforceable concern.

3. Coding-agent contract: exact files we can reuse

REPOSITORY: CURSOR-GOVERNANCE

skills/l9-coding-agent/

SKILL.md — entrypoint and execution lifecycle

runtime/BOOTSTRAP.yaml — lazy bootstrap router

contracts/EXECUTION_CONTRACT.yaml — execution contract semantics

schemas/execution-contract.schema.json — structured contract schema

scripts/validate_execution_contract.py — structural validator

contracts/VALIDATION_AND_EVIDENCE.yaml — validation obligations

contracts/CONVERGENCE.yaml — completion and convergence requirements

schemas/execution-receipt.schema.json — execution receipt schema

The source contract already specifies contract_id, objective, exact target, authority references, in/out scope, locked invariants, acceptance criteria, forbidden actions, validation obligations and delivery mode. It also supports explicit inspection and modification scopes.

I inspected the validator implementation as well. It checks the required structure, but does not independently establish that an authority reference is genuine or that the proposed effect is permitted. It also permits unknowns to be present with a warning.

Therefore the CTO should reuse this contract as its worker handoff, but the existing authorized execution boundary still needs to enforce actual permissions. Schema validation alone is not an execution grant.

4. Existing autonomy runtime: important distinction between APIs and retired interfaces

A direct code read uncovered a trap that a directory-level audit would have missed.

autonomy/runtime/cli.py exists but deliberately disables the file-path CLI interface. Its current implementation raises an error directing consumers to use AutonomyRuntime APIs. We must not follow older README examples that recommend invoking the runtime CLI.

The actual source surfaces worth investigating are:

Exact path in Cursor-Governance	What the code provides	CTO disposition
autonomy/runtime/engine.py	AutonomyRuntime, the underlying runtime class	Inspect for reuse
autonomy/adapters/orchestrator.py	AdapterOrchestrator, connecting sessions and runtime	Inspect for reuse
autonomy/adapters/bridge.py	JsonLineBridge, typed JSON-line protocol	Reuse candidate, not yet proven
autonomy/runtime/claims.py	ClaimRegistry, path-overlap and exclusive-resource rules	Reuse existing rules
autonomy/runtime/store.py	Runtime state storage accessed by claims	Inspect for continuity ownership
autonomy/runtime/cli.py	Disabled CLI entrypoint	Do not integrate

The JSON-line bridge implements register, request_agent, acknowledge_agent, authorize_tool, heartbeat, submit_artifact, status and sweep. Its main() constructs an AutonomyRuntime and an AdapterOrchestrator.

The claims implementation already supports overlapping repository-relative paths, glob scopes, read/write conflicts and transactional enforcement. For example, a claim against src/** can conflict with a write inside src/. That is exactly the kind of capability we should not reimplement in LangGraph.

However, this older autonomy subsystem may overlap with the Program Execution functionality now targeted for removal. A callable interface does not prove it remains an admitted, production-supported controller.

Architectural conclusion: reuse existing safe primitives where viable, but do not make the new CTO depend on the retired runtime CLI or automatically revive the legacy orchestration controller.

5. Memory integration: existing production interfaces, not a new database

The repository is named l9-graphiti-memory, but the Python import path is l9_graphite_memory.

These are the relevant implementation files:

Exact path	Code responsibility
src/l9_graphite_memory/sdk.py	MemorySDK, typed per-principal interface
src/l9_graphite_memory/services/memory_service.py	Canonical memory read/write/admission engine
src/l9_graphite_memory/server.py	Remote MCP server and principal resolution
src/l9_graphite_memory/authz/	Namespace authorization implementation
src/l9_graphite_memory/contracts/	Typed requests and receipts

In sdk.py, the CTO can consume existing operations such as search, hydrate, write, write_governed, health, lineage, and graph capability reporting. The service enforces namespace policy on writes, tracks explicit idempotency keys, and commits records with receipts and projection intents.

More importantly, Cursor-Governance already has an integration layer:

Exact path in Cursor-Governance	Purpose
ops/config/memory-binding.json	Pins the expected memory implementation
ops/memory/runtime_binding.py	Validates actual installed runtime against the binding
ops/memory/namespace_context.py	Resolves repository-aware namespace context
ops/memory/run_memory_mcp.sh	Launches the existing memory MCP interface
environment/agents/adapters/claude-code/memory/memory_bridge.py	Existing Claude-side memory transport

The binding references memory package version 2.6.0, with source commit 846f283f7dade101b324b87008ab4f5901f97074. This is one genuinely pinned dependency found in the source; it does not pin the entire CTO architecture.

Disposition: REUSE. The CTO needs a consumer adapter that uses the approved memory transport and a legitimately resolved CTO principal. It does not need a second Graphiti instance, a new memory API, or a parallel namespace policy.

The key distinction is that memory idempotency protects memory writes. It does not make Git operations, worker launches or deployment retries idempotent.

6. CTO identity already has a placeholder—but not an active admission

A deeper read found something the upstream registry alone did not reveal.

Cursor-Governance/environment/agents/agent_registry.yaml already contains an l-cto entry:

* Principal: l-cto-memory-client
* Role: observer
* Assigned namespaces: none
* Adapter: none
* Status: planned

ops/memory/agent_identity.py also recognizes l-cto as a reserved adapter identity.

This is useful reuse, but it is not permission to activate the new CTO. The upstream .github/semantics/actor_registry.yaml does not contain a canonical l-cto actor. It also explicitly states that identity registration does not assign operational authority.

There is a second important detail: the current memory identity resolver accepts an adapter-provided L9_MEMORY_AGENT_ID for recognized non-Cursor/non-Claude agents. It does not, by itself, cryptographically prove that the requesting process is a legitimate CTO.

Therefore the integration should extend the existing identity and memory-binding owners with authenticated runtime evidence, rather than merely setting L9_MEMORY_AGENT_ID=l-cto.

Disposition: EXTEND existing l-cto placeholder and upstream identity authority. Do not invent another CTO name, but do not treat the placeholder as admitted.

7. Existing host-side Git and publication machinery

The actual code already provides much of the CTO’s intended execution environment.

Exact path in Cursor-Governance	Existing operation
ops/scripts/agent_worktree_start.sh	Creates a dedicated agent branch/worktree from a fetched, pinned base
ops/scripts/resolve_stack_tip.py	Resolves permitted stacked-PR ancestry
ops/autonomy/l4_local.py	Local execution/release authorization
ops/scripts/run_pr_gate.sh	Existing publication validation path
ops/scripts/open_pr_after_gate.sh	Pushes and opens/reuses a PR after its gates
ops/autonomy/merge_gate.py	Rejects unauthorized merge effects
ops/autonomy/authorize_merge.py	Issues one human-approved, head-specific merge grant
ops/autonomy/stack_safe_merge.py	Verifies live head/grant and performs approved stack-safe merge

agent_worktree_start.sh already validates task identifiers, distinguishes default origin/main work from explicitly authorized non-main ancestry, and records task metadata for publication. There is no justification for writing CTO-specific worktree lifecycle logic.

open_pr_after_gate.sh also refreshes the remote base before publication and fails when that base cannot be verified. That belongs to the existing publisher, not LangGraph.

Security finding: interactive approval is not equivalent to host isolation

authorize_merge.py candidly documents a remaining limitation: its controlling-terminal challenge demonstrates interaction, but a worker running under the same operating-system account could deliberately forge it.

For the Docker CTO, this means the worker’s host execution permissions must exclude the ability to issue grants, modify grant records, or bypass the protected publication boundary. Merely instructing the model not to merge is insufficient.

8. The real missing integration: launching and supervising the coding worker

This is the most important unresolved engineering question.

The existing components cover substantial parts of the lifecycle, but they do not yet establish a single verified, callable path from the standalone CTO into a governed Claude Code execution session.

The distinction matters:

* skills/l9-coding-agent/ defines the coding agent’s operating contracts and lifecycle.
* environment/agents/adapters/claude-code/ projects governance, skills, session bootstrap and memory integration into Claude Code.
* autonomy/adapters/orchestrator.py can issue leases, render agent contracts, acknowledge capabilities and accept results.
* autonomy/adapters/bridge.py exposes those runtime operations through a JSON-line protocol.

However, the inspected AdapterOrchestrator.request_agent() returns a deployment description, lease and agent contract. It does not itself launch a Claude Code process. Nor does it prove that the existing autonomy controller is the correct supported integration for the new CTO.

That identifies the precise remaining discovery task: locate or prove an existing host-side governed worker launcher that accepts a validated native coding contract, establishes the correct Claude runtime, and returns a durable operation identity and evidence.

If that interface already exists, the CTO must consume it.

If it does not, the justified new code is a thin host-side execution adapter, not another worker framework, scheduler or coding agent.

9. One more substantial reuse discovery: canonical binding verification

The coding agent already has:

skills/l9-coding-agent/scripts/verify_canonical_binding.py

This is a substantial verifier, not merely a configuration checker. It requires an independently supplied upstream revision pin, checks the .github repository origin, rejects dirty semantic source trees, reads pinned Git objects, recomputes object hashes, and validates the producer’s projection artifact and compiler receipt. It returns typed BOUND, REJECTED, BLOCKED or STALE outcomes.

Reuse this existing invariant-binding verifier. Do not make the CTO fetch moving main YAML files and construct its own interpretation of canonical doctrine.

Its limit is equally important: it verifies the referenced invariant projection, not the independent authenticity of the supplied pin, the CTO’s actor admission, or an operational permission grant. Those remain separate boundaries.

10. Minimal proposed implementation map

Based on the inspected sources, the first CTO implementation should be mapped as follows.

Responsibility	Proposed implementation	Disposition
Executive reasoning	Small Python/LangGraph application within Cursor-Governance; exact directory not yet admitted	NEW
Identity admission	.github/semantics/actor_registry.yaml and surface_registry.yaml, following canonical admission	EXTEND
Existing CTO identity placeholder	environment/agents/agent_registry.yaml, ops/memory/agent_identity.py	EXTEND
Canonical invariant verification	skills/l9-coding-agent/scripts/verify_canonical_binding.py	REUSE
Coding task handoff	skills/l9-coding-agent/schemas/execution-contract.schema.json and validator	REUSE
Coding result format	skills/l9-coding-agent/schemas/execution-receipt.schema.json	REUSE
Worktree creation	ops/scripts/agent_worktree_start.sh	REUSE
Worker launch and observation	Locate existing governed Claude launcher; add narrow adapter only if missing	VERIFY / EXTEND
Worker resource claims	autonomy/runtime/claims.py, if current ownership permits	REUSE CANDIDATE
Executive persistence	LangGraph checkpoints with references to observed external effects	NEW, BOUNDED
Memory client	ops/memory/control_plane_client.py and existing binding machinery	REUSE
Memory authority	Existing MemoryService and namespace authorization	REUSE
PR publication	Existing L4 and make pr path	REUSE
Merge authorization	Existing human grant and merge gates	REUSE UNCHANGED
Legacy Program Execution	environment/program-execution/	DO NOT DEPEND ON

There is one nuance in the memory row: ops/memory/control_plane_client.py is already a properly bounded client. It delegates to the memory-owned CLI, validates the bound release’s receipt schema, and distinguishes unavailable memory, authorization denial, invalid receipts and idempotency conflicts. The CTO should use that existing behavior rather than introduce its own error taxonomy.

Required proof before coding against these paths

Remaining source and runtime verification

Capture exact commit SHAs for .github and Cursor-Governance.

Trace the actual Claude worker launch path from caller to process and result receipt.

Prove which root autonomy APIs remain supported independently of Program Execution.

Confirm the correct host-side authorization boundary and process/account isolation.

Resolve the l-cto placeholder into valid upstream identity and memory grants.

Run the existing contract, identity, memory and publication regression tests.

The existing test surfaces include tests/ops/memory/test_agent_identity.py, tests/ops/memory/test_cross_repo_lifecycle.py, and skills/l9-coding-agent/tests/test_coding_agent_canonical_binding.py. They provide concrete starting points for verification rather than a new test framework.

11. Audit verdict and next coding boundary

Source inspected · Not runtime verifiedRead-only

What is confirmed: L9 already has native coding contracts, canonical-binding verification, worktree creation, local release controls, PR publication, protected merge gates, a functioning memory API implementation, memory integration bindings, and source implementations for resource claims and execution receipts.

What remains unproven: the supported direct CTO-to-Claude host worker invocation, present-day runtime conformance of the legacy autonomy interfaces, operational admission of l-cto, deployment-level memory readiness, and exact revision consistency across the inspected repositories.

Because the publicly retrieved repository files were not all pinned to immutable SHAs, and I could not clone the repositories or run the code in this session, I would not yet call this an independently reproducible code audit.

The first implementation contract should therefore be constrained to two deliverables:

* Finish the exact-revision worker-launch trace and determine the minimal callable host interface using the existing coding agent.
* Build the small LangGraph executive loop against those proven interfaces, with a mocked execution boundary until real identity and effect grants are established.

No new generic executor, memory service, campaign controller, permission system, worktree manager or publisher should be authorized.

The main result of this microscope read is a narrower engineering target than our original seven-contract discussion suggested: most of the CTO’s supporting mechanisms already have source owners. The new product is executive judgment and continuity; the key integration uncertainty is the actual worker-launch boundary.


L9 CTO — Worker launch boundary and first executive loop

CTO-01 · October 14, 2026 · Read-only source investigation

1. Worker-launch trace: findings

The existing L9 coding-agent contract and governance activation mechanisms are confirmed, but I have not verified a complete, revision-pinned host-side launch path. The GitHub source browser exposed the relevant files, but I could not retrieve an immutable HEAD SHA or recursively inspect and execute the full repository.

The most consequential distinction is between assigning a worker and launching one.

CTO executive

Proposed LangGraph application

Native coding contract

skills/l9-coding-agent/

Source verified

Host-side worker invocation

Exact live caller → launcher not yet verified

Integration gap

Claude Code runtime

Governance bootstrap, tool gates, worker results

Activation source identified

Evidence reconciliation

Exact external results, not worker claims

Verified existing interfaces

Source path in Cursor-Governance	Finding
skills/l9-coding-agent/SKILL.md	Defines coding execution, validation, convergence and receipt obligations
skills/l9-coding-agent/schemas/execution-contract.schema.json	Existing l9.coding-agent.execution-contract/v1 schema
skills/l9-coding-agent/scripts/validate_execution_contract.py	Existing contract structural validator
autonomy/adapters/orchestrator.py	AdapterOrchestrator.request_agent() selects a runnable action, issues a lease and returns a contract; does not start a Claude process
autonomy/adapters/bridge.py	Existing JSON-line adapter protocol, not a proven direct Claude launcher
autonomy/runtime/cli.py	Explicitly disabled runtime CLI; do not use as the CTO’s execution endpoint
environment/agents/adapters/claude-code/README.md	Documents CLI/Web/Mobile activation and existing governance/bootstrap mechanisms
ops/scripts/agent_worktree_start.sh	Existing governed worktree preparation

The request_agent() return includes a deployment description, lease, required acknowledgment and agent contract. There is no corresponding process spawn inside that method.

The native coding schema already requires an objective, exact target, scope, invariants, acceptance criteria, forbidden actions, validation obligations and authority references. The CTO should pass this existing contract through the correct owner—not translate it into a second coding-contract language.

Decision: Use l9-coding-agent as the preferred execution capability, but treat the host launch adapter as unproven until its actual call chain and effect gates are verified. Program Execution remains excluded from the critical path under the October 6–7 governance amendments.

2. Minimal callable host interface

The correct CTO-facing abstraction is smaller than a general-purpose agent platform.

It needs three operations:

Operation	Input	Result
submit	Stable operation ID, native contract reference and digest, exact repository SHA, resolved identity and delegation reference	Durable acknowledgment or explicit rejection
observe	Operation ID	Actual host-observed state and evidence references
cancel	Operation ID and valid authority	Cancellation request and eventual disposition

cancel is required for the eventual host adapter, but is deliberately absent from the first synchronous mock.

from dataclasses import dataclass
from typing import Literal, Protocol
@dataclass(frozen=True)
class ExecutionRequest:
    operation_id: str
    campaign_id: str
    contract_id: str
    contract_sha256: str
    repository: str
    base_revision: str
    identity_ref: str
    delegation_ref: str
@dataclass(frozen=True)
class ExecutionObservation:
    operation_id: str
    state: Literal[
        "UNKNOWN", "ACCEPTED", "RUNNING",
        "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    evidence_refs: tuple[str, ...]
class HostExecutionPort(Protocol):
    def submit(self, request: ExecutionRequest) -> str: ...
    def observe(self, operation_id: str) -> ExecutionObservation: ...

This is a proposed CTO-facing Python interface, not a claim that these classes already exist in Cursor-Governance.

For real execution, the host adapter must resolve contract_id and contract_sha256 to an immutable, host-controlled native contract, verify every authority reference, and pass that contract through the established coding-agent validation and runtime mechanisms. A Docker-supplied pathname must never be trusted as an arbitrary host filesystem capability.

Its implementation must also preserve the distinction between:

* ACCEPTED: the host durably recorded the request.
* RUNNING: the host observed a real worker.
* SUCCEEDED: the host observed the worker’s terminal result.
* VERIFIED: the required independent evidence and acceptance obligations were satisfied.

VERIFIED is not returned by this basic execution interface; that determination belongs to the appropriate evidence and acceptance owner.

Safe integration rule

Do not make autonomy/adapters/bridge.py the worker launcher. Its protocol exposes adapter registration, leases, acknowledgments, authorization, heartbeat, artifacts and status—not a direct launch_claude operation.

Likewise, do not bypass Claude’s native governance activation. The existing adapter documents skill projection, session-start bootstrap, local tool gates and memory readiness.

3. Implementation: minimal LangGraph CTO, mock-only

I have prepared a self-contained Python prototype below. It is deliberately limited to one campaign, one native contract, one simulated operation.

It uses:

* Real LangGraph state transitions.
* The existing coding-agent JSON Schema.
* A stable operation identity.
* A persistent SQLite-backed mock host journal.
* LangGraph SQLite checkpoints.
* Host observation after dispatch.
* Explicit MOCK_COMPLETE, never a false real-execution success.

The current LangGraph API supports StateGraph with a thread-identified checkpointer, and its SQLite saver supports durable local checkpoints for small synchronous deployments.

The code is supplied here rather than installed in Cursor-Governance: this session has source-browsing access but no repository filesystem or shell execution capability. I cannot truthfully claim a commit, test run or Docker deployment.

File: cto_poc.py

"""L9 CTO proof of concept: LangGraph + mock-only execution.
No Claude imports, shell access, network requests, Git mutation,
authorization grants, or real worker launch.
"""
import argparse
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from typing import Any, TypedDict
from jsonschema import Draft202012Validator
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
def digest(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()
class CTOState(TypedDict, total=False):
    campaign_id: str
    source_sha: str
    contract: dict[str, Any]
    mode: str
    operation_id: str
    request_digest: str
    outcome: str
    reason: str
    evidence: dict[str, Any]
class MockHost:
    """Persistent simulated effect owner, separate from checkpoints."""
    def __init__(
        self,
        db_path: str | Path,
        drop_first_ack: bool = False,
    ):
        self.db_path = str(db_path)
        self.drop_first_ack = drop_first_ack
        with sqlite3.connect(self.db_path) as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS operations (
                    operation_id TEXT PRIMARY KEY,
                    request_digest TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            """)
    def submit(
        self, operation_id: str, request_digest: str
    ) -> dict[str, str]:
        # Only mock operations exist. This method never launches code.
        with sqlite3.connect(self.db_path, timeout=30) as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                """SELECT request_digest FROM operations
                   WHERE operation_id = ?""",
                (operation_id,),
            ).fetchone()
            if row is not None:
                if row[0] != request_digest:
                    raise ValueError("OPERATION_ID_CONFLICT")
            else:
                db.execute(
                    """INSERT INTO operations VALUES (?, ?, ?)""",
                    (operation_id, request_digest, "MOCK_DONE"),
                )
        # Simulate an effect committed with the acknowledgment lost.
        if self.drop_first_ack:
            self.drop_first_ack = False
            raise ConnectionError("SIMULATED_LOST_ACK")
        return {
            "operation_id": operation_id,
            "state": "ACCEPTED",
        }
    def observe(self, operation_id: str) -> dict[str, str]:
        with sqlite3.connect(self.db_path) as db:
            row = db.execute(
                """SELECT request_digest, status
                   FROM operations WHERE operation_id = ?""",
                (operation_id,),
            ).fetchone()
        if row is None:
            return {
                "operation_id": operation_id,
                "status": "UNKNOWN",
            }
        return {
            "operation_id": operation_id,
            "request_digest": row[0],
            "status": row[1],
            "evidence_kind": "SIMULATED_ONLY",
        }
    def operation_count(self) -> int:
        with sqlite3.connect(self.db_path) as db:
            return db.execute(
                "SELECT COUNT(*) FROM operations"
            ).fetchone()[0]
def build_graph(
    host: MockHost,
    coding_contract_schema: dict[str, Any],
):
    validator = Draft202012Validator(coding_contract_schema)
    def intake(state: CTOState) -> dict:
        if state.get("mode") != "mock_only":
            return {
                "outcome": "BLOCKED",
                "reason": "REAL_EXECUTION_NOT_ENABLED",
            }
        sha = state.get("source_sha", "")
        if not re.fullmatch(r"[0-9a-f]{40}", sha):
            return {
                "outcome": "BLOCKED",
                "reason": "INVALID_SOURCE_REVISION",
            }
        contract = state.get("contract", {})
        errors = list(validator.iter_errors(contract))
        if errors:
            return {
                "outcome": "BLOCKED",
                "reason": "NATIVE_CONTRACT_SCHEMA_INVALID",
            }
        if contract["target"].get("base_revision") != sha:
            return {
                "outcome": "BLOCKED",
                "reason": "CONTRACT_REVISION_MISMATCH",
            }
        if not state.get("campaign_id"):
            return {
                "outcome": "BLOCKED",
                "reason": "MISSING_CAMPAIGN",
            }
        return {"outcome": "INTAKE_READY", "reason": ""}
    def route_after_intake(state: CTOState) -> str:
        return (
            "stop" if state.get("outcome") == "BLOCKED"
            else "decide"
        )
    def decide(state: CTOState) -> dict:
        # Deterministic executive decision for the mock vertical slice.
        # A real reasoning adapter is deliberately not installed.
        contract = state["contract"]
        request = {
            "campaign_id": state["campaign_id"],
            "contract_id": contract["contract_id"],
            "contract_digest": digest(contract),
            "source_sha": state["source_sha"],
            "mode": "mock_only",
        }
        fingerprint = digest(request)
        return {
            "operation_id": f"mock-{fingerprint}",
            "request_digest": fingerprint,
            "outcome": "MOCK_SELECTED",
        }
    def act(state: CTOState) -> dict:
        acknowledgment = host.submit(
            state["operation_id"],
            state["request_digest"],
        )
        return {
            "outcome": "MOCK_ACCEPTED",
            "evidence": {"acknowledgment": acknowledgment},
        }
    def reconcile(state: CTOState) -> dict:
        observation = host.observe(state["operation_id"])
        if observation.get("status") != "MOCK_DONE":
            return {
                "outcome": "BLOCKED",
                "reason": "EXTERNAL_OPERATION_UNRESOLVED",
                "evidence": observation,
            }
        if (
            observation.get("request_digest")
            != state["request_digest"]
        ):
            return {
                "outcome": "BLOCKED",
                "reason": "EFFECT_IDENTITY_MISMATCH",
                "evidence": observation,
            }
        return {
            "outcome": "MOCK_COMPLETE",
            "reason": "",
            "evidence": observation,
        }
    graph = StateGraph(CTOState)
    graph.add_node("intake", intake)
    graph.add_node("decide", decide)
    graph.add_node("act", act)
    graph.add_node("reconcile", reconcile)
    graph.add_edge(START, "intake")
    graph.add_conditional_edges(
        "intake",
        route_after_intake,
        {"stop": END, "decide": "decide"},
    )
    graph.add_edge("decide", "act")
    graph.add_edge("act", "reconcile")
    graph.add_edge("reconcile", END)
    return graph
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument(
        "--checkpoints", default="cto-checkpoints.sqlite"
    )
    parser.add_argument(
        "--host-journal", default="cto-mock-host.sqlite"
    )
    args = parser.parse_args()
    contract = json.loads(args.contract.read_text())
    schema = json.loads(args.schema.read_text())
    host = MockHost(args.host_journal)
    initial: CTOState = {
        "campaign_id": args.campaign,
        "source_sha": args.source_sha,
        "contract": contract,
        "mode": "mock_only",
    }
    # One stable LangGraph thread per campaign.
    config = {
        "configurable": {
            "thread_id": f"cto:{args.campaign}"
        }
    }
    with SqliteSaver.from_conn_string(
        args.checkpoints
    ) as saver:
        graph = build_graph(host, schema).compile(
            checkpointer=saver
        )
        result = graph.invoke(initial, config)
        print(json.dumps(result, indent=2, sort_keys=True))
if __name__ == "__main__":
    main()

The SQLite mock journal and LangGraph checkpoints intentionally have separate ownership. This makes the failure case realistic: the mock effect can exist even when the graph did not receive an acknowledgment.

The mock’s submit() is idempotent for a matching operation ID and request digest. That is a property of this mock, not a guarantee about Claude Code, GitHub or the eventual host adapter.

4. Tests: rejection, idempotency and lost acknowledgments

The following tests use the existing coding-agent schema in the Cursor-Governance checkout. They do not need Docker, Claude credentials, upstream identity admission or network access.

File: test_cto_poc.py

import json
from pathlib import Path
import pytest
from langgraph.checkpoint.sqlite import SqliteSaver
from cto_poc import MockHost, build_graph
SHA = "a" * 40  # Synthetic revision for mock tests only.
SCHEMA_PATH = Path(
    "skills/l9-coding-agent/schemas/"
    "execution-contract.schema.json"
)
def contract():
    return {
        "contract_id": "CTO-MOCK-001",
        "objective": "Exercise a mock-only CTO decision cycle",
        "target": {
            "repository_or_artifact": "Quantum-L9/Cursor-Governance",
            "base_revision": SHA,
        },
        "authority_refs": [],
        "in_scope": ["mock-only processing"],
        "out_of_scope": ["repository mutation"],
        "locked_invariants": ["no real execution"],
        "acceptance_criteria": ["mock reconciliation succeeds"],
        "forbidden_actions": ["push", "merge", "deploy"],
        "validation_obligations": ["inspect simulated receipt"],
        "delivery_mode": "mock_only",
    }
def make_state(mode="mock_only", source_sha=SHA):
    return {
        "campaign_id": "mock-campaign",
        "source_sha": source_sha,
        "contract": contract(),
        "mode": mode,
    }
def make_graph(host, checkpointer):
    schema = json.loads(SCHEMA_PATH.read_text())
    return build_graph(host, schema).compile(
        checkpointer=checkpointer
    )
def test_mock_completes_without_real_execution(tmp_path):
    host = MockHost(tmp_path / "host.sqlite")
    config = {"configurable": {"thread_id": "test-1"}}
    with SqliteSaver.from_conn_string(
        str(tmp_path / "checkpoint.sqlite")
    ) as saver:
        graph = make_graph(host, saver)
        result = graph.invoke(make_state(), config)
    assert result["outcome"] == "MOCK_COMPLETE"
    assert result["evidence"]["evidence_kind"] == "SIMULATED_ONLY"
    assert host.operation_count() == 1
def test_real_execution_is_blocked(tmp_path):
    host = MockHost(tmp_path / "host.sqlite")
    config = {"configurable": {"thread_id": "test-2"}}
    with SqliteSaver.from_conn_string(
        str(tmp_path / "checkpoint.sqlite")
    ) as saver:
        graph = make_graph(host, saver)
        result = graph.invoke(
            make_state(mode="real"),
            config,
        )
    assert result["outcome"] == "BLOCKED"
    assert result["reason"] == "REAL_EXECUTION_NOT_ENABLED"
    assert host.operation_count() == 0
def test_wrong_revision_is_blocked(tmp_path):
    host = MockHost(tmp_path / "host.sqlite")
    config = {"configurable": {"thread_id": "test-3"}}
    with SqliteSaver.from_conn_string(
        str(tmp_path / "checkpoint.sqlite")
    ) as saver:
        graph = make_graph(host, saver)
        result = graph.invoke(
            make_state(source_sha="b" * 40),
            config,
        )
    assert result["outcome"] == "BLOCKED"
    assert result["reason"] == "CONTRACT_REVISION_MISMATCH"
    assert host.operation_count() == 0
def test_lost_ack_does_not_duplicate_effect(tmp_path):
    host_path = tmp_path / "host.sqlite"
    checkpoint_path = str(tmp_path / "checkpoint.sqlite")
    config = {"configurable": {"thread_id": "test-4"}}
    first_host = MockHost(
        host_path, drop_first_ack=True
    )
    with SqliteSaver.from_conn_string(
        checkpoint_path
    ) as saver:
        graph = make_graph(first_host, saver)
        with pytest.raises(
            ConnectionError, match="SIMULATED_LOST_ACK"
        ):
            graph.invoke(make_state(), config)
    # Simulate a completely new application process.
    recovered_host = MockHost(host_path)
    with SqliteSaver.from_conn_string(
        checkpoint_path
    ) as saver:
        recovered_graph = make_graph(recovered_host, saver)
        result = recovered_graph.invoke(None, config)
    assert result["outcome"] == "MOCK_COMPLETE"
    assert recovered_host.operation_count() == 1

These are proposed executable tests, not tests I have run. The last test specifically exercises a lost acknowledgment after a journal commit, followed by graph resumption. It should demonstrate one recorded mock operation rather than two.

5. Exact-revision trace: remaining verification

The missing SHA and actual host launcher must be determined on a complete checkout. The following read-only commands capture the starting revision and locate likely worker-launch implementations without modifying the repository.

set -euo pipefail
GOV="$HOME/.cursor-governance"
# Identify exact local and remote revisions.
git -C "$GOV" remote -v
git -C "$GOV" rev-parse --verify HEAD
git -C "$GOV" status --porcelain=v1
git -C "$GOV" ls-remote origin refs/heads/main
# Find actual Claude execution entrypoints and their callers.
rg -n --glob '*.py' --glob '*.sh' \
  'ClaudeSDKClient|ClaudeAgentOptions|claude_agent_sdk|claude -p|claude --print|subprocess\.(run|Popen)|asyncio\.create_subprocess|exec.*claude|launch.*agent' \
  "$GOV/autonomy" "$GOV/ops" "$GOV/environment" \
  "$GOV/skills/l9-coding-agent"
# Establish existing contract and governance consumers.
rg -n \
  'execution-contract.schema.json|validate_execution_contract|agent_worktree_start|session_start_claude_governance' \
  "$GOV/autonomy" "$GOV/ops" "$GOV/environment" \
  "$GOV/skills"

The results must identify the actual live call chain, including the code that starts the host process, how the Claude settings and hooks are loaded, how contract scope reaches that worker, and how its session identity and terminal receipt become observable.

A search hit or SDK import alone is insufficient. The call path must be followed through its current consumer and tests.

6. Running the mock prototype

The intended development commands, from a Cursor-Governance working directory with the two files above available, are:

uv pip install langgraph langgraph-checkpoint-sqlite jsonschema pytest
pytest -q test_cto_poc.py

For a manual invocation, create a fixture from contract() in the test file, with its target.base_revision set to the actual checked-out SHA, and invoke:

python cto_poc.py \
  --campaign CTO-MOCK-001 \
  --source-sha "$(git rev-parse HEAD)" \
  --contract mock-contract.json \
  --schema skills/l9-coding-agent/schemas/execution-contract.schema.json

This prototype belongs in an isolated development workspace until the proper Cursor-Governance source owner accepts its placement. The SQLite paths are development-only; production durability, locking, storage isolation and retention require separate proof.

7. Delivery status

Deliverable	Current result
Existing native coding-contract discovery	Source verified
Autonomy lease-versus-launch distinction	Source verified
Claude activation and governance entrypoints	Source identified
Actual host launcher and caller chain	Unresolved
Immutable current repository SHA	Unresolved
Minimal CTO-facing host interface	Proposed
LangGraph mock executive implementation	Source supplied
Mock regression tests	Source supplied, not executed
Repository commit or Docker deployment	Not performed

The next meaningful engineering action is no longer general architecture design. It is to execute the exact-revision trace against the local Cursor-Governance checkout, bind the proposed host port to the genuinely supported coding-agent launcher, and run the four mock tests.

Until then, the first LangGraph implementation can be developed and tested safely, but a real worker invocation must remain disabled.

This preserves the CTO architecture we agreed upon: LangGraph owns executive decisions and continuity; the existing coding agent owns implementation; host-side governance owns effect authorization; and independently verifiable evidence determines completion.

CTO execution result — October 14, 2026

I was able to inspect live source files in the public Cursor-Governance repository⁠￼, but I cannot access your Mac’s local checkout or execute Python, Git, or pytest in this session.

That means I cannot truthfully mark the exact-revision trace or four tests as passed, and I have not modified your repository.

What the source inspection confirms

Component	Verified finding
skills/l9-coding-agent/SKILL.md	Existing coding-agent contract and lifecycle
schemas/execution-contract.schema.json	Native structured coding contract
autonomy/adapters/orchestrator.py	request_agent() issues a lease and returns a worker contract, but does not launch Claude
autonomy/adapters/bridge.py	Provides JSON-line commands for adapter operations, not a Claude process launcher
environment/agents/adapters/claude-code/README.md	Existing Claude Code activation and governance integration

The native coding contract accepts the fields used by our proposed mock fixture, including target.base_revision, authority_refs, and delivery_mode. The JSON schema does not by itself prove permission to execute.

I also verified the exact request_agent() body: it selects a runnable action, issues a lease, records an agent_deployed receipt, and returns a deployment descriptor and contract. There is no actual Claude process launch inside that method.

Consequently, I would not bind the real CTO host port to that method. Doing so would confuse successful task assignment with successful worker execution.

What remains to execute locally

The previous cto_poc.py and test_cto_poc.py were supplied as code in the conversation; they have not been written into the checkout. No host adapter has been installed.

The repository documentation identifies ~/.cursor-governance/ as the normal Mac checkout location. It also identifies the existing Claude activation path, including hooks/session_start_claude_governance.sh, settings projection and tool gates. These must remain under the existing Claude adapter’s ownership.

Exact-revision reconnaissance command

Run this in your Mac terminal. It inspects the repository without modifying tracked files:

set -euo pipefail
GOV="$HOME/.cursor-governance"
test -d "$GOV/.git" || {
  echo "BLOCKED: Cursor-Governance checkout unavailable"
  exit 1
}
cd "$GOV"
SHA="$(git rev-parse --verify HEAD)"
echo "=== EXACT SOURCE ==="
printf 'HEAD: %s\n' "$SHA"
git remote -v
git status --short
git log -1 --format='%H %cI %s'
echo "=== WORKER-LAUNCH CANDIDATES ==="
rg -n -i \
  'ClaudeSDKClient|ClaudeAgentOptions|claude_agent_sdk|create_subprocess|subprocess\.|Popen\(|exec.*claude|launch.*worker|spawn.*agent' \
  autonomy ops environment skills/l9-coding-agent \
  -g '*.py' -g '*.sh' -g '*.ts' -g '*.js' \
  -g '!**/_archived/**' \
  || true
echo "=== NATIVE CONTRACT CONSUMERS ==="
rg -n \
  'validate_execution_contract|execution-contract.schema.json|execution-receipt.schema.json|agent_worktree_start' \
  autonomy ops environment skills tests \
  || true
echo "=== ACTIVE CLAUDE INTEGRATIONS ==="
rg -n \
  'session_start_claude_governance|local_execution_gate|merge_gate|claude_projection' \
  ops environment tests \
  || true
echo "=== PIN COMPLETE ==="
printf 'Audited local HEAD: %s\n' "$SHA"

That output is the evidence needed to follow the actual host-side call chain and decide whether the adapter can be reused or requires a narrow new implementation.

Once the two prototype files are placed in an isolated workspace with the correct native schema path, the four tests can be run with:

python -m pytest -v test_cto_poc.py

Their expected assertions are mock completion, real-execution denial, revision-mismatch denial, and no duplicate mock effect after a lost acknowledgment. All four currently remain unexecuted.

Current disposition

Live source inspection

Completed

Local HEAD pin and call-chain trace

Blocked by local access

Real launcher integration

Not authorized or implemented

Four mock tests

Not executed

The appropriate next execution environment is the Mac checkout, through a local coding agent or a ChatGPT Work session with access to that environment.

I would preserve the current mock-only boundary until the real launcher is identified and verified. This is the smallest safe path toward a running CTO without accidentally rebuilding or bypassing L9’s existing execution machinery.