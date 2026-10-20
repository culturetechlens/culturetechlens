# Research Report — CTL-REV-001 v5.0 "Tech Decoded Wave"

Package: CTL-REV-001 v5.0 · Data checked October 18, 2026 · Owner: CultureTechLens (William Maxey)
Task: (A) 3 missing product categories × 5 = 15 products; (B) the Tech Decoded plain-talk guide layer (3 guides). Contract: TECH_DECODED_BRIEF.md + EXPANSION_REGISTER_v5.md in this folder; v1–v4 contracts and evidence rules remain in force.

## Data (in this folder)
- **dataset-v5.json** — 115 categories × 5 = 575 products. First 112 categories = v4.0 verbatim (programmatically deep-equal to expansion-v4/dataset-v4.json); last 3 = this wave (also archived as expansion-15.json; batches batch-v5-a/b/c.json). Item schema = v3/v4 (16 fields incl. link_checked_date / price_checked_date = "2026-10-18").
- **tech-decoded.md** — the three decoder guides (see Guides below).
- v1–v4 dataset files untouched.

## Validation (parent-validated programmatically on the final files — counters, not line counts)
- Counts: 115 categories / 575 products; dataset-v5 prefix deep-equal to dataset-v4; expansion-15.json identical to the dataset-v5 tail.
- All 15 new items: exactly the 16 schema fields; pros = 3 / cons = 2 on every item.
- Badges: exactly one "Best Overall" + one "Best Value" in each of the 3 new categories.
- Duplicates: 0 across all 575 product names — exact, case-insensitive, and fuzzy-normalized checks all clean.
- **link_verified: 575/575 · price_verified: 497/575.** The new 15 are 15/15 links and 13/15 prices (the 2 unverified are named below and flagged in the data). The other 78 unverified prices are v1–v4 carryovers, still honestly flagged.
- Images: all 15 new image URLs independently re-verified by the parent — HTTP 200/206 + image content type, **15/15** (14 JPEG/PNG + 1 WebP).

## Per-category results
- **Ergonomic & Accessible Keyboards** (`ergonomic-accessible-keyboards`, E): Best Overall — Kinesis Advantage360 Professional, $479. Best Value — Kensington Pro Fit Ergo Wired, $53. Budget pick — AZIO KB505U Vision large-print, $34. Every accessibility claim in the copy traces to a fetched manufacturer page (Kinesis, Matias, Logitech, Kensington, AZIO maker pages).
- **Desktop, Mini & All-in-One Computers** (`desktop-mini-all-in-one-computers`, E): form-factor span held — tower ×2, mini ×2, all-in-one ×1, all complete purchasable computers (no barebones). Best Overall — Dell Pro Tower Plus (QBT1250), $1,789. Best Value — HP OmniDesk Desktop AI (M03-0000t), $730. Budget pick — Mac mini M4, $699. Upgradeable-vs-sealed stated per pick from fetched specs; convenience premiums stated in dollars in cons (≈$70 mini-over-tower; ≈$900 AIO-over-tower).
- **TVs by Room Size & Access Need** (`tvs-by-room-and-access`, C): organized by room/viewer — two 43″ small-room picks, two 75″+ large-room picks, two access-need picks (Sony BRAVIA 3 voice control; Samsung Q7F accessibility suite incl. Voice Guide / Audio Description / SeeColors / Sign Language Zoom per Samsung's own US accessibility page). Best Overall — LG 77″ C5 OLED evo, $2,200. Best Value — Samsung 43″ Crystal UHD U8000H, $230.

## Guides (tech-decoded.md)
- **Keyboards Decoded** — ~1,900 words, **6 sources**. All six types, switch-feel taxonomy with actuation forces, layouts incl. split/ergonomic, hot-swap/rollover/polling translated; typewriter → Model M → Hall effect thread. Ends linking to `mechanical-keyboards`, `ergonomic-accessible-keyboards`.
- **Computers Decoded** — ~2,350 words, **8 sources**. All eight form factors; CPU/GPU/RAM/SSD/ports in lived-use terms; 5-year cost directional only (no prices, per brief). NPU graded in tiers: Microsoft's 40+ TOPS Copilot+ definition (Verified Fact) vs. the short list of shipping NPU-accelerated features (Strong Evidence) vs. PCWorld's two-year "failed spectacularly" verdict (Contested — CTL grade RESEARCH). Ends linking to `laptops`, `gaming-laptops`, `desktop-mini-all-in-one-computers`, `computer-monitors`.
- **TVs Decoded** — ~2,570 words, **12 sources** (marginally over the 2,500-word nominal ceiling — flagged, not hidden). Label tree made honest (QLED = marketing-layer color coat on LCD; "Motion Rate" labeled a marketing term = native 60Hz on the cited model); HDR formats, HDMI 2.1/VRR/ALLM, size-vs-distance (SMPTE ~30° / THX ~40°), ACR/privacy, accessibility checklist from Samsung's support pages. Ends linking to `smart-tvs`, `tvs-by-room-and-access`, `soundbars`.
- Marketing terms labeled as marketing throughout: QLED family names, Motion Rate/TruMotion/MotionFlow, "AI upscaling," "AI PC." The only dollar figure in the guides is the $2.2M Vizio FTC settlement — a legal fact, not a product price.

## Honest gaps (by name — do not "fix" silently)
- **AZIO KB505U Vision ($34) — price_verified = false.** AZIO's own page carries no price; the street price appeared only in search-result offers (Best Buy page fetch failed; Newegg Business CAPTCHA-blocked). Recorded as approximate and flagged.
- **HP OmniStudio X 27″ ($1,630) — price_verified = false.** HP's PDP was fetched twice; its price never renders in fetched text (JS-driven). Figure comes from HP's own search-result offer for that exact URL, rounded and flagged.
- **Kensington Pro Fit Ergo Wired** — manufacturer page showed the keyboard unavailable with restock expected December 2026; kept as Best Value on its fetched $52.99 price, stock caveat stated in cons.
- **Logitech Ergo K860 for Business** — "Sold Out Temporarily" at fetch time; noted in cons.
- **Mac mini (M4)** — item claims are all from the fetched Best Buy configuration ($699, 16GB/256GB); 2026 reporting suggests Apple has since reshuffled configurations/pricing — a freshness pass is recommended before publication.
- Two sources blocked during research and not retried per policy (P.C. Richard 403, Newegg Business CAPTCHA); no dataset claim depends on either.
- **Guide claims softened/dropped:** manufacturer OLED lifespan-hour claims dropped as self-interested (burn-in graded from RTINGS' multi-year test only — real under static/high-brightness abuse, most sets surviving 10,000+ hours); uncorroborated NPU efficiency numbers (XDA-style ~80% power claims) dropped; vendor Hall-effect/optical speed and 100M-keystroke superlatives framed as brand ratings, not facts; conflicting OLED/QD-OLED nit figures dropped; Micro LED given no price (no reliable fetched source); large-print keyboard specifics kept to decision guidance (no fetched product sources).
