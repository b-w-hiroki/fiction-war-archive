"""生成サイトの canonical、説明、robots、sitemap の公開契約を検査する。"""
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
SITE = json.loads((ROOT / 'site.json').read_text())
BASE = SITE['pages_url'].rstrip('/')


def check_meta(path, canonical):
    text = path.read_text()
    assert re.search(r'<meta name="description" content="[^"]+">', text), f'{path}: description missing'
    assert f'<link rel="canonical" href="{canonical}">' in text, f'{path}: canonical mismatch'
    assert re.search(r'<meta property="og:title" content="[^"]+">', text), f'{path}: og:title missing'
    assert f'<meta property="og:url" content="{canonical}">' in text, f'{path}: og:url mismatch'


check_meta(DOCS / 'index.html', BASE + '/')
check_meta(DOCS / 'guide.html', BASE + '/guide.html')
for work in SITE['works']:
    check_meta(DOCS / work / 'index.html', f'{BASE}/{work}/')
    for battle in sorted((DOCS / work).glob('*.html')):
        if battle.name != 'index.html':
            check_meta(battle, f'{BASE}/{work}/{battle.name}')

robots = (DOCS / 'robots.txt').read_text()
assert f'Sitemap: {BASE}/sitemap.xml' in robots

tree = ET.parse(DOCS / 'sitemap.xml')
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = {node.text for node in tree.findall('.//s:loc', ns)}
expected = set()
for path in DOCS.rglob('*.html'):
    rel = path.relative_to(DOCS).as_posix()
    if rel == 'index.html':
        rel = ''
    elif rel.endswith('/index.html'):
        rel = rel[:-len('index.html')]
    expected.add(BASE + '/' + rel)
assert urls == expected, f'sitemap mismatch: missing={sorted(expected - urls)} extra={sorted(urls - expected)}'
assert all('?' not in url and '#' not in url for url in urls)

print(f'search metadata contract passed ({len(urls)} URLs)')
