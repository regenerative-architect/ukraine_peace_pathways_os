# Peace Pathways OS v4.2 — Test report

**16 October 2026.** The local checks below test source validity and browser interactivity, not legal correctness or live-service availability.

## Executed commands and checks

- `python build.py --check`: JSON Schema Draft 2020-12 validation for eight datasets, semantic integrity and source relationships.
- `python build.py`: regenerated deterministic `index.html` and SHA-256 manifest.
- `python -m unittest discover -s tests -p 'test_*.py' -q`: Python unit/regression suite including deliberate malformed legal references.
- `node --check app.js`: ECMAScript syntax.
- `python tests/browser_legal_atlas_smoke.py`: synthetic Chromium page at desktop 1440×900 and mobile 390×844; 59 records rendered; jurisdiction/topic/text filtering, three export flows, official links, Forge handoff, independent dossier scrollbar and no horizontal overflow/page errors.
- `python tests/browser_regenerative_smoke.py`: retained regeneration module smoke (if executed at release).

## Not independently certified

Full live-site navigation, HTTPS hosting, external law URLs at the exact time of every use, remote database/API uptime, all linked legislation's authenticity or applicability, full WCAG 2.2 AA, origin-persistent IndexedDB state, service-worker update lifecycle, distributed peer transport, security penetration tests, diplomacy feasibility and official adoption.
