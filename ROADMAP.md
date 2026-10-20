# Roadmap — named gaps, stated as plans

CultureTechLens publishes its gaps rather than hiding them. Each item below is a known limitation of the current public data, with its intended remedy. Status as of 2026-10-20.

## 1. Wikidata identifier enrichment (the clearest gap)
The knowledge graph's 4,111 master entities carry **zero Wikidata QIDs (0 of 4,111)** — no entity is yet linked to its Wikidata counterpart, which limits interoperability with the wider linked-open-data ecosystem. **Plan:** a dedicated QID-matching pass over the stamped slice first (3,488 entities), human-reviewed, with matches recorded per entity. CultureTechLens's own Wikidata item is Q141705779.

## 2. Knowledge graph v1.4 deposit
The Zenodo v1.3 abstract (2026-10-16) predates the canonical recount and Ruling A (2026-10-19). **Plan:** a v1.4 deposit whose abstract carries the canonical figures (master 4,111 / 2,527; stamped slice 3,488 / 2,162), alongside posting the pending Retraction-class erratum on v1.3's withdrawn "2,426 verified" figure.

## 3. Photo coverage
419 of 4,111 master entities carry a photo. **Plan:** clearance waves under CTL-PHOTO-001 (Documentary Image Integrity) — every published image ships with its full per-image record (source, creator, rights, credit, verification date). Photos publish to Drive/Zenodo deposits, not this repository (Phase 0).

## 4. Index structured data
The CultureTechLens Index (Edition 2026-10, DOI 10.5281/zenodo.23081630) is published as PDF; its structured data and methodology package (CTL-IDX-001) recovery is in progress. **Plan:** deposit the structured edition alongside the PDF so the Index is machine-citable, not only readable.

## 5. Release discipline
Each future change to the public datasets lands as a dated GitHub Release with generated counts, so the citable unit is an edition — not a moving folder.

CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence
