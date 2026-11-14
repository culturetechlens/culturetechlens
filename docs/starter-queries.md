---
title: Starter Queries — CultureTechLens Knowledge Graph
---

# Starter queries for teachers and journalists

**Culture, Clearly Seen.** · Black Cultural Intelligence · Source: CultureTechLens

Six questions the published graph answers today, with copy-paste code.
Load the slice once (the starter notebook, `notebooks/ctl-graph-starter.ipynb`, does this):

```python
import json, pandas as pd
BASE = "https://raw.githubusercontent.com/culturetechlens/culturetechlens/main"
entities = pd.read_csv(f"{BASE}/knowledge-graph/entities.csv")
edges = pd.read_csv(f"{BASE}/knowledge-graph/edges.csv")
byid = entities.set_index("kg_id")["name"]
```

## 1. What does the archive hold, and how sure is it?

```python
entities["node_type"].value_counts()
props = entities["props_json"].apply(json.loads)
props.apply(lambda p: (p.get("verification") or {}).get("status")).value_counts()
```
*Answer shape:* 3,488 records — 2,005 VERIFIED, 1,483 STRONG EVIDENCE. Every claim graded, every source named.

## 2. Which records are located in Chicago?

```python
chi = edges[(edges.edge_type == "LOCATED_IN") &
            (edges.to_id.map(byid) == "Chicago")]["from_id"].map(byid)
```
*Answer shape:* 238 located-in records in the stamped slice — venues, institutions, neighborhoods, works. Chicago is the graph's hub (248 relationships in the full master).

## 3. Who was honored at the Soul Train Awards, in which category?

```python
h = edges[edges.edge_type == "HONORED_BY"].copy()
h["honoree"], h["event"] = h["from_id"].map(byid), h["to_id"].map(byid)
h[h["event"].str.contains("Soul Train", na=False)][["honoree", "notes"]]
```
*Answer shape:* honoree + the category carried in the edge notes. 658 HONORED_BY edges across all award events.

## 4. What did the graph's biggest decades look like?

```python
def yr(p):
    y = p.get("year") or p.get("debut_year")
    return y if isinstance(y, int) and 1800 < y < 2030 else None
years = props.apply(yr).dropna().astype(int)
(years // 10 * 10).value_counts().sort_index()
```
*Answer shape:* 733 dated records, concentrated in the 1970s–2010s.

## 5. Which albums and works does a person appear on?

```python
a = edges[edges.edge_type == "APPEARS_ON"].copy()
a["person"], a["work"] = a["from_id"].map(byid), a["to_id"].map(byid)
a[a["person"] == "Beyoncé"]   # replace with any Person record name
```

## 6. The question the graph cannot answer yet — a research task

**"Which Bronzeville institutions opened before 1940?"** Today the slice
returns nothing: Bronzeville exists as a Place record, but its institutions
are wired to Chicago, not yet to the neighborhood, and opening years are
carried unevenly. That gap is real, named, and open — it is exactly the
kind of record-level research filed under **good first issue** in this
repository. Closing it takes primary sources (city directories, the
*Chicago Defender*, building permits), and verified results enter the
graph with the reporter's name on the correction trail.

---

**License:** CC BY 4.0 · **Cite as:** CultureTechLens, *Black Cultural
Knowledge Graph — Starter Queries*, 2026. Concept DOI:
[10.5281/zenodo.23403147](https://doi.org/10.5281/zenodo.23403147)

CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence · Source: CultureTechLens
