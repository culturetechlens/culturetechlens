#!/usr/bin/env python3
"""Schema lint — CultureTechLens flagship repository.

Structural validation of the knowledge-graph slice against the CTL-KG-001
conventions: required columns, kg_id format and uniqueness, the eight-type
vocabulary, parseable props_json, stamped verification on every entity,
and edges that resolve to entities in the slice.

Run: python3 tools/lint_schema.py
"""
import csv
import json
import re
import sys

ENTITY_COLUMNS = ["kg_id", "node_type", "name", "aliases", "props_json", "created", "source"]
EDGE_COLUMNS = ["from_id", "edge_type", "to_id", "since", "until", "evidence", "source_ids", "notes"]
NODE_TYPES = {"Person", "Work", "Place", "Event", "Institution", "Outlet", "Topic", "List"}
STAMPED = {"VERIFIED", "STRONG EVIDENCE"}
ID_RE = re.compile(r"^CTL-[A-Z]{1,2}-\d+$")

def main():
    errors = []
    with open("knowledge-graph/entities.csv", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != ENTITY_COLUMNS:
            errors.append(f"entities.csv columns {reader.fieldnames} != {ENTITY_COLUMNS}")
        entities = list(reader)
    with open("knowledge-graph/edges.csv", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != EDGE_COLUMNS:
            errors.append(f"edges.csv columns {reader.fieldnames} != {EDGE_COLUMNS}")
        edges = list(reader)

    ids = set()
    for n, row in enumerate(entities, start=2):
        kid = row["kg_id"]
        if not ID_RE.match(kid or ""):
            errors.append(f"entities.csv:{n} kg_id {kid!r} does not match CTL-<TYPE>-<number>")
        if kid in ids:
            errors.append(f"entities.csv:{n} duplicate kg_id {kid}")
        ids.add(kid)
        if row["node_type"] not in NODE_TYPES:
            errors.append(f"entities.csv:{n} node_type {row['node_type']!r} not in the eight-type vocabulary")
        if not (row["name"] or "").strip():
            errors.append(f"entities.csv:{n} empty name")
        try:
            props = json.loads(row["props_json"])
        except Exception as exc:
            errors.append(f"entities.csv:{n} props_json does not parse: {exc}")
            continue
        status = (props.get("verification") or {}).get("status")
        if status not in STAMPED:
            errors.append(f"entities.csv:{n} {kid} is not stamped (verification.status={status!r}); the public slice is stamped-only")

    for n, edge in enumerate(edges, start=2):
        for end in ("from_id", "to_id"):
            if edge[end] not in ids:
                errors.append(f"edges.csv:{n} {end} {edge[end]} does not resolve to an entity in the slice")
        if not (edge["edge_type"] or "").strip():
            errors.append(f"edges.csv:{n} empty edge_type")

    for err in errors[:50]:
        print("FAIL ", err)
    if errors:
        print(f"schema lint FAILED ({len(errors)} error(s))")
        return 1
    print(f"Schema lint passed: {len(entities)} entities, {len(edges)} edges, all stamped, all endpoints resolve.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
