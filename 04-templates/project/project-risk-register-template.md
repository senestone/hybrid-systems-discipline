<!--
File: 04-templates/project/project-risk-register-template.md

Purpose:
  Provide a lifecycle-wide register for risks, assumptions, issues,
  and dependencies that may affect governed project outcomes.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

Risk visibility does not constitute risk acceptance.
Only accountable human authority may accept residual risk.
-->

# Project Risk Register

Project Name:
Version:
Date (YYYY-MM-DD):
Maintained By:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, collaborators, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Draft / Active / Approved / Archived
Current Lifecycle Phase:
RTM Version Reference:
Decision Log Version Reference:
Glossary Version Reference:

---

# 1. Register Authority and Scope

This register is the authoritative project-level index for:

- Risks: uncertain events or conditions that may affect objectives
- Assumptions: statements treated as true but requiring validation
- Issues: realized conditions requiring action
- Dependencies: external or internal prerequisites outside the item's direct control

Artifact-specific risk sections SHALL link to this register when the risk persists beyond that artifact or affects more than one lifecycle area.

Recording a risk does not accept it. Residual risk acceptance requires accountable human authority.

---

# 2. Rating Method

Define the project rating method before scoring items.

## Likelihood

| Score | Label | Project Definition |
|-------|-------|--------------------|
| 1 | Rare | |
| 2 | Unlikely | |
| 3 | Possible | |
| 4 | Likely | |
| 5 | Almost Certain | |

## Impact

| Score | Label | Project Definition |
|-------|-------|--------------------|
| 1 | Negligible | |
| 2 | Minor | |
| 3 | Moderate | |
| 4 | Major | |
| 5 | Severe | |

Risk Score = Likelihood x Impact

| Score Range | Rating | Required Posture |
|-------------|--------|------------------|
| 1-4 | Low | Monitor |
| 5-9 | Moderate | Assign mitigation and review at affected gates |
| 10-16 | High | Active treatment and explicit gate review |
| 17-25 | Critical | Block affected advancement unless reduced or explicitly accepted by authorized human authority |

Projects MAY use another documented method. Scales SHALL NOT change silently between versions.

---

# 3. Register

| Item ID | Type | Title | Lifecycle Area | Related IDs | Likelihood | Impact | Score / Rating | Response | Owner | Trigger / Due Date | Status |
|---------|------|-------|----------------|-------------|------------|--------|----------------|----------|-------|--------------------|--------|
| RSK-001 | Risk | | | | | | | | | | Open |

Allowed Type values: Risk / Assumption / Issue / Dependency

Allowed Status values: Proposed / Open / Monitoring / Mitigating / Escalated / Accepted / Realized / Resolved / Closed / Superseded

Each item SHALL have a stable ID. Closed and superseded IDs SHALL NOT be reused.

---

# 4. Item Detail

Repeat this section for each item requiring more context than the register row provides.

## Item ID: RSK-XXX

Type:
Title:
Description:
Date Identified:
Identified By:
Lifecycle Phase Identified:
Category: Scope / Schedule / Architecture / Data / Security / Privacy / Compliance / Technology / Dependency / Test / Packaging / Operations / Documentation / Other
Related Requirement IDs:
Related Architecture or Design IDs:
Related Change IDs:
Related Decision Log Entries:

### Cause, Event, and Consequence

Cause:
Event or Condition:
Potential Consequence:

Risk statements SHOULD distinguish the uncertain condition from its consequence.

### Rating

Initial Likelihood:
Initial Impact:
Initial Score / Rating:
Confidence in Assessment: Low / Moderate / High
Assessment Basis:

### Response

Strategy: Avoid / Reduce / Transfer / Accept / Exploit / Share / Monitor / Resolve
Preventive Actions:
Contingency Actions:
Trigger or Early Warning:
Action Owner:
Target Date:
Required Resources or Dependencies:

### Residual Exposure

Residual Likelihood:
Residual Impact:
Residual Score / Rating:
Monitoring Method:
Review Frequency:

### Resolution or Acceptance

Outcome:
Evidence Reference:
Accepted or Closed By:
Approval accountability: Human/organizational authority only; AI tools must not accept residual risk or close an item as an approval authority.
Role:
Date:
Rationale:

---

# 5. Lifecycle Review

Review the register:

- At every phase gate
- When scope, requirements, architecture, design, implementation, test, packaging, or operations change materially
- When an assumption is validated or invalidated
- When a dependency changes
- When an issue is realized or resolved
- Before release authorization

At each review, confirm:

- New items captured
- Ratings remain current
- Owners and dates remain valid
- Mitigations have evidence
- Realized risks converted to issues
- Invalidated assumptions trigger impact assessment
- High and Critical items are visible to gate authorities
- Closed items include closure evidence

---

# 6. Aggregate Risk Posture

Open Low Items:
Open Moderate Items:
Open High Items:
Open Critical Items:
Overdue Actions:
Unvalidated Assumptions:
Blocked Dependencies:
Open Issues:

Overall Project Risk Posture: Low / Moderate / High / Critical

Summary and trend:

The aggregate rating SHALL NOT hide a Critical item or substitute for item-level review.

---

# 7. Change History

| Version | Date | Change Summary | Item IDs Affected | Maintained By | Approval Reference |
|---------|------|----------------|-------------------|---------------|--------------------|

Material rating, response, ownership, acceptance, or closure changes SHALL preserve lineage.

---

# 8. Approval

Reviewed By:
Approved By:
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:
Date:
Version Incremented: Yes / No

Approval confirms review of the register state. It does not imply acceptance of every listed risk unless acceptance is explicitly recorded at item level.

---

End of Project Risk Register Template
