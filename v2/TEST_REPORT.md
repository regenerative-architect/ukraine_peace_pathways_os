# Test report — 2026-10-16 · v1.1.0

## Verified in the updated v1.1 build

- `python tests/regression_v1_1.py`: **PASS** in headless Chromium. Confirmed the right Entity Atlas pane is a bounded independent scroll region; scrolling inside it does not scroll the page. Confirmed responsive mobile pane, Regenerate yields different actor-assignment names (not merely changed IDs), preserves filters and pinned partners, and selecting a pathway does not secretly regenerate. Confirmed the public community room is prefilled, a private room can be created, and the public room restored without network traffic.
- `python tests/smoke_browser.py`: **PASS** on the updated bundle (existing route, catalog, guide, import/export and mobile-nav coverage).

## Verified in the original baseline and rechecked where noted

- `python tests/check_catalog.py`: **PASS**. Exactly 75 distinct entity IDs, 32 distinct solution families, 747 distinct tailored guide records, 32 collaboration templates and 8 dated evidence entries; all guides reference an entity and one of its own assigned solutions; each guide has 4 simplified + 7 advanced learning steps, five phases, cost uncertainty, legal/verification gates, conditional exchange and stop rule; embedded seed matches external data.
- JavaScript parsed using Node.js v22 `new Function` syntax check: **PASS**.
- `python tests/smoke_browser.py`: **PASS**, tested through Chromium `page.set_content`: overview, responsive navigation, all 75 entity cards, client-side search, selection, simple/advanced guide display, completing a learning step, saving local notes, forging alternative combinations, selecting an anchor and pinned partner, saving a draft, browsing saved draft in peer console, random private-room-code generation, exporting workspace JSON, reimporting validated workspace JSON with user confirmation, mobile drawer, evidence view, and no uncaught JavaScript page exceptions.
- Screenshots taken of desktop and mobile overview states. These are static previews, not a substitute for real device testing.

## Not verified in this environment

The Chromium environment blocks page navigation to `http://localhost` and `file://` through an administrator policy. Accordingly, **do not treat the following as passed**:

- Real HTTPS/localhost service-worker installation, cache activation, runtime interception and offline reload.
- IndexedDB persistence across real origin page reloads or private/file-mode failure recovery.
- Peer discovery or WebRTC transfer over live Nostr/MQTT signaling, including different networks or TURN routing.
- Accessibility audit against WCAG 2.2 AA with assistive technology; only semantic markup, labels and keyboard code were inspected.
- Large rooms, abusive peer scenarios, varied network topologies, CSP restrictions or full internationalization. The default community lobby is neither moderated nor an authenticated service; its scale and performance have not been established.

## Priority real-world acceptance matrix before deployment

1. Load the full bundle under localhost or HTTPS in a clean browser; verify manifest, application shell, each route, desktop/mobile focus, storage and dark/light mode.
2. Allow the versioned service worker to activate, go offline, reload, open the atlas, solution guide, sources and saved designs; verify offline indicator distinguishes browser network hint from actual relay status.
3. Export a workspace, clear local data with confirmation, reimport it, verify notes, guide progress and saved designs; test invalid JSON and excessive size handling.
4. With two tabs, select the prefilled public community room and press Join on both (or use an identical private code, strategy and optional passphrase); require peer-join count to increase. Test one proposal sent only after explicit consent and received pending review; test discard and approved save.
5. Repeat with two devices on **different** ISPs and restricted networks; verify TURN failover and relay availability. No guarantee exists without operating infrastructure.
6. Conduct legal/IHL/domain expert review of the analytical catalogs before distributing outside an educational setting.

## Transparency

The source-ledger facts are dated. Each pathway is a hypothesis and each entity solution is a possible contribution, **not a formal assignment, endorsement, bilateral agreement, command order, actual ceasefire or verified humanitarian result**.
