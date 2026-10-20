# Methodology

**Tags:** methodology, evidence-grading, verification, source-hierarchy, canonical-counts

How CTL knows what it claims to know. The methodology set: CTL-MTH-001 Evidence Grading · MTH-002 Verification · MTH-003 Source Hierarchy · MTH-004 Canonical Counts · MTH-005 Verification & Provenance · MTH-006 Metrics & Audit Evidence · MTH-007 Release Gate. Datasets cite these by ID; this folder carries the public summaries.

## The evidence ladder (CTL-MTH-001)
Every claim in every CTL dataset carries one grade:
- **VERIFIED FACT** — established by a primary or authoritative source, fetched and read in full.
- **STRONG EVIDENCE** — supported by credible sourcing that falls short of primary confirmation.
- **REASONABLE INFERENCE** — a labeled conclusion drawn from verified facts; the reasoning is shown.
- **HYPOTHESIS** — a stated conjecture, published only as a question to be tested.
A claim is never published at a higher grade than its source supports, and UNRESOLVED is never asserted as settled (CTL-GOV-004).

## Verification stamps (knowledge graph)
An entity carries a **stamp** when its record has passed verification: VERIFIED (2,005 in the current slice) or STRONG EVIDENCE (1,483). The public graph is exactly the stamped slice — 3,488 of the 4,111 master entities; the 623 UNVERIFIED seed-standard rows are never published, labeled or not (CTL Phase 0, snapshot-only).

## Canonical counts (CTL-MTH-004)
Every number in this repository is **generated, never typed**: `counts.json` is computed from the master data by the scripts in `tools/`, and any hand-entered count found in a draft is a defect. Registers — not prose — are the authority for counting.

## Corrections
Errors, when found, are corrected in the open: datasets carry their corrections with them, superseded public snapshots keep their errata attached, and nothing is silently rewritten.

Canonical home: CTL methodology registry (internal). This folder is the public summary.
