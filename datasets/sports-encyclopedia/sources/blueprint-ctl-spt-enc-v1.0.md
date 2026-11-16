# Afro American Encyclopedia of Sports — Blueprint

**CTL-SPT-ENC v1.0** — CultureTechLens Sports Encyclopedia Governance
**Status:** Blueprint adopted for build — 2026-10-22
**Owner:** William Maxey, Founder / CultureTechLens (CTL)
**Working title:** Afro American Encyclopedia of Sports
**Canonical entity:** CultureTechLens (CTL) — never "Culture Tech Lens," "CT Lens," or other variants
**Standard:** CTL war chest — every entry defensible and cited. Nothing enters that cannot be defended.

> Sports history is not a list of heroes. It is a system: leagues Black athletes built when they were barred, institutions that trained them, records that were kept — and records that were not. This encyclopedia documents the system.

---

## 1. Why this exists — the existence audit (summary)

No complete, current, digital, all-sports African American sports encyclopedia exists. The closest works, verified 2026-10-22:

| Work | Year | Scope | Limit |
|---|---|---|---|
| Arthur Ashe, *A Hard Road to Glory* (3 vols.) | 1988 | Multi-sport history | 38 years old. Ashe built it because the most current comprehensive text he could find was already 20 years old. |
| David L. Porter, *African-American Sports Greats* | 1995 | 166 profiles, 12 sports | Current only through mid-1995 |
| Porter & others, *Latino and African American Athletes Today* | 2004 | 174 profiles, 18 sports | Post-1975 focus only; 17 women total |
| *Encyclopedia of Ethnicity and Sports in the United States* | 2000 | All ethnic groups | Not African American–specific; print / in-library |
| *Encyclopedia of Negro League Baseball* | — | 3,000+ entries | One sport only |
| Smithsonian NMAAHC, *Sports: Leveling the Playing Field* | 2016– | Museum gallery | Physical exhibition, not a searchable reference |
| The HistoryMakers Digital Archive | — | 93 sports oral histories | Oral history archive, not an encyclopedia |
| Encyclopedia.com, "Sports" | — | Baseball, Football, Boxing, Basketball, "Other Sports" | 5 buckets, early-2000s framing |

**Conclusion:** The field is print, partial, or frozen in 1988–2004. Everything systematic after 1995 — Serena and Venus Williams' full careers, Tiger Woods, LeBron James, Simone Biles, Allyson Felix, Claressa Shields, Coco Gauff, the WNBA's growth, the Black quarterback era, NIL — has no encyclopedic home. That gap is the opportunity, and it widens every season.

---

## 2. Scope rules

1. **Subject:** African American athletes, coaches, executives, owners, officials, institutions, teams, leagues, events, and records **inside the United States sports system** — professional, collegiate (including HBCUs), Olympic/Paralympic, and amateur.
2. **Diaspora rule:** An athlete born outside the U.S. is included when their defining career is in the U.S. system (a U.S. league, a U.S. national team, a U.S. college). A purely foreign career is out of scope and is cross-referenced, not entered.
3. **Eras:** 1875 (Oliver Lewis wins the first Kentucky Derby) to present. Earlier plantation-era and informal competition is covered in sport overviews where sources allow — labeled as such, never overstated.
4. **Women are structural, not an appendix.** Every sport carries a full women's section. There is no separate "Women in Sports" silo.
5. **Power is a subject.** Coaches, general managers, owners, agents, referees/umpires, commissioners, union leaders, trainers, and sportswriters (especially the Black press) are entry types equal to players.
6. **Absence is data.** Where Black participation in a sport is near-zero, the entry documents the exclusion — barriers, cost, geography, governing-body history — instead of skipping the sport. A documented absence is harder to copy than a list.
7. **No invented firsts.** A "first" claim requires two independent sources, at least one primary or institutional (league, hall of fame, governing body, contemporaneous Black press). Unverified firsts are published as "reported first — verification pending," or not published.

---

## 3. Naming and URL standard

Subject-first, brand-last — the CTL-PSGO v2.0 formula applied to sports.

**Sport page title formula:**
```
[Sport] in Black America | Afro American Encyclopedia of Sports | CultureTechLens
```
Example: `Baseball in Black America | Afro American Encyclopedia of Sports | CultureTechLens`

**Entry page title formula:**
```
[Person / Institution / Event Name] | [Sport] | CultureTechLens
```
Example: `Toni Stone | Baseball | CultureTechLens`

**Stable URLs — never break a published URL; 301 redirect if a slug must change:**
- Encyclopedia home: `culturetechlens.com/sports-encyclopedia`
- Sport: `culturetechlens.com/sports-encyclopedia/[sport-slug]` — e.g. `/sports-encyclopedia/baseball`
- Entry: `culturetechlens.com/sports-encyclopedia/[sport-slug]/[entry-slug]`
- Cross-sport indexes: `culturetechlens.com/sports-encyclopedia/firsts`, `/women`, `/hbcu`, `/power`, `/chicago`

---

## 4. ID system (mandatory, permanent, never reused)

| Object | ID format | Example |
|---|---|---|
| Sport | `CTL-SPT-##` | CTL-SPT-01 = Baseball |
| Entry (person, institution, team, event, record) | `CTL-SPE-####` | CTL-SPE-0001 |
| Cross-sport index / apparatus page | `CTL-SPX-##` | CTL-SPX-01 = Master Firsts Timeline |

IDs are never reused for a different subject, even if an entry is retired. Retired entries keep their ID and a retirement note. This is the registry a competitor cannot fake quickly.

---

## 5. Entry data schema (mandatory per entry)

| Field | Notes |
|---|---|
| Entry ID | CTL-SPE-#### |
| Entry type | Athlete / Coach / Executive / Owner / Official / Agent / Media / Institution / Team / League / Event / Record |
| Name | Canonical name + known variants |
| Sport | CTL-SPT-## + sport name |
| Discipline | e.g. Track & Field → 100m; Auto Racing → Drag Racing |
| Born / Founded | Date + place, sourced |
| Died / Dissolved | Date + place, sourced, if applicable |
| Teams / Institutions | With years |
| HBCU connection | School + years, or "None documented" |
| Firsts | Each first as its own sourced line — never bundled |
| Records / Honors | Stats as of a stated date; source named |
| Women's section flag | Entry is filed in the sport's women's index where applicable |
| Power role flag | Coach / executive / owner / official / agent / media, where applicable |
| Era | Pre-integration (–1947 baseball benchmark, sport-specific) / Integration / Post-integration / Modern (1996–) — sport-specific dates govern |
| Chicago connection | Team, school, birthplace, or "None documented" — powers the Chicago index |
| Sources | Minimum 2; primary/institutional preferred; full citations |
| Related entries | Minimum 3 internal links (link graph, §9) |
| Citation block | Per §8 |
| Status | Draft / Verified / Published / Needs update |
| Published / Updated | YYYY-MM-DD |

An entry that cannot fill Firsts, Records, and Sources from real sources does not publish. It stays Draft. That rule *is* the moat's quality wall.

---

## 6. The per-sport template (7 sections, every sport, no exceptions)

1. **Overview & segregation history** — how the sport excluded, and when/how that changed (sport-specific dates)
2. **Black leagues & institutions** — the parallel structures: Negro Leagues, American Tennis Association, United Golfers Association, Black Fives basketball, HBCU conferences (CIAA, SIAC, SWAC, MEAC), Black-owned teams and promotions
3. **Firsts timeline** — dated, sourced, one line per first
4. **Athletes** — entries per the §5 schema, to the sport's target count in §7
5. **Women** — full section: athletes, institutions, firsts, records
6. **Power** — coaches, executives, owners, officials, agents, media from that sport
7. **Records & sources** — the sport's record table (dated) and its bibliography

---

## 7. The 36 sports — taxonomy, targets, anchors

Targets are **full-depth (Gold) entry counts**: athletes + power + institutions + events for that sport. Anchors are the documented starting points for research — every anchor claim passes §2.7 verification before publication.

### Tier A — Core 8 (650 entries)

| ID | Sport | Disciplines counted inside | Target | Anchor institutions / figures |
|---|---|---|---|---|
| CTL-SPT-01 | Baseball | MLB, Negro Leagues, women's baseball | 120 | Negro Leagues (1920); Jackie Robinson; Satchel Paige; Toni Stone |
| CTL-SPT-02 | Basketball | NBA, WNBA, ABA, Black Fives, streetball | 120 | New York Rens; Harlem Globetrotters; Earl Lloyd; Lusia Harris |
| CTL-SPT-03 | Football | NFL, college, HBCU football, CFL (U.S. players) | 110 | Fritz Pollard; Grambling State / Eddie Robinson; Doug Williams |
| CTL-SPT-04 | Boxing | Professional, Olympic, women's boxing | 90 | Jack Johnson; Joe Louis; Muhammad Ali; Claressa Shields |
| CTL-SPT-05 | Track & Field | Sprints, distance, jumps, throws, combined events | 90 | Jesse Owens; Alice Coachman; Wilma Rudolph; Allyson Felix |
| CTL-SPT-06 | Tennis | Singles, doubles, ATA circuit | 50 | American Tennis Association (1916); Althea Gibson; Arthur Ashe; Serena Williams |
| CTL-SPT-07 | Golf | PGA, LPGA, UGA circuit | 40 | United Golfers Association (1925); Charlie Sifford; Lee Elder; Tiger Woods |
| CTL-SPT-08 | Horse Racing | Jockeys, trainers, owners | 30 | Oliver Lewis (first Kentucky Derby, 1875); Isaac Murphy; Black jockeys of the early Derbys |

### Tier B — Expansion 14 (337 entries)

| ID | Sport | Disciplines counted inside | Target | Anchor institutions / figures |
|---|---|---|---|---|
| CTL-SPT-09 | Soccer | MLS, NWSL, USMNT, USWNT, college | 45 | Cobi Jones; Briana Scurry; Crystal Dunn |
| CTL-SPT-10 | Gymnastics | Artistic, rhythmic, trampoline | 35 | Dominique Dawes; Gabby Douglas; Simone Biles |
| CTL-SPT-11 | Swimming & Diving | Pool, open water, diving, synchronized | 30 | Simone Manuel; Cullen Jones; Anthony Ervin; segregated-pool history |
| CTL-SPT-12 | Wrestling | Freestyle, Greco-Roman, folkstyle, professional | 35 | Kenny Monday; Jordan Burroughs; Tamyra Mensah-Stock; Bobo Brazil (pro) |
| CTL-SPT-13 | Cycling | Road, track, BMX, mountain | 20 | Major Taylor; Kittie Knox; Nelson Vails |
| CTL-SPT-14 | Volleyball | Indoor, beach | 25 | Flo Hyman; Rita Crockett |
| CTL-SPT-15 | Softball | Fastpitch, college, Olympic | 25 | Natasha Watley; Black college softball |
| CTL-SPT-16 | Lacrosse | Field, box | 20 | Jim Brown (Syracuse); Kyle Harrison; Chazz Woodson |
| CTL-SPT-17 | Rowing | Sweep, sculling, coxswain | 15 | Anita DeFrantz (Olympic medal, 1976) |
| CTL-SPT-18 | Fencing | Foil, épée, sabre | 15 | Peter Westbrook; Ibtihaj Muhammad; Miles Chamley-Watson |
| CTL-SPT-19 | Weightlifting & Powerlifting | Olympic lifting, powerlifting | 20 | John Davis (Olympic weightlifting champion) |
| CTL-SPT-20 | Figure Skating | Singles, pairs, ice dance | 15 | Debi Thomas; Starr Andrews |
| CTL-SPT-21 | Speed Skating | Long track, short track | 12 | Shani Davis; Erin Jackson |
| CTL-SPT-22 | Martial Arts | Judo, taekwondo, karate | 25 | Nia Abdallah (taekwondo, Olympic silver 2004); Rhadi Ferguson (judo) |

### Tier C — Moat-makers 14 (225 entries)

The sports every prior work skipped. Owning these is what turns a reference into a moat.

| ID | Sport | Disciplines counted inside | Target | Anchor institutions / figures |
|---|---|---|---|---|
| CTL-SPT-23 | Ice Hockey | NHL, women's, college | 20 | Willie O'Ree; Grant Fuhr; Anson Carter |
| CTL-SPT-24 | Auto Racing | NASCAR, IndyCar, drag racing, F1 (U.S. careers) | 25 | Wendell Scott; Willy T. Ribbs; Antron Brown; Bubba Wallace |
| CTL-SPT-25 | Mixed Martial Arts | UFC and major promotions | 30 | Jon Jones; Demetrious Johnson; Angela Hill |
| CTL-SPT-26 | Rodeo & Bull Riding | Rodeo events, PBR | 15 | Bill Pickett; Fred Whitfield; Charlie Sampson (bull riding world champion, 1982) |
| CTL-SPT-27 | Bowling | PBA, PWBA, college | 15 | George Branham III (first Black PBA Tour champion, 1986); Cheryl Daniels |
| CTL-SPT-28 | Billiards | Pool, snooker (U.S.) | 12 | Cisero Murphy (world pool champion) |
| CTL-SPT-29 | Bodybuilding | Bodybuilding, physique | 20 | Chris Dickerson; Lee Haney; Ronnie Coleman; Iris Kyle |
| CTL-SPT-30 | Skiing & Snowboarding | Alpine, freestyle, snowboard | 15 | Seba Johnson; Bonnie St. John (Paralympic); Zeb Powell |
| CTL-SPT-31 | Bobsled / Skeleton | Bobsled, skeleton, luge | 12 | Vonetta Flowers (first Black Winter Olympic gold, 2002); Elana Meyers Taylor |
| CTL-SPT-32 | Equestrian | Show jumping, dressage, eventing | 12 | Paige Johnson; documented-exclusion record (see §2.6) |
| CTL-SPT-33 | Rugby | Union, sevens, league (U.S.) | 15 | Phaidra Knight; Perry Baker |
| CTL-SPT-34 | Skateboarding | Street, park, vert | 12 | Stevie Williams; Ray Barbee; Samarria Brevard |
| CTL-SPT-35 | Surfing | Shortboard, longboard | 10 | Nick Gabaldon; Black Surfers Association (founded 1975) |
| CTL-SPT-36 | Shooting & Archery | Shooting sports, archery | 12 | Firsts-and-exclusion audit sport — no anchor published until §2.7 verification is met |

### Totals — verified arithmetic

- Tier A: 120 + 120 + 110 + 90 + 90 + 50 + 40 + 30 = **650**
- Tier B: 45 + 35 + 30 + 35 + 20 + 25 + 25 + 20 + 15 + 15 + 20 + 15 + 12 + 25 = **337**
- Tier C: 20 + 25 + 30 + 15 + 15 + 12 + 20 + 15 + 12 + 12 + 15 + 12 + 10 + 12 = **225**
- **Full-depth total: 1,212 entries across 36 sports** (= 44+ disciplines uncollapsed)
- Plus apparatus (§10): 5 cross-sport indexes and the Master Firsts Timeline

---

## 8. Citation standard (applies to every page)

Every sport page and entry page carries a copy-paste citation block, per CTL's existing citation standard:

```
Cite this:
CultureTechLens. "[Entry Name]." Afro American Encyclopedia of Sports, 2026.
CTL ID: CTL-SPE-#### · https://culturetechlens.com/sports-encyclopedia/[slug]
Published: YYYY-MM-DD · Updated: YYYY-MM-DD
```

Master citation for the work as a whole:
> CultureTechLens. *Afro American Encyclopedia of Sports.* Chicago-based Black cultural intelligence platform founded by William Maxey. https://culturetechlens.com/sports-encyclopedia

AI citability checklist (from CTL citation standard, applied per page): public and crawlable; clear title, organization, and date; facts in quotable sentences; citation block present; linked from at least one other CTL page. No orphan pages.

---

## 9. Link graph

```
Sport page → Entry pages → Institution pages → HBCU index → Firsts timeline →
Women index → Power index → Chicago index → CTL Index → CultureTechLens
```

Every entry links to: its sport page, at least one institution, and at least one related entry (§5). A knowledge graph that happens to be an encyclopedia — the same relationship layer as the CTL knowledge graph (300 entities) and the playlist link graph.

---

## 10. Apparatus — the cross-sport indexes (CTL-SPX)

| ID | Apparatus | Function |
|---|---|---|
| CTL-SPX-01 | Master Firsts Timeline | Every sourced first, 1875–present, one searchable chronology across all 36 sports |
| CTL-SPX-02 | Women Index | Every women's entry, per sport — the correction to 17-of-174 |
| CTL-SPX-03 | HBCU Index | CIAA, SIAC, SWAC, MEAC histories; HBCU athletes/coaches cross-linked to their sports |
| CTL-SPX-04 | Power Index | Coaches, executives, owners, officials, agents, media — updated annually with a dated count per league |
| CTL-SPX-05 | Chicago Index | Chicago-born, Chicago-schooled, and Chicago-team entries — CTL's home layer |

---

## 11. Build phases

Depth levels per sport: **Bronze** = overview + firsts timeline + 10 entries. **Silver** = 50% of target, all 7 template sections live. **Gold** = full target, scorecard ≥ 90 (§12).

| Phase | Work | Result |
|---|---|---|
| 1 — Claim | All 36 sport pages at Bronze (36 × ~12 = ~430 pages incl. entries) | Territory claimed; every sport citable; no competitor can say "first all-sports" after this |
| 2 — Core | Tier A (8 sports) to Gold | 650 entries; the sports 90% of readers come for, at full depth |
| 3 — Expansion | Tier B (14 sports) to Gold | 987 cumulative entries |
| 4 — Moat | Tier C (14 sports) to Gold | **1,212 entries; moat complete** |
| 5 — Apparatus | All 5 CTL-SPX indexes live; Power Index goes annual | The encyclopedia becomes a living institution, not a finished book |

Phase 1 first, on purpose: breadth is the claim, depth is the proof. Prior works did depth in a few sports and never claimed the rest.

---

## 12. Completeness scorecard (internal, per sport)

| Category | Weight |
|---|---|
| Overview & segregation history, sourced | 15% |
| Black institutions section complete | 15% |
| Firsts timeline — every first double-sourced | 15% |
| Entry count vs. target | 20% |
| Women's section at full depth | 15% |
| Power section complete | 10% |
| Citation blocks + stable URLs + internal links | 10% |
| **Total** | **100%** |

Gold requires ≥ 90. A sport below 90 does not get called complete in any CTL copy. Internal score only — never published as an external ranking claim.

---

## 13. Measurement (monthly, alongside the CTL Index cycle)

- Entries published / verified / needing update, by tier
- % of published entries that are women (target: women's entries are a full section in 36 of 36 sports; count reported honestly, not rounded up)
- % of published entries post-1995 (the era no prior work covers — target: this is the majority of new publishing)
- Power Index counts, by league, with dates
- External citations logged in `citation-log.md` (media, academic, AI answers)
- Corrections issued — logged publicly; a visible corrections record is a trust asset, not an embarrassment

## 14. Boundaries

- No entry publishes on a single source for a first, a record, or a death date.
- No "GOAT" or ranking language inside encyclopedia entries. Rankings live in the CTL Index, under its methodology. The encyclopedia states records and lets them stand.
- No content about living minors beyond published competition results.
- Statistics are always dated ("as of [date], per [source]") — sports records move, and an undated stat becomes a future error.
- Print is a later derivative. Digital-first: a print volume freezes at publication, which is exactly how Ashe (1988) and Porter (1995) became gaps.

## 15. Open decisions for William

1. **Title lock:** Working title is *Afro American Encyclopedia of Sports* (your phrase). Confirm as the canonical title, or change once — before Phase 1 pages publish, because URLs and citations depend on it.
2. **Chicago layer depth:** CTL-SPX-05 is specced as an index. Decide at Phase 5 whether Chicago gets full chapter treatment (Chicago teams, schools, and venues as institutions).
3. **Advisory names:** Phase 2+ benefits from named sport historians per Tier A sport (the Porter model used 44 contributors). Decide: solo CTL authorship, or credited contributors under CTL editorship and this schema.

---

*Prior works stopped at 12, then 18 sports, in print, in 1995 and 2004. This blueprint claims 36 sports, 1,212 entries, women and power as structure, digital and citable from day one. The moat is not the idea — anyone can have the idea. The moat is 1,212 defended entries under one ID system, one citation standard, and one name: CultureTechLens.*

**Changelog**
- v1.0 (2026-10-22): Blueprint created — existence audit, scope rules, naming/URL standard, CTL-SPT / CTL-SPE / CTL-SPX ID system, entry schema, 7-section sport template, 36-sport taxonomy with verified 1,212-entry target, 5-phase build, scorecard, measurement, boundaries, open decisions.
