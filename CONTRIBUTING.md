# Contributing

This toolkit is a governance artifact. Contributions should preserve lifecycle discipline, traceability, phase-gate authority, and human accountability.

## Contribution Standards

When proposing changes:

- Preserve lifecycle authority in `02-governance/00-lifecycle-bootstrap.md`.
- Keep phase-specific guardrails aligned with the lifecycle sequence.
- Keep templates, platform configuration, and repository agent guidance consistent.
- Avoid weakening traceability, packaging, testing, documentation, or human approval requirements.
- Distinguish defects from risks, uncertainties, tradeoffs, and preferences.
- Preserve epistemic qualifiers when revising user-facing or agent-facing guidance.

Changes that affect lifecycle behavior should identify the impacted files and explain whether corresponding templates, platform configs, or agent instructions also need updates.

## Instruction Maintenance

The repository contains standing instructions for adversarial collaboration, epistemic fidelity, authorship, attribution, and source-control metadata.

Treat the README's `AI Assistant Configuration` section and root `AGENTS.md` as the user-facing and repository-agent sources of truth.

When updating these instructions:

- Update the README guidance first.
- Propagate equivalent wording to `AGENTS.md`.
- Propagate equivalent wording to platform configuration files under `05-platform-config/`.
- Update `01-foundations/02-ai-operating-rules.md` when the change affects general AI agent behavior.
- Update templates under `04-templates/` when the change affects artifact fields, approval fields, attribution, or generated deliverables.
- Do not maintain multiple paraphrased versions unless a field has a strict length limit.
- If a shorter version is required, preserve the core principles.

For adversarial collaboration and epistemic fidelity, the core principles are:

- Challenge reasoning, assumptions, architecture, conclusions, plans, tradeoffs, weak evidence, edge cases, and plausible failure modes when useful.
- Preserve stated certainty and epistemic qualifiers.
- Distinguish speculation, hypothesis, inference, approximation, tentative belief, preference, and assertion.
- Do not strengthen a qualified statement into a categorical claim before challenging it.
- Critique the claim actually made.

For authorship and attribution, the core principles are:

- AI agents, assistants, models, tools, and automation must not claim authorship, ownership, preparation credit, contribution credit, maintenance responsibility, approval authority, or other attribution.
- Authorship, maintainer, owner, preparer, contributor, reviewer, approver, and equivalent fields must identify accountable humans, teams, roles, or organizations only.
- AI systems must not appear as authors, co-authors, committers, signers, reviewers, or attribution recipients in source control commits, commit messages, commit trailers, tags, changelogs, release logs, repository logs, or version-control metadata.
- If AI assistance must be disclosed for process, audit, or compliance reasons, record it as tooling or process context, not as authorship or attribution.

## Versioning Guidance

Use a simple version number whenever standing instruction wording changes, such as `1.0`, `1.1`, and `2.0`.

Suggested changelog format:

```text
Version 1.1 - YYYY-MM-DD
- Clarified that hypotheses should be challenged as hypotheses, not treated as assertions.
- Added instruction to distinguish defects from tradeoffs and uncertainty.
```

Review instruction wording after recurring failure patterns, especially cases where an assistant either over-agrees or challenges a stronger claim than the one actually made.

## Verification Checklist

Use this checklist after revising standing assistant instructions or attribution rules.

- The instruction explicitly permits challenge, counterargument, devil's-advocate review, and failure-mode analysis.
- The instruction does not ask the assistant to become more agreeable or less critical.
- The instruction explicitly preserves qualifiers and stated certainty.
- The instruction distinguishes speculation, hypothesis, inference, approximation, tentative belief, preference, and assertion.
- The instruction says not to strengthen qualified claims into categorical claims before challenging them.
- README, ChatGPT desktop guidance, ChatGPT Work guidance, platform configs, and repository guidance use the same canonical wording or a faithful shortened form.
- `AGENTS.md` includes `Review Behavior` guidance or an equivalent with both adversarial collaboration and epistemic fidelity intact.
- Artifact templates and persistent assistant instructions prevent AI systems from claiming authorship, ownership, maintenance responsibility, approval authority, source-control authorship, commit attribution, or equivalent attribution.

## Commit Metadata

Source control metadata must preserve human accountability.

- Do not list AI agents, assistants, models, tools, or automation as commit authors, co-authors, committers, signers, reviewers, or attribution recipients.
- Do not add AI attribution trailers such as `Co-authored-by`, `Generated-by`, or equivalent tool-credit metadata for AI systems.
- Commit messages should describe the change and its governance impact without attributing authorship or credit to AI tooling.
