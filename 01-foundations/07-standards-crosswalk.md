<!--
File: 01-foundations/07-standards-crosswalk.md

Purpose:
  Provide a high-level, non-certifying map between toolkit controls and
  selected systems, software, and AI governance references.
-->

# Standards Alignment Crosswalk

Reference Status Checked: 2026-09-28
Crosswalk Version: 1.0.0

## 1. Scope and Interpretation

This crosswalk supports orientation, adoption planning, and gap analysis. It does not reproduce standards text, provide clause-level conformity evidence, establish legal or regulatory sufficiency, or certify an organization, process, product, or management system.

The source standards remain authoritative. Several are copyrighted and may require licensed access. A toolkit artifact demonstrates conformity only when an accountable organization has implemented the applicable control, produced adequate evidence, and completed any required independent assessment.

Alignment labels mean:

- `Strong`: the toolkit provides direct, substantive controls or artifacts for the topic.
- `Partial`: the toolkit addresses part of the topic but requires organizational process or additional evidence.
- `Context`: the reference informs interpretation, but the topic is not a primary toolkit control.
- `Out of Scope`: the toolkit intentionally does not provide the organizational or specialist system required.

## 2. Reference Baseline

| Reference | Edition / Status Used | Relevant Scope | Official Source |
|-----------|-----------------------|----------------|-----------------|
| ISO/IEC/IEEE 29148 | 2018, published; replacement draft in development when checked | Requirements engineering processes and information items | [ISO catalogue](https://www.iso.org/standard/72089.html) |
| ISO/IEC/IEEE 15288 | 2023 | System life-cycle processes | [ISO catalogue](https://www.iso.org/standard/81702.html) |
| ISO/IEC/IEEE 12207 | 2026 | Software life-cycle processes | [ISO catalogue](https://www.iso.org/standard/90219.html) |
| NIST AI Risk Management Framework | AI RMF 1.0; revision activity underway when checked | Voluntary AI risk management functions and characteristics | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| NIST AI 600-1 | 2024, Generative AI Profile | Generative-AI risks and risk-management actions | [NIST publication](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) |
| ISO/IEC 42001 | 2023 | AI management systems | [ISO overview](https://www.iso.org/standard/42001) |

Edition status can change. Adoption and audit work SHALL verify the current official edition, amendments, corrigenda, transition rules, and applicable contractual or regulatory obligations.

## 3. High-Level Alignment

| Toolkit Area | 29148 | 15288 | 12207 | NIST AI RMF | NIST AI 600-1 | ISO/IEC 42001 | Alignment Note |
|--------------|-------|-------|-------|-------------|---------------|----------------|----------------|
| Governed increment and lifecycle gates | Context | Strong | Strong | Partial | Context | Partial | Establishes bounded work, sequencing, reviews, and human authorization; it does not implement every organizational life-cycle process. |
| Requirements and controlled terminology | Strong | Strong | Strong | Partial | Partial | Partial | Provides structured requirements, glossary, quality criteria, baselines, and change control. |
| Architecture and detailed design | Context | Strong | Strong | Partial | Partial | Context | Separates architecture from design and controls deterministic-probabilistic boundaries. |
| Bidirectional traceability | Strong | Strong | Strong | Partial | Partial | Partial | Connects needs, requirements, architecture, design, verification, validation, evidence, changes, risks, and release. |
| Verification and intended-use validation | Strong | Strong | Strong | Strong | Strong | Partial | Separates verification methods from stakeholder and operational validation scenarios and evidence. |
| Risk, uncertainty, and change control | Partial | Strong | Strong | Strong | Strong | Strong | Uses governed risk, uncertainty, decision, and impact-assessment records; organization-wide risk systems remain external. |
| Human authority, oversight, and accountability | Context | Strong | Strong | Strong | Strong | Strong | Assigns explicit human decision rights and prevents automation from conferring approval or risk-acceptance authority. |
| AI data, evaluation, harm, and drift assurance | Context | Partial | Partial | Strong | Strong | Strong | The optional AI Assurance Profile covers lineage, evaluations, affected parties, oversight, suppliers, incidents, and drift. |
| Packaging, deployment, and reproducibility | Context | Partial | Strong | Partial | Partial | Context | Requires reproducible packaging, environment evidence, rollback planning, and release controls. |
| Operation, maintenance, incident response, and retirement | Context | Strong | Strong | Strong | Strong | Partial | Extends governed evidence through monitoring, incidents, maintenance, deprecation, data disposition, and retirement. |
| Tailoring and assurance proportionality | Context | Strong | Strong | Strong | Strong | Strong | Baseline, Elevated, and High Assurance profiles bind tailoring to risk, evidence, and accountable approval. |
| Process measurement and improvement | Context | Partial | Partial | Partial | Partial | Partial | Pilot and assessment artifacts support bounded evidence and learning but do not constitute an organizational measurement program. |

## 4. Material Gaps and Intentional Boundaries

The toolkit does not by itself provide:

- A complete organizational quality management system or AI management system
- Certification readiness, accredited audit criteria, or clause-by-clause evidence
- Full acquisition, supply, portfolio, infrastructure, human-resources, or organizational training processes
- Sector-specific safety cases, cybersecurity frameworks, privacy programs, accessibility conformance, or regulated-product submissions
- Legal interpretation or jurisdiction-specific compliance determinations
- Quantitative assurance thresholds suitable for every domain or risk class
- Independent review, segregation of duties, or organizational authority merely by naming those controls in a template
- Evidence that instantiated artifacts are accurate, complete, approved, or operationally effective

Projects SHALL add domain-specific standards, laws, contracts, assurance cases, specialist reviews, and evidence where applicable. Conflicts between this toolkit and binding obligations require documented resolution by accountable human authority.

## 5. Adoption and Conformity Use

For a standards-driven adoption:

1. Identify applicable standards, clauses, laws, contracts, and organizational policies.
2. Establish a licensed, authoritative reference baseline.
3. Create a project- or organization-specific clause-to-control crosswalk.
4. Assign accountable owners and required independence.
5. Define objective evidence and acceptance criteria for each obligation.
6. Record gaps, risks, tailoring, and remediation decisions.
7. Obtain qualified legal, compliance, safety, security, privacy, or certification review where required.

The toolkit may supply supporting controls and evidence. It SHALL NOT be cited as sole proof of conformity.

## 6. Maintenance

Review this crosswalk when:

- A referenced standard is revised, replaced, amended, corrected, or withdrawn
- A material toolkit lifecycle, schema, or assurance control changes
- A new regulatory or contractual context is adopted
- Assessment experience reveals an overstated alignment or an unaddressed gap

Record reference updates in the changelog and evaluate compatibility under the Toolkit Release and Compatibility Policy.

---

End of Crosswalk
