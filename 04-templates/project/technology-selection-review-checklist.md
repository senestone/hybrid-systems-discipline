<!--
File: 04-templates/project/technology-selection-review-checklist.md

Purpose:
  Review a technology selection record before it becomes an approved
  implementation-planning baseline.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Technology Selection Review Checklist

Apply this checklist to a completed [technology selection record](technology-selection-template.md). It supplements the applicable phase gate; it does not authorize a new lifecycle phase.

For a Proposed record, mark downstream items `Pending` with an owner and revisit point. All applicable items must be satisfied before the record becomes an Approved implementation baseline.

## Authority

- [ ] The current lifecycle phase and approving owner are identified.
- [ ] Available Requirements, Architecture, Detailed Design, and RTM versions are linked; missing downstream versions are identified and resolved before approval.
- [ ] The Test Planning to Implementation gate is approved before a material implementation choice becomes a baseline; any earlier requirement-mandated choice follows its applicable phase guardrail.
- [ ] The proposed choice does not silently change an approved boundary or requirement.
- [ ] Any required rollback and renewed approval are identified before adoption.

## Comparison

- [ ] The decision scope and explicit non-decisions are clear.
- [ ] Hard constraints are separated from preferences and provisional targets.
- [ ] Credible alternatives, including the incumbent where applicable, use the same criteria.
- [ ] Dependency, license, platform, build, distribution, and maintenance costs are considered where relevant.
- [ ] Evidence links point to actual sources or reproducible experiments, not just a summary.

## Validation

- [ ] A narrow prototype tests the highest-risk claims when documentation alone is insufficient.
- [ ] Failures, rollback, recovery, and trust-boundary behavior are exercised where applicable.
- [ ] Unmeasured properties are marked unknown; no result is generalized beyond its test environment.
- [ ] Remaining tests, owners, and revisit triggers are explicit.

## Traceability and Decision

- [ ] Requirement IDs are mapped to the decision and evidence; Test Case IDs are added when defined and before approval for implementation.
- [ ] RTM, design, implementation, packaging, orchestration, and system-documentation impacts are stated.
- [ ] The choice, rejected alternatives, rationale, residual risks, and approval are recorded in the [project decision log](decision-log-template.md), with links in both directions.
- [ ] The record distinguishes Proposed, Approved, and Superseded states.
