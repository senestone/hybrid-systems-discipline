<!--
File: 01-foundations/06-toolkit-release-compatibility-policy.md

Purpose:
  Define toolkit versioning, release, compatibility, deprecation,
  migration, and instantiated-project upgrade discipline.
-->

# Toolkit Release and Compatibility Policy

## 1. Version Authority

`TOOLKIT_VERSION` is the authoritative working version identifier.

The toolkit uses Semantic Versioning:

- Major: incompatible governance contracts, lifecycle semantics, identifier models, or required artifact structures
- Minor: backward-compatible controls, templates, profiles, checks, or materially expanded guidance
- Patch: backward-compatible corrections and clarifications that do not add a required control

A `-dev` suffix identifies an unreleased development baseline. Development versions SHALL NOT be represented as published releases.

Release authorization, version selection, and tag creation require accountable human approval. Automation MAY verify readiness but SHALL NOT authorize or publish a release independently.

---

## 2. Release Contents

Each release SHALL include:

- Updated `TOOLKIT_VERSION`
- Changelog entry with release date
- Annotated repository tag in the form `vMAJOR.MINOR.PATCH`
- Passing toolkit conformance checks
- Release notes or changelog summary of material controls and fixes
- Compatibility and migration notes for instantiated projects
- Template Schema Registry version
- Known limitations, open risks, and deferred changes
- Human release authority and approval record in the repository's authorized release mechanism

The release tag SHALL identify the immutable toolkit baseline. A branch name or moving commit reference is insufficient for a governed project baseline.

---

## 3. Compatibility Contract

Compatibility is evaluated across:

- Lifecycle sequence and gate semantics
- Governed identifiers and traceability schema
- Required artifacts, fields, and approval records
- Platform-configuration behavioral contracts
- Validator command and supported runtime
- Post-release and optional profile obligations

Patch releases SHALL preserve artifact meaning and required fields.

Minor releases MAY add optional fields, profiles, checks, or backward-compatible required fields with documented defaults and migration guidance.

Major releases MAY change required semantics or remove deprecated behavior. They SHALL include explicit migration guidance and SHALL NOT silently reinterpret previously approved project evidence.

Platform configurations in a release are compatible with that release's lifecycle and template contracts. Mixing platform configurations, guardrails, or templates across toolkit versions requires impact assessment.

---

## 4. Template Schema Discipline

`TEMPLATE-SCHEMAS.md` is the authoritative Template Schema Registry.

Each template has a stable Schema ID and schema version independent of the instantiated artifact's own version. Schema versions use Semantic Versioning according to structural compatibility:

- Major: removes, renames, or changes the meaning of required fields or sections
- Minor: adds fields or sections with documented migration treatment
- Patch: corrects wording or formatting without changing required information

An instantiated project SHALL record:

- Governing toolkit release or approved development commit
- Template Schema Registry version
- Schema ID and version for each governed artifact
- Project-specific artifact version and approval status

Copying a template does not transfer future toolkit changes automatically.

---

## 5. Deprecation

Deprecated controls, fields, templates, and platform contracts SHALL be:

- Marked `Deprecated` with the first deprecated version
- Given a supported replacement or explicit removal rationale
- Assigned a planned removal version or review date
- Retained for at least one minor release when practical
- Covered by migration guidance before removal

Security, legal, safety, or severe-integrity defects MAY require accelerated removal. The release record SHALL explain the exception and affected migration obligations.

---

## 6. Instantiated-Project Upgrade

A project is governed by the toolkit version recorded in its approved Project Governance Profile until an upgrade is approved.

Before upgrading, perform an impact assessment covering:

- Changed lifecycle and gate obligations
- Artifact and schema changes
- Identifier and RTM migration
- Verification, validation, and evidence implications
- Tailoring and authority changes
- Platform configuration compatibility
- Operational and AI-assurance changes
- Previously approved exceptions and residual risks

An upgrade SHALL NOT retroactively invalidate prior human approvals without review. When a new control exposes a material gap, record the gap, assess risk, and disposition it explicitly.

Projects MAY remain on a supported prior release when the rationale, risks, support horizon, and upgrade trigger are documented.

---

## 7. Release Readiness Checklist

- [ ] Version and changelog aligned
- [ ] Template Schema Registry aligned
- [ ] Conformance validator passes locally and in continuous integration
- [ ] Internal links and platform parity pass
- [ ] Compatibility and migration impacts documented
- [ ] Deprecations and known limitations documented
- [ ] Standards references checked for current edition and status
- [ ] No AI system or automation listed as author, contributor, reviewer, approver, or release authority
- [ ] Accountable human release approval recorded
- [ ] Annotated tag created only after approval

---

End of Policy
