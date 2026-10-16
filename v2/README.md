# PEACE PATHWAYS OS — Collaborative Systems Lab

**Release:** 1.1.0 | **Source fact freeze:** 16 October 2026 | **Attribution:** Foster + Navi / Planetary Restoration Archive

An independent, offline-first educational web OS for analyzing lawful, civilian-centered collaboration pathways that might help end the Russia–Ukraine war. It **does not** represent Ukraine, Russia, the UN, or any government; it cannot authorize ceasefires or contact institutions automatically.

## One-minute start

1. **Offline, simplest:** unzip, double-click `index.html`. The atlas, all solutions, tailored guides, pathway forge, data export and local learning work without a server or internet. Local browser storage may be restricted in private/file modes; always export a backup.
2. **Hosted/PWA:** put the entire folder on a static HTTPS host (or run `python -m http.server 8080` from this folder and open `http://localhost:8080`). Open it once online to install the service worker. After the service worker has activated and cached the shell, reopen the site offline. `file://` cannot use service workers.
3. **Community lobby (explicit opt-in):** host on HTTPS or localhost; open **Collaboration** and click **Join community**. Every visitor uses the prefilled public code `peace-pathways-community-v1` and Nostr signaling by default, without needing an invitation or account. A peer count of zero means no verified connection, even if the console says “Waiting.” Do not send private information in this public, unmoderated room; sharing a saved proposal remains a separate, reviewed opt-in action. For a smaller private session, click **New private room**, optionally set a passphrase, then share the invitation URL with collaborators. Real external networks and signaling services are required.

## What is actually implemented

| Module | Functions |
|---|---|
| Overview | Evidence freeze, baseline, four portfolios and dashboard |
| Entity atlas | 75 ranked potential actors/groups, searchable capabilities, constraints, BATNA uncertainty and tailored banks; independently scrollable right-side profile/solutions pane, including keyboard and mobile access |
| Solutions bank | 32 categorized intervention designs, legal, monitoring, first-move, risk and measurable outcomes |
| Pathway forge | 4+ complementary seats; anchor any entity; pin up to five more; vary a goal and 3–16 assignments; **Regenerate** rotates partner assignments while preserving chosen constraints and indicates when no distinct options are available; inspect, save, export JSON |
| Skill constellation | 747 entity×solution guides with simplified and advanced tracks, checked learning steps, phased milestones and conditional reciprocity |
| Collaboration | **One-click, public community room prefilled by default**; Trystero v0.26.0 with **Nostr by default**, optional MQTT strategy, loaded only after explicit Join; private-room creation, optional secret, invite URL, confirmed peers, reviewed outgoing and quarantined incoming drafts, optional TURN |
| Evidence & safeguards | Dated source ledger, obstacle map, 24-month premortem, legal restrictions and escalation stop rules |
| Settings & portable data | IndexedDB with localStorage fallback, light/dark, EN/partial UK and RU navigation, JSON backup/restore, schema validation, reset confirmation |
| Hosted PWA | Versioned service worker; same-origin static precache after successful HTTPS/localhost install. External Trystero/CDN never cached or claimed offline. |

The complete 747-guide catalog is **embedded in** `index.html` so opening it under `file://` does not require fetching JSON. External JSON duplicates are furnished for machine-readable reuse and future versioned updates.

## Data directory

- `data/entities.json` — 75 entities, tier, capabilities, potential authority, risks, inferential stakeholder model, own solution IDs.
- `data/solutions.json` — 32 intervention designs, measures, staged actions, evidence thresholds, costs **uncertain**, conditional exchange, failure mode, legal review.
- `data/guide-bank.json` — 747 complete entity-specific advanced and simple guides.
- `data/pathway-catalog.json` — 32 collaboration recipes and complementary seat requirements.
- `data/evidence.json` — cited sources with dates, confidence, class and next-use implications.
- `data/seed.json` — same complete catalog in a single JSON object.

## Collaborative pairing diagnostic (important)

Trystero's public Nostr relays (or MQTT brokers when both parties select MQTT) are used only for **signaling** and are an external dependency. Signaling is distinct from WebRTC connection establishment. Even with the same room, carrier-grade NATs, restrictive firewalls, service-worker/network interference, relay policies and lack of TURN may prevent two distant devices from joining.

1. Verify both browsers load **the same hosted app version** and use the exact same **room code** (case-sensitive) and signaling strategy. The public room defaults to `peace-pathways-community-v1` and has **no passphrase**. Both devices must press Join; private rooms additionally require matching optional passphrases.
2. Confirm browser online, and try two tabs or two devices on the same network before crossing networks. The app reports a confirmed peer only after `onPeerJoin`. A single global P2P mesh is **not scalable or moderated**; the community room is an experimental small-group discovery lobby rather than a permanent public forum. At scale, deploy an operated moderated service with explicit identities and abuse controls.
3. When peers fail across networks but succeed locally, provision a legitimate TURN server, and enter its ephemeral `turn:` or `turns:` URL, username and credential on **both** devices **before pressing Join**. Trystero's `turnConfig` adds TURN to its default STUN servers. Credentials are never persisted by the app.
4. If CDN module loading fails, inspect Content Security Policy, browser network console, blocked public relay access or hosting constraints. Static catalog and local backups remain usable; the app does not invent a connection. Public lobby joining reveals network information to some peers and intermediary services; it must remain opt-in.
5. Production networks require operated, dependable infrastructure with a reviewed abuse policy; public relays are unsuitable for guaranteed service. Never use this application for sensitive private-person or protected ICRC information.

Official technical documentation: https://trystero.dev/docs/connections/ and https://trystero.dev/docs/signaling-strategies/ . No connection across separate networks is promised or claimed tested merely because the UI is functional.

## Interpreting the systems model

- **VERIFIED FACT**: a dated statement supported by a sourced record; context can still change.
- **REPORTED EVENT / OFFICIAL POSITION**: attributed claim; read the original source.
- **INFERENCE**: an analytical model, not an actor's stated private intentions.
- **PROPOSAL / HYPOTHETICAL PATHWAY**: no actor is presumed to consent, fund or participate.
- **LEARNING STEP**: checked only on your own device; neither combat casualties nor peace progress are scored from personal course completion.

**Pathway ratings** are illustrative ordinal interaction heuristics using capabilities, portfolio relevance, presence of direct parties and potential verification. They are **not** probabilities or evidence of acceptance. The entity tiers are strategic guesses needing continuous external verification. Each guide includes a legal review gate, independent metric, safety stop rule, and a high-uncertainty cost band. Specialist legal and technical review is mandatory before any real action.

## Limitations

- News and combat figures are **frozen as of 2026-10-16**. No automatic crawling, data connector, background monitoring, outreach or diplomacy.
- Named potential partners do not endorse this tool. No personal identity authentication or moderation is provided for P2P rooms. The **public community room code is intentionally known** and any compatible visitor may join; anyone holding a private code (plus optional passphrase) may potentially join a private room. The optional passphrase is never embedded in an invite URL.
- The "Earth Intelligence Engine" button is a compact local analytics/learning HUD, **not** a real-time external Earth-observation or intelligence feed. Future integration requires a lawful, authorized API and explicit user consent.
- English is the canonical research language. Ukrainian and Russian only translate the navigation labels; content falls back transparently to English.
- No durable network queue or cross-device synchronization. P2P proposals are only transmitted live when sender opts in; the receiving person must review and accept. Conflicts and merge choices remain manual.
- Exact cost estimates, real-time binding diplomatic positions, confirmed ceasefire compliance, personalized legal advice and guaranteed cross-network peer connection are outside this static bundle's capabilities.
- No live operational military positions, human targeting or sensitive individual-level records should be entered.

## Security, privacy, deployment

- All personal learning state and saved proposals are in IndexedDB first, with an explicit backup/export and localStorage fallback. No analytics, cookies, covert transmission or hidden telemetry.
- Peer draft payloads are bounded and sanitized with escaped text on display. TURN credentials remain session-only, in memory, and are not in backup JSON.
- Serve over HTTPS with standard security headers. If you add CSP, allow only the external Trystero JS host chosen by this version and the relay connections it uses; consider self-hosting a reviewed licensed dependency with the original license attached.
- Keep a versioned deployment and data migration plan before modifying schemas. A future version should include self-hosted relay choices and an explicit user-tested hosted cross-network matrix.

## Source and testing

`build.py` rebuilds reference JSON and a compact seed string. The unified `MODULES` registry inside `index.template.html` defines route, capabilities, dependencies, schema, lifecycle hooks, error handling and view mapping. `index.template.html` contains the app implementation with `__SEED_JSON__` injection placeholder. To rebuild after editing data or the shell:

```bash
python build.py
python - <<'PY'
from pathlib import Path
root=Path('.')
(root/'index.html').write_text((root/'index.template.html').read_text().replace('__SEED_JSON__',(root/'seed-snippet.txt').read_text()),encoding='utf-8')
PY
```

Validation: `python tests/check_catalog.py`, browser tests in `tests/smoke_browser.py` and new focused `tests/regression_v1_1.py` (requires Playwright/Chromium). Results documented in `TEST_REPORT.md`.

**Zero-Harm / Anti-Inversion:** No offensive cyber, illegal procurement, coercion, operational targeting or deceptive communication. Civilian protection, territorial integrity and accountable consent take priority over apparent gamification progress. See `ATTRIBUTIONS_AND_LICENSES.md`.

## v1.1 changes

- **Entity Atlas:** selected actor profile in the right column has its own vertical scrollbar and is keyboard-focusable; on narrow screens it moves before the main entity grid and stays a bounded scroll region.
- **Pathway Forge:** fixes the Regenerate button's formerly static output. The generator now varies top-matching candidates by generation, does not rebuild on every unrelated render, keeps anchors and pinned partners, rejects within-generation duplicate signatures, and reports exhaustion rather than falsely claiming new outcomes.
- **Collaboration:** a stable public community room is prefilled with a one-click Join option; create a private room and return to the public lobby without typing a room code. This is **not automatic network connection**. The public room is unmoderated and intended for small groups; it needs external infrastructure and should not carry sensitive data.
- **Offline:** service worker cache version bumped so hosted clients can receive the updated shell after activation. The research/evidence fact freeze remains 2026-10-16; no source freshness or live networking is implied.
