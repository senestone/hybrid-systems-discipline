<!--
File: 04-templates/system/verification-validation-report-template.md

Purpose:
  Record verification and validation execution, results, evidence,
  deviations, residual risk, and release recommendation.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

A report records evidence and may recommend a disposition.
It does not grant phase advancement or release authority.
-->

# Verification and Validation Report

Project Name:
Report ID: VAL-XXX
Version:
Date (YYYY-MM-DD):
Prepared By:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, collaborators, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Draft / Under Review / Approved / Superseded
System or Release Version:
Source Revision or Tag:
Test Plan Version Reference:
RTM Version Reference:
Packaging Plan Version Reference:
Risk Register Version Reference:
Glossary Version Reference:

---

# 1. Evidence Authority Declaration

Confirm:

- Tested build uniquely identified? (Yes / No)
- Approved Test Plan used? (Yes / No)
- Test environment controlled and recorded? (Yes / No)
- Test data authorized and versioned where required? (Yes / No)
- Requirement-to-Verification Case mappings and methods current? (Yes / No)
- Test Case mappings current for Test-method Verification Cases? (Yes / No)
- Validation scenarios trace to stakeholder needs, intended use, or operational outcomes? (Yes / No)
- Raw evidence retained and accessible? (Yes / No)
- Deviations and exceptions disclosed? (Yes / No)

Any "No" SHALL be explained and reflected in the report disposition.

This report records verification and validation evidence. Approval of the report confirms the accuracy and completeness of that record; it does not independently authorize release.

---

# 2. Scope and Objectives

Define:

- System, release, component, or change evaluated
- Verification objectives
- Validation objectives
- Requirements and non-functional requirements in scope
- Environments and configurations in scope
- Explicit exclusions
- Entry and exit criteria
- Related Change IDs

Unstated exclusions SHALL NOT be inferred as passing.

---

# 3. Evaluation Item and Environment Identification

Record:

- Source revision or tag
- Build identifier
- Package or artifact identifier and checksum
- Runtime and dependency versions
- Hardware, operating system, container, or cloud environment
- Configuration baseline
- External service or test-double versions
- Test harness and tool versions
- Test data set identifiers
- Probabilistic component, model, prompt, threshold, or seed versions where applicable

Results without reproducible evaluation-item identity are invalid unless an approved limitation explicitly states otherwise.

---

# 4. Execution Summary

| Metric | Count |
|--------|-------|
| Planned Verification Cases | |
| Completed Verification Cases | |
| Verified Verification Cases | |
| Failed Verification Cases | |
| Blocked Verification Cases | |
| Planned Test Cases | |
| Executed Test Cases | |
| Passed Test Cases | |
| Failed Test Cases | |
| Blocked Test Cases | |
| Not Run Test Cases | |
| Planned Validation Scenarios | |
| Completed Validation Scenarios | |
| Validated Scenarios | |
| Failed Validation Scenarios | |
| Blocked Validation Scenarios | |
| Cases or Scenarios Added During Execution | |
| Cases or Scenarios Retired with Approval | |

Execution Start:
Execution End:
Executed By:
Automation Run or Pipeline References:
Overall Disposition: Passed / Passed with Exceptions / Failed / Blocked

"Passed with Exceptions" requires each exception to be identified, risk-assessed, and accepted by accountable human authority.

---

# 5. Detailed Results

| Verification Case ID | Requirement / NFR ID | Method | Test Case ID (if applicable) | Configuration | Result | Evidence Ref | Defect / Deviation Ref | Executed By | Date |
|----------------------|----------------------|--------|------------------------------|---------------|--------|--------------|------------------------|-------------|------|

Allowed Method values: Test / Analysis / Inspection / Demonstration / Review / Measurement

Allowed Result values: Verified / Failed / Blocked / Not Run / Not Applicable

Evidence references SHALL resolve to retained logs, reports, screenshots, analyses, inspection records, demonstrations, reviews, measurements, audit records, or other reviewable outputs. A result without required evidence SHALL NOT be treated as verified.

---

# 6. Requirements and Coverage Reconciliation

| Requirement / NFR ID | Planned Verification Cases and Methods | Completed Verification Cases | Test Case IDs (if applicable) | Verification Status | Evidence Ref | RTM Updated? |
|----------------------|----------------------------------------|------------------------------|-------------------------------|---------------------|--------------|--------------|

Confirm:

- Every in-scope requirement has an explicit disposition
- Every completed verification activity maps to approved intent
- Every executed test maps to a Test-method Verification Case
- No unauthorized behavior was validated as scope
- Coverage gaps are identified as blockers, deviations, or accepted residual risk
- RTM verification and validation status and evidence references are current

Aggregate percentages SHALL NOT conceal uncovered Critical requirements or non-functional requirements.

---

# 7. System Validation Results

| Validation Scenario ID | Stakeholder Need / Intended Use / Outcome Ref | Representative Users or Operators | Operational Context | Related Requirement IDs | Result | Evidence Ref | Limitation / Deviation Ref |
|------------------------|------------------------------------------------|-----------------------------------|---------------------|-------------------------|--------|--------------|----------------------------|

Allowed Result values: Validated / Failed / Blocked / Not Run / Not Applicable

Confirm that validation evidence addresses:

- Stakeholder needs and expected outcomes
- Intended use and foreseeable misuse
- Representative users, operators, workflows, and environments
- Operational constraints and human factors where applicable
- Assumptions, limitations, and contexts not represented

Passing requirement verification SHALL NOT be reported as system validation unless the validation criteria and representative context were also evaluated.

---

# 8. Non-Functional Verification

| NFR ID | Measure | Required Threshold | Observed Result | Status | Evidence Ref |
|--------|---------|--------------------|-----------------|--------|--------------|

Address applicable areas:

- Performance and latency
- Capacity and throughput
- Availability and resilience
- Security and access control
- Privacy and data handling
- Observability and audit logging
- Accessibility and usability
- Compatibility and portability
- Maintainability and reproducibility

Claims of compliance SHALL be supported by explicit measures or approved qualitative criteria.

---

# 9. Failure, Recovery, and Boundary Verification

Document results for:

- Error and edge conditions
- Dependency failure
- Degradation and failover
- Backup, restore, and recovery
- Rollback
- Monitoring and alert generation
- Audit trail integrity

For probabilistic components, also record:

- Boundary enforcement results
- Acceptance and rejection behavior
- Deterministic state protection
- Fallback behavior
- Output-quality or safety thresholds
- Drift or repeatability observations
- Model, prompt, data, and configuration identity

Untested required failure behavior SHALL be reported as a coverage gap.

---

# 10. Defects, Deviations, and Exceptions

| Reference ID | Type | Description | Severity | Affected IDs | Disposition | Risk ID | Approval Ref |
|--------------|------|-------------|----------|--------------|-------------|---------|--------------|

Type values: Defect / Test Deviation / Environment Deviation / Waiver / Known Limitation

For each open item, state:

- Effect on report conclusions
- Workaround or containment
- Retest requirement
- Target release or resolution date
- Accountable owner
- Residual risk and acceptance authority

An unexplained deviation invalidates the affected result.

---

# 11. Packaging and Reproducibility Verification

Record:

- Clean build result
- Clean installation or deployment result
- Package integrity verification
- Smoke-test result against packaged artifact
- Configuration verification
- Rebuild or reproducibility result
- Artifact-to-source and artifact-to-RTM linkage
- Rollback verification result

Development-environment success SHALL NOT substitute for required packaged-environment verification.

---

# 12. Residual Risk and Release Recommendation

Open Risk IDs:
New or Changed Risk IDs:
Accepted Exceptions:
Known Limitations:

Recommendation:

- Recommend release
- Recommend release with stated conditions
- Do not recommend release
- Unable to recommend due to insufficient evidence

Rationale:

Conditions or follow-up actions:

The recommendation is advisory evidence for the human release authority. It is not release approval.

---

# 13. Traceability and Artifact Updates

Confirm updates to:

- RTM verification and validation status and evidence references
- Defect records
- Change Proposal and Impact Assessments
- Project Risk Register
- Project Glossary
- Test Plan and test inventory
- Packaging Plan
- System documentation and release notes

| Artifact | Version Before | Version After | Update Summary | Owner |
|----------|----------------|---------------|----------------|-------|

---

# 14. Review Checklist

- [ ] Scope and exclusions are explicit
- [ ] Evaluation item and environment are reproducibly identified
- [ ] Planned and executed test inventories reconcile
- [ ] Requirement verification coverage and methods are visible
- [ ] Validation scenarios address stakeholder needs, intended use, and operational context
- [ ] Raw evidence references resolve
- [ ] Failures, blocked tests, and omitted tests are disclosed
- [ ] Defects and deviations have dispositions
- [ ] Residual risks are linked to the Project Risk Register
- [ ] RTM evidence references are current
- [ ] Packaging and clean-environment results are recorded
- [ ] Acronyms and abbreviations link to the Project Glossary on first appearance
- [ ] Release recommendation follows from the evidence
- [ ] Human review is complete

---

# 15. Approval

Prepared By:
Reviewed By:
Approved By:
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:
Date:
Version Incremented: Yes / No

Approval confirms this report accurately represents the available evidence and disclosed limitations. Release requires separate authorization under the lifecycle bootstrap.

---

End of Verification and Validation Report Template
