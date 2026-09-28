<!--
File: 01-foundations/05-toolkit-usage-model.md

Purpose:
  Define how to operationalize the Hybrid Systems Governance Toolkit
  within AI-assisted development workflows.

This document explains:
  - What artifacts are loaded into the AI agent
  - When they are loaded
  - How enforcement changes by lifecycle phase
  - Minimal vs enterprise operating modes
-->

# Toolkit Usage Model

This toolkit is modular.

Not all files are loaded simultaneously.

The lifecycle is phase-gated.
AI configuration must reflect the current phase.

Improper loading leads to:

- Premature convergence
- Scope drift
- Over-constrained ideation
- Unnecessary verbosity
- Structural enforcement gaps

This document prevents that.

---

# 1. Core Bootstrap Set (Always Loaded)

At minimum, load:

- 02-governance/00-lifecycle-bootstrap.md
- 02-governance/13-tailoring-and-authority-guardrail.md
- Active Project Governance Profile
- 05-platform-config/<agent-config>.md
- 05-platform-config/enterprise-system-prompt.md

This establishes:

- Lifecycle sequencing authority
- AI behavioral enforcement
- Refusal protocol
- Rollback rules

No phase-specific specification templates are required during ideation. Cross-lifecycle control templates remain applicable when their triggers occur.

The Project Glossary template MAY be loaded during Ideation when controlled terminology, abbreviations, or acronyms begin to emerge.

The Project Risk Register template SHALL be loaded when risks, assumptions, issues, or dependencies are identified. Once created, the active register remains available throughout the lifecycle.

The Change Proposal and Impact Assessment template SHALL be loaded whenever a proposed change may affect an approved artifact, lifecycle boundary, validation obligation, or release posture.

The Work Effort Log template MAY be loaded in any phase when the project elects to measure human effort. It is a planning and audit-support artifact, not a phase-gate deliverable or evidence of engineering quality.

The approved Project Governance Profile SHALL remain available throughout the governed increment. It defines scope, tailoring, authority assignments, review independence, and evidence obligations.

The Technology Selection Record and review checklist MAY be loaded in any phase where a material technology hypothesis, candidate, investigation, or baseline affects authorized work. The record's status SHALL match the current lifecycle authority; prototype evidence does not authorize production use.

---

# 2. Phase-Specific Loading Model

## Phase 1 — Ideation

Load:

- Lifecycle Bootstrap
- Enterprise System Prompt
- Platform configuration
- Project Governance Profile template
- Project Glossary template when terminology is being formalized
- Project Risk Register template

Do NOT load:

- SRS template
- Architecture template
- RTM template
- Test plan template
- Packaging template

Purpose:
Allow structured exploration without premature formalization.

---

## Phase 2 — Requirements (SRS)

Load:

- Lifecycle Bootstrap
- SRS template
- Traceability template (optional scaffold)
- Project Glossary template
- Active Project Risk Register
- Change Proposal and Impact Assessment template when approved requirements or scope may change
- Enterprise System Prompt
- Platform config

Do NOT load:

- Architecture template (until approved)
- Implementation artifacts
- Packaging template

Purpose:
Define "what" without embedding structure.

---

## Phase 3 — High-Level Architecture

Load:

- Lifecycle Bootstrap
- Approved SRS
- Architecture template
- RTM template
- Active Project Glossary
- Active Project Risk Register
- Change Proposal and Impact Assessment template when an approved artifact may change
- Enterprise System Prompt
- Platform config

Purpose:
Map structure to requirements.

---

## Phase 4 — Detailed Design

Load:

- Lifecycle Bootstrap
- Approved SRS
- Approved HLA
- Detailed Design template
- RTM template
- Active Project Glossary
- Active Project Risk Register
- Change Proposal and Impact Assessment template when an approved artifact may change
- Enterprise System Prompt
- Platform config

Purpose:
Refine structure without altering architecture.

---

## Phase 5 — Traceability Consolidation

Load:

- RTM template
- Approved SRS
- HLA
- Detailed Design
- Lifecycle Bootstrap
- Active Project Glossary
- Active Project Risk Register
- Active Change Proposal and Impact Assessments

Purpose:
Confirm structural completeness before implementation.

---

## Phase 6 — Test Planning

Load:

- Test Plan template
- Approved SRS
- RTM
- Lifecycle Bootstrap
- Enterprise System Prompt
- Active Project Glossary
- Active Project Risk Register
- Active Change Proposal and Impact Assessments

Purpose:
Define verification methods, test coverage, and system-validation scenarios prior to implementation.

---

## Phase 7 — Implementation

Load:

- Lifecycle Bootstrap
- Approved SRS
- HLA
- Detailed Design
- Test Plan
- RTM
- Active Project Glossary
- Active Project Risk Register
- Active Change Proposal and Impact Assessments
- Verification and Validation Report template when recording executed results
- Platform configuration
- Implementation-capable platform configuration (for example, Cursor rules when using Cursor)
- Technology selection record and review checklist when a material implementation choice is pending

Purpose:
Controlled execution with traceability preservation.

---

## Phase 8 — Packaging and Orchestration

Load:

- Packaging template
- Test Plan
- RTM
- Lifecycle Bootstrap
- Active Project Glossary
- Active Project Risk Register
- Active Change Proposal and Impact Assessments
- Verification and Validation Report

Purpose:
Enforce reproducibility and release gating.

---

## Phase 9 — Documentation Closure

Load:

- System Documentation Package template
- Applicable Documentation deliverable templates
- RTM release snapshot
- Packaging plan
- Active Project Glossary
- Active Project Risk Register
- Closed or release-relevant Change Proposal and Impact Assessments
- Approved Verification and Validation Report
- Lifecycle Bootstrap

Purpose:
Align delivered system to governance artifacts.

---

# 3. Minimal Mode vs Enterprise Mode

## Minimal Mode

Load:

- Lifecycle Bootstrap
- Platform config
- Current phase template only
- Active cross-lifecycle control artifacts when applicable

Use for:
- Smaller teams
- Internal projects
- Low regulatory pressure

---

## Enterprise Mode

Load:

- Lifecycle Bootstrap
- All relevant guardrails
- Enterprise System Prompt
- Platform configuration
- Active phase template
- RTM (from Architecture onward)

Use for:
- Regulated environments
- External-facing products
- AI-integrated systems
- High audit exposure

---

# 4. Agent Capability Rules

Agent access and actions SHALL be governed by capability and current lifecycle phase, not by vendor or product name.

Before Implementation authorization, agents SHALL NOT generate, modify, or refactor implementation code. They MAY support authorized lifecycle work such as ideation, requirements, architecture, design, traceability, and test planning when the active platform configuration enforces the applicable phase guardrail.

During Implementation, code-generation and code-modification capabilities MAY be used only within approved requirements, architecture, design, traceability, and test constraints.

During Packaging and Orchestration or Documentation Closure, agent actions SHALL remain limited to the artifacts and changes authorized for that phase. Access to implementation capabilities does not authorize implementation changes or lifecycle advancement.

Platform-specific configurations, including `05-platform-config/cursor-rules.md`, SHALL implement these capability controls without overriding lifecycle authority.

---

# 5. Deterministic–Probabilistic Systems

If probabilistic components exist:

Beginning at Architecture phase, always load:

- RTM template
- Guardrails governing probabilistic boundaries
- Enterprise System Prompt

Do NOT defer boundary governance to implementation.

Containment is structural.

---

# 6. What Not to Do

Do not:

- Load all templates simultaneously during ideation
- Generate implementation before Detailed Design approval
- Skip RTM alignment prior to implementation
- Package without clean build validation
- Allow AI to redefine scope silently
- Suppress refusal protocol for speed

---

# 7. Operational Summary

The toolkit is:

- Phase-gated
- Artifact-driven
- Traceability-enforced
- Reproducibility-focused
- AI-aware
- Release-gated

It is not a prompt library.

It is a lifecycle control system.

Correct loading is part of governance.

---

End of Toolkit Usage Model
