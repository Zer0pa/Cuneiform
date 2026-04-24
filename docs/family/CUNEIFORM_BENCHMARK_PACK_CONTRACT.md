# Cuneiform Benchmark Pack Contract

## Purpose

Define the bounded contract for the cuneiform control pack so future extraction
work does not upgrade the lane beyond what the evidence supports.

## Inputs

- cuneiform benchmark and probe scripts under `scripts/cuneiform/`
- benchmark and diagnostic artifacts under `workspace/artifacts/cuneiform/`
- the `science_engineering_review_2026-04-10/` review pack

## Outputs

- a truthful control-pack front door
- source and data boundary docs
- a rerun guide for future extraction work
- staged evidence summaries that keep the failed governing gate visible

## Required Invariants

- The lane remains benchmark/control only.
- `NO_GO_GOVERNING_GATE_UNMET` remains visible if the underlying evidence has
  not changed.
- P6 and P7 diagnostics may be documented, but never promoted as substitute
  closure.
- Heavy or rights-limited assets stay out of the staged scaffold unless the
  data policy is explicitly amended.

## Explicit Non-Goals

- No flagship scientific narrative
- No generic methods ownership claim
- No public-release or commercialization claim

## Downstream Consumers

- internal extraction work for a minimal rerun scaffold
- portfolio-level auditors who need a known-script control lane
- future benchmark methods work that needs a stable control reference

