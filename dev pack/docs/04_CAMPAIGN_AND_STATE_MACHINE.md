# 04 | Campaign intake, LangGraph semantics and executive continuation

## 4.1 Input admission model

The first CTO receives **one campaign**, not arbitrary untrusted freeform agent instructions. Intake must resolve:

- Objective and operator-approved outcome, exact campaign identity, governing authority, source evidence and accepted architecture freeze.
- Repo targets with explicit *read vs write* classifications and exact baseline refs/digests.
- Ordered stage dependencies; proof owners; target-specific acceptance; protected-effect gates; timeout/cost ceilings; negative cases.
- Native execution-contract identity and byte digest for delegated coding work; specific verification obligations.
- Explicit excluded tasks, constraints and unresolved mandatory inputs.
- Existing grant/permit refs. A campaign pack, even if internally consistent, conveys **no authority by itself**.

Partial packs may be inspectable or planned but must not enter executable stages with missing material contracts. The reference Branch Consolidation pack is currently in this class until three native contract directories are supplied and validated.

## 4.2 State components and lifecycle

Use existing `StateGraph` and the `open_checkpointer()` owner. Keep graph state minimal and serializable; include stable campaign thread identity, current stage/action, source/target provenance, verified binding refs, one outstanding host operation ID, pending evidence links, known unknowns, remediation count and stop reason. **This list describes required information, not a new frozen canonical schema**; implementation may map to existing DTOs and must not invent upstream schema fields.

Suggested graph nodes, implemented only if not duplicating existing node responsibilities:

| Stage | Input | Deterministic side effect? | Success transition | Failure transition |
|---|---|---|---|---|
| `INTAKE` | campaign ref / user request | No | `BOOTSTRAP` | `BLOCKED` |
| `BOOTSTRAP` | exact sources / identity assertion / configuration | Read-only probes | `RECOVER` | `BLOCKED` |
| `RECOVER` | checkpoint, outstanding op ids | Read-only host observe | `HYDRATE` | `WAIT_RECONCILIATION` |
| `HYDRATE` | memory queries under bound principal | Read-only memory | `OBSERVE` | `BLOCKED` if mandatory; degraded if optional |
| `OBSERVE` | current target and stage evidence | Read-only repo/CI/host | `DECIDE` | `BLOCKED`/retry bounded probe |
| `DECIDE` | accepted plan and observed evidence | No effects; produces candidate action | `VALIDATE` | `ESCALATE` |
| `VALIDATE` | grants/claims/contract/source hash | Read-only verification | `SUBMIT` or `VERIFY` | `BLOCKED` |
| `SUBMIT` | stable operation ID + exact immutable inputs | Host effect submission | `RECONCILE` | `RECONCILE` (even on timeout) |
| `RECONCILE` | host journal, remote effect state | Read-only observation | `VERIFY` / `WAIT` | `BLOCKED_UNKNOWN` |
| `VERIFY` | independent artifact, CI, acceptance proof | Qualified assessor may act within permission | `ADVANCE` or `REMEDIATE` | `VERIFY_PENDING` |
| `REMEDIATE` | scoped findings, revision-bound guardrails | New authorized operation only | `VALIDATE` | `ESCALATE` |
| `ADVANCE` | accepted stage receipt | Checkpoint update | `OBSERVE` / `COMPLETE` | `BLOCKED` |
| `COMPLETE` | all stage receipts and no pending effects | No | terminal `COMPLETED_VERIFIED` | N/A |
| `BLOCKED`, `ESCALATE` | typed reasons | No prohibited effects | resume only after external condition resolved | terminal pause |

Do not execute tools from a `graph.py` builder. Compile/checkpointer wiring belongs in `executor.py`. Use same `thread_id` on resume, not a new thread. Use typed, bounded error categories from actual owners when available.

## 4.3 Executive decision algorithm

1. Hydrate the last accepted strategic objective and frozen architecture refs; do not let old memory override current source.
2. Derive eligible stages from completed predecessor evidence, not from an LLM claim that a predecessor is "done".
3. Observe the present repository/PR/worktree/lease/capability state at the same exact target revision.
4. Enumerate bounded candidate next actions and their known permissions, dependencies, estimated costs/risks, quality of evidence and reversibility.
5. Reject actions with missing material authority, disputed owner, irreconcilable target revision or unverified external effects.
6. Among remaining lawful candidates choose the highest leverage action within the delegated campaign; preserve dissent and rationale for material trade-offs.
7. Generate the existing native coding contract/host request; do not rename fields to suit CTO preference.
8. Dispatch through host admission. On ambiguity observe and reconcile before any retry.
9. Evaluate effect against the stage's independent acceptance owner; same-scope remediations get new immutable operation identity and explicit delta.
10. Report status and evidence; continue without unnecessary operator relay.

The executive is not a strategic planner, compiler or canonical permission oracle. When all legal candidates are blocked, it reports the smallest missing dependency and can continue *independent* read-only research without violating the frozen campaign.

## 4.4 Retry and interruption rules

| Event | Required CTO response |
|---|---|
| Submit returns timeout before ACK | `observe(op_id)` first; pending/unknown prevents new invocation |
| Worker process dies before an effect | Query host journal and independent Git; retry only if the host proves no irreversible effect and grant still applies |
| Worker says success, CI absent | Mark worker terminal, acceptance pending |
| Machine reboots, checkpoint preserved | Load same thread, reconcile host journal and GitHub before new action |
| Same operation ID sent with same digest | Host returns same durable record; no second spawn |
| Same operation ID sent with different digest | Host rejects conflict; investigate scope/identity misuse |
| Long-running action exceeds budget | Cancel if separately authorized, then observe terminal/effects; cancellation request isn't rollback |
| PR head changes while verifying | Invalidate target-dependent acceptance and resolve new exact head |
| Scope violation discovered | Stop affected write; preserve evidence; ask correct owner for reauthorization, not silent expansion |
| Different controller attempts active campaign | Host claims/fencing refuse overlapping writer; no race-to-first-commit |

## 4.5 Concurrency and extension strategy

First deployment: one campaign, one actual coding worker. No child swarms or five-lane concurrency. Future parallelization is only after root autonomy claims, independent worktrees, per-worker leases, evidence aggregation, integrator single-writer rules and failure cleanup demonstrate correct operation. Avoid assuming `max_parallel` in retired PE is available or authoritative.

## 4.6 Completion and evidence

The CTO can report `COMPLETED_VERIFIED` only if every required stage has evidence applicable to its *exact* artifact and current governing source, all protected effects carry the correct grant or explicit pending outcome, no unresolved operation could have changed state, and any independent assessor required by the campaign has actually delivered a bound result. The operator-facing result should include accomplishment, exact refs/hashes, verified tests/checks, outstanding nonblocking risks, protected pending actions, and replay/rollback instructions.
