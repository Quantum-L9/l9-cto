L9 CTO — Consolidated Architecture and Operating Charter

Revision: CTO-ARCH-001 / Conversation Baseline v0.1
Date: October 13, 2026
Status: Architectural direction converged; implementation architecture not fully frozen
Intended architectural owner: GAR in ChatGPT
Implementation home: Quantum-L9/Cursor-Governance
Upstream semantic authority: Quantum-L9/.github
Execution authorization: Not granted by this document

⸻

1. Executive Summary

The L9 CTO is an autonomous technical executive intended to replace the human operator’s routine activities behind the keyboard.

The operator will supply strategic objectives, campaign packs, delegations and exceptional decisions. The CTO will use the existing L9 execution/control plane to advance those objectives through completion.

The CTO is not merely a conversational assistant, project manager, task dispatcher, or advisory agent.

It is an operational agent responsible for inspecting engineering state, deciding what should happen next, invoking existing execution capabilities, supervising specialists, reconciling failures, verifying results, maintaining continuity and escalating only matters outside its delegated authority.

Primary mission:

Accept a properly authorized engineering campaign, assume day-to-day technical operating responsibility, operate the existing control plane, and deliver independently verifiable outcomes with minimal human intervention.

The CTO must not recreate an execution platform that already exists.

Its principal new capability is autonomous executive judgment applied to the existing L9 machinery.

Selected architectural foundation

* Standalone Python CTO application.
* LangGraph as the executive agent runtime.
* Initially hosted inside Docker Desktop on the operator’s Mac.
* Cursor-Governance as the existing execution/control plane.
* .github as upstream canonical semantic and identity authority.
* l9-graphiti-memory as the long-term memory product.
* Existing governed Claude Code and Claude Agent SDK facilities for coding execution.
* CO-Pilot as the GAR-side development, review and delegation operating protocol.
* No dependency on Igorbot or OpenClaw for the selected CTO runtime.

The proposed runtime begins with one CTO operator and one active campaign. Parallelism and more sophisticated autonomy are enabled progressively, without introducing unnecessary infrastructure.

⸻

2. Problem Definition

2.1 Current operating problem

The operator currently performs substantial technical coordination work manually.

This includes reviewing campaign packs, understanding their dependencies, choosing which agent or skill to invoke, preparing assignments, initiating work, checking results, responding to failures, preserving context, commissioning remediation and deciding what happens next.

The existing L9 environment already contains significant execution infrastructure.

The bottleneck is not necessarily the absence of another coding agent or execution system.

The bottleneck is the continuing requirement for a human to act as the intelligent operator connecting those capabilities.

2.2 Desired outcome

The CTO assumes those operational responsibilities.

Instead of receiving a recommendation that requires the operator to execute another sequence of commands, the CTO invokes the relevant control-plane capabilities itself, provided the action falls within an established delegation.

The operator remains responsible for strategic direction, business decisions, exceptional permissions and decisions reserved to a human by applicable authority.

2.3 Success criteria

A successful CTO can:

1. Accept an engineering campaign pack.
2. Understand its objectives, stages, dependencies, source requirements, restrictions and acceptance criteria.
3. Establish its own valid identity and operational permissions.
4. Recover relevant historical and shared knowledge.
5. Inspect authoritative current source and runtime state.
6. Determine the highest-leverage authorized next action.
7. Invoke the relevant existing control-plane capabilities.
8. Supervise execution and remediation.
9. Recover from interruptions without duplicating consequential effects.
10. Obtain appropriate independent evidence and acceptance.
11. Continue without routine human relays.
12. Escalate only when a genuine authority, strategy, architecture, risk or resource boundary is reached.

The CTO’s success is measured by completed and verified outcomes, not by the number of messages, tools, workflows or agents it creates.

⸻

3. Predecessor Architecture Decisions

Three predecessor candidates were reviewed.

3.1 Candidate 1 — Interim Igorbot CTO

The first proposal placed an l9-cto skill within Igorbot’s existing OpenClaw orchestrator.

It proposed bounded Claude Code execution, independent review, cron continuity and eventually commissioning a permanent CTO.

Its strengths included role separation, reuse of existing components, bounded remediation and explicit safety gates.

However, it was an execution-coordination design rather than a complete technical executive. It also depended on unresolved Igorbot ingress, sandbox, ACP, deployment and shared-rule conditions.

Disposition: Historical reference. Not the selected runtime direction.

3.2 Candidate 2 — Hardened Igorbot CTO

The second proposal strengthened Candidate 1 through:

* Explicit reuse of Cursor-Governance’s existing Claude worker bootstrap.
* Correct interpretation of OpenClaw session-level sandbox semantics.
* Executable protections against unauthorized PR merging.
* Reduced routine operator handoffs.
* Stronger source-bound validation, negative tests and recovery requirements.

It remained an Igorbot-based architecture and had not demonstrated live end-to-end operation.

Disposition: Preserve its execution, assurance and safety lessons. Do not adopt its runtime dependency.

3.3 Candidate 3 — Standalone Docker CTO

The third proposal described a standalone CTO application hosted initially on the operator’s Mac, independent of Igorbot and OpenClaw.

It proposed a containerized coordinator, external reasoning, durable local task state, a restricted Mac host-worker interface, governed Claude Agent SDK execution and separate human authorization.

The candidate also explicitly documented historical operator decisions selecting Cursor-Governance as the initial implementation home and rejecting an Igorbot-based runtime.

Disposition: Selected starting architecture, subject to the refinements established in this conversation.

3.4 Refinements agreed after Candidate 3

The subsequent discussion made six material changes:

First: The CTO is not another project coordinator. It replaces the operator’s routine keyboard activities.

Second: The CTO consolidates the operational functions previously allocated to Chief of Staff, Peer Execution and WorkState.

Third: Cursor-Governance has evolved into an execution plane, while canonical semantic governance lives upstream in .github. The CTO must leverage existing execution capabilities before introducing new ones.

Fourth: LangGraph is selected as the CTO’s executive agent runtime.

Fifth: The CTO is designed to consume a fully functioning L9 memory capability, with private CTO memory and/or authorized shared agent memory.

Sixth: All L9 identity, semantic authority and governance bindings must be derived through canonical upstream bootstrap rather than hardcoded into the CTO.

These later decisions supersede conflicting assumptions in the earlier candidate architecture.

⸻

4. Consolidated Decision Register

ID	Architectural decision	Current status
CTO-D001	CTO replaces the human’s routine technical operating role	Converged
CTO-D002	Candidate 3 is the starting architecture	Converged
CTO-D003	CTO is independent of Igorbot and OpenClaw	Converged
CTO-D004	Initial implementation belongs within Cursor-Governance	Converged direction; exact source placement unresolved
CTO-D005	.github remains canonical upstream authority	Converged
CTO-D006	CTO consumes existing execution-plane capabilities	Converged
CTO-D007	CTO assumes Chief of Staff, PE and WorkState operational responsibilities	Converged intent; migration details unresolved
CTO-D008	LangGraph is the executive runtime	Selected
CTO-D009	Initial host is Mac Docker Desktop	Selected initial direction
CTO-D010	Existing governed Claude execution is reused	Converged
CTO-D011	L9 Graphiti Memory supplies long-term memory	Converged direction
CTO-D012	Private and shared memory are supported through governed access	Converged requirement; deployment arrangement unresolved
CTO-D013	Identity and governance are resolved through upstream bootstrap	Converged invariant
CTO-D014	CO-Pilot operating structure governs CTO design and implementation	Converged
CTO-D015	Protected decisions retain their proper authorization boundaries	Converged
CTO-D016	Telegram may serve as initial operator ingress	Candidate
CTO-D017	DeepSeek may serve as the reasoning model	Candidate
CTO-D018	Checkpoint persistence uses an existing LangGraph-compatible store	Required; backend selection conditional
CTO-D019	Docker-to-Mac transport is narrow and independently secured	Required; mechanism unresolved
CTO-D020	The Branch Consolidation campaign is a reference acceptance workload	Selected
CTO-D021	No new general-purpose control plane or duplicate worker framework	Converged invariant

A conversationally converged decision does not, by itself, create a canonical source revision, formal L9 authority receipt or implementation permission.

⸻

5. Logical System Architecture

The CTO is an executive operating capability built on the existing execution plane.

5.1 High-level relationship

Operator / Principal

Provides objectives, campaign packs, standing delegations and exceptional decisions.

Planner

Provides accepted strategic priorities and intended outcomes where applicable.

GAR in ChatGPT

Owns architectural analysis, convergence, adversarial review and bounded implementation delegation.

L9 CTO

Operates engineering campaigns and exercises delegated technical operating judgment.

Cursor-Governance

Provides existing executable mechanisms for worker management, program execution, governed coding, control-plane tools, validation and publication.

L9 Graphiti Memory

Provides long-term knowledge, evidence lineage, governed memory access and available shared or private memory capabilities.

Quantum-L9/.github

Provides canonical semantics, identity models, invariants, authority definitions and applicable upstream governance.

5.2 Runtime structure

The initially proposed physical structure is:

Docker container:

* CTO application.
* LangGraph graph and runtime.
* Executive reasoning adapter.
* Campaign intake and interpretation.
* Identity/bootstrap consumer.
* MemoryService client.
* Restricted control-plane adapter.
* Workflow checkpoint persistence.
* Operator interaction interface.
* Structured status and evidence reporting.

Mac host:

* Existing Cursor-Governance checkout and execution facilities.
* Governed Claude Agent SDK worker.
* Existing coding-agent specialization.
* Host-owned Git and worker credentials.
* Authorized repository worktrees.
* Narrow, authenticated interface to the CTO container.

External or independently operated services:

* .github canonical source.
* GitHub repository/PR/CI services.
* L9 Graphiti Memory deployment.
* Selected reasoning model provider.
* Independent review and acceptance facilities where available.

These are logical and proposed physical boundaries. They do not authorize new repositories, daemons, host permissions or infrastructure.

⸻

6. CTO Executive Responsibility

The CTO’s purpose is to perform technical operating work that the human would otherwise perform.

6.1 Campaign intake

The CTO receives a campaign pack and identifies:

* The requested outcome.
* Accepted and proposed architectural decisions.
* Applicable canonical authority.
* Target repositories and revisions.
* Stage dependencies.
* Required execution contracts.
* Permitted and forbidden effects.
* Existing blockers and unknowns.
* Acceptance criteria and evidence requirements.
* Protected decisions requiring external authorization.

The CTO must distinguish a source-audited proposal, implementation-ready contract, independently verified result and authorized effect.

Receiving a pack never constitutes permission to mutate repositories.

6.2 Executive planning

The CTO converts an accepted campaign into an executable sequence using the existing control plane.

It determines readiness, sequencing, dependencies, staffing or worker requirements, proof obligations and budget constraints.

It may make implementation-level and operational decisions within its actual delegated authority.

It must not independently replace accepted global strategy or architecture.

6.3 Control-plane operation

The CTO directly invokes appropriate existing execution mechanisms.

It is not limited to producing prompts for the operator to copy.

It must be capable of issuing bounded, typed requests; monitoring their actual execution; consuming results; and initiating authorized follow-up operations.

The CTO should discover and bind current supported capabilities from Cursor-Governance rather than maintain a parallel hardcoded list of shell commands.

6.4 Specialist supervision

The CTO commissions existing execution specialists, including governed Claude Code workers.

It manages work sequencing, requests bounded remediation and reconciles independent evidence.

Workers cannot self-expand their mission, grant themselves permissions or substitute their own self-evaluation for independent acceptance.

6.5 Failure handling

The CTO handles routine failures without immediately escalating them to the human.

Examples include failed CI, incomplete tests, interrupted sessions, stale evidence, recoverable source conflicts and implementation defects that fit the accepted remediation scope.

Failures requiring changed architecture, new authority, expanded repository access or unapproved consequential effects are escalated.

6.6 Continuity

The CTO maintains the ability to resume campaigns after application restarts, worker interruptions and lost acknowledgements.

A restarted CTO must reconcile actual external effects before continuing.

Checkpoint existence alone does not establish that a remote operation succeeded or failed.

6.7 Reporting

The CTO gives the operator a compact executive report containing:

OBJECTIVE | VERIFIED DONE | BLOCKED | EXACT HEAD / ARTIFACT | NEXT SAFE ACTION | NEEDS OPERATOR

Reports distinguish observed results from inference and unknowns.

A routine status update should not become another action the human must perform.

⸻

7. Consolidation of Chief of Staff, PE and WorkState

The CTO is intended to replace their separate operator-facing responsibilities.

7.1 Chief of Staff

The CTO assumes technical campaign coordination, progress management, bounded specialist routing, blocker resolution and attention management.

This removes the need for a separate engineering campaign coordinator supervising the CTO.

Portfolio-level responsibilities that remain genuinely strategic must still respect Planner ownership.

7.2 Peer Execution

The CTO assumes executive responsibility for choosing when and how authorized engineering work is delegated, monitored, retried and reconciled.

However, existing Peer Execution code, adapters and worker-management mechanisms may remain valuable subordinate execution components.

Replacing a responsibility does not require deleting its working implementation.

The architecture must first distinguish reusable execution primitives from independently competing controllers.

7.3 WorkState

The CTO assumes responsibility for maintaining coherent engineering campaign continuity.

LangGraph checkpoints provide execution-thread continuity. Existing control-plane receipts and authoritative external artifacts provide execution facts. Long-term memory provides reusable knowledge.

Existing WorkState mechanisms may be reused, adapted or retired, but a second authoritative campaign writer must not remain active for the same scope.

7.4 Migration invariant

For each active campaign:

* One designated operational commander.
* One authoritative owner for each mutable state domain.
* Explicit ownership transfer or fencing when replacing a controller.
* No duplicated mutating dispatch.
* No shadow campaign status source.
* Preservation of existing receipts and historical evidence.

The exact migration from current capabilities remains a source-inspection and architecture-convergence task.

⸻

8. LangGraph Executive Runtime

8.1 Selected responsibility

LangGraph owns CTO decision-flow orchestration and resumable executive operating state.

It does not replace Cursor-Governance’s coding tools, workers, authorization gates or source-owned execution implementations.

8.2 Initial graph

The first implementation should use a small graph:

Intake → Bootstrap/Bind → Observe → Decide → Validate Authority → Act → Reconcile/Review → Continue, Escalate or Complete

This may be implemented with a smaller number of physical graph nodes where doing so preserves the required boundaries.

8.3 Responsibilities by stage

Intake: Read campaign input, identify required artifacts and reject unsupported execution assumptions.

Bootstrap/Bind: Resolve identity, governance, available capabilities and permitted authority.

Observe: Retrieve current campaign, source, worker, PR, CI, memory and permission evidence as needed.

Decide: Select the next operational play within the accepted objective.

Validate Authority: Deterministically determine whether the proposed operation is permitted.

Act: Invoke an existing control-plane capability through an authenticated interface.

Reconcile/Review: Establish what actually occurred and whether independent proof is required.

Continue: Advance the campaign or select bounded remediation.

Escalate: Suspend at a genuine protected decision or unresolved authority boundary.

Complete: Declare only the outcome supported by actual evidence and required acceptance.

8.4 One thread per campaign

A campaign should have a stable LangGraph thread identity.

That thread may retain references to its accepted objective, source bindings, stages, current decisions, outstanding operations, relevant evidence and authorized next actions.

The checkpoint must not become a substitute for GitHub, canonical semantics, authorization or independently verified external effects.

8.5 Native LangGraph facilities to use

The first implementation should leverage:

* Conditional graph routing.
* Stateful graph execution.
* Persistent checkpoints.
* Resume after interruption.
* Human-in-the-loop interrupts.
* Structured graph state.
* Runtime state inspection.
* Controlled graph branching.

Subgraphs and multi-campaign parallelism can be introduced when the reference campaign demonstrates the need.

8.6 Framework selection

LangGraph is selected.

DBOS and Temporal are not initial dependencies. Another workflow engine should be admitted only when a demonstrated requirement cannot be satisfied cleanly by LangGraph and the existing execution plane.

LangSmith is optional for observability; its deployment platform is not required for the initial application.

8.7 Persistence

SQLite-backed checkpointing is an initial local-development candidate.

PostgreSQL is a stronger candidate when concurrency, durability, operational availability or production requirements justify it.

The checkpoint-store selection and backup/recovery policy are not yet frozen.

⸻

9. Cursor-Governance Execution-Plane Integration

9.1 Ownership understanding

The repository name Cursor-Governance reflects historical governance responsibilities.

The selected architecture recognizes that canonical semantic governance has moved upstream into .github, while Cursor-Governance contains important execution capabilities.

The CTO must respect that separation.

9.2 Existing capability families to inspect and reuse

The predecessor evidence identifies relevant existing areas including:

* Program Execution controllers and campaign facilities.
* Peer Execution dispatch and provider mechanisms.
* Autonomy tooling.
* Runtime and worker identity bindings.
* Claude Agent SDK adapter.
* Governed Claude Code bootstrap and projection.
* l9-coding-agent.
* Coding contract compiler.
* GMP execution protocol.
* Worktree creation and isolation.
* PR publication, remediation and overlap controls.
* Generated artifact handling.
* Existing tests and evidence facilities.

These are reuse candidates, not yet a completed current-revision integration map.

9.3 Reuse-first rule

Before implementing a new CTO component, GAR must determine:

1. Whether the capability already exists.
2. Its exact source owner and active consumer.
3. Whether it is callable in the intended host.
4. Whether the CTO can consume it without shadowing authority.
5. What minimum integration is genuinely missing.

Every proposed implementation receives one disposition:

REUSE / EXTEND / REPLACE / NEW / DEFER

A new component must have a demonstrated semantic or operational gap.

9.4 No shadow execution plane

The CTO must not create an independent replacement for:

* Coding-agent governance.
* Claude bootstrap and projection.
* General worker execution.
* Existing sanctioned worktree operations.
* Shared publication controls.
* Global semantic validation.
* Canonical authority.
* Existing execution gates.

The CTO may need a thin adapter to invoke those capabilities. That adapter is not a second implementation of their logic.

9.5 Existing runtime versus executive authority

The CTO becomes the accountable technical operator of the execution plane.

That does not allow the CTO to fabricate the rights of a human, GAR, Planner, independent reviewer or canonical semantic owner.

Delegated action authority must be real, precise and independently enforced.

⸻

10. L9 Memory-Native Architecture

10.1 Requirement

The CTO must be designed to operate with fully functioning L9 long-term memory.

The chosen memory product is:

Quantum-L9/l9-graphiti-memory

The CTO should not create an alternative memory database, independent memory ontology or competing graph memory framework.

10.2 Private CTO memory

Private CTO memory is intended for knowledge such as:

* Campaign experiences.
* Recurring engineering problems.
* Known operational failure mechanisms.
* Historical remediation outcomes.
* Operator working preferences where authorized.
* Specialist performance observations supported by evidence.
* Previous technical decisions and their context.
* Reusable operational lessons.

Private memory must have explicit access controls.

Its physical deployment need not be separate if authorized logical isolation is sufficient.

10.3 Shared agent memory

The CTO may consume authorized shared L9 memory.

Shared knowledge can provide:

* Verified architectural background.
* Reusable engineering lessons.
* Source-backed discoveries.
* Cross-agent historical context.
* Known system relationships.
* Accepted operational guidance.
* Relevant prior incident and resolution information.

Access must be enforced by the existing memory system’s identity and namespace model.

The CTO does not automatically acquire every agent’s private memory.

10.4 Memory promotion

CTO-private learning should not automatically become globally trusted shared knowledge.

Promotion into shared memory follows the existing memory owner’s admission, provenance and authorization requirements.

An unverified worker assertion is not sufficient to establish shared truth.

10.5 Memory versus execution state

Three state categories remain distinct:

Execution state: LangGraph checkpoints and verified execution receipts.

Long-term knowledge: L9 MemoryService.

Canonical authority and operational truth: Upstream semantics, accepted grants, source repositories, GitHub and the relevant control-plane owners.

A memory record is evidence or knowledge context, not an automatic authorization.

10.6 Memory lifecycle

At campaign intake, the CTO retrieves relevant private and shared context.

During technical decisions, it checks whether retrieved knowledge is current, relevant and properly supported.

After verified work, it submits bounded memory candidates through the existing admission process.

At completion, it retains durable lessons and outcomes.

After restart, it recovers execution state first, reconciles external effects and refreshes relevant memory rather than replaying actions based on remembered intentions.

10.7 Full-capability and degraded behavior

The CTO is designed against the intended full MemoryService capability profile, including governed canonical storage, temporal validity and appropriate graph/active-memory services.

The actual availability, deployment topology and current APIs must be verified.

If memory is unavailable, the CTO must report the affected capabilities accurately.

It must not pretend that a checkpoint is shared memory or silently substitute a separate memory authority.

Exactly which operations can continue in a degraded memory state remains an operational policy decision. A full-memory readiness claim requires actual end-to-end proof.

⸻

11. Upstream Identity and Governance Bootstrap

11.1 Invariant

L9 identity and governance semantics flow downstream from .github.

The CTO must not hardcode a CTO actor identity, governance profile, semantic role mapping or permissions in its application.

11.2 Bootstrap trust anchor

A minimal trusted locator and verification basis must exist so the runtime can find and authenticate the upstream authority.

This may be configuration, but it must not become a duplicate semantic authority.

The bootstrap process must fail closed if the governing source or verification material cannot be trusted.

11.3 Bootstrap sequence

Phase 1 — Discover authority

Resolve the registered canonical sources, applicable admitted revision and immutable source coordinates from .github.

Do not mix independently fetched moving-main files from different revisions.

Phase 2 — Resolve identity

Resolve applicable Product, Release, Runtime, Actor and Surface identity dimensions using current upstream models and actual runtime evidence.

Phase 3 — Validate identity assertion

Establish an assertion bound to the resolved identity, governing revision and evidence of the real runtime.

A container name, model name or arbitrary local string must not self-establish an L9 actor.

Phase 4 — Resolve operational bindings

Resolve the relevant governance profile, delegated permissions, available execution capabilities and memory access.

Identity, execution authorization and memory authorization remain distinct.

Phase 5 — Initialize CTO runtime

Provide the verified bootstrap context to LangGraph and relevant integration adapters.

Phase 6 — Revalidate when necessary

Material upstream changes invalidate affected assumptions and require fresh resolution before consequential operations proceed.

11.4 Unknown CTO identity

The historical identity review indicated that the standalone CTO actor and Docker surface may not yet have canonical registrations.

Their exact current status must be independently rechecked.

If missing, the proper upstream owner must determine the correct admission or registration path.

The CTO must not impersonate an existing actor as a workaround.

11.5 Downstream attribution

Execution requests, worker results, memory operations, audit records and authorization checks must preserve their applicable resolved identities.

A Claude worker retains its own identity and delegated contract. It does not become the CTO merely because the CTO dispatched it.

11.6 Bootstrap failure

If identity or governance bootstrap fails:

* Consequential execution remains disabled.
* No permissive fallback profile is selected.
* No hardcoded identity is substituted.
* The actual failure is exposed through diagnostics.
* Recovery follows the correct upstream owner.

⸻

12. Authority and Decision Rights

Principal / Operator

Retains strategic business judgment and authorization reserved to the human or other designated approval principal.

The objective is to minimize human work, not to circumvent existing grant boundaries.

Planner

Retains ownership of strategic objectives, approved priorities and strategic-plan decisions where applicable.

The CTO consumes those decisions and executes within their accepted scope.

GAR in ChatGPT

Retains independent architectural judgment, source inspection, architecture convergence, bounded implementation delegation and acceptance responsibilities.

The CTO can request a GAR decision. It cannot impersonate GAR or generate a self-authenticating GAR approval.

CTO

Owns bounded engineering delivery and the routine technical operating process.

It may select authorized next actions, commission specialists, supervise execution, reconcile facts and continue approved campaigns.

Claude Code

Owns bounded implementation work assigned through the approved coding/execution system.

It cannot grant itself new scope or substitute coder self-review for independent assurance.

Independent assessor

Owns qualified independent assessment of the evidence within its actual mandate.

The CTO may invoke the assessor and consume the result, but must not manufacture a passing assessment.

Existing permission and effect owners

Continue to enforce protected operations at the real execution boundary.

An agent recommendation, model output, LangGraph interrupt response or natural-language message is not independently sufficient authorization.

Delegation model

The CTO should receive a precise standing operational delegation covering routine actions needed to deliver accepted engineering work.

Additional authority is required only when an action exceeds that delegation.

The intended operating model is broad day-to-day autonomy inside a narrowly understood and enforceable authority envelope.

⸻

13. Campaign-Pack Operating Protocol

13.1 Campaign pack as the primary work input

The CTO’s primary workload is an engineering campaign, not an isolated chat prompt.

A campaign pack may contain architecture, contracts, source evidence, target files, acceptance criteria, adversarial tests, runbooks, dependencies and open findings.

The CTO must interpret the pack without silently converting its proposals into accepted authority.

13.2 Campaign intake checks

The CTO first identifies:

* Whether the complete required pack is actually accessible.
* Whether referenced implementation contracts are present.
* Whether the relevant authority is current.
* Whether repository and host permissions exist.
* Whether required execution specialists are available.
* Whether stage dependencies are satisfied.
* Whether a valid next action exists.

Missing implementation inputs must be reported, not invented.

13.3 Native contract production

Where the existing L9 execution system requires a coding contract compiler or GMP scope lock, the CTO invokes that native owner.

It does not replace required compiler products with improvised Markdown instructions.

Generated artifacts must not be hand-edited to bypass owner validation.

13.4 Execution stage behavior

For each permitted stage, the CTO:

1. Establishes the exact current starting state.
2. Selects the authorized operation.
3. Binds the operation to its approved contract and target revision.
4. Invokes the appropriate execution interface.
5. Records the execution identity and acknowledgement.
6. Observes actual outcomes.
7. Obtains required verification.
8. Directs same-scope remediation as needed.
9. Advances only after the stage’s actual acceptance conditions hold.

13.5 Ambiguous outcomes

A worker timeout, missing message or expired lease does not prove that an external effect did not happen.

The CTO must reconcile remote evidence before retrying.

Potentially consequential duplicate execution remains blocked until effect disposition is established.

13.6 Stale evidence

A changed source revision, PR head, merge result, dependency, worker contract or material test environment may invalidate prior acceptance.

The CTO refreshes the affected evidence rather than transferring a previous green result to a new artifact.

13.7 Protected effects

Publication, merging, deployment, credential changes and other protected actions must follow the governing authority and actual effect-gate requirements.

The CTO should prepare the necessary evidence and ask only for the missing authorized decision.

It must not confuse a successful test with permission to perform the protected action.

⸻

14. Reference Workload: L9 Branch Consolidation

The supplied Branch Consolidation playbook is selected as a representative CTO acceptance workload.

It contains complex, dependent execution obligations and known adversarial failure cases.

Stage 0 — Preflight

The CTO binds current upstream and target repository revisions, validates scope, resolves execution contracts and establishes actual host/tool readiness.

It must detect missing trusted-test owners or invalid implementation prerequisites before claiming downstream readiness.

Stage 1 — Upstream semantic work

The CTO supervises a bounded .github semantic change and its required source validation.

Downstream execution waits for actual authorized upstream admission.

Mechanical validation alone is insufficient.

Stage 2 — Cursor-Governance stack safety

The CTO commissions bounded changes across the actual stack-resolution mechanisms and active consumers.

It ensures that default-independent branches and explicitly declared dependencies are handled correctly.

It supervises source-bound tests and independent review.

Stage 3 — Consolidated campaign

The CTO commissions the explicitly approved five-worker campaign.

Workers share one frozen base and produce bounded contributions.

One designated integrator assembles the authorized source, accounts for the complete worker roster, resolves permitted integration failures and regenerates relevant derived outputs.

The CTO coordinates the execution rather than becoming another source-code writer.

Stage 4 — Publication and merge-result assurance

The CTO obtains actual publication results through the existing governed publisher.

It verifies the current PR head, base and merge-result identity.

It coordinates independent protected acceptance. A self-controlled green check is not sufficient evidence of independent behavioral acceptance.

Stage 5 — Rollout proof

Following an authorized merge, the CTO obtains the required actual hosted Claude Code activation evidence, including fresh source and skill consumption.

A simulator or stale session cannot be promoted into runtime completion.

Pack completeness limitation

The campaign’s uploaded root documentation refers to three native contract directories. Their full referenced contract contents were not included in the supplied files reviewed in this conversation.

Therefore the pack is a reference architectural workload here, not automatically a complete runnable delegation.

An operational CTO must detect that distinction.

⸻

15. CO-Pilot Development and Assurance Invariant

The CTO itself is developed and challenged through the CO-Pilot operating structure.

This is separate from the CTO’s eventual runtime role.

GAR

GAR in ChatGPT owns reconnaissance, source-based architectural diagnosis, bounded design decisions, Claude delegation, implementation review and final architectural evaluation.

Claude Code

Claude implements exactly the approved bounded change.

It does not independently assume new architectural authority.

Cursor

Cursor is used for specific missing tests or runtime evidence when GAR explicitly delegates that proof and the necessary environment is available.

It is not a mandatory second coding authority.

Operator

The human currently handles the cross-application handoffs and grants reserved consequential actions.

The eventual CTO may automate operational handoffs only within an explicitly accepted authority and integration design.

Signed CO-Pilot enforcement

The supplied CO-Pilot candidate includes role-separated signed-event and executable gate concepts.

Actual cryptographic enforcement depends on genuine role keys, a trusted policy hash, a trusted runner and mandatory integration at the protected action boundary.

Those conditions have not been demonstrated for this CTO campaign.

No signed gate PASS or independent acceptance receipt is implied by this architecture document.

Review sequence

GAR source reconnaissance → architecture convergence → adversarial break-test → accepted bounded contract → Claude implementation → independent verification → GAR evaluation → next authorized play

The CO-Pilot workflow must preserve real denials and unresolved findings instead of weakening tests to force a positive result.

⸻

16. Security and Operational Safety

16.1 Docker boundary

The container is a constrained CTO process, not unrestricted administrator access to the host.

Initial design excludes broad mounts of the host home directory, raw Docker socket control and unrestricted host credentials.

16.2 Host worker boundary

The Mac-native execution adapter validates the actual request, target, identity, scope, contract and permission independently of the CTO’s reasoning output.

A structured request field is not itself a security sandbox.

16.3 Model output is untrusted for authority

The reasoning model may propose an action.

A deterministic control layer and existing governed execution boundary decide whether the action is authorized.

Prompt text cannot mint new permissions.

16.4 Credentials

Container ingress and model credentials remain separate from host Git and Claude worker credentials.

The CTO should not receive raw credentials that are unnecessary for its operating role.

Secrets must be excluded from prompts, shared task transport, logs and memory records where prohibited.

16.5 One action identity

External operations require stable correlation and retry/reconciliation identities.

The system must distinguish requested, accepted, running, observed, verified and authorized states.

16.6 No duplicate commanders

A campaign must not be simultaneously controlled by independent CTO, legacy PE and Chief-of-Staff execution owners.

Any migration requires deliberate fencing and continuity proof.

16.7 No false completion

The CTO must never report a PR as merged, a deployment as live, a test as run, a memory service as ready or a worker as governed without the corresponding evidence.

⸻

17. Operational Availability

The initial Docker Desktop host is a development and pilot environment.

The CTO will not be continuously available while the Mac is asleep, disconnected or the container is stopped.

Therefore startup recovery and external-effect reconciliation are core requirements, not optional enhancements.

The permanent hosting decision is deferred.

The architecture should avoid depending on Mac-specific semantics within its executive reasoning logic so that future relocation does not require recreating the CTO.

Transport into the Mac-native execution environment is separately selected and proven.

The predecessor candidates are:

* Restricted shared task spool.
* Authenticated loopback host bridge.

Neither is frozen. Selection requires actual security, atomicity, failure and recovery evidence.

⸻

18. Framework and Infrastructure Economy

Selected

* Python.
* LangGraph.
* Docker initial hosting.
* Cursor-Governance existing execution plane.
* Existing Claude execution adapters and coding skills.
* L9 Graphiti Memory.
* Upstream .github bootstrap.

Candidate choices

* Telegram Bot API for operator interaction.
* DeepSeek or another approved model for executive reasoning.
* SQLite-backed LangGraph checkpointing for initial development.
* PostgreSQL for stronger operational persistence when justified.
* Restricted spool or authenticated bridge for Docker-to-Mac transport.
* Optional LangSmith tracing.

Explicitly avoid as initial duplicate infrastructure

* A second agent framework.
* A new generic coding executor.
* Another workflow engine without demonstrated need.
* A competing long-term memory service.
* A duplicate canonical semantic registry.
* A separate unrestricted PR publisher.
* Another universal task scheduler.
* A parallel permission or identity system.
* A second authoritative campaign-state writer.
* A new agent committee pretending to be the CTO.

The principle is not to minimize all dependencies.

It is to maximize leverage from proven capabilities while minimizing new ownership surfaces.

⸻

19. Required Adversarial Tests

The architecture must survive the following classes of failure.

ID	Adversarial condition	Expected behavior
CTO-T01	Unknown or unregistered CTO identity	Bootstrap blocked; no identity substitution
CTO-T02	Upstream authority source unavailable or inconsistent	No consequential operation on invented governance
CTO-T03	Forged or stale authorization	Denied at actual effect boundary
CTO-T04	Campaign pack missing required contracts	Block affected executable stage; report exact missing evidence
CTO-T05	LLM recommends unauthorized repository mutation	Deterministic action gate denies
CTO-T06	Two controllers attempt the same campaign mutation	Only authorized commander may proceed
CTO-T07	Worker completes effect but acknowledgement is lost	Reconcile actual effect before retry
CTO-T08	LangGraph restarts mid-campaign	Resume correctly without blindly repeating external effects
CTO-T09	Memory returns superseded architecture knowledge	Revalidate against current canonical sources
CTO-T10	Unauthorized agent queries CTO-private memory	MemoryService denies
CTO-T11	Unverified worker observation is promoted to shared memory	Admission fails until provenance/authority requirements hold
CTO-T12	Worker claims code passed but required independent review is absent	Evidence reported; acceptance remains blocked
CTO-T13	PR head changes after acceptance	Invalidate affected evidence and rerun required verification
CTO-T14	Container attempts broad host credential/filesystem access	Host isolation denies
CTO-T15	Five successful workers produce broken combined behavior	CTO commissions bounded integration repair and re-verification
CTO-T16	Protected action requires owner grant	LangGraph suspends/escalates; no automatic permission
CTO-T17	Mac restarts while the CTO is active	Recover checkpoint and reconcile real worker state
CTO-T18	Relevant memory capabilities are degraded	Report accurate readiness; obey degraded-operation policy
CTO-T19	CTO receives conflicting strategic and architectural instructions	Route to actual owners; do not self-admit a resolution
CTO-T20	An already completed stage is replayed	Evidence-bound no-op or controlled reconciliation, not duplicate execution

Test names are requirements, not evidence that the tests have been executed.

⸻

20. Implementation Progression

CTO-1A — Source-bound architecture convergence

Resolve actual .github authority, identity requirements, Cursor-Governance active execution owners, and memory integration surfaces.

Identify the smallest new CTO application boundary and the exact reusable existing components.

Complete independent pre-freeze architectural challenge.

Exit: Accepted bounded architecture and source-owner map.

CTO-1B — Runnable LangGraph CTO

Create the minimum Python application running in Docker.

Use a mocked control-plane adapter first.

Demonstrate campaign intake, structured next-action reasoning, conditional routing and accurate reporting.

Exit: Runnable application and deterministic mocked operating cycle.

CTO-1C — Bootstrap and identity

Integrate upstream source-bound identity resolution and governance context using existing owner facilities.

Prove fail-closed behavior for missing or invalid identity.

Exit: Verified runtime identity and governed CTO activation.

CTO-1D — Checkpoints and continuity

Enable durable LangGraph checkpoints and safe campaign resumption.

Prove restart behavior and no blind replay of ambiguous effects.

Exit: Recoverable operating cycle.

CTO-1E — Memory integration

Connect to the existing L9 MemoryService through approved identity, namespaces and APIs.

Prove private/shared access, provenance handling and knowledge retrieval.

Exit: Memory-ready operating loop against the accepted capability profile.

CTO-1F — Real execution-plane integration

Bind a narrow verified Cursor-Governance capability.

Begin with a read-only operation, then a separately authorized bounded execution fixture.

Prove actual worker identity, permissions, effect isolation and receipts.

Exit: CTO can operate a real, governed control-plane path.

CTO-1G — Reference campaign proof

Use the Branch Consolidation campaign, with its required complete inputs and appropriate grants, to prove multi-stage operating judgment, worker supervision, bounded remediation, stale-proof handling and independent acceptance.

Exit: Evidence-backed end-to-end campaign behavior, with protected-action boundaries preserved.

CTO-1H — Operational promotion

Assess actual operator-intervention burden, recovery, availability, security, memory reliability and executive effectiveness.

Promote the CTO to additional campaigns only after satisfying their applicable runtime gates.

Exit: Explicitly accepted operator replacement capability within its authorized scope.

Stages describe architectural progression, not an automatic permission chain. Effectful implementation and publication require the actual applicable grants.

⸻

21. Open Architectural Decisions

The following are not resolved merely by the current conversation.

Identity admission

Does the current upstream registry already support the CTO actor/runtime/surface, or is a new accepted semantic revision necessary?

Exact source placement

Which existing Cursor-Governance owner is the legitimate source home for the CTO application and adapters?

A proposed ops/cto/ directory is not yet an approved placement.

Existing controller integration

Which Program Execution, Peer Execution and continuity capabilities are currently operative, reusable or superseded?

What specific fencing and migration ensure no duplicated command authority?

Control-plane interface

Which existing supported interfaces can the CTO invoke directly?

Which, if any, require a new thin adapter?

Operator delegation

What precise standing authority lets the CTO act autonomously without becoming a human impersonator or self-authorizing principal?

Memory readiness

Which actual L9 memory profile is available, how are private and shared namespaces authorized, and what degraded behavior is allowed?

Reasoning provider

Which model and endpoint meet capability, cost, reliability, privacy and structured-output requirements?

Docker transport

Which of the proposed container-to-host mechanisms satisfies security, race, crash and recovery requirements?

Persistence

What checkpoint backend and backup policy are appropriate for the initial host and future availability requirements?

Independent review

How can the CTO actually invoke the qualified independent assessor when required?

A local reviewer label or worker self-check is insufficient.

Campaign-pack normalization

Which existing native campaign schemas, compilers and contracts can be consumed directly, and what minimal intake normalization is needed?

Deployment and operational availability

When should the CTO move from Mac-local operation to an always-on environment?

Product classification

Whether the CTO ultimately requires formal L9 ProductKind, Node or Gate-routed admission must be decided at the appropriate semantic boundary. It must not be invented by the application.

These open questions should be resolved with current source evidence and adversarial testing, not by speculative infrastructure implementation.

⸻

22. Definition of Done

The CTO architecture will have demonstrated its primary objective when:

1. The CTO boots using real upstream-derived identity and governance bindings.
2. It has verified access to its intended execution and memory capabilities.
3. It receives a complete, valid campaign pack.
4. It independently decides the correct next authorized operation.
5. It operates the existing Cursor-Governance control plane.
6. It supervises delegated workers and consumes actual results.
7. It recovers from interruption and reconciles ambiguous effects correctly.
8. It obtains the required independent acceptance.
9. It avoids routine requests for the operator to perform technical relay work.
10. It escalates only matters outside delegated authority.
11. It preserves accurate status and durable lessons.
12. It reports a verifiable final outcome rather than merely claiming completion.

Primary performance measures

* Avoidable operator relays per accepted campaign.
* Verified completion rate.
* Time lost to manual handoffs.
* Recovery success after interruption.
* Duplicate consequential effects.
* Unauthorized action attempts successfully denied.
* False-positive completion or acceptance claims.
* Quality and relevance of escalations.
* Reuse of existing execution capabilities versus new components.
* Accuracy and utility of retained operational knowledge.

The desired steady state is that the operator delegates outcomes rather than performing execution steps.

⸻

23. Evidence and Admission Status

This document consolidates:

* The CO-Pilot skill contract and operating discussion.
* The two Igorbot CTO predecessor packs.
* The standalone Docker CTO semantic proposal.
* The candidate’s architecture expression, provenance and validation artifacts.
* The Branch Consolidation campaign playbook.
* The subsequent conversational decisions selecting LangGraph, unified CTO operational responsibility, Cursor-Governance reuse, L9 memory integration and upstream identity bootstrap.

It does not assert that historical source revisions remain current.

It does not constitute a producer-validated AuthorityResolution receipt, semantic compiler product, independent architecture break-test result, implementation authorization, signed CO-Pilot ledger or runtime acceptance report.

No code mutation, Docker deployment, live memory integration, LangGraph execution or CTO identity admission is established by this document.

Current architectural verdict

CONVERGED DIRECTION / PRE-FREEZE IMPLEMENTATION DESIGN

The mission, primary ownership boundaries, runtime direction and core framework choices are sufficiently established to guide source-bound architectural convergence.

The precise implementation must still be resolved against existing canonical owners and tested before admission.

⸻

24. Single Next Play

CTO-01 — Source-bound capability and ownership convergence

GAR should independently inspect the current .github, Cursor-Governance and l9-graphiti-memory source authorities.

The mission is to produce one exact-revision architecture map answering:

Which existing components can operate the CTO, which responsibilities must be consolidated, which minimal new executive capability is needed, and what identity, permission, memory and execution boundaries must be proven?

The result should include:

* Canonical authority and identity coordinates.
* Existing execution-plane capability inventory.
* Reuse / extend / replace / new / defer classification.
* Unified CTO command and continuity ownership.
* LangGraph integration boundary.
* Memory integration contract.
* Docker/host trust boundary.
* Bounded implementation sequence.
* Adversarial architecture findings.
* Unresolved decisions and exact owners.

Only after the architecture is accepted should GAR produce the first bounded Claude Code implementation contract.

No additional general-purpose platform is authorized by this decision.

⸻

25. Governing Design Principle

The CTO is the autonomous technical operator of L9.

It derives identity and governance from .github, reasons and maintains operating continuity through LangGraph, learns through L9 Graphiti Memory, and executes through the existing Cursor-Governance control plane.

It assumes the routine engineering operating responsibilities previously performed by the human and separately coordinated through Chief of Staff, Peer Execution and WorkState.

It does not replace canonical strategy, architectural authority, independent assurance or permissions reserved to their legitimate owners.

Its mandate is to turn accepted engineering campaigns into completed, verified outcomes while minimizing human keyboard intervention.


CTO-004 — Proven execution first. The CTO must use the existing l9-coding-agent capability as its preferred coding executor, through verified native contracts and host controls. Program Execution and Peer Execution are not assumed operationally proven, cannot be critical-path dependencies by default, and may be incorporated only after their specific capabilities demonstrate independent runtime reliability and a genuine advantage over direct coding-agent delegation.
