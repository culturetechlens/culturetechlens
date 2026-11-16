CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# SCOUR-LOG — Drive-wide scour for the Sports Encyclopedia (CTL-DS-SPO-000001)
### Executed 2026-11-16 by Dion, on William Maxey's directive: "scour the drive and find more to add to it"
### Method: every find verified from the actual file, counted, deduped by normalized name + CTL-SPE/graph ID against seed (153), roster v1 (244) and roster v2 (522). Dispositions: ADD (fits the entry schema, placement from the source's own data, inside the sport's remaining blueprint gap) · ANNEX (real sports material held off the roster, reason stated) · LOG ONLY (duplicate, unverifiable for placement, or out of scope).

## Search record
- **Drive folder searched in full:** "CTL Afro American Encyclopedia of Sports — Dataset Foundation CTL-DATA-SPORT-001 (2026-10-24)" (Drive ID 1Sy3eDHuC7GLa2MC_nCsXJaUw5XBqJF1J) — 22 files + wave1-fill-2026-10-29 subfolder (5 files).
- **Drive-wide name searches:** Sports Firsts · Sports Core · Sports Bench · seed-roster · gap-table · roster · Encyclopedia · Negro leagues · Olympics · Boxing · athlete · Entity Depth · sports-photo · wave1 · Sports Desk · CTL-DATA-SPORT.
- **Folders/packages opened:** CTL Sports Firsts (2026-11-12, Drive ID 14jX9ARYPStYJIzgdmXVYlKNb595lyuCk) — 8 files; Sports Core 10 packet folder; Sports Bench 6 packet folder; folder 01 dataset packages (local copies from the 2026-11-16 audit + Clones #3–#8 builds); Canonical Graph v2.1 ZIP (folder 91 copy).
- **Local dataset files cross-checked row by row:** KG333 (333), AEO-500 (500, Sports section 24), PERF-AEO-500 (500), FC300 (300), Photo Registry 232 (232), Chicago Black Culture merged (199), sports photo addendum 2026-11-03 (305, latest of 9 dated copies in Drive).

## Finds and dispositions

### ADD — 10 rows minted CTL-SPE-0524–0533
| Source | Found | Added | Detail |
|---|---|---|---|
| CTL Sports Firsts package, 2026-11-12 (register 01-firsts-register.md, Drive ID 1NphAX49yTIXH8QANqGJ0YgWtARclfoTw; staged packet 03, IDs CTL-E-7407–7415) | 26 register subjects: 17 already in roster v2 (the package's own HELD ledger) + 9 staged subjects confirmed absent from v2 | **7** | Poage, Taylor, Hubbard (Track & Field) · Shippen, Shady Rest (Golf) · Rajo Jack, Norfleet (Auto Racing). Grades carried verbatim: Verified ×5 (exact form), Provisional ×1 (Rajo Jack), Disputed ×1 (Norfleet — roster-status row, no annotation, no first asserted). The other 2 staged subjects → ANNEX below. |
| KG333 Black Americans Registry (CTL-DS-KG3-000001) + AEO-500 Sports section (24 subjects, all KG333-sourced) | 26 KG333 entities with sports descriptions; 20 already in v2; 6 new | **3** | Sha'Carri Richardson, Noah Lyles (Track & Field) · Coco Gauff (Tennis) — sports with open blueprint gap. The other 3 new → ANNEX (sports at target). AEO-500's 24 Sports subjects resolve to the same names (18 already in v2, the same 6 new) — counted once, not twice. |

### ANNEX — 54 rows in annex/held-and-manifest-annex.csv
| Source | Count | Reason |
|---|---|---|
| Sports Firsts staged subjects held | 2 | Texas Western Miners (Basketball at target 120/120) · Maurice Ashley (chess — not one of the blueprint's 36 sports; taxonomy ruling is William's). Both Verified in their registers. |
| KG333/AEO-500 crossovers held | 3 | JuJu Watkins, Anthony Edwards (Basketball 120/120) · Jayden Daniels (Football 110/110). Verified entities; held for Wave 2 / target revision, never silently over target. |
| Sports photo addendum 2026-11-03 (Drive ID 1Mot7f7l7lX2P9U9nTybKiBAaneUo13oZ; 305 rows, all status CLEARED, rights per row) | 49 subjects not in roster v2 (255 of 305 match v2 names; 1 further row, Earvin "Magic" Johnson, folds into the existing Magic Johnson row as an alias form — logged as a fold, not a find) | The addendum is a photo manifest: it carries no sport/discipline field, so a roster placement cannot be made from the row's own data (roster v1 placement rule). Subjects named individually in the annex as the Wave 2 candidate queue — Globetrotters, WNBA stars, wrestlers, MMA fighters, track/tennis greats among them. Photos do not ship with this dataset. |

### LOG ONLY — duplicates, out of scope, or unverifiable for placement
| Find | Count | Disposition |
|---|---|---|
| Wave 1 candidates (wave1-fill-2026-10-29/wave1-candidates.csv) | 278 | Already merged into roster v2 by the 2026-10-29 merge — duplicates by construction. Ships in sources/ as provenance. |
| Sports Core 10 + Sports Bench 6 staged packets (2026-10-16) | 16 entities | Already folded into the seed (seed provenance: packet 16) and through it into v1/v2. Duplicate. (Their JSON exports could not be downloaded intact — see spec F-S1; the seed's own provenance lines are the record used.) |
| Blueprint §7 anchors (CTL-SPT-ENC v1.0) | 96 names | Already accounted in roster v1: 91 added + 5 folded. Duplicate. |
| Knowledge Graph v2.1 (verified-only, 3,488 entities) sports-described Persons not in v2 | 14 | LOG ONLY: the set mixes true sports figures whose only placement evidence here is a general graph description (incl. current wrestlers) with false positives (disc jockeys, a producer, a news anchor, a two-sport college athlete turned official). None carries roster-grade placement data in this source; the wrestler tranche overlaps the photo-addendum annex queue, which is the cleaner record. |
| PERF-AEO-500 occupation crossovers not in v2 | 8 (of 9 flagged; Paul Robeson is already in v2) | LOG ONLY: performer-primary identities whose sport is a secondary Wikidata occupation (e.g. Terry Crews, Mr. T, Duane Martin). Their registry home is PERF; no sport placement is stated in the source row beyond the occupation string. |
| FC300 fictional characters, sport-related | 18 | REJECTED for the roster: fictional characters; the encyclopedia is a real-sports roster. Their home is FC300 (CTL-DS-FC3-000001). |
| Photo Registry 232 sports-subject cards | 3 true sports cards (Angel Reese/Chicago Sky 2024 · Negro leagues All-Stars, Comiskey Park 1936 · Rube Foster portrait 1924) of 232 | Manifest references only, rights per card (CC BY-SA 2.0 · rights as stated on card · Public domain). All three subjects are already in roster v2. No photos ship. (Keyword-adjacent music cards — e.g. Chess Records — are not sports material.) |
| Chicago Black Culture merged places (199) | 0 sports entries | Searched by name/category: the place set is churches, clubs, venues, theaters, banks. No stadium/arena/sports institution rows exist in the file. None added, none annexed. |
| Boxing profile essays in Drive (Boxing_Profiles_Complete.md, Boxing_Vol2_Profiles.md, 2026-05-02) | ~14 profiled names | Essay-form research, not roster data; the profiled champions are already in roster v2 (Boxing is at its 90/90 target). LOG ONLY. |
| CTL Entity Depth 600 program files (2026-10-25) | 2 site-deploy ZIPs (~134–191 MB) + notes | Not roster files — site build/deploy packages. Identified by name, size and the 2026-11-16 census; not opened. LOG ONLY. |
| Listal "Black sports" list (Ranked Lists Collection, register #4) | 12 items per register v1.0 | Provenance only. The seed already drew its Listal entries (64) from the founder's lists; the Listal copy job is CLOSED (William, 2026-11-16) and was not resumed or touched by this scour. |
| Drive-wide essay/stub files (Olympics, Boxing, athlete name searches) | ~90 small files | Essays, encyclopedia-entry drafts and 22–37-byte stub files from worker-era folders — narrative material, not structured roster data; every athlete named in the substantive ones is already in v2 or in the annex queue. LOG ONLY. |

## Scour totals
- **Found and verified as sports material not in roster v2: 64** (10 added + 54 annexed), plus 14 graph-description persons logged without placement evidence.
- **Duplicates confirmed and excluded: 370** (278 Wave 1 + 16 packet entities + 96 blueprint anchors, of which the anchors/packets overlap the seed/v1 counts by construction — the figure is a disposition count, not a unique-person count).
- **Roster movement: 522 → 532** (assigned 520 → 530; unassigned 2, unchanged). **Gap to the 1,212 blueprint target: 692 → 682.**
- Nothing was invented: every added row's name, sport, discipline, annotation and sources come from its named scour source; every held row names its blocker.
