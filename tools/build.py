"""作品ごとの会戦ページとポータルを生成する。

使い方:
  python3 tools/build.py ginei              # docs/ginei/ に公開用（相対リンク）を出力
  python3 tools/build.py ginei --artifact   # build/artifact/ginei/ に claude.ai アーティファクト用（絶対URL）を出力
"""
import sys, json, re, os, subprocess, importlib.util, glob, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / 'engine'
sys.path.insert(0, str(ENGINE))

PALS = {'noble': ('0x9b6fe0', '#b28cf0', '#7a4fc0'), 'coup': ('0xe0603f', '#ef7a5c', '#c0452a'),
        'iser': ('0x4cc38a', '#5fd39a', '#1f8a58'), 'rebel': ('0xd8505c', '#ec6e78', '#b83a46'),
        'ally': ('0x3fbccf', '#58c7d8', '#1b8ea2'),
        'zeon': ('0xd25a3e', '#ec7c5f', '#b4452b'), 'efsf': ('0x4a86d8', '#79abee', '#2d68be')}
COL = {'': None, 'noble': 'nob', 'coup': 'coup', 'iser': 'iser', 'rebel': 'reb', 'ally': 'all', 'zeon': 'zeon', 'efsf': 'efsf'}


SITE = json.loads((ROOT / 'site.json').read_text()) if (ROOT / 'site.json').exists() else {}
GA_RE = re.compile(r'\n?<!-- ga -->.*?<!-- /ga -->', re.S)


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


def build_battle(path, work_dir, refs, out_dir, ga=False):
    spec = importlib.util.spec_from_file_location('battle', path)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    key = Path(c.OUT).stem
    s = (ENGINE / 'template.html').read_text()
    for k in ['TITLE', 'HEAD', 'ERA', 'NOTE']:
        s = s.replace('@@%s@@' % k, getattr(c, k))
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


def build_portal(work_dir, metas, impact, link, strategy_url, out_file, standalone=False):
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
    html = (work_dir / 'portal_template.html').read_text()
    html = html.replace('/*@@DATA@@*/', 'const B=' + json.dumps(rows, ensure_ascii=False) + ';').replace('@@STRATEGY@@', strategy_url)
    if standalone:  # GitHub Pages 用。アーティファクトは公開時に枠が付くので不要
        html = ('<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + html.replace('<style>', '<style>\nbody{margin:0;padding-top:env(safe-area-inset-top,0px)}', 1)
                .replace('<div class="wrap">', '</head>\n<body>\n<div class="wrap">', 1) + '\n</body>\n</html>\n')
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(with_ga(html) if standalone else html)


def main():
    work = sys.argv[1]
    artifact = '--artifact' in sys.argv
    work_dir = ROOT / 'works' / work
    sys.path.insert(0, str(work_dir))
    from refs import R
    from impact import I
    out_dir = ROOT / ('build/artifact' if artifact else 'docs') / work
    metas = [build_battle(p, work_dir, R, out_dir, ga=not artifact) for p in sorted(glob.glob(str(work_dir / 'battles' / '*.py')))]
    if artifact:
        urls = json.loads((work_dir / 'artifacts.json').read_text())
        build_portal(work_dir, metas, I, lambda k: urls.get(k, '#'), urls.get('_strategy', ''), out_dir / 'index.html')
    else:
        build_portal(work_dir, metas, I, lambda k: f'{k}.html', 'strategy.html', out_dir / 'index.html', standalone=True)
        for extra in [ROOT / 'docs' / 'index.html', *out_dir.glob('strategy.html')]:  # 手書きのページにも反映
            extra.write_text(with_ga(extra.read_text()))
    print(f'{work}: {len(metas)}会戦とポータルを {out_dir.relative_to(ROOT)}/ に出力')


if __name__ == '__main__':
    main()
