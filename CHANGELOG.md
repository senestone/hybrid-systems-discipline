# Changelog

This file records material changes to the Hybrid Systems Discipline Toolkit.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and released versions follow Semantic Versioning as defined by the [Toolkit Release and Compatibility Policy](01-foundations/06-toolkit-release-compatibility-policy.md).

## [Unreleased]

### Added

- Risk-based Baseline, Elevated, and High Assurance governance profiles.
- Governed-increment definition, authority matrix, controlled tailoring, and controlled uncertainty.
- Lifecycle-aware technology-selection status model.
- Verification Case methods and separate intended-use validation scenarios.
- Post-release operational lifecycle governance and expanded Operational Runbook.
- Optional AI Assurance Profile covering data lineage, evaluation, harms, oversight, supplier change, drift, and retirement.
- Executable toolkit conformance validator and continuous-integration workflow.
- Toolkit versioning, compatibility, template-schema, process-assessment, and standards-alignment artifacts.

### Changed

- Corrected the Test Plan gate from Packaging readiness to Test Planning-to-Implementation readiness.
- Reconciled the Test Strategy and Test Case Inventory with the Test Plan.
- Replaced vendor-specific lifecycle restrictions with capability-based controls.
- Corrected stale platform paths and aligned platform instructions.
- Reframed positioning as an extension of established software and systems engineering.
- Reconciled loading guidance with Baseline, Elevated, and High Assurance profiles.
- Refined phase-gate orphan rules to distinguish Verification Cases, Test Cases, and Validation Scenarios.
- Expanded the Test Plan schema with optional failure-coverage, complex fixture/oracle, and execution suspension guidance without adding mandatory companion artifacts.

### Fixed

- Removed the requirement that every requirement map directly to a Test Case ID.
- Made RTM completeness phase-aware while prohibiting unresolved mappings at release.
- Distinguished packaging and clean-build verification from intended-use validation.

### Known Limitations

- The executable validator checks this toolkit repository; it does not yet validate instantiated project artifacts.
- Structural checks do not establish semantic correctness, evidence authenticity, standards conformity, or human approval.
- Toolkit effectiveness has not yet been established through a sufficiently broad body of completed, independently assessed projects.

No version listed above is released until accountable human authority approves the release and creates the corresponding signed or annotated repository tag under the release policy.
