# v4.5 Test report — 2026-10-16

- `python build.py --check` — PASS: 11 JSON datasets validated, cross references intact.
- `python -m unittest discover -s tests -q` — **53 tests passed**.
- `python build.py` — PASS; compiled `index.html` under 2 MB.
- `node --check app.js` — PASS.
- `python tests/browser_finance_law_smoke.py` — PASS desktop/mobile (60 links, filters, source links, 3 downloads, independent inspector scroll, legislative matrix/funder/Forge handoffs, no console page errors or horizontal overflow).
- `python tests/browser_funding_smoke.py` — PASS desktop/mobile.
- `python tests/browser_regenerative_smoke.py` — PASS desktop/mobile.
- Live hosted HTTPS, inter-peer room transport, external legislation availability and professional legal review are **not tested**.

---

# V4.4 test report — 16 October 2026

- `python build.py --check`: PASS, ten Draft 2020-12 JSON datasets; semantically crosslinked source and actor IDs.
- `python build.py`: PASS; generated HTML 1,362,682 bytes (under the 2 MB project limit).
- `node --check app.js`: PASS.
- `python -m unittest discover -s tests`: PASS, 42 tests including 8 new funding negative/contract cases.
- `python tests/browser_funding_smoke.py`: PASS, desktop (1440×900) and mobile (390×844), Chromium using offline-injected project HTML/CSS/JS. Checks list count, status/channel/query filters, source display, stakeholder dossier navigation, Markdown/CSV downloads, independent funding-panel scroll, and Forge handoff; zero page errors in those tests.
- Prior comprehensive v4.3 UI, live peer signalling and production-host HTTP/PWA security were **not** fully retested for this release. Deployment to any real institution remains subject to separate verification and security/accessibility audit.
