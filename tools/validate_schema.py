#!/usr/bin/env python3
"""CTL-KG-001 schema enforcement — the intake gate CTL-KG-001 never had.

The schema (CTL-KG-001-Schema-2026-10-16-v1) defines the rules on paper.
Until now nothing forced a record to obey them: the only validators in
tools/ check that props_json *parses*, IDs are unique, and edge endpoints
exist (publish_export.py), or assume props structure (recount.py).
props_json was a free-form blob: 99 distinct keys in the live master,
including duplicate concepts under two keys (birth/birth_date,
inst_type/institution_type) and schema-named keys nobody uses (url: 0
rows; the data uses `website` on 380).

This validator enforces the proposed contract in props_contract.json:

  ERROR (blocks intake in every mode)
    - header is not exactly kg_id,node_type,name,aliases,props_json,created,source
    - node_type outside the 8 CTL-KG-001 types
    - kg_id prefix does not match node_type, or ID malformed
    - duplicate kg_id or duplicate name (case-insensitive) in the file,
      and — with --against-master — against the live master
    - props_json does not parse, or parses to a non-object
    - verification object malformed (wrong shape or unknown status)
  ERROR in --strict (intake) mode, WARNING in --audit mode
    - a props key that is not in the contract allowlist for that type
    - a deprecated alias key (birth, death, institution_type, website,
      lane, release_date, premiere_date, first_aired)
    - the type's required key missing (work_type, outlet_type, ...)
    - a subtype value outside the CTL-KG-001 vocabulary
    - a year-like key holding a string instead of an int
  A master audit therefore reports legacy drift without rewriting a
  single master row; a staging batch must pass --strict before merge.

Discipline: READ-ONLY. This script never writes to the masters.
Usage:
  python3 validate_schema.py [entities.csv] [--strict|--audit]
                             [--against-master] [--json OUT] [--csv OUT]
Exit code 0 = no ERRORs, 1 = ERRORs found, 2 = could not run.
"""
import argparse, csv, json, re, sys, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = json.loads((HERE / "props_contract.json").read_text(encoding="utf-8"))
MASTER = HERE.parent / "data" / "entities" / "entities.csv"
EXPECTED_HEADER = ["kg_id", "node_type", "name", "aliases",
                   "props_json", "created", "source"]
ID_RE = re.compile(r"^CTL-(P|O|I|W|T|E|PL|L)-(\d+)$")


def check_file(path, strict, master_index=None):
    findings = []  # (level, kg_id, rule, detail)

    def err(kg, rule, detail):
        findings.append(("ERROR", kg, rule, detail))

    def drift(kg, rule, detail):
        findings.append(("ERROR" if strict else "WARNING", kg, rule, detail))

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != EXPECTED_HEADER:
            err("-", "header", f"header is {reader.fieldnames}, "
                                f"spec requires {EXPECTED_HEADER}")
        rows = list(reader)

    seen_ids, seen_names = {}, {}
    for r in rows:
        kg, typ, name = r.get("kg_id", ""), r.get("node_type", ""), r.get("name", "")
        if typ not in CONTRACT["per_type"]:
            err(kg, "node_type", f"unknown node_type {typ!r}")
            continue
        if not ID_RE.match(kg or "") or not kg.startswith(CONTRACT["id_prefix"][typ]):
            err(kg, "id_prefix", f"ID does not match prefix "
                                 f"{CONTRACT['id_prefix'][typ]} for {typ}")
        if kg in seen_ids:
            err(kg, "duplicate_id", "duplicate kg_id in file")
        seen_ids[kg] = True
        key = name.strip().lower()
        if key in seen_names:
            err(kg, "duplicate_name", f"name duplicates {seen_names[key]}")
        seen_names[key] = kg
        if master_index:
            if kg in master_index["ids"]:
                err(kg, "duplicate_id_master", "kg_id already in master")
            if key in master_index["names"]:
                err(kg, "duplicate_name_master",
                    f"name already in master as {master_index['names'][key]}")

        try:
            props = json.loads(r.get("props_json") or "")
            if not isinstance(props, dict):
                raise ValueError("props_json is not a JSON object")
        except Exception as e:
            err(kg, "props_json_parse", str(e))
            continue

        allowed = (set(CONTRACT["universal_allowed"])
                   | set(CONTRACT["per_type"][typ]["allowed"])
                   | set(CONTRACT["deprecated_aliases"]))
        for k in props:
            if k in CONTRACT["deprecated_aliases"]:
                drift(kg, "deprecated_alias",
                      f"{k!r} is a deprecated alias of "
                      f"{CONTRACT['deprecated_aliases'][k]!r}")
            elif k not in allowed:
                drift(kg, "unknown_key",
                      f"key {k!r} is not in the {typ} contract allowlist")

        spec = CONTRACT["per_type"][typ]
        # A deprecated alias still carries the concept, so it satisfies a
        # requirement (the alias itself is flagged separately above).
        present = set(props)
        for alias, canon in CONTRACT["deprecated_aliases"].items():
            if alias in present:
                present.add(canon)
        for req in spec.get("required", []):
            if req not in present:
                drift(kg, "missing_required", f"{typ} requires {req!r}")
        groups = spec.get("required_any", [])
        if groups and not any(all(g in present for g in group)
                               for group in groups):
            drift(kg, "missing_required",
                  f"{typ} requires one full group of {groups}")

        field = spec.get("subtype_field")
        if field and field in props:
            vocab = CONTRACT["subtype_vocabularies"][field]
            if str(props[field]) not in vocab:
                drift(kg, "subtype_vocab",
                      f"{field}={props[field]!r} is outside the "
                      f"CTL-KG-001 vocabulary")

        if "verification" in props:
            v = props["verification"]
            shape = CONTRACT["verification_shape"]
            if not isinstance(v, dict) or \
               sorted(v.keys()) != sorted(shape["required_subkeys"]):
                err(kg, "verification_shape",
                    f"verification subkeys are "
                    f"{sorted(v.keys()) if isinstance(v, dict) else type(v).__name__}, "
                    f"requires {shape['required_subkeys']}")
            elif v.get("status") not in shape["allowed_status"]:
                err(kg, "verification_status",
                    f"status {v.get('status')!r} not in {shape['allowed_status']}")

        for k in CONTRACT["int_year_keys"]:
            if k in props and not isinstance(props[k], int):
                drift(kg, "year_type",
                      f"{k}={props[k]!r} should be an int year")
    return rows, findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", default=str(MASTER),
                    help="entities CSV to validate (default: live master)")
    ap.add_argument("--strict", action="store_true",
                    help="intake mode: contract drift is an ERROR")
    ap.add_argument("--against-master", action="store_true",
                    help="also check ID/name collisions against the master")
    ap.add_argument("--json", help="write machine-readable report here")
    ap.add_argument("--csv", help="write findings CSV here")
    args = ap.parse_args()

    master_index = None
    if args.against_master and Path(args.file) != MASTER:
        with open(MASTER, newline="", encoding="utf-8") as f:
            mrows = list(csv.DictReader(f))
        master_index = {"ids": {r["kg_id"] for r in mrows},
                        "names": {r["name"].strip().lower(): r["kg_id"]
                                  for r in mrows}}

    try:
        rows, findings = check_file(Path(args.file), args.strict, master_index)
    except FileNotFoundError as e:
        print(f"cannot run: {e}")
        return 2

    by_level = collections.Counter(f[0] for f in findings)
    by_rule = collections.Counter(f[2] for f in findings)
    mode = "STRICT (intake)" if args.strict else "AUDIT"
    print(f"{args.file}: {len(rows)} rows, mode={mode}")
    print(f"ERRORs: {by_level.get('ERROR', 0)}  "
          f"WARNINGs: {by_level.get('WARNING', 0)}")
    for rule, n in by_rule.most_common():
        print(f"  {n:6d}  {rule}")
    for level, kg, rule, detail in findings[:15]:
        print(f"  [{level}] {kg} {rule}: {detail}")
    if len(findings) > 15:
        print(f"  … and {len(findings) - 15} more (see --csv/--json)")

    report = {"file": str(args.file), "rows": len(rows),
              "mode": mode, "errors": by_level.get("ERROR", 0),
              "warnings": by_level.get("WARNING", 0),
              "by_rule": dict(by_rule),
              "findings": [{"level": l, "kg_id": k, "rule": r, "detail": d}
                           for l, k, r, d in findings]}
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=2),
                                   encoding="utf-8")
    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["level", "kg_id", "rule", "detail"])
            w.writerows(findings)
    return 1 if by_level.get("ERROR") else 0


if __name__ == "__main__":
    raise SystemExit(main())
