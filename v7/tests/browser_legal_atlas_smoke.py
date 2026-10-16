"""Headless browser checks for legal documentation atlas. Synthetic page: no live network calls."""
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parents[1]
html=(P/'index.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="./styles.css">','<style>'+(P/'styles.css').read_text()+'</style>').replace('<script src="./app.js" defer></script>','<script>'+(P/'app.js').read_text()+'</script>')
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for name,width,height in [('desktop',1440,900),('mobile',390,844)]:
  ctx=browser.new_context(viewport={'width':width,'height':height},accept_downloads=True)
  page=ctx.new_page();errors=[];page.on('pageerror',lambda x:errors.append(str(x)))
  page.set_content(html);page.wait_for_timeout(350)
  if name=='mobile':page.locator('#menuToggle').click()
  page.locator('#routeNav a[href="#/legal"]').click();page.locator('h1').filter(has_text='Legal & institutional').wait_for()
  assert page.locator('#legalList button').count()==59
  assert page.locator('#legalCount').inner_text().startswith('59 of 59')
  page.locator('#legalJurisdiction').select_option('ua')
  assert page.locator('#legalList button').count()==4
  page.locator('#legalJurisdiction').select_option('all')
  page.locator('#legalCategory').select_option('sanctions')
  assert page.locator('#legalList button').count()>6
  page.locator('#legalCategory').select_option('all')
  page.locator('#legalSearch').fill('Geneva')
  assert page.locator('#legalList button').count()==0
  page.locator('#legalSearch').fill('Ukraine')
  assert page.locator('#legalList button').count()>2
  page.locator('#legalSearch').fill('')
  page.locator('#legalList button').last.click()
  assert page.locator('#legalInspector a[href^="https://"]').count()==1
  assert page.locator('#legalInspector').inner_text().strip()
  with page.expect_download() as exp:page.locator('[data-act="legal-export-selected"]').click()
  exported=Path(exp.value.path()).read_text()
  assert 'UNVERIFIED' in exported and 'Publisher URL:' in exported
  with page.expect_download() as exp:page.locator('[data-act="legal-export-list"]').click()
  assert Path(exp.value.path()).read_text().count('https://')>=59
  with page.expect_download() as exp:page.locator('[data-act="legal-export-json"]').click()
  assert 'schemaVersion' in Path(exp.value.path()).read_text()
  assert page.locator('.legal-inspector').evaluate('(el)=>el.scrollHeight > el.clientHeight')
  oldmain=page.evaluate('scrollY');page.locator('.legal-inspector').evaluate('(el)=>el.scrollTop=240')
  assert page.locator('.legal-inspector').evaluate('(el)=>el.scrollTop')>0
  assert page.evaluate('scrollY')==oldmain
  page.locator('#legalList button').first.click();page.locator('.legal-inspector').evaluate('(el)=>el.scrollTop=0');page.locator('.legal-list').evaluate('(el)=>el.scrollTop=0');page.evaluate('window.scrollTo(0,0)');page.wait_for_timeout(100)
  page.screenshot(path=str(P/f'preview_legal_atlas_{name}.png'),full_page=True)
  page.locator('[data-act="legal-to-forge"]').click()
  page.locator('.forge-inspector').wait_for(timeout=5000)
  assert page.locator('.forge-inspector').count()==1
  assert 'legal applicability' in page.locator('#forgeProblem').input_value().lower()
  assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),name
  assert not errors,errors
  print('PASS',name,'59 links; jurisdiction, topic and search filters; exports; Forge handoff; independent right scroll; zero JS errors')
  ctx.close()
 browser.close()
