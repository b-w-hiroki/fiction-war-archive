import { chromium } from 'playwright';
import fs from 'node:fs';

const base='http://127.0.0.1:8000';
const files=fs.readdirSync('docs/ginei').filter(f=>f.endsWith('.html')&&f!=='index.html'&&f!=='strategy.html').sort();
const three=fs.readFileSync('node_modules/three/build/three.min.js');
const browser=await chromium.launch({headless:true,args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});
const failures=[];
for(const file of files){
  const page=await browser.newPage({viewport:{width:390,height:844}});
  const errors=[];
  await page.route('https://cdnjs.cloudflare.com/ajax/libs/three.js/**',route=>route.fulfill({status:200,contentType:'application/javascript',body:three}));
  await page.route('https://fonts.googleapis.com/**',route=>route.fulfill({status:200,contentType:'text/css',body:''}));
  page.on('pageerror',e=>errors.push('pageerror: '+e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push('console: '+m.text())});
  try{
    const res=await page.goto(base+'/ginei/'+file,{waitUntil:'domcontentloaded',timeout:12000});
    if(!res||!res.ok()) throw new Error('HTTP '+(res&&res.status()));
    await page.waitForSelector('#stage canvas',{timeout:15000});
    const state=await page.evaluate(()=>({
      three:typeof THREE!=='undefined',
      canvas:!!document.querySelector('#stage canvas'),
      steps:document.querySelectorAll('#steps button').length,
      title:document.querySelector('#cTitle')?.textContent||'',
      play:!!document.querySelector('#play'),
      result:!!document.querySelector('#resOpen'),
      seek:!!document.querySelector('#phaseSeek'),
      seekMax:Number(document.querySelector('#phaseSeek')?.max||-1),
      mobileStepsHidden:getComputedStyle(document.querySelector('#steps')).display==='none',
      mobileTitleHorizontal:getComputedStyle(document.querySelector('.title')).writingMode==='horizontal-tb',
      capMore:!!document.querySelector('#capMore'),
      focusToggle:!!document.querySelector('#focusToggle')
    }));
    if(!state.three||!state.canvas||!state.steps||!state.play||!state.result||!state.seek||!state.capMore||!state.mobileStepsHidden||!state.mobileTitleHorizontal||!state.focusToggle||state.seekMax!==1000) throw new Error('UI init failed '+JSON.stringify(state));
    const steps=page.locator('#steps button');
    await page.locator('#focusToggle').click();
    const focusState=await page.evaluate(()=>({
      focus:document.querySelector('#hud').classList.contains('focus'),
      pressed:document.querySelector('#focusToggle').getAttribute('aria-pressed'),
      forceHidden:getComputedStyle(document.querySelector('.force')).visibility==='hidden',
      capHidden:getComputedStyle(document.querySelector('#cap')).visibility==='hidden',
      seekHidden:getComputedStyle(document.querySelector('.seek')).visibility==='hidden',
      playVisible:getComputedStyle(document.querySelector('#play')).visibility!=='hidden'
    }));
    if(!focusState.focus||focusState.pressed!=='true'||!focusState.forceHidden||!focusState.capHidden||!focusState.seekHidden||!focusState.playVisible) throw new Error('focus mode failed '+JSON.stringify(focusState));
    await page.locator('#focusToggle').click();
    if(await page.locator('#hud').evaluate(el=>el.classList.contains('focus'))) throw new Error('focus mode did not restore UI');
    if(await steps.count()>2){
      const seek=page.locator('#phaseSeek');
      const startNow=await page.locator('#seekNow').textContent();
      await seek.evaluate(el=>{el.value='500';el.dispatchEvent(new Event('input',{bubbles:true}))});await page.waitForTimeout(120);
      const mid=await seek.inputValue();
      const now=await page.locator('#seekNow').textContent();
      const aria=await seek.getAttribute('aria-valuenow');
      if(mid!=='500'||!now?.includes('.')||now===startNow||aria!=='50') throw new Error('seekbar did not scrub continuously: '+JSON.stringify({mid,now,startNow,aria}));
      await seek.evaluate(el=>{el.value='1000';el.dispatchEvent(new Event('input',{bubbles:true}))});await page.waitForTimeout(80);
      if(await seek.inputValue()!=='1000') throw new Error('seekbar did not reach end');
      await seek.evaluate(el=>{el.value='0';el.dispatchEvent(new Event('input',{bubbles:true}));el.dispatchEvent(new Event('change',{bubbles:true}))});await page.waitForTimeout(80);
    }
    await page.locator('#capMore').click();
    if(!await page.locator('#cap').evaluate(el=>el.classList.contains('expanded'))) throw new Error('mobile caption did not expand');
    await page.locator('#capMore').click();
    const initialTitle=await page.locator('#cTitle').textContent();
    await page.locator('#play').click();
    await page.waitForTimeout(350);
    const advancedTitle=await page.locator('#cTitle').textContent();
    if(await steps.count()>1 && advancedTitle===initialTitle) throw new Error('first play did not advance from initial phase');
    await page.locator('#play').click();
    const effectPhase={'fortress.html':5,'amritsar.html':4,'vermilion.html':5,'corridor.html':3,'maradetta.html':4,'shiva.html':2,'iser7.html':4}[file];
    if(effectPhase!==undefined){
      const seek=page.locator('#phaseSeek');
      await seek.fill(String(effectPhase));await seek.dispatchEvent('input');await page.waitForTimeout(80);
      await page.locator('#spd').click();await page.locator('#spd').click();await page.locator('#spd').click();
      await page.locator('#play').click();await page.waitForTimeout(2700);await page.locator('#play').click();
      if(errors.length) throw new Error('effect phase failed: '+errors.join(' | '));
    }
    await page.locator('#resOpen').click(); await page.waitForSelector('#res.on',{timeout:3000});
    await page.locator('#resClose').click(); await page.waitForTimeout(100);
    if(errors.length) throw new Error(errors.join(' | '));
    console.log('OK',file,state.steps,state.title);
  }catch(e){
    failures.push({file,error:String(e),errors});
    console.error('FAIL',file,String(e));
  }finally{await page.close();}
}
await browser.close();
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
console.log('All ginei pages passed:',files.length);
