#!/usr/bin/env python3
"""Peace Pathways OS v3: deterministic offline build, JSON Schema + semantic verification.

Commands:
  python -m pip install -r requirements.txt
  python build.py --check        # fail fast; never modify files
  python build.py                # check all five core data files, then atomically compile index.html

No network, third-party deployment or AI calls are performed by this build script.
"""
from __future__ import annotations
import argparse
from datetime import date
import json
import os
from pathlib import Path
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
CORE=('entities','evidence','guide-bank','pathway-catalog','solutions')


def _read_json(path:Path):
    if not path.is_file():
        raise ValueError(f'MISSING REQUIRED FILE: {path.relative_to(ROOT)}')
    try:
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except (UnicodeError,json.JSONDecodeError) as exc:
        raise ValueError(f'INVALID JSON in {path.relative_to(ROOT)}: {exc}') from exc


def _need_unique(records,label):
    seen=set()
    for n,record in enumerate(records):
        key=record['id']
        if key in seen:raise ValueError(f'{label}[{n}] duplicate id {key!r}')
        seen.add(key)
    return seen


def _semantic(data):
    errors=[]
    def err(s):errors.append(s)
    actors=_need_unique(data['entities'],'entities')
    evidence=_need_unique(data['evidence'],'evidence')
    solutions=_need_unique(data['solutions'],'solutions')
    _need_unique(data['guide-bank'],'guide-bank')
    catalog=data['pathway-catalog']
    tracks=_need_unique(catalog['trackDefinitions'],'trackDefinitions')
    phases=_need_unique(catalog['phases'],'phases')
    _need_unique(catalog['pathways'],'pathways')
    if tracks != {'t1','t2','t3'}:err('Exactly three defined tracks t1,t2,t3 are required')
    if phases != {'p1','p2','p3'}:err('Exactly three defined phases p1,p2,p3 are required')
    for s in data['solutions']:
        sid=s['id']
        if s['trackId'] not in tracks or s['phaseId'] not in phases:err(f'{sid}: invalid track/phase reference')
        for src in s['references']:
            if src not in evidence:err(f'{sid}: missing evidence id {src}')
        ids=[x['id'] for x in s['metrics']]
        if len(ids)!=len(set(ids)):err(f'{sid}: duplicate metric ids')
        if not s['status'].startswith('HYPOTHETICAL'):err(f'{sid}: status must clearly remain hypothetical')
    solution_lookup={s['id']:s for s in data['solutions']}
    for g in data['guide-bank']:
        if g['entityId'] not in actors:err(f"{g['id']}: unknown entityId {g['entityId']}")
        if g['solutionId'] not in solutions:err(f"{g['id']}: unknown solutionId {g['solutionId']}")
    for p in catalog['pathways']:
        for sid in p['solutionIds']:
            s=solution_lookup.get(sid)
            if s is None:err(f"{p['id']}: invalid solutionId {sid}")
            else:
                if (s['trackId'],s['phaseId'])!=(p['trackId'],p['phaseId']):err(f"{p['id']}: track/phase disagrees with {sid}")
        for ref in p['sourceIds']:
            if ref not in evidence:err(f"{p['id']}: unknown evidence id {ref}")
        available_metric_ids={m['id'] for sid in p['solutionIds'] if sid in solution_lookup for m in solution_lookup[sid]['metrics']}
        for mid in p['metricIds']:
            if mid not in available_metric_ids:err(f"{p['id']}: unknown metric id {mid}")
    # Defensible data checks: dates must parse, URLs cannot be javascript schemes; no live telemetry URLs.
    for source in data['evidence']:
        try:date.fromisoformat(source['date'])
        except ValueError:err(f"{source['id']}: invalid calendar date")
    try:date.fromisoformat(catalog['asOf'])
    except ValueError:err('pathway-catalog: invalid asOf date')
    return errors


def validate():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise ValueError('JSON Schema dependency missing. Run: python -m pip install -r requirements.txt') from exc
    data={}; problems=[]
    for name in CORE:
        path=ROOT/'data'/f'{name}.json'
        schema_path=ROOT/'schemas'/f'{name}.schema.json'
        try:
            document=_read_json(path)
            schema=_read_json(schema_path)
            Draft202012Validator.check_schema(schema)
            checker=Draft202012Validator(schema,format_checker=FormatChecker())
            found=sorted(checker.iter_errors(document),key=lambda e:(list(map(str,e.absolute_path)),e.message))
            for e in found[:50]:
                context='.'.join(map(str,e.absolute_path)) or '(root)'
                problems.append(f'{name}:{context}: {e.message}')
            if len(found)>50:problems.append(f'{name}: {len(found)-50} further schema violations')
            if not found:data[name]=document
        except (ValueError, OSError) as exc:
            problems.append(str(exc))
    if not problems:
        try:problems.extend(_semantic(data))
        except (ValueError,KeyError,TypeError) as exc:problems.append(f'Semantic integrity error: {exc}')
    if problems:raise ValueError('\n  - '+'\n  - '.join(problems))
    return data


def build(data):
    # Keep the legacy 747 large guides in data/guide-bank.json; avoid making every mobile
    # visitor download 5MB of historical content on initial navigation.
    catalog=data['pathway-catalog']
    payload={'version':'3.0.0','asOf':catalog['asOf'],
             'entities':data['entities'],'evidence':data['evidence'],
             'solutions':data['solutions'],'pathways':catalog['pathways'],
             'tracks':catalog['trackDefinitions'],'phases':catalog['phases']}
    text=json.dumps(payload,ensure_ascii=False,separators=(',',':'),allow_nan=False)
    # Inside a script[type=application/json], raw closing tags must not appear.
    text=text.replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    template_path=ROOT/'index.template.html'
    if not template_path.exists():raise ValueError('MISSING REQUIRED FILE: index.template.html')
    template=template_path.read_text(encoding='utf-8')
    if template.count('__CATALOG_JSON__')!=1:raise ValueError('Template must contain exactly one __CATALOG_JSON__ marker')
    document=template.replace('__CATALOG_JSON__',text)
    target=ROOT/'index.html'
    with tempfile.NamedTemporaryFile('w',dir=ROOT,prefix='.build-',suffix='.html',encoding='utf-8',delete=False) as f:
        tmp=Path(f.name);f.write(document);f.flush();os.fsync(f.fileno())
    try:os.replace(tmp,target)
    finally:tmp.unlink(missing_ok=True)
    return target,len(document.encode('utf-8'))


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Validate source data and references without compiling')
    args=parser.parse_args(argv)
    try:
        data=validate()
        print(f"PASS: schema + semantics; {len(data['entities'])} actors, {len(data['evidence'])} evidence, {len(data['guide-bank'])} guides, {len(data['solutions'])} solutions, {len(data['pathway-catalog']['pathways'])} pathways")
        if not args.check:
            path,n=build(data)
            print(f'BUILT {path.relative_to(ROOT)} ({n:,} UTF-8 bytes) · no network requests')
        return 0
    except Exception as exc:
        print(f'BUILD FAILED: {exc}',file=sys.stderr)
        return 1

if __name__=='__main__':sys.exit(main())
