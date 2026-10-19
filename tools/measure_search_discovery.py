"""公開前後で揃うHTTP計測結果をJSON出力する。"""
import json
import re
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


def pick(text, pattern):
    match = re.search(pattern, text, re.I)
    return match.group(1) if match else None


def measure_endpoint(base, endpoint, opener=urlopen):
    requested = urljoin(base, endpoint.lstrip('/'))
    record = {
        'endpoint': endpoint,
        'requestedUrl': requested,
        'finalUrl': None,
        'status': None,
        'contentType': None,
        'bytes': None,
        'error': None,
    }
    try:
        request = Request(requested, headers={'User-Agent': 'birdman-search-discovery-check/1.0'})
        with opener(request, timeout=20) as response:
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
        body = error.read()
        record.update({
            'finalUrl': error.geturl(),
            'status': error.code,
            'contentType': error.headers.get('Content-Type') if error.headers else None,
            'bytes': len(body),
            'error': str(error),
        })
    except (URLError, TimeoutError, OSError) as error:
        record['error'] = str(error)
    return record


def measure(base, opener=urlopen):
    base = base.rstrip('/') + '/'
    result = {
        'measuredAt': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'baseUrl': base,
        'endpoints': [
            measure_endpoint(base, endpoint, opener)
            for endpoint in ('/', '/robots.txt', '/sitemap.xml')
        ],
    }
    result['allHttpOk'] = all(
        entry['status'] is not None and 200 <= entry['status'] < 300
        for entry in result['endpoints']
    )
    return result


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        raise SystemExit('usage: python tools/measure_search_discovery.py https://example.com/')
    print(json.dumps(measure(argv[0]), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
