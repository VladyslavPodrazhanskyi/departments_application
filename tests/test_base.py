# tests/test_base.py

import unittest
from src import create_app, db
from src.services.department import DepartmentService
from src.services.employee import EmployeeService
from data.insert_db import populate_departments, populate_employees


class BasicTestCase(unittest.TestCase):
    """Base Test case for testing the Rest API
    and the Web application.

    All the other test cases
    are inherited from current Class.

    BasicTestCast has 2 methods:

    1) setUp -  is called before start of every test.
    2) tearDown - is called after finish of every test.
    """

    def setUp(self):
        """
        Method creates and initiate an instance of flask application with test config,
        an instance of test_client, app_context, creates all models for test db,
        populates db with fixtures and gets list of uuids both for for departments and employess
        for every test.
        :return: None
        """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        populate_departments()
        populate_employees()
        self.department_uuids = DepartmentService.get_all_uuids()
        self.employee_uuids = EmployeeService.get_all_uuids()

    def tearDown(self):
        """
         Method removes session, deletes all the data and tables
        from test database, closes app_context.
        :return: None
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
