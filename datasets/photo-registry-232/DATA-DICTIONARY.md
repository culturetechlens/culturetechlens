CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — Cited Photo Archive Registry (CTL-DS-PHO-000001)
### v1.0 package · 2026-11-16

## The 19 columns
Registry Row (extraction order) · CTL Photo Registry ID (key, CTL-PHOTO-REG-###) · Card_Title (as published) · Linked_CTL_Entity_As_Stated (the entity name as the site card states it; blank on 102 cards — the cards' own gap, spec F-P1) · KG300_Entity_ID (the graph join key; filled on 27 rows after the v1.0 linkage pass — see linkage-log.md) · KG300_Page_Slug (blank on all rows at extraction; slugs are minted by the site lane, not this dataset) · Photographer · Source (Wikimedia Commons 161 · Library of Congress 41 · NARA DOCUMERICA 17 · others) · Rights (the card's rights statement, verbatim; all 232 filled) · What_It_Documents · CTL_Citation_As_Published (the citation exactly as the card prints it) · Medusa_Register_Ref_As_Published (blank on 177) · Medusa_Candidate_Keywords (marked in the data "UNREGISTERED — register via administration before use") · AEO_Question / AEO_Answer_From_Card (the card's answer-engine pair) · Photos_Page_URL · CTL_Photo_File_URL (filled on 104 rows) · Verification_Note (extraction provenance, 2026-11-04) · Title_Subject_KG300_Match (the 8 title-recovered matches recorded at extraction).

## The boundary (spec §3)
This registry mirrors the **published** Cited Photo Archive cards. The internal **Photo Rights Log v4** (2,127 rows) is the clearance system of record under CTL-PHOTO-001/002. They are different instruments and are never merged; growth flows log → card → registry.

## License note
The registry's metadata is CC BY 4.0. The photographs carry their own per-row rights (column: Rights) and are not relicensed by this dataset.
