# Peace Pathways OS v3.0 — multi-track diplomacy decision support

**Independent research software. Neither an official peace process nor a live security-monitoring system.**

This is a complete, static, open-source workspace for analysts, humanitarian researchers and civic institutions to **evaluate conditional mechanisms** concerning the Russia–Ukraine conflict. It is designed to reject unsupported assertions of authority, party consent, safety, enforcement or institutional participation. It cannot negotiate a ceasefire, enforce international obligations, direct international bodies, or make military decisions. The reference evidence snapshot is **16 October 2026**; the current legal and geopolitical situation must be reviewed before external use.

## Run it

1. Open `index.html` directly for an offline-capable reference catalog, research cases, printable issue dossiers and local backups. No Python or server is required to read the built site.
2. For a hosted PWA, serve the entire directory under **HTTPS** (or `http://localhost`), e.g. `python -m http.server 8080` from the repository root and visit `http://localhost:8080`. Install/cache requires an initial successful online visit; live source URLs and optional peer networking **never** work offline.
3. To change the data, install the Python schema checker and rebuild:

```bash
python -m pip install -r requirements.txt
python build.py --check
python build.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

`build.py` checks **all five required files** and their individual Draft 2020-12 JSON schemas **before** building: `data/entities.json`, `data/evidence.json`, `data/guide-bank.json`, `data/pathway-catalog.json`, and `data/solutions.json`. It also checks identifier uniqueness, relationships and reference integrity and atomically writes `index.html`. It makes **no network calls**. If any JSON is absent, malformed or semantically broken, compilation fails without replacing the previous built file.

The complete code and data are provided: no omitted source files, stub APIs, live military data feeds, or project-specific cloud accounts. A compiled `index.html` is included so the application can be used without installing Python.

## Features

| Module | Function | What it does **not** imply |
|---|---|---|
| Multi-track pathway matrix | Three tracks, three conditional phases, 13 high-detail pathways, source IDs, veto points, risk mitigations and independent outcomes | A diplomatic offer was accepted |
| 45 issue dossiers | 32 inherited issue categories and 13 newly specified bottlenecks with steps, measures, baselines, cautions | Funds, mandates, access or equipment exist |
| 75 stakeholder profiles | Searchable institutional capability / authority hypotheses | That institutions participate or endorse this work |
| Bargaining analysis | Locally record public/source-based outside options, constraints, reciprocity, confidence problems and veto scenarios | Quantified battlefield advantage or real private intent |
| Negotiation workbench | Document a case and evidence references against applicable **hard** authority gates | That an entered link verifies an actual agreement |
| Verification protocol | Scope, observables, safe access, dispute intake, failure, remediation, legal basis | IAEA, OSCE or UN enforcement authorization |
| Decision and risk register | Date-stamped notes, rejected hypotheses and exportable memos | Independently validated claims |
| Offline/local autonomy | Static references, browser local state, backup import/export, no accounts | Live updates, cross-device sync, or peer access offline |
| Optional peer review | Explicit Join and explicit Send of limited draft summary; network-dependent, unmoderated | Identity verification, confidential collaboration, guaranteed availability |

**Design rule:** No numerical “likelihood of peace,” points, XP, progress ladders or gamification. Blockers remain blockers, not penalties that can be offset by accumulating other scores.

## Three analytical tracks

- **Track 1: security and civilian de-escalation.** Model monitor mandates, non-sensitive sensor evidence, a **negotiable 30 km artillery-separation hypothesis**, serious medical transfers and civilian protection, nuclear power safety and shipping corridors. The old OSCE SMM closed in 2022. New missions require a lawful new mandate, separate party consent and safe access. IAEA assesses nuclear safety but does not unilaterally enforce a perimeter. Never upload live drone telemetry or vessel routing information.
- **Track 2: governance, law and rights.** Any free economic or public service zone is conditioned on Ukrainian sovereignty, authorization and lawful administration. UN transitional governance is only a **scenario**, not an operational institution in Ukraine. The proposed five-year cooling period is an assessment variable, **not a lawful warrant** for occupied-territory referenda. Minority/language rights remedies must be assessed against current competent jurisdictions; the ECHR lacks general jurisdiction over post-16 September 2022 Russian acts.
- **Track 3: civilian reconstruction.** The Ukraine/Moldova grids were already synchronized with continental Europe in March 2022: the focus is resilience, not initial connection. EU windfall revenues from immobilized assets have pre-existing earmarked legal uses; do not reassign them in an invented trust. AI prioritizes human-accredited mine survey but does **not** clear mines autonomously or certify land safe.

## Data contracts and project tree

```text
ukraine_peace_pathways_os/
  index.html                  precompiled working single-page static app
  index.template.html         static shell and non-JS documentation
  app.js                      semantic routes, analysis, IndexedDB, exports, opt-in peers
  styles.css                  accessible responsive / print styles
  build.py                    fail-fast schema+reference checks; atomic compilation
  requirements.txt            pinned-major JSON Schema dependency
  data/
    entities.json             75 actor/authority dossiers
    evidence.json             29 curated source records with dated provenance
    guide-bank.json           747 compact, non-gamified actor × issue review prompts
    pathway-catalog.json      3 tracks, 3 phases, 13 conditional institutional pathways
    solutions.json            45 operationally-structured intervention candidates
  schemas/                    Draft 2020-12 schemas for all 5 required JSON files
  assets/                     local icons
  sw.js                       versioned same-origin shell caching (hosted only)
  manifest.webmanifest        PWA metadata
  reference/legacy_guide_bank_v1_1.json.gz
                               complete unmodified v1.1 guide bank, provenance only
  tests/                      browser smoke, build integrity tests, screenshots
  NEGOTIATION_FRAMEWORK.md    political-strategic gate model
  RESEARCH_PROTOCOL.md        analyst research and source review
  CASE_STUDIES.md             example issue applications
  LEGAL_LIMITS.md             mandate, law and safety analysis
  TEST_REPORT.md              tested scope vs unverified external deployment
  ATTRIBUTIONS_AND_LICENSES.md
  LICENSE
```

`index.html` embeds the 45 active dossiers and matrix so **file://** operation does not require cross-origin JSON fetches. The 747 guides are accessible directly in `data/guide-bank.json`, and their full original v1.1 narratives remain in gzip under `reference/` (excluded from the browser's initial download). Run `python -m gzip -d` on a copy of the archived gzip or Python's `gzip.open()` to inspect the historical reference. The legacy historical data are **not** treated as verified institutional policy.

## Data schema / intervention example

Every active `solutions.json` item has `trackId`, `phaseId`, high-level `executionSteps` with `owner`, `action`, and `acceptanceEvidence`; `metrics` with `unit`, `definition`, **unverified** `baseline`, a **proposed** target and validation method; `risks` with an explicit stop/review trigger; linked `references` and an unverified `mandateGate`. A pathway in `pathway-catalog.json` references those issues, adds consent/veto points, incentive tests and lawful fallbacks. `build.py` ensures referenced IDs resolve.

When adding a solution, avoid claiming actual agreement, funding or access. Targets are **design criteria**, not forecasts or guarantees. Do not model tactical assets, current force positions, protected-person identities, exploitable nuclear safety weaknesses or live shipping details.

## Research workflow

Select **Multi-track pathway matrix → specific mechanism → Open as research case → Bargaining matrix → Prerequisite register → Monitoring protocol → Decision/risk log → Export memo**. Enter public sources only when they establish the exact proposition; document alternative interpretations. A status of “documentation recorded” still calls for external independent review and **never** means authorized or executable.

For imported v2 data, `IndexedDB` workspace key `peace-accord-workbench-v2` is intentionally retained. The case normalizer adds the new incentive section without discarding existing cases. v1.1 proposals can still be imported as **unverified** cases; game state is not migrated. Back up before moving or resetting browser profiles.

## Threat model and zero-harm limits

The app's data stores are under the browser's origin and are **not encrypted**. Anyone with your unlocked device or access to that browser profile may view them. Never store classified material, identifying data about detainees/children, unannounced contacts, raw military locations, real-time vessel/flight/drone tracking or confidential draft agreements. Browser local storage and JSON downloads are not secure government document systems.

The browser's optional P2P room fetches Trystero libraries from a third-party CDN *only after the Join button is clicked*; signaling and peers may learn connection metadata. It is unmoderated, has no identity verification or built-in audit security and should be **disabled or independently security-reviewed for official institutional work**. Offline research requires neither peer support nor online accounts. No hidden telemetry is used.

All code is independent public-interest research. Legal, humanitarian, cybersecurity and subject-matter experts must review proposals before real-world use. There is no “zero-risk” technology guarantee. See `LEGAL_LIMITS.md`.

## Deployment checklist

- Run `python build.py --check` and `python build.py`; run browser and corruption tests.
- Deploy **entire repo** or at least `index.html`, `app.js`, `styles.css`, `manifest.webmanifest`, icons and `sw.js`; keep the full `data/` and `schemas/` in the public repository for reproducibility.
- Use HTTPS, a restrictive CSP compatible with the optional remote P2P adapter if enabled, and appropriate cache/privacy policies; no cookies are necessary. Consider disabling public P2P on sensitive institutional deployments.
- Revalidate sources as of the actual briefing date. The static ledger is not automatically current.
- When changing any static shell files, increment the cache version in `sw.js`; otherwise old clients may retain prior assets.
- Inspect `TEST_REPORT.md` for tested versus still-untested environmental dependencies.

Copyright © 2026 Foster + Navi / Planetary Restoration Archive. MIT-licensed project code; see source and third-party credits.
