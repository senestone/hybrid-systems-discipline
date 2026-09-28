<!--
File: 02-governance/15-ai-assurance-profile.md

Purpose:
  Define optional additional assurance controls for governed increments
  containing material AI or probabilistic behavior.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# 15 - AI Assurance Profile

## 1. Applicability

Activate this profile when the Project Governance Profile identifies material AI or probabilistic behavior affecting decisions, users, rights, safety, security, privacy, operations, or business or mission outcomes.

The profile supplements the core lifecycle. It does not replace requirements, architecture, traceability, verification, validation, human authority, or operational governance.

Record activation, exclusions, tailoring, and accountable authority in the Project Governance Profile.

---

## 2. AI System and Boundary Inventory

For each material probabilistic component, record:

- Component and boundary identifier
- Intended purpose and prohibited use
- Model, provider, version, endpoint, prompt, tool, retrieval, and configuration baseline
- Inputs, outputs, data flows, trust boundaries, and downstream decisions
- Human review, override, escalation, and fallback
- Deterministic containment and state-protection controls
- Known limitations, assumptions, dependencies, and failure modes
- Ownership and operational monitoring responsibility

Opaque or unowned probabilistic behavior is prohibited.

---

## 3. Data and Evaluation Lineage

Document applicable training, tuning, retrieval, grounding, test, and evaluation data:

- Source, provenance, authorization, and collection period
- Version, checksum, split, sampling method, and transformations
- Population or use-context represented
- Known exclusions, imbalance, contamination, leakage, and quality limitations
- Sensitive, personal, confidential, licensed, or regulated data posture
- Retention, access, deletion, and reproducibility constraints

Evaluation data SHALL be sufficiently independent of development data for the claim being assessed. Known overlap or contamination SHALL be disclosed and reflected in confidence and risk disposition.

---

## 4. Evaluation Design

Define before evaluation:

- Claim or decision supported by each metric
- Target population, operational context, and sampling rationale
- Error and harm taxonomy
- False-positive and false-negative posture
- Acceptance, rejection, escalation, and abstention thresholds
- Baseline and comparison method
- Statistical confidence, uncertainty, and practical-significance treatment
- Slice, subgroup, boundary, stress, and long-tail coverage
- Repeatability, stochastic variation, seed, and run-count approach
- Human-evaluation rubric, reviewer qualification, and disagreement handling

Aggregate metrics SHALL NOT conceal high-consequence failures or materially underperforming slices.

Evaluation results SHALL state limitations and SHALL NOT generalize beyond represented data, users, environments, languages, or use contexts without evidence.

---

## 5. Harm, Fairness, Misuse, and Adversarial Evaluation

Where applicable, evaluate:

- Foreseeable misuse and abuse
- Prompt injection, data exfiltration, tool misuse, and privilege escalation
- Unsafe, illegal, deceptive, or policy-violating outputs
- Hallucination, unsupported inference, and overreliance
- Bias, fairness, accessibility, and disparate performance
- Privacy leakage, memorization, re-identification, and inference
- Security boundary bypass and denial of service
- Human automation bias, override failure, and escalation delay
- Cascading effects on deterministic state or downstream decisions

Applicability decisions and exclusions SHALL include rationale and accountable human approval.

---

## 6. Human Oversight and Contestability

Define:

- Decisions requiring human review before effect
- Reviewer information, competence, time, and authority needs
- Override, correction, appeal, and escalation paths
- User notice and explanation obligations
- Conditions requiring abstention, fallback, suspension, or shutdown
- Logging sufficient to reconstruct material decisions without exposing protected data improperly

Human oversight SHALL be operationally feasible and tested. A nominal human-in-the-loop control without time, information, authority, or a usable interface is not an effective control.

---

## 7. Change and Supplier Control

Treat material changes to a model, provider, endpoint, prompt, system instruction, tool, retrieval corpus, embedding, threshold, safety control, data pipeline, or evaluation method as governed changes.

For externally managed or silently updated services, define:

- Version-detection and change-notification capability
- Contractual and technical controls
- Regression and revalidation triggers
- Fallback, rollback, substitution, and exit strategy
- Evidence available when internals are inaccessible

Provider claims SHALL be distinguished from project verification evidence.

---

## 8. Operational Monitoring and Response

Define thresholds and response actions for applicable:

- Quality and task-performance drift
- Safety, harm, fairness, privacy, and security signals
- Input and output distribution change
- Retrieval, data, prompt, configuration, model, and provider drift
- Override, rejection, fallback, complaint, and escalation rates
- Cost, latency, availability, and dependency failures

Monitoring SHALL identify the accountable responder, review cadence, evidence retained, and conditions for investigation, revalidation, rollback, suspension, or retirement.

---

## 9. Assurance Evidence and Release

The Test Plan, RTM, Verification and Validation Report, Project Risk Register, and Operational Runbook SHALL together identify:

- AI-specific Requirement, Boundary, Verification Case, Test Case, Validation Scenario, Risk, Change, and evidence IDs
- Model, prompt, data, provider, threshold, tool, and configuration baselines
- Evaluation limitations and residual risks
- Human approvals and operational owners
- Monitoring and retirement triggers

Activation of this profile does not establish safety, compliance, certification, or fitness for use. Those conclusions require evidence and the applicable accountable authority.

---

## 10. Informative Standards Alignment

This profile is informed by the voluntary [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST AI 600-1, Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).

Projects using a standards crosswalk SHALL record the referenced edition and access date. NIST guidance may evolve; verify the current official publication before claiming alignment.

A crosswalk is not evidence of implementation, conformity, certification, legal sufficiency, or regulatory compliance.

---

End of Profile
