CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — KG333 Black Americans Registry (CTL-DS-KG3-000001)
### v1.0 package · 2026-11-16

## The 20 columns
Rank (1–333, the build's editorial order) · CTL Entity ID (key, CTL-KG100-###) · Name · Category (23 values, kept verbatim incl. build-wave names — spec F-K4) · AEO Primary Question · Trend Signal (free-text editorial signal, not a controlled vocabulary — spec F-K5) · Wikidata QID (or "NONE - KG GAP") · Wikidata URL · Wikipedia Title · Wikipedia URL (blank on 12 rows: the 11 GAPs + 1 QID without an enwiki sitelink) · Wikidata Description (verified) · Verification Status (Verified 2026-11-04 / Verified 2026-11-04 (corrected) / the two GAP statuses) · Verification Note (method + provenance per row, incl. addenda) · Next CTL Action · AEO Direct Answer · AEO Question Cluster (5) (pipe-separated) · AEO Keywords (semicolon list) · CTL Entity Page Slug (culturetechlens.com/knowledge-graph/…; liveness UNVERIFIED — spec F-K2) · AEO Schema (Person or Place + FAQPage + Article) · AEO Target Surface.

## The corrected-verification pattern
22 rows are "Verified (corrected)": the Wikidata search's top hit was a different entity, and the note documents how the right QID was resolved (search alternatives, role search, or the Wikipedia page's pageprops) and re-verified by description + enwiki sitelink. This pattern is required in every future verification pass: a corrected QID without its note does not ship.

## GAP rules
GAP rows (11) carry no fabricated identifiers — the QID cell states the gap. Their Next CTL Action is the dataset's own: publish the CTL entity page first, then propose Wikidata creation with CTL's page and sources as references.
