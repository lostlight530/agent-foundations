# A1 | agent-foundations | October 01–22 provenance and source-custody audit

- Repository: `lostlight530/agent-foundations`
- Exact current main: `22c6712763ff8004f9a91cbb0f78432c0ee61d27`
- Previous A2 relation: `historical-audits/2026-10/2026-10-21-a2-month-relation.md` at blob `342b206d87e5bca16d3e4b4da16735015aa55d25`
- Previous A1 custody record: `historical-audits/2026-10/2026-10-21-a1-source-custody.md`; inherited baseline reports 85 provenance events through the prior cutoff
- Audit window: 2026-10-01 through 2026-10-22 inclusive (N−1 cutoff for 2026-10-23)
- Current source identities compared: 39; unchanged: 35; append-only N−1 revisions: 2; current N-day changes excluded: 2; missing: 0
- Provenance event count: 85 inherited + 4 merged events through Oct22 = 89; Oct23 PR #320 is outside the A1 cutoff and reserved for A2
- This review does not admit a paper into SOURCES, promote Verified Core, or infer implementation/validation from a merged research document

## Per-source identity and temporal decisions

| Exact source path | Previous A2 Git blob | Current main Git blob | Bytes | A1 decision |
|---|---|---|---:|---|
| `FOUNDATION/ARCHITECTURE.md` | `0c39c076da29d169aeaf141b2ebee94f7a836a3b` | `0c39c076da29d169aeaf141b2ebee94f7a836a3b` | 9627 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/COLLABORATION.md` | `94bb8b85557d41124c794bf8c562df2d278593b3` | `94bb8b85557d41124c794bf8c562df2d278593b3` | 9072 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/EVIDENCE.md` | `9c7e0cd274081148b34eb0a6c9d0097cea085ff5` | `9c7e0cd274081148b34eb0a6c9d0097cea085ff5` | 9780 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/INDEX.md` | `289ad219a795090fd5c24e9528f207dcd95a43dc` | `289ad219a795090fd5c24e9528f207dcd95a43dc` | 7142 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/MAINTENANCE.md` | `39740d184fa6170fc7012afa99eacfbf99a9bcd0` | `39740d184fa6170fc7012afa99eacfbf99a9bcd0` | 8453 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/MEMORY.md` | `e5b20a3431ffe2a32a42c9574230fadd965cd9a1` | `e5b20a3431ffe2a32a42c9574230fadd965cd9a1` | 6755 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/PROVENANCE.md` | `40f0cdb0103d2fac8bc5a5ca5742a1a250160b96` | `40f0cdb0103d2fac8bc5a5ca5742a1a250160b96` | 12316 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/REVIEW.md` | `cc72b0951bf2ce23bbf2274ede57a0d1cc83d301` | `cc72b0951bf2ce23bbf2274ede57a0d1cc83d301` | 9841 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/SOURCES.md` | `781bdd4f2d275e667244888e68fac48857a56d37` | `781bdd4f2d275e667244888e68fac48857a56d37` | 49319 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/TOOLS.md` | `7322e8ef3cea7b66499370d89cabb212a27a9b3e` | `7322e8ef3cea7b66499370d89cabb212a27a9b3e` | 7748 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/arxiv_probe.py` | `54bd6091ab22667ecb8a89f49d24e16af0ae3185` | `54bd6091ab22667ecb8a89f49d24e16af0ae3185` | 5609 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/claim.schema.json` | `4578b92834a14b8c8fceb14f0c26b2536410e261` | `4578b92834a14b8c8fceb14f0c26b2536410e261` | 1370 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/independent-gpt/README.md` | `e6377149b7a55c7ef0fa735780251361a07c4df3` | `e6377149b7a55c7ef0fa735780251361a07c4df3` | 6721 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/plans/2026-08-05-readme-narrative-repair.md` | `463509663db0f405bb39550d91f730c6da98963a` | `463509663db0f405bb39550d91f730c6da98963a` | 3412 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/specs/2026-08-05-readme-narrative-repair-design.md` | `b02af44a579b01a3cd5f1aee403b8509eb0d6dab` | `b02af44a579b01a3cd5f1aee403b8509eb0d6dab` | 2599 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/test_contract.py` | `42c9211626fe315ce28304cefb339754d45d77ee` | `42c9211626fe315ce28304cefb339754d45d77ee` | 6649 | NO_FOLLOW_UP / PRESERVE |
| `FOUNDATION/validate.py` | `8ce5d29cfdd31c9d6b33edbc0b94d44c53c98cbb` | `8ce5d29cfdd31c9d6b33edbc0b94d44c53c98cbb` | 9736 | NO_FOLLOW_UP / PRESERVE |
| `docs/en/Architecture_Principles.md` | `90503b04e766a01602d4fe4f43f00f0589cfe5e0` | `90503b04e766a01602d4fe4f43f00f0589cfe5e0` | 123815 | NO_FOLLOW_UP / PRESERVE |
| `docs/en/Collaboration_System.md` | `3c6d02ecc2b30e79c0901dc96db3e31712ccb588` | `3c6d02ecc2b30e79c0901dc96db3e31712ccb588` | 258478 | NO_FOLLOW_UP / PRESERVE |
| `docs/en/Memory_System.md` | `dd31d620b42d574329002808a9d1b6253c6b03ba` | `41aad4fb2c483d48da348ebb00de939a402d307c` | 95215 | PR320_OCT23 / OUT_OF_CUTOFF_RESERVED_FOR_A2 |
| `docs/en/Monthly_Blueprint_Current.md` | `461dfeb087b784de0ff40cae12ecdcd4c7f84b22` | `461dfeb087b784de0ff40cae12ecdcd4c7f84b22` | 5778 | NO_FOLLOW_UP / PRESERVE |
| `docs/en/README.md` | `33ba8878127c3da5f3a59ffc444adb54249f13ec` | `33ba8878127c3da5f3a59ffc444adb54249f13ec` | 3365 | NO_FOLLOW_UP / PRESERVE |
| `docs/en/TAPE_2026-09-10_CORRECTION.md` | `676758aad5b4ed0445aa5d70f3406828c2cc639b` | `676758aad5b4ed0445aa5d70f3406828c2cc639b` | 3921 | NO_FOLLOW_UP / PRESERVE |
| `docs/en/Tool_System.md` | `e3ee65adb601a056df6fd3e4f2233b90773b0795` | `491efccd31600daca90a608b296ac049b9337692` | 58724 | APPEND_ONLY_PR319_OCT22 / N_MINUS_1_INPUT |
| `docs/monthly/2026-06-strategic-blueprint.md` | `bbe44ca35ad6515713dc967aafb4466f0fa0202f` | `bbe44ca35ad6515713dc967aafb4466f0fa0202f` | 2960 | NO_FOLLOW_UP / PRESERVE |
| `docs/monthly/2026-07-strategic-blueprint.md` | `2018c8b59f438bb107116b09a68811dc36e2e30f` | `2018c8b59f438bb107116b09a68811dc36e2e30f` | 8271 | NO_FOLLOW_UP / PRESERVE |
| `docs/monthly/2026-08-strategic-blueprint.md` | `13b4bb6081b9c39cb53ea6a55dd6a3417af2819d` | `13b4bb6081b9c39cb53ea6a55dd6a3417af2819d` | 2618 | NO_FOLLOW_UP / PRESERVE |
| `docs/monthly/2026-08-through-23-strategic-blueprint.md` | `8198e57ff8662ded800c56ebc90b8eb86020c87d` | `8198e57ff8662ded800c56ebc90b8eb86020c87d` | 5415 | NO_FOLLOW_UP / PRESERVE |
| `docs/monthly/2026-08-through-27-strategic-blueprint.md` | `ba10249678baface4594a18a32e467da065b6ccb` | `ba10249678baface4594a18a32e467da065b6ccb` | 4374 | NO_FOLLOW_UP / PRESERVE |
| `docs/monthly/2026-08-through-30-strategic-blueprint.md` | `42dc9f7d21ac42cfcb848a959b95169fdbb91476` | `42dc9f7d21ac42cfcb848a959b95169fdbb91476` | 2756 | NO_FOLLOW_UP / PRESERVE |
| `docs/monthly/2026-09-strategic-blueprint.md` | `09bcc820bec30df2d34f4a2b6bde4b1ed98d1578` | `09bcc820bec30df2d34f4a2b6bde4b1ed98d1578` | 7601 | NO_FOLLOW_UP / PRESERVE |
| `docs/monthly/2026-10-strategic-blueprint.md` | `44baa112ad4ea91cd81bf8841ba3624fabd3988a` | `44baa112ad4ea91cd81bf8841ba3624fabd3988a` | 487639 | NO_FOLLOW_UP / PRESERVE |
| `docs/zh/Architecture_Principles.md` | `7b148c9f16dc40cf3b5907c12d6046df30139436` | `7b148c9f16dc40cf3b5907c12d6046df30139436` | 116574 | NO_FOLLOW_UP / PRESERVE |
| `docs/zh/Collaboration_System.md` | `ec13e481cb695c8e9f55efd00c1d749863d9a029` | `ec13e481cb695c8e9f55efd00c1d749863d9a029` | 231973 | NO_FOLLOW_UP / PRESERVE |
| `docs/zh/Memory_System.md` | `1338fbb17e671d6804805bb78a9348af3201cd26` | `7986cdb2678fa825a830c87f15663d3f9b9e7ca5` | 89972 | PR320_OCT23 / OUT_OF_CUTOFF_RESERVED_FOR_A2 |
| `docs/zh/Monthly_Blueprint_Current.md` | `ea8717056f9fff978df402e2933644d1cc662119` | `ea8717056f9fff978df402e2933644d1cc662119` | 5390 | NO_FOLLOW_UP / PRESERVE |
| `docs/zh/README.md` | `c7516f8d6dfd186ec4577552fca2ea319c9ea49f` | `c7516f8d6dfd186ec4577552fca2ea319c9ea49f` | 3098 | NO_FOLLOW_UP / PRESERVE |
| `docs/zh/TAPE_2026-09-10_CORRECTION.md` | `6c6158bae3921373623cd46438f7abffee4874db` | `6c6158bae3921373623cd46438f7abffee4874db` | 3504 | NO_FOLLOW_UP / PRESERVE |
| `docs/zh/Tool_System.md` | `600aea40e9d4e0d14b10a394489354a65f2738da` | `010e3cc8befee32df29c03fa5c6cf4147437db14` | 54524 | APPEND_ONLY_PR319_OCT22 / N_MINUS_1_INPUT |

## Newly observed merged delivery events through the N−1 cutoff

| PR | Merged at | Title | Merge commit | Event class |
|---:|---|---|---|---|
| #316 | 2026-10-21T06:33:13Z | `research(daily): 2026-10-21 GPT Tool System causal-provenance study (EN/ZH)` | `2eda4d8a233bce1891e27ee60630d31d25004217` | NATIVE_DAILY / Tool_System append-only research |
| #317 | 2026-10-21T11:27:23Z | `A1 agent-foundations: 85 provenance events and 39 current source identities` | `32186a6219d4f7fe2c7bbb86d9458ad8738e1304` | A1_MAINTENANCE / source custody checkpoint |
| #318 | 2026-10-21T11:37:09Z | `A2 agent-foundations: Oct01–21 complete current-month native evidence relation` | `a6f622c555afcca6ff9b10247ab0958bb391c532` | A2_MAINTENANCE / current relation checkpoint |
| #319 | 2026-10-22T04:47:53Z | `Foundations GPT Native Daily 2026-10-22: PROVISO tool commitment (EN/ZH)` | `32e3300de5163ae2b7fe2aa637f14b958cd6aa02` | NATIVE_DAILY / append-only Tool_System research |

## Current N-day source changes intentionally excluded from A1

| Source path | Previous A2 Git blob | Current main Git blob | Bytes | A1 disposition |
|---|---|---|---:|---|
| `docs/en/Memory_System.md` | `dd31d620b42d574329002808a9d1b6253c6b03ba` | `41aad4fb2c483d48da348ebb00de939a402d307c` | 95215 | PR #320 / N_DAY_INPUT_EXCLUDED_FROM_A1 / ADMIT_ONLY_AFTER_FRESH_MAIN_IN_A2 |
| `docs/zh/Memory_System.md` | `1338fbb17e671d6804805bb78a9348af3201cd26` | `7986cdb2678fa825a830c87f15663d3f9b9e7ca5` | 89972 | PR #320 / N_DAY_INPUT_EXCLUDED_FROM_A1 / ADMIT_ONLY_AFTER_FRESH_MAIN_IN_A2 |

## Historical status and evidence boundaries

- PR #319 is a 2026-10-22 append-only bilingual PROVISO study in `docs/en/Tool_System.md` and `docs/zh/Tool_System.md`; the new research block does not replace prior history
- PR #320 is a 2026-10-23 append-only bilingual Memory System study of arXiv:2610.29869v1; it is deliberately excluded from the N−1 decision set and must enter the next A2 relation only
- PR #320 does not create an Sxx registry identity, Verified Core admission, implementation, local validation, paper replication or runtime test
- The 2026-10-22 and 2026-10-23 source identity changes are current document evolution, not proof of new independent source lineage
- No original daily research body, `FOUNDATION/SOURCES.md`, claim schema, verified-core state, implementation, test or historical audit was modified
- Full `FOUNDATION/validate.py`, runtime replay, paper experimental reproduction and current external source recertification: NOT_EXECUTED by this audit
- Files changed by this proposal: this dated A1 source-custody record only
- Next gate: merge all ten A1 deliveries, reread current main, then create the A2 month-wide relation through 2026-10-23

## Result

`A1_SOURCE_CUSTODY / OCT22_APPEND_ONLY_RETAINED / OCT23_MEMORY_INPUT_RESERVED_FOR_A2 / N_MINUS_1_CUTOFF_2026-10-22`

