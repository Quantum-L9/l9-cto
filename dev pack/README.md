# v1.1 | Authority + AgentPod decision lock (2026-10-14)

**LOCKED as design:** Source repository remains `Quantum-L9/Cursor-Governance` (no new CTO repository). Mac host transport is **AgentPod Hub MCP → enrolled macOS `apn` node → authorized runtime station**. Preferred workers are Cursor CLI **ACP** (needs new AgentPod descriptor/proof) and Claude Code (existing AgentPod harness, L9 project-policy equivalence must be proven). `apn` is a local node daemon, **not** the CTO client. An enrolled machine credential is **not** CTO authority. For agent automation use an appropriately scoped Hub agent principal/MCP entrypoint. No privileged generic AgentPod terminal or broad file-write capability for CTO.

**LOCKED as authority division:** `l9-authority-resolver` resolves current applicable `.github` semantics and immutable coordinates; `Cursor-Governance/autonomy/runtime/` with `AdapterOrchestrator` is the **single existing enforcement owner** for campaign leases, roles, capability decisions, claims, receipt records and human-protected effects; AgentPod is transport, not L9 authorization. The CTO is a coordinator, not a role with free-standing code-write/merge rights. Workers obtain separate action-specific leases and native code contracts. The host MUST independently verify effective authorization at effect time. No new CTO policy ledger, scheduler, shadow publisher, runtime grant or repository.

**STILL NOT PROVEN:** canonical CTO actor/surface admission, producer-validated identity projection/resolution receipt, operating binding, AgentPod principal/MCP grants, native Cursor station descriptor, ACP hook conformance, APN host-side L9 gateway/revocation mediation, durable operation journal and replay safety, OS identity isolation, actual Mac canaries, memory principal and independent completion. All live effect gates remain blocked until demonstrated. See `docs/12_RISK_UNKNOWN_AND_DECISION_REGISTER.md` and `machine/decision_register.yaml`.

**Version precedence:** This v1.1 statement plus revised chapters supersedes *only* earlier generic-host-transport and SDK-only default assumptions. Original source annexes remain byte-identical and historical. F1 remains mock-only, with the same five admitted prospective files. No real execution or upstream mutation is granted by this developer pack.

# L9 CTO | Architecture & Build Developer Pack

**Pack:** CTO-DEV-PACK-001 · **Date:** 2026-10-14 · **Edition:** 1.1 (decision-lock update) · **Disposition:** DEVELOPMENT SPECIFICATION, NOT AN EXECUTION GRANT

**Mission:** Build a functioning standalone L9 technical executive that conducts routine engineering campaigns on the existing Cursor-Governance control plane. The CTO decides, delegates, supervises, reconciles and verifies. It does not impersonate actors, duplicate the control plane, mint its own permissions or self-certify success.

## Read this first

1. `docs/00_EXECUTIVE_CONTRACT.md` for operator intent, frozen decisions, non-goals, operational definition of done.
2. `docs/01_SOURCE_AUTHORITY_AND_FACTS.md` for source revisions, provenance and what is **not proven**.
3. `docs/02_SYSTEM_ARCHITECTURE.md` for trust boundaries, components, flows and authority ownership.
4. `docs/03_BOOTSTRAP_AND_READINESS.md` for CTO-BOOTSTRAP-001 and CTO-READY-001, their deterministic acceptance gates and revalidation.
5. `docs/04_CAMPAIGN_AND_STATE_MACHINE.md` + `docs/05_HOST_WORKER_PORT_AND_EFFECTS.md` for operational behavior, AgentPod-selected host transport, exact failure semantics, and unfinished host enforcement.
6. `docs/06_MEMORY_SECURITY_AND_PERMISSIONS.md` for memory, secrets, host isolation and prohibited actions.
7. `docs/07_LOCKED_FILETREE.md` for REUSE / EXTEND / NEW / CONDITIONAL / DEFER dispositions and justification per file.
8. `docs/08_WORK_PACKAGES_AND_DEPENDENCIES.md` and `machine/work_items.json` for granular implementation and parallel work admission.
9. `docs/09_ACCEPTANCE_AND_NEGATIVE_TESTS.md` and `machine/acceptance_tests.json` for testable GO / NO-GO.
10. `docs/10_OPERATOR_RUNBOOK.md`, `docs/11_REFERENCE_CAMPAIGN.md` and `docs/12_RISK_UNKNOWN_AND_DECISION_REGISTER.md` for deployment, first real workload and unknown ownership.
11. `handoffs/CLAUDE_CODE_BOUND_DELEGATION.md` for an implementation-ready contract with **no automatic permission to write, publish, merge or deploy**.
12. `docs/13_TRACEABILITY_AND_COVERAGE.md` for claim-to-source and claim-to-test closure.

`CTO_MASTER_SPEC.md` is a single-file combined rendering of the developer documents. `sources/` contains the exact available original design/recon/filetree artifacts. `machine/` is the reviewable, structured projection of the same proposed implementation plan, not an admitted upstream L9 semantic schema. `validation/` contains local consistency reports, digests, and limitations.

## Pinned inspected baselines

- `Quantum-L9/.github` `d4397e53f8f4c23458a80f87db9552463ad9e26f`
- `Quantum-L9/Cursor-Governance` `4cc0d7dc858021bc8e2a95a904e2945fd3d3acba` (original historical recon); **later reviewed main** `0bb60d78f8bdc22d09bd8464830cdfa62d61d0ed`
- `Quantum-L9/l9-graphiti-memory` `441b741e31a7bb5a57849e5b49b97465b1c7ee58`

The initial three were current `main` heads when independently rechecked during v1.0 creation. v1.1 separately rechecked the revised source seams; source history is not rewritten. **No Mac runtime, live Docker/host bridge, model invocation, signed canonical projection, or end-to-end code execution was proved.** The file tree's content is a design commitment for later delegated implementation, not evidence that its new files exist.

## Non-negotiable stop conditions

- A missing canonical CTO actor/surface or verified identity assertion stops consequential CTO operation.
- No real coding worker launch until an independently enforceable permission boundary, worker adapter and durable operation journal have been verified.
- A completed LangGraph node or worker-reported `success` is not independent evidence that an external effect occurred or passed acceptance.
- Merge authority requires a live human-issued exact-PR/head grant. The CTO and its worker must not issue one.
- No Program Execution dependency, Igorbot/OpenClaw dependency, parallel publisher, second long-term memory, general worker scheduler or general control plane.
- Any authority, transport or new schema requiring upstream admission must be processed by its owning authority outside this implementation pack.

## Assurance language

- **DESIGNED**: represented in this pack; not installed.
- **SOURCE-OBSERVED**: inspected at the pinned exact repository revision; not runtime-proven.
- **PROVED IN TEST**: actual recorded execution on an exact implementation commit and environment.
- **LIVE-PROVED**: actual host/worker effect plus independently observed result.
- **ADMITTED**: separately authorized by the applicable canonical/effect owner.

Never translate DESIGNED or SOURCE-OBSERVED into READY, LIVE-PROVED or ADMITTED.

## Status and source limitations

The available source is the attached CTO design (October 13), appended October 14 reconnaissance/design conversation document, source-inspected recon and the explicitly locked filetree plus the visible user decisions in this chat. A complete independently exported chronological original conversation is **not** available, nor are the Branch Consolidation playbook's referenced three native contract directories. Architectural semantic expression coverage therefore remains **partial**, and the pack makes **no claim of independent original-chat completeness or canonical semantic compilation**.
