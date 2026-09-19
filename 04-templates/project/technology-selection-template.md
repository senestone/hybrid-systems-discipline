<!--
File: 04-templates/project/technology-selection-template.md

Purpose:
  Record the evidence, alternatives, rationale, and lifecycle impact behind
  implementation technology choices.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Technology Selection Record

Project:
Decision ID:
Status: Proposed / Approved / Superseded
Date:
Owner:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Lifecycle phase:
Related decision-log entry (ID and link):
Requirements version:
Architecture version:
Detailed Design version:
RTM version:

Use `Not yet available` with a reason for downstream artifact versions that do not exist in the current phase. Replace these before approval for implementation.

---

## 1. Decision Boundary

State the specific choice under review: language, runtime, storage adapter, build tool, framework, deployment technology, or another bounded concern. State what this decision does not select. Identify the approved phase gate that permits the choice and any unresolved prerequisite.

Evidence gathering may begin earlier, but a Proposed record is not an implementation baseline. Apply the current phase guardrail to any prototype or candidate discussion. Approve a material implementation choice only after the Test Planning to Implementation gate, when the approved requirements, architecture, design, RTM, and test mapping support it. A requirement-mandated choice made earlier still needs the applicable phase approval and impact review.

Do not treat a prototype, a default tool preference, or an available dependency as approval. If the choice changes an approved requirement, architecture boundary, or design contract, return to the earliest affected phase under change control.

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

Include failure and rollback behavior, clean build, runtime dependencies, portability, and applicable Requirement IDs. Add Test Case IDs once Test Planning defines them. State which criteria remain untested. A successful narrow prototype does not establish system-wide conformance.

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
