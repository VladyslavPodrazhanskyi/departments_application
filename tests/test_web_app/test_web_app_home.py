import http

from tests.test_base import BasicTestCase


class HomeTestCase(BasicTestCase):
    def test_home(self):
        client = self.app.test_client()
        resp = client.get('/')
        assert resp.status_code == http.HTTPStatus.OK
