import http

from tests.test_base import BasicTestCase


class SmokeTestCase(BasicTestCase):
    """Test case for testing get methods
    of the Smoke resource of the Rest API.
    """
    def test_smoke(self):
        resp = self.client.get('/api')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertEqual('OK', resp.json['message'])


