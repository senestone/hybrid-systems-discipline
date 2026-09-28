<!--
File: 02-governance/00-lifecycle-bootstrap.md

Purpose:
  Establish lifecycle authority and enforce disciplined,
  phase-gated progression across hybrid deterministic–probabilistic systems.

This document is the constitutional lifecycle authority for the toolkit.

All guardrails, templates, and platform configurations defer to this document.

This document governs:
- Phase sequencing
- Advancement control
- Rollback authority
- Traceability enforcement
- Packaging and release gating
- Deterministic–probabilistic boundary governance
-->

# Project Lifecycle Bootstrap

This document defines the mandatory lifecycle sequence and enforcement model.

This toolkit is development-model neutral. It provides governance, traceability, artifact discipline, and phase-gate controls that may be applied within iterative, spiral, agile, waterfall, or hybrid processes. Its phases represent stabilization checkpoints for artifacts and decisions, not a mandate for linear, one-pass delivery.

Lifecycle sequencing authority resides here.

Guardrails define phase-specific behavior.  
Templates define structural artifacts.  
Platform configurations enforce behavioral compliance.  

This document defines advancement authority and structural integrity rules.

Explicit human approval is required to advance between phases.

No implicit advancement is permitted.

---

# 1. Authority Hierarchy

The following hierarchy governs lifecycle control:

1. This document (00-lifecycle-bootstrap.md)
2. Guardrails under 02-governance/
3. Lifecycle templates under 04-templates/
4. Platform-specific AI configurations
5. Project-level artifacts

If conflict occurs, defer upward in this hierarchy.

No artifact may override lifecycle sequencing authority.

---

# 2. Mandatory Lifecycle Sequence

Projects SHALL follow this order:

1. Ideation  
2. Requirements (SRS)  
3. High-Level Architecture (HLA)  
4. Detailed Design (DD)  
5. Traceability Consolidation (RTM alignment)  
6. Test Planning and Definition  
7. Implementation  
8. Packaging and Orchestration  
9. Documentation Alignment and Closure  

No phase may be skipped, collapsed, merged, or reordered without explicit human authorization.

## 2.1 Governed Increment Application

The lifecycle applies to a bounded governed increment, which MAY be a product, release, capability, feature set, change, or architectural increment.

Each governed increment SHALL have:

- A stable identifier and explicit scope boundary
- Approved baselines appropriate to its current phase
- End-to-end traceability for included scope
- Defined verification, validation, release, and operational obligations
- An approved Project Governance Profile identifying tailoring decisions and human authority roles

A project need not fully specify its entire future product before implementation of an authorized increment begins. Scope outside the governed increment SHALL remain excluded, deferred, or controlled through an approved change.

The lifecycle sequence SHALL be completed for each governed increment. Iteration within a phase and repetition across increments are permitted; implicit phase skipping is not.

---

# 3. Phase Gate Model

Each phase requires:

- Defined objectives
- Defined deliverables
- Defined exit criteria
- Explicit human authorization before advancement

Phase exit without authorization is prohibited.

Release without phase completion is prohibited.

---

# 4. Advancement Rules

The AI agent must:

- Identify current lifecycle phase
- Verify required artifacts exist and are approved
- Confirm RTM alignment where applicable
- Refuse premature advancement
- Surface lifecycle violations explicitly

Silence is not compliance.

Material ambiguity or uncertainty requires explicit control.

Unresolved material uncertainty SHALL be recorded with a stable Risk, Assumption, Issue, or Dependency ID; bounded by its possible downstream effect; assigned to an accountable human role; and given a resolution, monitoring, or disposition plan.

Advancement is prohibited when unresolved uncertainty could invalidate downstream work. Non-material residual uncertainty MAY remain when it is explicit, bounded, linked to affected artifacts, and accepted within the approving role's authority.

---

# 5. Rollback Authority

If any of the following occur:

- Scope change
- Requirement modification
- Architectural modification
- Design boundary alteration
- Deterministic–probabilistic boundary change
- Packaging change impacting behavior
- Test coverage regression
- RTM traceability gap

Then:

- A Change Proposal and Impact Assessment SHALL identify the affected artifacts, risks, validation obligations, and earliest impacted phase.
- The lifecycle SHALL roll back to the earliest impacted phase.
- RTM SHALL be updated.
- Decision Log SHALL record the change.
- Project Risk Register SHALL be updated when risk, assumption, issue, or dependency posture changes.
- Human reauthorization SHALL be required.

Untracked structural change is prohibited.

---

# 6. Deterministic–Probabilistic Governance

If probabilistic subsystems exist, the lifecycle SHALL enforce:

- Explicit boundary declaration
- Validation harness specification
- Containment logic definition
- Fallback behavior definition
- Observability controls
- Reproducibility considerations
- RTM boundary mapping

Unbounded probabilistic integration is prohibited.

Containment integrity overrides speed.

---

# 7. Traceability Authority

The Requirements Traceability Matrix (RTM) is mandatory.

The lifecycle SHALL ensure:

- 100% Requirement coverage
- 100% Architecture mapping
- 100% Design mapping
- 100% Implementation mapping
- 100% Verification Case mapping with an appropriate verification method
- Packaging traceability
- Orchestration traceability

Orphan artifacts block advancement.

Traceability gaps block release.

---

# 8. Verification and Validation Authority

Verification establishes objective evidence that specified requirements are fulfilled. Permitted methods include Test, Analysis, Inspection, Demonstration, Review, and Measurement. Each Requirement ID SHALL map to at least one Verification Case ID and an appropriate method.

Validation establishes objective evidence that the delivered system supports stakeholder needs, intended use, and the operational context. Validation SHALL be planned and traced separately from requirement verification.

Testing SHALL verify:

- All Functional Requirements
- All Critical Non-Functional Requirements
- Failure modes
- Edge conditions
- Deterministic–probabilistic containment
- Clean build reproducibility
- Packaging integrity

Passing tests are mandatory before Packaging.

Testing without traceability is invalid.

Testing is a major verification method. It SHALL NOT be treated as synonymous with all verification or with validation.

Executed results, deviations, evidence references, residual risks, and release recommendation SHALL be recorded in a Verification and Validation Report.

---

# 9. Packaging and Release Gating

Before release authorization:

- Clean build reproducibility verified
- Artifact integrity validated
- Version alignment confirmed
- Deterministic–probabilistic containment preserved
- Verification and Validation Report approved as an accurate evidence record
- Open release-relevant risks reviewed and explicitly dispositioned
- RTM release snapshot finalized
- Documentation aligned

Release without packaging verification is prohibited.

Release without RTM finalization is prohibited.

Release without documentation closure is prohibited.

---

# 10. Documentation Closure

Lifecycle completion requires:

- Updated system documentation
- Updated architecture summary
- Updated packaging details
- Updated project glossary for the governed project instance
- Current Project Risk Register with release-relevant items dispositioned
- Approved Verification and Validation Report
- Closed or explicitly carried-forward release-relevant change assessments
- Final RTM snapshot
- Formal human approval

Lifecycle is complete only after documentation approval.

## 10.1 Post-Release Operational Continuity

Release and documentation closure complete a governed development increment; they do not terminate governance of the deployed or supported system.

After release, the Operational Lifecycle Guardrail SHALL govern deployment transition, operations, monitoring, incidents, maintenance, drift, deprecation, data disposition, and retirement.

Material post-release change SHALL define a new governed increment and return to the earliest affected lifecycle phase. Operational urgency may invoke only an approved, bounded emergency pathway with evidence capture and retrospective impact assessment.

Operational acceptance, risk acceptance, emergency authority, suspension, and retirement remain human decisions.

---

# 11. Governance Principles

This lifecycle model exists to:

- Prevent architectural drift
- Prevent scope expansion without review
- Preserve traceability
- Enforce reproducibility
- Bound probabilistic systems
- Reduce systemic risk
- Enable audit reconstruction
- Support enterprise-scale delivery

Lifecycle discipline is structural risk management.

---

# 12. Operational Directive

The AI agent SHALL:

- Maintain lifecycle awareness at all times
- Prevent premature progression
- Enforce rollback when required
- Preserve traceability integrity
- Preserve glossary and terminology integrity
- Preserve change-impact, risk, and verification-evidence integrity
- Promote reproducibility
- Preserve deterministic–probabilistic containment
- Maintain professional tone
- Refuse shortcuts that violate governance

Governance integrity overrides conversational flow.

---

End of Lifecycle Bootstrap
