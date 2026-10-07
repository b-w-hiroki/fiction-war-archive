import { chromium } from 'playwright';
import fs from 'node:fs';

const cases=[
  {url:'/ginei/astarte.html',legend:['艦隊'],src:["kind:'fleet'","r:'close'","r:'far'"]},
  {url:'/kingdom/kankoku.html',legend:['歩兵','騎兵'],src:["kind:'infantry'","kind:'cavalry'","r:'close'","r:'far'"]},
  {url:'/gundam-uc0079/odessa.html',legend:['要塞','陸上兵器','艦船'],src:["kind:'fortress'","kind:'ground_vehicle'","kind:'ship'","r:'close'","r:'far'"]},
  {url:'/gundam-uc0079/garma.html',legend:['航空機','陸上兵器','艦船'],src:["kind:'aircraft'","kind:'ground_vehicle'","kind:'ship'","r:'close'","r:'far'"]},
  {url:'/arslan/atropatene1.html',legend:['歩兵','騎兵'],src:["kind:'infantry'","kind:'cavalry'","r:'close'","r:'far'"]}
];
const base='http://127.0.0.1:8000';
const browser=await chromium.launch({headless:true,args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});
const failures=[];
for(const c of cases){
  const disk='docs'+c.url;
  const html=fs.readFileSync(disk,'utf8');
  for(const token of ['function inferKind','function combatMode','function closeClash','function arcShot',...c.src]){
    if(!html.includes(token)) failures.push({url:c.url,error:'missing '+token});
  }
  const page=await browser.newPage({viewport:{width:390,height:844}});
  const errors=[];
  page.on('pageerror',e=>errors.push('pageerror: '+e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push('console: '+m.text())});
  try{
    const res=await page.goto(base+c.url,{waitUntil:'domcontentloaded',timeout:15000});
    if(!res||!res.ok()) throw new Error('HTTP '+(res&&res.status()));
    await page.waitForSelector('#stage canvas',{timeout:15000});
    await page.waitForTimeout(500);
    const state=await page.evaluate(()=>({
      legend:[...document.querySelectorAll('#kindLegend .k')].map(x=>x.textContent.trim()),
      canvas:!!document.querySelector('#stage canvas'),
      overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth+1
    }));
    for(const label of c.legend) if(!state.legend.includes(label)) throw new Error('legend missing '+label+' '+JSON.stringify(state.legend));
    if(!state.canvas) throw new Error('canvas missing');
    if(state.overflow) throw new Error('horizontal overflow');
    const seek=page.locator('#phaseSeek');
    await seek.fill('500');await seek.dispatchEvent('input');await page.waitForTimeout(250);
    await seek.dispatchEvent('change');await page.locator('#play').click();await page.waitForTimeout(900);await page.locator('#play').click();
    if(errors.length) throw new Error(errors.join(' | '));
    console.log('OK',c.url,state.legend.join(','));
  }catch(e){
    failures.push({url:c.url,error:String(e),errors});
    console.error('FAIL',c.url,String(e));
  }finally{await page.close()}
}
await browser.close();
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
console.log('Unit kind/range QA passed:',cases.length);
