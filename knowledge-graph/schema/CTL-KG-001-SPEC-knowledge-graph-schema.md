# CTL-KG-001 — Knowledge Graph Schema Spec (v1, 2026-10-16)

**Purpose.** Define the shared vocabulary — node types, edge types, IDs — for
the CultureTechLens knowledge graph, so today's tables (taxonomy, rolodex,
citation files) accumulate into a graph-loadable dataset instead of needing a
rebuild later.

**Scope rule.** The spec defines *types*, not records. Records migrate from
existing data. A worked example (WKKC) proves the model with real entities.

---

## 1. Node types (8)

| # | Type | ID prefix | Key properties |
|---|------|-----------|----------------|
| 1 | Person | `CTL-P` | name, aliases[], roles[], birth/death dates, bio_source |
| 2 | Outlet | `CTL-O` | name, outlet_type (wire/newspaper/tv/radio/digital/podcast), city, url, verified_contact |
| 3 | Institution | `CTL-I` | name, inst_type (school/museum/church/company/org), city |
| 4 | Work | `CTL-W` | title, work_type (article/book/album/film/episode), pub_date, url, ctl_grade |
| 5 | Topic | `CTL-T` | lane number + slug — **reuses taxonomy IDs** (`CTL-T-08` = lane 08) |
| 6 | Event | `CTL-E` | name, event_type (concert/broadcast/award-ceremony/summit), date, venue |
| 7 | Place | `CTL-PL` | name, place_type (studio/venue/address/neighborhood), address, city, coords |
| 8 | List | `CTL-L` | name, list_type (award/ranking/canon), issuer, year |

People are built as **authority records**: one stable ID per real person,
aliases listed, duplicates merged — the library-science discipline, applied to
the graph.

---

## 2. Edge types (15) — two layers, one graph

### Layer A — Coverage (what CTL has covered; mostly exists today)

| # | Edge | From → To | Properties |
|---|------|-----------|------------|
| 1 | MENTIONS | Work → any node | context snippet |
| 2 | FILED_UNDER | Work → Topic | — |
| 3 | AUTHORED_BY | Work → Person | role |
| 4 | PUBLISHED_IN | Work → Outlet | pub_date |

### Layer B — Influence (who moves the culture; the moat)

| # | Edge | From → To | Properties |
|---|------|-----------|------------|
| 5 | INFLUENCED | Person → Person | notes |
| 6 | MENTORED | Person → Person | period |
| 7 | CITES | Person/Work → Person/Work | context |
| 8 | COVERS | Outlet → Person/Topic | beat |
| 9 | AFFILIATED_WITH | Person → Outlet/Institution | role, period |
| 10 | APPEARS_ON | Person → List | rank, year |
| 11 | HONORED_BY | Person → List/Event | award name, year |
| 12 | PERFORMED_AT | Person → Event | date, role |
| 13 | LOCATED_IN | Person/Outlet/Institution → Place | period |
| 14 | FOUNDED | Person → Outlet/Institution | year |
| 15 | SAMPLED | Work → Work | notes |
| 16 | APPEARED_IN | Person → Work | character, role, year — the cast edge; powers filmographies and co-star ("with who") queries |

### Edge properties (every edge, both layers)

`since`, `until`, `evidence` (VERIFIED FACT / STRONG EVIDENCE / REASONABLE
INFERENCE / HYPOTHESIS — the CTL grading system), `source_ids[]`, `notes`.
Influence claims get the same grading discipline as published articles.

---

## 3. ID conventions

- Format: `CTL-<PREFIX>-<zero-padded sequence>` — e.g. `CTL-P-0001`, `CTL-O-0042`.
- Topics skip the sequence: `CTL-T-08` (taxonomy lane number, permanent).
- IDs are assigned once, never reused, never changed. Corrections add new edges;
  they don't rewrite IDs. Merges keep the older ID and record the alias.

---

## 4. Migration path — what to add to today's tables

No rebuild. Three additions, done incrementally:

1. **taxonomy-index.json / register.csv** — add `kg_id` per category
   (`CTL-T-nn`) and a claim ID (`CTL-C-####`) per citation entry.
2. **rolodex contacts.csv** — add `outlet_id` (`CTL-O-####`) per outlet row;
   add `person_id` when a named contact person is recorded.
3. **Two new load files** (the future graph-DB ingest path — plain CSVs,
   graph-loadable as-is):
   - `entities.csv` — one row per node: `kg_id, node_type, name, aliases, props_json, created, source`
   - `edges.csv` — one row per edge: `from_id, edge_type, to_id, since, until, evidence, source_ids, notes`

Build these two files as a side effect of work already happening: every dossier
written, every CTL25 candidate vetted, every rolodex contact verified adds rows.
No separate "graph project" needed until the queries demand a graph engine.

---

## 5. Worked example — WKKC mini-graph (proves the model with real data)

Nodes:

```
CTL-P-0001  Person       Kevin Brown            (roles: station manager)
CTL-P-0002  Person       Marv Dyson              (roles: DJ, ex-WGCI)
CTL-P-0003  Person       James Kelly            (roles: broadcaster)
CTL-O-0001  Outlet       WKKC 89.3 FM            (radio, Chicago)
CTL-I-0001  Institution  Kennedy-King College   (school, Chicago)
CTL-PL-0001 Place        6301 S. Halsted, Englewood, Chicago (studio/transmitter)
CTL-T-08    Topic        black-media-press        (taxonomy lane 08)
CTL-W-0001  Work         "The WKKC Flywheel"      (article, 2026-10-15)
```

Edges (both layers, shared nodes):

```
(CTL-P-0001)-[:AFFILIATED_WITH {role:"station manager", since:1977, until:1997,
  evidence:"VERIFIED FACT"}]->(CTL-O-0001)
(CTL-P-0002)-[:AFFILIATED_WITH {role:"on-air", since:2004,
  evidence:"STRONG EVIDENCE"}]->(CTL-O-0001)
(CTL-O-0001)-[:LOCATED_IN {evidence:"VERIFIED FACT"}]->(CTL-PL-0001)
(CTL-O-0001)-[:AFFILIATED_WITH {role:"owned/operated by",
  evidence:"VERIFIED FACT"}]->(CTL-I-0001)
(CTL-W-0001)-[:FILED_UNDER]->(CTL-T-08)                     // coverage layer
(CTL-W-0001)-[:MENTIONS]->(CTL-P-0001)                     // coverage layer
(CTL-P-0002)-[:AFFILIATED_WITH {role:"ex-WGCI", evidence:"STRONG EVIDENCE"}]->(CTL-O-0001)
```

Questions this answers that today's tables can't: "who ran WKKC and when?"
(multi-hop: Person → AFFILIATED_WITH → Outlet, filtered by date), "which people
connect WKKC to the broader Black-media lane?" (Person → Outlet → Topic),
"who mentored whom in Chicago Black radio?" (once MENTORED edges accumulate).

---

## 6. Companion file

`CTL-KG-001-schema.json` — machine-readable twin of sections 1–3, plus
`subtype_vocabularies`: the starter enums for `work_type`, `outlet_type`,
`inst_type`, `event_type`, `place_type`, `list_type`. Extend by adding values;
never rename existing ones. Any future graph database (Neo4j or otherwise)
ingests `entities.csv` + `edges.csv` validated against it.

## 7. Domain coverage — what goes where

Every cultural domain fits the 8 node types via subtypes. Nothing needs a new
node type; two of the asked-about items aren't nodes at all:

| Domain | Node type | Subtype / handling |
|---|---|---|
| Songs, albums | Work | `work_type`: song, album |
| Movies, TV shows | Work | `work_type`: film, tv_series, tv_episode |
| Policies, legislation | Work | `work_type`: policy, legislation |
| Events | Event | `event_type`: concert, festival, game, summit… |
| Sports teams / leagues | Institution | `inst_type`: team, league |
| Athletes | Person | roles: athlete |
| Games / matches | Event | `event_type`: game |
| Restaurants | Place | `place_type`: restaurant |
| Dishes, defunct brands, nostalgic artifacts | Work | `work_type`: artifact |
| Dishes | Work | `work_type`: dish |
| Vernacular phrases | Work | `work_type`: phrase — the Black vernacular lexicon, era-tagged |
| Food / nostalgia as subject areas | Topic | taxonomy lanes |
| Stats | — | **properties**, not nodes: on Person (`career_pts`), on PERFORMED_AT edges (`points`, `attendance`), on Works (`chart_peak`) |
| Timeline | — | **a view, not data**: every node/edge with dates renders as a timeline automatically |
