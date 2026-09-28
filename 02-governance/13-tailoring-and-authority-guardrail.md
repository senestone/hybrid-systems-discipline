<!--
File: 02-governance/13-tailoring-and-authority-guardrail.md

Purpose:
  Define proportional governance profiles, explicit tailoring controls,
  and human decision-right assignments for each governed increment.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# 13 - Tailoring and Authority Guardrail

## 1. Purpose

The toolkit SHALL be applied proportionately to the consequences and uncertainty of the governed increment.

Tailoring adjusts artifact depth, review independence, verification rigor, and evidence retention. It does not silently remove lifecycle phases, traceability, change control, risk review, or human authorization.

Each governed increment SHALL have an approved Project Governance Profile before advancement from Ideation.

---

## 2. Assessment Factors

Assess each factor as Low, Moderate, High, or Not Applicable and record the rationale:

- Safety impact
- Security impact
- Privacy impact
- Regulatory or contractual exposure
- External-user exposure
- Operational criticality
- Data sensitivity
- Probabilistic-system impact and autonomy
- Architectural and integration complexity
- Reversibility and recovery cost
- Novelty and strength of available evidence

An `Unknown` rating SHALL be treated as an uncertainty requiring an owner, resolution plan, and conservative interim posture.

---

## 3. Governance Profiles

### Baseline

Use when consequences are limited, the increment is readily reversible, interfaces are bounded, and no assessment factor creates material safety, security, privacy, regulatory, or operational exposure.

- Mandatory lifecycle phases and human gates remain in force.
- One person MAY hold multiple authority roles when assignments are explicit.
- Required artifacts MAY be concise or combined when identifiers, approvals, and traceability remain unambiguous.
- Review MAY be performed by the accountable role when independence is not required by policy, contract, or risk posture.
- Evidence SHALL be retained through the defined operational support period or superseding baseline.

### Elevated

Use when one or more factors have material external-user, operational, data, security, privacy, probabilistic, integration, or recovery consequences.

- Required artifacts SHALL be complete enough for independent reconstruction.
- Independent review SHOULD be used for architecture, security or privacy, verification, and release decisions relevant to the elevated factors.
- Negative, recovery, misuse, and operational scenarios SHALL receive explicit coverage where applicable.
- Evidence-retention periods and protected evidence locations SHALL be defined before implementation.
- Exceptions require documented impact assessment and approval by the affected authority role.

### High Assurance

Use when failure could cause severe safety, security, privacy, legal, regulatory, mission, financial, or irreversible operational harm.

- Independent review and segregation of duties SHALL be defined for affected decisions unless an approved exception explains why separation is infeasible and how equivalent oversight is achieved.
- Verification depth, sampling rationale, environment fidelity, and evidence provenance SHALL be explicit.
- High-consequence assumptions and uncertainties SHALL be resolved or formally dispositioned before affected work advances.
- Release requires explicit concurrence from every applicable specialized authority identified in the Project Governance Profile.
- Evidence retention SHALL satisfy the longest applicable legal, regulatory, contractual, operational, or organizational obligation.

The highest material factor governs unless accountable human authority approves and records a different profile with rationale and risk disposition.

---

## 4. Required Authority Assignments

The Project Governance Profile SHALL assign accountable humans, teams, roles, or organizations for:

- Project or increment ownership
- Requirements authority
- Architecture authority
- Risk ownership and residual-risk acceptance
- Security and privacy authority, when applicable
- Verification and validation authority
- Release authority
- Operational ownership

One person MAY hold multiple roles for Baseline or Elevated work unless independence is required. Role combination SHALL be explicit; it SHALL NOT be inferred from participation.

AI systems and automation SHALL NOT hold an authority role, approve a gate, accept residual risk, or authorize release.

---

## 5. Tailoring Decisions and Exceptions

Every tailored obligation or exception SHALL record:

- The affected control, artifact, review, or evidence obligation
- The default requirement
- The proposed adjustment
- The governed increment and lifecycle phases affected
- Rationale and supporting evidence
- New or changed risk
- Compensating controls
- Approval authority and date
- Expiration, review point, or superseding condition

A material tailoring decision requires a Change Proposal and Impact Assessment when it changes an approved Project Governance Profile or downstream obligation.

Tailoring SHALL NOT:

- Remove explicit human gate authorization
- Eliminate bidirectional traceability for approved scope
- Treat absent evidence as successful verification or validation
- Convert an unresolved material uncertainty into an implicit assumption
- Permit an AI system or automation to exercise human authority
- Override legal, regulatory, contractual, security, privacy, or safety obligations

---

## 6. Controlled Uncertainty

Not every uncertainty must be eliminated before advancement. Every unresolved material uncertainty SHALL be:

- Recorded with a stable Risk, Assumption, Issue, or Dependency ID
- Bounded by its possible effect on scope, requirements, architecture, design, verification, release, or operations
- Assigned to an accountable human role
- Given a resolution, monitoring, or disposition plan
- Linked to affected artifacts and gates
- Subject to an explicit deadline, trigger, or revisit point

Advancement is prohibited when unresolved uncertainty could invalidate downstream work or when its exposure exceeds the authority of the approving role.

---

## 7. Review and Change

Review the Project Governance Profile:

- At every phase gate
- When a material assessment factor changes
- When governed scope expands or a new increment begins
- When an authority assignment changes
- When an exception expires or a compensating control fails
- Before release and transfer to operations

Profile changes SHALL preserve prior decisions and link superseding versions.

---

End of Guardrail
