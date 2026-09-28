<!--
File: 04-templates/project/process-assessment-report-template.md

Purpose:
  Record evidence, limitations, findings, and recommendations from a
  pilot or process assessment without overstating causal conclusions.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Process Assessment Report

Project or Pilot Name:
Governed Increment ID(s):
Assessment ID:
Assessment Period:
Toolkit Version or Commit Reference:
Template Schema ID: HSD-PROJ-PROCESS-ASSESSMENT
Template Schema Version: 1.0.0
Report Version:
Status: Draft / Under Review / Approved for Accuracy / Superseded
Prepared By:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Related Governance Profile Version:
Related Decision, Change, and Risk ID(s):

---

# 1. Assessment Purpose and Boundaries

State:

- Decision or learning objective supported by this assessment
- Included teams, workflows, lifecycle phases, and governed increments
- Excluded work and populations
- Observation period and comparison period
- Intended readers and permitted uses
- Confidentiality, privacy, and access constraints

This report SHALL distinguish process evidence from product verification and validation evidence. It does not replace phase-gate review, release approval, risk acceptance, or evidence recorded in the Verification and Validation Report.

---

# 2. Questions and Hypotheses

| Question or Hypothesis ID | Question or Qualified Hypothesis | Measure or Evidence | Decision Relevance | Predefined Success or Concern Threshold |
|---------------------------|----------------------------------|---------------------|--------------------|-----------------------------------------|
| PAQ-001 | | | | |

Phrase causal propositions as hypotheses unless the assessment design supports causal inference. Record exploratory questions separately from criteria defined before observation.

---

# 3. Assessment Design

## 3.1 Baseline and Comparison

Describe:

- Baseline source and time period
- Comparison group or within-team comparison, if any
- Unit of analysis
- Sampling and inclusion rules
- Sample size and missing observations
- Known differences between baseline and assessed conditions

Use `No credible baseline` when a defensible baseline is unavailable. Do not substitute recollection or inferred values without labeling their evidentiary limits.

## 3.2 Data Provenance and Quality

| Data Source ID | Source and Owner | Collection Method | Coverage | Known Quality Limitation | Access / Retention Control |
|----------------|------------------|-------------------|----------|--------------------------|----------------------------|
| PAD-001 | | | | | |

Record transformations, exclusions, corrections, and aggregation rules sufficiently to reproduce reported results.

## 3.3 Confounders and Sources of Bias

| Factor ID | Confounder, Bias, or Alternative Explanation | Likely Effect | Mitigation or Sensitivity Check | Residual Limitation |
|-----------|----------------------------------------------|---------------|---------------------------------|---------------------|
| PAF-001 | | | | |

Consider team experience, novelty, scope complexity, staffing changes, tooling changes, selection effects, learning effects, and changes in review rigor.

---

# 4. Measurement Plan and Results

## 4.1 Metric Register

| Metric ID | Metric and Operational Definition | Source | Baseline | Observed Result | Sample / Coverage | Interpretation | Confidence / Limitation |
|-----------|-----------------------------------|--------|----------|-----------------|-------------------|----------------|-------------------------|
| PAM-001 | | | | | | | |

Consider metrics relevant to the stated questions, including:

- Artifact production, review, correction, and approval effort
- Requirements and traceability defects
- Phase-gate reversals or rejected submissions
- Architecture and design rework
- Planned-to-observed implementation variance
- Human correction of agent-produced material by error category
- Unsupported inference or fabricated-evidence incidents
- Escaped defects and verification failures
- Packaging, deployment, and orchestration failures
- Documentation drift and stale operational guidance
- Onboarding time and support burden
- Reuse of approved artifacts, patterns, or evidence

Counts and percentages SHALL identify their denominator. Efficiency metrics SHALL be interpreted alongside quality and governance outcomes.

## 4.2 Human Effort

Report human effort only from an active Work Effort Log or another approved measurement protocol.

| Lifecycle Phase or Activity | Measured Human Effort | Measurement Coverage | Unmeasured Records or Work | Source Reference | Interpretation Limitation |
|-----------------------------|-----------------------|----------------------|----------------------------|------------------|---------------------------|
| | | | | | |

Use `Unmeasured` when reliable human effort is unavailable. Do not infer human effort from conversation timestamps, commits, artifact changes, calendar duration, or agent runtime.

## 4.3 Automated Runtime and Consumption

| Tool or Automated Activity | Runtime / Consumption Measure | Measurement Window | Source Reference | Relationship to Human Work | Limitation |
|----------------------------|-------------------------------|--------------------|------------------|----------------------------|------------|
| | | | | | |

Automated runtime and consumption SHALL remain separate from human effort. Neither is a proxy for the other.

---

# 5. Qualitative Evidence

| Evidence ID | Participant or Source Category | Collection Method | Finding | Corroborating or Contradicting Evidence | Limitation |
|-------------|--------------------------------|-------------------|---------|-----------------------------------------|------------|
| PAQ-E001 | | | | | |

Protect confidential or personal information. Report themes with sufficient context to be useful without implying representativeness beyond the observed sample.

---

# 6. Governance Conformance

| Obligation or Control | Expected Evidence | Observed Status | Evidence Reference | Deviation / Risk / Change ID | Disposition |
|-----------------------|-------------------|-----------------|--------------------|------------------------------|-------------|
| Lifecycle sequencing and gate authorization | | Conforming / Partial / Nonconforming / Not Assessed | | | |
| Requirements and traceability discipline | | Conforming / Partial / Nonconforming / Not Assessed | | | |
| Human authority and approval boundaries | | Conforming / Partial / Nonconforming / Not Assessed | | | |
| Change and risk control | | Conforming / Partial / Nonconforming / Not Assessed | | | |
| Verification and validation evidence | | Conforming / Partial / Nonconforming / Not Assessed | | | |
| Operational and documentation continuity | | Conforming / Partial / Nonconforming / Not Assessed | | | |

Do not treat artifact existence as proof of substantive conformance. Sample content, links, approvals, and evidence where necessary.

---

# 7. Findings and Lessons

| Finding ID | Finding | Evidence Strength | Affected Workflow or Control | Consequence | Related Metric / Evidence / Risk IDs |
|------------|---------|-------------------|------------------------------|-------------|--------------------------------------|
| PAFN-001 | | Strong / Moderate / Limited / Inconclusive | | | |

Record contradictory and null findings. Distinguish observed facts, interpretation, hypotheses, preferences, and unresolved uncertainty.

---

# 8. Recommendations

| Recommendation ID | Recommendation | Finding Basis | Expected Benefit | Cost / Tradeoff / Risk | Proposed Owner | Required Change or Decision ID | Priority |
|-------------------|----------------|---------------|------------------|------------------------|----------------|--------------------------------|----------|
| PAR-001 | | | | | | | |

Recommendations MAY propose continuation, modification, additional measurement, restricted expansion, or termination. They SHALL NOT themselves authorize a governance change, toolkit modification, broader rollout, or risk acceptance.

---

# 9. Limitations and Causal Restraint

State explicitly:

- Missing or low-quality data
- Sample-size and representativeness limits
- Uncontrolled confounders
- Changes in scope or measurement during the assessment
- Results that cannot be reproduced or independently checked
- Claims the evidence does not support
- Conditions under which conclusions may not generalize

Avoid causal language unless the design, data, and analysis support it. Prefer precise formulations such as `was associated with`, `was observed during`, or `participants reported` when causality is not established.

---

# 10. Conclusion and Decision Inputs

Summarize:

- Questions answered, partly answered, and unresolved
- Evidence-supported benefits and costs
- Material risks and uncertainties
- Readiness for another bounded pilot or broader consideration
- Additional evidence required before a scale decision

Scaling remains a separate human decision subject to governance, risk, change, and authority controls.

---

# 11. Review and Approval for Accuracy

- Data provenance and transformations reviewed? (Yes / No)
- Material limitations and contradictory evidence disclosed? (Yes / No)
- Human effort reported only from approved measurements? (Yes / No / Not Applicable)
- Automated runtime reported separately? (Yes / No / Not Applicable)
- Governance deviations linked to governed records? (Yes / No / Not Applicable)
- Conclusions match the stated evidence strength? (Yes / No)

Reviewed By:
Role:
Review Date:
Approval Decision ID:
Accuracy Disposition: Approved for Accuracy / Revisions Required / Rejected

Approval here confirms report accuracy and evidentiary discipline only. It is not approval to scale, release, change governance, accept risk, or advance a lifecycle phase.

---

End of Template
