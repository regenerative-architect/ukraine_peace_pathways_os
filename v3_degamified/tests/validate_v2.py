"""Static release validation without outside network access."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,re
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text()
soup=BeautifulSoup(html,'html.parser')
assert soup.title.string.startswith('Peace Accord')
assert soup.find('script',id='catalog')
actual=json.loads(soup.find('script',id='catalog').string)
expected={k:json.loads((root/'data'/f'{k}.json').read_text()) for k in ['entities','solutions','evidence']}
assert actual==expected, 'Embedded catalog is stale'
assert len(actual['entities'])==75
assert len(actual['solutions'])==32
assert len(actual['evidence'])>=18
assert len(set(x['id'] for x in actual['entities']))==75
assert len(set(x['id'] for x in actual['solutions']))==32
for e in actual['entities']:
 assert 'rank' not in e and 'tier' not in e and 'guide_count' not in e
for s in actual['solutions']:
 assert 'simple' not in s and 'advanced' not in s
 assert s.get('legal') and s.get('failure') and s.get('verify')
for src in actual['evidence']:
 assert src['url'].startswith('https://') and re.match(r'^\d\d\d\d-\d\d-\d\d$',src['date']),src
app=(root/'app.js').read_text();css=(root/'styles.css').read_text()
for token in ['const GATES','function assessment(','function verification(','function decisions(','function memo(','function normalize(','function importLegacy(','function collaboration(']:assert token in app
for token in ['.profile-scroll','@media(max-width:790px)','@media print','prefers-reduced-motion']:assert token in css
assert 'const DIRECT=' in app
assert 'scoreActor' not in app and 'level-up' not in app and 'saved.completed' not in app
assert (root/'reference/legacy_guide_bank.json').exists()
print('PASS catalog integrity, counts, references, degamification and required modules')
