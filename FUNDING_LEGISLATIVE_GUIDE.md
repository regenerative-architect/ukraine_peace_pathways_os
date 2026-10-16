# Financing × Legislative Gates — v4.5 research guide

**Last compiled:** 16 October 2026. **Status:** independent research, not a legal opinion, sanctions clearance, funding award, or diplomatic mandate.

## Scope

This module connects **30 existing evidence-graded funding profiles** with **14 regenerative proposals**, creating **60 explicitly curated research links**, each attached to selected legal jurisdictions and a compatible research topic. The resulting **218 jurisdiction–proposal reviews** reuse the established legal matrix. **118** have topical source flags and **100** have no mechanism-specific assessment. Both classes still require independent counsel; they do not confer authorization. The source directory contains **30 jurisdictions** and **67 official reference records**. Some are discovery portals, not adjudicated transaction-specific instruments.

### How to use

1. Open `index.html` and choose **Financing × legislative gates** from the left navigation.
2. Narrow by a documented funding profile, cooperation stage, jurisdiction or full-text query.
3. Read the right-hand panel independently: it identifies the proposed option, actor funding evidence, source-mapped preliminary legal issue, potential legal nexuses, permissions to investigate and explicit halt conditions.
4. Follow the official publisher links and identify the exact date, controlled entities, ownership, transaction route, goods/services, sovereign asset title, procurement rules, relevant sanction listings and all applicable legal systems.
5. Export a Markdown dossier or CSV/JSON directory for an independent legal/institutional reviewer; use **Inspect legal intersection** for the preexisting matrix or **Open in Pathway Forge** for a staged research plan.
6. Do not execute financial transfers or share confidential case information based on a displayed result.

### Distinguish these cases

- **Conventional civilian reconstruction aid:** May be possible under existing authorized programs, but the OS does not check award eligibility, donor terms, procurement, beneficial ownership or governmental authority. The status is unassessed until a competent reviewer confirms it.
- **Restricted counterparties, Russian sovereign assets, or relief from sanctions:** Treat as a more stringent legal gate. This OS cannot establish that an exemption applies, that a licence exists, or that approval will be granted. Separate EU/national, US, UK, Canadian and other applicable restrictions may coexist.
- **Possible third-country trade exposure:** The underlying record does not establish deliberate financing of Russia’s military operations, participation in the OS, or an illegality. Do not imply causation or criminal responsibility.
- **Humanitarian protection and land release:** Rights and professional clearance requirements are not tradable incentives; independent, accredited implementing authorities remain essential.
- **Conditional and post-agreement actions:** Explicitly speculative. No actual diplomatic agreement or sanctions relaxation is established.

### Source category and provenance discipline

The `finance-law-bridge.json` file expresses **screening research hypotheses only**. Data has immutable IDs referencing the existing `funding-atlas.json`, `regenerative-funding.json`, and `compatibility-matrix.json`. Records contain a potential jurisdictional nexus, not an assertion that the corresponding law applies. Existing source flags remain untouched; all other intersections remain *not assessed*. Verified country legislation portals added in this release: [Finland (Finlex)](https://www.finlex.fi/en/legislation) and [India Code](https://www.indiacode.nic.in/indiacode/home.jsp).

High-change official sources should be consulted online before interpreting current restrictions:
- [OFAC Russia sanctions / general licences](https://ofac.treasury.gov/sanctions-programs-and-country-information/russian-harmful-foreign-activities-sanctions)
- [UK Russia statutory sanctions guidance](https://www.gov.uk/government/publications/russia-sanctions-guidance/russia-sanctions-guidance)
- [Canada sanctions permits and certificates](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/certificates_permits-certificats_permis.aspx?lang=eng)
- [EU restrictive-measures legislation](https://eur-lex.europa.eu/eli/reg/2014/833/oj)

Review authority cannot be inferred from a website reference, a general licence without its actual conditions, a preliminary research flag, or stakeholder funding history.

### Build and validation

```sh
python -m pip install -r requirements.txt
python build.py --check
python -m unittest discover -s tests -v
python build.py
# Optional browser smoke if Playwright and Chromium are installed
python tests/browser_finance_law_smoke.py
```

`index.html` embeds the data and supports `file://` use; offline reference metadata does **not** include live online legal text. On a hosted HTTPS origin, the service worker precaches the shell; it cannot promise availability of external statutes, new legislation, or peer networks. Data import/export remains local; no institutional outreach is performed by the OS.

## Zero-harm / anti-inversion

Never display or transmit identifying details of protected civilians, private negotiations, tactical information, banking credentials, or nonpublic beneficial-ownership data. Do not interpret potential investor status as endorsement, or defensive aid to Ukraine as equivalent to Russia's aggression. No module facilitates sanctions avoidance or unauthorized disbursement.

## Attributions

Foster + Navi / Planetary Restoration Archive. Research concepts informed by public official legal publishers and source-linked original archive entries. See `ATTRIBUTIONS_AND_LICENSES.md` and `LICENSE` for project notices.
