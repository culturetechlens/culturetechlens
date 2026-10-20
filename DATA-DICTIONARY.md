# Data Dictionary

Field definitions for every dataset in this repository. Counts: `counts.json` (generated, never hand-typed).

## knowledge-graph/entities.csv — one row per entity (stamped slice)
| Field | Meaning |
|---|---|
| `kg_id` | Stable CTL identifier. Prefix encodes type: P Person · W Work · O Outlet · I Institution · PL Place · E Event · T Topic · L List. Never reused. |
| `node_type` | Person / Work / Outlet / Institution / Place / Event / Topic / List. |
| `name` | Canonical display name. |
| `aliases` | Alternate names, spellings, and stage names (list). |
| `props_json` | Property bag (JSON). Always carries `verification` on shipped rows: `{status, source, date, claims}` where status is VERIFIED or STRONG EVIDENCE. Other keys vary by type (e.g. `roles`, `city`, `era`, `year`, `photo`, `known_for`). |
| `created` | Date the record entered the graph. |
| `source` | Intake source label for the record. |

## knowledge-graph/edges.csv — one row per relationship
| Field | Meaning |
|---|---|
| `from_id` / `to_id` | Endpoint entity `kg_id`s. In the shipped slice, both endpoints are stamped entities. |
| `edge_type` | Relationship type from the CTL-KG-001 schema matrix (64 types with allowed endpoint types). |
| `since` / `until` | Optional validity window for the relationship. |
| `evidence` | Evidence grade carried by the edge. |
| `source_ids` | Citation Register entry IDs backing the edge (may be empty on legacy rows). |
| `notes` | Structured notes (JSON) where present. |

## citation-register/entries.json + entries.csv — one record per graded claim
| Field | Meaning |
|---|---|
| `entry_id` / `entry_no` | Register identifier / sequence number. |
| `claim` | The exact claim as graded. |
| `grade` | CTL-MTH-001 grade: VERIFIED FACT / STRONG EVIDENCE / REASONABLE INFERENCE / HYPOTHESIS (plus CTL-INTERNAL). |
| `status_line` | Grade + verification date, as published. |
| `source_line` | The named source and how it was verified (with fetch date). |
| `first_url` | Primary source URL. |
| `lane` | Register lane (topic line) the entry belongs to. |
| `entry_type` | Record type (citation). |
| `wikipedia_sourced` | Whether Wikipedia is the source — CTL policy counts these separately; the current register has 0. |

## reviews/dataset-v5.json — array of categories
Category: `id`, `name`, `tagline`, `items[]`.
Item: `name`, `brand`, `badge` (editorial pick label), `rating` (CTL score), `tagline`, `pros[]`, `cons[]`, `price_usd`, `price_verified` (bool), `price_checked_date`, `link`, `link_label`, `link_verified` (bool), `link_checked_date`, `image`, `image_credit`.

## film-canon/films-110.csv — the adopted canon list
One row per adopted film, CTL-FILM-001–110. List only: the film studies themselves are not published in this repository.

CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence
