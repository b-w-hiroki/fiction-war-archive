import { chromium } from 'playwright';

const base='http://127.0.0.1:8000';
const browser=await chromium.launch({headless:true});
const widths=[390,320];
const failures=[];
for(const width of widths){
  const page=await browser.newPage({viewport:{width,height:844}});
  const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  try{
    const res=await page.goto(base+'/',{waitUntil:'domcontentloaded',timeout:12000});
    if(!res||!res.ok()) throw new Error('HTTP '+(res&&res.status()));
    await page.waitForSelector('#works',{timeout:5000});
    const state=await page.evaluate(()=>({
      scrollWidth:document.documentElement.scrollWidth,
      clientWidth:document.documentElement.clientWidth,
      bodyWidth:document.body.getBoundingClientRect().width,
      h1Width:document.querySelector('h1')?.getBoundingClientRect().width||0,
      toolsWidth:document.querySelector('.tools')?.getBoundingClientRect().width||0,
      cardWidths:[...document.querySelectorAll('a.w')].slice(0,3).map(el=>el.getBoundingClientRect().width),
      title:getComputedStyle(document.querySelector('h1')).fontSize
    }));
    if(state.scrollWidth>state.clientWidth+1) throw new Error('horizontal overflow '+JSON.stringify(state));
    if(state.h1Width>state.clientWidth) throw new Error('heading overflow '+JSON.stringify(state));
    if(state.toolsWidth>state.clientWidth+1) throw new Error('tools overflow '+JSON.stringify(state));
    if(state.cardWidths.some(w=>w>state.clientWidth+1)) throw new Error('card overflow '+JSON.stringify(state));
    if(errors.length) throw new Error(errors.join(' | '));
    const guide=await page.goto(base+'/guide.html',{waitUntil:'domcontentloaded',timeout:12000});
    if(!guide||!guide.ok()) throw new Error('guide HTTP '+(guide&&guide.status()));
    const guideState=await page.evaluate(()=>({
      scrollWidth:document.documentElement.scrollWidth,
      clientWidth:document.documentElement.clientWidth,
      cards:document.querySelectorAll('.grid .card').length,
      combat:document.querySelectorAll('.combat .card').length,
      examples:[...document.querySelectorAll('a.example')].map(a=>a.getAttribute('href'))
    }));
    if(guideState.scrollWidth>guideState.clientWidth+1) throw new Error('guide horizontal overflow '+JSON.stringify(guideState));
    if(guideState.cards!==8) throw new Error('guide unit cards '+guideState.cards);
    if(guideState.combat!==2) throw new Error('guide combat cards '+guideState.combat);
    if(guideState.examples.length<6) throw new Error('guide example links missing');
    console.log('OK',width,state,guideState);
  }catch(e){
    failures.push({width,error:String(e),errors});
    console.error('FAIL',width,String(e));
  }finally{await page.close()}
}
await browser.close();
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
console.log('Hub mobile widths passed');
