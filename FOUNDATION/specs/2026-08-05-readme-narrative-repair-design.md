# Agent Foundations README Narrative Repair Design

Date: 2026-08-05
Status: approved design baseline
Base: `main@28a4787fd834c1b9f396184937026cd8c5b16d65`

## Objective

Replace the root README's obsolete deterministic-agent and convergence claims with a bilingual entry point to the independently maintained `FOUNDATION/` evidence system. Existing SOP-generated documents, Pages content, and automation remain untouched.

## Verified starting point

`FOUNDATION/` explicitly defines the repository as a theory and evidence base, not an autonomous-agent runtime. It distinguishes repository tests, primary standards, peer-reviewed evidence, preprints, analogies, proposals, and unverified claims. The root README still says the repository mathematically proves deterministic behavior, guarantees convergence, deployed DecDPO, and is theoretically immune to failures. Those claims contradict the verified core.

## README design

The replacement README will:

1. identify the repository as a bilingual theory, evidence, and architecture-decision base;
2. direct readers to the verified-core reading order;
3. explain Claim IDs, evidence levels, implementation states, and validation states;
4. summarize architecture, memory, tools, and collaboration as bounded research domains;
5. distinguish external results, proposals, pseudocode, and executable repository evidence;
6. provide the validator and test commands;
7. explain the ownership boundary between `FOUNDATION/` and the existing SOP-generated `docs/` stream;
8. remove monthly incident narratives, unverified deployment statements, and convergence/safety guarantees.

## Protected-path design

`FOUNDATION/validate.py` retains `README.md` as protected by default and gains a repeatable exact-path allowance. The verification workflow passes the README allowance only when the PR carries the maintainer-applied `scope:approved-readme` label. Homepage, license, and bilingual docs READMEs remain protected without exemption.

## Verification and acceptance

`FOUNDATION/validate.py` and `FOUNDATION/test_contract.py` must pass on Python 3.12 and 3.14. New tests cover default denial and the exact README allowance. The README must contain no forbidden absolute phrases, every linked path must exist, and its capability statements must match the implementation/validation states in `FOUNDATION/`.

## Non-goals and rollback

No edit to `docs/**`, homepage, monthly blueprints, Jules/SOP automation, source registry semantics, or claim records. Delivery uses one PR from `codex/scientific-closure-20260805`. Rollback is a merge-commit revert.
