#!/usr/bin/env python3
"""Chromium UI smoke test with set_content() for environments where localhost/file URLs are blocked.
Run hosted in a network-permitting browser to test IndexedDB, service worker and real P2P.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
errors=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 context=browser.new_context(viewport={'width':1370,'height':940},accept_downloads=True)
 page=context.new_page();page.on('pageerror',lambda error:errors.append(str(error)))
 page.set_content((R/'index.html').read_text(encoding='utf-8'),wait_until='domcontentloaded',timeout=20000)
 assert '75' in page.locator('main').inner_text()
 page.locator('[data-route="entities"]').first.click()
 page.locator('article[data-entity]').first.wait_for(timeout=10000)
 assert page.locator('article[data-entity]').count()==75
 page.locator('#globalSearch').fill('IAEA')
 assert page.locator('article[data-entity]').count()==1
 page.locator('#globalSearch').fill('')
 page.locator('[data-entity="iaea"]').first.click()
 assert 'IAEA' in page.locator('main').inner_text()
 page.locator('[data-guide^="iaea__"]').first.click()
 assert page.locator('#inspector.open').count()==1
 cb=page.locator('#panelBody input[data-complete]').first
 cb.check()
 assert cb.is_checked()
 assert '1/' in page.locator('#panelBody').inner_text()
 page.locator('#panelBody [data-set-depth="advanced"]').click()
 assert page.locator('#panelBody input[data-complete]').count()>=7
 page.locator('#guideNotes').fill('Private review: require documented civilian protection outcome.')
 page.locator('[data-save-note]').click()
 assert 'Local notes saved' in page.locator('#toast').inner_text()
 page.locator('#closePanel').click()
 page.locator('[data-route="pathways"]').first.click()
 page.locator('.path-card').first.wait_for(timeout=15000)
 assert page.locator('.path-card').count()>1
 assert 'Direct-party assent required' in page.locator('main').inner_text()
 page.locator('#anchorSel').select_option('turkiye')
 page.locator('#extraActor').select_option('india')
 assert 'India' in page.locator('main').inner_text()
 page.locator('[data-save-path]').first.click()
 page.locator('[data-route="collaboration"]').first.click()
 page.locator('#sharePath').wait_for(timeout=10000)
 assert page.locator('#sharePath option').count()==1 and 'Save a path first' not in page.locator('#sharePath').inner_text()
 page.locator('[data-action="new-room"]').click()
 assert page.locator('#roomCode').input_value().startswith('peace-')
 page.locator('[data-route="settings"]').first.click()
 with page.expect_download(timeout=10000) as info:page.locator('[data-action="export-backup"]').last.click()
 assert info.value.suggested_filename=='peace-pathways-workspace.json'
 page.on('dialog',lambda dialog:dialog.accept())
 from pathlib import Path as _P
 backup_bytes=_P(info.value.path()).read_bytes()
 page.locator('#fileImport').set_input_files({'name':'workspace.json','mimeType':'application/json','buffer':backup_bytes})
 page.wait_for_timeout(250)
 assert 'Backup imported' in page.locator('#toast').inner_text()
 page.set_viewport_size({'width':390,'height':844})
 page.locator('#menuBtn').click()
 assert 'open' in page.locator('#sidebar').get_attribute('class')
 page.locator('#sidebar [data-route="evidence"]').click()
 page.get_by_role('heading',name='Evidence & safeguards').wait_for(timeout=10000)
 assert 'Evidence & safeguards' in page.locator('main').inner_text()
 assert not errors, 'JS errors: '+str(errors)
 browser.close()
print('PASS UI: routes, 75 entities, search, guide steps and depth, combinatorial pathways, pinned actors, saved drafts, room-code generation, JSON download, mobile nav, evidence, no page exceptions.')
print('NOT TESTED HERE: HTTP-hosted service worker offline reload, cross-network WebRTC, IndexedDB persistence: environment disallows localhost/file navigation.')
