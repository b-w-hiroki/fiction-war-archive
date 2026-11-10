import { chromium } from 'playwright';
import fs from 'node:fs';
import assert from 'node:assert/strict';

const base = process.env.QA_BASE || 'http://127.0.0.1:8000';
const label = process.env.QA_LABEL || 'after';
fs.mkdirSync('qa-astarte', {recursive: true});
const three = fs.readFileSync('node_modules/three/build/three.min.js');
const browser = await chromium.launch({args: ['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist']});
try {
  for (const width of [390, 320]) {
    const page = await browser.newPage({viewport: {width, height: 844}, reducedMotion: 'reduce'});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.route('https://cdnjs.cloudflare.com/ajax/libs/three.js/**', route => route.fulfill({contentType: 'application/javascript', body: three}));
    await page.route('https://fonts.googleapis.com/**', route => route.fulfill({contentType: 'text/css', body: ''}));
    await page.goto(base + '/ginei/astarte.html');
    await page.waitForSelector('#stage canvas');
    assert.equal(await page.locator('.quick-tour-card').count(), 3);
    for (const phase of [0, 2, 6]) {
      const card = page.locator('[data-tour-phase="' + phase + '"]');
      await card.scrollIntoViewIfNeeded();
      const box = await card.boundingBox();
      assert.ok(box.x >= 0 && box.x + box.width <= width + 1, 'card outside viewport');
      assert.ok(await card.evaluate(el => el.scrollWidth <= el.clientWidth), 'card text overflow');
      await card.focus();
      assert.ok(await card.evaluate(el => el === document.activeElement));
      await page.screenshot({path: 'qa-astarte/' + label + '-' + width + '-card-' + phase + '.png'});
      await page.keyboard.press(phase === 2 ? 'Space' : 'Enter');
      assert.equal(await page.locator('#brief').isVisible(), false);
      assert.equal(await page.locator('#steps button.on').evaluate(el => Array.from(el.parentNode.children).indexOf(el)), phase);
      assert.ok(await page.locator('#briefOpen').evaluate(el => el === document.activeElement));
      await page.keyboard.press('Enter');
      assert.ok(await page.locator('#brief').isVisible());
    }
    const first = page.locator('.quick-tour-card').first();
    await first.focus();
    await page.keyboard.press('Tab');
    assert.ok(await page.locator('.quick-tour-card').nth(1).evaluate(el => el === document.activeElement));
    await page.keyboard.press('Shift+Tab');
    assert.ok(await first.evaluate(el => el === document.activeElement));
    await page.locator('#briefClose').click();
    await page.locator('#briefOpen').click();
    await page.locator('#briefStart').click();
    assert.equal(await page.locator('#brief').isVisible(), false);
    assert.deepEqual(errors, []);
    console.log('PASS', label, width, '3 phase jumps; Enter/Space; Tab/Shift+Tab; close/reopen');
    await page.close();
  }
} finally { await browser.close(); }
