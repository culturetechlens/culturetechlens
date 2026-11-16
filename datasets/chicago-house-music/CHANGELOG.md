# CHANGELOG — Chicago House Music Knowledge Graph (CTL-DS-MUS-000001)
No silent edits: every change is dated and states what changed.

## v1.0 package (2026-11-16, assembled by Dion under the dataset spec)
- Assembled from the v0.1 staged build (2026-11-14) after William Maxey's rulings of 2026-11-16: dataset ID CTL-DS-MUS-000001 confirmed; staged grade mapping RATIFIED (Unknown→Unresolved; Needs Review→Provisional with flag kept; compound grades base-mapped with source text preserved; nothing upgraded).
- **Correction — edge count:** the staged network_edges file's 190 rows include **34 fully blank rows**. v1.0 removes them: **156 edges**. Dataset totals move from 852 staged rows to **818 data rows**. The staged original is untouched.
- Name resolution added (subject_name/object_name): 210 of 380 staged endpoints now carry display names (flagship graph + this dataset's own tables). 170 remain unresolved — their entity files live in the source brief packages.
- Evidence dedupe pass: exact-text matching across the 368 claims found **zero duplicates**; no rows merged. Near-duplicates in different wordings are a flagged human-review item, not a script task.
- Added: DATA-DICTIONARY.md, JSON exports of all 8 tables, SQLite export (first in the CTL catalog), free sample (15 Verified artists), 7 charts + ultra-wide board, AEO cited questions (50, Verified claims only) + generated FAQ JSON-LD, llms.txt, CITATION.cff / zenodo-metadata.json / dataset.jsonld from one metadata.json.
- ID-scheme note: the Research Registry's Type 06 scheme renders this ID CTL-RDS-MUS-000001; William's ruled form CTL-DS-MUS-000001 stands; the conflict is recorded in both registries, unresolved.
- NOT in v1.0: Zenodo deposit and DOI (founder token sitting), merge into the production graph (separate GOV-006 decision), any photo use (PHOTO-001 pass not run), venue coordinates or any map (blank by design).

## v0.1 STAGED (2026-11-14)
- Specialist dataset built: 8 tables, 852 rows as staged (incl. the 34 blank edge rows corrected above). Staged only — not merged, not published, no DOI. Build scripts and sha256 MANIFEST in the staged package.
