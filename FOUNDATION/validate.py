#!/usr/bin/env python3
"""Deterministic contract checks for the independent Agent Foundations core."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "FOUNDATION"

DOMAIN_FILES = (
    FOUNDATION / "ARCHITECTURE.md",
    FOUNDATION / "COLLABORATION.md",
    FOUNDATION / "MEMORY.md",
    FOUNDATION / "TOOLS.md",
)

REQUIRED_FILES = (
    FOUNDATION / "INDEX.md",
    FOUNDATION / "EVIDENCE.md",
    FOUNDATION / "SOURCES.md",
    FOUNDATION / "PROVENANCE.md",
    FOUNDATION / "claim.schema.json",
    FOUNDATION / "validate.py",
    FOUNDATION / "test_contract.py",
    *DOMAIN_FILES,
)

PROTECTED_PATHS = {
    "README.md",
    "index.html",
    "LICENSE",
    "docs/en/README.md",
    "docs/zh/README.md",
}

CLAIM_HEADING_RE = re.compile(r"^## (AF-(?:ARCH|COLLAB|MEM|TOOL)-\d{3})\b", re.MULTILINE)
SOURCE_HEADING_RE = re.compile(r"^## (S\d{2})\b", re.MULTILINE)
SOURCE_REF_RE = re.compile(r"\bS\d{2}\b")
USES_RE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
FULL_SHA_RE = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")

REQUIRED_METADATA = (
    "State / 状态:",
    "Evidence / 证据:",
    "Mapping / 映射:",
    "Implementation / 实现:",
    "Validation / 验证:",
    "Sources / 来源:",
    "Scope and limits / 范围与局限:",
)

FORBIDDEN_PHRASES = (
    "absolutely safe",
    "fully immune",
    "inevitably convergent",
    "zero hallucination",
    "100% mathematical immunity",
    "绝对安全",
    "完全免疫",
    "零幻觉",
    "必然收敛",
)


def claim_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(CLAIM_HEADING_RE.finditer(text))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(1), text[match.start():end]))
    return blocks


def registered_sources(text: str) -> set[str]:
    return set(SOURCE_HEADING_RE.findall(text))


def action_references(text: str) -> list[str]:
    return USES_RE.findall(text)


def changed_paths(base_ref: str) -> set[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def validate(base_ref: str | None = None, allowed_protected: set[str] | None = None) -> list[str]:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT).as_posix()}")

    schema_path = FOUNDATION / "claim.schema.json"
    if schema_path.is_file():
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid claim schema JSON: {exc}")
        else:
            if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                errors.append("claim schema must declare Draft 2020-12")
            if schema.get("additionalProperties") is not False:
                errors.append("claim schema must reject unknown top-level properties")

    source_path = FOUNDATION / "SOURCES.md"
    sources = registered_sources(source_path.read_text(encoding="utf-8")) if source_path.is_file() else set()
    if sources and sources != {f"S{number:02d}" for number in range(1, 35)}:
        errors.append("source registry must contain the contiguous range S01-S34")

    all_claim_ids: list[str] = []
    for path in DOMAIN_FILES:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        blocks = claim_blocks(text)
        if not blocks:
            errors.append(f"no claim blocks in {path.relative_to(ROOT).as_posix()}")
            continue
        for claim_id, block in blocks:
            all_claim_ids.append(claim_id)
            for label in REQUIRED_METADATA:
                if label not in block:
                    errors.append(f"{claim_id} missing metadata: {label}")
            referenced = set(SOURCE_REF_RE.findall(block))
            missing = referenced - sources
            if missing:
                errors.append(f"{claim_id} references unregistered sources: {sorted(missing)}")
            if not referenced:
                errors.append(f"{claim_id} has no registered source")
            lowered = block.casefold()
            found = [phrase for phrase in FORBIDDEN_PHRASES if phrase.casefold() in lowered]
            if found:
                errors.append(f"{claim_id} contains unscoped absolute language: {found}")

    duplicates = sorted(claim_id for claim_id, count in Counter(all_claim_ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate Claim IDs: {duplicates}")

    workflow_dir = ROOT / ".github" / "workflows"
    if not workflow_dir.is_dir():
        errors.append("missing .github/workflows")
    else:
        for path in sorted(workflow_dir.glob("*.y*ml")):
            for reference in action_references(path.read_text(encoding="utf-8")):
                if reference.startswith("./"):
                    continue
                if not FULL_SHA_RE.fullmatch(reference):
                    errors.append(
                        f"action not pinned to a full SHA in {path.relative_to(ROOT).as_posix()}: {reference}"
                    )

    if base_ref:
        try:
            changed = changed_paths(base_ref)
        except RuntimeError as exc:
            errors.append(f"unable to inspect protected paths: {exc}")
        else:
            allowed = {path.replace("\\", "/") for path in (allowed_protected or set())}
            violations = sorted((changed & PROTECTED_PATHS) - allowed)
            if violations:
                errors.append(f"protected paths changed: {violations}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", help="base Git ref used to enforce protected paths")
    parser.add_argument(
        "--allow-protected",
        action="append",
        default=[],
        metavar="PATH",
        help="exact protected path permitted by reviewed workflow context",
    )
    args = parser.parse_args()

    errors = validate(args.base_ref, set(args.allow_protected))
    if errors:
        print("Agent Foundations validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Agent Foundations validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
