# v4.5 — Financing × Legislative Gates (2026-10-16)

- Adds `data/finance-law-bridge.json` and a strict schema: 60 curated, nonbinding actor × regenerative-option research links with explicit legal research gates.
- Adds interactive route with four filters, 218 provisional jurisdiction reviews, source-backed right inspector, independent scrolling, Markdown/CSV/JSON exports, and linked legal/funding and Pathway Forge handoffs.
- Adds Finland and India official legislative repository links to the 28-jurisdiction legal directory, bringing it to 30 jurisdictions / 67 documents.
- Adds schema and reference checks rejecting unknown actors, laws and options; rejects invented permission statuses; enforces stage consistency and full coverage of funding records.
- Adds 11 new Python tests (53 total) and desktop/mobile browser smoke scripts. Retains original v4.4 application modules, data and local-case persistence.
- Explicitly retains uncertain or not-assessed classifications. Does **not** render sanctions clearance, proof of funds, legal opinions or accepted peace commitments.

---

# v4.4 — Evidence-graded conflict financing & support atlas (2026-10-16)

- 30 public-source-backed financing, weapons-transfer, economic or proposed-participation dossier records, 22 dated sources, 78 stakeholder actors and seven differentiated funding/support channels.
- New research route with separate scrollable list and right-side dossier, source URLs, role/status filters, source-anchored Markdown, CSV and Pathway Forge handoff.
- Funding roles integrated inside existing Stakeholder Atlas dossiers, with opt-in 'show mapped actors' filter.
- Clear differentiation between Russian state war budget, transfers supporting Russia, lawful defence of Ukraine, civilian-recovery funding, financial intermediaries, indirect market exposure and unverified prospective partners.
- Budget allocations, loans, guarantees, actual payouts, arms-transfer trend indicators and market revenue are recorded as distinct accounting classes, not summed.
- Versioned Draft 2020-12 funding schema; build rejects broken actor/source references, duplicate profiles, future-dated source snapshots, invalid categories and unverifiable approval states.
- Offline embedded metadata, standalone source data precached for hosted PWAs, 42 automated unit tests and desktop/mobile smoke checks.
- No new integrations, authenticated funding evidence, bank access, institutional endorsements or automatic follow-up monitoring.

# v4.2 — Legal & Institutional Documentation Atlas (2026-10-16)

- Added `data/legal-atlas.json`: 59 curated public official-source URLs from 28 national/supranational/international jurisdictions, with instrument/repository/guidance distinctions, reference dates, language, legal caveats, subjects, and current-law recheck flags.
- Added `schemas/legal-atlas.schema.json` with Draft 2020-12 validation; build.py validates mandatory records, IDs, HTTPS sources, jurisdiction relationships, and review dates, and embeds offline metadata in the compiled app.
- Added searchable/filterable **Legal & documentation atlas** route with independently scrolling right inspector, direct publisher links, Markdown/JSON exports, and Pathway Forge handoff.
- Retained all existing diplomacy/demilitarization/finance/guide/negotiation features and original schema checks.
- Fixed mobile navigation drawer scrolling when route registry extends beyond viewport.
- Added `LEGAL_DOCUMENTATION_GUIDE.md` explaining due diligence, legal effect, language and applicability limitations; updated deployment/test documentation and service-worker precache.
- Source titles and notes are available offline; linked full texts are online-only and must be freshly confirmed. No validity, official endorsement, sanctions clearance or legal compliance claim.

# v4.1 — Conflict-to-Regeneration expansion (2026-10-16)

Added 14 finance and ecological recovery alternatives with explicit funder categories, cooperation gates and law/verification/financial classifications. Added independently scrollable screen and exportable expert review packets. Added schema, build semantic validation, and new evidence from SIPRI/World Bank/UNDP/Council of Europe/Ukrainian DREAM. Maintained all v4 components, including independent Forge inspector scrolling.

# Release notes — v4.0.0 (16 October 2026)

- **Merged v3 base** (all stakeholder, issue, negotiations, monitoring, decisions, casework, peer-adapter and institutional policy content) with **v2 Pathway Forge** concepts and dependency validation.
- Added Pathway Forge as a native route: regenerate eight combinations; select independent reviewer type, problem and pathway; open nine evidence-gated prompts; copy and export; use desktop sticky **independently scrolling right inspector**, mobile vertically stacked independent scroll inspector.
- New conditional demilitarization policy design library with 10 pathways: civilian infrastructure, nuclear safety, ceasefire monitoring, heavy weapons separation *hypothesis*, humanitarian exchanges, maritime safety, arms transparency, mine action, voluntary reintegration and ecological reconstruction.
- Eight independent reviewer audience profiles and exportable review packets; never imply partnership, support or participation.
- Integrated all 747 preserved guide templates into offline search with paged result display.
- Added explicit machine-readable solution dependency references, cycle detection and cross-audience/portfolio integrity checks.
- Added v2 backup import conversion for notes/bookmarks, retaining unverified status and user confirmation; v3 native case persistence remains.
- Made public peer signaling an **explicit user choice**, not the default room. Peer identities remain unverified; confidential data not safe to share.
- Enabled mobile in-drawer search, build SHA-256 manifest, six JSON Schema checks, expanded test coverage to 16 tests and added GitHub Actions validation.
- No official partnerships, mandates or negotiated terms are represented or claimed.
