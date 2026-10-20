# Knowledge Graph — CTL-KG-001

**Tags:** knowledge-graph, entities, edges, black-imdb, stamped-slice

What's connected: 8 node types (Person, Work, Place, Institution, Outlet, Event, Topic, List), stable CTL IDs. This folder ships the **stamped slice** of CTL-KG-001 as of 2026-10-19: **3,488 entities, 2,162 edges** (`entities.csv`, `edges.csv`; schema in `schema/`, CTL-KG-001 v1). Every entity here carries a verification stamp in its `props_json` (VERIFIED 2,005 / STRONG EVIDENCE 1,483); every edge joins two stamped entities. The full working master — 4,111 entities / 2,527 edges including 623 UNVERIFIED seed-standard rows — stays internal under CTL Phase 0 (snapshot-only, 2026-10-19): CTL does not publish unverified rows, labeled or not. Canonical counts: [`../counts.json`](../counts.json) (generated, never typed).

Historical public snapshot v1.3 (2026-10-16): DOI 10.5281/zenodo.23403147 — superseded; its "2,426 verified" figure is withdrawn by a Retraction-class erratum pending posting on that record.
