<!--
File: 04-templates/project/change-impact-assessment-template.md

Purpose:
  Provide a governed record of a proposed change, its lifecycle-wide
  impacts, required rollback point, verification needs, and authorization.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

Assessment does not authorize a change.
Material change without assessment and human authorization is prohibited.
-->

# Change Proposal and Impact Assessment

Project Name:
Change ID: CHG-XXX
Title:
Date (YYYY-MM-DD):
Prepared By:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, collaborators, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Proposed / Under Review / Approved / Rejected / Implemented / Verified / Closed / Superseded
Current Lifecycle Phase:
Target Release or Milestone:
Decision Log Reference:
RTM Version Reference:
Risk Register Version Reference:
Glossary Version Reference:

---

# 1. Applicability and Authority

Create an assessment before authorizing a change that may affect:

- Approved scope or requirements
- Architecture or system boundaries
- Detailed design or interface contracts
- Deterministic-probabilistic boundaries
- Implementation behavior
- Test scope, acceptance criteria, or evidence
- Packaging, orchestration, deployment, or operations
- Security, privacy, compliance, or data handling
- User, administrator, or support documentation
- Controlled terminology

Purely editorial changes with no semantic, behavioral, traceability, operational, or approval impact MAY be exempt. Record the exemption rationale when materiality is uncertain.

This assessment identifies required action. It does not replace a Decision Log entry, phase-gate approval, RTM update, or accountable human authorization.

---

# 2. Change Summary

Document:

- Requested change
- Reason for change
- Request source
- Problem, defect, opportunity, or obligation addressed
- Current behavior or state
- Proposed behavior or state
- Explicit exclusions
- Urgency and desired completion date

Change scope SHALL be specific enough to assess without inferring unstated intent.

---

# 3. Classification

Change Type:

- Corrective
- Adaptive
- Perfective
- Preventive
- Security or Compliance
- Documentation
- Emergency

Materiality:

- Minor: no approved behavioral or structural contract changes
- Material: affects one or more approved artifacts or validation obligations
- Critical: affects safety, security, compliance, data integrity, release integrity, or deterministic-probabilistic containment

Priority: Low / Moderate / High / Critical

Emergency handling SHALL NOT eliminate retrospective assessment, traceability, testing, or approval obligations.

---

# 4. Lifecycle Impact Matrix

| Area | Impacted? | Artifact or ID References | Required Update | Owner | Status |
|------|-----------|---------------------------|-----------------|-------|--------|
| Project Primer / Scope | Yes / No | | | | |
| Requirements | Yes / No | | | | |
| High-Level Architecture | Yes / No | | | | |
| Detailed Design | Yes / No | | | | |
| Interfaces / Data | Yes / No | | | | |
| Implementation | Yes / No | | | | |
| Test Plan / Test Cases | Yes / No | | | | |
| RTM | Yes / No | | | | |
| Packaging / Orchestration | Yes / No | | | | |
| Operations / Monitoring | Yes / No | | | | |
| Security / Privacy / Compliance | Yes / No | | | | |
| System Documentation | Yes / No | | | | |
| Project Glossary | Yes / No | | | | |
| Project Risk Register | Yes / No | | | | |

Every "No" for a plausibly affected area SHALL be defensible from available evidence.

---

# 5. Traceability and Rollback Determination

Record:

- Requirement IDs affected
- Architecture component IDs affected
- Detailed Design references affected
- Implementation units affected
- Verification Case IDs, methods, Test Case IDs, and Validation Scenario IDs affected
- Packaging and orchestration references affected
- Documentation deliverables affected
- Risk IDs affected or created
- Earliest lifecycle phase affected
- Required rollback phase
- Phase gates requiring re-evaluation

The lifecycle SHALL return to the earliest affected phase. A later-phase approval cannot waive an earlier affected phase without explicit human authorization under the lifecycle bootstrap.

---

# 6. Deterministic-Probabilistic Boundary Impact (If Applicable)

Assess:

- Boundary placement or invocation contract
- Validation and acceptance logic
- Fallback or degradation behavior
- Deterministic state protection
- Observability and audit evidence
- Model, prompt, data, threshold, or configuration changes
- Drift detection and reproducibility

Boundary impact that cannot be bounded SHALL block authorization.

---

# 7. Risk and Trade-Off Assessment

| Risk ID | Description | Likelihood | Impact | Mitigation | Residual Rating | Owner |
|---------|-------------|------------|--------|------------|-----------------|-------|

Document:

- Benefits expected
- New risks introduced
- Existing risks changed
- Assumptions relied upon
- Dependencies and coordination needs
- Consequences of making the change
- Consequences of not making the change
- Revisit or abort triggers

New or changed risks SHALL be reflected in the active Project Risk Register.

---

# 8. Verification and Evidence Plan

Define:

- Acceptance criteria
- Test cases to add, revise, rerun, or retire
- Non-functional verification required
- Regression scope
- Clean-environment or packaging verification
- Operational or documentation verification
- Evidence to retain
- Verification and Validation Report reference to be produced

No material change is complete until its acceptance criteria are verified and linked evidence is available.

---

# 9. Implementation and Recovery Plan

Document:

- Planned implementation sequence
- Dependencies and prerequisites
- Data migration or compatibility steps
- Deployment or rollout controls
- Monitoring during introduction
- Rollback criteria
- Rollback procedure
- Recovery verification
- Communication obligations

Irreversible steps SHALL be identified before authorization.

---

# 10. Authorization

Assessment Reviewed By:
Decision: Approved / Rejected / Deferred / More Information Required
Decision Log Entry:
Authorized Rollback Phase:
Conditions of Approval:
Approved By:
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:
Date:

Approval authorizes the bounded change and required lifecycle rework only. It does not authorize phase advancement or release.

---

# 11. Closure

Complete after implementation and verification:

- Implemented artifact/version references
- Verification and Validation Report reference
- RTM version updated
- Risk Register version updated
- Glossary version updated
- Documentation version updated
- Deviations from approved assessment
- Residual risks accepted by accountable human authority
- Closure decision
- Closed By
- Closure Date

Unverified or incompletely traced changes SHALL remain open.

---

End of Change Proposal and Impact Assessment Template
