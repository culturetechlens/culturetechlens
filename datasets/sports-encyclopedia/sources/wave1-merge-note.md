**CULTURETECHLENS** · "Culture, Clearly Seen." · Black Cultural Intelligence

# Wave 1 Merge Note — Roster v2 (CTL-DATA-SPORT-001)

**Date:** 2026-10-29 · **Merge executed by:** Wave 1 merge worker, under head rulings of 2026-10-29 · **Blueprint:** CTL-SPT-ENC v1.0 (adopted at the head 2026-10-24)
Cite as: CultureTechLens, *Afro American Encyclopedia of Sports — Wave 1 Merge Note, Roster v2 (CTL-DATA-SPORT-001)*, 2026-10-29.
Source: CultureTechLens

## Audit verdict (as received)

The head audit **PASSED** the Wave 1 candidate set: 278/278 candidates delivered, all four sports to target (Baseball 75 · Basketball 50 · Football 67 · Boxing 86), counts recomputed at the head, the firsts inventory verified, annotations blank throughout (no invented text), and the coordinator's catch — Roster v1 double-counting Rube Foster — verified at the head. The merge below executes the head's three rulings exactly. Roster v1 files (01–14) are immutable and were not edited; Roster v2 ships as new files 15–19.

## The three rulings, as executed

**Ruling 1 — Rube Foster fold.** Roster v1 held the same man twice: CTL-SPE-0001 "Andrew "Rube" Foster" (subject, seed, rich annotation) and CTL-SPE-0033 "Rube Foster" (athlete, graph U-06674). In Roster v2, **CTL-SPE-0001 survives as the single Foster row**: its annotation and notes are kept, its kind is set to **athlete** (he was both founder and player), graph_union_id **U-06674** is carried onto it, and its notes state the fold. **CTL-SPE-0033 does not appear as a row in v2**; it is recorded in `17-id-mapping-wave1.csv` as FOLDED-INTO CTL-SPE-0001. The ID CTL-SPE-0033 is retired and will never be reused.

**Ruling 2 — Replacement Baseball row.** Because the fold reduces Baseball by one, one additional Baseball candidate was added at merge to the wave's standard: **Willie McCovey** (temp ID W1-BSB-076), athlete, discipline MLB, sources **Baseball Hall of Fame; Encyclopaedia Britannica; Baseball-Reference**. McCovey — Hall of Fame first baseman (inducted 1986), 1959 National League Rookie of the Year, 521 career home runs, primarily with the San Francisco Giants — was verified absent from Roster v1 and from all 278 Wave 1 candidates before selection. His row carries `chicago_connection: None documented` (no Chicago tie is documented; none was invented) and an empty `firsts_flag` — no firsts claim is made, so blueprint §2.7 is satisfied by construction. Baseball therefore lands at exactly **120 unique rows**. Minting choice (stated per the brief): the replacement mints **last in the Baseball block**, as CTL-SPE-0320.

**Ruling 3 — Toothpick Jones accepted.** Sam "Toothpick" Jones (W1-BSB-035 → **CTL-SPE-0279**) is merged as a distinct person. His v2 row's notes carry the explicit disambiguation: Samuel "Toothpick" Jones (1925–1971), baseball pitcher, is distinct from (1) Sam Jones (1933–2021), the basketball guard, and (2) Samuel Pond "Sad Sam" Jones (1892–1966), the baseball pitcher carried in unresolved conflation at CTL-SPE-0243. The CTL-SPE-0243 conflation **HOLD (2026-10-16) remains open and is untouched by this merge** — CTL-SPE-0243 and CTL-SPE-0244 remain the roster's 2 unassigned rows, unchanged.

## Merge mechanics

Permanent IDs were minted sequentially from **CTL-SPE-0245** in the v1 deterministic order — sports in CTL-SPT order (Baseball, Basketball, Football, Boxing), within a sport by the candidates' temp-ID order: Baseball CTL-SPE-0245–0320 (75 candidates + the replacement, last), Basketball CTL-SPE-0321–0370 (50), Football CTL-SPE-0371–0437 (67), Boxing CTL-SPE-0438–0523 (86). **Minted range: CTL-SPE-0245–CTL-SPE-0523 (279 IDs).** The full temp-ID → permanent-ID mapping is `17-id-mapping-wave1.csv` (279 minted/replacement lines + the SPE-0033 fold line). The v2 roster schema adds `chicago_connection` and `firsts_flag` for **all** rows (see Deviations & method notes for how v1 rows were coded). Candidate columns otherwise carried over unchanged; wave annotations stay blank.

## Final counts — Roster v2

- **Total rows: 522** = 243 surviving Roster v1 rows (244 − folded CTL-SPE-0033) + 279 Wave 1 rows (278 candidates + 1 replacement).
- **Sport-assigned: 520 · Unassigned: 2** (CTL-SPE-0243, CTL-SPE-0244, both carried unchanged).
- **By status:** roster 459 · stub 63 · full 0 · published 0. (The fold removed one stub — CTL-SPE-0033 — from v1's 64.)
- **By kind:** athlete 380 · subject 66 · team 41 · coach 26 · institution 8 · league 1.
- **Graph-linked:** 24 wave rows carry a verified graph_union_id, plus U-06674 now carried on the surviving Foster row.

### Gap table v2 (control sheet — full detail in `18-gap-table-v2.csv`)

| Sport | Target | Rostered (v2) | Remaining |
|---|---|---|---|
| Baseball | 120 | 120 | 0 |
| Basketball | 120 | 120 | 0 |
| Football | 110 | 110 | 0 |
| Boxing | 90 | 90 | 0 |
| Track & Field | 90 | 4 | 86 |
| Tennis | 50 | 4 | 46 |
| Golf | 40 | 4 | 36 |
| Horse Racing | 30 | 2 | 28 |
| Soccer | 45 | 3 | 42 |
| Gymnastics | 35 | 3 | 32 |
| Swimming & Diving | 30 | 3 | 27 |
| Wrestling | 35 | 4 | 31 |
| Cycling | 20 | 3 | 17 |
| Volleyball | 25 | 2 | 23 |
| Softball | 25 | 1 | 24 |
| Lacrosse | 20 | 3 | 17 |
| Rowing | 15 | 1 | 14 |
| Fencing | 15 | 3 | 12 |
| Weightlifting & Powerlifting | 20 | 1 | 19 |
| Figure Skating | 15 | 2 | 13 |
| Speed Skating | 12 | 2 | 10 |
| Martial Arts | 25 | 2 | 23 |
| Ice Hockey | 20 | 3 | 17 |
| Auto Racing | 25 | 4 | 21 |
| Mixed Martial Arts | 30 | 3 | 27 |
| Rodeo & Bull Riding | 15 | 3 | 12 |
| Bowling | 15 | 2 | 13 |
| Billiards | 12 | 1 | 11 |
| Bodybuilding | 20 | 4 | 16 |
| Skiing & Snowboarding | 15 | 3 | 12 |
| Bobsled / Skeleton | 12 | 2 | 10 |
| Equestrian | 12 | 1 | 11 |
| Rugby | 15 | 2 | 13 |
| Skateboarding | 12 | 3 | 9 |
| Surfing | 10 | 2 | 8 |
| Shooting & Archery | 12 | 0 | 12 |
| **TOTAL** | **1212** | **520** | **692** |

All sports outside the Wave 1 four are unchanged from Roster v1.

## Women and Chicago tallies (merged roster)

- **Women (persons): 80** = 39 Wave 1 women (Baseball 5 · Basketball 16 · Football 5 · Boxing 13, per the audited candidate package) + 41 Roster v1 women identified at merge from the v1 rows' own records: Toni Stone; Allie Quigley, Angel Reese, Candace Parker, Courtney Vandersloot, Elena Delle Donne, Kahleah Copper, Lusia Harris; Claressa Shields; Alice Coachman, Wilma Rudolph, Allyson Felix; Althea Gibson, Serena Williams; Briana Scurry, Crystal Dunn; Dominique Dawes, Gabby Douglas, Simone Biles; Simone Manuel; Tamyra Mensah-Stock; Kittie Knox; Flo Hyman, Rita Crockett; Natasha Watley; Anita DeFrantz; Ibtihaj Muhammad; Debi Thomas, Starr Andrews; Erin Jackson; Nia Abdallah; Angela Hill; Cheryl Daniels; Iris Kyle; Seba Johnson, Bonnie St. John; Vonetta Flowers, Elana Meyers Taylor; Paige Johnson; Phaidra Knight; Samarria Brevard. One further women-focused row, the Chicago Sky (team, Wave 1 Basketball), sits outside the women-persons count, as in the candidate package.
- **Chicago-coded rows: 75** = 48 Wave 1 rows (Team 32 · Birthplace 13 · School 3, as audited) + 27 Roster v1 rows (all Team, coded under the method below). Merged by type: **Team 59 · Birthplace 13 · School 3 · None documented 447.**

## Firsts inventory, carried forward

**46 flagged firsts: 38 two-sourced claims · 8 verification-pending** — carried into Roster v2 unchanged in the `firsts_flag` column, under blueprint §2.7: a first publishes only with two independent sources, at least one primary/institutional; the 8 pending rows (including 3 Baseball rows whose underlying claims were never specified in their source fragments) are labeled "reported first — verification pending" in the flag itself, with an explicit do-not-publish instruction on the 3 unspecified Baseball rows. The full per-row inventory is in the Wave 1 candidate package README (`wave1-fill-2026-10-29/README.md`), which is filed with this merge. The replacement row (McCovey) adds no first.

## Deviations and method notes (every one, named)

1. **Foster sources unioned.** The ruling specified the surviving row's annotation, notes, kind, and graph ID. At merge, CTL-SPE-0001's `sources` were unioned with the folded row's (result: `listal:List 1; graph:played_for; listal:List 4`) so the fold does not silently drop CTL-SPE-0033's provenance. The fold is stated in the row's notes.
2. **The folded row's annotation is not in v2.** Per the ruling, the surviving row keeps CTL-SPE-0001's annotation. CTL-SPE-0033's annotation ("The paradox: he built the Negro National League…") therefore does not appear in Roster v2; it remains preserved verbatim in the immutable Roster v1 files (09/10). Named here so the loss is a recorded consequence of the ruling as written, not a silent one.
3. **v1 Chicago coding is conservative by rule.** For Roster v1 rows, `chicago_connection` was coded **only** from the row's own `notes` field (a `played_for Chicago …` line → Team) plus Chicago-named franchise rows whose notes read "team franchise itself" (Cubs, White Sox, Chicago American Gears, Chicago Bulls, Chicago Bears → Team); everything else is "None documented," and every v1 `firsts_flag` is empty. Chicago ties documented only in a v1 row's *annotation* — e.g., Andrew "Rube" Foster's league run from Chicago, Angel Reese's and Courtney Vandersloot's Chicago seasons, Candace Parker's Chicago title, Caleb Williams's Bears tenure — were **not** coded, per the brief's notes-only rule. The merged Chicago tally (75) is therefore a documented floor, not a ceiling; a future annotation-inclusive coding pass can raise it, but nothing was invented to raise it here.
4. **Wave candidate notes keep their staged wording.** Per the brief ("candidate columns carry over unchanged"), Wave 1 rows retain their build-time notes (including "Staged Wave 1 candidate for head audit; not merged into Roster v1"), which now read as provenance. The only note edits in the entire merge are the two the head ordered: the Foster fold note on CTL-SPE-0001 and the disambiguation appended to Sam "Toothpick" Jones (CTL-SPE-0279). The replacement row's notes are new, as the ruling required.
5. **Replacement minting position.** The brief allowed the replacement to mint last in Baseball's block or in sequence; it mints **last in the Baseball block (CTL-SPE-0320)**, keeping each sport's minted block contiguous.
6. **No other deviation.** No v1 row other than CTL-SPE-0001 was altered in any field; no candidate was dropped, added (beyond the ruled replacement), or re-sorted; the CTL-SPE-0243 conflation HOLD and both unassigned rows are exactly as Roster v1 left them.

## Files in this merge

| File | What it is |
|---|---|
| `15-roster-v2.csv` / `16-roster-v2.json` | Roster v2 — 522 rows, 13 columns (v1's 11 + `chicago_connection` + `firsts_flag`) |
| `17-id-mapping-wave1.csv` | All 279 Wave 1 temp IDs → minted CTL-SPE IDs, plus the CTL-SPE-0033 fold line |
| `18-gap-table-v2.csv` | Control sheet regenerated from Roster v2, with totals row (520 / 1,212 · 692 remaining) |
| `19-wave1-merge-note.md` | This note |

Cite as: CultureTechLens, *Afro American Encyclopedia of Sports — Wave 1 Merge Note, Roster v2 (CTL-DATA-SPORT-001)*, 2026-10-29.
Source: CultureTechLens
