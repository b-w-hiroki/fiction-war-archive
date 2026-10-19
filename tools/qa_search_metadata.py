"""生成サイトの canonical、説明、robots、sitemap の公開契約を検査する。"""
import json
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
SITE = json.loads((ROOT / 'site.json').read_text())
BASE = SITE['pages_url'].rstrip('/')
SHARE_IMAGE = f'{BASE}/og-fiction-war-archive.png'
MEASUREMENT_SCRIPT = ROOT / 'tools' / 'measure_search_discovery.py'
compile(MEASUREMENT_SCRIPT.read_text(), str(MEASUREMENT_SCRIPT), 'exec')


def check_meta(path, canonical):
    text = path.read_text()
    assert re.search(r'<meta name="description" content="[^"]+">', text), f'{path}: description missing'
    assert f'<link rel="canonical" href="{canonical}">' in text, f'{path}: canonical mismatch'
    assert re.search(r'<meta property="og:title" content="[^"]+">', text), f'{path}: og:title missing'
    assert f'<meta property="og:url" content="{canonical}">' in text, f'{path}: og:url mismatch'
    assert f'<meta property="og:image" content="{SHARE_IMAGE}">' in text, f'{path}: og:image mismatch'
    assert '<meta property="og:image:width" content="1200">' in text, f'{path}: og:image width missing'
    assert '<meta property="og:image:height" content="630">' in text, f'{path}: og:image height missing'


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

share_path = DOCS / 'og-fiction-war-archive.png'
share = share_path.read_bytes()
assert share[:8] == b'\x89PNG\r\n\x1a\n', 'share image must be PNG'
width, height = struct.unpack('>II', share[16:24])
assert (width, height) == (1200, 630), f'share image dimensions: {width}x{height}'


def local_path(url):
    parsed = urlparse(url)
    relative = unquote(parsed.path).lstrip('/')
    if not relative or relative.endswith('/'):
        relative += 'index.html'
    return DOCS / relative


for canonical in sorted(urls):
    page = local_path(canonical)
    text = page.read_text()
    for raw in re.findall(r'\b(?:href|src)=["\']([^"\']+)["\']', text, re.I):
        if '${' in raw or raw.startswith(('#', 'data:', 'mailto:', 'tel:', 'javascript:')):
            continue
        target = urlparse(urljoin(canonical, raw))
        if target.netloc != urlparse(BASE).netloc or target.path.startswith('/__/'):
            continue
        assert local_path(target.geturl()).exists(), f'{page}: broken local reference {raw}'

print(f'search metadata contract passed ({len(urls)} URLs)')
