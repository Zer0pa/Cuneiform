# FAQ

## What is this repo?

This is a staged control-module pack for the cuneiform lane. It preserves the
benchmark truth, source boundary, and rerun contract for a lane whose inherited
governing gate failed.

## How does this relate to the wider Zer0pa portfolio?

It is support infrastructure for the portfolio's methods and evidence layers.
It is not the flagship story, not the current product wedge, and not a generic
platform component.

## What is actually verified here?

The staged evidence summary verifies that the control lane exists and that the
P5 governing gate failed at `governing_1nn_accuracy = 0.021916`. The installable
smoke package verifies manifest custody and shape only. See
`docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`,
`docs/evidence/CUNEIFORM_CONTROL_RESULTS.md`, and
`artefacts/smoke/manifest_validation_report.json`.

## What is still unknown or deferred?

A full scientific rerun surface and any future gate repair remain deferred.
Data-rights clearance for image-bearing assets is also deferred. The current
package is intentionally limited to manifest validation.

## Why does public documentation mention audit limits?

Because this scaffold is easy to overread. Audit limits prevent the pack from
being mistaken for proof of a repaired scientific result or a public-ready
standalone repo.

## Where should I start if I want to inspect the technical structure?

Read `docs/ARCHITECTURE.md`, then `code/README.md`, then the named authority
artifacts.

## Where do I report defects, disputes, or questions?

Use the issue templates for bugs, evidence disputes, feature requests, and
questions. Use `SECURITY.md` for private vulnerability reporting.
