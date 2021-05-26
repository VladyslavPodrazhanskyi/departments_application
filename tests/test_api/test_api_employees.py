# tests/test_api/test_api_employees.py

import http
import json

from src import db
from tests.test_base import BasicTestCase
from src.services.department import DepartmentService
from src.models.models import Department


class EmployeeApiTestCase(BasicTestCase):
    """Test case for testing get, post, put, delete methods
    of the Employees resource of the Rest API.
    """

    def test_api_employee_get(self):
        """ Test of the method get. """
        # test get without uui
        url_without_uuid = '/api/employees/'
        resp = self.client.get(url_without_uuid)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn("employees", resp.json)

        # test get with correct uuid
        url_with_correct_uuid = f'/api/employees/{self.employee_uuids[0]}'
        resp = self.client.get(url_with_correct_uuid)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertEqual("Irina Kulikova", resp.json.get("employee_name"))

        # test get with incorrect uuid
        url_incorrect_uuid = f'/api/employees/incorrect_uuid'
        client = self.app.test_client()
        resp = client.get(url_incorrect_uuid)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)

    def test_api_employee_post(self):
        """ Test of the method post. """
        # test post with correct data
        url = '/api/employees'
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.CREATED, resp.status_code)
        self.assertEqual('Test employee', resp.json.get('employee_name'))
        self.assertEqual('2000-01-01', resp.json.get('birth_date'))
        self.assertEqual(12000, resp.json.get('salary'))

        # test post with incorrect department
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': 'incorrect department'
        }
        resp = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.BAD_REQUEST, resp.status_code)
        self.assertEqual("department does not exist", resp.json.get("message"))

        # test post with incorrect data
        incorrect_data = {
            'incorrect field': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = self.client.post(url, data=json.dumps(incorrect_data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.BAD_REQUEST, resp.status_code)

    def test_api_employee_put(self):
        """ Test of the method put. """
        # test put with incorrect data
        url = f'/api/employees/{self.employee_uuids[0]}'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': self.department_uuids[1]
        }
        resp = self.client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertEqual('Updated employee', resp.json.get('employee_name'))
        self.assertEqual('2010-02-02', resp.json.get('birth_date'))
        self.assertEqual(15000, resp.json.get('salary'))

        # test put with incorrect uuid
        incorrect_url = f'/api/employees/incorrect_uuid'
        resp = self.client.put(incorrect_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)

        # test put with incorrect data
        incorrect_data = {
            'incorrect field': 'Update',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = self.client.put(url, data=json.dumps(incorrect_data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.BAD_REQUEST, resp.status_code)

        # test put with incorrect department
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': 'incorrect department'
        }
        resp = self.client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.BAD_REQUEST, resp.status_code)
        self.assertEqual("department does not exist", resp.json.get('message'))

    def test_delete_employee(self):
        """ Test of the method delete. """
        # test delete employee with correct uuid
        url = f'/api/employees/{self.employee_uuids[0]}'
        resp = self.client.delete(url)
        self.assertEqual(http.HTTPStatus.NO_CONTENT, resp.status_code)

        # test delete employee with incorrect uuid
        url = f'/api/employees/incorrect_uuid'
        resp = self.client.delete(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)
