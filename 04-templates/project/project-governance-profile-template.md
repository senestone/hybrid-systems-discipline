<!--
File: 04-templates/project/project-governance-profile-template.md

Purpose:
  Define the governed increment, proportional governance profile,
  human decision rights, tailoring decisions, and evidence obligations.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Project Governance Profile

Project Name:
Governed Increment ID:
Increment Name:
Increment Type: Product / Release / Capability / Feature Set / Change / Architectural Increment / Other
Profile Version:
Status: Draft / Approved / Superseded
Effective Date (YYYY-MM-DD):
Prepared By:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Project Primer Version Reference:
Risk Register Version Reference:
Glossary Version Reference:
Related Change ID(s):
Supersedes Profile Version:

---

# 1. Governed Increment

Define the bounded body of work governed by this lifecycle instance:

- Intended outcome
- Included scope and Requirement ID range, when available
- Explicit exclusions
- Product or system baseline affected
- Planned release, deployment, or decision boundary
- Dependencies on other increments
- Conditions that require a new increment or formal scope change

The increment SHALL be coherent enough to baseline, trace, verify, validate, release or otherwise disposition, and transfer to an operational owner where applicable.

Future product scope outside this increment need not be fully specified. It SHALL NOT be introduced into this increment without change control.

---

# 2. Risk-Based Profile Assessment

| Factor | Rating | Rationale and Evidence | Related Risk or Requirement IDs |
|--------|--------|------------------------|---------------------------------|
| Safety impact | Low / Moderate / High / N/A / Unknown | | |
| Security impact | Low / Moderate / High / N/A / Unknown | | |
| Privacy impact | Low / Moderate / High / N/A / Unknown | | |
| Regulatory or contractual exposure | Low / Moderate / High / N/A / Unknown | | |
| External-user exposure | Low / Moderate / High / N/A / Unknown | | |
| Operational criticality | Low / Moderate / High / N/A / Unknown | | |
| Data sensitivity | Low / Moderate / High / N/A / Unknown | | |
| Probabilistic-system impact and autonomy | Low / Moderate / High / N/A / Unknown | | |
| Architectural and integration complexity | Low / Moderate / High / N/A / Unknown | | |
| Reversibility and recovery cost | Low / Moderate / High / N/A / Unknown | | |
| Novelty and evidence strength | Low / Moderate / High / N/A / Unknown | | |

Selected Profile: Baseline / Elevated / High Assurance
Selection Rationale:
Profile Decision ID:

Use the [Tailoring and Authority Guardrail](../../02-governance/13-tailoring-and-authority-guardrail.md) to determine obligations. A lower profile than indicated by a material factor requires explicit rationale, risk disposition, and human approval.

---

# 3. Authority and Decision Rights

| Authority Role | Accountable Human, Team, Role, or Organization | Decisions and Gates | Required Concurrence or Independence | Delegate / Backup |
|----------------|------------------------------------------------|---------------------|--------------------------------------|-------------------|
| Project or Increment Owner | | Scope and outcome | | |
| Requirements Authority | | Requirements baseline and changes | | |
| Architecture Authority | | Architecture baseline and structural changes | | |
| Risk Acceptance Authority | | Residual-risk disposition within stated limits | | |
| Security / Privacy Authority | | Applicable security and privacy posture | | |
| Verification and Validation Authority | | Evidence sufficiency and result disposition | | |
| Release Authority | | Release authorization | | |
| Operational Owner | | Operational acceptance, monitoring, and retirement | | |

State any combined roles and why the selected profile permits combination. For required segregation of duties, identify prohibited role combinations.

Participation, drafting, review assistance, or tool execution does not confer authority.

---

# 4. Tailoring Decisions

| Tailoring ID | Default Obligation | Approved Adjustment | Rationale and Evidence | Risk / Change Ref | Compensating Control | Approved By and Date | Review or Expiration |
|--------------|--------------------|---------------------|------------------------|-------------------|----------------------|----------------------|----------------------|
| TLR-001 | | | | | | | |

Use `None` when no tailoring is approved. Silence SHALL NOT be interpreted as permission to omit an obligation.

---

# 5. Verification, Review, and Evidence Depth

Define:

- Required independent reviews
- Required verification methods and environment fidelity
- Required validation participants and intended-use contexts
- Required security, privacy, safety, accessibility, or AI-assurance reviews
- Sampling, statistical confidence, or coverage rationale where applicable
- Evidence repositories and access controls
- Evidence-retention periods and disposition rules
- Required audit or reconstruction capability

---

# 6. Controlled Uncertainty

| Item ID | Uncertainty | Bounded Effect | Accountable Role | Resolution / Monitoring Plan | Affected Artifacts and Gates | Trigger or Due Date | Current Disposition |
|---------|-------------|----------------|------------------|------------------------------|------------------------------|---------------------|---------------------|

Material uncertainties SHALL also appear in the Project Risk Register. Advancement is prohibited when an unresolved uncertainty could invalidate downstream work.

---

# 7. Approval and Review

Confirm:

- Governed increment is bounded and coherent? (Yes / No)
- Assessment factors have evidence-based ratings? (Yes / No)
- Human authority roles are assigned? (Yes / No)
- Tailoring and exceptions are explicit? (Yes / No / Not Applicable)
- Material uncertainties are controlled and linked? (Yes / No / Not Applicable)
- Evidence and retention obligations are defined? (Yes / No)

Approved By:
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:
Date:
Decision ID:
Next Mandatory Review:

If any required confirmation is `No`, the profile is not approved and phase advancement is prohibited.
