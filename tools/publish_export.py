#!/usr/bin/env python3
"""CTL-KG public export pipeline — LOCKED decision 2026-10-19.

Static JSON first (Phase 1), Cloudflare D1 named Phase 2, Neo4j internal
derived layer only, Kuzu killed. CSV masters stay canonical; this script is
READ-ONLY against the masters and generates derivatives in one publish run:

  graph-public.json   stamped slice ONLY (VERIFIED / STRONG EVIDENCE entities,
                      edges with both endpoints stamped) — no unverified row
                      can appear in the public file by construction
  counts.json         computed from the validated masters, never typed
  import-d1.sql       SQLite/D1 import for the SAME slice (Phase 2, not deployed)
  import-neo4j.cypher Cypher import for the SAME slice (internal only, not deployed)
  explorer.html       search-first static explorer (copied from template if present
                      alongside this script as explorer-template.html)

Discipline per the 2026-10-17 dataset rules: validate first, write outputs to
a temp location, validate outputs, then rename into place. Aborts with no
outputs touched if the masters fail validation.

Usage: python3 publish_export.py [out_dir]   (default: ../CTL-KG-004-Public-Export-<date>-v1)
"""
import csv, json, collections, datetime, os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
STAMPED_GRADES = {'VERIFIED', 'STRONG EVIDENCE'}

def load_masters():
    ent_path = os.path.join(DATA, 'entities', 'entities.csv')
    edge_path = os.path.join(DATA, 'edges', 'edges.csv')
    with open(ent_path, encoding='utf-8', newline='') as f:
        ents = list(csv.DictReader(f))
    with open(edge_path, encoding='utf-8', newline='') as f:
        edges = list(csv.DictReader(f))
    return ents, edges

def validate(ents, edges):
    errors = []
    ids = [r['kg_id'] for r in ents]
    if len(ids) != len(set(ids)):
        dup = [i for i, c in collections.Counter(ids).items() if c > 1]
        errors.append(f'duplicate entity ids: {dup[:10]}')
    idset = set(ids)
    for i, r in enumerate(ents):
        try:
            json.loads(r['props_json'])
        except Exception as e:
            errors.append(f'entities row {i} {r.get("kg_id")}: props_json does not parse: {e}')
    for i, e in enumerate(edges):
        if e['from_id'] not in idset:
            errors.append(f'edges row {i}: from_id {e["from_id"]} not in entities')
        if e['to_id'] not in idset:
            errors.append(f'edges row {i}: to_id {e["to_id"]} not in entities')
    return errors

def public_entity(r):
    props = json.loads(r['props_json']) if r['props_json'] else {}
    ver = props.pop('verification', {}) or {}
    source = ver.get('source', '')
    pub_ver = {'status': ver.get('status'), 'date': ver.get('date')}
    if source.startswith('http://') or source.startswith('https://'):
        pub_ver['source'] = source
    else:
        # never leak local filesystem paths into the public file
        pub_ver['source'] = None
        pub_ver['source_kind'] = 'ctl-internal-document'
    if ver.get('claims'):
        pub_ver['claims'] = ver['claims']
    out = {
        'id': r['kg_id'],
        'type': r['node_type'],
        'name': r['name'],
        'aliases': r['aliases'],
        'grade': ver.get('status'),
        'verification': pub_ver,
        'props': props,
    }
    if r.get('wikidata_qid'):
        out['wikidata_qid'] = r['wikidata_qid']
    return out

def sql_escape(s):
    return "'" + str(s).replace("'", "''") + "'"

def build_d1_sql(pub_ents, pub_edges):
    lines = [
        '-- CTL-KG-001 public slice — Cloudflare D1 / SQLite import (Phase 2, generated, do not hand-edit)',
        '-- Source: canonical CSV masters via tools/publish_export.py. Slice = stamped entities only.',
        'DROP TABLE IF EXISTS edges;',
        'DROP TABLE IF EXISTS entities;',
        'CREATE TABLE entities (id TEXT PRIMARY KEY, type TEXT NOT NULL, name TEXT NOT NULL, aliases TEXT, grade TEXT, json TEXT);',
        'CREATE TABLE edges (from_id TEXT NOT NULL, edge_type TEXT NOT NULL, to_id TEXT NOT NULL, since TEXT, until TEXT, evidence TEXT, source_ids TEXT, notes TEXT);',
        'CREATE INDEX idx_entities_name ON entities(name);',
        'CREATE INDEX idx_entities_type ON entities(type);',
        'CREATE INDEX idx_edges_from ON edges(from_id);',
        'CREATE INDEX idx_edges_to ON edges(to_id);',
    ]
    for e in pub_ents:
        lines.append('INSERT INTO entities VALUES (%s,%s,%s,%s,%s,%s);' % (
            sql_escape(e['id']), sql_escape(e['type']), sql_escape(e['name']),
            sql_escape(e['aliases'] or ''), sql_escape(e['grade'] or ''),
            sql_escape(json.dumps(e, ensure_ascii=False))))
    for e in pub_edges:
        lines.append('INSERT INTO edges VALUES (%s,%s,%s,%s,%s,%s,%s,%s);' % (
            sql_escape(e['from']), sql_escape(e['type']), sql_escape(e['to']),
            sql_escape(e['since'] or ''), sql_escape(e['until'] or ''),
            sql_escape(e['evidence'] or ''), sql_escape(e['source_ids'] or ''),
            sql_escape(e['notes'] or '')))
    return '\n'.join(lines) + '\n'

def cypher_escape(s):
    return "'" + str(s).replace('\\', '\\\\').replace("'", "\\'").replace('\n', ' ') + "'"

def build_neo4j_cypher(pub_ents, pub_edges):
    # Internal derived layer only (locked 2026-10-19) — never the public engine.
    lines = [
        '// CTL-KG-001 public slice — Neo4j import (INTERNAL derived layer only, generated, do not hand-edit)',
        '// Source: canonical CSV masters via tools/publish_export.py. Slice = stamped entities only.',
        'CREATE CONSTRAINT ctl_entity_id IF NOT EXISTS FOR (n:Entity) REQUIRE n.id IS UNIQUE;',
    ]
    by_type = collections.defaultdict(list)
    for e in pub_ents:
        by_type[e['type']].append(e)
    for typ, rows in sorted(by_type.items()):
        label = ''.join(ch for ch in typ if ch.isalnum()) or 'Entity'
        for e in rows:
            lines.append('MERGE (n:Entity:%s {id: %s}) SET n.name = %s, n.aliases = %s, n.grade = %s;' % (
                label, cypher_escape(e['id']), cypher_escape(e['name']),
                cypher_escape(e['aliases'] or ''), cypher_escape(e['grade'] or '')))
    for e in pub_edges:
        rel = ''.join(ch if (ch.isalnum() or ch == '_') else '_' for ch in e['type'].upper())
        lines.append('MATCH (a:Entity {id: %s}), (b:Entity {id: %s}) MERGE (a)-[:%s]->(b);' % (
            cypher_escape(e['from']), cypher_escape(e['to']), rel))
    return '\n'.join(lines) + '\n'

def main():
    today = datetime.date.today().isoformat()
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        HERE, '..', f'CTL-KG-004-Public-Export-{today}-v1')
    out_dir = os.path.abspath(out_dir)
    ents, edges = load_masters()
    errors = validate(ents, edges)
    if errors:
        print('VALIDATION FAILED — no outputs written:')
        for e in errors[:25]:
            print(' -', e)
        return 1

    stamped = {}
    grades = collections.Counter()
    types = collections.Counter()
    for r in ents:
        types[r['node_type']] += 1
        props = json.loads(r['props_json']) if r['props_json'] else {}
        status = (props.get('verification') or {}).get('status')
        grades[status or 'UNVERIFIED'] += 1
        if status in STAMPED_GRADES:
            stamped[r['kg_id']] = r

    pub_ents = [public_entity(stamped[k]) for k in stamped]
    pub_ents.sort(key=lambda e: (e['type'], e['name'].lower()))
    pub_edges = []
    for e in edges:
        if e['from_id'] in stamped and e['to_id'] in stamped:
            pub_edges.append({'from': e['from_id'], 'type': e['edge_type'], 'to': e['to_id'],
                              'since': e['since'], 'until': e['until'], 'evidence': e['evidence'],
                              'source_ids': e['source_ids'], 'notes': e['notes']})

    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    counts = {
        'dataset': 'CTL-KG-001',
        'generated_at': now,
        'generator': 'tools/publish_export.py (computed from master CSVs; never hand-edit)',
        'master': {'entities_total': len(ents), 'edges_total': len(edges),
                   'entities_by_type': dict(sorted(types.items())),
                   'verification': {'VERIFIED': grades.get('VERIFIED', 0),
                                    'STRONG_EVIDENCE': grades.get('STRONG EVIDENCE', 0),
                                    'stamped_total': len(stamped),
                                    'unverified': grades.get('UNVERIFIED', 0)}},
        'public_slice': {'entities': len(pub_ents), 'edges_both_endpoints_stamped': len(pub_edges)},
    }
    graph = {
        'dataset': 'CTL-KG-001',
        'kind': 'public-slice',
        'rule': 'Stamped entities only (VERIFIED / STRONG EVIDENCE); edges only where both endpoints are stamped. CSV masters are canonical; this file is a generated derivative.',
        'generated_at': now,
        'counts': counts['public_slice'] | {'master_entities_total': len(ents), 'master_edges_total': len(edges)},
        'entities': pub_ents,
        'edges': pub_edges,
    }

    os.makedirs(out_dir, exist_ok=True)
    tmp_dir = out_dir + '.tmp'
    os.makedirs(tmp_dir, exist_ok=True)
    files = {
        'graph-public.json': json.dumps(graph, ensure_ascii=False, indent=1),
        'counts.json': json.dumps(counts, ensure_ascii=False, indent=2),
        'import-d1.sql': build_d1_sql(pub_ents, pub_edges),
        'import-neo4j.cypher': build_neo4j_cypher(pub_ents, pub_edges),
    }
    for name, content in files.items():
        with open(os.path.join(tmp_dir, name), 'w', encoding='utf-8') as f:
            f.write(content)
    # validate the written public JSON before it replaces anything
    with open(os.path.join(tmp_dir, 'graph-public.json'), encoding='utf-8') as f:
        check = json.load(f)
    leaked = [e['id'] for e in check['entities'] if e['grade'] not in STAMPED_GRADES]
    if leaked:
        print('ABORT: unverified entities in public export:', leaked[:10])
        return 1
    idset = {e['id'] for e in check['entities']}
    bad_edges = [e for e in check['edges'] if e['from'] not in idset or e['to'] not in idset]
    if bad_edges:
        print('ABORT: slice edges with an endpoint outside the slice:', len(bad_edges))
        return 1
    if '/home/' in files['graph-public.json'] or 'workspace/ctl' in files['graph-public.json'].replace('CultureTechLens', ''):
        # claims text may legitimately cite CTL docs; hard-fail only on raw home paths in sources
        srcs = [e['verification'].get('source') for e in check['entities']]
        if any(s and s.startswith('/') for s in srcs):
            print('ABORT: local path leaked into a public source field')
            return 1
    tmpl = os.path.join(HERE, 'explorer-template.html')
    if os.path.exists(tmpl):
        with open(tmpl, encoding='utf-8') as f:
            files['explorer.html'] = f.read()
        with open(os.path.join(tmp_dir, 'explorer.html'), 'w', encoding='utf-8') as f:
            f.write(files['explorer.html'])
    for name in files:
        os.replace(os.path.join(tmp_dir, name), os.path.join(out_dir, name))
    os.rmdir(tmp_dir)

    print(json.dumps(counts, indent=2))
    for name in files:
        p = os.path.join(out_dir, name)
        raw = open(p, 'rb').read()
        import gzip
        print(f'{name}: {len(raw)} bytes, gzip {len(gzip.compress(raw, 9))} bytes, md5 {hashlib.md5(raw).hexdigest()}')
    print('written:', out_dir)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
