# CHANGELOG — Cited Photo Archive Registry (CTL-DS-PHO-000001)
No silent edits: every change is dated and states what changed.

## v1.0 package (2026-11-16, assembled by Dion under the dataset spec)
- Dataset ID CTL-DS-PHO-000001 ruled by William Maxey (2026-11-16); registered the same day. Boundary ruled: this registry is never merged with the internal Photo Rights Log v4.
- Linkage pass (spec §4, exact unique name match only, logged in linkage-log.md): +5 KG300 entity IDs filled — 27 of 232 rows linked. The pass deliberately stops there; the remaining rows need human matching against card subjects, and the count is printed as-is.
- Added: DATA-DICTIONARY.md, JSON + SQLite exports, FAQ JSON-LD from the 232 card Q&As (232), charts + ultra-wide board, llms.txt, sample-25, CITATION.cff / zenodo-metadata.json from one metadata.json, MANIFEST. The as-extracted CSV ships unmodified alongside the linked CSV.
- NOT in v1.0: Zenodo deposit/DOI (founder sitting), page-slug minting (site lane), Medusa keyword registration (administration), any photo file hosting change.

## Extraction (2026-11-04)
- 232 evidence cards extracted verbatim from culturetechlens.com/photos/ in 4 segments and reconciled into the registry (CSV + JSON-LD + XLSX in Drive folder 01).
