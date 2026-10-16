"""Host a local test server, check offline shell and IndexedDB across page reloads."""
from pathlib import Path
import contextlib
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from playwright.sync_api import sync_playwright
import time
root=Path(__file__).resolve().parents[1]
handler=partial(SimpleHTTPRequestHandler,directory=str(root))
server=ThreadingHTTPServer(('127.0.0.1',0),handler)
thread=Thread(target=server.serve_forever,daemon=True);thread.start()
base=f'http://127.0.0.1:{server.server_address[1]}/'
try:
 with sync_playwright() as pp:
  browser=pp.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  ctx=browser.new_context(viewport={'width':1180,'height':900})
  page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(base+'index.html');page.wait_for_timeout(1300)
  page.evaluate('navigator.serviceWorker.ready')
  print('SW ready:',page.evaluate('!!navigator.serviceWorker.controller'))
  page.locator('a[href="#/issues"]').click();page.locator('[data-act="select-issue"][data-id="nuclear-safety-zone"]').click()
  page.locator('button[data-act="example"]').first.click();page.locator('[name="title"]').fill('HOSTED PERSISTENCE TEST')
  page.locator('#caseForm button[type="submit"]').click();page.wait_for_timeout(500)
  page.reload();page.wait_for_timeout(350);page.locator('a[href="#/workbench"]').first.click()
  assert 'HOSTED PERSISTENCE TEST' in page.locator('[name="title"]').input_value()
  page.locator('a[href="#/settings"]').click();page.locator('[data-act="check-sw"]').click();page.wait_for_timeout(200)
  print('Cache:',page.locator('#swInfo').inner_text())
  ctx.set_offline(True)
  page.goto(base+'index.html');page.wait_for_timeout(350)
  assert 'From conceptual pathways' in page.locator('h1').inner_text()
  assert page.locator('#netStatus').inner_text().startswith('Offline')
  page.locator('a[href="#/workbench"]').first.click()
  assert 'HOSTED PERSISTENCE TEST' in page.locator('[name="title"]').input_value()
  print('OFFLINE RELOAD AND CASE PERSISTENCE PASS; page errors',errors)
  assert not errors
  browser.close()
finally:
 server.shutdown();server.server_close();thread.join(timeout=2)
