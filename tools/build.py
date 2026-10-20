"""作品ごとの会戦ページとポータルを生成する。

使い方:
  python3 tools/build.py all                # 全作品と作品一覧（トップ）を docs/ に出力（GitHub Pages 用・相対リンク）
  python3 tools/build.py all --artifact     # 同じものを build/artifact/ に出力（claude.ai 用・絶対URL）
年表は全作品を1ページに収め、見出しのメニューでページ内を切り替える。
"""
import sys, json, re, os, subprocess, importlib.util, glob, tempfile
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / 'engine'
sys.path.insert(0, str(ENGINE))

PALS = {'noble': ('0x9b6fe0', '#b28cf0', '#7a4fc0'), 'coup': ('0xe0603f', '#ef7a5c', '#c0452a'),
        'iser': ('0x4cc38a', '#5fd39a', '#1f8a58'), 'rebel': ('0xd8505c', '#ec6e78', '#b83a46'),
        'ally': ('0x3fbccf', '#58c7d8', '#1b8ea2'),
        'zeon': ('0xd25a3e', '#ec7c5f', '#b4452b'), 'efsf': ('0x4a86d8', '#79abee', '#2d68be'),
        'parse': ('0x3aa6b8', '#5cc4d6', '#1f7a8c'), 'lusi': ('0xd2505a', '#e8707a', '#b0303a'), 'sind': ('0xe08a3a', '#eda15a', '#b8641a'),
        'turan': ('0x9a6fe0', '#ad8ae6', '#6d47ad'), 'misr': ('0xd0aa30', '#d9b84a', '#9a7a12'), 'hilmes': ('0xc06a9a', '#d081ad', '#8a3b6e'), 'serpent': ('0x8a7a9a', '#a596b8', '#5a4a6a'),
        'titan': ('0xc87a3a', '#e0a070', '#9a5420'), 'scout': ('0x3e9a5a', '#6cc488', '#22703c'), 'marley': ('0xb04a4a', '#d87a7a', '#8a2a2a'), 'allied': ('0x3c8f88', '#69aaa4', '#2f746f'),
        'gamilas': ('0x4a9ad8', '#7ab8ee', '#2d74be'), 'earth': ('0xd8803a', '#eda15a', '#b8641a')}
COL = {'': None, 'noble': 'nob', 'coup': 'coup', 'iser': 'iser', 'rebel': 'reb', 'ally': 'all', 'zeon': 'zeon', 'efsf': 'efsf', 'parse': 'parse', 'lusi': 'lusi', 'sind': 'sind', 'turan': 'turan', 'misr': 'misr', 'hilmes': 'hilmes', 'serpent': 'serpent', 'titan': 'titan', 'scout': 'scout', 'marley': 'marley', 'allied': 'allied', 'gamilas': 'gamilas', 'earth': 'earth'}


SITE = json.loads((ROOT / 'site.json').read_text()) if (ROOT / 'site.json').exists() else {}
GA_RE = re.compile(r'\n?<!-- ga -->.*?<!-- /ga -->', re.S)
SEARCH_META_RE = re.compile(r'\n?<!-- search metadata -->.*?<!-- /search metadata -->', re.S)


def page_url(path=''):
    return SITE.get('pages_url', '').rstrip('/') + ('/' + path.lstrip('/') if path else '/')


def plain_text(value):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', value)).strip()


def with_search_meta(html, description, canonical):
    """手書きの公開補助ページに、再生成可能な検索メタ情報を付ける。"""
    html = SEARCH_META_RE.sub('', html)
    title_match = re.search(r'<title>(.*?)</title>', html, re.S)
    if not title_match:
        raise ValueError(f'title missing for {canonical}')
    title = plain_text(title_match.group(1))
    meta = (
        '\n<!-- search metadata -->\n'
        f'<meta name="description" content="{escape(description, quote=True)}">\n'
        f'<link rel="canonical" href="{canonical}">\n'
        '<meta property="og:type" content="website">\n'
        f'<meta property="og:title" content="{escape(title, quote=True)}">\n'
        f'<meta property="og:description" content="{escape(description, quote=True)}">\n'
        f'<meta property="og:url" content="{canonical}">\n'
        f'<meta property="og:image" content="{page_url("og-fiction-war-archive.png")}">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta property="og:image:alt" content="フィクション戦史アーカイブの作品・会戦一覧">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{escape(title, quote=True)}">\n'
        f'<meta name="twitter:description" content="{escape(description, quote=True)}">\n'
        f'<meta name="twitter:image" content="{page_url("og-fiction-war-archive.png")}">\n'
        '<meta name="twitter:image:alt" content="フィクション戦史アーカイブの作品・会戦一覧">\n'
        '<!-- /search metadata -->'
    )
    return html.replace('</title>', '</title>' + meta, 1)


def with_ga(html):
    """GitHub Pages 版にだけ Google Analytics を入れる。site.json の ga_id が空なら何もしない"""
    html = GA_RE.sub('', html)
    gid = SITE.get('ga_id', '').strip()
    if not gid or '</head>' not in html:
        return html
    tag = (f'<!-- ga --><script async src="https://www.googletagmanager.com/gtag/js?id={gid}"></script>'
           f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{gid}');</script><!-- /ga -->")
    return html.replace('</head>', tag + '\n</head>', 1)


def node(code):
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
        f.write(code)
    r = subprocess.run(['node', f.name], capture_output=True, text=True)
    os.unlink(f.name)
    return r


def build_battle(path, work_dir, refs, out_dir, ga=False, back=''):
    spec = importlib.util.spec_from_file_location('battle', path)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    key = Path(c.OUT).stem
    s = (ENGINE / 'template.html').read_text()
    for k in ['TITLE', 'HEAD', 'ERA', 'NOTE']:
        s = s.replace('@@%s@@' % k, getattr(c, k))
    title = c.TITLE.replace(' 3D俯瞰', '')
    description = f'{title}（{c.ERA}）を作中情報に基づいて3D俯瞰で再構成し、経過、戦果、原作・アニメの該当箇所を確認できます。'
    canonical = page_url(f'{work_dir.name}/{key}.html')
    s = (s.replace('@@DESCRIPTION@@', escape(description, quote=True))
         .replace('@@CANONICAL@@', canonical)
         .replace('@@OG_IMAGE@@', page_url('og-fiction-war-archive.png')))
    s = s.replace('@@SE@@', getattr(c, 'SE', '帝国軍')).replace('@@SA@@', getattr(c, 'SA', '同盟軍'))
    pal, pale = getattr(c, 'PAL', None), getattr(c, 'PALE', None)
    if pal:  # 側Aの配色を先に替える（Eの置換と衝突しないように）
        a3, a, al = PALS[pal]
        s = s.replace('0x3fbccf', a3).replace('#58c7d8', a).replace('0x58c7d8', '0x' + a[1:]).replace('--all:#1b8ea2', '--all:' + al)
    if pale:
        e3, e, el = PALS[pale]
        s = s.replace('0xe0a43a', e3).replace('#e8b44c', e).replace('0xe8b44c', '0x' + e[1:]).replace('--emp:#b8841a', '--emp:' + el).replace('--acc:#b8841a', '--acc:' + el)
    data = c.DATA + '\nRESULT.refs=' + json.dumps([{'k': a, 'v': b} for a, b in refs.get(key, [])], ensure_ascii=False) + ';\n'
    s = s.replace('/*@@ENV@@*/', c.ENV).replace('/*@@DATA@@*/', data)
    s = s.replace('<!--@@BACK@@-->', f'<a class="back" href="{back}">‹ 年表へ戻る</a>' if back else '')
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f'{key}.html').write_text(with_ga(s) if ga else s)
    js = re.findall(r'<script>(.*?)</script>', s, re.S)[0]
    chk = subprocess.run(['node', '--check', '-'], input=js, capture_output=True, text=True)
    if chk.returncode:
        sys.exit(f'{key}: 構文エラー\n{chk.stderr}')
    r = node(data + ';console.log(JSON.stringify({res:RESULT,phases:PH.length}))')
    if r.returncode:
        sys.exit(f'{key}: データ読み込みエラー\n{r.stderr}')
    m = json.loads(r.stdout)
    m.update({'key': key, 'title': c.TITLE.replace(' 3D俯瞰', ''), 'era': c.ERA, 'uc': getattr(c, 'UC', 0),
              'arc': getattr(c, 'ARC', ''), 'pal': pal or '', 'pale': pale or ''})
    return m


def load_work(work):
    return json.loads((ROOT / 'works' / work / 'work.json').read_text())


def make_rows(metas, impact, link):
    rows = []
    for m in metas:
        k, r = m['key'], m['res']
        se = COL[m['pale']] or 'emp'
        sa = COL[m['pal']] or 'all'
        sides = [{'n': s['name'], 'c': se if s['side'] == 'E' else sa, 'b': s.get('before', ''), 'l': s.get('loss', ''),
                  'r': s.get('rate'), 'd': s.get('dead', []), 'cm': s.get('cmdr', '')} for s in r['sides']]
        win = next((z for z, x in zip(sides, r['sides']) if x['side'] == r['winner']), None)
        rows.append({'k': k, 'u': link(k), 't': m['title'], 'era': m['era'], 'uc': m['uc'], 'arc': m['arc'],
                     'oc': r['outcome'], 'sum': r['summary'], 'when': r.get('when', ''), 's': sides,
                     'win': win['n'] if win else '', 'wc': win['c'] if win else 'none', 'ph': m['phases'],
                     'refs': r.get('refs', []), 'im': impact[k][0], 'imt': impact[k][1]})
    rows.sort(key=lambda x: x['uc'])
    return rows


def build_portal(default, works, hub, out_file, artifact):
    """全作品の年表を1ページに収め、見出しのメニューでページ内を切り替える。default は最初に表示する作品"""
    colors = {}
    for w in works.values():
        colors.update(w.pop('colors', {}) or {})
    for w in works.values():
        w.pop('colors', None)
    hub_target = ' target="_blank" rel="noopener"' if artifact else ''
    js = ('const WORKS=' + json.dumps(works, ensure_ascii=False) + ';\n'
          + f'const DEF={json.dumps(default)},HUB={json.dumps(hub)},HUBT={json.dumps(hub_target)},'
          + f'SITE={json.dumps(SITE.get("name", ""), ensure_ascii=False)};')
    html = (ENGINE / 'portal.html').read_text()
    html = (html.replace('/*@@DATA@@*/', js)
            .replace('/*@@VARS_L@@*/', ''.join(f'--{k}:{v[0]};' for k, v in colors.items()))
            .replace('/*@@VARS_D@@*/', ''.join(f'--{k}:{v[1]};' for k, v in colors.items()))
            .replace('@@TITLE@@', works[default]['title']))
    if not artifact:  # GitHub Pages 用。アーティファクトは公開時に枠が付くので不要
        description = plain_text(works[default]['lead'])
        canonical = page_url(f'{default}/')
        metadata = (f'<meta name="description" content="{escape(description, quote=True)}">\n'
                    f'<link rel="canonical" href="{canonical}">\n'
                    '<meta property="og:type" content="website">\n'
                    '<meta property="og:locale" content="ja_JP">\n'
                    f'<meta property="og:site_name" content="{escape(SITE.get("name", ""), quote=True)}">\n'
                    f'<meta property="og:title" content="{escape(works[default]["title"], quote=True)}">\n'
                    f'<meta property="og:description" content="{escape(description, quote=True)}">\n'
                    f'<meta property="og:url" content="{canonical}">\n'
                    f'<meta property="og:image" content="{page_url("og-fiction-war-archive.png")}">\n'
                    '<meta property="og:image:width" content="1200">\n'
                    '<meta property="og:image:height" content="630">\n'
                    '<meta property="og:image:alt" content="フィクション戦史アーカイブの作品・会戦一覧">\n'
                    '<meta name="twitter:card" content="summary_large_image">\n'
                    f'<meta name="twitter:image" content="{page_url("og-fiction-war-archive.png")}">\n'
                    '<meta name="twitter:image:alt" content="フィクション戦史アーカイブの作品・会戦一覧">\n')
        html = ('<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + metadata
                + html.replace('<style>', '<style>\nbody{margin:0;padding-top:env(safe-area-inset-top,0px)}', 1)
                .replace('<div class="wrap">', '</head>\n<body>\n<div class="wrap">', 1) + '\n</body>\n</html>\n')
    out_file.parent.mkdir(parents=True, exist_ok=True)
    html = html.replace('<!--@@PUBLIC_LINKS@@-->', '' if artifact else public_links('../'))
    out_file.write_text(html if artifact else with_ga(html))


def build_hub(counts, link_portal, out_file, artifact):
    t = ' target="_blank" rel="noopener"' if artifact else ''
    items = []
    for w in SITE['works']:
        cfg = load_work(w)
        ab = cfg.get('about', {})
        info = (f'<p class="by">{ab["creator"]}　／　{ab["form"]}</p><p class="sm"><budoux-ja>{ab["summary"]}</budoux-ja></p>' if ab else '')
        items.append(f'<li><a class="w" href="{link_portal(w)}"{t}><b>{cfg["short"]}</b>'
                     f'<span>{cfg["span"]}　{counts[w]}の{cfg["unit"]}</span><em>年表を開く</em>{info}</a></li>')
    items += [f'<li class="soon">{x}　準備中</li>' for x in SITE.get('soon', [])]
    description = plain_text(SITE['lead'])
    html = ((ENGINE / 'hub.html').read_text().replace('@@NAME@@', SITE['name']).replace('@@LEAD@@', SITE['lead'])
            .replace('@@DESCRIPTION@@', escape(description, quote=True)).replace('@@URL@@', page_url())
            .replace('@@OG_IMAGE@@', page_url('og-fiction-war-archive.png'))
            .replace('@@ITEMS@@', '\n  '.join(items)))
    if artifact:  # claude.ai では doctype〜head を公開時に補うので本文だけ
        html = re.sub(r'^<!doctype html>\n<html lang="ja">\n<head>\n(<meta [^>]*>\n)*', '', html)
        html = html.replace('</head>\n<body>\n', '').replace('\n</body>\n</html>', '')
    out_file.parent.mkdir(parents=True, exist_ok=True)
    html = html.replace('<!--@@PUBLIC_LINKS@@-->', '' if artifact else public_links())
    out_file.write_text(html if artifact else with_ga(html))


def build_work(work, artifact):
    """会戦ページを出力し、年表用の作品データを返す"""
    work_dir = ROOT / 'works' / work
    cfg = load_work(work)
    for m in ('refs', 'impact'):
        sys.modules.pop(m, None)
    sys.path.insert(0, str(work_dir))
    from refs import R
    from impact import I
    sys.path.pop(0)
    out_dir = ROOT / ('build/artifact' if artifact else 'docs') / work
    battles = sorted(glob.glob(str(work_dir / 'battles' / '*.py')))
    if artifact:
        urls = json.loads((work_dir / 'artifacts.json').read_text())
        metas = [build_battle(p, work_dir, R, out_dir) for p in battles]
        pages = SITE.get('pages_url', '').rstrip('/')  # claude.ai に未公開の会戦は GitHub Pages 版へリンク
        link, strategy = (lambda k: urls.get(k) or (f'{pages}/{work}/{k}.html' if pages else '#')), urls.get('_strategy', '')
    else:
        metas = [build_battle(p, work_dir, R, out_dir, ga=True, back=f'index.html#{work}') for p in battles]
        link, strategy = (lambda k: f'../{work}/{k}.html'), f'../{work}/strategy.html'
        for extra in out_dir.glob('strategy.html'):  # 手書きのページにも反映
            description = f'{plain_text(cfg["title"])}の主要勢力と戦略上の変遷を時系列で確認できる補助資料です。'
            canonical = page_url(f'{work}/{extra.name}')
            extra.write_text(with_ga(with_search_meta(extra.read_text(), description, canonical)))
    data = {k: cfg[k] for k in ('title', 'short', 'span', 'unit', 'date', 'yl', 'eras', 'names', 'order', 'colors')}
    data['lead'] = cfg['lead'].replace('@@STRATEGY@@', strategy)
    data['notes'] = cfg['notes'].replace('@@STRATEGY@@', strategy)
    data['B'] = make_rows(metas, I, link)
    print(f'{work}: {len(metas)}件の会戦ページを {out_dir.relative_to(ROOT)}/ に出力')
    return data


def public_links(prefix=''):
    return ('<nav class="public-links" aria-label="運営情報">'
            + ''.join(f'<a href="{prefix}{path}.html">{label}</a>' for path, label in
                      [('about', 'このサイトについて'), ('privacy', 'プライバシー'), ('contact', 'お問い合わせ')])
            + '</nav>')


def build_public_pages(base):
    config = SITE['public_release']
    template = (ENGINE / 'public-page.html').read_text()
    for slug, title in [('about', 'このサイトについて・免責事項'), ('privacy', 'プライバシーポリシー'), ('contact', 'お問い合わせ')]:
        content = (ENGINE / f'{slug}-content.html').read_text()
        content = content.replace('@@CONTACT_EMAIL@@', escape(config['contact_email'], quote=True))
        if slug == 'contact':
            content = content.replace('<form id="contact-form">', '<form id="contact-form" data-endpoint="' + escape(config['contact_endpoint'], quote=True) + '">')
        html = template.replace('@@TITLE@@', title).replace('@@CONTENT@@', content)
        html = html.replace('@@SCRIPT@@', '<script src="contact.js" defer></script>' if slug == 'contact' else '')
        description = f'フィクション戦史アーカイブの{title}。AI収集・非公式コンテンツの運営方針とお問い合わせの案内。'
        (base / f'{slug}.html').write_text(with_search_meta(html, description, page_url(f'{slug}.html')))
    (base / 'contact.js').write_text((ENGINE / 'contact.js').read_text())


def main():
    artifact = '--artifact' in sys.argv
    works = {w: build_work(w, artifact) for w in SITE['works']}
    base = ROOT / ('build/artifact' if artifact else 'docs')
    if artifact:
        hub = json.loads((ROOT / 'artifacts.json').read_text()).get('_hub', '#')
        portal = lambda w: json.loads((ROOT / 'works' / w / 'artifacts.json').read_text()).get('_portal', '#')
    else:
        hub, portal = '../index.html', (lambda w: f'{w}/index.html#{w}')
    for w in works:  # 作品ごとの入口。中身は同じで、最初に開く作品だけが違う
        build_portal(w, json.loads(json.dumps(works)), hub, base / w / 'index.html', artifact)
    build_hub({w: len(d['B']) for w, d in works.items()}, portal, base / 'index.html', artifact)
    favicon = ROOT / 'favicon.svg'
    if favicon.exists() and not artifact:
        (base / 'favicon.svg').write_bytes(favicon.read_bytes())
    guide = (ENGINE / 'guide.html').read_text()
    guide = guide.replace('</body>', '<footer style="max-width:1000px;margin:24px auto;padding:20px">' + public_links() + '</footer></body>').replace('</style>', '.public-links{display:flex;flex-wrap:wrap;gap:8px 18px}.public-links a{display:inline-flex;align-items:center;min-height:44px}</style>') if not artifact else guide
    (base / 'guide.html').write_text(guide if artifact else with_ga(guide))
    if not artifact:
        build_public_pages(base)
    if not artifact and SITE.get('domain'):  # GitHub Pages の独自ドメイン
        (base / 'CNAME').write_text(SITE['domain'] + '\n')
        (base / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + page_url('sitemap.xml') + '\n')
        urls = []
        for html_file in sorted(base.rglob('*.html')):
            rel = html_file.relative_to(base).as_posix()
            if rel == 'index.html':
                rel = ''
            elif rel.endswith('/index.html'):
                rel = rel[:-len('index.html')]
            urls.append(page_url(rel))
        sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                   + ''.join(f'  <url><loc>{escape(url)}</loc></url>\n' for url in urls)
                   + '</urlset>\n')
        (base / 'sitemap.xml').write_text(sitemap)
    print(f'年表（{len(works)}作品を切り替え）と作品一覧を {base.relative_to(ROOT)}/ に出力')


if __name__ == '__main__':
    main()
