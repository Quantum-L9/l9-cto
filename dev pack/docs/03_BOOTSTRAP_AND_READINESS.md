# 03 | Service-native bootstrap and evidence-based readiness

## 3.1 Accepted bootstrap design (CTO-BOOTSTRAP-001)

**One governance system, three activation mechanisms.** Cursor uses IDE `sessionStart`; Claude Code uses `SessionStart` + project settings; CTO runs deterministic service-start and restart validation that consumes upstream authority and the same operating-plane controls. CTO does not execute Cursor or Claude hooks as its own bootstrap. When it dispatches Claude, the launched Claude process still independently activates its own project hook/settings chain and retains its separate actor identity.

The service may be **alive and inspectable** even when no consequential execution is allowed. Do not conflate *liveness*, *dependency health*, *identity resolution*, *capability evidence* and *authorization to perform a particular effect*.

## 3.2 Startup deterministic sequence

| Step | Input/proof | Owner | On missing or invalid |
|---|---|---|---|
| B00 Trusted authority locator | Independently provisioned upstream identity and pinned source verification basis | Deployment plus canonical authority owner | Expose `AUTHORITY_UNTRUSTED`, stop consequential dispatch |
| B01 Freeze canonical snapshot | One immutable `.github` SHA, declared source closure, no mixed moving refs | Source authority/projection consumer | `SOURCE_REVISION_UNKNOWN`, block dependent actions |
| B02 Qualified projection consumption | Applicable profile, source object digests, producer artifact and verifiable receipt | Semantic compiler/canonical profile owner | `PROJECTION_UNBOUND`; no local regeneration to bypass |
| B03 Resolve distinct identities | Product/release/runtime/actor/surface as applicable; CTO actor and service surface validated | Canonical identity resolver | `IDENTITY_NOT_ADMITTED` or `IDENTITY_UNVERIFIED`; refuse live actions |
| B04 Bind operating-plane grants | Active CTO binding and actual delegated scope, effective runtime profile, issuer/expiry | Cursor-Governance authorization owner | `DELEGATION_UNBOUND`; read-only diagnostics only |
| B05 Verify local image/config | Image source digest, Python pinned deps, no privilege mounts, checkpoint volume writable/durable | Runtime/deployment owner | `RUNTIME_UNAVAILABLE`; retain diagnostic output |
| B06 Bind memory principal | Package/contract pin, actual signed principal, namespaces and read/write grants | MemoryService / operating identity owner | `MEMORY_UNBOUND`; block memory-dependent work |
| B07 Recover checkpoint and effect state | Same thread ID; read host journal before any prior operation retry | LangGraph + host-effect owner | `RECOVERY_UNRESOLVED`; deny any potentially duplicate effect |
| B08 Verify host interface | Authenticated host endpoint, request binding, host-side effect scope, exact worker binary | Mac host owner | `HOST_UNREACHABLE`; deny real worker submission |
| B09 Read-only canary | Authorized, unique operation ID; observed process start/exit, journal and evidence | Host SDK + effect observer | `WORKER_UNPROVEN`; deny mutation |
| B10 Campaign admission | Complete native contract, exact repository SHA, allowed scope, current delegation and all prerequisites | CTO + existing gate owners | `CAMPAIGN_BLOCKED` or accurate missing evidence list |
| B11 Enter per-operation eligible mode | Every effect-specific requirement still true; no known unresolved identical action | Existing effect authorizer | Admit only the specified effect, no global authority |

No fixed CTO actor ID, new ProductKind, service provider, transport, or permission fields may be inferred from this sequence. These are **obligations**, not claims that the upstream owner already provides them.

## 3.3 Five core gate obligations (CTO-READY-001)

**G1 Identity:** verify accepted canonical CTO actor and service runtime surface, assertion authenticity, source/currentness and provenance. Local string `l-cto` alone fails.

**G2 Delegation:** verify a non-self-issued effective grant applicable to the exact repository, operation kind, executable, target SHA, file scope, worker, issuer and time window. If existing contract expresses a subset, consume it; do not add fields to a locked schema to cover an unknown.

**G3 Host worker:** demonstrate the host authenticates independent CTO requests, verifies native coding contract bytes/digest and worktree restrictions, launches an existing SDK worker, writes a durable operation acceptance record, and returns independently observable results. A working network socket or report file alone fails.

**G4 Recovery:** prove checkpoint preservation AND host effect journal correlation AND replay/idempotency of same operation ID across process death/lost ack. Distinct ids with same effects need policy-controlled reconciliation, not blind execution. Journal must preexist the consequential launch.

**G5 Memory:** prove signed CTO principal, MemoryService contract-compatible runtime, effective namespace grants and a real read/hydration against an authorized namespace. If memory is optional for the current operation, report degraded/unknown and withhold memory-dependent decisions; never substitute a different agent's principal.

For live delegated execution G1–G4 are mandatory. G5 is mandatory for operations consuming memory state or writing governed lessons. A campaign requiring memory cannot silently skip the dependency. Host-side mutation remains separately governed even if all five startup checks passed.

## 3.4 Evaluation semantics (not an invented canonical schema)

Describe each obligation as `PASS`, `FAIL`, `UNKNOWN` or `STALE` and attach evidence coordinate/revision/time. These are *reporting categories in this pack*, not new canonical enum members. Missing, contradictory, stale or unverifiable required proof means **not eligible**. `UNKNOWN` is not a warning that a caller may override. A mutable local success flag cannot supply provenance.

The CTO may publish a structured **readiness view** for operator inspection, but the actual host/effect gate must recompute or validate the underlying current evidence independently. CTO-readiness itself is *not* a grant and does not cause a bypass. `READY_FOR_READ` is allowed without worker eligibility.

## 3.5 Per-operation admission (mandatory after startup)

Before any `submit` with side effects:

1. Resolve the exact current target SHA and compare it with contract base and expected operation target. Reject stale or ambiguous targets.
2. Verify accepted frozen campaign step dependencies and that claimed scope does not overlap an active independent commander.
3. Verify current actor assertion and effective delegation, not merely presence of a cached bootstrap receipt.
4. Verify native coding contract structural validity with its owner and enforce semantic authority/permission at the real host boundary separately.
5. Verify host journal state for the identical operation ID; if accepted/running/terminal return observed current record, not another spawn.
6. Verify host worker account isolation and inability to write human grant-issuer data.
7. Reserve host operation record and root autonomy claims atomically as needed; process launch follows durable acceptance, not precedes it.
8. After completion, verify expected external effects with independent target providers before advancing acceptance.

**TOCTOU protection:** where GitHub SHA, grants, claims or worker health can change between check and effect, the host must validate at execution time and use effect API head checks/immutable input. CTO-side preflight alone does not secure the race.

## 3.6 Invalidation triggers

- Upstream canonical digest, current admitted profile or actor/surface status changes.
- Grant expires, revoked or scope changes; exact requested PR head moves.
- Worker process, SDK dependency, project hooks or host account changes.
- Worktree base, capability scopes, target ref or execution profile changes.
- Host journal reports conflicting digest for a known operation ID.
- Required MemoryService version, namespace authorization or principal changes.
- Checkpoint path changes, DB missing/corrupt, Mac restarts with unresolved effects.
- New independent reviewer finds invalid evidence or change breaches locked invariant.

Invalidate only affected evidence. Do not restart or recompile every component indiscriminately. Pending external outcomes must be reconciled before dependent operations resume.

## 3.7 Proof vector catalog

| ID | Input injection | Required outcome |
|---|---|---|
| BR-001 | Docker app launches, no authority pin | Service inspectable, live execution denied |
| BR-002 | Valid source pin, unknown CTO actor | No fallback to Cursor/Claude |
| BR-003 | Valid actor, no current delegation | Worker submit denied by host |
| BR-004 | Valid grant, hostile target repository/SHA | Deny before worktree creation |
| BR-005 | Transport reachable but host doesn't execute worker | No READY/VERIFIED claim |
| BR-006 | Signed CTO memory principal absent, memory health succeeds under Claude principal | CTO memory remains unbound |
| BR-007 | Valid initial bootstrap, grant revoked | Next protected action denied |
| BR-008 | SDK-installed but project governance files missing | Worker launch denied |
| BR-009 | Host returns `accepted`, no terminal record | Remain pending; no acceptance |
| BR-010 | Restart after checkpoint with host effect already committed | Observe/no second spawn |
| BR-011 | Stale successful readiness receipt | Revalidate; never elevate cached result |
| BR-012 | Actor-only identity mistaken for permission | Deny effect, report distinct missing delegation |

## 3.8 Implementation placement and acceptance

The CTO graph executor owns the composition and presentation of bootstrap readiness in `workflows/dags/cto/executor.py` and uses existing source-specific verifier readers. Existing `ops/scripts/emit_claude_readiness.py`, `write_runtime_readiness_receipt.py`, runtime-bound memory and adapter conformance are reference owners, not evidence the CTO has already passed. New CTO-domain negative tests belong in `tests/workflows/test_cto_runtime.py`; any owner-level regression sits next to the modified owner. Do not introduce `cto/readiness_schema.yaml` or `cto/permissions.py` unless source-grounded irreducibility requires it and a separate revision authorizes changing the locked filetree.

## v1.1 | CTO-ready gate integration, no second validator

- **Authority Resolver:** freeze current `.github` revision; resolve actor, surface, applicable source contracts and target-specific provenance. A skill's text or a local registry value is not a validated AuthorityResolution or a signed runtime assertion.
- **Root Autonomy Runtime:** verify campaign authorization, action readiness, role-policy ceiling, acknowledged active lease, operation mapping and scoped resource in `CapabilityGateway`. A coordinator may schedule/request but does not inherit workers' mutation capabilities.
- **AgentPod adapter:** require conformant peer/provider/surface binding, actual scoped Hub MCP agent principal, authenticated node station, and capability-specific worker route. `apn` machine identity is not a CTO actor grant; fleet/operator token is not the CTO's agent credential.
- **Host re-enforcement:** before any code/effect tool call, verify lease still valid, exact contract bytes/digest, target repo/base SHA, worker permission and host account isolation. No generic AgentPod Terminal or file-write capability available to the CTO. ACP `allow-once`/`allow-always` is NOT an L9 grant.
- **Recovery:** host-accepted operation ID bound durably before execution, observe-first on reconnect/restart, duplicate-id conflict detection, independent Git/CI/worktree evidence before VERIFIED.
- **Status:** provider online, MCP connected, APN enrolled, ACP process started, memory readable and Docker healthy are *component observations only*. Never independently imply live CTO execution READY.

Any missing required proof remains `BLOCKED` or `UNKNOWN` for the affected effect; F1 always reports `MOCK_ONLY` even with all fake adapter checks green. CTO-READY-001 is a *local design obligation*, not a newly minted global receipt schema.
