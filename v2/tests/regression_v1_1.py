#!/usr/bin/env python3
"""Patch-specific UI regression. No network or real P2P join attempted."""
from pathlib import Path
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
errors=[]
with sync_playwright() as pw:
  browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  ctx=browser.new_context(viewport={'width':1440,'height':900})
  p=ctx.new_page();p.on('pageerror',lambda e:errors.append(str(e)))
  p.set_content((R/'index.html').read_text(),wait_until='domcontentloaded',timeout=30000)
  p.locator('[data-route="entities"]').first.click()
  panel=p.locator('.atlas-profile')
  panel.wait_for(timeout=8000)
  measurements=panel.evaluate('(el)=>({visible:el.clientHeight,total:el.scrollHeight,top:el.getBoundingClientRect().top,style:getComputedStyle(el).overflowY})')
  print('Desktop panel:',measurements)
  assert measurements['total']>measurements['visible']+150, 'Entity panel should be independently scrollable'
  assert measurements['style']=='auto'
  p.evaluate('window.scrollTo(0,0)')
  panel.hover();p.mouse.wheel(0,550)
  p.wait_for_timeout(180)
  inside=panel.evaluate('(e)=>e.scrollTop')
  assert inside>10,f'right panel did not scroll: {inside}'
  assert p.evaluate('window.scrollY')<8,'main page scrolled while wheeling over right panel'
  p.locator('#actorPick').select_option('iaea')
  assert 'IAEA' in panel.inner_text()
  panel.evaluate('(e)=>e.scrollTop=e.scrollHeight')
  assert panel.evaluate('(e)=>e.scrollTop')>0
  # Path Forge: unique candidate assignments and no hidden rebuild on selecting existing card.
  p.locator('[data-route="pathways"]').first.click()
  c=p.locator('.path-card');c.first.wait_for(timeout=10000)
  before=c.evaluate_all('(els)=>els.map(e=>e.querySelector(".actors")?.innerText).join("\u2759")')
  assert len(before)>70
  initial_key=c.first.get_attribute('data-path')
  p.locator('[data-action="generate"]').click()
  after=c.evaluate_all('(els)=>els.map(e=>e.querySelector(".actors")?.innerText).join("\u2759")')
  print('Candidate signatures changed:',before!=after)
  assert before!=after,'Regenerate should create at least one different actor assignment'
  assert 'Generation 2' in p.locator('main').inner_text()
  pathid=c.nth(1).get_attribute('data-path')
  c.nth(1).click()
  assert c.nth(1).get_attribute('data-path')==pathid, 'Selecting a pathway must not replace underlying data'
  assert p.locator('.path-card.active').count()==1
  p.locator('#anchorSel').select_option('turkiye')
  p.locator('#extraActor').select_option('india')
  assert 'India' in p.locator('main').inner_text()
  pinnedbefore=p.locator('main').inner_text()
  p.locator('[data-action="generate"]').click()
  assert 'India' in p.locator('main').inner_text()
  assert p.locator('#anchorSel').input_value()=='turkiye'
  # Default community: no network until Join. Stable public room ID and easy switch to private.
  p.locator('[data-route="collaboration"]').first.click()
  assert p.locator('#roomCode').input_value()=='peace-pathways-community-v1'
  assert p.locator('button[data-action="connect"]').inner_text()=='↗ Join community'
  assert 'OFFLINE' in p.locator('main').inner_text()
  p.locator('[data-action="new-room"]').click()
  assert p.locator('#roomCode').input_value().startswith('peace-')
  assert p.locator('button[data-action="connect"]').inner_text()=='↗ Join private room'
  assert p.locator('#roomSecret').count()==1
  p.locator('[data-action="community-room"]').click()
  assert p.locator('#roomCode').input_value()=='peace-pathways-community-v1'
  assert p.locator('#roomSecret').count()==0
  assert p.locator('button[data-action="connect"]').inner_text()=='↗ Join community'
  # Mobile: selected profile appears first and has bounded height, independent scroll.
  p.set_viewport_size({'width':390,'height':844})
  p.locator('#menuBtn').click()
  p.locator('#sidebar [data-route="entities"]').click()
  mobile=panel.evaluate('(el)=>({visible:el.clientHeight,total:el.scrollHeight,style:getComputedStyle(el).overflowY})')
  assert mobile['total']>mobile['visible']
  assert mobile['style']=='auto'
  assert p.locator('.atlas-profile-wrap').evaluate('(e)=>getComputedStyle(e).order')=='-1'
  assert not errors,'Uncaught JS errors: '+str(errors)
  print('PASS v1.1: independent desktop and mobile atlas scrolling; changed alternatives; stable selections; pins retained; default opt-in community/private flows.')
  browser.close()
