<!--
File: 04-templates/project/work-effort-log-template.md

Purpose:
  Record measured human effort against governed engineering work without
  confusing active labor, elapsed session time, or automated runtime.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Work Effort Log

Project:
Time zone:
Tracking start date:
Tracking purpose:
Default timestamp precision: Minute / Second / Other
Rounding rule:
Maintainer:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, collaborators, maintainers, owners, preparers, creators, contributors, or attribution recipients.
Glossary Version Reference:

## Purpose and Use

Use this log to support:

- Effort reconstruction and auditability
- Planning and estimation calibration
- Cost or funding analysis
- Identification of workflow bottlenecks
- Comparison of planned and observed effort by activity or lifecycle phase
- Recognition of review, governance, testing, and documentation work that commits alone do not show

This log SHALL NOT be used as a standalone measure of individual productivity, quality, value, or performance. Minutes, session counts, artifact counts, and commit counts are context-dependent and SHALL NOT be compared without considering work type, complexity, uncertainty, review obligations, and outcome quality.

## Measurement Rules

- Record a session when work starts and close it when work stops. Record actual start and end times in the stated time zone and declared precision.
- `Active minutes` means time spent doing the named work. Exclude breaks, waiting for builds or responses, and unattended runs. If work occurred but no reliable active duration exists, write `Unmeasured`; do not derive it from timestamps alone.
- Split sessions when the activity class or primary artifact changes materially. A short review or correction can remain in the same session as the work it validates.
- Record human review or decision time separately from implementation time if it is measured. Do not infer one person's time from another person's activity or from automated tool duration.
- Identify the accountable person or team for each measured session; automation is evidence or tooling context, not a labor contributor.
- Link to the artifact or commit produced. Record failed or discarded work when it consumed measured effort.
- Do not backfill historical estimates as measurements. Mark historical work `Unmeasured` unless a reliable time record exists.
- Use the declared rounding rule consistently. For example, a project MAY round any non-zero session shorter than one minute to one active minute, but it SHALL state that convention rather than imply false precision.
- When timestamp duration and active minutes differ, explain excluded wait time, interruptions, parallel work, or another material cause in `Notes`.
- Do not sum simultaneous sessions for the same person as independent labor unless the entries represent distinct measured participants.
- Preserve corrections transparently. Do not silently replace a material time, classification, accountable party, or evidence reference without recording the correction in Change History.

Use `Unknown` for a timestamp or descriptive value that cannot be determined. Use `Unmeasured` only for active human effort known to have occurred without a reliable duration. Neither value means zero.

## Measurement Methods

| Method | Use for |
|---|---|
| Timer | Contemporaneous timer or time-tracking record |
| Manual | Start, end, and active effort recorded contemporaneously by the accountable person or team |
| External record | Reliable calendar, ticket, timesheet, or equivalent source identified in Notes |
| Unmeasured | Work occurred, but no reliable duration exists |

Do not label reconstructed estimates as measured effort. If estimates are needed for planning, keep them in a separate estimate artifact or clearly separated forecast section.

## Activity Classes

| Class | Use for |
|---|---|
| Artifact | Requirements, architecture, design, RTM, decision records, and other engineering documents |
| Governance | Recording phase gates, baselines, change control, risk status, and other lifecycle administration |
| Code | Product implementation and experimental prototypes |
| Test | Test cases, test code, execution analysis, and defect reproduction |
| Test data | Fixtures, sample packages, migration data, and expected results |
| Build and tooling | Makefiles, CI, dependency setup, scripts, packaging, and orchestration |
| Review and decision | Human evaluation, approval decisions, and technical trade studies |
| Operations and support | Deployment, monitoring, incident response, maintenance, and user or operator support |
| Project administration | Scheduling, reporting, coordination, and other non-engineering project administration |

Projects MAY define additional classes. Add them to this table before use and preserve class meaning across reporting periods.

## Sessions

| Date | Person or team | Lifecycle phase | Start | End | Active minutes | Method | Class | Artifact or scope | Related IDs | Result and evidence | Notes |
|---|---|---|---|---|---:|---|---|---|---|---|---|
| YYYY-MM-DD | Accountable human or team | Phase or Cross-Lifecycle | HH:MM or Unknown | HH:MM or Unknown | Number or Unmeasured | Method | Class | Path / artifact ID | Requirement, Decision, CHG, RSK, Test, or VAL IDs | Link to artifact, test, commit, or review record | Excluded wait time, limitation, or correction reference |

`Related IDs` SHOULD contain stable governed identifiers when they exist. Do not invent identifiers solely to populate the log.

## Optional Machine Execution Metrics

Record unattended or automated runtime separately from human effort when it provides engineering value.

| Date | Run ID | Run Type | Start | End | Wall Time | Environment | Artifact or Scope | Result and Evidence | Related Human Session |
|---|---|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | RUN-XXX | Build / Test / Analysis / Deployment / Other | Timestamp | Timestamp | Duration | Environment ID or description | Path / ID | Link to logs or result | Session date and reference |

Machine wall time SHALL NOT be added to human active minutes. Human time spent configuring, monitoring, analyzing, or responding to the run MAY be recorded as a separate measured session.

## Rollup

Reporting period start:
Reporting period end:
Prepared by:
Calculation method or tooling context:

Sum only numeric `Active minutes`. Never convert `Unknown` or `Unmeasured` entries to zero. Report their counts beside every applicable total.

### By Activity Class

| Class | Measured Sessions | Active Minutes | Unknown Sessions | Unmeasured Sessions | Notes |
|---|---:|---:|---:|---:|---|

### By Lifecycle Phase

| Lifecycle Phase | Measured Sessions | Active Minutes | Unknown Sessions | Unmeasured Sessions | Notes |
|---|---:|---:|---:|---:|---|

### By Artifact or Scope

| Artifact or Scope | Measured Sessions | Active Minutes | Unknown Sessions | Unmeasured Sessions | Notes |
|---|---:|---:|---:|---:|---|

### Measurement Coverage

Total sessions:
Sessions with numeric active minutes:
Unknown sessions:
Unmeasured sessions:
Earliest measured session:
Latest measured session:

Coverage counts describe record completeness, not the duration of unmeasured work. Do not estimate a percentage of total effort when unmeasured duration is unknown.

### Interpretation

Document:

- Material concentration of effort
- Rework or repeated-review signals
- Measurement limitations
- Changes in tracking practice during the period
- Planning assumptions informed by the observations
- Conclusions that the data does not support

## Change History

| Date | Entry or Period Affected | Correction or Method Change | Reason | Changed By |
|---|---|---|---|---|

Routine additions of new sessions do not require Change History entries. Material corrections to prior records or measurement rules do.

---

End of Work Effort Log Template
