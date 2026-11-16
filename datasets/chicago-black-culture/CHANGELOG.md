# CHANGELOG — Chicago Black Culture (CTL-DS-CHI-000001)
No silent edits: every change is dated and states what changed.

## v1.0 merge package (2026-11-16, assembled by Dion under the dataset spec)
- Dataset ID CTL-DS-CHI-000001 ruled by William Maxey (2026-11-16), legacy alias CTL-DATA-CHI-001 recorded; Data Register entry #13 AMENDED (not a new line); Research Registry Type 06 entry added.
- THE MERGE: Build 01 (183 rows, union file) + Build 02 (124 rows, v0 seed) → 199 rows; 108 joined on exact normalized name; 75 new CTL-CBC IDs assigned (0125–0199); 7 near-match pairs deliberately NOT merged (MERGE-LOG).
- GRADES: legacy vocabulary base-mapped (STRONG EVIDENCE → Supported on 8 rows); 8 cross-build grade conflicts resolved lowest-wins; source strings preserved in grade_source_text. Final: Verified 161 · Supported 8 · Provisional 29 · Unresolved 1.
- Added: merged CSV/JSON/SQLite, sources/ (both builds unmodified), MERGE-LOG.md, DATA-DICTIONARY.md, generated FAQ JSON-LD (199, labeled), charts + board, llms.txt, sample-30, metadata trio, MANIFEST.
- NOT in v1.0: Zenodo deposit/DOI (founder sitting), resolution of the 7 near-match pairs, neighborhood completion, coordinates (excluded by ruling M5).

## Build history (October 2026)
- 2026-10-24: dataset folder established as CTL-DATA-CHI-001 with schema, data dictionary, coverage-and-gaps notes and dataset cards. Build 01 (union of master graph + build slice, 183 rows) and Build 02 (v0 seed, 124 rows) coexisted unreconciled until this merge.
