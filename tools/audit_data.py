#!/usr/bin/env python3
"""Summarize unresolved data-quality markers per work."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
site=json.loads((ROOT/"site.json").read_text())
rows=[]
for work in site["works"]:
    base=ROOT/"works"/work
    battle_files=list((base/"battles").glob("*.py"))
    texts=[]
    for p in battle_files+[base/"refs.py",base/"impact.py"]:
        if p.exists():
            texts.append(p.read_text())
    joined="\n".join(texts)
    rows.append((work,len(battle_files),joined.count("推定"),joined.count("不明")))

print("| work | battles | 推定 | 不明 |")
print("| --- | ---: | ---: | ---: |")
for work,battles,estimated,unknown in sorted(rows,key=lambda r:(r[2]+r[3],r[3]),reverse=True):
    print(f"| {work} | {battles} | {estimated} | {unknown} |")
print()
print("total battles:",sum(r[1] for r in rows))
print("total 推定:",sum(r[2] for r in rows))
print("total 不明:",sum(r[3] for r in rows))
