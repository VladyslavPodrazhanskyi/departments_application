import unittest
from flask import current_app
from src import create_app, db

from src.models.models import Department, Employee


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])  # ??? testing

    def test_dep_is_added(self):
        department = Department('test_dep', 'test_descr')
        db.session.add(department)
        db.session.commit()
        self.assertEqual(db.session.query(Department).filter_by(name='test_dep').first().description, 'test_descr')


if __name__ == '__main__':
    unittest.main(verbosity=2)
