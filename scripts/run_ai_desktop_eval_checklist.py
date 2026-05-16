#!/usr/bin/env python3
"""Emit or validate the Avalonia 12 AI desktop eval checklist."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHECKLIST = ROOT / "evals" / "avalonia-12-ai-desktop-eval-checklist.md"

REQUIRED_CASES = [
    "AI Desktop Workbench",
    "Tray Utility and Clipboard Flow",
    "Overlay and Notification Review",
    "Plugin MCP Settings",
]

REQUIRED_FIELDS = [
    "Expected route:",
    "Actual route:",
    "Evidence classes observed:",
    "No-copy result:",
    "Avalonia source verification:",
    "Notes:",
]


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_checklist() -> list[str]:
    body = read_text(CHECKLIST)
    missing: list[str] = []

    for case in REQUIRED_CASES:
        if f"## Eval Case: {case}" not in body:
            missing.append(f"missing case: {case}")

    for field in REQUIRED_FIELDS:
        if field not in body:
            missing.append(f"missing field: {field}")

    for marker in [
        "mnemo",
        "Netor.Cartana",
        "ClippyAI",
        "Everywhere",
        "StabilityMatrix",
        "avallama",
        "WhisperVoiceInput",
        "Avalonia 12 source facts",
        "Avalonia 12 project patterns",
        "Avalonia 11.x migration contrast",
        "No-copy",
        "73-avalonia-12-ai-desktop-product-patterns.md",
        "74-avalonia-12-ai-desktop-recipes-and-checklists.md",
    ]:
        if marker not in body:
            missing.append(f"missing marker: {marker}")

    return missing


def emit_json() -> int:
    missing = validate_checklist()
    payload = {
        "checklist": str(CHECKLIST.relative_to(ROOT)),
        "cases": REQUIRED_CASES,
        "requiredFields": REQUIRED_FIELDS,
        "valid": not missing,
        "missing": missing,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not missing else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate checklist structure")
    parser.add_argument("--json", action="store_true", help="emit JSON checklist metadata")
    args = parser.parse_args()

    if args.json:
        return emit_json()

    missing = validate_checklist()
    if args.check:
        if missing:
            for item in missing:
                print(f"FAIL: {item}")
            return 1
        print("OK: ai-desktop-eval-checklist=ok")
        return 0

    print(read_text(CHECKLIST))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
