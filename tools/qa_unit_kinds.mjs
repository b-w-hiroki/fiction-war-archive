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
fs.mkdirSync('test-results/field-visual',{recursive:true});
for(const c of cases){
  const disk='docs'+c.url;
  const html=fs.readFileSync(disk,'utf8');
  // Land scenes must use the dimmed field palette and current sky-lighting pipeline.
  if(/skyColor=new THREE.Color\(|waterColor=new THREE.Color\(/.test(html)){
    for(const token of ['skyColor=new THREE.Color(', 'multiplyScalar(.34)', 'multiplyScalar(.25)', 'multiplyScalar(.29)', 'DirectionalLight(0xfff2dc,.72)', 'HemisphereLight(0xcfe0f0,0x4a4a3a,.48)']){
      if(!html.includes(token)) failures.push({url:c.url,error:'terrain lighting regression: missing '+token});
    }
    if(html.includes('scene.background=new THREE.Color(0x34404d)')) failures.push({url:c.url,error:'stale terrain sky background'});
  }
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
    if(await page.locator('#brief').isVisible()) await page.locator('#briefStart').click();
    await page.waitForTimeout(500);
    await page.screenshot({path:'test-results/field-visual/'+c.url.split('/').filter(Boolean).join('-')+'-390.png'});
    const state=await page.evaluate(()=>({
      legend:[...document.querySelectorAll('#kindLegend .k')].map(x=>x.textContent.trim()),
      canvas:!!document.querySelector('#stage canvas'),
      overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth+1,
      legendFont:parseFloat(getComputedStyle(document.querySelector('#kindLegend .k')).fontSize),
      iconSize:document.querySelector('#kindLegend .i').getBoundingClientRect().width,
      legendWidth:document.querySelector('#kindLegend').getBoundingClientRect().width,
      rangeMode:document.querySelector('#rangeMode')?.textContent||'',
      rangeFont:parseFloat(getComputedStyle(document.querySelector('#rangeMode')).fontSize),
      captionFont:parseFloat(getComputedStyle(document.querySelector('#cap p')).fontSize),
      phaseFont:parseFloat(getComputedStyle(document.querySelector('#cTitle')).fontSize),
      seekFont:parseFloat(getComputedStyle(document.querySelector('#seekNow')).fontSize),
      seekHeight:document.querySelector('#phaseSeek').getBoundingClientRect().height,
      panelBg:getComputedStyle(document.querySelector('.force')).backgroundColor,
      labelInk:getComputedStyle(document.querySelector('#cTitle')).color,
      fontFamily:getComputedStyle(document.body).fontFamily,
      panelWidth:document.querySelector('.force').getBoundingClientRect().width,
      labelCollisionLogic:document.documentElement.innerHTML.includes('visibleLabs.sort'),
      strongFactionColor:document.documentElement.innerHTML.includes("const opOf=s=>s.s==='gone'||s.s==='hidden'?0:1"),
      stateLabels:document.documentElement.innerHTML.includes("charge:'▶ 突撃'")&&document.documentElement.innerHTML.includes("broken:'× 崩壊'"),
      momentum:document.querySelector('#momentumText')?.textContent||'',
      momentumPos:parseFloat(document.querySelector('#momentumMark')?.style.left||'0')
    }));
    for(const label of c.legend) if(!state.legend.includes(label)) throw new Error('legend missing '+label+' '+JSON.stringify(state.legend));
    if(!state.canvas) throw new Error('canvas missing');
    if(state.overflow) throw new Error('horizontal overflow');
    if(state.legendFont<11) throw new Error('legend font too small '+state.legendFont);
    if(state.iconSize<14) throw new Error('legend icon too small '+state.iconSize);
    if(state.legendWidth>390) throw new Error('legend too wide '+state.legendWidth);
    if(!['待機','近距離戦','遠距離戦','近・遠 混戦'].includes(state.rangeMode)) throw new Error('range HUD invalid '+state.rangeMode);
    if(state.rangeFont<11) throw new Error('range HUD font too small '+state.rangeFont);
    if(state.captionFont<14) throw new Error('caption font too small '+state.captionFont);
    if(state.phaseFont<19) throw new Error('phase title too small '+state.phaseFont);
    if(state.seekFont<12) throw new Error('seek label too small '+state.seekFont);
    if(state.seekHeight<28) throw new Error('seek touch target too small '+state.seekHeight);
    if(!state.panelBg.includes('0.94')&&!state.panelBg.includes('0.97')) throw new Error('HUD panel too transparent '+state.panelBg);
    if(!state.fontFamily.includes('Noto Sans JP')) throw new Error('readability font missing '+state.fontFamily);
    if(state.panelWidth>375) throw new Error('HUD panel consumes too much width '+state.panelWidth);
    if(!state.labelCollisionLogic) throw new Error('label collision control missing');
    if(!state.strongFactionColor) throw new Error('unit states can fade faction colors');
    if(!state.stateLabels) throw new Error('explicit unit state labels missing');
    if(!state.momentum) throw new Error('battle momentum missing');
    if(state.momentumPos<8||state.momentumPos>92) throw new Error('battle momentum marker invalid '+state.momentumPos);
    // Expanded phase copy must not be trapped by the compact caption height.
    await page.locator('#capMore').click();
    const captionExpanded=await page.locator('#cap').evaluate(el=>({expanded:el.classList.contains('expanded'),maxHeight:parseFloat(getComputedStyle(el).maxHeight),scrollHeight:el.scrollHeight}));
    if(!captionExpanded.expanded||captionExpanded.maxHeight<=130) throw new Error('expanded caption still clipped '+JSON.stringify(captionExpanded));
    await page.locator('#capMore').click();
    // Unit panel, focus mode and camera follow must remain operable.
    await page.locator('#unitSelect').click();
    if(!await page.locator('#unitInfo').isVisible()) throw new Error('unit detail did not open');
    if(!await page.locator('#unitInfoText').textContent()) throw new Error('unit detail empty');
    // Expanded captions and unit details must not obscure the seek/play controls.
    await page.locator('#capMore').click();
    const expandedLayout=await page.evaluate(()=>{
      const box=id=>document.getElementById(id).getBoundingClientRect();
      const hit=(a,b)=>a.left<b.right&&b.left<a.right&&a.top<b.bottom&&b.top<a.bottom;
      const visible=id=>getComputedStyle(document.getElementById(id)).display!=='none';
      const cap=box('cap'),unit=box('unitInfo'),seek=box('phaseSeek'),play=box('play');
      return {capSeek:hit(cap,seek),unitSeek:hit(unit,seek),unitPlay:hit(unit,play),capPlay:hit(cap,play),unitCap:visible('unitInfo')&&hit(unit,cap)};
    });
    if(Object.values(expandedLayout).some(Boolean)) throw new Error('expanded HUD overlap '+JSON.stringify(expandedLayout));
    await page.locator('#capMore').click();
    await page.locator('#unitSelect').click();
    await page.locator('#unitInfoClose').click();
    if(await page.locator('#unitInfo').isVisible()) throw new Error('unit detail did not close');
    await page.locator('#focusToggle').click();
    if(!await page.locator('#hud').evaluate(el=>el.classList.contains('focus'))) throw new Error('focus mode not enabled');
    await page.locator('#focusToggle').click();
    if(await page.locator('#hud').evaluate(el=>el.classList.contains('focus'))) throw new Error('focus mode not disabled');
    const layout=await page.evaluate(()=>{
      const rect=id=>document.getElementById(id).getBoundingClientRect();
      const overlap=(a,b)=>a.left<b.right&&b.left<a.right&&a.top<b.bottom&&b.top<a.bottom;
      return {titleBrief:overlap(rect('briefOpen'),rect('cTitle')),toggleTitle:overlap(rect('focusToggle'),rect('cTitle')),toggleBrief:overlap(rect('focusToggle'),rect('briefOpen')),togglePlay:overlap(rect('focusToggle'),rect('play'))};
    });
    if(Object.values(layout).some(Boolean)) throw new Error('mobile HUD overlap '+JSON.stringify(layout));
    const seek=page.locator('#phaseSeek');
    await seek.fill('500');await seek.dispatchEvent('input');await page.waitForTimeout(250);
    const rangeAfterSeek=await page.locator('#rangeMode').textContent();
    const momentumAfterSeek=await page.locator('#momentumText').textContent();
    if(!rangeAfterSeek) throw new Error('range HUD empty after seek');
    if(!momentumAfterSeek) throw new Error('momentum HUD empty after seek');
    await seek.dispatchEvent('change');await page.locator('#play').click();await page.waitForTimeout(900);await page.locator('#play').click();
    // 320px compact viewport regression: no horizontal overflow or offscreen controls.
    await page.setViewportSize({width:320,height:720});
    await page.waitForTimeout(200);
    const compact=await page.evaluate(()=>({
      overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth+1,
      play:document.querySelector('#play').getBoundingClientRect(),
      seek:document.querySelector('#phaseSeek').getBoundingClientRect()
    }));
    await page.screenshot({path:'test-results/field-visual/'+c.url.split('/').filter(Boolean).join('-')+'-320.png'});
    if(compact.overflow) throw new Error('320px horizontal overflow');
    for(const key of ['play','seek']){
      const b=compact[key];
      if(b.width<20||b.left<0||b.right>321) throw new Error('320px control out of bounds '+key+' '+JSON.stringify(b));
    }
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
