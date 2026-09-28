<!--
File: 04-templates/project/technology-selection-template.md

Purpose:
  Record the evidence, alternatives, rationale, staged approval, and lifecycle
  impact behind material technology choices.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Technology Selection Record

Project:
Decision ID:
Status: Hypothesis / Candidate / Under Investigation / Provisional Architectural Baseline / Approved for Detailed Design / Approved for Implementation / Locked for Release / Superseded
Date:
Owner:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Lifecycle phase:
Related decision-log entry (ID and link):
Requirements version:
Architecture version:
Detailed Design version:
RTM version:
Glossary version:
Risk Register version:
Related Change ID(s):

Use `Not yet available` with a reason for downstream artifact versions that do not exist in the current phase. Resolve each reference before the status that depends on it.

---

## 1. Decision Boundary

State the specific choice under review: language, runtime, storage adapter, build tool, framework, deployment technology, or another bounded concern. State what this decision does not select. Identify the approved phase gate that permits the choice and any unresolved prerequisite.

Evidence gathering may begin in any authorized phase, but a Hypothesis, Candidate, or Under Investigation record is not a baseline. Apply the current phase guardrail to every prototype or candidate discussion.

Use lifecycle-aware status deliberately:

| Status | Meaning and Earliest Use |
|--------|--------------------------|
| Hypothesis | A possible option or claim identified during authorized exploration; no selection implied. |
| Candidate | An option admitted for comparative evaluation after relevant constraints are known. |
| Under Investigation | Evidence gathering or a bounded prototype is active; production use is not authorized. |
| Provisional Architectural Baseline | Human-approved for a stated architectural dependency or constraint; unresolved evidence and rollback triggers remain explicit. |
| Approved for Detailed Design | Human-approved for design reliance after affected requirements and architecture are approved. |
| Approved for Implementation | Human-approved for production adoption no earlier than the Test Planning to Implementation gate and before implementation use. |
| Locked for Release | The selected version and configuration are included in the release baseline; change requires formal impact assessment. |
| Superseded | Replaced by a linked decision; historical rationale and evidence are retained. |

A status SHALL NOT authorize work outside the current lifecycle phase. Earlier baseline status is permitted only when the choice is necessary to complete that phase and the applicable authority approves its stated scope, evidence, uncertainty, and rollback triggers.

Do not treat a prototype, a default tool preference, or an available dependency as production approval. Prototype and spike outputs are non-production evidence unless the governed implementation is separately approved and traced. If the choice changes an approved requirement, architecture boundary, or design contract, return to the earliest affected phase under change control.

## 2. Drivers and Constraints

| Driver | Authoritative reference | Required behavior or quality | How it will be evaluated |
|---|---|---|---|
| | Requirement / NFR / design section | | Test, measurement, review, or prototype |

Record target users, deployment assumptions, portability needs, data ownership, trust boundaries, interoperability, performance, maintainability, cost, licensing, and team capability only where they affect this choice. Label assumptions and provisional targets explicitly.

## 3. Candidate Options

Include the incumbent or a no-new-technology option where meaningful. Use the same criteria for every candidate.

| Candidate | Meets required constraints? | Evidence | Strengths | Costs and risks |
|---|---|---|---|---|
| | Yes / No / Unknown | Source or experiment reference | | |

Distinguish verified behavior from documentation claims and inference. Link directly to the supporting source, test result, or experiment. Record rejected options and the reason each was rejected.

## 4. Prototype and Measurement Evidence

| Question | Method and environment | Result | Limitations |
|---|---|---|---|
| | Reproducible command, fixture, hardware, and version | | |

Include failure and rollback behavior, clean build, runtime dependencies, portability, and applicable Requirement IDs. Add Verification Case IDs, methods, and applicable Test Case IDs once Test Planning defines them. State which criteria remain unverified. A successful narrow prototype does not establish system-wide conformance.

## 5. Decision and Rationale

Selected option:
Approval status and approver:
Approval date:
Decision-log entry (ID and link):

Explain why this option best satisfies the drivers, what it costs, and why the alternatives are less suitable for this scope. If no option is yet approved, leave the selection pending and name the evidence or owner decision needed next.

## 6. Architecture and Traceability Impact

| Artifact or boundary | Impact | Required update or validation |
|---|---|---|
| Requirements / RTM | | |
| Architecture / Detailed Design | | |
| Implementation / tests | | |
| Packaging / orchestration / documentation | | |

Declare whether any phase rollback, RTM revision, or renewed human authorization is required. Preserve technology-neutral contracts where the approved design requires them.

## 7. Residual Risks and Revisit Triggers

| Risk or assumption | Mitigation or monitoring | Trigger for reconsideration | Owner |
|---|---|---|---|
| | | | |

Record migration or exit cost, dependency support posture, and the consequences if the selected technology proves unsuitable. Link any superseding decision to this record.

## 8. Review

- [ ] Required constraints and authoritative references identified.
- [ ] Alternatives evaluated against the same criteria.
- [ ] Evidence is reproducible and limitations are explicit.
- [ ] Rejected alternatives and residual risks are recorded.
- [ ] RTM, design, test, packaging, and orchestration impact assessed.
- [ ] Required phase gate and human approval recorded before use as an approved baseline.

Use the [technology selection review checklist](technology-selection-review-checklist.md) for a focused review and record the final decision in the [project decision log](decision-log-template.md).
