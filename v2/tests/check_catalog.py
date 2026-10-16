#!/usr/bin/env python3
"""Static catalog and version smoke checks. Run from anywhere."""
from pathlib import Path
import json,re,sys
R=Path(__file__).resolve().parents[1]
read=lambda f: json.loads((R/'data'/f).read_text(encoding='utf-8'))
entities,solutions,guides,recipes,evidence=[read(f) for f in ['entities.json','solutions.json','guide-bank.json','pathway-catalog.json','evidence.json']]
assert len(entities)>=70 and len(solutions)>=30 and len(guides)>700 and len(recipes)==len(solutions)
assert len({x['id'] for x in entities})==len(entities)
assert len({x['id'] for x in solutions})==len(solutions)
assert len({x['id'] for x in guides})==len(guides)
eids={x['id'] for x in entities};sids={x['id'] for x in solutions}
for e in entities:
 assert 4<=len(e['solutions'])<=10,(e['id'],len(e['solutions']))
 assert set(e['solutions'])<=sids
 assert e['stakeholderModel']['BATNA'].startswith('UNCERTAIN')
for g in guides:
 assert g['entityId'] in eids and g['solutionId'] in sids
 assert g['solutionId'] in next(x for x in entities if x['id']==g['entityId'])['solutions']
 assert len(g['simpleGuide'])>=4 and len(g['advancedGuide'])>=7 and len(g['phases'])==5
 assert g['budgetPlanning'] and g['conditionalExchange'] and g['goNoGo']
for s in solutions:
 assert len(s['slots'])==4 and s['legal'] and s['verify'] and s['goNoGo']
for source in evidence:
 assert source['url'].startswith('https://') and source['date'] and source['class'] and source['confidence']
html=(R/'index.html').read_text(encoding='utf-8');assert '__SEED_JSON__' not in html
seed=json.loads(re.search(r'<script type="application/json" id="seed-data">([\s\S]+?)</script>',html).group(1))
assert len(seed['entities'])==len(entities) and len(seed['guides'])==len(guides)
assert (R/'manifest.webmanifest').exists() and (R/'sw.js').exists()
print('PASS:',len(entities),'entities,',len(solutions),'solutions,',len(guides),'guides,',len(recipes),'pathway templates,',len(evidence),'citations; embedded seed matches.')
