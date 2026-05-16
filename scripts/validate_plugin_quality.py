#!/usr/bin/env python3
"""Validate the Avalonia 12 plugin routing, evidence, and evaluation assets."""

from __future__ import annotations

import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[1]
AVALONIA_REPO = WORKSPACE / "frameworks" / "Avalonia"
AI_PROJECTS = WORKSPACE / "docs" / "reference" / "ai-desktop-projects.md"

EXPECTED_SKILLS = {
    "avalonia-12-migration",
    "avalonia-accessibility-and-validation",
    "avalonia-bindings-and-xaml",
    "avalonia-bootstrap-and-lifetime",
    "avalonia-controls-and-windowing",
    "avalonia-design-systems",
    "avalonia-fluent-design",
    "avalonia-input-and-commands",
    "avalonia-layout-and-virtualization",
    "avalonia-platform-services",
    "avalonia-rendering-and-graphics",
    "avalonia-styling-and-resources",
    "avalonia-testing-diagnostics-and-performance",
    "avalonia-threading-and-dispatcher",
    "avalonia-views-and-templating",
    "html-css-to-avalonia",
    "winforms-to-avalonia",
    "winui-to-avalonia",
    "wpf-to-avalonia",
}

EVIDENCE_MARKERS = [
    "Avalonia 12 source facts",
    "Avalonia 12 project patterns",
    "Avalonia 11.x migration contrast",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(ROOT)}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def validate_source_baseline() -> list[str]:
    version_props = read(AVALONIA_REPO / "build" / "SharedVersion.props")
    tfm_props = read(AVALONIA_REPO / "build" / "TargetFrameworks.props")
    require("<Version>12.1.999</Version>" in version_props, "Avalonia source baseline is not 12.1.999")
    require("<AvsCurrentTargetFramework>net10.0</AvsCurrentTargetFramework>" in tfm_props, "Avalonia source baseline is not net10.0")
    return ["source-baseline=12.1.999/net10.0"]


def validate_reference_projects() -> list[str]:
    body = read(AI_PROJECTS)
    for project in ["mnemo", "Netor.Cartana", "ClippyAI"]:
        require(project in body, f"missing Avalonia 12 reference project evidence: {project}")
    for project in ["Everywhere", "StabilityMatrix", "avallama", "WhisperVoiceInput"]:
        require(project in body and "排除默认参考" in body, f"missing exclusion evidence for {project}")
    return ["reference-projects=3-default-avalonia-12"]


def validate_skill_catalog() -> list[str]:
    skill_dirs = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    require(skill_dirs == EXPECTED_SKILLS, f"unexpected skill catalog: {sorted(skill_dirs ^ EXPECTED_SKILLS)}")

    root_skill = read(ROOT / "SKILL.md")
    for skill in sorted(EXPECTED_SKILLS):
        require(f"skills/{skill}/SKILL.md" in root_skill, f"root SKILL.md does not route to {skill}")

    for skill in sorted(EXPECTED_SKILLS):
        skill_file = ROOT / "skills" / skill / "SKILL.md"
        body = read(skill_file)
        require("../../references/70-avalonia-12-source-and-reference-baseline.md" in body, f"{skill} lacks Avalonia 12 baseline reference")
        for marker in EVIDENCE_MARKERS:
            require(marker in body, f"{skill} lacks evidence marker: {marker}")
        agent_file = ROOT / "skills" / skill / "agents" / "openai.yaml"
        agent = read(agent_file)
        require("Avalonia 12" in agent, f"{skill} agent prompt is not Avalonia 12 explicit")

    return [f"skills={len(EXPECTED_SKILLS)}"]


def validate_plugin_manifest() -> list[str]:
    manifest = json.loads(read(ROOT / ".codex-plugin" / "plugin.json"))
    require(manifest["name"] == "avalonia-codex-plugin", "plugin manifest name changed unexpectedly")
    require(manifest["skills"] == "./skills/", "plugin manifest skills path is not ./skills/")
    interface = manifest.get("interface", {})
    require("Avalonia 12" in manifest.get("description", ""), "manifest description is not Avalonia 12 explicit")
    require("Avalonia 12" in interface.get("longDescription", ""), "manifest longDescription is not Avalonia 12 explicit")
    return ["plugin-manifest=ok"]


def validate_evaluation_assets() -> list[str]:
    routing_ref = read(ROOT / "references" / "71-skill-routing-and-evaluation.md")
    evals = read(ROOT / "evals" / "avalonia-12-plugin-prompts.md")
    examples = read(ROOT / "examples" / "avalonia-12-task-samples.md")

    for marker in [
        "umbrella",
        "app-building",
        "migration",
        "debugging",
        "source-reference",
        "ui-patterns",
    ]:
        require(marker in routing_ref, f"routing reference lacks lane marker: {marker}")

    require(evals.count("## Eval ") >= 8, "evaluation prompt set must contain at least 8 evals")
    require(evals.count("Expected route:") >= 8, "evaluation prompt set must name expected routes")
    require(examples.count("## Sample ") >= 5, "task samples must contain at least 5 samples")
    return ["evals>=8", "samples>=5"]


def validate_plan_scope() -> list[str]:
    superseded_preview_files = [
        ROOT / "plan" / "avalonia-12-preview2-migration-reference-update-plan.md",
        ROOT / "plan" / "avalonia-12-preview2-migration-analysis.md",
    ]

    for path in superseded_preview_files:
        body = read(path)
        require("Superseded" in body, f"{path.relative_to(ROOT)} must be explicitly marked superseded")
        require("historical" in body.lower(), f"{path.relative_to(ROOT)} must describe its historical-only status")
        require("12.1.999" in body, f"{path.relative_to(ROOT)} must point to the current Avalonia 12 baseline")
        require("net10.0" in body, f"{path.relative_to(ROOT)} must point to the current target framework")
        require(
            "Do not" in body and "current guidance" in body,
            f"{path.relative_to(ROOT)} must warn against reuse as current guidance",
        )

    closeout = ROOT / "plan" / "avalonia-12-plugin-rewrite-audit.md"
    body = read(closeout)
    for marker in [
        "Systematic Reclose",
        "Scope",
        "Findings",
        "Changes",
        "Verification",
        "Residual Risks",
        "Next Minimal Tasks",
    ]:
        require(marker in body, f"closeout report lacks section marker: {marker}")

    return ["plan-scope=ok"]


def validate_forbidden_default_11x() -> list[str]:
    forbidden = [
        re.compile(r"default(?:[^\\n]{0,80})11\\.3\\.12", re.IGNORECASE),
        re.compile(r"stable lane", re.IGNORECASE),
        re.compile(r"api-index-12\\.0\\.0-rc1-generated"),
        re.compile(r"Repository: `Avalonia@11\\.3\\.12`"),
        re.compile(r"Avalonia git ref: `11\\.3\\.12`"),
    ]

    scanned = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".json"}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("plan/"):
            # Historical audit and planning files intentionally quote old search
            # patterns and removed artifact names. They are reviewed separately.
            continue
        text = read(path)
        scanned += 1
        for pattern in forbidden:
            if pattern.search(text):
                fail(f"forbidden default 11.x marker in {rel}: {pattern.pattern}")

    return [f"default-11x-scan-files={scanned}"]


def main() -> int:
    checks: list[str] = []
    checks.extend(validate_source_baseline())
    checks.extend(validate_reference_projects())
    checks.extend(validate_skill_catalog())
    checks.extend(validate_plugin_manifest())
    checks.extend(validate_evaluation_assets())
    checks.extend(validate_plan_scope())
    checks.extend(validate_forbidden_default_11x())
    print("OK: " + ", ".join(checks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
