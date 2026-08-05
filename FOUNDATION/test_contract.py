from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("validate.py")
SPEC = importlib.util.spec_from_file_location("foundation_validator", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
README_PATH = MODULE_PATH.parents[1] / "README.md"
README_TEXT = README_PATH.read_text(encoding="utf-8")


class ParsingTests(unittest.TestCase):
    def test_claim_blocks_preserve_boundaries(self) -> None:
        text = "# T\n## AF-MEM-001 — A\nbody\n## AF-MEM-002 — B\nnext\n"
        blocks = validator.claim_blocks(text)
        self.assertEqual([claim_id for claim_id, _ in blocks], ["AF-MEM-001", "AF-MEM-002"])
        self.assertNotIn("AF-MEM-002", blocks[0][1])

    def test_registered_sources(self) -> None:
        text = "# Sources\n## S01 — One\n## S18 — Last\n"
        self.assertEqual(validator.registered_sources(text), {"S01", "S18"})

    def test_action_reference_parser(self) -> None:
        text = "steps:\n  - uses: actions/checkout@" + "a" * 40 + " # v6\n"
        self.assertEqual(validator.action_references(text), ["actions/checkout@" + "a" * 40])


class SchemaTests(unittest.TestCase):
    def test_schema_is_draft_2020_12_and_closed(self) -> None:
        schema = json.loads((validator.FOUNDATION / "claim.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])


class ProtectedPathTests(unittest.TestCase):
    def test_root_readme_is_denied_by_default(self) -> None:
        with patch.object(validator, "changed_paths", return_value={"README.md", "FOUNDATION/INDEX.md"}):
            errors = validator.validate("origin/main")
        self.assertIn("protected paths changed: ['README.md']", errors)

    def test_root_readme_is_allowed_only_when_explicit(self) -> None:
        with patch.object(validator, "changed_paths", return_value={"README.md", "FOUNDATION/INDEX.md"}):
            errors = validator.validate("origin/main", {"README.md"})
        self.assertFalse(any(error.startswith("protected paths changed") for error in errors))

    def test_root_readme_allowance_does_not_allow_other_protected_paths(self) -> None:
        changed = {"README.md", "index.html", "LICENSE", "docs/en/README.md", "docs/zh/README.md"}
        with patch.object(validator, "changed_paths", return_value=changed):
            errors = validator.validate("origin/main", {"README.md"})
        self.assertIn(
            "protected paths changed: ['LICENSE', 'docs/en/README.md', 'docs/zh/README.md', 'index.html']",
            errors,
        )

    def test_allowed_paths_normalize_slashes_but_remain_exact(self) -> None:
        changed = {"docs/en/README.md", "docs/zh/README.md"}
        with patch.object(validator, "changed_paths", return_value=changed):
            errors = validator.validate("origin/main", {"docs\\en\\README.md"})
        self.assertIn("protected paths changed: ['docs/zh/README.md']", errors)

    def test_foundation_only_change_passes_protected_gate(self) -> None:
        with patch.object(validator, "changed_paths", return_value={"FOUNDATION/INDEX.md"}):
            errors = validator.validate("origin/main")
        self.assertFalse(any(error.startswith("protected paths changed") for error in errors))

class ReadmeNarrativeTests(unittest.TestCase):
    def test_obsolete_guarantees_and_monthly_claims_are_absent(self) -> None:
        forbidden = (
            "fully deterministic",
            "deterministic behavioral guarantees",
            "guarantee convergence",
            "guarantees convergence",
            "inevitable convergence",
            "officially deployed",
            "theoretically immune",
            "monthly strategic blueprint",
            "this month, industry",
            "完全确定性",
            "确定性行为保证",
            "保证收敛",
            "必然稳定",
            "正式部署的 decdpo",
            "理论免疫",
            "月度理论防线",
            "本月业内",
        )
        lowered = README_TEXT.casefold()
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase.casefold(), lowered)

    def test_verified_core_links_follow_index_reading_order(self) -> None:
        paths = (
            "FOUNDATION/EVIDENCE.md",
            "FOUNDATION/ARCHITECTURE.md",
            "FOUNDATION/MEMORY.md",
            "FOUNDATION/TOOLS.md",
            "FOUNDATION/COLLABORATION.md",
            "FOUNDATION/SOURCES.md",
            "FOUNDATION/PROVENANCE.md",
        )
        positions = [README_TEXT.index(f"({path})") for path in paths]
        self.assertEqual(positions, sorted(positions))

    def test_bilingual_sections_share_evidence_and_status_axes(self) -> None:
        english, chinese = README_TEXT.split("## 中文", maxsplit=1)
        shared_tokens = (
            "E0_REPOSITORY_TEST",
            "E1_PRIMARY_STANDARD",
            "E2_PEER_REVIEWED",
            "E3_REPRODUCIBLE_PREPRINT",
            "E4_PREPRINT",
            "E5_BACKGROUND",
            "E6_UNVERIFIED",
            "DIRECT_REQUIREMENT",
            "DESIGN_ANALOGY",
            "CANDIDATE_MECHANISM",
            "COUNTEREVIDENCE",
            "OUT_OF_SCOPE",
            "NOT_IMPLEMENTED",
            "REFERENCE_ONLY",
            "PARTIAL_PROTOTYPE",
            "IMPLEMENTED",
            "NOT_TESTED",
            "STATIC_CHECKED",
            "EXPERIMENTALLY_TESTED",
            "REPRODUCED",
            "EXTERNALLY_REVIEWED",
        )
        for token in shared_tokens:
            with self.subTest(token=token):
                self.assertIn(token, english)
                self.assertIn(token, chinese)

if __name__ == "__main__":
    unittest.main()
