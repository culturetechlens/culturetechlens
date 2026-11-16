CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — Afro American Encyclopedia of Sports (CTL-DS-SPO-000001)
### v1.0 package · 2026-11-16 · Canonical file: data/sports-encyclopedia-roster.csv (532 rows × 13 columns)

## The 13 columns (roster v2 schema, carried verbatim)
- **entry_id** — CTL-SPE-NNNN, permanent, never reused. CTL-SPE-0033 is retired (folded into CTL-SPE-0001 in roster v2) and appears in no current roster. Scour adds run CTL-SPE-0524–0533.
- **sport_id** — CTL-SPT-01…36 from the adopted blueprint (CTL-SPT-ENC v1.0); blank on the 2 unassigned rows, whose sport field reads UNASSIGNED.
- **sport** — the blueprint sport name; UNASSIGNED for CTL-SPE-0243/0244 (reasons in their notes).
- **name** — the subject's name as carried by its best source.
- **kind** — athlete · team · coach · institution · league · subject (post-scour: athlete 389 · subject 66 · team 41 · coach 26 · institution 9 · league 1). The seed's person/school kinds were remapped at roster v1 (person → athlete/subject by placement; school → institution); the seed ships unmodified in sources/ with its original kinds.
- **discipline** — the sub-discipline or circuit the source states (e.g. MLB, PGA, Sprints, NASCAR). Blank where no source in hand states one (2 inherited rows + Coco Gauff's scour add) — blank means unstated, never zero.
- **graph_union_id** — the subject's Knowledge Graph join key where one is carried (union U- IDs and build CTL-E- IDs both appear, as the source rosters carried them; 99 filled pre-scour, +7 scour adds carrying their merged CTL-E-7407–7415 IDs).
- **sources** — every source the row came from, named (graph edges, packets, lists, halls of fame, references). Scour adds name their scour source first-class (CTL Sports Firsts Register 2026-11-12; KG333/AEO-500 registries).
- **annotation** — annotation-grade text where one exists from an evidence-graded source (the stub rows). Blank on roster-status rows.
- **status** — the dataset's own ladder, verbatim (below).
- **notes** — relationships, flags, folds, holds and provenance the source states. Scour adds open with "SCOUR ADD (Clone #9, 2026-11-16)" and state their dedupe and any carried dispute.
- **chicago_connection** — Team · Birthplace · School · None documented. Coded conservatively (v2 merge method: from the row's own notes/franchise identity only); "None documented" means no connection is documented in the row's data — it does not assert no connection exists.
- **firsts_flag** — the row's "first" claim in its exact sourced form with its sources, under blueprint §2.7 (a first publishes only with two independent sources, at least one primary/institutional). 46 inherited flags (38 two-sourced · 8 verification-pending) + 7 scour flags. One scour flag reads DISPUTED — do not publish as a first.

## Status ladder — the dataset's vocabulary (verbatim, entry schema 2026-10-24)
1. **roster** — name + provenance only. An entry slot, not an entry. (463 post-scour)
2. **stub** — annotation-grade text exists from an evidence-graded source. (69)
3. **full** — a complete encyclopedia entry. **0 — stated plainly.**
4. **published** — full + shipped under a founder go. **0.**

No CTL claim grades are applied to roster rows. Where a scour source graded a *claim* (the Sports Firsts register's GOV-004 grades), the grade lives in the row's notes/firsts_flag in its original words — Verified in exact form · Provisional (Rajo Jack) · Disputed (Tia Norfleet) — and is never converted into a status.

## Companion files
- **GAP-TABLE-POST-SCOUR.csv** — the control sheet regenerated after the scour: per sport, target (blueprint), rostered in v2, rostered post-scour, remaining. Totals: target 1,212 · v2 520 assigned · post-scour 530 assigned · remaining 682. (The 2 unassigned rows count in the 532 total but toward no sport.)
- **annex/held-and-manifest-annex.csv** (54 rows: name · kind · sport_or_blocker · source · disposition) — verified sports material held off the roster: 5 held finds (sports at target; chess taxonomy gap) + 49 sports-photo-addendum subjects (photo-manifest references only; rights live in the addendum's own rows in sources/, per row).
- **sources/** — every predecessor file unmodified, including roster-v2-pre-scour.csv (the 522-row canonical file this package's canonical file succeeds, with the 10 scour adds appended and flagged in their notes — the succession is stated, never silent).
