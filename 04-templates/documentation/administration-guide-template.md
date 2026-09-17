<!--
File: 04-templates/documentation/administration-guide-template.md

Purpose:
  Provide privileged operational and administrative documentation for
  systems that require server, service, shared runtime, or administrative control.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Administration Guide

Project Name:  
Version:  
Date (YYYY-MM-DD):  
Author(s):  
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Draft / Approved  
Architecture Version Reference:  
Packaging Plan Version Reference:  
RTM Version Reference:  

---

# 1. Applicability

The Administration Guide is required when the system includes any of the following:

- Server or hosted runtime
- Multi-user administration
- Privileged configuration
- Shared infrastructure
- Scheduled jobs or background workers
- Operational monitoring
- Backup, restore, or data retention duties
- Security administration

If none apply, ignore this template after documenting and approving the omission in the System Documentation Package.

Example: this template may be omitted for a standalone, non-server-based application with no privileged configuration, shared runtime, multi-user administration, operational monitoring, or administrative duties.

---

# 2. Administrative Roles and Responsibilities

Document:

- Administrator roles
- Required permissions
- Separation of duties
- Escalation paths
- Audit responsibilities

Privileged responsibility SHALL be explicit.

---

# 3. Runtime Operations

Document:

- Start, stop, and restart procedures
- Health checks
- Scheduled tasks
- Queue or worker operations
- Maintenance windows
- Capacity considerations

Operational ambiguity is prohibited.

---

# 4. Security Administration

Document:

- Identity and access management
- Role assignment
- Secret rotation
- Certificate management
- Audit logging
- Security review evidence

Security controls SHALL align with approved NFRs.

---

# 5. Monitoring, Logging, and Alerting

Document:

- Metrics collected
- Log locations
- Alert conditions
- Dashboard references
- Retention expectations
- Incident response references

Observability SHALL support failure analysis and audit review.

---

# 6. Backup, Restore, and Recovery

Document:

- Backup scope
- Backup frequency
- Restore procedure
- Recovery time expectations
- Recovery point expectations
- Rollback procedure
- Data migration considerations

Recovery claims SHALL be validated by test evidence where applicable.

---

End of Administration Guide Template
