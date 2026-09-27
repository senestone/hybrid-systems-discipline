<!--
File: 04-templates/project/project-glossary-template.md

Purpose:
  Provide a reusable governed glossary template for normative terms,
  phrases, abbreviations, and acronyms used by projects instantiated
  from this toolkit.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md

An instantiated Project Glossary preserves semantic consistency.
It does not replace requirements, architecture, design, traceability,
or approval artifacts.
-->

# Project Glossary

Project Name:
Version:
Date (YYYY-MM-DD):
Author(s):
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Status: Draft / Approved
Lifecycle Phase:
RTM Version Reference:

---

# 1. Glossary Authority Declaration

Confirm:

- Project glossary created? (Yes / No)
- Current lifecycle phase identified? (Yes / No)
- Glossary version referenced by active lifecycle artifacts? (Yes / No)
- New terminology reviewed for ambiguity? (Yes / No)
- Acronyms and abbreviations linked on first use in active documents? (Yes / No)

If any answer is "No," glossary alignment is incomplete.

---

# 2. Scope

This glossary SHALL include:

- Normative terms and phrases that carry controlled meaning
- Domain-specific terms requiring consistent interpretation
- Abbreviations
- Acronyms
- Lifecycle, governance, or artifact terms used across documents

This glossary SHALL NOT include:

- Generic dictionary words with no project-specific meaning
- Terms used only once and not needed for interpretation
- Implementation identifiers unless they affect document meaning
- Informal aliases that are not approved terminology

Terminology that changes requirement, architecture, design, test, packaging, or documentation meaning SHALL trigger impact review.

---

# 3. Link and Anchor Convention

Each glossary entry SHALL have a stable anchor identifier.

Use the following anchor prefixes:

- `term-` for normative or domain terms
- `abbr-` for abbreviations
- `acr-` for acronyms

Examples:

- `term-controlled-artifact`
- `abbr-config`
- `acr-rtm`

Documents SHALL link the first appearance of each acronym or abbreviation to the corresponding glossary entry.

Documents SHOULD link the first appearance of a normative term or phrase when the term has a controlled glossary meaning.

Subsequent uses MAY remain unlinked unless additional clarity is needed.

---

# 4. Normative Terms and Phrases

| Anchor ID | Term / Phrase | Definition | Normative Force | First Introduced In | Related Artifact ID(s) | Status | Notes |
|-----------|---------------|------------|-----------------|---------------------|-------------------------|--------|-------|
| term-example | Example Term | Controlled meaning used by the project. | SHALL / SHOULD / MAY / Informational | Artifact path or ID | Requirement / HLA / DD / RTM / Test / Doc ID | Draft / Approved / Deprecated | |

Normative terms SHALL be defined before they are used to approve lifecycle artifacts.

Ambiguous normative terms SHALL block approval until resolved.

---

# 5. Abbreviations

| Anchor ID | Abbreviation | Expanded Form | Definition / Usage | First Introduced In | Related Artifact ID(s) | Status | Notes |
|-----------|--------------|---------------|--------------------|---------------------|-------------------------|--------|-------|
| abbr-example | Ex. | Example | Approved abbreviation usage. | Artifact path or ID | Requirement / HLA / DD / RTM / Test / Doc ID | Draft / Approved / Deprecated | |

Abbreviations SHALL be expanded or linked on first appearance in each document.

---

# 6. Acronyms

| Anchor ID | Acronym | Expanded Form | Definition / Usage | First Introduced In | Related Artifact ID(s) | Status | Notes |
|-----------|---------|---------------|--------------------|---------------------|-------------------------|--------|-------|
| acr-rtm | RTM | Requirements Traceability Matrix | Authoritative lifecycle mapping artifact. | `02-governance/09-traceability-guardrail.md` | RTM | Approved | |

Acronyms SHALL be expanded or linked on first appearance in each document.

---

# 7. Deprecated or Superseded Terms

| Previous Term | Replacement Term | Reason | Impacted Artifact(s) | Decision Ref | Effective Date | Status |
|---------------|------------------|--------|----------------------|--------------|----------------|--------|
| | | | | | | Deprecated / Superseded |

Deprecated terminology SHALL NOT remain in active artifacts unless retained as historical context.

If retained, the document SHALL identify the approved replacement term.

---

# 8. Change Control

For each glossary change, record:

- Date
- Term, abbreviation, or acronym affected
- Change type: Added / Revised / Deprecated / Superseded
- Reason for change
- Impacted artifacts
- Required downstream updates
- Human reviewer or approval authority

| Date | Entry | Change Type | Reason | Impacted Artifact(s) | Downstream Updates Required | Reviewed / Approved By |
|------|-------|-------------|--------|----------------------|-----------------------------|------------------------|
| | | Added / Revised / Deprecated / Superseded | | | | |

Glossary changes that alter artifact meaning SHALL trigger lifecycle impact analysis.

---

# 9. Review Checklist

Before glossary approval, confirm:

- All normative terms and phrases have definitions
- All abbreviations have expanded forms
- All acronyms have expanded forms
- Anchor IDs are stable and unique
- First-use links are present for acronyms and abbreviations in active documents
- Controlled terminology is used consistently across lifecycle artifacts
- Deprecated terms have approved replacements or historical justification
- Impacted artifacts have been updated
- Human approval granted

If any checklist item fails, glossary approval is incomplete.

---

# Approval

Approved By:
Approval accountability: Human/organizational authority only; AI tools must not be listed as approvers or approval authorities.
Role:
Date:
Version Incremented: Yes / No

Approval confirms that the glossary reflects the controlled terminology used by current lifecycle artifacts.

---

End of Project Glossary Template
