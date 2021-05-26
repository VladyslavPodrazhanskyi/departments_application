# test/test_web_app/test_web_app_core.py

import http

from tests.test_base import BasicTestCase


class CoreTestCase(BasicTestCase):
    """ Test of core view function of the the web application.
    (home page and api description page)
    """

    def test_home(self):
        """ Test view function index of the web application. """
        resp = self.client.get('/')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Global Pharma Trade LLC', resp.get_data(as_text=True))

    def test_api(self):
        """ Test view function api of the web application. """
        resp = self.client.get('/api')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Api rest service', resp.get_data(as_text=True))
