#!/usr/bin/env python3
"""Generate local-first Peace Pathways OS: attributed public-source educational planning data.
No remote requests or services; deterministic, inspectable data assembly.
"""
from pathlib import Path
import json, html, re, itertools, collections, unicodedata
ROOT=Path(__file__).parent
DATA=ROOT/'data'
DATA.mkdir(exist_ok=True)
# Scope: actors and groupings from earlier ranked stakeholder analysis; grouped representatives
# are not claims of formal coordination, mandates, or endorsement of this tool.
ACTORS='''
Ukraine|1|state|decision,security,humanitarian,legal,civilian,energy,maritime|Authorized Ukrainian authorities must consent to sovereign decisions and operational instructions.|Security, territorial integrity, protection of civilians and meaningful guarantees are vital.
Russia|1|state|decision,security,trade,energy,maritime,legal|Russian civilian and military authorities can decide whether Russian forces cease attacks or withdraw.|Russian acceptance cannot be inferred from talks; independently verify implementation.
United States|1|state|mediation,security,finance,trade,legal|Coordinates high-level diplomacy, sanctions and potential security commitments.|Changes in policy may undermine counterpart confidence and predictability.
European Union|1|intergovernmental|finance,trade,security,legal,reconstruction,verification|EU institutions and member states control important European financial and sanctions decisions.|Member-state powers, legal competences and unanimity requirements differ.
China|1|state|trade,mediation,finance,decision|Maintains extensive political and commercial ties and diplomatic access to Moscow.|Willingness to exercise costly influence remains unproven.
Türkiye|1|state|mediation,maritime,trade,security,humanitarian|Can convene talks and support technical Black Sea maritime arrangements.|Shipping safety cannot be guaranteed unilaterally.
India|1|state|mediation,trade,energy,maritime,finance|Can connect energy, maritime, commercial and diplomatic workstreams.|May prioritize strategic autonomy; commitments require explicit consent.
United Arab Emirates|1|state|mediation,humanitarian,finance|Has experience facilitating prisoner exchanges and hosting meetings.|Humanitarian success does not demonstrate comprehensive-settlement authority.
United Kingdom|2|state|security,finance,legal,reconstruction,verification|Could underwrite security and implementation support through lawful commitments.|Cannot unilaterally guarantee another government's decisions.
France|2|state|security,mediation,legal,reconstruction,verification|Has UN, EU and European security channels and reconstruction capacity.|Post-ceasefire security activity requires mandates and consent.
Germany|2|state|finance,security,reconstruction,energy,trade|Can mobilize industrial, energy and recovery resources.|Domestic political and budgetary tradeoffs apply.
Coalition of the Willing|2|coalition|security,verification,finance,reconstruction|Potentially organizes voluntary security commitments after hostilities cease.|Composition, authorities and deployments cannot be presumed.
NATO|2|alliance|security,verification,defensive-cyber|Coordinates allied defence and deterrence commitments.|Alliance consensus and escalation risks constrain options.
Egypt|2|state|mediation,maritime,trade,humanitarian|Could help convene a food-and-shipping safe-passage workstream.|No authority to command belligerents or commercial ships.
Brazil|2|state|mediation,trade,finance,civilian|Offers Global South diplomatic connectivity and multilateral diplomacy.|Any mediation formula must genuinely include Ukraine.
Switzerland|2|state|mediation,verification,legal,humanitarian|Could host diplomacy and develop monitoring procedures.|Neutral facilitation cannot substitute for mandate or consent.
OSCE|2|intergovernmental|verification,mediation,security,legal|Possible technical monitoring, incident processes and dialogue support.|Mandate, access, resources and consensus are significant hurdles.
United Nations Secretariat|2|intergovernmental|mediation,humanitarian,legal,verification|Offers good offices, operational coordination and international framework.|Secretariat cannot impose a settlement or exceed mandate.
Saudi Arabia|2|state|mediation,energy,trade,finance|May convene talks and support commodity and confidence measures.|High-level access is not proof of effective coercive leverage.
Kazakhstan|2|state|mediation,trade,humanitarian|Offers regional diplomacy and possible confidence-building channels.|Political and economic dependencies constrain room to maneuver.
IAEA|3|intergovernmental|nuclear,verification,energy,legal|Provides nuclear-safety expertise and supports technical repair arrangements.|Safeguards mandate is not a general ceasefire-enforcement mandate.
ICRC|3|humanitarian|humanitarian,prisoners,children,civilian,legal|Neutral, impartial intermediary for detention, tracing and repatriation.|Requires access, parties' cooperation and humanitarian confidentiality.
Qatar|3|state|mediation,children,humanitarian|Offers child and family reunification mediation experience.|Consent and child protection govern all interventions.
Ukrainian and Russian military commands|3|operational|decision,security,verification,energy,maritime|Only authorized command structures can transmit synchronized ceasefire orders.|No third party may impersonate, instruct or target combatants.
UN OCHA|3|humanitarian|humanitarian,civilian,verification|Can coordinate relief and protection information within its mandate.|Access is negotiated; no guarantee of safe corridors.
IMO|3|intergovernmental|maritime,trade,legal,verification|Provides maritime safety standards, coordination and reporting channels.|No military enforcement powers.
UNCTAD|3|intergovernmental|trade,maritime,finance,food|Can study and facilitate trade, grain, fertilizers and supply chains.|Commercial facilitation is not a military agreement.
World Food Programme|3|humanitarian|food,humanitarian,trade,logistics|Supports food-security analysis, sourcing and distribution.|Access and funding constrain operations.
UNICEF|3|humanitarian|children,civilian,humanitarian,education|Child protection, education and basic-services support.|Protection and safeguarding requirements are paramount.
UNHCR|3|humanitarian|humanitarian,civilian,refugees,reconstruction|Assists displaced people and supports voluntary, safe durable solutions.|Returns cannot be compelled or presumed safe.
International Coalition for Return of Ukrainian Children|3|coalition|children,humanitarian,legal,verification|Can coordinate lawful return and reunification efforts.|Child identity, consent and privacy require careful safeguards.
EU Satellite Centre|3|institution|verification,data,security|Could provide authorized earth-observation analysis for civilian verification.|Geospatial intelligence must avoid operational targeting and privacy harms.
Ukrainian and Russian energy-grid operators|3|operational|energy,nuclear,verification,logistics|Can perform technically authorized repairs and grid-level protection planning.|Work requires permits, safety guarantees and protected access.
Poland|4|state|security,logistics,finance,reconstruction,refugees|Critical logistics and cross-border relief coordination.|Security responsibilities and domestic interests matter.
Canada|4|state|security,finance,mediation,reconstruction|Can coordinate assistance, diplomacy and recovery support.|Limited independent leverage over Moscow.
Finland|4|state|security,verification,mediation,defensive-cyber|Can offer resilience and security-policy expertise.|Border and alliance security sensitivities matter.
Norway|4|state|energy,maritime,finance,reconstruction|Energy, maritime engineering and humanitarian financing expertise.|Not a direct party to territorial negotiations.
Romania|4|state|maritime,security,logistics,trade|Black Sea logistics, trade and regional safety.|Spillover and regional escalation risks.
Bulgaria|4|state|maritime,trade,security|Black Sea technical safety and port logistics.|Limited direct diplomatic leverage.
Estonia Latvia Lithuania|4|coalition|security,defensive-cyber,legal,verification|Regional digital resilience, defence cooperation and sanctions expertise.|This is an analytical grouping, not a single legal entity.
Italy|4|state|reconstruction,finance,mediation,humanitarian|Recovery financing, EU negotiation and welfare coordination.|Support depends on political and financial mandates.
Belgium|4|state|finance,legal,trade,reconstruction|Important EU financial infrastructure and immobilized-asset legal questions.|Asset treatment requires judicial and international-law review.
Japan|4|state|finance,reconstruction,trade,energy|G7 coordination, resilient infrastructure and economic financing.|Security commitments differ from European allies.
South Korea|4|state|reconstruction,trade,finance,technology|Industrial, recovery and digital resilience capabilities.|Domestic and regional security constraints apply.
Australia New Zealand|4|coalition|finance,humanitarian,legal,security|Can support global diplomatic coalitions, relief and lawful measures.|Analytical grouping; each government decides independently.
South Africa|5|state|mediation,trade,legal,civilian|May connect African and BRICS diplomatic networks.|Access does not prove successful leverage.
African Union Commission|5|intergovernmental|mediation,food,civilian,humanitarian|Can represent continental conflict-prevention and food-security priorities.|No general mandate to resolve European territorial disputes.
G7|5|coalition|finance,trade,reconstruction,security,legal|Could coordinate financial instruments, sanctions and security assistance.|Not all influential third countries are members.
G20|5|coalition|trade,finance,mediation,food|Can convene major economies on global spillovers.|Consensus is difficult and decisions rarely enforceable.
BRICS|5|coalition|trade,finance,mediation,food|Connects countries with important trade and diplomatic channels.|Members have diverging incentives and positions.
UN General Assembly|5|intergovernmental|legal,civilian,mediation,verification|Can build legitimacy and express member-state positions.|Resolutions typically do not compel force compliance.
UN Security Council|5|intergovernmental|legal,security,verification,mediation|Could authorize appropriate international mechanisms if members agree.|Permanent-member veto and legal limits are central.
Indonesia|5|state|mediation,trade,food|Global South convening and food-market diplomacy.|Indirect influence on battlefield decisions.
Arab League and OIC|5|coalition|mediation,humanitarian,food,maritime|Could coordinate relief, food and diplomatic appeals.|Independent mandates and diverse memberships.
Moldova|5|state|refugees,security,humanitarian,reconstruction|Regional safety and displaced-person support.|Vulnerability to conflict spillover.
US Treasury OFAC and EU sanctions authorities|6|regulatory|finance,trade,legal,verification|May administer lawful conditional and reversible sanctions measures.|Measures require precise authority and compliance verification.
Euroclear and European financial authorities|6|institution|finance,legal,reconstruction|Could lawfully administer financial instruments within applicable law.|Sovereign-asset treatment is legally and politically contested.
World Bank Group|6|development|finance,reconstruction,energy,civilian|Can manage recovery financing, development safeguards and public accountability.|Eligibility, debt, anti-corruption and security risks.
EBRD|6|development|finance,reconstruction,energy,trade|Can finance private-sector resilience and infrastructure.|Banking mandate and procurement safeguards apply.
European Investment Bank|6|development|finance,reconstruction,energy|Can finance long-life resilient infrastructure.|Financing mandates and project safeguards apply.
IMF|6|development|finance,legal,reconstruction|Supports macro-financial resilience and transparent fiscal planning.|Is not a peace-enforcement body.
Shipping insurers and P&I clubs|6|commercial|maritime,trade,finance,verification|Can underwrite lawful maritime movements when risks are verified and acceptable.|Commercial risk, sanctions and underwriting rules apply.
Satellite and telecommunications providers|6|commercial|data,verification,defensive-cyber,communication|Can supply authorized technical evidence and resilient communication.|Must prevent privacy abuse and operational targeting.
Centre for Humanitarian Dialogue|6|civil-society|mediation,humanitarian,civilian|Specialist facilitation and private dialogue design.|Involvement or authorization cannot be assumed.
Berghof Foundation|6|civil-society|mediation,civilian,education|Conflict transformation, dialogue and process design.|No formal authority over parties.
International Crisis Group|6|civil-society|data,mediation,legal,civilian|Independent analysis and publication of risks and incentives.|Research is not negotiating authority.
Ukrainian municipalities and civil society|6|civil-society|civilian,reconstruction,education,refugees,verification|Can identify locally important protection and restoration priorities.|Consultation must be representative and never coercive.
Russian independent humanitarian and legal groups|6|civil-society|humanitarian,legal,civilian,prisoners|Where safe and lawful, can help document humanitarian needs and family tracing.|Severe personal security and legal risks require strict data minimization.
Belarusian government|6|state|decision,trade,legal,security|Could cease support enabling hostilities and reduce regional escalation.|External participation must be evidence-led and lawful.
Iranian government and relevant institutions|6|state|decision,trade,legal,security|Could end any unlawful military support contributing to attacks.|Assess specific evidence; avoid collective attribution.
North Korean government|6|state|decision,trade,legal,security|Could terminate arms and force support that prolongs combat.|Verification and sanctions compliance required.
Third-country export intermediaries|6|commercial|trade,legal,verification|Can implement end-use diligence and report suspicious dual-use diversions.|Manufacturer origin alone does not establish complicity.
Russian military-industrial and state-controlled sectors|6|commercial|trade,legal,energy,finance|Any demobilization or compliant conversion requires lawful state decisions.|Should not presume voluntary participation or absolve wrongdoing.
Veterans and survivor support networks|6|civil-society|civilian,education,humanitarian,reconstruction|Can support trauma-informed services, reintegration and community recovery.|Protect privacy, consent and equitable access.
University and science consortiums|6|research|data,energy,education,reconstruction,verification|Can test recovery technologies and evaluate interventions transparently.|Research must be non-operational and conflict-sensitive.
'''
entities=[]
for n,line in enumerate(ACTORS.strip().splitlines(),1):
    name,tier,kind,cap,mandate,constraint=line.split('|')
    entities.append({'id': re.sub('[^a-z0-9]+','-',unicodedata.normalize('NFKD',name).encode('ascii','ignore').decode('ascii').lower()).strip('-'), 'rank':n,'name':name,'tier':int(tier),'kind':kind,'capabilities':cap.split(','),'mandate':mandate,'constraint':constraint,'status':'Potential contribution — not an endorsement, pledge or verified participation','confidence':'Medium: capability assessment; willingness unverified'})

# All solutions are structured proposed interventions. Separate evidence-backed contextual facts from proposals.
# Required output format: id|title|tags|type|outcome|firstMove|verification|failure|legal|metric
SOLUTION_ROWS='''
civilian-impact-ledger|Civilian harm monitoring|civilian,data,verification,legal|humanitarian|Evidence-based priorities for reducing civilian harm|Choose a civilian-safe, aggregate monitoring indicator with public methodology|Cross-check incident claims against UN/OHCHR and independent records|Selective counting or re-identification of victims|Protect personal data and avoid operational targeting|Documented civilian harm trends by source and date
energy-truce|Reciprocal energy infrastructure restraint|energy,decision,mediation,verification|sectoral|Prohibit defined attacks on civilian energy systems|Draft reciprocal scope, definitions and synchronized effective time|Independently investigate alleged incidents before attributing responsibility|Announced restraint is mistaken for accepted, implemented agreement|IHL civilian-object protection; no authorization for attacks|Verified incidents and service restoration
nuclear-safety|Nuclear safety repair access|nuclear,energy,verification,mediation|sectoral|Keep critical nuclear cooling and electrical supply safe|Identify safe, consented repair windows and IAEA technical coordination|Record independent safety assessments and confirmed repairs|Safety guarantees collapse or observers lack access|IAEA mandate, nuclear safety, IHL and site-access consent|Safe power availability and independently confirmed repairs
black-sea-safety|Black Sea merchant shipping safety|maritime,trade,mediation,verification|sectoral|Reduce harm to civilian vessels, ports and food flows|Draft safe-passage rules with ship operators and parties|Track maritime incident reports and independently verified transits|False safety assurances expose seafarers to danger|Law of the sea, shipping standards, IHL and sanctions|Verified civilian transits and incidents
prisoner-exchanges|Prisoner and detainee exchanges|prisoners,humanitarian,decision,mediation|humanitarian|Enable humane treatment, family contact and lawful releases|Request neutral confidential liaison among authorized parties|ICRC or trusted agreed intermediary confirms completed transfers|Publicity endangers people or releases are misreported|Third Geneva Convention and ICRC principles|Confirmed exchanges, missing-person updates
missing-persons|Missing-person tracing|prisoners,humanitarian,legal,children|humanitarian|Clarify fate and whereabouts with family consent|Establish consent-first confidential case referral|Authorized family notification, documented closure and safeguards|Sensitive identities leak or families are misled|Privacy, IHL missing-person obligations|Verified cases resolved with informed consent
children-reunification|Child reunification|children,humanitarian,mediation,legal|humanitarian|Safely reunite children and families using best-interest principles|Define consent and identity-verification pathway|Independent qualified child-protection case follow-up|Child protection is subordinated to political narratives|Convention on the Rights of the Child, privacy, IHL|Safe, verified family reunifications
relief-access|Humanitarian aid access|humanitarian,civilian,logistics,mediation|humanitarian|Increase impartial food, medicine and shelter access|Define needs-driven logistics corridor with safety commitments|Confirm distribution and independent humanitarian access|Convoys are obstructed or diverted|IHL humanitarian access, neutrality and impartiality|Verified deliveries and sustained access days
local-pause|Site-specific humanitarian pause|decision,mediation,verification,energy|sectoral|Permit bounded repairs, evacuations or aid missions|Define objective, site scope and safe start-stop protocol|Independent confirmation of access and cessation conditions|Local pause becomes unverified pretext for larger claims|Party consent, civilian protection and neutral oversight|Completed protected mission without verified incident
general-ceasefire|Monitored general armistice|decision,security,verification,mediation|armistice|Stop hostilities with enforceable mechanisms|Propose reciprocal ceasefire text and a trusted joint communication channel|Neutral authorized incident review and verified compliance reporting|Rearmament, disputed lines or unverifiable compliance|UN Charter, IHL, command authority and mandate|Verified incident rate and civilian protection
incident-verification|Neutral incident verification|verification,data,legal,mediation|armistice|Make violations adjudicable and reversibly addressed|Agree observer access, evidence handling and incident categories|Independent corroboration and documented appeals process|Fabricated evidence, denied access or rushed attribution|Consent, proportionality, privacy, impartiality|Reports resolved within agreed timelines
security-guarantees|Credible security guarantees|security,decision,legal,finance|settlement|Prevent renewed aggression without undermining sovereignty|Identify credible legal commitments and practical triggers|Legislative authorizations, resources and independent audits|Nonbinding assurances substituted for enforceable obligations|UN Charter self-defence and treaty/constitutional law|Funded commitments with measurable readiness
sovereignty-framework|Sovereignty and territorial legal framework|legal,decision,mediation,civilian|settlement|Separate practical ceasefire lines from legal status|Record sovereignty protections and nonrecognition clauses|Legal scrutiny, consent and public clarity|Temporary lines become coerced recognition|UN Charter territorial integrity; human rights|Agreements preserve de jure status while reducing harm
sanctions-conditionality|Conditional sanctions and compliance|legal,trade,finance,verification|settlement|Tie lawful measures to independently tested behavior|Map competent authorities, waivers, targets and reversal triggers|Published compliance rulings and independent audits|Premature relief or avoidable civilian costs|Applicable sanctions law and due process|Documented compliance and civilian-impact review
export-diligence|Dual-use export control integrity|trade,legal,verification,data|prevention|Reduce unlawful procurement and sanctions evasion|Prioritize end-use controls, lawful reporting and training|Regulatory findings and audited compliance improvements|Country-of-origin assumptions replace evidence of diversion|Export-control law and privacy; no illicit sourcing|Verified compliance controls and validated findings
winter-energy|Civilian energy resilience|energy,reconstruction,civilian,finance|recovery|Restore heat, electricity and critical civilian services|Identify high-value repairs and protected decentralized backups|Audited service availability and independent safety inspections|Projects bypass local needs or create new hazards|Humanitarian principles and public procurement rules|Households and facilities with restored service
shelter-health|Shelter and essential health services|humanitarian,civilian,reconstruction,finance|recovery|Maintain shelter, medicine, schools and continuity of care|Map verified unmet civilian service needs with local partners|Transparent service coverage, patient safety and safeguarding|Unequal provision or aid diversion|Human rights, healthcare neutrality and procurement safeguards|Access to safe shelter and healthcare
recovery-contracts|Accountable reconstruction projects|reconstruction,finance,legal,civilian|recovery|Rebuild transparent and climate-resilient civilian assets|Co-design a priority project with affected communities|Open contracting, independent audit and post-use inspections|Corruption, displacement or low-quality infrastructure|Procurement law, land rights and environmental safeguards|Completed audited projects and real service outcomes
asset-governance|Legally sound recovery finance|finance,legal,reconstruction|recovery|Finance recovery within property and public law|Commission independent legal review of each financing route|Public accounting and judicially sustainable governance|Illegal confiscation or opaque fund distribution|State immunity, domestic law, due process|Audited disbursement and legal findings
refugee-returns|Voluntary refugee and displaced-person solutions|refugees,civilian,humanitarian,reconstruction|recovery|Support safety, agency and dignified durable choices|Consult displaced communities on barriers and preferences|Voluntary informed choices and protection outcome checks|Premature coercive return or exclusion|Non-refoulement, human rights and data protection|Safe voluntary durable solutions
justice-evidence|Accountability and evidence preservation|legal,data,verification,civilian|justice|Preserve admissible evidence and survivors' rights|Define independent evidence-handling and safeguarding protocol|Chain of custody audits and competent legal review|Evidence contamination or victim retraumatization|IHL, human rights, criminal procedure and privacy|Validated preserved records, survivor support
mine-clearance|Humanitarian mine action|civilian,reconstruction,humanitarian,verification|recovery|Reduce civilian risk from explosive remnants|Coordinate accredited humanitarian operators and risk education|Accredited land-release and injury reporting|Untrained participation puts civilians at risk|Humanitarian mine action standards and national permissions|Accredited clearance and reduced casualties
defensive-cyber|Defensive infrastructure cyber resilience|defensive-cyber,energy,data,verification|prevention|Protect hospitals, grids and public digital services|Assess authorized defensive backups, patching and continuity|Documented tests and incident reporting without offensive intrusion|Intrusive measures or data leakage|Authorization, cybersecurity law and privacy|Service continuity and validated resilience tests
information-integrity|Truthful information and rumor resistance|communication,data,education,civilian|prevention|Reduce false claims that erode humanitarian trust|Publish source-grade annotations and correction procedures|Independent fact-checking and correction timestamps|Covert persuasion, censorship or forced messaging|Free expression, privacy and transparent attribution|Corrected reports and verified information reach
confidence-dialogue|Consent-based diplomatic confidence building|mediation,decision,civilian,legal|diplomacy|Create small verifiable bilateral or multilateral exchanges|Seek lawful convening consent and agenda-limited meetings|Agreed written actions with independent implementation checks|Dialogue is mistaken for endorsement or false peace|Sovereignty, mediation neutrality and transparent authority|Completed reciprocal action commitments
food-continuity|Global food and fertilizer continuity|food,trade,maritime,humanitarian|sectoral|Improve essential food supply through lawful safe trade|Map ports, importing needs and lawful maritime safeguards|Verified delivery and world food-security indicators|Trade arrangements unintentionally evade sanctions|Humanitarian exemptions, trade and shipping law|Verified food deliveries and price-access trends
environment-restoration|Environment and water recovery|reconstruction,energy,civilian,data|recovery|Protect water, soils and ecosystem functioning|Audit civilian water and environmental risks|Open pollution and water-quality reports|Clean-up creates exposure or displaces households|Environmental law, health and land rights|Verified safe water and remediated assets
supply-chain-integrity|Public procurement and supply-chain transparency|trade,finance,legal,verification|prevention|Reduce corruption and illicit diversion in lawful procurement|Design controlled screening of suppliers and intermediaries|Audits separating origin, exporter, intermediary and destination|False accusations based on nationality or manufacturer|Procurement, sanctions, export control and due process|Verified supplier controls and reduced exceptions
peace-financing|Outcome-linked civilian peace financing|finance,reconstruction,verification,mediation|settlement|Link recovery support to lawful, verifiable civilian gains|Design disbursement milestones independent of political rhetoric|Public financial audits and civilian-outcome reviews|Perverse incentives or promises exceeding budgets|Financial law, public accountability and rights|Funds tied to confirmed civilian outcomes
civilian-consultation|Inclusive civilian consultation|civilian,mediation,legal,education|diplomacy|Make affected communities genuine participants|Invite representative and consented safe participation|Publish anonymized feedback and response matrices|Token consultation or endangered participants|Protection, inclusion and meaningful informed consent|Diverse participation and acted-upon feedback
risk-forecast|Scenario planning and catastrophic-failure premortem|data,verification,security,legal|prevention|Anticipate bad-faith compliance, errors and reversals|Run independent 24-month failure scenarios with stop rules|Document warnings, assumptions and tested mitigations|Predictions become unsupported certainty|Uncertainty transparency and non-operational analysis|Closed high-risk gaps and revised safeguards
veteran-reintegration|Veteran and survivor recovery|civilian,education,humanitarian,reconstruction|recovery|Provide trauma-informed livelihoods and reintegration|Co-design accessible non-stigmatizing services|Independent rights-based outcome evaluations|Privacy breaches and inequitable eligibility|Disability rights, informed consent and labor law|Durable voluntary support and employment outcomes
'''
SOLUTIONS=[]
for line in SOLUTION_ROWS.strip().splitlines():
    sid,title,tags,category,outcome,first,verify,failure,legal,metric=line.split('|')
    SOLUTIONS.append(dict(id=sid,title=title,tags=tags.split(','),category=category,outcome=outcome,first=first,verify=verify,failure=failure,legal=legal,metric=metric, status='PROPOSAL (not an existing institutional commitment)'))
SOL_BY={s['id']:s for s in SOLUTIONS}
# Each capability maps to a ranked solutions bank. 4-11 proposals per entity.
for e in entities:
    scores=[]
    tags=set(e['capabilities'])
    for s in SOLUTIONS:
        shared=tags.intersection(s['tags'])
        if not shared:continue
        bonus=3 if e['tier']<=2 and s['category'] in ('settlement','sectoral','diplomacy') else 0
        # defend role-specific tailoring
        score=sum(3 if t in ('decision','prisoners','nuclear','children') else 2 for t in shared)+bonus
        scores.append((score,s['id']))
    scores.sort(key=lambda x:(-x[0],x[1]))
    e['solutions']=[sid for _,sid in scores[:10]]
    e['guide_count']=len(e['solutions'])
    e['stakeholderModel']={
      'documentedAuthority':e['mandate'],
      'potentialLeverage':[t.replace('-',' ') for t in e['capabilities']],
      'inferredIncentive':'INFERENCE, NOT AN OFFICIAL POSITION: '+('Protect civilian lives, maintain lawful agency and secure credible commitments.' if e['id']=='ukraine' else 'A credible, bounded arrangement should improve civilian safety while respecting this actor’s mandate and constraints.'),
      'constraints':e['constraint'],
      'redLines':'UNKNOWN without entity-specific authorized, dated consultation; law and affected communities must be protected.',
      'BATNA':'UNCERTAIN: validate documented alternatives and opportunity costs; do not invent private motives.',
      'spoilerRisk':'Loss of mandate, non-cooperation, disinformation, funding gaps or verification failure; test context specifically.'
    }

# Per-solution 4-6 seats with respective qualifications, actual entities are matched by tags.
SLOTS = {
 'humanitarian':[('Direct party','decision'),('Neutral intermediary','humanitarian'),('Protection practitioner','civilian'),('Verification / evidence','verification')],
 'sectoral':[('Direct party','decision'),('Convener / facilitator','mediation'),('Technical implementer','energy'),('Independent verifier','verification')],
 'armistice':[('Command authority','decision'),('Diplomatic convener','mediation'),('Security guarantor','security'),('Independent verifier','verification')],
 'settlement':[('Sovereign decision-maker','decision'),('External diplomatic bridge','mediation'),('Financial / legal counterpart','finance'),('Implementation verifier','verification')],
 'recovery':[('Affected community','civilian'),('Project finance','finance'),('Implementation capacity','reconstruction'),('Independent oversight','verification')],
 'justice':[('Civilian protection','civilian'),('Legitimate legal authority','legal'),('Evidence stewardship','data'),('Independent review','verification')],
 'prevention':[('Authorized operator','legal'),('Independent research','data'),('Technical safeguards','defensive-cyber'),('Independent oversight','verification')],
 'diplomacy':[('Direct party / mandate','decision'),('Facilitator','mediation'),('Civilian participation','civilian'),('Review / accountability','legal')]
}
# Fix sectoral technical slot by solution primary specialty, preserving decision and verifier.
tech_preference=['nuclear','maritime','energy','food','trade','prisoners','children','logistics']
for s in SOLUTIONS:
    slots=[{'seat':seat,'tag':tag} for seat,tag in SLOTS[s['category']]]
    if s['category']=='sectoral':
        special=next((t for t in tech_preference if t in s['tags']),s['tags'][0])
        slots[2]['tag']=special
    if s['category']=='humanitarian':
        special=next((t for t in ['children','prisoners','refugees','humanitarian','food'] if t in s['tags']), 'humanitarian')
        slots[1]['tag']=special
    s['slots']=slots
    s['costBand']={'humanitarian':'Variable: limited pilot to major aid operation','sectoral':'Variable: technical pilot to full verification mission','armistice':'High uncertainty: observers, guarantees and political consent','settlement':'High uncertainty: multi-year diplomacy and implementation','recovery':'Project-specific: independent engineering and public procurement estimates needed','justice':'Variable: specialist professional and safeguarding costs','prevention':'Variable: staffing, audit and technical controls','diplomacy':'Variable: convening and continuing implementation'}[s['category']]
    s['independentMetric']=s['metric']
    s['goNoGo']='GO only with authorized consent, a documented legal review, protected civilian data and a credible verification protocol. STOP if evidence, safety or authority fail.'
    s['dependencies']=['Authorized institutional owner and safe participant contact','Lawful scope and resources','Independent verification and incident-response mechanism','Civilian-impact review and reversible fallback']
    s['conditionalExchange']='ACTION: '+s['first']+' → VERIFIED RESPONSE: '+s['verify']+' → BENEFIT: '+s['outcome']+'. Suspend expansion upon '+s['failure']+'.'
    s['stages']=[
      {'phase':'0–72 hours','heading':'Define a narrow, civilian-centered ask','action':s['first'],'checkpoint':'Document consent needs and a no-harm stop rule.'},
      {'phase':'2–6 weeks','heading':'Verify the reciprocal or authorized response','action':s['verify'],'checkpoint':'Review evidence quality and documented disagreements.'},
      {'phase':'2–6 months','heading':'Scale cautiously if protection improves','action':'Extend the intervention only after independent checks against the metric: '+s['metric']+'.','checkpoint':'Report civilian benefits, cost and unintended effects.'},
      {'phase':'6–24 months','heading':'Institutionalize responsible oversight','action':'Transfer mature tasks to the competent legal institutions, publish an accessible audit trail and maintain an incident-review channel.','checkpoint':'Independent oversight remains funded and functional.'},
      {'phase':'2–10 years','heading':'Test durability and regenerative outcomes','action':'Track recurrence, rights, legitimate sovereignty and restorative public-service impacts.','checkpoint':'Sustained civilian benefit survives leadership or funding changes.'}
    ]
    s['advanced']={
        'causal_model':'Hypothesis: '+s['outcome']+'. Test whether the intervention changes incentives, operational behavior and measurable civilian results; do not infer causality from coincidence.',
        'legal_review':s['legal']+'. Commission competent counsel before any real implementation.',
        'verification_protocol':'Set baseline → define incident threshold → authenticate records → independent adjudication → timely appeal → proportional, lawful response. '+s['verify']+'.',
        'red_team':'Assume false compliance, denied access, misuse of information, unintended civilian harm and leadership changes. Failure mode: '+s['failure']+'.',
        'fallback':'If consent, authority or evidence fails, stop escalation, preserve humanitarian channels and narrow the action to observable civilian protection.'}
    s['simple']=[
        'Understand the problem: '+s['outcome']+'.',
        'Identify the actual authority and obtain consent; proposing is not negotiating.',
        'Start small: '+s['first']+'.',
        'Check real-world impact: '+s['metric']+'.'
    ]

# Dated source ledger; active URLs with dates and confidence; no live data APIs or fabricated real-time counts.
evidence=[
 {'id':'un-charter','name':'Charter of the United Nations, Articles 2 and 51','date':'1945-06-26','class':'LEGAL TEXT','confidence':'High','claim':'Sovereign equality, peaceful dispute resolution, prohibition of force and self-defence provide foundational legal constraints.','url':'https://www.un.org/en/about-us/un-charter/full-text','implication':'No forced territorial recognition or coercive settlement proposal.'},
 {'id':'ohchr-sep','name':'OHCHR civilian-protection report: September 2026','date':'2026-10-15','class':'VERIFIED MONITORING REPORT','confidence':'High for documented minimum counts','claim':'At least 328 civilians killed and 2,105 injured in Ukraine during September 2026 (documented minimum).','url':'https://ukraine.ohchr.org/en/Protection-of-Civilians-in-Armed-Conflict-September-2026','implication':'Prioritize verified civilian protection and warn against undercounting.'},
 {'id':'iaea-oct','name':'Reuters: IAEA-facilitated Zaporizhzhia repair truce','date':'2026-10-15','class':'REPORTED DEVELOPMENT','confidence':'Medium–high; independent repair outcome not established here','claim':'Rosatom reported a locally scoped IAEA-mediated truce for power-supply repairs.','url':'https://www.reuters.com/world/russias-rosatom-says-truce-place-zaporizhzhia-power-supply-repairs-2026-10-15/','implication':'Test narrow technical pause models, not a claim of general ceasefire.'},
 {'id':'osce-feb','name':'OSCE support for monitoring a negotiated settlement','date':'2026-02-02','class':'OFFICIAL POSITION','confidence':'High','claim':'OSCE leadership indicated readiness to support implementation monitoring, if authorized.','url':'https://www.osce.org/chairpersonship/661975','implication':'Explore consent-based monitoring mandates and funding.'},
 {'id':'icrc-neutral','name':'ICRC: value of neutrality for humanitarian work','date':'2025-02-21','class':'OFFICIAL HUMANITARIAN MANDATE','confidence':'High','claim':'Neutral, independent and impartial intermediary activities include repatriation and reconnecting families.','url':'https://www.icrc.org/en/article/russia-ukraine-international-armed-conflict-value-neutrality-humanitarian-work','implication':'Respect confidentiality; do not publish sensitive cases or impose advocacy roles.'},
 {'id':'rdna5','name':'World Bank Group support to Ukraine: March 2026','date':'2026-03-01','class':'INSTITUTIONAL ESTIMATE','confidence':'High for published estimate; projections uncertain','claim':'February 2026 RDNA5 estimated nearly US$588 billion in reconstruction needs over the following decade.','url':'https://thedocs.worldbank.org/en/doc/ccf8044b6df7e0dd03f3899580b97d35-0080012026/original/WBG-Support-Ukraine-March-2026.pdf','implication':'Financing designs need audits, prioritization and local ownership.'},
 {'id':'trystero-doc','name':'Trystero: official getting started and connection requirements','date':'2026-10-16','class':'TECHNICAL DOCUMENTATION CHECKED','confidence':'High for API at version 0.26.0','claim':'Both peers must share app ID, room ID, signaling strategy and password; some network pairs need TURN.','url':'https://trystero.dev/docs/connections/','implication':'Opt-in peer connection with room-code diagnostics and honest TURN fallback.'},
 {'id':'trystero-strategy','name':'Trystero: signaling strategies','date':'2026-10-16','class':'TECHNICAL DOCUMENTATION CHECKED','confidence':'High for version 0.26.0','claim':'Default Trystero uses public Nostr relays; signaling and data transport are distinct.','url':'https://trystero.dev/docs/signaling-strategies/','implication':'Never claim network or relay availability in offline mode.'},
]

for fname,obj in [('entities.json',entities),('solutions.json',SOLUTIONS),('evidence.json',evidence)]:
    (DATA/fname).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Distinct comprehensively customized guide-bank records per each solution assigned to each actor.
guides=[]
for e in entities:
    for i,sid in enumerate(e['solutions']):
        s=SOL_BY[sid]
        guides.append({
          'id':e['id']+'__'+sid,'entityId':e['id'],'solutionId':sid,'level':'Beginner → practitioner → systems architect',
          'classification':'PROPOSED CAPABILITY PATHWAY; does not assert entity assent',
          'entry':'For '+e['name']+': '+s['outcome']+'. This path uses the actor’s '+', '.join(e['capabilities'][:3])+' capacity, not an assumed agreement.',
          'authority':e['mandate'],'risk':e['constraint'],
          'simpleGuide':[
              {'label':'Spot the opportunity','instruction':s['simple'][0]},
              {'label':'Find a lawful owner','instruction':'For '+e['name']+': '+e['mandate']+' Confirm the exact authority; do not claim a mandate.'},
              {'label':'Make one bounded first move','instruction':s['first']+' Add an explicit human authorization step.'},
              {'label':'Check success safely','instruction':s['verify']+' Measure: '+s['metric']+'.'}
          ],
          'advancedGuide':[
              {'label':'Causal theory and counterfactual','instruction':s['advanced']['causal_model']},
              {'label':'Incentives, BATNA and binding constraints','instruction':'Compare '+e['name']+' participation to a no-deal baseline. Constraint: '+e['constraint']+' Ask what would change voluntary acceptance.'},
              {'label':'Law and authorizations','instruction':s['advanced']['legal_review']+' Actor remit: '+e['mandate']},
              {'label':'Verification and evidence thresholds','instruction':s['advanced']['verification_protocol']},
              {'label':'24-month adversarial premortem','instruction':s['advanced']['red_team']+' Account for leadership changes, resource loss and rearmament.'},
              {'label':'Stop rule and fallback','instruction':s['advanced']['fallback']},
              {'label':'Measurement and adaptation','instruction':'Baseline: record dated public evidence. Leading signal: written consent and safe access. Outcome: '+s['metric']+'. Note unknown causality.'}
          ],
          'suggestedPartners':[slt['seat']+' ('+slt['tag']+')' for slt in s['slots']],
          'phases':s['stages'],
          'budgetPlanning':s['costBand'],
          'dependencies':s['dependencies'],
          'conditionalExchange':s['conditionalExchange'],
          'decisionOwner':'The competent authorized decision-maker for '+e['name']+' (not this app or its users).',
          'goNoGo':s['goNoGo'],
          'license':'Original educational synthesis; named institutions have not endorsed it.'
        })
(DATA/'guide-bank.json').write_text(json.dumps(guides,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Curated high-level win conditions that users can load or remix.
recipes=[{'id':s['id'],'title':s['title'],'goal':s['outcome'],'kind':s['category'],'slots':s['slots'],'keyMetric':s['metric'],'legal':s['legal'],'fallback':s['advanced']['fallback']} for s in SOLUTIONS]
(DATA/'pathway-catalog.json').write_text(json.dumps(recipes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('entities',len(entities),'solution templates',len(SOLUTIONS),'distinct guides',len(guides),'pathway templates',len(recipes))

# Seed data embedded directly for file:// offline browsing; external JSON copies are interoperable.
seed={'version':1,'snapshot':'2026-10-16','entities':entities,'solutions':SOLUTIONS,'evidence':evidence,'guides':guides,'recipes':recipes}
(DATA/'seed.json').write_text(json.dumps(seed,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
seed_compact=json.dumps(seed,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
(Path(ROOT/'seed-snippet.txt')).write_text(seed_compact,encoding='utf-8')
