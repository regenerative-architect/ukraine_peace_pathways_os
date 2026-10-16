/* HTTPS/localhost only. Versioned, same-origin, cache-first static shell; no hidden network requests. */
const VERSION='peace-pathways-shell-v1-2026-10-16';
const CORE=['./','./index.html','./manifest.webmanifest','./assets/icon-192.png','./assets/icon-512.png','./data/entities.json','./data/solutions.json','./data/guide-bank.json','./data/evidence.json','./data/pathway-catalog.json'];
self.addEventListener('install',event=>{
  event.waitUntil((async()=>{const c=await caches.open(VERSION);await c.addAll(CORE)})());
  // Do not skipWaiting: preserve an open session until tabs are closed/reloaded.
});
self.addEventListener('activate',event=>event.waitUntil((async()=>{
 const keys=await caches.keys();await Promise.all(keys.filter(x=>x.startsWith('peace-pathways-shell-')&&x!==VERSION).map(x=>caches.delete(x)));
 await self.clients.claim();
})()));
self.addEventListener('fetch',event=>{
 const req=event.request;
 if(req.method!=='GET')return;
 const u=new URL(req.url);
 if(u.origin!==self.location.origin)return; // never cache public relays or CDN transport
 if(req.mode==='navigate'){
  event.respondWith((async()=>{try{return await fetch(req)}catch{const cache=await caches.open(VERSION);return await cache.match('./index.html')||Response.error()}})());return;
 }
 event.respondWith((async()=>{
  const cache=await caches.open(VERSION),hit=await cache.match(req);
  if(hit)return hit;
  return await fetch(req); // no automatic cache of arbitrary URLs
 })());
});
