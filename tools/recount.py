#!/usr/bin/env python3
"""Generate counts.json from the live CTL-KG master CSVs.
Read-only against the masters. Run at release time, after validation.
Usage: python3 recount.py [data_dir]  (default: ../data relative to this script)
"""
import csv, json, collections, os, sys, datetime

here = os.path.dirname(os.path.abspath(__file__))
data = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, '..', 'data')
ent = list(csv.DictReader(open(os.path.join(data, 'entities', 'entities.csv'), encoding='utf-8')))
edges = list(csv.DictReader(open(os.path.join(data, 'edges', 'edges.csv'), encoding='utf-8')))

grades = collections.Counter()
types = collections.Counter()
for r in ent:
    types[r['node_type']] += 1
    p = json.loads(r['props_json'])
    grades[p['verification']['status'] if 'verification' in p else 'UNVERIFIED'] += 1
vids = {r['kg_id'] for r in ent if '"verification"' in r['props_json']}
slice_edges = [e for e in edges if e['from_id'] in vids and e['to_id'] in vids]

counts = {
    'dataset': 'CTL-KG-001',
    'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
    'generator': 'tools/recount.py (computed from master CSVs; never hand-edit)',
    'entities_total': len(ent),
    'edges_total': len(edges),
    'entities_by_type': dict(sorted(types.items())),
    'verification': {
        'VERIFIED': grades.get('VERIFIED', 0),
        'STRONG_EVIDENCE': grades.get('STRONG EVIDENCE', 0),
        'stamped_total': sum(grades.values()) - grades.get('UNVERIFIED', 0),
        'unverified': grades.get('UNVERIFIED', 0),
    },
    'verified_slice': {
        'entities': len(vids),
        'edges_both_endpoints_verified': len(slice_edges),
    },
}
out = os.path.join(data, 'counts.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(counts, f, indent=2)
print(json.dumps(counts, indent=2))
print('written:', out)
