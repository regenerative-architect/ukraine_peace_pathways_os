# Verification and test report — Peace Pathways OS v3.0

Baseline: 16 October 2026. Scope is the downloaded code, offline static tool and schema test suite, not actual diplomatic institutional performance.

## Automated static checks

- `node --check app.js`: JavaScript syntax.
- `python build.py --check`: Draft 2020-12 schema verification of all five required JSON files; unique IDs; referential integrity; date format; mandatory role/source links; non-authorized status.
- `python build.py`: validates and generates `index.html` atomically with escaped embedded JSON, with no network requests.
- `python -m unittest discover -s tests -p 'test_*.py' -v`: corruption, missing file, malformed JSON, invalid schema, unknown references, injection escaping and no-output-on-failure tests.

## Browser checks

- `python tests/legacy_smoke_v3.py`: from prior v2 regression, tested 75-profile atlas, independent scrolling, issue-to-case, legal gate, monitoring form, ledger, user source input, backup download, dark theme, mobile keyboard menu and no mobile overflow.
- `python tests/smoke_matrix_v3.py`: 13 accessible pathway entries, track filtering, five-year cooling legality warnings, source-linked pathway memo export, creating a workbench case from a matrix option, sovereignty-specific gate, saved bilateral incentive fields, exported briefing content, AI-supervised mine action dossier, mobile layout and no runtime JavaScript exceptions.
- Screenshot evidence under `tests/desktop_matrix_v3.png`, `tests/mobile_matrix_v3.png`, `tests/desktop_v3.png` and `tests/mobile_v3.png`.

## Not established by these tests

- A live negotiated cessation of hostilities, an OSCE/UN/IAEA mandate or any institution’s agreement, monitoring safety, quantitative operational effectiveness or legitimate implementation.
- A secure institutional collaboration platform. External Trystero Nostr/MQTT peer exchange is opt-in but **not end-to-end compatibility tested across real networks**; it is unsuitable for confidential use without independent review.
- Complete WCAG 2.2 AA certification with assistive technology, multiple language support, or browser/device compatibility beyond tested Chromium and screen sizes.
- A production hosting assessment (HTTPS configuration, CSP, dependency availability, service-worker upgrades and runtime caching across every browser) or a security penetration test.

**Release claim:** a complete buildable and browser-tested static research application, not an institutionally validated operational peacekeeping system. Verified status in the app is always **evidence entered**, not a state endorsement or peace guarantee.

## Local hosting restriction in this build environment

A supplementary `tests/hosted_smoke_v3.py` attempts to test HTTPS-equivalent localhost service-worker registration, reload persistence and offline reconnection. **It was not able to run here:** the Chromium runtime returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` for the local HTTP loopback URL. Direct `file://` navigation was similarly blocked by the container browser policy. The inline Chromium tests passed, but **hosted service-worker behavior and file-origin behavior have not been independently verified in this execution environment**. Run the supplementary test on a local machine where loopback connections are allowed; do not treat this check as passed.
