<!--
File: 04-templates/project/work-effort-log-template.md

Purpose:
  Record measured active effort against engineering artifacts without
  confusing elapsed tool time with actual work.

Lifecycle authority resides in:
  02-governance/00-lifecycle-bootstrap.md
-->

# Work Effort Log

Project:
Time zone:
Tracking start date:
Maintainer:
Attribution: Human/organizational accountability only; AI tools must not be listed as authors, maintainers, owners, preparers, creators, contributors, or attribution recipients.

## Measurement Rules

- Record a session when work starts and close it when work stops. Record actual start and end times in the stated time zone.
- `Active minutes` means time spent doing the named work. Exclude breaks, waiting for builds or responses, and unattended runs. If active time is not known, write `Unknown`; do not derive it from timestamps alone.
- Split sessions when the activity class or primary artifact changes materially. A short review or correction can remain in the same session as the work it validates.
- Record human review or decision time separately from implementation time if it is measured. Do not infer one person's time from another person's activity or from automated tool duration.
- Identify the accountable person or team for each measured session; automation is evidence or tooling context, not a labor contributor.
- Link to the artifact or commit produced. Record failed or discarded work when it consumed measured effort.
- Do not backfill historical estimates as measurements. Mark historical work `Unmeasured` unless a reliable time record exists.

## Activity Classes

| Class | Use for |
|---|---|
| Artifact | Requirements, architecture, design, RTM, decision records, and other engineering documents |
| Code | Product implementation and experimental prototypes |
| Test | Test cases, test code, execution analysis, and defect reproduction |
| Test data | Fixtures, sample packages, migration data, and expected results |
| Build and tooling | Makefiles, CI, dependency setup, scripts, packaging, and orchestration |
| Review and decision | Human review, approval, and technical trade studies |

## Sessions

| Date | Person or team | Start | End | Active minutes | Class | Artifact or scope | Result and evidence | Notes |
|---|---|---|---|---:|---|---|---|---|
| YYYY-MM-DD | Accountable human or team | HH:MM or Unknown | HH:MM or Unknown | Number, Unknown, or Unmeasured | Class | Path / ID | Link to artifact, test, or commit | Excluded wait time or limitation |

## Rollup

For a chosen reporting period, sum only numeric `Active minutes` by class and by artifact. Report the number of `Unknown` or `Unmeasured` sessions beside every total. Keep machine build/test wall time as a separate performance metric, not as labor effort.
