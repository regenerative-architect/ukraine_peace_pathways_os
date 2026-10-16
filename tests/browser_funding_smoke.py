"""Standalone offline Chromium desktop and mobile funding catalog checks."""
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parents[1]
html=(P/'index.html').read_text().replace('<link rel="stylesheet" href="./styles.css">','<style>'+(P/'styles.css').read_text()+'</style>').replace('<script src="./app.js" defer></script>','<script>'+(P/'app.js').read_text()+'</script>')
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for device,w,h in [('desktop',1440,900),('mobile',390,844)]:
  ctx=browser.new_context(viewport={'width':w,'height':h},accept_downloads=True)
  page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.set_content(html);page.wait_for_timeout(300)
  if device=='mobile':page.locator('#menuToggle').click()
  page.locator('#routeNav a[href="#/funding"]').click();page.locator('h1').filter(has_text='Financing and support').wait_for()
  assert page.locator('.funding-list .clickrow').count()==30
  assert '30 SOURCED DOSSIERS' in page.locator('.eyebrow').inner_text()
  page.locator('#fundStatus').select_option('confirmed-recurring');assert 1<page.locator('.funding-list .clickrow').count()<30
  page.locator('#fundStatus').select_option('all')
  page.locator('#fundChannel').select_option('external-material-to-russia');assert page.locator('.funding-list .clickrow').count()==2
  page.locator('#fundChannel').select_option('all')
  page.locator('#fundQuery').fill('World Bank');assert page.locator('.funding-list .clickrow').count()==2
  page.locator('#fundQuery').fill('');assert page.locator('.funding-list .clickrow').count()==30
  page.locator('[data-act="fund-select"][data-id="rus-budget"]').click()
  assert 'state budget' in page.locator('.funding-inspector').inner_text().lower()
  assert page.locator('.funding-inspector a[href^="https://"]').count()>0
  assert page.locator('.funding-inspector').evaluate('(e)=>e.scrollHeight>e.clientHeight'),device
  sy=page.evaluate('scrollY');page.locator('.funding-inspector').evaluate('(e)=>e.scrollTop=250')
  assert page.locator('.funding-inspector').evaluate('(e)=>e.scrollTop')>0 and page.evaluate('scrollY')==sy
  with page.expect_download() as dl:page.locator('[data-act="fund-export"]').click()
  assert 'Oil' in Path(dl.value.path()).read_text() or 'Russian' in Path(dl.value.path()).read_text()
  with page.expect_download() as dl:page.locator('[data-act="fund-export-csv"]').click()
  assert Path(dl.value.path()).read_text().count('\n')>=29
  page.locator('[data-act="fund-to-actor"]').click()
  assert 'Documented funding/support relationships' in page.locator('.profile-scroll').inner_text()
  page.locator('#fundOnly').check();assert page.locator('.catalog-scroll .clickrow').count()<=78
  page.locator('[data-act="fund-select"][data-id="rus-budget"]').click()
  page.locator('[data-act="fund-forge"]').click()
  assert 'Russian federal' in page.locator('#forgeProblem').input_value()
  assert page.locator('.forge-inspector').count()==1
  assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),device
  assert not errors,errors
  page.screenshot(path=str(P/('preview_funding_'+device+'.png')))
  ctx.close();print('PASS',device,'catalog filters, sources, exports, dossiers, stakeholder and Forge handoffs, independent scroll')
 browser.close()
