# Deployment and rollback

**Recommended:** Create a new Git branch and a separate HTTPS preview before replacing production. Back up any previous user-created JSON; browsers do not transfer localStorage/IndexedDB across origins or devices.

1. Run `python -m pip install -r requirements.txt`, `python build.py --check`, `python -m unittest discover -s tests -p 'test_*.py' -v`, `node --check app.js` and `python build.py`.
2. Upload every application file while retaining relative paths. Do not upload only `index.html` without its JS/CSS/icons/service worker and supporting research files.
3. Confirm navigation and application execution in a current Chrome, Firefox and Safari on actual origin; check browser console for errors and keyboard/focus navigation.
4. Test Forge inspector nested vertical wheel/touch/keyboard scrolling separately from main document; also test an 8-combination regeneration, chain export, guide search, policy packet export, case backup and import.
5. Test first-online-load / offline-reload on the hosted origin. Service worker does not run from local `file://`. A service worker update replaces cached shell on next successful online fetch; verify manifest matches deployed versions.
6. Keep optional peer networking OFF for institutional work until a security assessment, trusted-identity model and participant agreement exist. Public rooms are unmoderated; no secure diplomatic communications are provided.
7. Obtain independent legal, humanitarian, peacebuilding and mine-action expert validation of any specific proposed scenario, especially the constitutional, IHL, nuclear and sovereignty gates.

**Rollback:** Restore the prior Git commit / static deployment snapshot, clear or version service worker caches as needed, and import only a compatible previously exported local workspace. Do not assume a rollback restores user data; browser-local data is outside the repository.

**Privacy:** local case files remain browser-local unless explicitly exported or shared by the user. Static web hosting may have ordinary server access logs outside application control. Optional peer signaling reveals network metadata to service providers and connected peers.

**Security:** CSP should be hardened by the host after reviewing the single inline JSON bootstrap and optional dynamic import. No production security certification was conducted. SHA-256 checks do not certify the publisher.
