CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — Chicago Black Culture (CTL-DS-CHI-000001)
### v1.0 merge package · 2026-11-16

## The merged table (26 columns)
ctl_cbc_id (key; Build 02's IDs kept, new IDs CTL-CBC-0125…0199 assigned to Build-01-only places — MERGE-LOG) · name · category (Church/Club/Venue/Theater/Bank) · subcategory · kind · graph_type · description (Build 01) · aliases · address (partial, unverified for publication) · neighborhood (thin coverage — spec F-C2) · era (free text) · years_active · status_today (October 2026 free-text snapshot — F-C3) · **evidence_grade** (mapped, below) · grade_source_text (verbatim grades from both builds) · grade_conflict (yes on 8 rows) · legacy_grade_mapped · in_master · in_build · source_ledger · relationships_count · conflicts_count (27 rows ≥1 in Build 01) · photo_flag · union_id · graph_id · provenance (both / build01_only / build02_only).

## Grade mapping (spec M4)
VERIFIED/Verified → **Verified** · STRONG EVIDENCE → **Supported** (legacy vocabulary, flagged) · Provisional → **Provisional** · no grade → contributes nothing. Final grade = the LOWEST mapped grade across the row's builds. Result: Verified 161 · Supported 8 · Provisional 29 · Unresolved 1. Nothing was upgraded; grade_source_text preserves every original string.

## The FAQ file is generated
aeo-faq-GENERATED.jsonld was composed mechanically from row fields on 2026-11-16 (spec §4). It contains no fact that is not in its row. It is a discovery aid, not source data.

## No map
No coordinates ship and no GeoJSON exists for this dataset (spec M5): addresses are partial and unverified.
