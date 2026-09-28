#!/usr/bin/env python3
"""Run bounded structural conformance checks for the toolkit repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "_site", "dist", "build", "node_modules"}
LOCAL_ONLY_FILES = {"agent-critique.md"}

CANONICAL_PHASE_TOKENS = (
    "Ideation",
    "Requirements",
    "High-Level Architecture",
    "Detailed Design",
    "Traceability Consolidation",
    "Test Planning",
    "Implementation",
    "Packaging",
    "Documentation",
)

LIFECYCLE_SOURCES = {
    "02-governance/00-lifecycle-bootstrap.md": "# 2. Mandatory Lifecycle Sequence",
    "02-governance/12-phase-gate-checklist.md": "## 2. Lifecycle Sequence (Authoritative Order)",
    "README.md": "## Governance Model",
}

REQUIRED_SECTIONS = {
    "02-governance/00-lifecycle-bootstrap.md": (
        "## 2.1 Governed Increment Application",
        "## 10.1 Post-Release Operational Continuity",
    ),
    "02-governance/08-test-guardrail.md": (
        "## 6.1 System Validation",
        "## 14. Verification and Validation Completion and Release Criteria",
    ),
    "02-governance/13-tailoring-and-authority-guardrail.md": (
        "## 3. Governance Profiles",
        "## 4. Required Authority Assignments",
        "## 6. Controlled Uncertainty",
    ),
    "02-governance/14-operational-lifecycle-guardrail.md": (
        "## 4. Incident and Problem Management",
        "## 7. Deprecation and Retirement",
    ),
    "02-governance/15-ai-assurance-profile.md": (
        "## 3. Data and Evaluation Lineage",
        "## 4. Evaluation Design",
        "## 8. Operational Monitoring and Response",
    ),
    "04-templates/project/project-governance-profile-template.md": (
        "# 1. Governed Increment",
        "# 2. Risk-Based Profile Assessment",
        "# 3. Authority and Decision Rights",
        "# 4. Tailoring Decisions",
    ),
    "04-templates/system/test-plan-template.md": (
        "## 4.5 Verification Case Inventory",
        "## 4.6 Test Case Inventory",
        "## 4.7 Validation Strategy and Scenarios",
        "# 14. Phase Gate Declaration",
    ),
    "04-templates/system/traceability-matrix-template.md": (
        "## 3.1 Validation Traceability",
        "# 6. Bidirectional Verification Rules",
    ),
    "04-templates/system/verification-validation-report-template.md": (
        "# 5. Detailed Results",
        "# 7. System Validation Results",
        "# 15. Approval",
    ),
    "04-templates/documentation/operational-runbook-template.md": (
        "# 4. Monitoring, Thresholds, and Drift",
        "# 9. Maintenance and Operational Change",
        "# 11. Deprecation, Data Disposition, and Retirement",
    ),
}

PLATFORM_REQUIRED_PHRASES = (
    "Governed increment and approved Project Governance Profile",
    "Verification Case IDs",
    "Operational Lifecycle Guardrail",
    "AI Assurance Profile",
    "human authorization",
)

PROHIBITED_STALE_PATTERNS = {
    r"toolkit/platforms/": "stale platform path",
    r"Requirement-to-[Tt]est mapping": "obsolete requirement-to-test rule",
    r"All Requirement IDs map to Test Case IDs": "obsolete all-requirements-to-tests rule",
    r"Traditional (?:SDLC|lifecycle) models were not designed": "superseded positioning claim",
    r"Cursor is loaded only during Implementation": "vendor-specific lifecycle restriction",
}


class Validator:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.check_count = 0

    def check(self, condition: bool, message: str) -> None:
        self.check_count += 1
        if not condition:
            self.failures.append(message)

    def markdown_files(self) -> list[Path]:
        files: list[Path] = []
        for path in ROOT.rglob("*.md"):
            relative = path.relative_to(ROOT)
            if any(part in IGNORED_PARTS for part in relative.parts):
                continue
            if relative.as_posix() in LOCAL_ONLY_FILES:
                continue
            files.append(path)
        return sorted(files)

    def read(self, relative: str) -> str:
        path = ROOT / relative
        self.check(path.is_file(), f"required file is missing: {relative}")
        return path.read_text(encoding="utf-8") if path.is_file() else ""

    def check_internal_links(self, files: list[Path]) -> None:
        link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                target = target.strip().strip("<>")
                if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                file_part = unquote(target.split("#", 1)[0])
                resolved = (path.parent / file_part).resolve()
                self.check(
                    resolved.exists(),
                    f"broken internal link in {relative}: {target}",
                )

    def check_file_metadata(self, files: list[Path]) -> None:
        pattern = re.compile(r"^File:\s*(.+?)\s*$", re.MULTILINE)
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            match = pattern.search(text)
            if match:
                self.check(
                    match.group(1) == relative,
                    f"File metadata mismatch in {relative}: {match.group(1)}",
                )

    def check_markdown_tables(self, files: list[Path]) -> None:
        separator = re.compile(r"^\s*\|[-:| ]+\|\s*$")
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            lines = path.read_text(encoding="utf-8").splitlines()
            for index in range(len(lines) - 1):
                if lines[index].lstrip().startswith("|") and separator.match(lines[index + 1]):
                    header_cells = lines[index].count("|") - 1
                    separator_cells = lines[index + 1].count("|") - 1
                    self.check(
                        header_cells == separator_cells,
                        f"table shape mismatch in {relative}:{index + 1}",
                    )

    def extract_numbered_list(self, text: str, marker: str) -> list[str]:
        start = text.find(marker)
        if start < 0:
            return []
        items: list[str] = []
        for line in text[start + len(marker) :].splitlines():
            match = re.match(r"^\s*(\d+)\.\s+(.+?)\s*$", line)
            if match:
                items.append(match.group(2))
            elif items and line.strip() and not line.startswith(" "):
                break
        return items[: len(CANONICAL_PHASE_TOKENS)]

    def check_lifecycle_order(self) -> None:
        for relative, marker in LIFECYCLE_SOURCES.items():
            text = self.read(relative)
            items = self.extract_numbered_list(text, marker)
            self.check(
                len(items) == len(CANONICAL_PHASE_TOKENS),
                f"lifecycle sequence in {relative} does not contain nine phases",
            )
            for index, token in enumerate(CANONICAL_PHASE_TOKENS):
                self.check(
                    index < len(items) and token in items[index],
                    f"lifecycle phase {index + 1} in {relative} must contain '{token}'",
                )

    def check_required_sections(self) -> None:
        for relative, headings in REQUIRED_SECTIONS.items():
            text = self.read(relative)
            for heading in headings:
                self.check(
                    heading in text,
                    f"required section missing from {relative}: {heading}",
                )

    def check_platform_parity(self) -> None:
        platform_dir = ROOT / "05-platform-config"
        platform_files = sorted(platform_dir.glob("*.md"))
        self.check(bool(platform_files), "no platform configuration files found")
        for path in platform_files:
            relative = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            for phrase in PLATFORM_REQUIRED_PHRASES:
                self.check(
                    phrase in text,
                    f"platform parity phrase missing from {relative}: {phrase}",
                )

    def check_stale_patterns(self, files: list[Path]) -> None:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            for pattern, label in PROHIBITED_STALE_PATTERNS.items():
                self.check(
                    re.search(pattern, text) is None,
                    f"{label} found in {relative}",
                )

    def check_local_only_files(self) -> None:
        gitignore = self.read(".gitignore")
        ignored_lines = {
            line.strip()
            for line in gitignore.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
        for relative in LOCAL_ONLY_FILES:
            self.check(relative in ignored_lines, f"local-only file is not ignored: {relative}")

    def run(self) -> int:
        files = self.markdown_files()
        self.check(bool(files), "no Markdown files found")
        self.check_internal_links(files)
        self.check_file_metadata(files)
        self.check_markdown_tables(files)
        self.check_lifecycle_order()
        self.check_required_sections()
        self.check_platform_parity()
        self.check_stale_patterns(files)
        self.check_local_only_files()

        if self.failures:
            print(f"Toolkit conformance: FAIL ({len(self.failures)} issue(s))")
            for failure in self.failures:
                print(f"- {failure}")
            print("Automation reports structural findings; it does not approve lifecycle gates.")
            return 1

        print(f"Toolkit conformance: PASS ({self.check_count} checks)")
        print("Automation reports structural findings; it does not approve lifecycle gates.")
        return 0


if __name__ == "__main__":
    sys.exit(Validator().run())
