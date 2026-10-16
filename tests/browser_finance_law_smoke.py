"""Offline Chromium interaction smoke for financing × legislative gates v4.5."""
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parents[1]
html=(P/'index.html').read_text().replace('<link rel="stylesheet" href="./styles.css">','<style>'+(P/'styles.css').read_text()+'</style>').replace('<script src="./app.js" defer></script>','<script>'+(P/'app.js').read_text()+'</script>')
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for device,w,h in [('desktop',1440,900),('mobile',390,844)]:
  ctx=browser.new_context(viewport={'width':w,'height':h},accept_downloads=True)
  page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(html);page.wait_for_timeout(300)
  if device=='mobile':page.locator('#menuToggle').click()
  page.locator('#routeNav a[href="#/finance-law"]').click()
  page.locator('h1').filter(has_text='Financing × legislative gates').wait_for()
  assert page.locator('.fl-list .clickrow').count()==60
  assert page.locator('.fl-inspector').count()==1
  assert 'No legal green light' in page.locator('.fl-inspector').inner_text()
  page.locator('#flStage').select_option('post-agreement');assert 0<page.locator('.fl-list .clickrow').count()<60
  page.locator('#flStage').select_option('all')
  page.locator('#flJurisdiction').select_option('fi');assert page.locator('.fl-list .clickrow').count()==2
  page.locator('#flJurisdiction').select_option('all')
  page.locator('#flFunding').select_option('euroclear-assets');assert page.locator('.fl-list .clickrow').count()==2
  page.locator('#flFunding').select_option('all')
  page.locator('#flSearch').fill('World Bank');assert page.locator('.fl-list .clickrow').count()==4
  page.locator('#flSearch').fill('');assert page.locator('.fl-list .clickrow').count()==60
  page.locator('.fl-list .clickrow').nth(1).click();assert page.locator('.fl-inspector a[href^="https://"]').count()>0
  assert page.locator('.fl-inspector').evaluate('(e)=>e.scrollHeight>e.clientHeight'), device
  top=page.locator('.fl-inspector').evaluate('(e)=>e.scrollTop');scroll=page.evaluate('scrollY');page.locator('.fl-inspector').evaluate('(e)=>e.scrollTop=250')
  assert page.locator('.fl-inspector').evaluate('(e)=>e.scrollTop')>top and page.evaluate('scrollY')==scroll,device
  with page.expect_download() as dl:page.locator('[data-act="fl-export-md"]').click()
  text=Path(dl.value.path()).read_text();assert 'NO APPROVAL' in text and 'Official legal references' in text
  with page.expect_download() as dl:page.locator('[data-act="fl-export-csv"]').click()
  assert len(Path(dl.value.path()).read_text().splitlines())>170
  with page.expect_download() as dl:page.locator('[data-act="fl-export-json"]').click()
  assert 'research-only-unassessed' in Path(dl.value.path()).read_text()
  # take preview of initial module on desktop/mobile, with no hover/selection obstructing
  page.locator('.fl-list .clickrow').nth(0).click()
  page.locator('.fl-inspector').evaluate('(e)=>e.scrollTop=0')
  page.screenshot(path=str(P/('preview_finance_law_'+device+'.png')),full_page=(device=='mobile'))
  page.locator('[data-act="fl-open-matrix"]').first.click();assert page.locator('h1').filter(has_text='Legislative').count()>0
  page.locator('#routeNav a[href="#/funding"]').click() if device=='desktop' else page.evaluate("location.hash='#/funding'")
  page.locator('h1').filter(has_text='Financing and support').wait_for()
  page.locator('[data-act="fund-select"][data-id="eu-budget"]').click();page.locator('[data-act="finance-law-from-fund"]').click()
  assert page.locator('#flFunding').input_value()=='eu-budget'
  page.locator('[data-act="fl-forge"]').click();assert page.locator('#forgeProblem').input_value().startswith('# Cross-jurisdiction financing law')
  assert page.locator('.forge-inspector').count()==1
  assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),device
  assert not errors,errors
  ctx.close();print('PASS',device,'60 links, filters, legal sources, exports, independent scrolling, matrix/funding/Forge handoff')
 browser.close()
