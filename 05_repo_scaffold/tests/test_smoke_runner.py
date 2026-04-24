"""Self-test for the smoke runner.

Runs the manifest-validation runner against bundled synthetic fixtures.
A passing fixture must yield verdict PASS; a fixture with a deliberate
invariant violation must yield verdict FAIL. The test is hermetic — no
network, no filesystem outside `tests/fixtures/`, no third-party deps.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from cuneiform_control.smoke import run_manifest_validation as smoke  # noqa: E402


FIXTURES = ROOT / "tests" / "fixtures"
SCHEMA = ROOT / "code" / "cuneiform_control" / "schemas" / "benchmark_manifest.schema.json"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


class SmokeRunnerSelfTest(unittest.TestCase):
    def test_min_pass_fixture_returns_pass(self):
        manifest = FIXTURES / "manifest_min_pass.json"
        report_path = FIXTURES / ".tmp_report_pass.json"
        try:
            rc = smoke.run(
                manifest_path=manifest,
                schema_path=SCHEMA,
                expected_sha256=sha256_of(manifest),
                report_path=report_path,
            )
            self.assertEqual(rc, 0, "min-pass fixture must return exit 0")
            report = json.loads(report_path.read_text())
            self.assertEqual(report["verdict"], "PASS")
            self.assertEqual(report["schema_errors"], [])
            self.assertTrue(all(inv["ok"] for inv in report["invariants"]))
            self.assertEqual(report["governing_verdict"], "NO_GO_GOVERNING_GATE_UNMET")
            self.assertEqual(report["governing_1nn_accuracy"], 0.021916)
        finally:
            if report_path.exists():
                report_path.unlink()

    def test_invariant_fail_fixture_returns_fail(self):
        manifest = FIXTURES / "manifest_min_fail_invariant.json"
        report_path = FIXTURES / ".tmp_report_fail.json"
        try:
            rc = smoke.run(
                manifest_path=manifest,
                schema_path=SCHEMA,
                expected_sha256=sha256_of(manifest),
                report_path=report_path,
            )
            self.assertEqual(rc, 1, "invariant-fail fixture must return exit 1")
            report = json.loads(report_path.read_text())
            self.assertEqual(report["verdict"], "FAIL")
            # The summary counts disagree with array lengths; at least one
            # invariant must report ok=False.
            self.assertTrue(any(not inv["ok"] for inv in report["invariants"]))
            # Governing verdict still preserved.
            self.assertEqual(report["governing_verdict"], "NO_GO_GOVERNING_GATE_UNMET")
        finally:
            if report_path.exists():
                report_path.unlink()

    def test_sha256_mismatch_returns_fail(self):
        manifest = FIXTURES / "manifest_min_pass.json"
        report_path = FIXTURES / ".tmp_report_sha.json"
        try:
            rc = smoke.run(
                manifest_path=manifest,
                schema_path=SCHEMA,
                expected_sha256="0" * 64,
                report_path=report_path,
            )
            self.assertEqual(rc, 1, "sha256 mismatch must return exit 1")
            report = json.loads(report_path.read_text())
            self.assertEqual(report["verdict"], "FAIL")
            self.assertTrue(
                any("sha256 mismatch" in f for f in report["failures"]),
                f"failures should mention sha256 mismatch: {report['failures']}",
            )
        finally:
            if report_path.exists():
                report_path.unlink()


if __name__ == "__main__":
    unittest.main()
