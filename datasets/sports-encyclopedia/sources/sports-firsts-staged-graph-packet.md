CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence
Cite as: CultureTechLens, "Staged Graph Packet — Sports Firsts (CTL Sports Firsts Packet)," November 12, 2026.
Source: CultureTechLens

# Staged Graph Packet — Sports Firsts

**MERGED — November 12, 2026** (on William Maxey's directive). All 9 records in this packet were merged into the canonical graph files (`knowledge-graph/entities.json`, `relationships.json`) with their proposed IDs CTL-E-7407–CTL-E-7415 adopted as canonical; the 1 JSON relationship merged with them; validate.py passed 0 errors / 0 warnings on the merged graph (entities 4,796 → 4,805; relationships 5,979 → 5,980). The 3 relationships proposed in this document only were adjudicated at merge and dropped (reasons in the merge log). Full record: `05-merge-log-2026-11-12.md` in this folder. The text below is the packet as staged, preserved as the pre-merge record.

---

**[As staged:] STAGED ONLY — NOT MERGED.** This packet stages GOV-006-style entity records for the Sports Firsts subjects who have no record in the Black Cultural Knowledge Graph. Nothing in this packet has been merged, nothing has been added to the canonical graph files (`knowledge-graph/entities.json`, `relationships.json`), and no ID in this packet is a minted graph ID. The machine-readable packet is `03-staged-graph-packet.json` in this folder.

## How the graph was checked
The build graph master (`~/workspace/culturetechlens/knowledge-graph/entities.json`, 4,796 records at check time, the November 2026 build graph) was searched by name and alias for all 26 register subjects, with fuzzy substring passes for the misses. The website snapshot CSV in `website/master/` was NOT used — it predates the November sports merges and would undercount. The Afro American Encyclopedia of Sports roster v2 (522 rows, 2026-10-24 dataset) was checked the same way.

## Graph ledger (26 subjects)
- **HELD — 17 subjects** already have canonical records (each is also in the Encyclopedia of Sports roster v2): Oliver Lewis CTL-E-6891 · Moses Fleetwood Walker CTL-E-6852 · Major Taylor CTL-E-6903 · Jack Johnson CTL-E-5508 · Fritz Pollard CTL-E-5871 · Jackie Robinson CTL-E-5415 · Alice Coachman CTL-E-6886 · Willie Thrower CTL-E-5936 · Althea Gibson CTL-E-6887 · Willie O'Ree CTL-E-6921 · Wendell Scott CTL-E-6923 · Arthur Ashe CTL-E-6211 · George Branham III CTL-E-6929 · Debi Thomas CTL-E-6916 · Tiger Woods CTL-E-6890 · Vonetta Flowers CTL-E-6939 · Shani Davis CTL-E-5583. No action staged for these.
- **STAGED — 9 subjects** are confirmed gaps (absent from the graph and from the roster) and are staged below.

## Staged records (9) — all IDs PROPOSED
The highest minted canonical ID at staging time was CTL-E-7406. Proposed IDs run CTL-E-7407–CTL-E-7415 in register order. They are proposals only: a merge mints real IDs and may renumber.

| PROPOSED ID | Subject | Type | Schema verification | GOV-004 grade | Description words | Sources |
|---|---|---|---|---|---|---|
| CTL-E-7407 | John Matthew Shippen Jr. | Person | Verified | Verified | 235 | 2 |
| CTL-E-7408 | George Poage | Person | Verified | Verified | 171 | 2 |
| CTL-E-7409 | John Baxter Taylor Jr. | Person | Verified | Verified | 170 | 2 |
| CTL-E-7410 | Shady Rest Golf and Country Club | Organization | Verified | Verified | 204 | 2 |
| CTL-E-7411 | Rajo Jack (Dewey Gatson) | Person | Provisional | Provisional | 226 | 2 |
| CTL-E-7412 | William DeHart Hubbard | Person | Verified | Verified | 188 | 2 |
| CTL-E-7413 | 1965–66 Texas Western Miners | Organization | Verified | Verified | 182 | 2 |
| CTL-E-7414 | Maurice Ashley | Person | Verified | Verified | 188 | 2 |
| CTL-E-7415 | Tia Norfleet | Person | Provisional | **Disputed** | 209 | 2 |

Every staged record carries: a description of at least 100 words (actual range 170–235), at least 2 independent sources with at least 1 authoritative, in the graph's six-field source form (accessed · citation · name · primary · supports · url), project tag PPL-001 (matching the November sports tranche convention), and a notes field marking it PROPOSED and unmerged.

**Schema constraint, stated plainly:** the graph schema's verification levels are only Verified and Provisional. Tia Norfleet's governing GOV-004 grade is **Disputed** — carried in her record's notes and in this packet — while her schema-level verification value is set to Provisional, the lowest the schema allows. No CTL surface may render her claim as fact from this record.

## Staged relationships (1 in JSON; the rest PROPOSED here only)
In the JSON, checked against the schema's relationship type matrix:
- **CTL-E-7407 (Shippen) — affiliated_with → CTL-E-7410 (Shady Rest)** — matrix-safe (Person → Organization). Evidence: Shippen was Shady Rest's professional and lived on site, 1931–1964 (Township of Scotch Plains).

Proposed in this document only, deliberately kept OUT of the JSON until a merge adjudicates endpoints and types:
- **1965–66 Texas Western Miners → Don Haskins (head_coach_of inverse / led_by)** — Haskins has no staged record in this packet and the direction/type pairing needs merge-time adjudication; the coaching fact is carried in the team's description instead.
- **George Poage → Chicago (associated_with is Person → Neighborhood only)** — Poage's Chicago residence (from c. 1920, postal clerk to 1953) is documented, but no canonical Neighborhood endpoint is asserted here; the fact is carried in his description.
- **John Baxter Taylor Jr. → William DeHart Hubbard (related_to)** — a legitimate Person → Person matrix type, but the "successor firsts" link is editorial rather than evidentiary; left out of the JSON so the staged packet carries evidence-bearing edges only.

## Known conflicts carried in the records, not resolved over
- Shippen's birth day: December 2, 1879 (MGA) vs. December 5, 1879 (PGA Tour) — description gives the month and year and flags the split.
- John Baxter Taylor's birth year: 1882 (World Athletics, Penn, National Portrait Gallery) vs. 1883 in Wikipedia-derived mirrors — 1882 used, variant noted.
- Shady Rest acquisition mechanism: purchase (Township) vs. lease (NRHP-nomination reporting) — description says "took over," asserting neither.
- Rajo Jack's racing start (1920 / 1923 / by 1925) and a stray 1951 death date in one secondary source, contradicted by his documented 1954 race — record uses February 1956 and grades the whole record Provisional.
- Maurice Ashley's title year: 1999 (requirements completed March 14, 1999; Britannica, US Chess, HistoryMakers, contemporaneous NYT) vs. 2000 in some FIDE-derived listings — 1999 used, variance noted.
- Tia Norfleet's very claim — staged as Disputed with both sides in the description and one source per side.

## Validation
`knowledge-graph/validate.py` cannot validate this packet standalone: it is hardcoded to the canonical files in the knowledge-graph folder and takes no path arguments. Stated plainly, per the build directive. An equivalent standalone check was therefore run against the staged JSON, applying validate.py's own rule set from `schema.json`: required fields present · entity type and subtype within schema enums · verification within schema levels · project_ids registered · IDs unique within the packet and non-colliding with all 4,796 canonical IDs · descriptions ≥100 words · ≥2 sources per record · every source exactly the six-field form with a well-formed URL · relationship endpoints present in the packet and within the type matrix. **Result: 0 errors, 0 warnings — STAGED VALIDATION PASSED.** This is a schema-conformance check of the staged fragment, not a merge validation; a real merge must still run validate.py against the combined graph.

## Counting note
Staged ledger, counted from `03-staged-graph-packet.json` itself: 9 entities (7 Person · 2 Organization) · 18 source records (2 per entity) · 1 relationship. Combined with the held ledger: 17 HELD + 9 STAGED = 26 subjects, matching the register.
