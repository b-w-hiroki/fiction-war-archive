import { chromium } from 'playwright';
import fs from 'node:fs';

const base='http://127.0.0.1:8000';
const files=fs.readdirSync('docs/ginei').filter(f=>f.endsWith('.html')&&f!=='index.html'&&f!=='strategy.html').sort();
const browser=await chromium.launch({headless:true,args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});
const failures=[];
for(const file of files){
  const page=await browser.newPage({viewport:{width:390,height:844}});
  const errors=[];
  page.on('pageerror',e=>errors.push('pageerror: '+e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push('console: '+m.text())});
  try{
    const res=await page.goto(base+'/ginei/'+file,{waitUntil:'networkidle',timeout:30000});
    if(!res||!res.ok()) throw new Error('HTTP '+(res&&res.status()));
    await page.waitForSelector('#stage canvas',{timeout:15000});
    const state=await page.evaluate(()=>({
      three:typeof THREE!=='undefined',
      canvas:!!document.querySelector('#stage canvas'),
      steps:document.querySelectorAll('#steps button').length,
      title:document.querySelector('#cTitle')?.textContent||'',
      play:!!document.querySelector('#play'),
      result:!!document.querySelector('#resOpen')
    }));
    if(!state.three||!state.canvas||!state.steps||!state.play||!state.result) throw new Error('UI init failed '+JSON.stringify(state));
    const steps=page.locator('#steps button');
    if(await steps.count()>1){await steps.nth(1).click(); await page.waitForTimeout(250);}
    await page.locator('#play').click(); await page.waitForTimeout(400); await page.locator('#play').click();
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
