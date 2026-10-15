# v1.1 resolved host-transport selection (supersedes generic selection in historical text below)

**Selected host technology:** AgentPod Hub with its agent-facing MCP API and enrolled rootless macOS `apn` node. CTO never operates the native APN node credential or an operator `fleet` session. Cursor uses its documented CLI `agent acp` interface, which is **not yet registered as an AgentPod harness** at inspected upstream revision. Claude Code is present as an AgentPod descriptor; actual L9 execution-contract/hook equivalence is still unproved. Do not implement generic ad hoc loopback HTTP/spool/SDK bridge before testing this chosen route.

**Logical host API** `submit → observe → cancel` remains an invariant, but it must be *mapped to real AgentPod Hub/MCP and station operations after reading provider contract*. Do not assume the verbs are actual Hub methods or invent MCP names. Root `AdapterOrchestrator`, lease/capability gateway and host journal own L9-side obligation. Enforce the grant on the APN/worker side, not only at the CTO container. A green `AdapterConformance` proves its own configured checks, **not** endpoint authenticity, code-tool mediation, operation idempotency or safe OS isolation. The physical journal owner is the existing root autonomy transactional store only if native producer review confirms legally compatible operation identity/lifecycle; no new journal database without separate justification. Also prove the AgentPod hub cannot provide an unmediated fallback Terminal/fs.write path under the CTO principal.

**Open integration questions:** exact scoped AgentPod service/agent principal and MCP dispatch method, whether Cursor ACP needs a new descriptor in AgentPod upstream or can be exposed via a tested existing harness without bypass, host-side per-effect L9 recheck, full operation idempotency, separate OS users, project hook inheritance for both workers, disconnect recovery and cancellation effects. None is runtime-proven. Read the following historical generic-port design as requirements to realize *through AgentPod*, not a competing transport choice.

# 05 | Docker-to-Mac host execution seam and durable effects

## 5.1 Status and ownership

This is the primary unfinished integration. The repository contains a **real Claude SDK launcher**, the native coding-agent contract and root autonomy leases, but no proven authenticated CTO-to-Mac `submit → observe → cancel` transport with immutable effect journal and anti-replay. **Do not treat this design section as an existing API or authorization to implement a new general service**. The host technology is AgentPod by explicit operator decision. Resolve its exact agent-MCP/APN/capability integration from current provider contracts and subject the host-side L9 mediation to independent adversarial tests before live dispatch.

The owner split remains fixed:

- CTO LangGraph chooses a task and correlates it with the campaign.
- Native coding-agent contract expresses bounded implementation work.
- Root autonomy owner governs applicable leases/claims/actions/receipts.
- AgentPod Hub routes only a properly scoped agent principal through the enrolled macOS APN station; the host independently rechecks L9 authorization before any effect.
- Cursor CLI ACP or Claude Code executes inside its own restricted worktree/account, preserving the applicable L9 project hooks and worker contract.
- GitHub, CI, host journal and independent reviewers establish effect/acceptance facts.

## 5.2 Candidate interface semantics (logical, not committed JSON fields)

**`submit`**: accepts an immutable operation identity, campaign ID, native contract identity/digest, exact repository + base SHA, admissible scope, actor provenance and independently issued delegation ref. Returns durable host acceptance or a typed denial. Success means the host has persisted a record; it does **not** mean a worker has performed an effect.

**`observe`**: accepts a previously authenticated operation reference; returns host-observed admission status, process state, operation evidence and terminal status if known. Host observations must not reveal credentials or arbitrary host paths. Polling a nonexistent operation must not create one. Observations after crash must come from persistent host evidence, not CTO in-memory state.

**`cancel`**: when authorized for that operation, requests controlled worker termination and records whether termination was confirmed, whether an effect may already have occurred, and what reconciliation remains. No implicit rollback, process kill based solely on user-supplied PID, or bypass of root autonomy claims.

These functions may be realized by an already available supported bridge or a minimal source-justified host adapter. The host transport **has been selected as AgentPod Hub MCP → APN**; provider-specific authenticated mapping for these logical operations is still unresolved, and a provider protocol is not invented by this pack. No invented socket, localhost port, secret filename, or new host daemon is admitted by this pack.

## 5.3 Host-side deterministic algorithm

### Submission

1. Authenticate the caller across the actual Docker/host boundary using a trust anchor inaccessible to the CTO model, not an unprotected custom header or the same user-readable secret.
2. Validate CTO actor assertion and current upstream/binding provenance against trusted references.
3. Resolve operation identity, immutable request fingerprint and native coding contract bytes at the host. Recompute digest and target identity.
4. Validate existing operating-plane delegation/claims for exact target/effect/file scope. Check worker-specific permission and grant expiration.
5. Consult transactionally durable journal for operation ID. If same fingerprint is already present, return existing record; if conflicting fingerprint, deny without execution.
6. Persist accepted operation and associated campaign/action/claim references in one durable host-owned transaction or equivalent contract-safe sequence.
7. Establish a dedicated isolated worktree from proven base using existing `agent_worktree_start.sh`; pin its path, base and task metadata in the record.
8. Launch actual existing Claude SDK, with `cwd` bound to that worktree, source-controlled `CLAUDE.md`, `.claude/settings.json`, `.mcp.json`, bounded mode/turns/budget and no shadow policy keys.
9. Capture process/session identity and stream terminal and failure observations to the persistent journal. The current launcher default `reports/agent_sdk/latest.json` **is not per-operation durable evidence**; host must bind output to operation before using it.
10. On completion, record terminal process facts. Separately determine external changes and required verification. Preserve UNKNOWN if process died mid-write or host response was lost.

### Observation/reconciliation

1. Read same durable operation record without changing it.
2. Check process liveness/session identity if current, leases and worktree state.
3. Query authoritative effect services (GitHub exact ref/commit/PR head, CI, local source diff) as needed.
4. Reconcile inconsistent states; terminal worker success never implies `VERIFIED`.
5. Return read-limited evidence references and any `UNKNOWN` preventing safe continuation.

## 5.4 Minimal operation state semantics

Use **existing root autonomy status/receipt constructs wherever they already model the required lifecycle**. The following are explanatory transition concepts, *not* approval to add a new enum schema:

```text
absent -> accepted -> running -> terminal_observed -> independently_verified
                       |               |
                       v               v
                  outcome_unknown  verification_pending
                       |               |
                       +--- reconcile--+

accepted/running --authorized_cancel--> termination_pending
termination_pending --> terminal_observed OR outcome_unknown
```

An accepted operation may remain unknown after a crash. An executable retry is possible only when the authoritative host/effect owners can prove no duplicate or when the effect itself is idempotent under its provider contract and current grant. Lack of a journal row is not automatically proof that no external write occurred if pre-journal legacy runners may have run; classify that scenario separately before adopting the new path.

## 5.5 Host journal owner choice

`autonomy/runtime/store.py` is a **candidate** existing storage owner: it has WAL, transactional methods, campaign/action/lease/claim/artifact/receipt tables; `autonomy/adapters/cursor/host_bridge.py` shows adapter-specific extension within root SQLite. Validate its active lifecycle and concurrency semantics first. If it can lawfully store stable CTO operation acceptance and recovery metadata, extend in place. If not, produce an upstream owner/contract decision before adding a new state database. Do not turn an existing Cursor hook table into a generic service bus by analogy alone.

## 5.6 Worker launcher reuse and constraints

Source: `environment/agents/adapters/claude-agent-sdk/l9_agent.py`. It supports `ClaudeSDKClient`, `setting_sources=['project']`, `cwd`, `permission_mode` choices `default|acceptEdits|plan`, JSON-schema report, bounded turns/budget and file checkpointing. It **does not** currently provide CTO durable operation IDs, live host ingress or cross-process cancellation and reconciliation. `validate_agent_sdk_env.py` forbids another project policy copy. Worker launch must use actual project trust and attached native hook enforcement; no `bypassPermissions`, environment-crafted bypass, broad allowlist, `can_use_tool` shadow or model-authored host executable path.

**Source-level minimum health** (`--mcp-status`) is a probe, not proof that a code task can run. **Real read-only canary** must demonstrate host-signed request, actual SDK invocation, project settings loaded, unprivileged tools, isolated worktree, native reports and correct journal response. **Mutation canary** later needs real grant, exact target, tests and independent effect confirmation.

## 5.7 Threat model and adversarial boundaries

| Threat | Required prevention and proof |
|---|---|
| Model supplies forged actor/grant | Host authenticates against trusted source; negative forged assertion test |
| Same-UID worker accesses merge-grant file | Worker uses separate OS account/filesystem privileges; canary tries read and fails |
| Container mounts host home/keys/docker socket | Image/compose restrictions + runtime inspection/negative probes |
| Caller swaps native contract after validation | Recompute host-side SHA256 of accepted bytes; reject changed content |
| Operation ID reused with different payload | Transactional fingerprint conflict denies without launch |
| ACK lost after external commit | Subsequent observe returns existing operation and observed commit; spawn counter unchanged |
| No current delegation but previous bootstrap green | Host checks authority at effect boundary and denies |
| Worktree collision | Existing task metadata/claims plus distinct scoped paths; no foreign modification |
| Worker result self-certifies independent verification | Separate assessor/provider evidence required |
| Host dies after accepted but before spawn | Recovery inspects accepted journal, process/effect evidence and decides lawful continuation |
| Host dies after spawn before result | Process/session and external effect recon before rerun |
| Cancellation during Git operation | No success/rollback guess; inspect Git refs and reconcile |

## 5.8 Test phases

**P0 structural:** contract validator, SDK options, wrong-repo rejection, no new policy keys, journal logic with fake launcher.

**P1 controlled host:** authenticated read-only SDK canary in dedicated worktree; real host journal, timeout, cancellation and restart scenarios. Confirm failure when workspace is untrusted or project governance missing.

**P2 governed mutation:** exact approved isolated fixture repo and grant, one intentionally limited code delta, actual independent file/Git evidence and denial of out-of-scope edits. No production or unrelated repo.

**P3 interruption:** kill CTO before ack, keep/kill host as separate cases; confirm no duplicate external effect, correct rebind and honest UNKNOWN.

**P4 publication:** on an explicitly authorized test PR, existing publisher path only; verify actual PR head and receipt. No auto merge. Validate protected grant remains human-only.

## 5.9 Decision locked to AgentPod; remaining integration proof

Host transport selection is **AgentPod**, not open HTTP/spool. Owner must prove the exact secure and least-privileged Hub MCP → APN → agent station implementation with independent L9 authorization, OS separation, operation journal and negative tests. Whether L9 needs a native wrapper or an upstream AgentPod Cursor descriptor is still a bounded proof, not permission to replace AgentPod or invent a localhost port. F1 Compose continues shipping with **no live worker access**.
