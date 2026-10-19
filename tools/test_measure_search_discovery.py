import io
import unittest
from email.message import Message
from urllib.error import HTTPError, URLError

from tools.measure_search_discovery import measure


class MeasureSearchDiscoveryTest(unittest.TestCase):
    def test_http_error_keeps_available_response_metadata(self):
        def opener(request, timeout):
            headers = Message()
            headers['Content-Type'] = 'text/plain; charset=utf-8'
            raise HTTPError(request.full_url, 404, 'Not Found', headers, io.BytesIO(b'missing'))

        result = measure('https://example.com/', opener=opener)

        self.assertFalse(result['allHttpOk'])
        for record in result['endpoints']:
            self.assertEqual(record['finalUrl'], record['requestedUrl'])
            self.assertEqual(record['status'], 404)
            self.assertEqual(record['contentType'], 'text/plain; charset=utf-8')
            self.assertEqual(record['bytes'], 7)
            self.assertIn('HTTP Error 404', record['error'])

    def test_transport_error_uses_null_response_fields_and_fails_health(self):
        def opener(request, timeout):
            raise URLError('offline')

        result = measure('https://example.com/', opener=opener)

        self.assertFalse(result['allHttpOk'])
        for record in result['endpoints']:
            self.assertIsNone(record['finalUrl'])
            self.assertIsNone(record['status'])
            self.assertIsNone(record['contentType'])
            self.assertIsNone(record['bytes'])
            self.assertIn('offline', record['error'])


if __name__ == '__main__':
    unittest.main()
