# 13 | Two-way architecture, source and implementation traceability

## 13.1 Provenance model

`SOURCE`: original CTO charter and appended design/recon documents in `sources/`; exact user-converged decisions in visible conversation; direct pinned repository facts listed in `docs/01_SOURCE_AUTHORITY_AND_FACTS.md`. `DESIGN`: chapters 00–12. `REALIZATION`: WP-00–WP-16, locked filetree paths. `PROOF`: BT/CP/IO/RC/MS/PB test families. `UNKNOWN`: U-01–U-20.

**Completeness limitation:** source documents and current visible conversation decisions are available, but not a independently bounded full original conversation export, so no original-chat 100% coverage claim is made. The captured design represents the materially converged *available* evidence and explicitly marks source deficits.

## 13.2 Forward mapping

| Source commitment | Architecture chapter | Work package | Proof |
|---|---|---|---|
| CTO-D001 executive role | 00,02,04 | WP-01/02/12 | CP-001–012, PB-010 |
| CTO-D002 Mac Docker Python | 02,07,10 | WP-02/04/15 | RC-002, MS-008 |
| CTO-D003 no Igorbot/OpenClaw | 00,07 | WP-00/16 | prohibited import/dependency check |
| CTO-D004 upstream canonical authority | 01,03 | WP-05 | BT-002–005 |
| CTO-D005 LangGraph, durable continuation | 02,04 | WP-01/02 | RC-001–010 |
| CTO-D006 existing root autonomy/SDK/coding contract | 05,07 | WP-07–12 | CP-003, IO-001–016 |
| CTO-D007 governed L9 memory | 06 | WP-06/11 | MS-001–012 |
| CTO-D008 distinct CTO actor | 03,06 | WP-05/06 | BT-002/003/010 |
| CTO-D009 CTO service-native bootstrap | 03 | WP-02/05/06 | BT-001–014 |
| CTO-D010 no false READY | 03,09 | WP-02/03/08/09 | BT-001, BT-006, IO-008 |
| CTO-D011 one campaign/worker | 00,04 | WP-01/12 | CP-004, BT-012 |
| CTO-D012 stable operation and reconciliation | 04,05 | WP-08/10/15 | IO-002–006, RC-003–010 |
| CTO-D013 protected human grants | 05,06,10 | WP-09/13 | PB-002–005, MS-009 |
| CTO-D014 consolidate active operational coordination | 02,04 | WP-12/15/16 | BT-012, owner-fencing review |
| CTO-D015 Branch Consolidation | 11 | WP-14 | CP-010, PB-006–010 |
| CTO-D016 minimal files/owner reuse | 07 | all work packages | file delta+owner proof |
| CTO-D017 recon→filetree→code | 01,07,08 | WP-00 | source census, confirmed filetree |
| CTO-D018 CO-Pilot independent assurance | 08,09 | WP-00–16 | independent assessor receipts |

## 13.3 Reverse mapping requirements

A downstream implementation review must account for **every** changed file: linked WP, original accepted obligation, upstream owner or scoped authorization, declared tests and evidence. Unlinked files are not automatically legitimate. Every test must point to a protected failure class or positive accepted outcome; tests inventing features outside the architecture must not widen the scope. Every new semantic/identity identifier must trace to admitted canonical owner or be marked unresolved, not copied into generated files.

## 13.4 Verification report template

```text
subject: CTO implementation commit <40-hex>
source: .github canonical <sha>, CG <sha>, memory <sha>
architecture: CTO-DEV-PACK-001 / frozen decisions
scope: exact changed paths and native contracts
work_packages: named WP ids
passed_tests: actually executed test receipts, not plans
failed_tests: named failures and known prior baselines
not_run: live Mac/host/CI/MemoryService unavailable tests
identity: source-resolved/current or BLOCKED with owner
worker: source-only/mock-only/live-canaried with evidence
recovery: actual op ids, spawn counts, checkpoint/journal refs
external_effects: independent GitHub/CI/worktree observations
protected: human grant reference, or MERGE_PENDING
acceptance: independent owner and exact receipt, or NOT_PROVEN
unknowns: all material U ids still unresolved
```

## 13.5 Explicit assurance ceilings

- This pack's artifact checksum confirms internal file integrity, not correctness against the unseen full chat.
- Source inspection confirms code exists at a pinned revision, not that it runs on the Mac.
- Existing tests observed in source are not tests executed in this production environment.
- Composer-produced machine JSON is a planning aid, not canonical source or a granted execution contract.
- If a developer invents a local CTO permission by adding optional fields to a locked contract, the implementation fails architectural fidelity even if its tests pass.

## 13.6 Audit cadence

At each phase close: test source→design→file/work item→receipt mapping; challenge unexplained files, false ready statuses, accepted-but-unverified effects, stale authority, missing negative cases and accidental scope expansion. Require evidence-based closure of in-scope defects without regressing frozen decisions. Reconstruct from donor independently before making a *full-original-source* coverage claim.

## v1.1 | Added operator-lock traceability and remaining limits

| User-visible operator commitment | Decision | Source owner | Work package | Planned tests |
|---|---|---|---|---|
| AgentPod selected, no custom generic host bridge | CTO-D019 | AgentPod Hub/node, CG adapter | WP-07/08/10 | IO-017–024 |
| Cursor to be controlled via APN as agent/API | CTO-D022 | Cursor official ACP, AgentPod descriptor | WP-17/09 | IO-019, IO-020, IO-025 |
| Authority Resolver skill and existing autonomy reused | CTO-D020/021 | `.github` resolver, `autonomy/runtime`, `autonomy/adapters` | WP-05/06/18 | BT-015–018, IO-026 |
| Separate host L9 gate and no privileged terminal | CTO-D024 | Root autonomy and AgentPod provider | WP-18 | IO-017/018/025/026, PB-011 |
| No new CTO repository, no owner duplication | CTO-D023 | Cursor-Governance/AgentPod separate authority | WP-00/16/17 | file/permission census |

**Source-completeness qualification unchanged:** this visible user-turn capture is partial, not a provenance-certified complete original conversation. `capture.yaml` and the candidate expression reflect only the new visible decisions; derived artifacts do not grant canonical authority or successful test results.
