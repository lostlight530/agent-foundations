# Contributing

Contributions are welcome when they improve Agent Foundations' verified core, source registry, reproducibility, documentary tooling, bilingual consistency, or repository infrastructure without strengthening claims beyond their evidence.

## Start from the current core

Use [`FOUNDATION/INDEX.md`](FOUNDATION/INDEX.md) to locate the current owning surface. In particular:

- `FOUNDATION/EVIDENCE.md` owns claim/evidence semantics;
- `FOUNDATION/SOURCES.md` owns canonical external-source identities;
- `FOUNDATION/PROVENANCE.md` owns source/version, producer, reproducibility, correction, and AI-use provenance;
- `FOUNDATION/ARCHITECTURE.md`, `MEMORY.md`, `TOOLS.md`, and `COLLABORATION.md` own their research domains;
- `FOUNDATION/REVIEW.md` owns review disposition;
- `FOUNDATION/MAINTENANCE.md` owns verified-core maintenance rules;
- validator/schema/test files own structural executable checks;
- root metadata, `.github/`, security, citation, and release files are repository infrastructure.

Historical audits and generated research streams remain inputs or point-in-time evidence. They are not automatically current verified-core authority.

## Claim and source changes

Keep the repository's dimensions separate:

```text
source registered != claim supported
claim supported != implemented
implemented != validated
reviewed != reproduced
repository DOI != external scientific source
```

Preserve stable Claim IDs unless a deliberate migration is required. When a claim changes, update both language surfaces that share the Claim ID and keep evidence, mapping, implementation, and validation states aligned.

For an external source, preserve canonical source identity. A later arXiv version is provenance for the same paper identity unless the source itself is genuinely different. Pair version and date only when that pairing has been verified.

## Executable and schema changes

For validator, schema, helper, or other executable changes:

1. define the behavior or defect at a named revision;
2. add or update proportionate regression coverage;
3. keep structural validation distinct from theorem/claim validation;
4. document any compatibility or protected-path effect.

Current verification entry points include:

```bash
python FOUNDATION/validate.py
python -m unittest FOUNDATION.test_contract -v
python FOUNDATION/validate.py --base-ref origin/main
```

Record only checks actually executed. A validator present in the repository is not an executed result.

## Evidence and provenance

A material research change should make it possible to recover the source identity/version, checked surface, supported proposition, assumptions, limitation, current status, and repository mapping.

Do not silently rewrite historical material merely because later evidence improves the current interpretation. Preserve conflicts and insufficient evidence explicitly.

AI assistance may support drafting, translation, organization, or candidate-source discovery. Generated output is not evidence by itself; contributors remain responsible for every claim, citation, and validation result.

## Pull requests

Use the repository pull-request template and include:

- the problem and bounded change;
- affected Claim IDs, sources, core documents, executable checks, or metadata;
- evidence/rationale and current status impact;
- validation actually performed;
- material checks or source surfaces not examined;
- bilingual, compatibility, historical, and provenance impact;
- security/privacy impact when relevant;
- a practical rollback.

## Security, privacy, license, and attribution

Follow `SECURITY.md` for sensitive reports. Do not publish credentials, private data, or exploit details requiring coordinated disclosure.

Contributions to repository-owned work are submitted under the current `LICENSE`. Third-party sources retain their own attribution and licensing. Git/PR history remains the source of contribution attribution.
