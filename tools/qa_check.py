# -*- coding: utf-8 -*-
"""Automated QA/UAT for 쌤플레이: every sample end-to-end, images, mobile overflow, a11y basics, console errors."""
import sys, json
from playwright.sync_api import sync_playwright
URL = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/index.html'
issues = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for vw, label in [(1280, 'desktop'), (390, 'mobile')]:
        pg = b.new_page(viewport={'width': vw, 'height': 860})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        pg.goto(URL + '?qa=' + label); pg.wait_for_timeout(1200)
        # gallery: scroll to load every lazy thumb
        pg.evaluate("document.querySelectorAll('#groups img.thumb').forEach(i=>i.loading='eager')")
        pg.wait_for_timeout(2500)
        broken = pg.evaluate("[...document.querySelectorAll('#groups img.thumb')].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src.split('/').pop())")
        if broken: issues.append(f'[{label}] broken thumbs: {broken}')
        ov = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
        if ov > 1: issues.append(f'[{label}] horizontal overflow on gallery: {ov}px')
        unnamed = pg.evaluate("[...document.querySelectorAll('button,a')].filter(e=>e.offsetParent&&!(e.textContent.trim()||e.getAttribute('aria-label')||e.title)).map(e=>e.id||e.className)")
        if unnamed: issues.append(f'[{label}] buttons/links without accessible name: {unnamed}')
        if label == 'mobile':
            res = pg.evaluate("""async()=>{const out=[];const w=ms=>new Promise(r=>setTimeout(r,ms));
              for(const s of samples){
                enterWork(s.key,false,true);await w(30);
                const img=$('selImage');await new Promise(r=>{if(img.complete)r();else{img.onload=img.onerror=r}});
                if(!img.naturalWidth)out.push(s.key+': preview image failed');
                for(let i=0;i<3;i++){$('fillEx').click();await w(10);
                  if(!validate())out.push(s.key+': preset '+i+' fails validation');
                  const o=$('output').value;if(o.length<300)out.push(s.key+': prompt too short');
                  if(!o.includes(val('topic')))out.push(s.key+': prompt missing topic');
                  if(/undefined|null|NaN|\\$\\{/.test(o))out.push(s.key+': prompt has template junk');}
                const ov=document.documentElement.scrollWidth-document.documentElement.clientWidth;if(ov>1)out.push(s.key+': overflow '+ov);
                for(const k of ['topic','extra','content']){if(!document.querySelectorAll('#'+k+'ExList button').length)out.push(s.key+': no '+k+' examples')}
              }return out}""")
            issues += ['[uat] ' + x for x in res]
        if errs: issues.append(f'[{label}] console errors: {errs[:5]}')
        pg.close()
    b.close()
print(json.dumps({'issues': issues, 'count': len(issues)}, ensure_ascii=False, indent=1))
