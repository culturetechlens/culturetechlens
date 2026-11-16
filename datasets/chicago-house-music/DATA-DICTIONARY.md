CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — Chicago House Music Knowledge Graph (CTL-DS-MUS-000001)
### v1.0 package · 2026-11-16 · Generated from the shipped schemas; conventions stated once, here

Cite as: CultureTechLens, "Data Dictionary — Chicago House Music Knowledge Graph (CTL-DS-MUS-000001)", 2026-11-16.

## Conventions (read first)
- **Blank means not recorded / not asserted — never zero, never "does not exist"** (CTL standard). Coordinates are the standing example: blank by design.
- **Grades** are the CTL ladder: Verified / Supported / Provisional / Disputed / Unresolved (title case in these tables, per the staged build's normalization; the all-caps form is the Index/graph-store style). Grade mapping from source vocabularies was ratified by William Maxey 2026-11-16: `Unknown → Unresolved`; `Needs Review → Provisional` (review_flag kept); compound grades mapped to base grade with the full source text preserved.
- **IDs:** venue location_id (V###), label label_id, artist ctl_ids (semicolon list — an artist can carry IDs from several source systems), claim claim_id, bibliography source_id. ctl_ids / claim source_ids are the join keys to the parent graph and the research packages.
- **Multi-value fields** are semicolon-separated and say so below. Never split them silently in analysis.

## 01_venues (18 rows)
location_id (key) · venue_name · location_type · historical_address (as documented; not a geocode) · latitude / longitude (**blank by design** — no coordinates asserted; see spec Gate G4) · opening_date / closing_date (as documented, may be partial or disputed — the text is the record) · associated_people · source_ids (semicolon list) · grade columns per the staged build (base grade + preserved source text).

## 02_artists (115 rows)
name (key in this table) · ctl_ids (semicolon list of entity IDs across source systems; blank = no ID assigned in source) · subtypes · dates (as documented) · best_grade (the highest grade the person carries in any source brief; **blank = ungraded in source — 73 of 115**, stated openly) · all_grades_seen (semicolon list) · source_briefs (semicolon list of CTL-RB/CTL-DR package IDs).

## 03_labels (16 rows)
label_id (key) · label_name · founded (year as documented) · founders_or_owners_as_documented · documented_first_release · notes · disputes_or_allegations (recorded, not adjudicated) · verification_status · source_ids · ctl_grade. Discogs label IDs, where verified, are named in the spec §2 (Trax 267 · D.J. International 688 · Dance Mania 314 · Jes Say 7406).

## 04_discography (46 rows)
artist · title · expected_year (the first-release year as documented in CTL sources) · discogs_release_id (Discogs identifier; the verification hook) · discogs_title · discogs_year (the year of the Discogs pressing record — **may differ from expected_year; both are printed, never blended**) · discogs_label (**multi-value**: label plus publishers and other credits exactly as Discogs returns them — label counts must use the first value only) · discogs_catno · verification (45 of 46 Discogs-verified; 1 Provisional) · ctl_attestation.

## 05_network_edges (156 rows in v1.0)
subject · relationship · object · grade (the edge's CTL grade) · evidence · provenance (source lane). **v1.0 additions:** subject_name / object_name — display names resolved 2026-11-16 from the flagship graph and this dataset's own tables where the endpoint is an ID; blank where the endpoint's entity file (in the source briefs) was not available to this build — 170 of 380 staged endpoints remain unresolved and are listed as a known gap (spec F-H4). **The staged file's 34 fully blank rows are removed in v1.0** (spec F-H9; logged in CHANGELOG).

## 06_evidence_register (368 rows)
claim_id (key) · claim (the claim text) · ctl_grade · review_flag (kept from source `Needs Review` mappings) · source_ids (semicolon list) · evidence_type · notes · provenance (the lane the claim was compiled from: ZIP intake, one of six brief ledgers, or the staged package). Dedupe pass 2026-11-16: exact-text matching found **zero duplicates**; near-duplicate claims in different wordings remain, by design, until a human review pass — the count 368 is the compiled count and is labeled as such.

## 07_bibliography (50 rows)
source_id (key) · title · publisher_or_site · author · date_as_shown (verbatim) · url · source_type · notes · seed_source.

## 08_photo_manifest (49 rows) — CANDIDATES, NOT CLEARED PHOTOS
file_title · commons_url · direct_url · width · height · license (as recorded from Wikimedia Commons) · artist_credit · search_term (which of the 6 searches found it) · identity_status (**UNVERIFIED on every row** — the PHOTO-001 identity pass has not run; no row in this table is cleared for any use) · source.

## Derived files
- **chicago-house-music.sqlite** — the 8 tables above in one SQLite database (first packaged SQLite export in the CTL catalog), generated from the CSVs; the CSVs govern in any conflict.
- **sample-artists-15.csv** — the 15 Verified-grade artists, the free sample on the foundation plan's first-sale pattern.
- **metadata.json** — the single source from which CITATION.cff, zenodo-metadata.json, and dataset.jsonld are generated.
