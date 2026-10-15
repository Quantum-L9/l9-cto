# 00 | Mission, frozen design decisions and delivery contract

## 0.1 Operator intent

The operator delegates a *technical outcome*, not a sequence of prompts to manually shuttle between tools. The CTO assumes the routine behind-the-keyboard technical executive role: inspect, choose, assign, monitor, correct, remember and verify. It may autonomously advance only those operations justified by actual delegated authority. Human-only decisions remain with their actual owners. A useful CTO reduces human relays rather than hiding them behind pseudo-automation.

Success is **one real, reproducibly accepted campaign**, interrupted and recovered without duplicate consequential operations, operated through current Cursor-Governance tools, not a dashboard showing optimistic green lights.

## 0.2 Decision record and status

| ID | Architectural commitment | Status and source basis |
|---|---|---|
| CTO-D001 | Standalone Python technical executive performing routine engineering operations | CONVERGED, original charter |
| CTO-D002 | Initial Mac Docker Desktop runtime, inside Cursor-Governance repo | LOCKED starting realization, design + operator confirmation |
| CTO-D003 | Independent of Igorbot and OpenClaw | LOCKED, user correction and original charter |
| CTO-D004 | `.github` owns canonical semantics and identity, no local substitute | LOCKED, confirmed source registry |
| CTO-D005 | Python + LangGraph for executive state and decision flow | LOCKED, operator acceptance |
| CTO-D006 | Reuse existing Cursor-Governance root autonomy capabilities, actual Claude SDK launcher, and native coding-agent contracts | LOCKED, pinned recon |
| CTO-D007 | Reuse `l9-graphiti-memory` for long-term private/shared memory under its own authorization | LOCKED, pinned memory binding |
| CTO-D008 | Distinct CTO actor and service surface, bootstrap derives verified upstream binding; no impersonation | LOCKED requirement; upstream *registration* NOT ADMITTED |
| CTO-D009 | Cursor IDE, Claude SessionStart and CTO service boot are different activation paths consuming the same governance | **CTO-BOOTSTRAP-001 LOCKED**, direct operator agreement |
| CTO-D010 | No READY from container health or memory alone; prove identity, delegation, worker interface, recovery | **CTO-READY-001** proposed acceptance realization of directly accepted readiness concern; no runtime proof |
| CTO-D011 | One active campaign + one delegated worker for the first real slice | LOCKED first-stage limit |
| CTO-D012 | Stable operation ID, host-observed effect journal, restart reconciliation and independent acceptance | LOCKED invariant |
| CTO-D013 | Merge and other protected grants remain independently human-authorized | LOCKED; current merge gates inspected |
| CTO-D014 | Fold routine operational coordination of CoS/PE/WorkState into CTO without inheriting retired Program Execution runtime | LOCKED intent; exact migration and fencing require source evidence |
| CTO-D015 | Branch Consolidation reference workload | SELECTED REFERENCE; not yet a runnable pack because native contract directories are missing |
| CTO-D016 | No new file unless an existing owner cannot lawfully satisfy the obligation | LOCKED implementation discipline |
| CTO-D017 | One bounded source recon → source-grounded filetree → coding | LOCKED operator sequencing, satisfied through these source documents |
| CTO-D018 | CO-Pilot: GAR architectural envelope → bounded Claude Code implementation → independent review and actual proofs | LOCKED development discipline |

**Do not misread the table:** A locked *requirement* can still depend on future canonical admission and live proof. CTO-READY-001 is the implementation-oriented gate design presented after user raised the false-READY danger; it is not a claim that `.github` admitted a new canonical contract.

### 0.2a Subsequent explicit operator locks, 2026-10-14

| ID | New locked decision | What it does **not** prove |
|---|---|---|
| CTO-D019 | **AgentPod selected** for Mac host control: CTO → AgentPod scoped agent MCP → enrolled APN Mac node → guarded Cursor ACP / Claude worker | A working host station, protocol bridge, local installation, or enforceable dispatch grant |
| CTO-D020 | **Authority Resolver + existing root Autonomy Runtime** are the authority-resolution and execution-authorization owners, respectively | Canonical CTO admission, live issuer grants or runtime integration |
| CTO-D021 | CTO coordinates and requests; existing action-specific `coordinator`/worker role and root lease/capability rules enforce each action; AgentPod does not grant L9 policy | Permission to act as a human, run host terminal unrestricted, or self-authorize a worker |
| CTO-D022 | **Cursor ACP is the selected Cursor worker interface**; it controls Cursor CLI agent sessions, not an already-open IDE session; Claude supported through AgentPod harness, with existing SDK still available for bounded native equivalence | Cursor is already a built-in AgentPod station, or project hooks behave identically |
| CTO-D023 | **No new CTO repository**; work stays in Cursor-Governance, with separately owner-authorized upstream identity and any AgentPod adapter change | Authority to write any of these repositories |
| CTO-D024 | Root autonomy authorization is **host re-enforced**, deny-by-default; durable host journal and independent verification cannot be replaced by AgentPod transport success | Existing JSON-line bridge is a secured host API or that ACP permissions enforce L9 grants |

The operator locked these architecture choices in the visible follow-up. The engineering proofs remain open in `docs/12`. A new AgentPod harness adapter requires its **own** upstream owner/grant, not a silent writable-scope expansion.

## 0.3 Single-line system promise

Given an authorized, correctly scoped engineering campaign and current governing authority, the CTO can determine the next authorized technical action, delegate it through existing protected execution paths, observe the actual result, obtain appropriate independent verification, persist continuity and recover safely after process or host interruption.

## 0.4 Architecture boundaries

**Owned by CTO:** executive choice, campaign intake/continuation, sequencing based on accepted dependencies, contextual hydration, operation-id correlation, review/escalation decisions, cross-operation convergence and accurate operator reporting.

**Not owned by CTO:** canonical semantic definitions; actor/surface admission; provider choice as canonical semantics; GitHub permissions or grants; memory storage, shared-memory promotion rules; native code implementation logic; Claude permissions/hooks; global execution lease protocol; publication/merge semantics; independent reviewer authority; deployment/host secret issuance.

## 0.5 Non-goals, explicitly excluded in initial tranche

No generic control plane, second dispatcher or scheduler, full PE resurrection, Telegram or elaborate UI, forced DeepSeek model binding, five-way parallelism, LangSmith platform dependency, database migration beyond existing SQLite checkpoint support, always-on cloud host, direct Docker mount of host home or Docker socket, automatic merges, architecture refreezing during code, autonomy self-grants or automatic semantic compiler invocation to manufacture canonical profiles.

## 0.6 Success rubric

1. Native service startup under Docker produces explicit per-capability evidence with missing mandatory components blocked.
2. Canonical identity, current binding and actual standing delegation are **validated**, not guessed.
3. CTO consumes a bounded complete campaign and produces a lawful next-action choice.
4. Mock path completes with honest `MOCK_ONLY` and strict refusal of real mutation.
5. Real path (later) submits a native coding contract through a *trusted host authority boundary*, invokes actual Claude with its own bootstrap and observes outcome.
6. Resume after intentional worker ACK loss, host interruption and replay does not duplicate external effects.
7. Host, Git and artifact acceptance evidence is attributed to the exact source/target revision, not copied from worker prose.
8. Memory permits CTO-scoped knowledge as authorized, denies unauthorized principal cross-access, and is not misused as an effect journal.
9. Protected publication/merge never inherits authority from CI success or the CTO's self-report.
10. First operator campaign demonstrates measurable reduction of routine human relays and zero false-positive completion claims.

## 0.7 Explicit non-authorization

This pack is an engineering specification and proposed implementation handoff. It does **not** grant code mutation, external repository access, push, merge, deployment, secret access, new actor admission, new semantic profile or the creation of a protected workflow. A downstream coding session must bind its own exact current targets, write permissions, frozen base and validated commands.
