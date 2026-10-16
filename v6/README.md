# Peace Pathways OS v4.1 — Demilitarization & Civilian Protection Commons

**Foster + Navi / Planetary Restoration Archive · 16 October 2026**

An offline-first, non-gamified **independent decision-support research system** for examining lawful, civilian-centered options for de-escalation in the Russia–Ukraine war. This edition merges the v3 policy/evidence/workbench functionality with the v2 interactive research forge, brings the complete 747-template research library into the offline application, strengthens data contracts and dependency-cycle checks, and adds conditional demilitarization and independent-review modules.

It **is not** a peace treaty, a negotiation participant, a deployment authority, a live monitoring service or a substitute for qualified legal, humanitarian or diplomatic review. None of the cited institutions have endorsed this project. Military-restraint cases are conditional policy hypotheses: no imposed unilateral disarmament or changes of sovereignty are assumed.

## Start

**No build required for reading and local research:** unzip the whole bundle and open `index.html` in a browser; keep `app.js`, `styles.css`, `assets/`, `data/` and other files alongside it. File mode does not support service workers or online peer signaling. IndexedDB may be restricted in some local-file configurations; check Workspace & backups and export JSON regularly.

**For development:**

```sh
python -m pip install -r requirements.txt
python build.py --check
python -m unittest discover -s tests -p 'test_*.py' -v
node --check app.js
python build.py
```

**Hosted static deployment:** upload `index.html`, `app.js`, `styles.css`, `manifest.webmanifest`, `sw.js`, `build-manifest.json`, `assets/`, `data/` and the desired policy/reference documents to any HTTPS static host. Run a fresh hosted smoke test on the deployed origin. PWA cache requires first successful online load; user data does **not** automatically sync between devices.

## Routes

| Section | Capabilities |
|---|---|
| Executive brief | Clarifies limitations, public safety and research context |
| Diplomatic constraints | Consent, applicable law and veto points |
| Multi-track matrix | Three tracks, three phases and thirteen research portfolios |
| Regenerative finance & conflict-funder alternatives | 14 separately gated, civilian-first options grouped by legal financing class and potential funder roles |
| Demilitarization pathways | Ten conditional civilian protection, arms-restraint, verification and recovery scenarios |
| Pathway Forge | Eight generated interdisciplinary options per batch, nine evidence-gated prompt stages and independent right-hand scrolling |
| 747 research templates | Local offline search, inspector, and case creation |
| Institutional review packets | Eight categories with specific technical review requests, risks and Markdown exports |
| Negotiation workbench | Local cases with lawful authority, independent verification and noncompliance gates |
| Incentives | Non-quantified BATNA, reciprocal commitments and implementation vetoes |
| Verification | Monitoring protocols distinct from enforcement authority |
| Evidence | Dated source list with legal/situational provenance distinction |
| Collaboration | Optional explicit peer transport for **public-only** draft summaries, not confidential records |
| Workspace & backups | Import/export and local reset with confirmation |

## Source data and build checks

`data/entities.json` (75), `evidence.json` (33), `guide-bank.json` (747), `pathway-catalog.json` (13 pathways), `solutions.json` (45 dossiers) and new `demilitarization.json` (10 scenarios; 8 review-audience types), and `regenerative-funding.json` (14 interventions, 8 funder categories and 3 separate cooperation gates). All six have Draft 2020-12 schemas. `build.py --check` validates type/schema, duplicate IDs, references, units/metrics as represented by schemas, three tracks and phases, no unverified status disguised as authorization, and dependency cycles. A bad validation run does not overwrite `index.html`. A successful build emits a SHA-256 manifest; hash checks **do not prove authorship**.

All 747 guides are embedded into the generated `index.html` to support searching on `file://` and offline. The HTML is kept below 2 MB. The guides are research **templates**, not 747 externally reviewed plans.

## Migration

Keep a backup of any prior repository checkout. This is a **merge of the provided v3 ZIP and v2 reference rebuild**, not a direct merge of an inaccessible original Git history. Preserve your original repository in a branch before deploying. v3 cases remain on the existing IndexedDB/localStorage schema (`schema:2`); v2 research-note exports (`version:2`, `notes`, `reviewed`, `bookmarks`) have a guarded import route that transforms text notes into **unverified** ledger entries. Other v2 metadata is not silently mapped to verified evidence. A v1.1 research bundle with supported `schema:1` plans can also be imported. All imports prompt before replacing local workspace state. **Export your existing workspace first.**

## Independence and constraints

- A 30 km heavy-artillery separation is a proposed analytical assumption, not a negotiated buffer or military instruction.
- A five-year cooling period cannot authorize a local territorial referendum under Ukrainian constitutional and international law.
- The former OSCE SMM closed in 2022; proposed observation needs fresh consent and mandate.
- IAEA technical monitoring and temporary repair facilitation do not constitute coercive enforcement.
- No live AIS, drones, telemetry, coordinates, armed deployments, strike models, protected-person records, or AI-directed explosive clearance are provided.
- AI-assisted land classification does not equate to accreditation, clearance, or legal land release. Follow IMAS and competent national authorities.
- Sovereign assets and extraordinary proceeds have different legal statuses; no transfers are implemented by this software.
- Appropriately bounded protected-person access and humanitarian rights must not be made conditional on political concessions.

## Testing actually performed

- 16 Python unit tests passed (including deliberately invalid data, missing references, invalid status, cyclic dependency, schema validation and atomic build).
- Node JavaScript syntax check passed.
- Headless Chromium static-document smoke checks passed: 16 navigation sections, 10 demilitarization scenario choices, 8 reviewer profiles, guide search, Forge regeneration, nine-stage selection, exported Markdown, desktop and mobile nested-scroll `scrollHeight > clientHeight` and scrollTop change, no browser page errors, no horizontal mobile overflow.
- **Not independently verified in this run:** hosted navigation due to test-environment HTTP blocking, persistent IndexedDB across genuine origin reload, production service worker caching, true remote WebRTC peer connections, independent policy/field outcomes, full WCAG 2.2 AA certification and a security penetration test. Do not claim those are passed.

## Zero Harm / Anti-Inversion

Use public information and voluntary, legally authorized review. Explicitly separate proposal from consent; observed data from assumptions; research from action. Avoid location-specific military data, surveillance of protected people, coercive population-transfer or disarmament demands, automated field actions, and unreviewed sanctions/economic interventions. A software safety policy can reduce but never guarantee zero misuse.

## Attributions and licenses

Code and original interface content: Foster + Navi / Planetary Restoration Archive, MIT license. Retained v3 source architecture and v2 conceptual forge features as adapted, not external proprietary code. Third-party sources are linked rather than redistributed. Optional Trystero is dynamically loaded from a third-party CDN only when a user expressly joins a peer room; inspect its upstream license, availability and security before use. See `ATTRIBUTIONS_AND_LICENSES.md` and `LICENSE`.

## v4.1 · Conflict-to-Regeneration research module

This edition adds 14 research-stage financial and ecological alternatives aimed at conflict-related financing ecosystems. It differentiates Russian government funding for aggression from Ukraine's lawful self-defence and supporting donor actions; does not presume Ukraine should disarm or waive rights; and separates three legal implementation horizons: (1) parallel civilian recovery work now, (2) reciprocal commitments only after competent parties agree and independent verification is defined, and (3) post-agreement cooperation under applicable law.

**Not a solicitation, project escrow, sanctions license, or fund-transfer platform.** The user can filter eligible actor *categories*, inspect detailed mechanisms and quantifiable evaluation suggestions, and export a dated independent-review Markdown packet. No current commitments or institutional endorsement are inferred. Existing RDNA5, World Bank URTF, UNDP local financing, Council of Europe damage register and DREAM are contextual precedents. Restricted assets, proposed financing, approved grants and paid reparations are kept legally distinct.

The right-hand Forge panel remains independently scrollable; the regenerative-finance dossier has its own independent scrolling. All updates are included in build/source validation, hashed manifest and service-worker versioned cache, and retain offline `file://` core use.

**Safety:** Public analysis only. Do not send identifiable protected-person data, classified details, real-time infrastructure coordinates, sanctioned transfers or confidential financial arrangements. Assess sanctions, adverse human-rights consequences, environmental risk and public procurement through the competent institutions. All proposals remain unverified.
