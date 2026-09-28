<!--
File: 02-governance/09-traceability-guardrail.md

Purpose:
  Enforce structural, bidirectional, lifecycle-wide traceability
  across hybrid deterministic–probabilistic systems.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

Traceability is a structural control mechanism.
Without it, governance collapses into narrative.
-->

# 09 — Traceability Guardrail

## 1. Purpose

Traceability is the enforcement spine of lifecycle governance.

It SHALL:

- Bind intent to execution
- Bind requirements to structure
- Bind structure to behavior
- Bind behavior to verification
- Bind verification and validation evidence to release
- Preserve change impact visibility
- Prevent scope drift
- Enable audit reconstruction
- Enable reproducibility assessment

Traceability is not documentation.

It is structural linkage.

---

## 2. Authoritative Traceability Model

The system SHALL maintain a formally governed Traceability Matrix (RTM).

The RTM is the authoritative lifecycle mapping artifact.

It SHALL be:

- Current
- Versioned
- Reviewable
- Bidirectional
- Phase-gated

Forward linkage alone is insufficient.

Reverse linkage is mandatory.

Traceability completeness is phase-aware. Mappings to artifacts already required by the current or completed phase SHALL be resolved. Future-phase mappings MAY be marked `Pending` only when the target artifact and required resolution gate are identified. `Pending` SHALL NOT be used for an overdue or missing mapping.

---

## 3. Minimum RTM Schema

The RTM SHALL include, at minimum:

- Requirement ID
- Requirement short description
- Architectural Component ID(s)
- Detailed Design reference(s)
- Implementation reference(s)
- Verification Case ID(s)
- Verification method
- Test Case ID(s), when the method is Test
- Verification status
- Validation Scenario ID(s), where the requirement supports a validated stakeholder need or intended use
- Version identifier
- Last-updated timestamp

Optional but recommended:

- Owner
- Risk classification
- Risk Register ID(s)
- Change Proposal and Impact Assessment ID(s)
- Verification or validation evidence reference
- Release target

RTM schema SHALL be stable and governed.

Ad hoc formats are prohibited.

---

## 4. Requirement Traceability

Each Requirement ID MUST, as the lifecycle produces the applicable artifacts:

- Map to ≥1 Architectural Component
- Map to ≥1 Detailed Design element
- Map to ≥1 Implementation artifact
- Map to ≥1 Verification Case ID with an appropriate method

If a mapping required by the current or a completed phase is missing, the requirement is incomplete. Future mappings SHALL identify their target phase or gate.

Unmapped requirements SHALL block advancement.

---

## 5. Architectural Traceability

Each Architectural Component MUST:

- Reference supporting Requirement ID(s)
- Map to Detailed Design elements
- Maintain boundary integrity

Architectural components without requirement basis SHALL be removed or formally justified.

Unjustified structure is prohibited.

---

## 6. Detailed Design Traceability

Each Detailed Design element MUST:

- Reference parent Architectural Component ID
- Reference Requirement ID(s)
- Map to Implementation artifact(s)
- Map to Verification Case ID(s)

Design without traceability is invalid.

---

## 7. Implementation Traceability

Each implemented unit SHALL:

- Embed Requirement ID reference
- Embed Architectural Component reference
- Embed Detailed Design reference
- Map to Verification Case ID(s)

Code without traceability markers SHALL block release.

Retroactive traceability insertion after implementation is prohibited.

---

## 8. Verification and Validation Traceability

Each Verification Case ID MUST:

- Reference one or more Requirement IDs
- Identify a method: Test / Analysis / Inspection / Demonstration / Review / Measurement
- Define explicit acceptance criteria
- Record a verification result and evidence reference when executed

When the method is Test, the Verification Case SHALL link to one or more Test Case IDs. A requirement that is not appropriately verified by test SHALL use another justified method; it SHALL NOT be forced into an artificial test.

Each Test Case ID MUST:

- Reference Requirement ID
- Reference its parent Verification Case ID
- Reference Design element
- Reference the planned Implementation target during Test Planning and the actual Implementation artifact before execution closure
- Define explicit expected results or thresholds
- Record test result
- Link to retained evidence in the Verification and Validation Report or another approved evidence artifact

Each Validation Scenario ID MUST:

- Reference a stakeholder need, intended use, operational outcome, or other approved validation basis
- Identify the representative users, operators, environment, and assumptions
- Define validation criteria and record a result
- Link to affected Requirement IDs and retained evidence

A requirement that cannot be verified by any appropriate method is incomplete. A system that cannot be validated against its intended use lacks release evidence.

---

## 9. Deterministic–Probabilistic Boundary Traceability

If probabilistic components exist, the RTM MUST explicitly track:

- Boundary declaration ID
- Validation harness mapping
- Containment enforcement logic
- Fallback mapping
- Observability validation mapping
- Drift detection mapping (if applicable)

Probabilistic behavior SHALL NOT exist outside RTM coverage.

Untracked probabilistic pathways are prohibited.

---

## 10. Change Impact Discipline

When any artifact changes:

- Requirement
- Architecture
- Design
- Implementation
- Test

The RTM SHALL be updated immediately. A material change SHALL reference an approved Change Proposal and Impact Assessment.

Impact analysis SHALL include:

- Downstream artifacts
- Test coverage shifts
- Failure posture impact
- Boundary integrity impact
- Packaging and orchestration implications
- Project Risk Register implications
- Glossary and documentation implications

Unassessed change impact is prohibited.

---

## 11. Orphan Detection

The following conditions SHALL block advancement:

- Requirement without downstream mapping
- Architectural component without requirement mapping
- Design element without architecture parent
- Implementation artifact without requirement reference
- Test case without requirement mapping
- Scope item not present in RTM

Orphaned artifacts are governance violations.

---

## 12. Phase Gate Enforcement

Traceability SHALL be reviewed at:

- Requirements completion
- Architecture completion
- Detailed Design completion
- Pre-Implementation gate
- Pre-verification execution review
- Pre-Packaging gate
- Pre-Release approval

No phase may advance without RTM validation.

RTM review is mandatory at each phase gate.

---

## 13. Versioning and Auditability

The RTM SHALL:

- Include version identifier
- Include last-modified timestamp
- Reflect current lifecycle state
- Preserve lineage where required
- Enable independent audit reconstruction

Opaque lineage is unacceptable.

---

## 14. Refusal Protocol

AI SHALL refuse to:

- Generate artifacts without ID structure
- Accept scope not present in RTM
- Proceed when mappings are incomplete
- Declare verification or validation sufficient without RTM confirmation
- Advance phase without RTM review
- Suppress probabilistic boundary traceability

Refusal preserves structural integrity.

---

## 15. Completion Criteria

Traceability is valid only when:

- All Requirement IDs are mapped
- All Architecture elements are mapped
- All Design elements are mapped
- All Implementation artifacts are mapped
- All Test Cases are mapped to Test-method Verification Cases
- All Verification Cases are mapped with methods and status
- Validation scenarios and status are visible
- Material changes link to Change IDs
- Release-state verification and validation link to approved evidence
- Relevant risks link to Risk IDs
- No orphaned artifacts exist
- Version metadata is present
- Human approval is granted

At release, no required mapping may remain `Pending`.

If any condition is unmet, release is prohibited.

Traceability is the final structural check before controlled progression.

---

End of Guardrail
