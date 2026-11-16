# CULTURETECHLENS
## "Culture, Clearly Seen." · Black Cultural Intelligence

# Entry Schema — Afro American Encyclopedia of Sports (CTL-DATA-SPORT-001)

Every entry in the dataset carries these fields. The schema is the contract the blueprint's roster — when it lands — gets audited against.

| Field | Rule |
|---|---|
| `entry_id` | CTL-AAES-NNNN, sequential, never reused |
| `name` | The subject's name as carried by its best source |
| `kind` | person · team · subject (moment/work/institution entries ride as subject until the taxonomy ruling) |
| `sport` | The sport, from a controlled list. **The controlled list is NOT yet ruled**: the blueprint claims 36; the head record evidences baseball, basketball, football today. The list gets set from the blueprint at pillage, or by founder ruling — never padded from memory |
| `context` | League/era framing the source itself gives (e.g. "Baseball — Negro leagues") |
| `graph_union_id` | Combined Graph union ID where the subject already lives in the graph — the join to evidence, relationships, photos |
| `sources` | Every source the seed row came from, named (graph edge, packet, list, dossier) |
| `annotation` | The current best short text, where one exists from a VERIFIED-claim source |
| `status` | The ladder below |
| `notes` | Relationships and facts the seed source states (e.g. played_for targets) |

## Status ladder

1. **roster** — name + provenance only. An entry slot, not an entry.
2. **stub** — annotation-grade text exists from an evidence-graded source (today: the 64 Listal annotations, drawn from VERIFIED dossier claims).
3. **full** — a complete encyclopedia entry: biography/record narrative, evidence-graded claims with citations, photo status from the Photo Rights Log, graph relationships stated. *Zero entries are at full today — stated plainly.*
4. **published** — full + shipped (site/Zenodo) under a founder go.

## Counting doctrine (standing)

The encyclopedia's public count is the number of entries **in this dataset, by status** — never the blueprint's claimed 1,212 until the blueprint itself is in hand and its roster counted. If the audited blueprint roster differs from 1,212, the audited number governs and the difference is reported, not smoothed over.

Cite as: CultureTechLens, *Afro American Encyclopedia of Sports — Dataset Foundation (CTL-DATA-SPORT-001)*, 2026-10-24. Source: CultureTechLens
