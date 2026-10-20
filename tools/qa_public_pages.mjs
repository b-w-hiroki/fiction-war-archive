import {chromium} from 'playwright';
import assert from 'node:assert/strict';
import {mkdirSync} from 'node:fs';
const browser=await chromium.launch({headless:true});
const endpoint='https://asia-southeast1-otsukai-app-4b62b.cloudfunctions.net/submitContactForm';
mkdirSync('qa-public',{recursive:true});
try {
 for(const width of [320,390,430]) {
  const page=await browser.newPage({viewport:{width,height:844}});
  let calls=[];let mode='success';
  await page.route(endpoint,async route=>{
   calls.push(route.request().postDataJSON());
   await new Promise(resolve=>setTimeout(resolve,100));
   await route.fulfill({status:mode==='success'?200:500,contentType:'application/json',body:JSON.stringify(mode==='success'?{result:{ok:true}}:{error:{status:'INTERNAL'}})});
  });
  for(const path of ['about.html','privacy.html','contact.html']) {
   const response=await page.goto('http://127.0.0.1:8000/'+path);
   assert(response.ok());
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
   assert.equal(await page.locator('footer a').count(),4);
   await page.screenshot({path:`qa-public/${path}-${width}.png`,fullPage:true});
  }
  await page.locator('button[type=submit]').click();
  assert.equal(calls.length,0,'empty form cannot send');
  await page.locator('#name').fill('QA fixture');
  await page.locator('#email').fill('fixture@example.invalid');
  await page.locator('#category').selectOption({label:'著作権・権利関係'});
  await page.locator('#subject').fill('送信契約');
  await page.locator('#message').fill('これはmock専用の検証データです。');
  await page.locator('button[type=submit]').click();
  assert.equal(calls.length,0,'consent is required');
  await page.locator('#agree').check();
  await page.locator('button[type=submit]').click();
  await page.evaluate(()=>document.getElementById('contact-form').dispatchEvent(new Event('submit',{bubbles:true,cancelable:true})));
  await page.waitForFunction(()=>document.getElementById('contact-status').textContent.includes('受け付けました'));
  assert.equal(calls.length,1,'in-flight duplicate blocked');
  assert(calls[0].data.subject.startsWith('[戦史アーカイブ]'));
  assert(calls[0].data.message.includes('お問い合わせ種別：著作権・権利関係'));
  assert.equal(await page.locator('#email').inputValue(),'');
  mode='error';
  await page.locator('#name').fill('QA fixture');
  await page.locator('#email').fill('fixture@example.invalid');
  await page.locator('#category').selectOption({label:'重大な不具合'});
  await page.locator('#subject').fill('再試行');
  await page.locator('#message').fill('保持される本文');
  await page.locator('#agree').check();
  await page.locator('button[type=submit]').click();
  await page.waitForFunction(()=>document.getElementById('contact-status').textContent.includes('確認できませんでした'));
  assert.equal(await page.locator('#message').inputValue(),'保持される本文');
  assert.equal(await page.locator('button[type=submit]').isEnabled(),true);
  await page.screenshot({path:`qa-public/contact-error-${width}.png`,fullPage:true});
  await page.close();
 }
 console.log('Public pages: 3 widths, required fields, consent, service identity, duplicate prevention, success, failure/input retention passed. All sends mocked.');
} finally {await browser.close();}
