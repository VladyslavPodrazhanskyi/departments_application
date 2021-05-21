import http

from tests.test_base import BasicTestCase


class HomeTestCase(BasicTestCase):
    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Global Pharma Trade LLC', resp.get_data(as_text=True))


