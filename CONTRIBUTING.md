# Contributing

Contributions are welcome when they preserve Agent Foundations' evidence, provenance, verified-core admission, and maintenance boundaries.

Before proposing a change, recover current repository truth from latest merged `main` and read the relevant owner under `FOUNDATION/`, especially `EVIDENCE.md`, `PROVENANCE.md`, `REVIEW.md`, `MAINTENANCE.md`, and `independent-gpt/README.md` when maintenance/recovery is involved.

## Maintenance and producer boundary

Private Jules task prompts and repository memory remain producer-side controls and are not reconstructed or copied into public files unless the maintainer explicitly publishes them. The repository currently has no public `AGENTS.md`; do not infer one from private automation, prior conversations, or model memory.

Jules-generated research remains repository/historical input. Independent Review may calibrate its interpretation. Independent GPT may recover maintenance state and prepare a bounded control-plane repair. These roles are distinct and do not prove what a private producer consumed.

Before writing:

1. identify the owning file/contract;
2. record the exact fresh `main` revision;
3. inspect relevant open PRs and active maintenance branches;
4. avoid parallel repairs for the same surface/logical period;
5. preserve history, producer identity, and negative/unknown evidence.

No confirmed maintenance defect means `NO_CHANGE_REQUIRED`; do not create activity-only changes.

## Contribution rules

- Keep claims bounded by named evidence, assumptions, implementation status, and validation status.
- Do not promote summaries, analogies, pseudocode, or external results into repository capability without executable repository evidence.
- Preserve stable Claim IDs and bilingual alignment where a change affects the verified core.
- Do not rewrite historical records to make later state appear earlier.
- Keep generated `docs/**` research streams separate from the independently maintained `FOUNDATION/` core unless a separately authorized task explicitly owns a research correction.
- Preserve canonical source identity and five-axis admission semantics.
- Include reproducible validation commands and actual results for executable/schema/validator changes.
- An unrun check is `NOT_EXECUTED`; document inspection is not checker execution.

Keep these distinctions explicit:

```text
research generation != verified-core admission
source registered != claim supported
mapping relevant != implementation present
implementation present != validation complete
review state != maintenance action
validator contract reviewed != validator executed
current path presence != earlier execution
later success != earlier success
correction != history rewrite
```

## Validation

Current structural/documentary verification commands include:

```text
python FOUNDATION/validate.py
python -m unittest FOUNDATION.test_contract -v
python FOUNDATION/validate.py --base-ref origin/main
```

Run only checks supported by the actual environment and changed surface. Record exact commands, revision/environment, exit status, and relevant output. These checks do not establish semantic truth, mathematical correctness, translation quality, or external experimental reproduction.

## AI-assisted work

AI assistance follows `FOUNDATION/PROVENANCE.md`. Generated output is untrusted until checked against repository truth and primary evidence where material. Model agreement is not independent evidence. Do not expose private prompts, hidden reasoning, credentials, or unrelated operator context.

## Pull requests

A maintenance or verified-core repair PR should state:

- exact base `main` revision and current head;
- owning surface / Claim IDs / logical period when applicable;
- overlapping PR/branch check;
- changed files and deliberately unchanged boundaries;
- validation actually executed and results;
- checks not executed;
- history/provenance/bilingual impact;
- security/privacy impact where relevant;
- rollback boundary;
- unresolved evidence or coordination state.

Before delivery, refresh current `main`, recheck live ownership, inspect the aggregate `main...branch` diff, open one Draft PR, and stop for maintainer review unless a different repository-native workflow explicitly applies.

Do not push directly to `main`, force-push history, auto-merge, or claim universal health from a structural check.

The maintainer retains final doctrine, review, and merge authority.
