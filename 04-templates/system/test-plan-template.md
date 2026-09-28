<!--
File: 04-templates/system/test-plan-template.md

Purpose:
  Define enforceable verification and validation governance aligned with lifecycle
  discipline for hybrid deterministic–probabilistic systems.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

Testing verifies requirements — not code.
Release without sufficient verification and validation evidence is prohibited.
-->

# Test Plan

Project Name:  
Version:  
Date (YYYY-MM-DD):  
Author(s):  
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Draft / Approved  
Requirement Version Reference:  
Architecture Version Reference:  
RTM Version Reference:  
Glossary Version Reference:
Risk Register Version Reference:
Relevant Change Assessment References:
Verification and Validation Report Reference:

---

# 1. Test Authority Declaration

Confirm:

- Requirements approved? (Yes / No)  
- Architecture approved? (Yes / No)  
- Detailed Design approved? (Yes / No)  
- RTM initialized? (Yes / No)  
- Advancement to Test Planning authorized? (Yes / No)  

If any answer is “No,” test planning is premature.

---

# 2. Test Scope

Define explicitly:

- Requirement IDs in scope  
- NFR categories in scope  
- Packaging verification scope
- Orchestration verification scope
- Deterministic–probabilistic containment verification scope (if applicable)

Out-of-scope areas SHALL be declared.

Scope ambiguity SHALL block advancement.

---

# 3. Test Objectives

Define:

- What must be proven  
- What risk posture must be mitigated  
- What acceptance posture must be achieved  
- What constitutes release readiness  

Testing SHALL verify requirements and NFRs — not internal implementation structure.

---

# 4. Test Strategy

## 4.1 Testing Levels

Specify applicable levels and justify exclusions:

- Unit Testing  
- Integration Testing  
- System Testing  
- Regression Testing  
- Performance Testing  
- Security Testing  
- Reliability / Resilience Testing  
- User Acceptance Testing (UAT)  
- Packaging Verification
- Orchestration / Clean Build Verification

Unjustified exclusion of test levels SHALL be documented.

---

## 4.2 Deterministic–Probabilistic Verification (If Applicable)

If probabilistic components exist, define:

- Acceptance boundaries  
- Variability tolerance thresholds  
- Rejection criteria  
- Containment verification tests
- Fallback verification tests
- Observability verification tests
- Drift verification (if applicable)

Probabilistic verification SHALL be explicit.

Implicit trust is prohibited.

---

## 4.3 Functional Verification

Define approach for verifying:

- All FR IDs  
- Acceptance criteria coverage  
- Edge cases  
- Negative cases  
- Error conditions  

Each FR SHALL map to at least one Verification Case ID. Functional behavior SHOULD use Test as a verification method unless another method is justified.

---

## 4.4 Non-Functional Verification

Define verification strategy for:

- Performance  
- Scalability  
- Reliability  
- Security  
- Observability  
- Auditability  
- Reproducibility  

Each NFR SHALL map to measurable verification.

Assumed compliance is prohibited.

---

## 4.5 Verification Case Inventory

Maintain the inventory in this section or reference an approved, versioned inventory artifact.

| Verification Case ID | Requirement ID(s) | Method | Acceptance Criteria | Planned Evidence | Environment / Inputs | Owner | Status |
|----------------------|-------------------|--------|---------------------|------------------|----------------------|-------|--------|
| VC-001 | | Test / Analysis / Inspection / Demonstration / Review / Measurement | | | | | Planned |

Every approved Requirement ID SHALL map to at least one Verification Case ID and an appropriate method. When the method is Test, identify the linked Test Case IDs in the Test Case Inventory and RTM.

---

## 4.6 Test Case Inventory

Maintain the inventory in this section or reference an approved, versioned inventory artifact.

At minimum, record:

| Test Case ID | Parent Verification Case ID | Requirement ID(s) | Test Level / Type | Objective or Scenario | Preconditions and Test Data | Expected Result / Acceptance Threshold | Environment | Priority / Risk Ref | Automation Status | Planned Evidence Location |
|--------------|-----------------------------|-------------------|-------------------|-----------------------|-----------------------------|----------------------------------------|-------------|---------------------|-------------------|---------------------------|

Each Test Case ID SHALL be unique and SHALL map to at least one approved Requirement ID.

The inventory SHALL include nominal, boundary, negative, failure, recovery, and deterministic-probabilistic containment cases where applicable.

Detailed procedures MAY reside in approved linked artifacts when the inventory preserves their identifiers, requirement mappings, versions, and locations.

### 4.6.1 Failure Coverage Matrix (When Applicable)

When the system has a governed failure catalogue, error taxonomy, state-transition failure model, or material recovery contract, map each applicable failure condition to planned coverage in this section or an approved linked artifact.

| Failure Contract ID | Trigger or Injection Method | Expected Status and Prohibited Side Effects | Recovery / Retry Expectation | Test Case ID(s) | Planned Evidence |
|---------------------|-----------------------------|---------------------------------------------|------------------------------|-----------------|------------------|

The matrix MAY group failures that share one deterministic rule, but every governed condition SHALL have an explicit disposition. The existence of an error code, enum, or branch is not evidence that its behavior is covered.

---

## 4.7 Validation Strategy and Scenarios

Validation establishes whether the integrated system supports stakeholder needs, intended use, and the operational context. It is distinct from verification of specified requirements.

| Validation Scenario ID | Stakeholder Need / Intended Use / Outcome Ref | Representative Users or Operators | Operational Context | Related Requirement IDs | Validation Criteria | Planned Evidence | Status |
|------------------------|------------------------------------------------|-----------------------------------|---------------------|-------------------------|---------------------|------------------|--------|
| VS-001 | | | | | | | Planned |

Define representative environments, participants, workflows, foreseeable misuse, assumptions, and limitations. Passing requirement verification SHALL NOT be treated as automatic system validation.

---

# 5. Traceability Enforcement

All Requirement IDs SHALL map to one or more Verification Case IDs with an appropriate method.

All Test Case IDs SHALL map to a Test-method Verification Case ID and one or more Requirement IDs.

No Test Case SHALL exist without a Requirement reference.

All Validation Scenario IDs SHALL map to an approved stakeholder need, intended use, or operational outcome and to affected Requirement IDs.

Traceability gaps SHALL block advancement.

RTM SHALL be updated with:

- Verification Case ID
- Verification Method
- Test Case ID, when applicable
- Verification and validation status
- Evidence reference

---

# 6. Test Environment

Document:

- Hardware  
- OS versions  
- Runtime versions  
- External integrations  
- Configuration model  
- Packaging-equivalent environment  
- Clean build verification environment

Environment drift SHALL be minimized.

Local-only verification is insufficient.

---

# 7. Test Data Governance

Define:

- Data sources  
- Data generation strategy  
- Data anonymization (if applicable)  
- Edge-case coverage  
- Data retention rules
- Expected-result authority and review
- Privacy, licensing, and redistribution constraints

Invalid or uncontrolled data SHALL invalidate test results.

When test data is generated, versioned, security-sensitive, licensed, shared across cases, or relied upon as a reproducibility oracle, define in this section or an approved linked fixture plan:

- Stable fixture and expected-result identifiers and versions
- Integrity metadata such as size and digest where appropriate
- Generator source, parameters, deterministic seed, toolchain, and command identity
- Linked Test Case IDs and bounded fixture purpose
- Expected results derived independently from candidate implementation output
- Positive, boundary, negative, failure, recovery, and prohibited-side-effect coverage
- Distribution, access, retention, and destruction classifications
- Representative workload assembly and environment-dependent comparison rules
- Change-control and regression effects when a fixture or expected result changes

Prefer minimal synthetic and redistributable fixtures. Production, personal, secret, protected, access-controlled, or ambiguously licensed data SHALL NOT enter a portable fixture set without explicit authorization and controls.

A separate Test Data and Fixture Plan is optional. Use one only when the complexity would make this Test Plan difficult to review or maintain.

---

# 8. Entry Criteria

Testing may begin when:

- Detailed Design approved  
- RTM updated  
- Test cases drafted and reviewed  
- Environment validated  
- Automation (if applicable) prepared  

Premature execution SHALL be halted.

Define execution ordering or waves when later activities depend on earlier contract, integration, safety, or environment evidence. Later evidence SHALL NOT waive an earlier failed invariant.

## 8.1 Suspension and Resumption Criteria

Define conditions that invalidate or suspend an execution, such as:

- Fixture, expected-result, build, dependency, or environment identity mismatch
- Environment contamination or loss of required isolation
- Unsafe logging, privacy exposure, or uncontrolled resource behavior
- Missing evidence capture or inability to distinguish product failure from infrastructure failure
- Failure of a prerequisite invariant or containment boundary

For each applicable condition, define evidence preservation, responsible disposition, corrective action, and the criteria for resuming or restarting execution.

---

# 9. Verification and Validation Exit Criteria

Planned verification and validation for release are complete only when:

- All High-priority FRs verified
- All Critical NFRs verified
- Deterministic–probabilistic containment verified (if applicable)  
- No unresolved High-severity defects  
- Clean build verified
- Packaging verification complete
- Validation scenarios completed with results, evidence, and limitations recorded
- RTM updated to reflect verification and validation state
- Documentation updated  
- Human approval granted  

If any condition is unmet, release is prohibited.

---

# 10. Defect Governance

Define:

- Defect severity levels  
- Priority levels  
- Escalation criteria  
- Re-test procedure  
- Phase rollback triggers  

Critical defects SHALL trigger:

- Root cause analysis  
- RTM update  
- Possible phase regression  

---

# 11. Automation and Orchestration Integration

If applicable, define:

- Automated test coverage goals  
- CI/CD integration  
- Regression automation  
- Packaging verification automation
- Clean build automation  
- Failure gating logic  

Automation SHALL enforce lifecycle discipline.

It SHALL NOT bypass human gate authorization.

---

# 12. Metrics and Reporting

Define:

- Requirement coverage percentage  
- NFR verification coverage
- Defect density  
- Pass/fail thresholds  
- Trend tracking  
- Verification and Validation Report ownership, evidence locations, and reporting cadence

Metrics SHALL support governance and audit reconstruction.

The Verification and Validation Report SHALL reconcile planned Verification Cases, tests, and validation scenarios with completed results, retained evidence, deviations, defects, coverage, and residual risk.

---

# 13. Risk Assessment

Identify:

- High-risk Requirement IDs  
- Architectural risk concentration points  
- Integration fragility  
- Probabilistic containment risk (if applicable)  

Persistent or cross-cutting risks SHALL reference stable IDs in the Project Risk Register.
- Operational risk  

High-risk items SHALL receive increased verification and validation depth.

---

# 14. Phase Gate Declaration

Confirm readiness to proceed from Test Planning to Implementation:

- Test strategy defined? (Yes / No)
- Verification Case Inventory complete with methods and reviewed? (Yes / No)
- Test Case Inventory complete for all Test-method Verification Cases? (Yes / No)
- Requirement-to-Verification mapping complete with no orphan requirements? (Yes / No)
- Validation scenarios defined for stakeholder needs, intended use, and operational context? (Yes / No)
- NFR verification strategy and measurable thresholds defined? (Yes / No)
- Failure, recovery, and negative scenarios defined? (Yes / No)
- Deterministic–probabilistic containment verification defined, if applicable? (Yes / No / Not Applicable)
- Verification and Validation Report structure and evidence-retention approach defined? (Yes / No)
- Human approval granted? (Yes / No)

If any required answer is “No,” remain in Test Planning.

---

# Approval

Approved By:  
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:  
Date:  
Version Incremented: Yes / No  

Implementation without an approved Test Plan is prohibited.

---

End of Test Plan Template
