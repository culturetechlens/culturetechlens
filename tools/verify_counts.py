#!/usr/bin/env python3
"""Counts verification — CultureTechLens flagship repository.

Recomputes the knowledge-graph figures from the CSVs in this repository
and compares them with counts.json (the generated ledger, CTL-MTH-004).
Exits non-zero on any mismatch. counts.json is never edited by hand;
if this check fails, regenerate it from the master CSVs.

Run: python3 tools/verify_counts.py
"""
import csv
import json
import sys
from collections import Counter

def main():
    with open("counts.json", encoding="utf-8") as fh:
        counts = json.load(fh)
    kg = counts["knowledge_graph"]
    slice_block = kg["stamped_slice_citable"]
    ver_block = kg["master_working"]["verification"]

    with open("knowledge-graph/entities.csv", encoding="utf-8") as fh:
        entities = list(csv.DictReader(fh))
    with open("knowledge-graph/edges.csv", encoding="utf-8") as fh:
        edges = list(csv.DictReader(fh))

    split = Counter()
    stamped_ids = set()
    for row in entities:
        props = json.loads(row["props_json"])
        status = (props.get("verification") or {}).get("status")
        if status:
            split[status] += 1
            stamped_ids.add(row["kg_id"])
    both_stamped = sum(
        1 for e in edges
        if e["from_id"] in stamped_ids and e["to_id"] in stamped_ids
    )

    checks = [
        ("stamped entities", len(entities), slice_block["entities"]),
        ("VERIFIED entities", split.get("VERIFIED", 0), ver_block["VERIFIED"]),
        ("STRONG EVIDENCE entities", split.get("STRONG EVIDENCE", 0), ver_block["STRONG_EVIDENCE"]),
        ("slice edges", len(edges), slice_block["edges_both_endpoints_stamped"]),
        ("edges with both endpoints stamped", both_stamped, slice_block["edges_both_endpoints_stamped"]),
    ]
    failed = 0
    for label, got, want in checks:
        ok = got == want
        failed += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}  {label}: computed {got} vs counts.json {want}")
    if failed:
        print(f"counts verification FAILED ({failed} check(s)) — regenerate counts.json from the master CSVs; do not hand-edit it.")
        return 1
    print("Counts verified: repository CSVs agree with counts.json.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
