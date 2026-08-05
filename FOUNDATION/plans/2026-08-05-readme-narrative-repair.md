# Agent Foundations README Narrative Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the root README a truthful bilingual entry point to the verified `FOUNDATION/` core without changing the SOP-generated documentation stream.

**Architecture:** Extend the existing validator with a narrow reviewed exception for the root README, test it, then replace legacy guarantees and monthly narrative with the current claim/evidence model.

**Tech Stack:** Python 3.12/3.14, unittest, Markdown, GitHub Actions.

## Global Constraints

- Do not modify `docs/**`, homepage, monthly blueprints, Jules/SOP files, source registry semantics, or existing claims.
- README remains protected unless the PR has `scope:approved-readme`.
- Implement on `codex/scientific-closure-20260805`.

---

### Task 1: Exact protected-path exception

**Files:**
- Modify: `FOUNDATION/validate.py`
- Modify: `FOUNDATION/test_contract.py`
- Modify: `.github/workflows/verify-foundation.yml`

**Interfaces:**
- Extends: `validate(base_ref: str | None = None, allowed_protected: set[str] | None = None) -> list[str]`
- Produces: repeatable `--allow-protected PATH`

- [ ] **Step 1: Write failing tests**

Mock `changed_paths` and assert README is denied by default, allowed when exact, and that `index.html`, `LICENSE`, and bilingual docs READMEs remain denied.

- [ ] **Step 2: Run focused tests**

Run: `python -m unittest FOUNDATION.test_contract -v`  
Expected: FAIL because the allowance argument does not exist.

- [ ] **Step 3: Implement exact subtraction**

Use:
```python
allowed = {p.replace("\\", "/") for p in (allowed_protected or set())}
violations = sorted((changed & PROTECTED_PATHS) - allowed)
```
Parse `--allow-protected` with `action="append"`. The workflow adds README only for the maintainer-applied label.

- [ ] **Step 4: Verify**

Run: `python FOUNDATION/validate.py && python -m unittest FOUNDATION.test_contract -v`  
Expected: PASS.

- [ ] **Step 5: Commit**

Commit message: `test: add reviewed README ownership exception`.

### Task 2: Rewrite the root README

**Files:**
- Modify: `README.md`
- Modify: `FOUNDATION/test_contract.py`

- [ ] **Step 1: Add failing narrative/link tests**

Reject deterministic-agent guarantees, inevitable convergence, deployed DecDPO, theoretical immunity, and monthly incident claims in both languages. Require links to all files in the `FOUNDATION/INDEX.md` reading order.

- [ ] **Step 2: Write claim-equivalent English and Chinese sections**

Cover repository boundary, evidence levels, mapping/implementation/validation states, four bounded domains, validator commands, ownership split, and limitations.

- [ ] **Step 3: Run full validation**

Run: `python FOUNDATION/validate.py && python -m unittest FOUNDATION/test_contract.py -v`  
Expected: PASS on Python 3.12 and 3.14.

- [ ] **Step 4: Commit**

Commit message: `docs: ground Agent Foundations README in evidence states`.

### Task 3: Cloud PR and main verification

- [ ] **Step 1: Create/apply `scope:approved-readme` and open one PR**
- [ ] **Step 2: Require both Python matrix jobs and Pages build to pass**
- [ ] **Step 3: Merge and verify main; revert the merge commit if validation or Pages fails**
