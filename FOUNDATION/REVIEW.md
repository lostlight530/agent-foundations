# Verified-Core Review States / 可验证核心审核状态

Status: public documentary review vocabulary

## Purpose / 目的

This file records public review states for Agent Foundations claims and historical research corrections.

It describes evidence disposition only. It does not execute repository behavior or create implementation capability.

## Review states / 审核状态

1. `REVIEW_PENDING`
   - material has entered review
2. `SOURCE_IDENTITY_VERIFIED`
   - the cited source identity/version is established where material
3. `CLAIM_SURFACE_VERIFIED`
   - the strongest inspected source surface is identified and bounded
4. `PRIMARY_SOURCE_CONFLICT`
   - checked primary surfaces disagree
5. `INSUFFICIENT_EVIDENCE`
   - available evidence cannot support the requested claim strength
6. `MAPPING_SCOPED`
   - external evidence is classified as requirement, analogy, candidate mechanism, counterevidence, or out of scope
7. `IMPLEMENTATION_SEPARATED`
   - external result and local implementation/validation status are explicitly distinct
8. `CALIBRATION_REQUIRED`
   - historical material remains useful but interpretation/provenance requires correction
9. `CALIBRATED`
   - an explicit erratum/reconciliation records the current bounded interpretation
10. `ACCEPTED_FOR_VERIFIED_CORE`
   - the proposition fits the current public evidence contract

These are documentary states, not confidence scores.

## Review sequence / 审核顺序

A normal review can move through:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → CLAIM_SURFACE_VERIFIED → MAPPING_SCOPED → IMPLEMENTATION_SEPARATED → ACCEPTED_FOR_VERIFIED_CORE`

A correction can move through:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → CLAIM_SURFACE_VERIFIED → CALIBRATION_REQUIRED → CALIBRATED → MAPPING_SCOPED → IMPLEMENTATION_SEPARATED`

A conflict can stop at:

`PRIMARY_SOURCE_CONFLICT`.

An evidence-limited claim can stop at:

`INSUFFICIENT_EVIDENCE`.

No state transition makes an external result an implementation unless a concrete repository artifact independently establishes implementation.

## Review checks / 审核检查

When relevant, verify that:

- explicit arXiv `vN` citations use the date belonging to that version
- source identity is not confused with theorem/equation verification
- abstract support is not promoted into theorem support
- a mechanism equation is not promoted into a convergence/error bound without the supplying theorem
- unverified long formulas remain bounded paper-level evidence
- primary-source disagreements remain unresolved until stronger evidence resolves them
- mathematical results retain their assumptions, comparator, domain, quantifiers, and version
- external results are not upgraded into local implementation claims
- `DESIGN_ANALOGY`, `CANDIDATE_MECHANISM`, `REFERENCE_ONLY`, `NOT_IMPLEMENTED`, and other status axes remain distinct
- bilingual research does not strengthen a claim merely through translation
- later weaving/errata does not rewrite the originating research period

## Repository evidence surfaces / 仓库证据面

- `EVIDENCE.md` — claim/evidence vocabulary and validator boundary
- `SOURCES.md` — canonical S01–S32 source identities
- `PROVENANCE.md` — source/version and historical provenance semantics
- four domain claim maps — architecture/memory/tools/collaboration propositions
- `claim.schema.json` — machine-readable claim vocabulary
- `validate.py` — structural/documentary validator
- `arxiv_probe.py` — bibliographic identity/version helper
- August errata — explicit historical corrections

These surfaces complement one another. None is a semantic truth oracle.

## Current August calibration examples / 当前 8 月校准示例

The W33/W34 errata demonstrate several review states in practice:

- explicit later-version citations paired with v1 dates → source-version calibration required
- corrected version/date pairs → `CALIBRATED`
- mechanism equation presented too strongly as a formal bound → claim strength narrowed
- conflict between primary source surfaces → preserved as `PRIMARY_SOURCE_CONFLICT`
- source identity corrected without claiming the paper mechanism is implemented locally

## Minimal public review record / 最小公开审核记录

A durable review record may contain:

- Claim ID or artifact
- current review state
- public source identity/version
- strongest checked source surface
- supported proposition and assumptions
- mapping state
- implementation/validation state
- missing or conflicting evidence
- erratum pointer when applicable
- final bounded disposition

The review record should contain only information necessary to understand and audit the public evidence decision.