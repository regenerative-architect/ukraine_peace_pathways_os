# Test report — Peace Accord Workbench v2.0

## Automated / directly inspected on 16 October 2026

- JavaScript parser: `node --check app.js` — passed.
- Inline browser harness: Chromium with Playwright loaded the actual generated `index.html` and **inlined the app.js and styles.css assets** to bypass sandbox browser navigation restrictions; JS executed and UI rendered without uncaught page errors.
- Navigation: all ten links visible; major routes navigated in smoke test.
- Stakeholder atlas: all 75 profiles listed; selecting a profile changes dossier. Independently scrollable dossier measured (`overflow:auto`, scroll height greater than client height) at desktop width.
- Issue dossiers: create a working case from catalog template; title and accountable-owner input submitted.
- Evidence gates: set a gate to `documented`, enter an official-website URL and note, reassess; result **remains UNRESOLVED**, demonstrating that partial documentation does not imply authority.
- Verification protocol: edited and saved text through form control.
- Decision ledger: added a timestamped user note, then verified it in rendered output.
- Sources: 18 baseline cards shown, added a locally marked user-provided source in the page.
- Workspace: JSON backup download event generated with expected filename; theme selection switches DOM theme; exercised settings route.
- Responsive layout: 390-pixel viewport without horizontal overflow. Mobile drawer opens and closes with Escape, updating aria-expanded.
- Screenshots: `tests/desktop_v2.png`, `tests/mobile_v2.png`.

## Not established by testing

- The environment's Chromium policy returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` for **direct file:// and HTTP localhost navigation**, even though inline browser content loaded. Therefore direct-file launch, real browser IndexedDB durability across reload, service worker install/caching, and hosted deep links were **not** fully verified end-to-end in this environment.
- Actual Trystero CDN import, NAT traversal, distributed Nostr/MQTT signaling, remote cross-device peer join and peer message delivery were **not** tested. They require external networks and device/browser combinations.
- No legal, diplomatic, humanitarian, source-accuracy, mandate, or civil-society expert endorsement was sought or obtained.
- Accessibility was checked structurally (semantic controls, focus outline, escape, mobile layout, print CSS, reduced motion) but no exhaustive WCAG 2.2 AA external audit or assistive-technology matrix was completed.

## Repeat locally

```sh
cd peace_accord_workbench
node --check app.js
python tests/smoke_inline_v2.py
python -m http.server 8000
```

Visit `http://localhost:8000` in a browser that permits local HTTP, test cache installation while online, reload disconnected, verify `indexedDB`/storage after refresh, import/export and reset, repeat mobile and print. Then test P2P in a pair of separate real devices over HTTPS; do not claim connectivity from showing a room status alone.

## Rebuilding embedded catalog after changes

The canonical normalized source files are in `data/`. To update the embedded JSON inside `index.html` (for file:// read-only support), run the following inside the root:

```python
from pathlib import Path
import json
root=Path('.')
catalog={k:json.loads((root/'data'/f'{k}.json').read_text()) for k in ['entities','solutions','evidence']}
serialized=json.dumps(catalog,ensure_ascii=False,separators=(',',':')).replace('<',r'\u003c')
(root/'index.html').write_text((root/'index.template.html').read_text().replace('__CATALOG_JSON__',serialized))
```

Do **not** mark prototype outputs as verified institutional outcomes. Independent source checks and professional review are necessary.
