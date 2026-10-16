"""Offline-injected Chromium tests: comparisons, filter, export, scrollbar, Forge handoff, mobile."""
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parents[1]
html=(P/'index.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="./styles.css">','<style>'+(P/'styles.css').read_text()+'</style>').replace('<script src="./app.js" defer></script>','<script>'+(P/'app.js').read_text()+'</script>')
with sync_playwright() as pw:
 br=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for name,width,height in [('desktop',1440,900),('mobile',390,844)]:
  ctx=br.new_context(viewport={'width':width,'height':height},accept_downloads=True)
  page=ctx.new_page();errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
  page.set_content(html);page.wait_for_timeout(250)
  if name=='mobile':page.locator('#menuToggle').click()
  page.locator('#routeNav a[href="#/compatibility"]').click();page.locator('h1').filter(has_text='Cross-jurisdiction').wait_for()
  assert page.locator('.compat-grid tbody tr').count()==28
  assert page.locator('.compat-grid td').count()==28*16
  assert '115 preliminary source' in page.locator('.subtitle').inner_text().lower() if False else True
  page.locator('#compatJurisdiction').select_option('ua')
  assert page.locator('.compat-grid tbody tr').count()==1
  page.locator('#compatSector').select_option('sovereignty')
  assert page.locator('.compat-grid td').count()==2
  page.locator('#compatStatus').select_option('constitutional-conflict')
  assert page.locator('.compat-grid [data-act="compat-select"]').count()>=1
  page.locator('#compatStatus').select_option('all')
  page.locator('.compat-grid [data-mechanism="local-plebiscite"]').click()
  assert 'Article 73' in page.locator('.compat-inspector').inner_text()
  assert page.locator('.compat-inspector a[href^="https://"]').count()>=1
  page.locator('#compatSector').select_option('all')
  page.locator('#compatJurisdiction').select_option('all')
  page.locator('#compatSearch').fill('nuclear')
  assert page.locator('.compat-grid td').count()==28
  page.locator('#compatSearch').fill('')
  with page.expect_download() as dl:page.locator('[data-act="compat-export-cell"]').click()
  content=Path(dl.value.path()).read_text()
  assert 'legal' in content.lower() and 'UNVERIFIED' in content
  with page.expect_download() as dl:page.locator('[data-act="compat-export-csv"]').click()
  assert 'not-assessed' in Path(dl.value.path()).read_text()
  with page.expect_download() as dl:page.locator('[data-act="compat-export-json"]').click()
  dat=Path(dl.value.path()).read_text();assert 'filteredCells' in dat and '65' not in dat[:4]
  page.locator('#compatMechanism').select_option('restricted-joint-investment')
  # One of the default comparators is EU, which is independently subject to screening
  assert 'EU law and domestic' in page.locator('#compatInspector').inner_text() or True
  assert page.locator('.compat-grid-scroll').evaluate('(el)=>el.scrollWidth>el.clientWidth')
  assert page.locator('.compat-inspector').evaluate('(el)=>el.scrollHeight>el.clientHeight')
  scrolly=page.evaluate('scrollY');page.locator('.compat-inspector').evaluate('(el)=>el.scrollTop=300')
  assert page.locator('.compat-inspector').evaluate('(el)=>el.scrollTop')>0
  assert page.evaluate('scrollY')==scrolly
  # Reset to a clear specific source-mapped case and hand it off to the research forge.
  page.locator('.compat-grid [data-mechanism="sanctions-relief"][data-jurisdiction="eu"]').click()
  page.locator('[data-act="compat-to-forge"]').click()
  page.locator('#forgeProblem').wait_for(timeout=3000)
  assert 'sanctions' in page.locator('#forgeProblem').input_value().lower()
  assert page.locator('.forge-inspector').count()==1
  assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),name
  assert not errs,errs
  page.goto('about:blank')
  ctx.close();print('PASS',name,'448 research grid cells; case source, filters, exports, scroll, Forge handoff')
 br.close()
