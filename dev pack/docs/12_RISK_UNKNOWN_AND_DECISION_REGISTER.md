# 12 | Risks, unresolved choices and owner-directed proof requests

## 12.1 Classification rule

A frozen design choice is not an open preference. A currently unproven implementation *obligation* must be resolved from its owner without reopening the frozen design. A material contradiction requires a separately authorized architecture revision, not a local patch. Status classes in the table are local planning labels, not admitted L9 semantic lifecycle types.

| ID | Unknown / risk | Present evidence | Required owner and proof | Blocks |
|---|---|---|---|---|
| U-01 | Canonical CTO actor identity admission | `.github` actor registry lacks CTO | Upstream actor registry owner admits exact actor and valid identity assertion | F2/F3 live |
| U-02 | Canonical CTO service surface / runtime identity | Surface registry lacks Docker CTO surface | Identity/surface/topology owner resolves exact dimension(s), no invented ProductKind | F2/F3 live |
| U-03 | Qualified projection producer receipt | Source current but canonical producer PASS not independently demonstrated | Current semantic compiler/projection owner supplies verified revision-bound artifact and receipt | Canonical bootstrap claim |
| U-04 | Standing scoped CTO delegation | No CTO effect grants on inspected local registry | Operator + effect owner approve narrower concrete scopes and issuer/expiry | F3 |
| U-05 | **AgentPod selected; secure provider binding unproven** | AgentPod MCP/APN architecture LOCKED; native `submit/observe/cancel` mapping unproved | AgentPod+CG owners demonstrate authenticated scoped principal and exact methods, host denial and receipt/idempotency | F3 |
| U-06 | Root autonomy journal legal extension | SQLite store exists, journal placement not committed | Root autonomy owner validates storage schema/claim contract before extension | F3 |
| U-07 | Claude Code and Cursor real Mac canaries | AgentPod descriptor lists Claude; Cursor ACP documented externally, not registered in AgentPod | Host and provider owners demonstrate AgentPod Claude+Cursor sessions, project hooks, grants and read-only canaries | F3 |
| U-08 | Real memory principal/private/shared namespaces | Package pinned; CTO principal not active | Memory owner + operating registry verify signed principal, namespace grants, denial probes | Memory-dependent F4 |
| U-09 | Host-effect reconciliation across restarts | Generic LangGraph saver test exists; no CTO live journal | Host/effect owner proves crash windows and no duplicate external action | F3 |
| U-10 | Independent assessor invocation | Requirement accepted, actual callable assessor not bound | Acceptance owner and CTO execution surface prove independent evidence path | F4 closure |
| U-11 | Exact Branch Consolidation source contracts | Three native contract directories missing | Source-pack owner supplies signed/exact content and review | F5 |
| U-12 | Service model provider configuration | Python/LangGraph chosen; DeepSeek only candidate | Runtime owner uses existing provider/configurable interface and proves structured decisions | F4 if model required |
| U-13 | Operator ingress interface | Telegram candidate, not selected | Use minimal existing intake/status path; new UI needs observed need | No F1 block |
| U-14 | Always-on hosting beyond Mac | Initial Docker Mac locked | Operational experience/SLOs trigger later hosting choice | Not initial |
| U-15 | Backup and upgrade of checkpoints/journal | Existing SQLite helper only | Deployment owner proves restore on actual host and schema compatibility | F6 |
| U-16 | Consolidation of legacy CoS/PE/WorkState | Operational convergence desired; PE runtime is eviction target | Map active living features and ensure one commander; no PE dependency | F4/F6 owner fence |
| U-17 | Host worker's OS principal separation | Same-account challenge forgeability documented | Host owner proves separate uid/user secret/merge-grant isolation | F3 |
| U-18 | Source filetree justified placement | File placement accepted; new exact-runtime imports unbuilt | CG owner implements smallest files and runs package/test proofs | F1 |
| U-19 | AgentPod mapping of observe/cancel and effect API | Logical requirements locked; actual Hub MCP/ACP operations not mapped | Provider+root-autonomy owners prove exact map, cancellation behavior and independently observed effects | F3 |
| U-20 | Mac-local vs hosted MemoryService reachability | Package API and binding source known; real deployment route unobserved | Memory transport owner establishes network/stdio arrangement with scoped keys | Memory-dependent F4 |

## 12.2 Highest-risk attacks

**R1 False READY:** startup and memory health are green while worker cannot execute or grants absent. Mitigation: effect-specific G1–G4, negative BT-001/BT-006/IO-008 and host-enforced eligibility.

**R2 Duplicate external effects:** CTO crashes after worker commit before ACK. Mitigation: durable acceptance before spawn, stable id, journal observe and independently checked Git target; IO-004/RC-003.

**R3 Same-account grant forgery:** hostile worker can mint something that looks like human terminal confirmation. Mitigation: separate host principal/filesystem rights, human issuer never reachable, PB-003/MS-009.

**R4 Shadow execution plane:** CTO accidentally creates own scheduler, publisher or policy. Mitigation: existing owner mapping, new-file irreducibility gate, source-level negative tests and prohibited-file scan.

**R5 Phantom successful campaign:** mocked contract `PASS`, test fixture or worker prose reported as real. Mitigation: explicit evidence provenance and separate acceptance status, CP-011/RC-005/PB-010.

**R6 Semantic drift:** `.github` actor/project details drift from generated local identity projection. Mitigation: revision-bound source verification and fail-closed stale receipt; BT-004/BT-005.

**R7 Hidden PE dependency:** retired path imported into new CTO. Mitigation: live code import graph check, explicit no-PE deployment test and review A21.

## 12.3 Decision log for deferred implementation parameters

Already selected: **AgentPod Hub MCP + Mac APN**. Do not reopen generic HTTP/spool as an equal option. Still unselected: exact AgentPod MCP principal/methods, ACP descriptor realization, host L9 enforcement seam, model provider, checkpoint DB migration, dashboard/TG interface, parallel worker count, host always-on topology, exact CTO actor/surface canonical names, a new host bridge file, general service endpoint, new event/receipt family. These remain local implementation or owner-admission choices only when supported by current source and positive+negative tests. Uncertainty is not authorization to invent them.

## 12.4 Developer escalation format

For any blocked package report: `unknown_id`, exact target owner/ref, source observation, why required for the current stage, attempted read-only verification, safe blocked behavior, minimum owner decision/evidence needed, and independently buildable work that can continue. Avoid serializing unrelated independent work behind one external admission.


## 12.5 v1.1 resolved design decisions vs unimplemented admission

**Resolved at operator-design level:**

| ID | Resolution | Status | Source / owner |
|---|---|---|---|
| RD-01 | Code stays in `Quantum-L9/Cursor-Governance`; no new CTO repository | LOCKED / NO CODE WRITTEN | Operator acceptance, earlier filetree |
| RD-02 | Host transport is AgentPod Hub MCP → Mac APN node | LOCKED / PROVIDER FIT UNPROVEN | Operator lock, AgentPod node+Hub docs |
| RD-03 | Cursor runs through documented Cursor CLI ACP, not automatic IDE chat control | LOCKED TARGET / ADAPTER ABSENT | Official Cursor docs + AgentPod current registry |
| RD-04 | Claude Code remains supported worker via AgentPod; reuse native L9 coding contracts and settings | LOCKED / POLICY PARITY UNPROVEN | AgentPod descriptor + current CG SDK/hook sources |
| RD-05 | Authority Resolver resolves applicable exact canonical law, **never issues grants** | LOCKED / QUALIFIED RECEIPT MISSING | L9 resolver skill + `.github` registries |
| RD-06 | CG **root AutonomyRuntime** owns campaign leases, roles, claims, gateway decisions, receipts | LOCKED / LIVE CTO BINDING MISSING | `autonomy/runtime/*`, adapter owner |
| RD-07 | CTO is coordinator; separately leased workers may mutate; merge grants remain human-only | LOCKED / HOST ENFORCEMENT UNPROVEN | Role policy + protected merge scripts |
| RD-08 | AgentPod is transport only, with host-side L9 reauthorization; deny unmediated terminal/fs.write | LOCKED INVARIANT / NEGATIVE PROOF MISSING | AgentPod documented terminal risk |
| RD-09 | No second policy ledger, scheduler, journal DB, publisher, memory or control-plane repository | LOCKED / IMPLEMENTATION REVIEW REQUIRED | Operator minimal-owner rule |

**Open proof requests, all still NOT_PROVEN:**

| ID | Required evidence (no guessed PASS) | Owner / earliest blocked phase |
|---|---|---|
| AP-01 | CTO actor/surface admission from exact `.github` owner; source revision and applicable assertion | Upstream identity owner / F2 |
| AP-02 | Producer-validated applicable projection and exact AuthorityResolution, not copied skill prose | Resolver + semantic projection producer / F2 |
| AP-03 | Proper CG `agent_registry` and `PEER_RUNTIME_BINDINGS` CTO binding, coordinator lease ceiling, memory principal | CG operating + memory / F2 |
| AP-04 | Scoped AgentPod **agent** principal and MCP API capabilities without operator `fleet` or node secret reuse | AgentPod Hub owner / F3 |
| AP-05 | Cursor ACP AgentPod descriptor or owner-approved compatible mediated equivalent, proven negative and positive | AgentPod node-agent owner / F3, WP-17 |
| AP-06 | Existing Claude AgentPod station and Cursor CLI project hooks/AGENTS/MCP/coding contract parity | Worker + CG owner / F3, WP-09 |
| AP-07 | Actual APN host effect gate consults L9 current lease/capability/revocation and exact contract SHA; can't be bypassed with terminal/fs.write | Root Autonomy+Host+Hub / F3, WP-18 |
| AP-08 | Durable host op id/digest, accepted-before-spawn journal, observe-first recovery and cancellation semantics | Root Autonomy journal + AgentPod / F3 |
| AP-09 | Mac OS principal isolation: worker cannot access human merge grant / secrets even as same machine user | Host owner / F3 |
| AP-10 | Authenticated CTO MemoryService principal, private/shared scope, package compatibility and actual endpoint | CG+MemoryService / F4 |
| AP-11 | Independently observed real host, Git, CI, worker results, not checkpoint/model/AgentPod status | Evidence/acceptance owner / F4 |
| AP-12 | Branch Consolidation reference campaign's actual native contract source directories | Reference owner / F5 |
| AP-13 | Real Docker & APN versions/availability on Mac; inbound/outbound hub reachability, local signed source refs | Host operator / F3 |
| AP-14 | Current project-based AgentPod support grant and upstream PR if required; external repo not writable by CTO pack | AgentPod repository owner / F3 |

**Test evidence status:** v1.1 adds specified BT/IO/MS/PB cases in chapter 09 and `machine/acceptance_tests.json`. They are all NOT_RUN. The update supplies no runtime PASS or upstream admission. Host permission/supply-chain provider integration is a risk, not a reason to broaden privileges.
