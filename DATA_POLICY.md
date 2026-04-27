# Data Policy

## Purpose

This pack preserves the cuneiform control lane without outrunning the current
rights and provenance posture.

## Asset Policy

| Asset Family | Current Policy | Why |
|---|---|---|
| Staged docs, PRD, and handover surfaces | `PUBLISH_NOW` inside the migration package | They are authored for this pack and contain no restricted heavy assets |
| Benchmark and diagnostic summaries | `PUBLISH_NOW` as derived text or small metadata | They preserve control-lane truth without shipping large restricted assets |
| Benchmark manifests and derived JSON outputs | `PUBLISH_WITH_REVIEW` | Small derived artifacts are useful, but each file still needs provenance review before remote promotion |
| Image previews and raw image-bearing corpora | `FETCH_EXTERNALLY_OR_INTERNAL_ONLY` | Rights posture is unresolved for some sources |
| Model weights and intermediate experimental checkpoints | `INTERNAL_ONLY` | They are not needed for the current control-pack truth surface |
| Heavy corpora or full rerun substrates | `FETCH_EXTERNALLY` | The migration pack must avoid uncontrolled blob vendoring |

## Public Boundary

- A future public repo may expose derived summaries and manifests.
- It must not ship unrestricted image-bearing assets until the rights posture is
  cleared.
- If a future rerun needs external data, the fetch and checksum flow must be
  documented before promotion.

## Current Blocking Inputs

- explicit redistribution ruling for image-bearing assets
- explicit redistribution ruling for image-bearing assets
- admission decision on which benchmark manifests are safe for remote custody

