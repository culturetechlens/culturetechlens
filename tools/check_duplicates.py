#!/usr/bin/env python3
"""Duplicate detection — CultureTechLens flagship repository.

Fails on structural duplicates: a repeated kg_id or a byte-identical
edge row. Reports repeated (from_id, edge_type, to_id) triples with
differing evidence or dates as warnings — a relationship can be attested
more than once — and same-name records as warnings too. Those are
editorial questions, not build errors.

Run: python3 tools/check_duplicates.py
"""
import csv
import sys
from collections import Counter

def main():
    with open("knowledge-graph/entities.csv", encoding="utf-8") as fh:
        entities = list(csv.DictReader(fh))
    with open("knowledge-graph/edges.csv", encoding="utf-8") as fh:
        edges = list(csv.DictReader(fh))

    failed = 0
    dup_ids = [k for k, v in Counter(r["kg_id"] for r in entities).items() if v > 1]
    for kid in dup_ids:
        print(f"FAIL  duplicate kg_id: {kid}")
        failed += 1
    dup_rows = [k for k, v in Counter(tuple(e.values()) for e in edges).items() if v > 1]
    for row in dup_rows:
        print(f"FAIL  byte-identical edge row repeated: {row[0]} {row[1]} {row[2]}")
        failed += 1
    trip = Counter((e["from_id"], e["edge_type"], e["to_id"]) for e in edges)
    for triple, v in sorted(trip.items()):
        if v > 1:
            print(f"WARN  edge triple attested {v}x with differing evidence/dates: {triple} — attestation multiplicity, editorial review")
    name_type = Counter((r["name"].strip().lower(), r["node_type"]) for r in entities)
    for (name, ntype), v in sorted(name_type.items()):
        if v > 1:
            print(f"WARN  {v} records named {name!r} of type {ntype} — editorial review, not a build error")

    if failed:
        print(f"duplicate detection FAILED ({failed} structural duplicate(s))")
        return 1
    print(f"No structural duplicates: {len(entities)} unique kg_ids, {len(edges)} unique edges.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
