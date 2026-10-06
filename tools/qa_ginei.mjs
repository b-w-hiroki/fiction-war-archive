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
      shockwave:typeof shockwave==='function'
    }));
    if(!state.three||!state.canvas||!state.steps||!state.play||!state.result||!state.seek||!state.shockwave||state.seekMax!==state.steps-1) throw new Error('UI init failed '+JSON.stringify(state));
    const steps=page.locator('#steps button');
    if(await steps.count()>2){
      const seek=page.locator('#phaseSeek');
      await seek.fill(String((await steps.count())-1));
      await seek.dispatchEvent('input');
      await page.waitForTimeout(120);
      const v=await seek.inputValue();
      const now=await page.locator('#seekNow').textContent();
      if(v!==String((await steps.count())-1)||!now?.startsWith(String(await steps.count()))) throw new Error('seekbar did not jump to final phase');
      await seek.fill('0');await seek.dispatchEvent('input');await page.waitForTimeout(80);
    }
    const initialTitle=await page.locator('#cTitle').textContent();
    await page.locator('#play').click();
    await page.waitForTimeout(350);
    const advancedTitle=await page.locator('#cTitle').textContent();
    if(await steps.count()>1 && advancedTitle===initialTitle) throw new Error('first play did not advance from initial phase');
    await page.locator('#play').click();
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
