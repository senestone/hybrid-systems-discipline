<!--
File: 04-templates/system/traceability-matrix-template.md

Purpose:
  Provide enforceable bidirectional lifecycle traceability
  across hybrid deterministic–probabilistic systems.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

Traceability is a structural control mechanism.
Release without validated traceability is prohibited.
-->

# Requirements Traceability Matrix (RTM)

Project Name:  
Version:  
Last Updated (YYYY-MM-DD):
Maintained By:  
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Draft / Approved  
Requirement Version Reference:  
Architecture Version Reference:  
Design Version Reference:  
Test Plan Version Reference:  
Glossary Version Reference:
Risk Register Version Reference:
Verification and Validation Report Version Reference:

---

# 1. RTM Authority Declaration

Confirm:

- Current lifecycle phase identified? (Yes / No)
- Requirements approved when required by the current phase? (Yes / No / Not Yet Applicable)
- Architecture approved when required by the current phase? (Yes / No / Not Yet Applicable)
- Detailed Design approved when required by the current phase? (Yes / No / Not Yet Applicable)
- Test Plan aligned when required by the current phase? (Yes / No / Not Yet Applicable)
- Advancement to next phase authorized? (Yes / No)  

If any answer required for the current phase is `No`, traceability validation is incomplete. Future-phase mappings MAY be marked `Pending` only with a target artifact and resolution gate; required current-phase mappings SHALL resolve before advancement.

---

# 2. Purpose

The RTM SHALL ensure:

- Every requirement maps to architecture  
- Every architectural element maps to requirements  
- Every design artifact maps to architecture  
- Every implementation artifact maps to design  
- Every requirement maps to one or more Verification Cases with appropriate methods
- Every test case maps to a Test-method Verification Case and approved requirements
- Validation scenarios map stakeholder needs and intended use to affected requirements and evidence
- Packaging and orchestration artifacts map to release state  
- Deterministic–probabilistic boundaries are traceable  

Traceability SHALL be bidirectional and complete.

Completeness is phase-aware. At release, no required mapping may remain `Pending`.

---

# 3. Core Traceability Matrix

| Req ID | Req Type | Requirement Summary | HLA Component ID | DD Artifact | Implementation Unit | Verification Case ID | Verification Method | Test Case ID | Change Ref | Risk Ref | Packaging Ref | Orchestration Ref | Verification Status | Evidence Ref |
|--------|----------|---------------------|------------------|-------------|---------------------|----------------------|---------------------|--------------|------------|----------|---------------|-------------------|---------------------|--------------|

Example:

| FR-001 | FR | User authentication | HLA-Auth | DD-Login | auth/login.py | VC-001 | Test | TC-001 | CHG-001 | RSK-001 | PKG-v1.0 | ORCH-Build-01 | Verified | VAL-001 |

---

## Field Definitions

**Req ID**  
FR-XXX or NFR-XXX identifier from SRS.

**Req Type**  
FR / NFR.

**Requirement Summary**
Concise description of the approved requirement; the SRS remains authoritative.

**HLA Component ID**  
Approved architectural component.

**DD Artifact**  
Design-level module, interface, or artifact identifier.

**Implementation Unit**  
Code module, package, service, or deployment unit.

**Verification Case ID**
Stable identifier for the planned verification activity, such as VC-001.

**Verification Method**
Test / Analysis / Inspection / Demonstration / Review / Measurement.

**Test Case ID**  
Executable test identifier when the Verification Method is Test; otherwise `Not Applicable`.

**Change Ref**
Change Proposal and Impact Assessment ID when the row is affected by a material change.

**Risk Ref**
Project Risk Register ID for release-relevant exposure associated with the row.

**Packaging Ref**  
Reference to packaging plan artifact or release identifier.

**Orchestration Ref**  
Reference to build or pipeline identifier.

**Verification Status**
Planned / Ready / In Progress / Verified / Failed / Blocked / Not Applicable.

**Evidence Ref**  
Reference to test report, validation artifact, or audit evidence.

## 3.1 Validation Traceability

Validation SHALL be traced separately from requirement verification.

| Validation Scenario ID | Stakeholder Need / Intended Use / Outcome Ref | Representative Users or Operators | Operational Context | Related Requirement IDs | Validation Criteria | Status | Evidence Ref |
|------------------------|------------------------------------------------|-----------------------------------|---------------------|-------------------------|---------------------|--------|--------------|
| VS-001 | | | | | | Planned | |

Allowed Status values: Planned / Ready / In Progress / Validated / Failed / Blocked / Not Applicable

Passing requirement verification SHALL NOT be treated as automatic validation of stakeholder need or intended use.

---

# 4. Deterministic–Probabilistic Boundary Traceability (If Applicable)

For probabilistic subsystems, include:

| Req ID | Boundary ID | Validation Harness | Containment Logic | Fallback Ref | Observability Ref | Drift Validation | Status |

Probabilistic behavior SHALL NOT exist outside RTM coverage.

Untracked boundaries are governance violations.

---

# 5. Non-Functional Traceability

Each NFR SHALL explicitly map to:

- Architectural mechanism  
- Design enforcement  
- Verification Case and method
- Test Case when the method is Test
- Packaging consideration  
- Orchestration consideration  

Example:

| NFR ID | Architectural Mechanism | Design Artifact | Verification Case | Method | Test Case (if applicable) | Packaging Impact | Status |

Assumed NFR compliance is prohibited.

---

# 6. Bidirectional Verification Rules

Traceability MUST support:

Forward tracing:
Requirement → Architecture → Design → Implementation → Verification Case → Evidence → Packaging

Backward tracing:
Evidence → Verification Case → Implementation → Design → Architecture → Requirement

Validation tracing:
Stakeholder Need / Intended Use / Outcome → Validation Scenario → Related Requirements → Evidence

If any chain breaks, advancement is prohibited.

---

# 7. Orphan Detection

The following SHALL block progression:

- Requirement without architectural mapping  
- Architectural component without requirement  
- Design artifact without architecture parent  
- Implementation unit without design reference  
- Verification case without requirement reference
- Test case without requirement reference  
- Test case without a parent Test-method Verification Case
- Validation scenario without an approved stakeholder need, intended use, or outcome basis
- Packaging artifact without RTM linkage  
- Orchestration artifact without RTM linkage  

No orphan artifacts permitted.

---

# 8. Change Control and Lineage

When any of the following change:

- Requirement  
- Architecture  
- Design  
- Implementation  
- Verification case or method
- Test case  
- Validation scenario
- Packaging configuration  
- Orchestration pipeline  

The RTM SHALL be updated immediately. Material changes SHALL reference the applicable Change ID.

Each update SHALL record:

- Date  
- Change ID, when material
- Change summary  
- Impacted IDs  
- Phase rollback requirement (if any)  

Untracked change invalidates lifecycle integrity.

---

# 9. Coverage Validation Checklist

Before phase advancement, confirm:

- 100% FR coverage to design  
- 100% NFR coverage to architecture  
- 100% implementation traceability  
- 100% requirement-to-verification coverage with methods
- 100% Test-method Verification Cases linked to Test Case IDs
- Validation scenarios cover approved stakeholder needs, intended use, and operational outcomes
- Deterministic–probabilistic boundaries mapped (if applicable)  
- Packaging traceability complete  
- Orchestration traceability complete  
- No orphan artifacts  

Failure blocks advancement.

---

# 10. Release-State Snapshot

Before release authorization:

- RTM Version incremented  
- Verification and validation status updated to release state
- Evidence references finalized  
- Verification and Validation Report version aligned
- Release-relevant Risk IDs dispositioned
- Change IDs closed or explicitly carried forward
- Packaging reference aligned to artifact  
- Orchestration reference aligned to build  
- Documentation version aligned  

Release without finalized RTM snapshot is prohibited.

---

# 11. Approval

Approved By:  
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:  
Date:  
Version Incremented: Yes / No  

RTM validation required before:

- Implementation completion  
- Test phase closure  
- Packaging approval  
- Release authorization  

---

End of Requirements Traceability Matrix Template
