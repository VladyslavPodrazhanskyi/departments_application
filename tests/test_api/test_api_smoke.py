import http

from tests.test_base import BasicTestCase


class SmokeTestCase(BasicTestCase):
    def test_smoke(self):
        resp = self.client.get('/api')
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertEqual(resp.json['message'], 'OK')


