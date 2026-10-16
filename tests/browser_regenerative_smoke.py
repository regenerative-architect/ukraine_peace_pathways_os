"""Manual Playwright smoke test; no external network required."""
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parents[1]
h=(P/'index.html').read_text(encoding='utf-8').replace('<link rel="stylesheet" href="./styles.css">','<style>'+(P/'styles.css').read_text()+'</style>').replace('<script src="./app.js" defer></script>','<script>'+(P/'app.js').read_text()+'</script>')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for name,width,height in [('desktop',1440,900),('mobile',390,844)]:
  ctx=b.new_context(viewport={'width':width,'height':height},accept_downloads=True)
  pg=ctx.new_page();errs=[];pg.on('pageerror',lambda x:errs.append(str(x)));pg.set_content(h);pg.wait_for_timeout(400)
  if name=='mobile':pg.locator('#menuToggle').click()
  pg.locator('a[href="#/regeneration"]').click()
  pg.locator('h1').filter(has_text='Conflict funding').wait_for()
  assert pg.locator('[data-act="regen-select"]').count()==14
  assert pg.locator('.regen-inspector').count()==1
  pg.locator('#regenMode').select_option('post-agreement')
  assert pg.locator('[data-act="regen-select"]').count()>=2
  pg.locator('#regenMode').select_option('all')
  pg.locator('#regenKind').select_option('russian-state')
  assert pg.locator('[data-act="regen-select"]').count()>=2
  pg.locator('#regenKind').select_option('all')
  pg.locator('[data-act="regen-select"]').last.click()
  assert pg.locator('.regen-inspector').inner_text().strip()
  with pg.expect_download() as d:pg.locator('[data-act="regen-export"]').click()
  content=Path(d.value.path()).read_text()
  assert 'UNVERIFIED' in content and 'LEGAL' in content.upper() and '##' in content
  z=pg.locator('.regen-inspector').evaluate('(el)=>({sh:el.scrollHeight,ch:el.clientHeight})')
  assert z['sh']>z['ch'],('inspector overflow',z,name)
  pg.locator('.regen-inspector').evaluate('(el)=>el.scrollTop=220')
  assert pg.locator('.regen-inspector').evaluate('(el)=>el.scrollTop')>0
  pg.evaluate('window.scrollTo(0,0)');pg.wait_for_timeout(200)
  pg.screenshot(path=str(P/f'preview_regeneration_{name}.png'),full_page=True)
  pg.locator('[data-act="regen-to-forge"]').click()
  pg.locator('.forge-inspector').wait_for(timeout=5000);assert pg.locator('.forge-inspector').count()==1
  assert 'regenerative financing mechanism' in pg.locator('#forgeProblem').input_value().lower()
  assert pg.locator('.forge-inspector').evaluate('(el)=>el.scrollHeight > el.clientHeight')
  pg.locator('.forge-inspector').evaluate('(el)=>el.scrollTop=160')
  assert pg.locator('.forge-inspector').evaluate('(el)=>el.scrollTop')>0
  assert not pg.evaluate('document.documentElement.scrollWidth>innerWidth')
  assert not errs,errs
  print('PASS',name,'14 options, filters, export, both independently scrolling inspectors, no JS errors or overflow')
  ctx.close()
 b.close()
