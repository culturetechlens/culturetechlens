# CULTURETECHLENS
## "Culture, Clearly Seen." · Black Cultural Intelligence

# Roster v1 — Head Build Note (CTL-DATA-SPORT-001)

**Date:** 2026-10-24 · **Blueprint:** CTL-SPT-ENC v1.0, adopted at the head by William's ruling, 2026-10-24 · **Build home:** this package (local + Drive folder 1Sy3eDHuC7GLa2MC_nCsXJaUw5XBqJF1J)

## What Roster v1 is

Roster v1 folds the verified seed into the adopted blueprint taxonomy and adds the blueprint's own named anchors where they were not already in the seed. It is a roster — names, IDs, sport placement, provenance, and status — not written encyclopedia entries. Full-entry writing is a later phase.

## Counts (counted from the built files, 2026-10-24)

- **244 roster rows total** — 242 assigned to a sport + 2 in the explicit unassigned bucket (below)
- **153 seed entries folded** — 151 sport-assigned, 2 unassigned; every seed ID remapped, none silently renumbered (see `11-id-mapping-aaes-to-spe.csv`, 153 mapping rows)
- **91 blueprint anchors added** — from 96 anchor names parsed from CTL-SPT-ENC §7; 5 folded into seed entries already present by name: Jackie Robinson, Satchel Paige, Fritz Pollard, Doug Williams, Jack Johnson
- **Status carried from the seed:** 64 stub · 180 roster (91 anchors + 89 seed roster-level). **0 full, 0 published** — stated plainly
- **Kinds:** athlete 154 · subject 51 (all carrying a taxonomy-review flag) · team 29 · institution 5 · coach 4 · league 1
- **Gap to target:** 242 assigned against the 1,212 blueprint target = **970 remaining** (see `12-gap-table-v1.csv`, the control sheet; regenerated after every wave)

## How sport placement was decided

Only the row's own data was used, in this order: (1) the seed `context` field (64 Listal rows: Baseball, Basketball, Football); (2) the `played_for` team in the seed notes, mapped by that team's own sport; (3) a team's own franchise identity (27 seed teams); (4) the staged-packet lane for packet-only rows (Jack Johnson → Boxing; Doc Rivers, Bobby Simmons → Basketball). Discipline is carried from the seed context where present, otherwise from the assigning team / blueprint anchor line.

## Unassigned bucket (explicit, never guessed)

| Entry | Reason |
|---|---|
| Sam "Sad Sam" Jones (CTL-SPE-0243) | The seed packet record itself is an unresolved conflation — basketball Sam Jones vs. baseball Samuel Pond Jones — flagged HOLD-for-merge-review on 2026-10-16. A sport cannot be assigned from the row's own data without guessing. |
| Simeon Career Academy (CTL-SPE-0244) | School / multi-sport institution from the Sports Core 10 packet; the seed row carries no single-sport lane. Taxonomy review required. |

These two keep permanent CTL-SPE IDs and count in the 244, but they do **not** count toward any sport's rostered total in the gap table.

## Flags carried, not propagated

- **Giannis Antetokounmpo** — the seed's `played_for Miami Heat` edge is noisy/unverified. His roster placement is Basketball by team-edge type only; the suspect edge is flagged in his row's notes, not asserted as fact. Entry-level verification happens at the full-entry stage.
- **Bo Jackson** — the seed supports Baseball only (Chicago White Sox). His dual-sport career is noted in his row; no Football placement was invented from outside the seed data.
- **Jim Brown** — added as a Lacrosse anchor per the blueprint §7; his Football significance is noted as a cross-sport flag for full-entry verification.
- Placement by team edge is a starting placement, not a verified fact, for all graph-derived rows — the same caution applies dataset-wide.

## ID rule applied

Sports in CTL-SPT order (01→36); within a sport, seed entries first in old-ID (CTL-AAES) order, then blueprint anchors not already present. IDs CTL-SPE-0001…CTL-SPE-0244 are permanent and never reused. The mapping file is the record of the remap.

## Next

Wave 1 fill: Baseball (75 remaining), Basketball (50), Football (67), Boxing (86) — candidate rows audited at the head before any merge, §2.7 two-source discipline on every "first" claim. Gap table regenerates after the wave.

Cite as: CultureTechLens, *Afro American Encyclopedia of Sports — Roster v1 Note (CTL-DATA-SPORT-001)*, 2026-10-24.
Source: CultureTechLens
