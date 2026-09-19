# Hybrid Systems Discipline Toolkit

Specification-Driven AI Collaboration and Architectural Discipline  
for Hybrid Deterministic–Probabilistic Systems

---

## Overview

Modern enterprise systems are no longer purely deterministic.

They increasingly integrate deterministic subsystems with probabilistic components such as large language models, retrieval systems, ranking engines, and generative pipelines.

Hybrid systems inherit the properties — and failure modes — of both modalities.

Traditional SDLC models were not designed to govern probabilistic behavior.

This toolkit provides structured lifecycle discipline for integrating probabilistic systems into deterministic architectures without sacrificing rigor, traceability, auditability, or economic control.

This toolkit is development-model neutral. It provides governance, traceability, artifact discipline, and phase-gate controls that may be applied within iterative, spiral, agile, waterfall, or hybrid processes. Its phases represent stabilization checkpoints for artifacts and decisions, not a mandate for linear, one-pass delivery.

The toolkit governs decision readiness, artifact integrity, and traceability continuity. It does not prescribe sprint structure, implementation cadence, team ceremonies, or delivery mechanics. Teams may implement incrementally, iteratively, or continuously so long as requirements, architecture, design, validation, and release evidence remain coherent.

This is not a prompt library.  
This is not a productivity hack collection.  
This is not a replacement for engineering judgment.

It is a lifecycle governance operating system for hybrid systems.

---

## Why This Exists

AI-assisted development has changed the structural risk profile of software engineering.

Code can now be generated faster than it can be structurally reviewed.

Without explicit governance:

- Requirements drift silently
- Architecture erodes incrementally
- Probabilistic components expand beyond defined boundaries
- Tests lag implementation
- Packaging becomes environment-specific and fragile
- Traceability becomes aspirational rather than enforced

Speed without structural discipline becomes systemic risk.

This toolkit establishes the missing governance layer.

---

## What This Toolkit Provides

This repository defines:

- A constitutional lifecycle authority
- Phase-gated advancement control
- Deterministic–probabilistic boundary containment
- Mandatory bidirectional traceability
- Explicit rollback authority
- Reproducible packaging enforcement
- Release gating tied to validation and documentation
- AI agent behavioral enforcement alignment

Governance integrity overrides conversational flow.

---

## How This Toolkit Is Used

The toolkit is modular and phase-gated.

It is not intended to be loaded wholesale into an AI system.

Instead:

- The **Lifecycle Bootstrap** establishes sequencing authority.
- Phase-specific templates are loaded only during the relevant lifecycle stage.
- The **Enterprise System Prompt** governs AI behavior.
- Platform configurations enforce discipline during implementation.
- The **Traceability Matrix** enforces structural completeness before release.

Correct loading is part of governance.

See the [Toolkit Usage Model](01-foundations/05-toolkit-usage-model.md) for operational guidance.

---

## Intended Audience

This toolkit is designed for:

- Engineering leaders responsible for AI integration
- System architects designing hybrid deterministic–probabilistic systems
- Technical program managers overseeing AI-enabled workflows
- Governance and risk professionals managing AI-related operational risk
- Organizations transitioning from experimentation to institutional integration

It assumes professional accountability and structured review processes.

It is not optimized for informal prototyping.

---

## Repository Structure

### 01 — Foundations

Conceptual, strategic, and operational posture:

- `00-whitepaper.md`
- `01-executive-positioning.md`
- `02-ai-operating-rules.md`
- `03-debug-triage-playbook.md`
- `04-pilot-program-guide.md`
- `05-toolkit-usage-model.md`

These documents define why the discipline exists and how it is operationalized.

---

### 02 — Governance

Constitutional lifecycle control and guardrails:

- [Lifecycle Bootstrap](02-governance/00-lifecycle-bootstrap.md) (authoritative sequencing control)
- Phase-specific guardrails:
  - Ideation
  - Requirements
  - Architecture
  - Detailed Design
  - Implementation
  - Code Documentation
  - System Documentation
  - Test
  - Traceability
  - Packaging
  - Orchestration
- [Phase Gate Checklist](02-governance/12-phase-gate-checklist.md)

The [Guardrails Index](02-governance/guardrails-index.md) links every phase guardrail.

Guardrails enforce behavior within phases.  
Lifecycle sequencing authority resides in the Bootstrap.

---

### 03 — Executive

Strategic framing for institutional adoption:

- Executive Positioning
- Executive Adoption Overview

Supports leadership-level governance alignment and integration maturity planning.

---

### 04 — Templates

Structured execution artifacts.

**Project Templates**
- [Project Primer](04-templates/project/project-primer-template.md): intent and scope during Ideation.
- [Decision Log](04-templates/project/decision-log-template.md): approved decisions, authority, and change lineage across phases.
- [Daily Log](04-templates/project/daily-log-template.md): phase status, work, issues, and traceability updates.
- [Technology Selection Record](04-templates/project/technology-selection-template.md): evidence and impacts for material implementation choices; link its ID to the Decision Log.
- [Technology Selection Review Checklist](04-templates/project/technology-selection-review-checklist.md): review the selection record before approval and adoption.
- [Work Effort Log](04-templates/project/work-effort-log-template.md): measured human effort with artifact or commit links, separate from the Daily Log.

Create project-specific copies of these templates. Use stable IDs and links between a technology selection record, its Decision Log entry, and the affected Requirements, Architecture, Detailed Design, RTM, Test Plan, and release artifacts. Mark downstream references pending until that phase produces them; resolve them before the applicable approval gate. The [Lifecycle Bootstrap](02-governance/00-lifecycle-bootstrap.md) and [Phase Gate Checklist](02-governance/12-phase-gate-checklist.md) govern when those links become required.

**System Templates**
- [Requirements](04-templates/system/requirements-template.md)
- [Architecture](04-templates/system/architecture-template.md)
- [Detailed Design](04-templates/system/detailed-design-template.md)
- [Traceability Matrix](04-templates/system/traceability-matrix-template.md)
- [Test Plan](04-templates/system/test-plan-template.md)
- [Packaging Plan](04-templates/system/packaging-plan-template.md)

**Documentation Templates**
- [System Documentation Package](04-templates/documentation/system-documentation-package-template.md)
- [System Overview](04-templates/documentation/system-overview-template.md)
- [Installation Guide](04-templates/documentation/installation-guide-template.md)
- [User Guide](04-templates/documentation/user-guide-template.md)
- [Administration Guide](04-templates/documentation/administration-guide-template.md)
- [Online Help / In-Product Help](04-templates/documentation/online-help-template.md)
- [Release Notes](04-templates/documentation/release-notes-template.md)
- [Operational Runbook](04-templates/documentation/operational-runbook-template.md)

Templates convert abstract discipline into executable structure.

---

### 05 — Platform Configuration

AI-assisted environment enforcement:

- ChatGPT configuration
- Claude configuration
- Gemini configuration
- Cursor rules
- Enterprise system prompt

These files align AI behavior with lifecycle governance.

The discipline is platform-agnostic.  
Tool configuration follows architecture — never the reverse.

---

## AI Assistant Configuration

AI assistants used with this toolkit should be configured as disciplined engineering collaborators, not passive agreement engines or unbounded code generators.

Use the platform files in `05-platform-config/` where supported. For tools that support persistent user, project, workspace, or repository instructions, include the following collaboration rule.

```text
Adversarial Collaboration and Epistemic Fidelity

Act as an adversarial collaborator when it improves the work. Challenge my reasoning, assumptions, architecture, conclusions, plans, and tradeoffs when useful. Identify counterarguments, hidden assumptions, weak evidence, edge cases, and plausible failure modes. Do not default to agreement, and do not dilute strategic devil's-advocate review when the stakes, ambiguity, or design surface justify it.

At the same time, preserve epistemic fidelity when interpreting what I say. Keep my stated degree of certainty intact. Distinguish speculation, hypothesis, inference, approximation, tentative belief, preference, and assertion. Do not strengthen a qualified statement into a categorical claim before challenging it. Critique the claim actually made, not a more absolute version of it.

In short: be adversarial about reasoning, but conservative about interpreting intent.
```

For constrained instruction fields, use this shorter form:

```text
Use adversarial collaboration without weakening epistemic fidelity: challenge my reasoning, assumptions, architecture, conclusions, and failure modes when useful, but preserve my qualifiers and certainty level. Do not turn speculation, hypotheses, approximations, or tentative inferences into categorical claims before challenging them. Critique what I actually claimed.
```

### ChatGPT Desktop Client

Place the collaboration rule in the most durable available personalization mechanism, such as Custom Instructions, Personalization, Memory summary, or an equivalent persistent instruction area.

Suggested placement:

- Put the full rule in the section that describes how ChatGPT should respond.
- If space is limited, use the short form.
- When Memory is available and appropriate, ask ChatGPT to remember this as a standing interaction preference.

### ChatGPT Work Projects and Workspaces

Add the collaboration rule to project-level or workspace-level instructions where engineering, product, research, governance, or strategy work is discussed.

Recommended placement:

- Add it under `Collaboration Style`, `Review Standards`, or `Reasoning Expectations`.
- Use the full rule for shared workspaces where multiple assistants or tasks may rely on the same expectations.
- Keep it separate from coding conventions, security rules, and delivery requirements so future edits do not weaken it accidentally.

For shared project review, also include:

```text
When reviewing project work, distinguish defects from risks, uncertainties, preferences, and tradeoffs. Preserve the author's level of confidence while still surfacing strong counterarguments and failure modes.
```

### Repository Agents

For Codex or other repository-aware agents, use the root `AGENTS.md` file as the repository-level behavioral contract.

Repository agents must:

- Follow lifecycle authority in `02-governance/00-lifecycle-bootstrap.md`.
- Apply the relevant phase guardrail from `02-governance/`.
- Preserve traceability discipline and human gate authority.
- Use adversarial collaboration while preserving epistemic fidelity.
- Avoid turning qualified claims into stronger claims before critique.

For monorepos or nested workspaces, keep root `AGENTS.md` canonical and add narrower local guidance only when a subproject genuinely requires different behavior.

### Authorship and Attribution

AI agents, assistants, models, tools, and automation must not claim authorship, ownership, preparation credit, contribution credit, maintenance responsibility, approval authority, or other attribution in artifacts.

Artifact fields such as `Author(s)`, `Author`, `Maintainer`, `Prepared By`, `Created By`, `Owner`, `Contributor`, and equivalent attribution fields must identify accountable humans, teams, roles, or organizations only.

Do not insert phrases such as "created by ChatGPT," "generated by Claude," "authored by Codex," or equivalent AI attribution into documents, source headers, templates, release notes, logs, diagrams, generated reports, or metadata.

AI agents, assistants, models, tools, and automation must also not appear as authors, co-authors, committers, signers, reviewers, or attribution recipients in source control commits, commit messages, commit trailers, tags, changelogs, release logs, repository logs, or version-control metadata.

If AI assistance must be disclosed for process, audit, or compliance reasons, record it as tooling or process context, not as authorship or attribution.

---

## Governance Model

The lifecycle is mandatory and phase-gated at the governance level:

1. Ideation  
2. Requirements (SRS)  
3. High-Level Architecture  
4. Detailed Design  
5. Traceability Consolidation  
6. Test Planning  
7. Implementation  
8. Packaging and Orchestration  
9. Documentation Closure  

No governance phase may be skipped or collapsed without explicit authorization.

This does not require waterfall implementation. It requires that implementation not be used as a substitute for unresolved ideation, requirements, architecture, design, traceability, or validation work.

Release is prohibited without:

- Traceability completion
- Clean build reproducibility
- Packaging validation
- Documentation alignment
- Human approval

Rollback is mandatory when structural changes occur.

---

## Relationship to the White Paper

The white paper establishes:

- Modality divergence between deterministic and probabilistic systems
- Failure mode inheritance
- The absence of intrinsic mechanistic verification in probabilistic systems
- The need for compensating verification architecture
- The economic consequences of modality misuse

This toolkit operationalizes those principles.

---

## Recommended Adoption Path

For organizations new to hybrid discipline:

1. Read the white paper.
2. Establish the Lifecycle Bootstrap as authoritative.
3. Implement Requirements and Architecture guardrails first.
4. Introduce traceability enforcement.
5. Enforce Phase Gates before scaling.
6. Introduce pilot programs.
7. Align AI platform configurations last.

Do not begin with platform configuration files.

Architecture precedes acceleration.

---

## Contributing

See `CONTRIBUTING.md` for contribution standards, instruction maintenance guidance, verification checks, and source-control attribution rules.

---

## What This Toolkit Is Not

- Not a collection of isolated prompts
- Not a substitute for engineering judgment
- Not a rapid prototype accelerator
- Not a marketing artifact

It is structural risk management for hybrid systems.

---

## Licensing

Copyright (c) 2026 Charles McKnight

Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).

You are free to share and adapt this material for any purpose, including commercial use, provided appropriate attribution is given and adaptations are distributed under the same license.

See the LICENSE file for full details.

---

## Attribution

If you use or adapt this toolkit, please attribute as:

> Charles McKnight, *Hybrid Systems Discipline Toolkit* (2026)

Citation of the white paper is encouraged where appropriate.

---

## Maturity Notice

This toolkit reflects hybrid system governance practices as of 2026.

As probabilistic systems evolve — including advances in explainability and containment techniques — implementation patterns may adapt.

The foundational principle remains durable:

**Hybrid systems require explicit architectural discipline.**

---

## Contact

For discussion, collaboration, or speaking inquiries:

charles.mcknight@senestone.com
