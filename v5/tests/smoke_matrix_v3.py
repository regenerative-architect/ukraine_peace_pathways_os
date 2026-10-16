"""Browser smoke; uses Chromium if present, otherwise report missing runtime (non-passing)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parents[1]
h=(p/'index.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="./styles.css">','<style>'+(p/'styles.css').read_text()+'</style>').replace('<script src="./app.js" defer></script>','<script>'+(p/'app.js').read_text()+'</script>')
with sync_playwright() as play:
 browser=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 ctx=browser.new_context(accept_downloads=True,viewport={'width':1366,'height':880});page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.set_content(h);page.wait_for_timeout(350)
 page.locator('a[href="#/matrix"]').click();assert 'Multi-track diplomacy matrix' in page.locator('h1').inner_text()
 print('Matrix candidates:',page.locator('[data-act="select-path"]').count());assert page.locator('[data-act="select-path"]').count()==13
 assert page.get_by_text('30 km heavy-artillery separation hypothesis').count()>=1
 page.locator('#matrixTrack').select_option('t2');assert page.locator('[data-act="select-path"]').count()==3
 page.locator('[data-act="select-path"]').filter(has_text='Five-year').click()
 assert 'coercive' in page.locator('.profile-scroll').inner_text().lower() or 'coercion' in page.locator('.profile-scroll').inner_text().lower()
 with page.expect_download() as d:page.locator('[data-act="export-pathway"]').click()
 memo=d.value.path().read_text();assert 'REFERENDUM' in memo.upper() and 'Classification:' in memo
 page.locator('[data-act="example"]').last.click();assert page.locator('h1').inner_text()=='Negotiation workbench'
 assert page.locator('[data-gate="scope-sovereignty"]').count()==3
 page.locator('a[href="#/bargaining"]').click()
 page.locator('h1').filter(has_text='Incentives and credible commitments').wait_for(timeout=5000)
 page.locator('[name="ukraine_outside"]').fill('Analyst hypothesis: minimum sovereign-law protections; external verification required.')
 page.locator('[name="russia_blocker"]').fill('Unknown: no official counterparty position documented.')
 page.locator('#bargainingForm button[type="submit"]').click()
 assert 'Analyst hypothesis' in page.locator('[name="ukraine_outside"]').input_value()
 page.locator('a[href="#/workbench"]').first.click()
 with page.expect_download() as d:page.locator('[data-act="export-memo"]').first.click()
 memo=d.value.path().read_text();assert 'Bargaining incentive hypotheses' in memo and 'Analyst hypothesis' in memo
 page.locator('a[href="#/issues"]').click();page.locator('[data-act="select-issue"][data-id="ai-assisted-mine-action"]').click()
 assert page.get_by_text('Human-supervised',exact=False).count()>0
 page.screenshot(path=str(p/'tests/desktop_matrix_v3.png'),full_page=True)
 print('Desktop errors:',errors);assert not errors
 mobile=browser.new_context(viewport={'width':390,'height':844});pm=mobile.new_page();me=[];pm.on('pageerror',lambda e:me.append(str(e)));pm.set_content(h);pm.wait_for_timeout(350)
 pm.locator('#menuToggle').click();pm.locator('a[href="#/matrix"]').click();assert not pm.evaluate('document.documentElement.scrollWidth>innerWidth')
 pm.screenshot(path=str(p/'tests/mobile_matrix_v3.png'),full_page=True)
 print('Mobile errors:',me);assert not me
 browser.close()
print('BROWSER V3 PASS')
