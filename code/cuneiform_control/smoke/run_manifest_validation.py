#!/usr/bin/env python3
"""SMOKE-01-MANIFEST-VALIDATION runner.

Validates the inherited cuneiform annotated-sign benchmark manifest:
  1. SHA-256 matches a pinned value.
  2. JSON parses.
  3. Top-level shape conforms to a conservative pinned schema.
  4. Cross-field invariants hold (summary counts vs array lengths).

This runner intentionally does NOT compute any scientific metric. It does NOT
rerun the failed governing 1NN probe. A PASS here means the inherited
artefact's custody and shape are intact; it does NOT mean
NO_GO_GOVERNING_GATE_UNMET has been repaired.

No third-party dependencies — uses only the Python standard library so the
smoke can run on any Python 3.8+ host without provisioning.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


GOVERNING_VERDICT = "NO_GO_GOVERNING_GATE_UNMET"
GOVERNING_1NN_ACCURACY = 0.021916
SMOKE_TARGET_ID = "SMOKE-01-MANIFEST-VALIDATION"


def sha256_of_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def sha256_of_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# Lightweight schema validation (subset of JSON Schema 2020-12 sufficient for
# the cuneiform manifest schema shipped at
# code/cuneiform_control/schemas/benchmark_manifest.schema.json). A PR that
# wants full validation can swap in `jsonschema`; we keep stdlib-only on
# purpose so the smoke runs without any provisioning step.
# ---------------------------------------------------------------------------

def _type_match(value: Any, expected: Any) -> bool:
    py = {
        "object": dict,
        "array": list,
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "null": type(None),
    }
    if isinstance(expected, list):
        return any(_type_match(value, e) for e in expected)
    if expected == "integer" and isinstance(value, bool):
        return False
    if expected == "number" and isinstance(value, bool):
        return False
    return isinstance(value, py[expected])


def _validate(node: Any, schema: Dict[str, Any], path: str, errors: List[str]) -> None:
    if "const" in schema and node != schema["const"]:
        errors.append(f"{path}: const mismatch (expected {schema['const']!r}, got {node!r})")
        return

    if "type" in schema:
        if not _type_match(node, schema["type"]):
            errors.append(f"{path}: type mismatch (expected {schema['type']}, got {type(node).__name__})")
            return

    if "pattern" in schema and isinstance(node, str):
        import re
        if not re.search(schema["pattern"], node):
            errors.append(f"{path}: pattern mismatch ({schema['pattern']!r})")

    if isinstance(node, dict):
        for req in schema.get("required", []):
            if req not in node:
                errors.append(f"{path}: missing required key '{req}'")
        props = schema.get("properties", {})
        for k, sub_schema in props.items():
            if k in node:
                _validate(node[k], sub_schema, f"{path}.{k}", errors)
        # additionalProperties: True (default in our schema) — no constraint

    elif isinstance(node, list):
        items_schema = schema.get("items")
        if items_schema is not None:
            for i, item in enumerate(node):
                _validate(item, items_schema, f"{path}[{i}]", errors)

    elif isinstance(node, (int, float)) and not isinstance(node, bool):
        if "minimum" in schema and node < schema["minimum"]:
            errors.append(f"{path}: minimum violated ({node} < {schema['minimum']})")


def validate_against_schema(manifest: Any, schema: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    _validate(manifest, schema, "$", errors)
    return errors


# ---------------------------------------------------------------------------
# Cross-field invariants (the real value of this smoke)
# ---------------------------------------------------------------------------

def check_invariants(manifest: Dict[str, Any]) -> List[Tuple[str, bool, str]]:
    summary = manifest.get("summary", {})
    out: List[Tuple[str, bool, str]] = []

    def chk(name: str, predicate: bool, detail: str) -> None:
        out.append((name, bool(predicate), detail))

    sign_records = manifest.get("sign_records", [])
    tablets = manifest.get("tablets", [])
    missing = manifest.get("missing_tablets_preview", [])

    chk(
        "summary.available_sign_record_count == len(sign_records)",
        summary.get("available_sign_record_count") == len(sign_records),
        f"summary={summary.get('available_sign_record_count')!r} vs len={len(sign_records)}",
    )
    chk(
        "summary.downloaded_tablet_count == len(tablets)",
        summary.get("downloaded_tablet_count") == len(tablets),
        f"summary={summary.get('downloaded_tablet_count')!r} vs len={len(tablets)}",
    )
    chk(
        "summary.missing_tablet_count == len(missing_tablets_preview)",
        summary.get("missing_tablet_count") == len(missing),
        f"summary={summary.get('missing_tablet_count')!r} vs len={len(missing)}",
    )
    chk(
        "summary.annotated_tablet_count == downloaded + missing",
        summary.get("annotated_tablet_count")
        == (summary.get("downloaded_tablet_count", 0) + summary.get("missing_tablet_count", 0)),
        f"annotated={summary.get('annotated_tablet_count')!r} vs downloaded+missing="
        f"{summary.get('downloaded_tablet_count', 0) + summary.get('missing_tablet_count', 0)}",
    )
    chk(
        "schema_version == 1",
        manifest.get("schema_version") == 1,
        f"schema_version={manifest.get('schema_version')!r}",
    )
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run(
    manifest_path: Path,
    schema_path: Path,
    expected_sha256: str | None,
    report_path: Path | None,
    manifest_label: str | None = None,
    schema_label: str | None = None,
) -> int:
    raw = manifest_path.read_bytes()
    observed_sha = sha256_of_bytes(raw)
    schema = json.loads(schema_path.read_text())
    schema_sha = sha256_of_bytes(schema_path.read_bytes())

    failures: List[str] = []

    if expected_sha256 is not None and expected_sha256 != observed_sha:
        failures.append(
            f"sha256 mismatch: expected={expected_sha256} observed={observed_sha}"
        )

    try:
        manifest = json.loads(raw.decode("utf-8"))
    except Exception as exc:  # pragma: no cover - defensive
        failures.append(f"json parse error: {exc!r}")
        manifest = None

    schema_errors: List[str] = []
    invariant_results: List[Tuple[str, bool, str]] = []
    if manifest is not None:
        schema_errors = validate_against_schema(manifest, schema)
        if schema_errors:
            failures.extend(f"schema: {e}" for e in schema_errors)
        invariant_results = check_invariants(manifest)
        for name, ok, detail in invariant_results:
            if not ok:
                failures.append(f"invariant: {name} :: {detail}")

    verdict = "PASS" if not failures else "FAIL"

    report = {
        "smoke_target_id": SMOKE_TARGET_ID,
        "verdict": verdict,
        "manifest_path": manifest_label if manifest_label is not None else str(manifest_path),
        "manifest_sha256": observed_sha,
        "manifest_sha256_pinned": expected_sha256,
        "manifest_bytes": len(raw),
        "schema_path": schema_label if schema_label is not None else str(schema_path),
        "schema_sha256": schema_sha,
        "schema_errors": schema_errors,
        "invariants": [
            {"name": name, "ok": ok, "detail": detail}
            for name, ok, detail in invariant_results
        ],
        "failures": failures,
        "governing_verdict": GOVERNING_VERDICT,
        "governing_1nn_accuracy": GOVERNING_1NN_ACCURACY,
        "note": (
            "Smoke checks custody and shape only. A PASS does NOT repair "
            "NO_GO_GOVERNING_GATE_UNMET, does NOT change governing_1nn_accuracy, "
            "and does NOT promote any P6/P7 diagnostic into a gate closure."
        ),
    }

    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True))

    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if verdict == "PASS" else 1


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--schema", required=True, type=Path)
    parser.add_argument(
        "--checksum",
        default=None,
        help="expected sha256 (omit to compute observed only — not recommended for evidence runs)",
    )
    parser.add_argument(
        "--report",
        default=None,
        type=Path,
        help="path to write deterministic JSON report",
    )
    parser.add_argument(
        "--manifest-label",
        default=None,
        help=(
            "optional symbolic label to write into the report's manifest_path "
            "field (e.g. '<MONOREPO>/workspace/…/manifest.json'). Parameterizes "
            "operational paths so reports can be committed without leaking "
            "local absolute paths. Falls back to --manifest if omitted."
        ),
    )
    parser.add_argument(
        "--schema-label",
        default=None,
        help="optional symbolic label for the report's schema_path field.",
    )
    args = parser.parse_args(argv)
    return run(
        args.manifest,
        args.schema,
        args.checksum,
        args.report,
        manifest_label=args.manifest_label,
        schema_label=args.schema_label,
    )


if __name__ == "__main__":
    raise SystemExit(main())
