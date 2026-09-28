<!--
File: 04-templates/documentation/operational-runbook-template.md

Purpose:
  Provide operational procedures for production, hosted, distributed,
  regulated, or business-critical systems.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Operational Runbook

Project Name:  
Version:  
Date (YYYY-MM-DD):  
Author(s):  
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Draft / Approved  
Architecture Version Reference:  
Test Plan Version Reference:  
Packaging Plan Version Reference:  
RTM Version Reference:  
Glossary Version Reference:
Project Governance Profile Reference:
Risk Register Version Reference:
Verification and Validation Report Reference:
Released Baseline / Artifact Reference:
Operational Owner:

---

# 1. Applicability

The Operational Runbook is required for production, hosted, distributed, regulated, or business-critical systems.

If not applicable, document the justification in the System Documentation Package.

---

# 2. Operational Ownership and Acceptance

Document:

- Operational Owner and delegated authority
- Service owner, on-call, security, privacy, data, vendor, and business contacts as applicable
- Supported release, configuration, dependency, model, prompt, data, and provider baselines
- Service hours and support boundaries
- Known limitations, residual Risk IDs, and operating constraints
- Operational acceptance decision and date
- Conditions requiring suspension, rollback, or renewed release authorization

Automation and deployment success do not constitute operational acceptance.

---

# 3. Normal Operations

Document:

- Routine operating procedures
- Scheduled maintenance
- Health verification
- Capacity checks
- Backup checks
- Monitoring review cadence
- Routine evidence retained and location
- Operator access and segregation-of-duties controls
- Data retention and disposition checks

---

# 4. Monitoring, Thresholds, and Drift

| Signal or Indicator | Baseline / Expected Range | Warning Threshold | Action Threshold | Accountable Role | Response Action | Evidence Location | Review Cadence |
|---------------------|---------------------------|-------------------|------------------|------------------|-----------------|-------------------|----------------|

Include applicable availability, performance, capacity, security, privacy, data-quality, business-outcome, user-harm, complaint, dependency, configuration, and probabilistic-system signals.

For every action threshold, define investigation, containment, fallback, re-verification, revalidation, rollback, suspension, or notification actions as applicable.

---

# 5. Incident Response

Document:

- Incident classification
- Initial triage steps
- Evidence collection
- Escalation path
- Communication expectations
- Resolution criteria
- Emergency authority, limits, and expiration
- Required incident identifiers and evidence locations
- Related Risk, Change, Requirement, Verification Case, Validation Scenario, and defect IDs
- Regulatory, contractual, customer, user, or stakeholder notification triggers

Emergency actions SHALL preserve available evidence and receive retrospective impact assessment within the defined deadline.

---

# 6. Degradation and Failover

Document:

- Degraded operating modes
- Failover triggers
- Manual intervention steps
- User impact
- Verification and validation required after failover

---

# 7. Recovery and Rollback

Document:

- Recovery procedure
- Rollback procedure
- Data restoration procedure
- Recovery time expectations
- Recovery point expectations
- Related Verification Case ID(s)
- Related Test Case ID(s)
- Evidence and approval required before return to normal service

Recovery posture SHALL align with approved verification and validation evidence.

---

# 8. Problem Management and Post-Incident Review

Document:

- Review owner
- Required evidence
- Root cause analysis expectations
- RTM update expectations
- Documentation update expectations
- Phase rollback triggers, if applicable
- Recurrence and trend-analysis criteria
- Corrective and preventive actions
- Problem record and decision ownership
- Due dates and closure evidence

Recurring, systemic, high-severity, or poorly understood incidents SHALL enter problem management.

---

# 9. Maintenance and Operational Change

Document:

- Scheduled and emergency maintenance pathways
- Change classification and approval authority
- Security and dependency update cadence
- Pre-deployment verification and rollback requirements
- Post-deployment verification and validation requirements
- Configuration and baseline update procedure
- Change Proposal, RTM, Risk Register, V&V Report, and documentation update triggers
- Maximum time allowed for retrospective assessment after emergency action

Material operational changes SHALL define a governed increment and return to the earliest affected lifecycle phase.

---

# 10. Probabilistic and AI Operations (If Applicable)

Document:

- Model, provider, endpoint, prompt, tool, retrieval, data, threshold, and configuration baseline
- Quality, safety, fairness, privacy, security, cost, and latency signals as applicable
- Drift-detection method and thresholds
- Human review, override, escalation, fallback, and shutdown procedures
- Provider-change detection and response
- Evaluation data and evidence refresh cadence
- Revalidation, rollback, suspension, and retirement triggers

Silent provider or model change SHALL NOT be treated as an approved baseline change.

---

# 11. Deprecation, Data Disposition, and Retirement

Document:

- Deprecation and end-of-support timeline
- Migration or replacement path
- User, operator, customer, and stakeholder communications
- Data export, retention, deletion, legal hold, and evidence disposition
- Credential, key, integration, endpoint, model, and infrastructure shutdown
- Downstream dependency confirmation
- Final access and processing termination checks
- Retirement approval and retained evidence

---

# 12. Review and Approval

Review Cadence:
Next Review Date:
Last Exercise or Recovery Test:
Open Operational Risk IDs:
Open Operational Change IDs:

Approved By:
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:
Date:

Confirm:

- Ownership and escalation paths current? (Yes / No)
- Baselines and operating constraints current? (Yes / No)
- Monitoring thresholds have defined response actions? (Yes / No)
- Incident, recovery, and emergency procedures exercised proportionately? (Yes / No)
- Maintenance and change pathways align with lifecycle governance? (Yes / No)
- Deprecation, data disposition, and retirement obligations defined? (Yes / No)

---

End of Operational Runbook Template
