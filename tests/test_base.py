import unittest
from src import create_app, db
from src.services.department import DepartmentService
from src.services.employee import EmployeeService
from data.insert_db import populate_departments, populate_employees


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        populate_departments()
        populate_employees()
        self.department_uuids = DepartmentService.get_all_uuids()
        self.employee_uuids = EmployeeService.get_all_uuids()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


