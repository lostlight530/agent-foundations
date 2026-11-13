# Agent Foundations Pages — evidence-reader maintenance

The deployed static source is root `index.html`; the Pages workflow `.github/workflows/deploy-pages.yml` copies that page and `docs/` into its public artifact. The research source of truth is the versioned `FOUNDATION/` **directory**, not the HTML copy

## Current vs historical

- **Current**: evidence-first bilingual reading interface; interpret research claims through the index, evidence vocabulary, source register, provenance and independently recorded implementation/validation axes
- **Archived versions**: earlier root homepage at main `15a61191ac7166762493b13a0ea25cc9bb7cf999`, and the frontend before this repair at `41a1b029f57fc0cbb5dfed3e2ce33ff6b16f1f95`, both recoverable through Git history
- The four-domain research history, dated timeline and canonical `FOUNDATION/**` research files remain separate from current verified-document claims

No dynamic Agent runtime is established by publication; passing documentary schema checks does not prove live autonomous execution

## Maintainable information architecture

Keep evidence reference links individually labeled: `INDEX.md` is the entry and claim index, `EVIDENCE.md` documents evidence axes, `SOURCES.md` records sources, `PROVENANCE.md` tracks origin, and the repository link is the browse entry

Keep links high-contrast and keyboard focusable on dark backgrounds, make the long research matrix mobile scrollable, preserve language matching and avoid Chinese `U+3002` in visible homepage copy. Do not change canonical research values or delete historical records in a UI cleanup

Prior UI baseline: [PR #419](https://github.com/lostlight530/agent-foundations/pull/419)
