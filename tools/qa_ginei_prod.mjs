import { chromium } from 'playwright';
const base='https://fiction-war-archive.birdman-studio.com';
const files=['astarte.html','amritsar.html','fortress.html','vermilion.html'];
const browser=await chromium.launch({headless:true,args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});
const failures=[];
for(const file of files){
  const page=await browser.newPage({viewport:{width:390,height:844}});
  const errors=[];
  page.on('pageerror',e=>errors.push('pageerror: '+e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push('console: '+m.text())});
  try{
    const url=base+'/ginei/'+file;
    const res=await page.goto(url,{waitUntil:'domcontentloaded',timeout:20000});
    if(!res||!res.ok()) throw new Error('HTTP '+(res&&res.status())+' '+url);
    await page.waitForSelector('#stage canvas',{timeout:15000});
    const state=await page.evaluate(()=>({three:typeof THREE!=='undefined',steps:document.querySelectorAll('#steps button').length,title:document.querySelector('#cTitle')?.textContent||''}));
    if(!state.three||!state.steps) throw new Error('init failed '+JSON.stringify(state));
    const steps=page.locator('#steps button'); if(await steps.count()>1) await steps.nth(1).click();
    await page.locator('#play').click(); await page.waitForTimeout(350); await page.locator('#play').click();
    await page.locator('#resOpen').click(); await page.waitForSelector('#res.on',{timeout:3000});
    if(errors.length) throw new Error(errors.join(' | '));
    console.log('PROD OK',file,state.steps,state.title);
  }catch(e){failures.push({file,error:String(e),errors});console.error('PROD FAIL',file,String(e))}
  await page.close();
}
await browser.close();
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
