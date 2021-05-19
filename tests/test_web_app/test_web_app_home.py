import http

from tests.test_base import BasicTestCase


class HomeTestCase(BasicTestCase):
    def test_home(self):
        client = self.app.test_client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertIn('Global Pharma Trade LLC', resp.get_data(as_text=True))


