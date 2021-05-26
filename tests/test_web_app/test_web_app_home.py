# test/test_web_app/test_web_app_home.py

import http

from tests.test_base import BasicTestCase


class HomeTestCase(BasicTestCase):
    """ Test of view function index of the the web application.
    (home page)
    """

    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Global Pharma Trade LLC', resp.get_data(as_text=True))
