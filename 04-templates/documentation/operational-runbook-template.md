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

---

# 1. Applicability

The Operational Runbook is required for production, hosted, distributed, regulated, or business-critical systems.

If not applicable, document the justification in the System Documentation Package.

---

# 2. Normal Operations

Document:

- Routine operating procedures
- Scheduled maintenance
- Health verification
- Capacity checks
- Backup checks
- Monitoring review cadence

---

# 3. Incident Response

Document:

- Incident classification
- Initial triage steps
- Evidence collection
- Escalation path
- Communication expectations
- Resolution criteria

---

# 4. Degradation and Failover

Document:

- Degraded operating modes
- Failover triggers
- Manual intervention steps
- User impact
- Validation after failover

---

# 5. Recovery and Rollback

Document:

- Recovery procedure
- Rollback procedure
- Data restoration procedure
- Recovery time expectations
- Recovery point expectations
- Related Test Case ID(s)

Recovery posture SHALL align with validated test evidence.

---

# 6. Post-Incident Review

Document:

- Review owner
- Required evidence
- Root cause analysis expectations
- RTM update expectations
- Documentation update expectations
- Phase rollback triggers, if applicable

---

End of Operational Runbook Template
