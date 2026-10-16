# Attributions & Licenses

## Original work, transformation and code

**Foster + Navi / Planetary Restoration Archive, 2026.** Original Peace Pathways OS v1.1 catalog, the concept, and this degamified v2.0 interface and methodology. The code is released under MIT; see `LICENSE`. This edition is an independent policy-analysis research prototype, not affiliated with or endorsed by a state, the UN, OSCE, ICRC, NATO, European Union, or any other named body.

The v1.1 catalog of 75 profiles and 32 intervention families is adapted, with ranked tiers, completion systems and artificial diplomatic scoring removed. The former 747-guide reference catalog survives in `reference/legacy_guide_bank.json` for provenance, not as normative evidence or an implemented interactive module. `reference/legacy_pathways.json` preserves historical structures, also not loaded by the v2 UI. Case-specific risk and authority information is analytic and requires independent verification.

## Open-source concepts and optional transport

- **Trystero v0.26.0**: peer-to-peer WebRTC abstraction, optional network feature loaded from `https://esm.run/trystero@0.26.0` (Nostr) or `https://esm.run/@trystero-p2p/mqtt@0.26.0` only after an affirmative Join click. Homepage/docs: https://trystero.dev/ ; licensing: https://github.com/dmotz/trystero . This bundle contains no vendored Trystero code; network functions depend on external project availability and license terms. Review upstream license and privacy implications before deployment.
- Standard Web APIs: IndexedDB, File/Blob APIs, service workers and static HTML/CSS/JavaScript. No framework, telemetry SDK or account requirement.
- Icons: pre-existing PRA originals from uploaded v1.1 bundle, retained as locally hosted assets.

## Independent public sources

The dated ledger links to primary texts and reports from the UN, OHCHR, ICRC, OSCE, Ukrainian presidential office, UK government, World Bank and IAEA reporting, as well as time-stamped Reuters news reports. References are used as **links and concise attributed paraphrases**, not reproduced copyright text or claims of institutional endorsement. Rights and trademarks remain with their respective organizations. See `data/evidence.json` and `NEGOTIATION_FRAMEWORK.md`.

## Principles

Evidence is not consent; hypothesis is not a mandate; an announced proposal is not an agreed ceasefire; a written obligation is not verified implementation. No automatic contact, personal-data collection or real-time military monitoring is included. Zero-harm safeguards reduce abuse opportunities but provide no absolute safety guarantee.
