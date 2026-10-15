# 06 | MemoryService, host security and rights of action

## 6.1 Three independent persistence planes

| Plane | Purpose | Owner | What it must not prove |
|---|---|---|---|
| LangGraph checkpoint | Executive thread steps, interrupted workflow continuation | Existing `workflows/dags/_runtime/durable_checkpointer.py` | Remote operation success or external permission |
| Host operation journal/root autonomy | External effect admission, worker/process observation, leases/claims/effect correlation | `autonomy/runtime` and qualified adapter owner | Long-term semantic memory or human approval |
| MemoryService | Long-term episodic/private/shared knowledge, governed memory writes and retrieval | `Quantum-L9/l9-graphiti-memory` | GitHub effect truth, worker idempotency, strategic authority |

Never introduce a fourth cross-cutting store for convenience. SQLite initial checkpoint is source-backed and sufficient for one campaign if the mounted volume is durable; PostgreSQL migration is future evidence-driven scope, not a launch prerequisite.

## 6.2 CTO memory actor binding

A reserved `l-cto` identifier appears in `ops/memory/agent_identity.py`, but source explicitly calls it not wired. `environment/agents/agent_registry.yaml` has no active CTO entry at current pinned head, and upstream registries have no canonical CTO actor or service surface. Memory authorization must wait for upstream admission and operating-plane binding. A local setting of `L9_MEMORY_AGENT_ID=l-cto` **does not establish signed identity or namespace grants**.

Use existing `ops/memory/runtime_binding.py` to verify the memory package and contract (current manifest expects v2.6.0), `ops/memory/materialize_agent_authority.py` for per-principal scoped authorization, `ops/memory/agent_assertion.py` for signed assertion production and `run_memory_mcp.sh` where the selected transport actually applies. In-process `MemorySDK` is source-observed in the memory package, but its service/principal initialization must follow the actual deployment and trust contract; never bypass `MemoryService` policy through direct DB access.

## 6.3 Namespace design obligations

**CTO-private:** its own episodic campaign notes, failure classification, outcome evaluation and learning under exact CTO-specific grants.

**Shared:** only authorized operating knowledge and observations needed by other agents. Promotion to globally trusted shared knowledge follows MemoryService phase-lock/governed-write/review semantics and cannot be inferred from CTO preference.

**Other agents' private:** inaccessible unless the authoritative memory principal/namespace model explicitly grants it. Cross-principal access tests must be negative.

Names, mapping from repository to namespace and exact grant forms come from the **existing memory model and operating registry**, not an invented `cto/private` JSON rule in this pack. Do not hardcode a namespace string based on conversational intuition.

## 6.4 Memory lifecycle

- **Before action:** source-bound hydrate within authorized namespaces; distinguish no results from service failure; re-check current semantic source if memory recalls old architecture.
- **During action:** keep structured evidence/operation refs in actual effect journal; do not write worker's unverified statements as facts.
- **After accepted effect:** write a bounded, attributable fact with source ID, actual actor, namespace and evidence; qualified promotion if required.
- **On shutdown:** close the authorized memory session; lack of successful close must not erase external effect journal or authorize retry.

## 6.5 Least-privilege deployment

- Container runs non-root, read-only root filesystem if compatible, limited writable checkpoint volume, dropped capabilities, no privileged flag, no host network by default, restrictive resources and signal-driven termination.
- Host worker operates under an identity **without** access to human merge-grant issuer data, global secret stores or unrelated checkout locations.
- Credentials remain host/Infisical-owned and are materialized only by existing mechanisms. No human principal in process env, argv, prompts, logs, container image or repo.
- Service endpoint/spool, when approved, authenticates CTO and independently validates action scopes at the host. `localhost` by itself is no authentication boundary.
- Prevent client-supplied shell, PID, path or Git URL from becoming arbitrary host execution. Host chooses a fixed set of permitted behaviors backed by existing contracts.
- Logs and reports contain operation identity, digest, status and approved evidence references, not keys or arbitrary private memory.

## 6.6 Right-to-act matrix

| Activity | Read-only CTO | CTO with narrow campaign delegation | Worker | Human authority |
|---|---|---|---|---|
| Read authorized repos/current CI | Yes when access granted | Yes | Yes within worker scope | Yes per account |
| Hydrate its memory | Only with signed memory principal | Same | Its own principal | Human door where applicable |
| Propose coding task | Yes, no execution | Yes | No self-expansion | May delegate |
| Launch one code worker | No | Via actual host gate only | Cannot self-authorize peer | May separately authorize |
| Create/edit target source | No | CTO doesn't directly write host checkout | Yes only per native worker grant/hooks/worktree | May authorize |
| Publish PR | No | Only delegated existing publisher/gates | Existing publisher with authorization | Governing human rights |
| Merge protected PR | No | **No** | **No** | Exact head-bound human grant through existing gate |
| Write cross-agent memory | No without grant | Existing governed memory contracts | Its own eligible namespaces only | Authorized approval/provisioning |
| Change canonical actor or policy | No | No | No | Appropriate canonical owner separately |

## 6.7 Negative security demonstrations before promotion

Prove denied: unknown actor, forged grant, expired grant, wrong repo/SHA, different contract digest under same op id, repo broadening, raw GitHub bypass, worker reading merge grant, container reading Mac home, container Docker socket, unauthorized memory namespace read/write, stale signed assertion, and effect attempt during network partition. Evidence must include actual denial at the protected interface, not only a unit test of a model instruction.

## 6.8 Host failure and backup posture

SQLite persistent volume survives container recreate and Mac reboot. Backups and restore shall be tested before always-on promotion; checkpoint restoration must include correct schema/SQLite mode and no leakage into untrusted volume. Host journal durability must be independent from Docker container lifetime. Actual external GitHub state is authoritative during reconciliation. Do not copy a memory DB dump across agents to manufacture shared memory or effect state.

## v1.1 | APN and root autonomy privilege boundary

1. Source-grounded root autonomy `coordinator` capabilities are `campaign.inspect`, `graph.inspect`, `scheduler.request`, `status.inspect`; it has no general repository-write entitlement. Mutating workers use independently leased existing executor/remediator role ceilings and explicit campaign scope.
2. The shared root `CapabilityGateway` checks active, acknowledged, agent-bound lease, role capability, campaign-allowed/forbidden operations, and scoped paths. Host worker must revalidate for actual effect; an earlier gateway verdict must not be reused after grant revocation, base-SHA drift or expiry.
3. AgentPod `apn` node credentials authenticate the host; Hub agent principal/MCP grants authenticate agent dispatch; CTO canonical ActorIdentity is separate. No token becomes a surrogate canonical assertion.
4. General AgentPod `terminal` runs an unconfined shell as the APN host user. It MUST NOT be available to the CTO principal, nor usable through a secondary identity/route. General AgentPod `fs.write` must also be denied absent a mediated native effect path. Rootless APN alone is insufficient: isolate the worker from the human's merge/secret files with actual OS credentials and filesystem permission checks.
5. Cursor ACP permission responses are transport-level prompts; never auto-answer `allow-always`, and never interpret a prompt grant as L9 effect permission. Claude station route must preserve the existing native project settings, hooks, external native coding contract and applicable per-repo grant. Do not assume station discovery demonstrates conformance.
6. Root autonomy's `pr.merge`, `pr.admin_merge`, `git.force_push`, secrets and test-weakening constraints remain protected. No AgentPod agent principal is allowed to act as the interactive human merge-grant issuer. No alternate 'fleet' or generic terminal escape.
