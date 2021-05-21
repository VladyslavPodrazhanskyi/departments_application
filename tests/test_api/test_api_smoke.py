import http

from tests.test_base import BasicTestCase


class SmokeTestCase(BasicTestCase):
    def test_smoke(self):
        resp = self.client.get('/api')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertEqual('OK', resp.json['message'])


