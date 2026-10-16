# Peace Pathways OS v4.1 — Test report

Tested: 16 October 2026. This report distinguishes observed local behavior from untested deployment conditions.

## Executed validations

- `python build.py --check`: PASS, all seven Draft 2020-12 JSON datasets and semantic references.
- `python build.py`: PASS, generated 1,210,720-byte `index.html` (below 2 MB).
- `node --check app.js`: PASS, JavaScript syntax.
- `python -m unittest discover -s tests -p 'test_*.py' -q`: PASS, 20 unit/regression tests, including data dependencies, schema contract, atomic compilation, and regenerative source/funder link integrity.
- `python tests/browser_regenerative_smoke.py`: PASS in headless Chromium at 1440×900 desktop and 390×844 mobile using a self-contained test-document injection (not an HTTP host).
  - Both views: 14 alternatives rendered; funder and stage filters operated; selection worked; Markdown review brief downloaded; panel had independent scrollbar; panel scrollTop changed; no JavaScript page errors; no horizontal viewport overflow.
  - Navigation from selected alternative to Pathway Forge populated the Forge question with its legal constraints and generated the normal nine-stage chain.
  - Pathway Forge inspector remained independently scrollable on desktop and mobile.

## Limits and remaining release gates

- Hosted HTTPS navigation, service worker precache lifecycle, full origin-persistent IndexedDB restore, peer-to-peer transport across independent networks, comprehensive WCAG 2.2 AA and penetration testing were **not** performed in this release.
- Proposed financing instruments are not actual grants; no funds were transferred, pledged, matched or approved by any institution.
- All 14 regeneration alternatives are policy research only, not official proposals adopted by parties. The provided sources establish context but do not guarantee feasibility.
- Review sanctions, legal instruments and conditions against current authoritative primary sources before using a review packet in any live professional decision.
