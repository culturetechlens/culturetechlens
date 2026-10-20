# Tools — how the numbers are made

**Tags:** tools, recount, validation, public-export, ctl-mth-004

The counts in [`../counts.json`](../counts.json) are generated, never typed (CTL-MTH-004). These are the scripts that generate and check them, published so anyone can rerun the arithmetic:

- `recount.py` — reads the master CSVs (`entities.csv`, `edges.csv`) and emits `counts.json`: totals, per-type counts, verification grades, and the stamped-slice size.
- `validate_schema.py` — validates the graph against the CTL-KG-001 schema (node/edge types, required fields, ID format).
- `publish_export.py` — builds the public export (stamped slice only) from the masters; the export that feeds the site explorer.

Licence: MIT (code), see [`../LICENSES.md`](../LICENSES.md). The masters themselves live in [`../knowledge-graph/`](../knowledge-graph/).
