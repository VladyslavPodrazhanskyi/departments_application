import http

from tests.test_base import BasicTestCase


class SmokeTestCase(BasicTestCase):
    def test_smoke(self):
        client = self.app.test_client()
        resp = client.get('/api')
        assert resp.status_code == http.HTTPStatus.OK
