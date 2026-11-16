CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — FC300 Black Fictional Characters (CTL-DS-FC3-000001)
### v1.0 package · 2026-11-16

## The 25 columns
Rank (1–300) · CTL Character ID (key, CTL-FC300-###; names repeat across franchises — never key on name) · Character · Franchise_or_Work · Medium_Category (7 values) · Creator (blank 56 — unrecorded, not zero) · First_Appearance · Portrayed_By_or_Voiced_By (blank 71 — many literary/comics characters have no portrayer) · Coverage_Status (below) · Wikidata_QID ("NONE — see Coverage Status" where none exists) · Wikidata_URL · Wikipedia_Title · Wikipedia_URL (blank 3) · Image_Source_URL · Image_Credit · Image_License_Status · Image_Alt_Text · Citation · AEO_Primary_Question · AEO_Direct_Answer · AEO_Question_Cluster (5) · Medusa_Keywords · CTL_Page_Slug (culturetechlens.com/fictional-characters/…; liveness UNVERIFIED — spec F-F2) · AEO_Schema · Verification_Note (2026-11-04 API pass).

## Coverage Status — the dataset's evidence vocabulary (verbatim, spec R2)
- **Own Wikipedia Article** (102): the character has a standalone article.
- **Wikidata Item — No Own Wikipedia Article** (37): a structured record exists; no article.
- **Own Wikipedia Article — No Wikidata Item Yet (Partial Gap)** (4).
- **Franchise Coverage Only — No Character QID Found** (157): the character is documented only inside the franchise/work's page. Plain-language: *the world hasn't given this character a record of their own — this registry does.*

## Image rules (spec R3)
Every row is link-only. Image_Source_URL points at the covering page; Image_License_Status instructs a file-page check before any reuse and warns that character art/stills are usually non-free (Wikipedia fair use). **No image files are distributed with this dataset, in any version.**
