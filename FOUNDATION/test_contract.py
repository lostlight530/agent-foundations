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
    def test_protected_change_fails(self) -> None:
        with patch.object(validator, "changed_paths", return_value={"README.md", "FOUNDATION/INDEX.md"}):
            errors = validator.validate("origin/main")
        self.assertIn("protected paths changed: ['README.md']", errors)

    def test_foundation_only_change_passes_protected_gate(self) -> None:
        with patch.object(validator, "changed_paths", return_value={"FOUNDATION/INDEX.md"}):
            errors = validator.validate("origin/main")
        self.assertFalse(any(error.startswith("protected paths changed") for error in errors))


if __name__ == "__main__":
    unittest.main()
