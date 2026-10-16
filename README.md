# Peace Accord Workbench v2.0 — policy feasibility, not simulated peace

**Independent project:** Foster + Navi / Planetary Restoration Archive (PRA)  
**Baseline of public source review:** 16 October 2026  
**Purpose:** Help researchers, NGOs, educators and policy professionals structure *testable* civilian-protection and conflict-resolution proposals for the Russia–Ukraine war, while exposing missing diplomacy, strategic incentives, legal competence, verification and funding. **The application cannot negotiate a ceasefire, authorize a deal, certify consent or end an armed conflict.**

## One-minute start

1. Unzip the archive. Double-click `index.html` inside the `peace_accord_workbench` folder. Keep `app.js`, `styles.css`, assets and other files alongside it. The embedded stakeholder, issue and source catalog is usable without internet. Browser `file://` storage restrictions vary; export JSON backups after substantive work.
2. Open **Executive brief** to choose a realistic issue track. Select an example or browse the **Issue dossiers** (32 templates). The example button creates a *private, explicitly unverified* case — not a proposed agreement accepted by anyone.
3. Open **Negotiation workbench**; name the competent owner, parties, limitations and next check. Enter each institutional prerequisite as `unknown`, `documented` (link + explanation) or `blocked`. **Documented is user-provided, not verified.** The program never displays an `authorized` or `ready for deployment` outcome.
4. Use **Monitoring & verification** to draft how an incident would be observed, challenged and adjudicated. In the **Decision & risk ledger**, state alternative explanations and what would falsify the proposal's assumptions.
5. Export a markdown briefing memo or JSON backup. Get qualified diplomatic, legal, humanitarian and monitoring reviewers to examine it before any external use.

## Major changes from v1.1

| v1.1 concept | v2.0 implementation |
|---|---|
| XP, achievements, steps completed | Removed altogether; no gamified proxy for peace progress |
| Entity rankings and tiers | Removed from app data and UI; 75 **unverified capability hypotheses** remain |
| Randomized pathway pairings | Replaced with human-defined stakeholders, roles and **explicit unresolved consent** |
| Ordinal likelihood/impact scores | Removed; no fabricated negotiation probabilities |
| Levelled guides / constellation HUD | Removed from interface; old guide catalog preserved only in `/reference` |
| General solution cards | 32 issue dossiers with monitoring, law, dependencies, failures and uncertain costs |
| Generic implementation stages | Feasibility checks, conflicting source positions, authority and command-to-compliance constraints |
| Progress board | Decision, risk, objection and provenance register with dated analyst entries |
| Peer lobby | Opt-in, unmoderated Trystero peer-review room; no automatic syncing |

## Modules and tangible output

- **Executive brief:** separates narrow humanitarian, military-restraint and political-settlement tracks; currently dated public-source anchors.
- **Diplomatic constraints:** decision-right and high-level strategic-feasibility matrix; public-position cross-checks; limits on negotiated concessions, force compliance, verification and ratification.
- **Stakeholder atlas:** original 75 public-interest analytic actor descriptions with authority limits, uncertain BATNA, unverified incentives and separately scrollable dossier. Neither capability nor inclusion proves a role.
- **Issue dossiers:** original 32 research blueprints grouped by eight issue families; each has monitoring need, legal constraints, dependencies, risks and a creation action.
- **Source register:** 18 dated institutional/reported texts and original baseline entries, plus user-created public sources (never independently validated). All available offline; linked sites require internet.
- **Negotiation workbench:** named owner, forum, scope, proposed participants, issue-specific gate register with evidence citations, explicit blockers and memo/JSON export.
- **Monitoring & verification:** editable mandate, definitions, independent baselines, access, incident attribution uncertainty, dispute review, breach response, protection and sustainment.
- **Decision & risk ledger:** timestamped user observations, challenges, proposed steps and falsification tests; manual audit trail.
- **Peer review:** small-group, experimental WebRTC drafts via Trystero (Nostr or MQTT signaling); public room is an *opt-in, unmoderated demonstration*, no identities or guarantees. Peer data is quarantined until manually imported and classified as unverified.
- **Workspace:** IndexedDB first, localStorage fallback, light/dark, explicit JSON import/export, destructive reset requiring two confirmations, and v1.1 saved-plan import. The previous XP ledger does not migrate.
- **Hosted PWA:** HTTPS/localhost service worker with local shell cache after first successful visit; external websites, peer signaling and uncached resources cannot work offline. `file://` does not support service workers.

## Real-world efficacy — criteria and non-claims

Software is not a diplomatic actor. A tool like this might be useful **only when** it improves the quality of a proposal considered by competent entities. A serious assessment should distinguish:

1. **Analytical quality:** Does the dossier name all affected rights, credible veto holders, legal authorizers, counterparty positions, incentives, risks, objective disconfirming evidence and unknowns? Requires external reviewers.
2. **Process traction:** Does an identifiable, authorized institution acknowledge reviewing the proposal? The app does not contact institutions or establish review.
3. **Negotiation traction:** Have the necessary parties acknowledged, negotiated and *actually accepted* the same scope? The app does not know.
4. **Implementation:** Is there a funded, safe, empowered implementation/monitoring mechanism with independently reviewed incident reports?
5. **Outcomes:** Did protection improve under a credible evaluation method (e.g. documented civilian harm/service interruptions, subject to confounders and reporting limitations)? The app does **not** measure or causally attribute peace outcomes.

Never interpret saved proposals, user-entered URLs, local UI status or peer messages as reaching criteria 2–5.

## Important structural constraints

- **Both Ukraine and Russia** must explicitly consent when their respective obligations, military restraint or cross-line humanitarian cooperation are required. A third-party speech or community poll cannot substitute for them. Sectoral, armistice, settlement and diplomacy cases display bilateral gates by default.
- **Sovereignty and international law:** No proposed territorial concession, forced transfer, humanitarian denial or unsafe disclosure becomes lawful by being modeled. The UN Charter and Ukraine's internationally recognized boundaries are relevant governing baselines; legal interpretation belongs to competent specialists.
- **Political economy and strategic constraints:** Wartime leverage, continuity of external support, credible commitments, domestic ratification, sanctions decision rights and shifts in military objectives affect bargaining. Only attributable, dated **strategic-level** sources should be considered here; not tactics, positions or targeting data.
- **Monitoring design:** The OSCE Special Monitoring Mission to Ukraine closed in March 2022. New observation requires an actual mandate, budget, security, access and impartial review, not merely adding “OSCE” as an actor.
- **Neutral intermediaries:** The ICRC may support humanitarian exchanges, family links and passage subject to party consent and its own operational remit. It is not automatically assigned a proposed role.
- **Expert judgment:** All agency, cost, technical, legal, capacity and timelines remain provisional until externally checked. Missing facts remain **unknown**, not a numerical confidence score.

## Site structure

```
peace_accord_workbench/
  index.html                 Embedded catalog + accessible shell (works under file://)
  index.template.html        Source shell with __CATALOG_JSON__ build injection point
  app.js                     Routes, views, gates, workspace, exports, optional peer review
  styles.css                 Responsive, accessible and print-friendly styles
  manifest.webmanifest       Hosted PWA metadata
  sw.js                      Versioned same-origin offline shell cache
  assets/icon-*.png          Locally hosted icons
  data/entities.json         Source stakeholder catalog with rank/tier removed
  data/solutions.json        Source issue catalog with guide/completion material removed
  data/evidence.json         Frozen curated and reported source ledger
  reference/                Preserved v1.1 guide bank and pathway catalog, not loaded
  RESEARCH_PROTOCOL.md       Review protocol for externally credible use
  CASE_STUDIES.md            Two current, non-authorized feasibility examples
  NEGOTIATION_FRAMEWORK.md   Strategic, legal and implementation checklist
  ATTRIBUTIONS_AND_LICENSES.md
  TEST_REPORT.md
  tests/smoke_inline_v2.py   Playwright DOM/interaction smoke tests
  tests/*.png                Captured reference screenshots
```

For later changes to `data/*.json`, rerun the small build snippet from `TEST_REPORT.md` to regenerate the embedded catalog in `index.html`. This is deliberate to retain `file://` read-only accessibility without runtime fetches. Use `python -m http.server 8000` from this directory for hosted-local testing, if network policy permits, and deploy static files over HTTPS for PWA and WebRTC.

## Source currency, neutrality and privacy

The reference baseline is date-frozen to **2026-10-16** and not continuously updated. Open cited sources to verify wording and subsequent events. Reported Russian or Ukrainian positions are **attributed statements**, not independently proven intentions. The app advocates lawful civilian protection, sovereign agency and non-coercion; it does not endorse a government party's military goals, and does not imply neutral legal equivalence between invasion and defense.

No app telemetry, accounts, personal analytics, external search ingestion, covert data transmission or automatic institutional outreach exists. Optional external search links and P2P network access are explicit actions. Public community rooms are not appropriate for confidential work. Never enter names/addresses of endangered individuals, prisoner identifiers, confidential diplomatic channels, sensitive sites or locations, tactical force information, or classified material.

**Zero-Harm / Anti-Inversion:** This edition prioritizes falsifiability over persuasion, blocks inferred consent, leaves unresolvable prerequisites visible, avoids strategic targeting workflows, treats incident data as potentially contested, and requires manual export and human validation. These reduce but cannot eliminate misuse risk.

## Limitations and diagnostics

- No live negotiation or combat status ingestion; source claims expire in practical relevance.
- No identity authentication, access control, moderated P2P community or verified cross-network peer connection. Trystero uses third-party CDN and public signaling when voluntarily joined; direct WebRTC may fail without TURN.
- No automatic event scraping, threat detection, forecasting, grant matching, funding commitment or external communication. “Documented” only means a local evidence URL and note were entered.
- Tested: JavaScript syntax; Playwright inline-DOM smoke interactions, responsive rendering and download event; see `TEST_REPORT.md`. The environment's browser navigation policy blocked direct `file://` and localhost page navigation, so full HTTP/PWA and cross-device runtime are **not represented as passed**.
- This is a research prototype, not a deployable conflict-mediation platform. Real institutional use requires specialist co-design, audited data, secure hosting/identity, protocol testing, external review and consent.

MIT license applies to original and new application code; other parties' research and brands remain attributed, not relicensed. Consult `ATTRIBUTIONS_AND_LICENSES.md`.
