CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence
Cite as: CultureTechLens, "Merge Log — Sports Firsts Staged Packet (CTL Sports Firsts Package)," November 12, 2026.
Source: CultureTechLens

# Merge Log — Sports Firsts Staged Packet → Canonical Graph
**MERGE COMPLETED November 12, 2026**, on William Maxey's directive in this chat ("Merge the 9 staged records into the graph"). The 9 PROPOSED records staged in `03-staged-graph-packet.json` (CTL-E-7407–CTL-E-7415) were merged into the canonical graph (`~/workspace/culturetechlens/knowledge-graph/entities.json` + `relationships.json`) with their staged IDs adopted as canonical, per past CTL merge practice. Validation passed clean. Nothing was published or deployed — the records go public at the next approved site package.

## Backups (taken before any write)
- `knowledge-graph/_archive/entities-backup-2026-11-12-pre-sports-firsts-merge.json` — SHA-256 `49340ba5167ddd54312f8dbd3e5f4361c60f65dd8b746476ca747a50bbfb2151`
- `knowledge-graph/_archive/relationships-backup-2026-11-12-pre-sports-firsts-merge.json` — SHA-256 `cc0998b800f1b859363b59169057393613c6f2506a894aa3d33e12f08f54040c`
- Concurrency guard: the canonical files' SHA-256s were recorded at merge start (entities `49340ba5…`, relationships `cc0998b8…`, mtime 2026-11-05) and re-verified identical immediately before writing — no parallel-session change was overwritten.

## Pre-merge assertions — all passed
- **(a) ID collision:** CTL-E-7407–7415 absent from the canonical graph; the highest canonical ID before merge was CTL-E-7406, so the staged run is exactly sequential.
- **(b) Duplicate sweep:** all 9 names and aliases checked exactly, plus fuzzy token passes (Shippen, Poage, Haskins, Shady, Rajo, Gatson, Norfleet, Hubbard, DeHart, Texas Western, Miners, Baxter Taylor) — no existing record for any of the 9 under any spelling (substring hits were unrelated people: Freddie Hubbard, Slim Shady alias on Eminem, other Ashleys/Maurices).
- **(c) Source shape:** all 18 staged sources carry the full six-field form (accessed · citation · name · primary · supports · url) — no enrichment needed.
- **(d) Project IDs:** all 9 records carry **PPL-001**, which IS a registered schema project — no correction required. (Logged openly: the two Organization records, Shady Rest and Texas Western, also carry PPL-001, following the November sports-tranche convention for this cohort; the Kirkland-precedent correction applies only to unregistered project IDs, and none was present. Registering or retagging projects is a separate step, not done here.)
- **(e) Relationships:** the 1 JSON edge passes the schema type matrix (Shippen, Person — affiliated_with → Shady Rest, Organization). The 3 edges proposed in `03-staged-graph-packet.md` only were adjudicated and **all 3 dropped** (below).

## Corrections made at merge (all logged, none silent)
1. **Record notes updated (all 9):** each staged record's notes opened with "PROPOSED staged record … this record is NOT merged into the canonical graph. Do not cite the ID as a graph ID until a merge mints it." That statement became false at merge, so the preamble was replaced with "Merged 2026-11-12 from the CTL Sports Firsts staged packet; the proposed staged ID was adopted as the canonical ID at merge." All substantive conflict notes after the preamble (Shippen birth-day split, Taylor birth year and medley-relay correction, Shady Rest purchase-vs-lease, Rajo Jack dating, Ashley title-year variance, Norfleet Disputed grade) are preserved verbatim.
2. **Edge converted to canonical form:** the Shippen → Shady Rest edge carried a non-canonical `note` key (not among the schema's relationship fields); it was stripped so the merged edge carries exactly the canonical six fields (from · to · type · evidence · source · verification). Its provenance wording is preserved in this log.
3. **Verification levels unchanged:** Rajo Jack stays Provisional; Tia Norfleet stays schema-Provisional with her governing GOV-004 grade **Disputed** carried in her record's notes — not upgraded.

## Edges proposed in the .md — adjudicated, all dropped
- **Texas Western → Don Haskins (head_coach_of):** type is matrix-valid (Person → Organization), but Don Haskins has NO record in the canonical graph — the endpoint does not exist after this merge. Dropped; the coaching fact remains in the team's description.
- **George Poage → Chicago (associated_with):** associated_with is Person → Neighborhood only, and no canonical Neighborhood endpoint for Poage's Chicago residence is asserted. Dropped; the fact remains in his description.
- **John Baxter Taylor Jr. → William DeHart Hubbard (related_to):** matrix-valid Person → Person and both endpoints now exist, but the packet documents this link as editorial ("successor firsts"), carrying no evidence or source — canonical relationships require both. Dropped; may be re-proposed with evidence in a later packet.

## Counts (recomputed from the canonical files, before and after)
| Ledger | Before | After | Delta |
|---|---|---|---|
| Entities | 4,796 | 4,805 | **+9** (CTL-E-7407–7415) |
| Relationships | 5,979 | 5,980 | **+1** (Shippen affiliated_with Shady Rest) |
| Entity source references | 13,676 | 13,694 | **+18** (2 per merged record) |

Baseline check before merge: validate.py on the untouched canonical files = 0 errors, 0 warnings.
**Final validation: `validate.py` on the merged canonical files — 0 errors, 0 warnings, VALIDATION PASSED.** No rollback was needed. All 9 IDs were re-read from the merged entities.json and confirmed present with their staged verification levels.

## Final canonical file hashes (post-merge)
- entities.json — SHA-256 `6ee71a199901ad073273599af7b164138f7d6edf1a05f6d567ca814706d11e1c`
- relationships.json — SHA-256 `0144ce7b522d3f738a1f589f7e5c14a58c75a02be0dead8c600ebe98429fe9b7`

## Not done (separate lanes, by design)
- **counts.json NOT regenerated:** it lives in `website/` and is generated from the website's vendored master CSVs (website lane, generated-only per the counts pipeline); the graph merge does not feed it directly. Site figures update at the next approved site package.
- No site publish/deploy, no AAES roster edits, no other graph changes, no sends.
