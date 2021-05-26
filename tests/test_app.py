# tests/test_app.py

from flask import current_app
from tests.test_base import BasicTestCase


class AppTestCase(BasicTestCase):
    """Test case for checking that instance of test Flask
    application is created and configured correctly.
    """

    def test_app_exists(self):
        """ Test checks that an instance of Flask application is created. """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """ Test check that instance of Flask application
        configured correctly for testing
        """
        self.assertTrue(current_app.config['TESTING'])
