"""公開前後で同じHTTP観測結果をJSON出力する。"""
import json
import re
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

if len(sys.argv) != 2:
    raise SystemExit('usage: python tools/measure_search_discovery.py https://example.com/')

base = sys.argv[1].rstrip('/') + '/'
result = {
    'measuredAt': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
    'baseUrl': base,
    'endpoints': [],
}


def pick(text, pattern):
    match = re.search(pattern, text, re.I)
    return match.group(1) if match else None


for endpoint in ('/', '/robots.txt', '/sitemap.xml'):
    requested = urljoin(base, endpoint.lstrip('/'))
    record = {'endpoint': endpoint, 'requestedUrl': requested}
    try:
        request = Request(requested, headers={'User-Agent': 'birdman-search-discovery-check/1.0'})
        with urlopen(request, timeout=20) as response:
            body = response.read()
            text = body.decode(response.headers.get_content_charset() or 'utf-8', errors='replace')
            record.update({
                'finalUrl': response.geturl(),
                'status': response.status,
                'contentType': response.headers.get('Content-Type'),
                'bytes': len(body),
            })
            if endpoint == '/':
                record.update({
                    'title': pick(text, r'<title>([^<]*)</title>'),
                    'description': pick(text, r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)'),
                    'canonical': pick(text, r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']*)'),
                    'ogImage': pick(text, r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']*)'),
                })
            if endpoint == '/sitemap.xml':
                record['locCount'] = len(re.findall(r'<loc>[^<]+</loc>', text))
    except HTTPError as error:
        record.update({'status': error.code, 'error': str(error)})
    except (URLError, TimeoutError, OSError) as error:
        record['error'] = str(error)
    result['endpoints'].append(record)

result['allHttpOk'] = all(200 <= entry.get('status', 0) < 300 for entry in result['endpoints'])
print(json.dumps(result, ensure_ascii=False, indent=2))
