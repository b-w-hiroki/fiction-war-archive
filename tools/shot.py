"""3D再現ページをスマホ幅で撮影して確認する。
使い方: python3 tools/shot.py <htmlのパス> <場面番号,カンマ区切り> [res] [待ち時間ms]
three.js は CDN の代わりに THREE_JS（既定 /tmp/node_modules/three/build/three.min.js）を読む。
事前に: cd /tmp && npm i three@0.128.0
"""
import asyncio,sys,os
from playwright.async_api import async_playwright
f=sys.argv[1];idx=[int(x) for x in sys.argv[2].split(',')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.route('**/three.min.js',lambda r:r.fulfill(path=os.environ.get('THREE_JS','/tmp/node_modules/three/build/three.min.js')))
        await pg.route('**/fonts.googleapis.com/**',lambda r:r.abort())
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file://'+os.path.abspath(f));await pg.wait_for_timeout(3500)
        shots=[]
        for i in idx:
            await pg.evaluate(f"document.querySelectorAll('#steps button')[{i}].click()")
            await pg.wait_for_timeout(int(sys.argv[4]) if len(sys.argv)>4 else 5500);n=f'/tmp/sh{i}.png';await pg.screenshot(path=n);shots.append(n)
        if len(sys.argv)>3:
            await pg.evaluate("document.getElementById('resOpen').click()");await pg.wait_for_timeout(800);await pg.screenshot(path='/tmp/shres.png');shots.append('/tmp/shres.png') # RES
        print('errors:',errs)
        from PIL import Image
        ims=[Image.open(x) for x in shots];o=Image.new('RGB',(390*len(ims),844))
        for k,im in enumerate(ims):o.paste(im,(390*k,0))
        o.save('/tmp/cmp.png')
        await b.close()
asyncio.run(main())
