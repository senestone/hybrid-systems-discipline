<!--
File: 02-governance/08-test-guardrail.md

Purpose:
  Enforce disciplined, traceable, and compensating verification
  architecture for hybrid deterministic–probabilistic systems.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

Testing is a structural control mechanism.
It is not a post-implementation activity.
-->

# 08 — Test Guardrail

## 1. Purpose

Verification and validation provide the compensating evidence architecture. Testing is a primary verification method within that architecture.

Verification establishes objective evidence that specified requirements are fulfilled.

Validation establishes objective evidence that the delivered system supports stakeholder needs, intended use, and operational context.

It SHALL:

- Verify functional requirements
- Verify non-functional requirements
- Confirm architectural assumptions
- Enforce deterministic behavior
- Contain probabilistic uncertainty
- Detect regressions
- Preserve reproducibility posture
- Reduce operational risk

Testing is defined prior to implementation.

Implementation without defined verification and validation intent is prohibited.

---

## 2. Lifecycle Authority

Testing spans:

- Requirements
- Architecture
- Detailed Design
- Implementation
- Packaging
- Release

Lifecycle authority resides in:

`02-governance/00-lifecycle-bootstrap.md`

No phase advancement is authorized without defined verification and validation alignment.

---

## 3. Test Planning Mandate

Before Implementation begins, the following test-planning content SHALL exist:

- Approved Test Plan
- Test Strategy
- Test Case Inventory
- Verification Case Inventory with selected methods
- Requirement-to-Verification Case mapping
- Validation scenarios for stakeholder needs, intended use, and operational context
- Acceptance criteria
- Failure scenario definitions
- NFR verification strategy

The Test Plan is the governing verification-and-validation planning artifact. The Test Strategy, Verification Case Inventory, Test Case Inventory, and validation scenarios MAY be maintained as sections of the Test Plan or as approved, versioned artifacts linked from it.

Requirement acceptance criteria and failure scenarios MAY remain in their approved source artifacts when the Test Plan and RTM reference them unambiguously. Separate documents are not required solely to satisfy this mandate.

If verification-and-validation planning content is incomplete, implementation SHALL NOT begin.

As verification and validation activities are performed, results SHALL be recorded in a Verification and Validation Report that reconciles the planned inventories, actual execution, retained evidence, deviations, defects, and coverage.

---

## 4. Traceability Enforcement

Every Requirement ID MUST map to:

- At least one Verification Case ID
- A selected method: Test / Analysis / Inspection / Demonstration / Review / Measurement
- Defined acceptance criteria and planned evidence

When Test is the selected method, the Verification Case SHALL map to at least one Test Case ID. A non-test method SHALL include a rationale appropriate to the requirement and risk profile.

If a requirement cannot be verified by an appropriate method, it is incomplete.

Traceability Matrix (RTM) SHALL include:

- Requirement → Design → Implementation → Verification Case → Evidence mapping
- Test Case linkage where Test is the selected method
- Validation Scenario linkage to stakeholder need, intended use, or operational outcome

Unmapped requirements SHALL block advancement.

Each completed verification or validation status SHALL reference evidence in the Verification and Validation Report or another approved evidence artifact.

---

## 5. Functional Verification

Functional tests SHALL verify:

- Nominal flows
- Boundary conditions
- Edge cases
- Error handling
- Recovery logic
- State transitions
- Cross-component interaction integrity

Functional verification MUST be deterministic wherever possible.

---

## 6. Non-Functional Verification

Non-functional requirements MUST be verified explicitly using methods appropriate to the characteristic and acceptance threshold.

Planning SHALL define verification strategy for:

- Performance thresholds
- Latency constraints
- Throughput targets
- Security posture
- Access controls
- Fault tolerance
- Availability targets
- Observability integrity
- Audit logging completeness
- Reproducibility expectations

Assumed NFR compliance is prohibited.

---

## 6.1 System Validation

Validation SHALL evaluate the integrated system against:

- Stakeholder needs
- Intended use and foreseeable misuse
- Representative users and operators
- Operational workflows and environments
- Business, mission, or service outcomes
- Human factors and user expectations where applicable

Validation scenarios SHALL remain traceable to their approved basis, affected Requirement IDs, results, and evidence. Passing requirement verification does not by itself establish system validation.

---

## 7. Deterministic–Probabilistic Containment Testing

If probabilistic components exist, testing MUST:

- Verify boundary enforcement
- Verify invocation contract
- Verify acceptance/rejection logic
- Verify fallback behavior
- Verify deterministic state protection
- Verify logging and observability
- Verify reproducibility constraints (where applicable)
- Verify drift detection posture (if defined)

Probabilistic outputs SHALL NOT be treated as self-validating.

Containment integrity is mandatory.

---

## 8. Failure Modeling Verification

Tests SHALL explicitly exercise:

- Deterministic failure paths
- Probabilistic uncertainty handling
- Integration failure scenarios
- Dependency outage simulation
- Degradation posture
- Recovery and rollback mechanisms

Failure pathways MUST be observable and testable.

Untested failure logic is prohibited.

---

## 9. Automation Requirement

Where feasible, tests SHALL be:

- Automated
- Executable via single documented command
- Integrated into build/orchestration system
- Deterministic in outcome (where determinism is expected)
- Repeatable in clean environments

Manual-only testing increases risk and SHALL be justified.

---

## 10. Clean Environment Verification

Tests MUST execute successfully in:

- Clean local environments
- Continuous Integration (if applicable)
- Packaged runtime artifacts
- Deployment-equivalent environments (where feasible)

Local success without packaging verification is insufficient.

---

## 11. Regression Discipline

Testing SHALL:

- Prevent regression via automated coverage
- Update when requirements evolve
- Update when architecture changes
- Update when probabilistic boundaries shift

Test stagnation is a governance failure.

Material test-scope, acceptance-criteria, environment, or evidence deviations SHALL be assessed through the Change Proposal and Impact Assessment process before affected results are accepted.

---

## 12. Observability Verification

Testing MUST confirm:

- Logging boundaries
- Error propagation behavior
- Monitoring hooks
- Audit record generation
- Failure signal clarity

Systems that cannot be observed cannot be governed.

---

## 13. Refusal Protocol

AI SHALL refuse to:

- Begin implementation without test plan
- Declare coverage sufficient without mapping
- Skip NFR verification
- Ignore probabilistic containment verification
- Advance phase without verification and validation alignment
- Approve release without sufficient verification and validation evidence
- Declare verification complete without an evidence-bearing Verification and Validation Report
- Conceal failed, blocked, omitted, or deviating test execution

Refusal preserves verification integrity.

---

## 14. Verification and Validation Completion and Release Criteria

Verification and validation obligations are satisfied only when:

- All Requirement IDs map to Verification Case IDs with appropriate methods
- Every Test-method Verification Case maps to executed Test Case IDs
- Functional verification passes
- NFR verification strategy is executed
- Validation scenarios establish stakeholder need, intended use, and operational-context disposition
- Probabilistic containment tests pass (if applicable)
- Failure paths are exercised
- Tests pass in clean environment
- Packaging verification succeeds
- Verification and Validation Report reconciles planned and completed verification cases, tests, and validation scenarios
- Evidence references resolve and are reflected in the RTM
- Defects, deviations, exceptions, and residual risks are dispositioned
- Project Risk Register reflects verification and validation findings
- RTM reflects complete coverage
- Human approval is granted

If any condition is unmet, advancement to release is prohibited. These execution criteria do not apply to the Test Planning to Implementation gate, which is governed by the approved planning content in Section 3 and the phase-gate checklist.

Release SHALL NOT proceed without sufficient verification and validation evidence for the governed increment and its approved risk profile.

---

End of Guardrail
