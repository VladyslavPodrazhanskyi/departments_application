import http
import json

from src import db
from tests.test_base import BasicTestCase
from src.services.department import DepartmentService
from src.models.models import Department


class EmployeeTestCase(BasicTestCase):
    def test_employee_get_without_uuid(self):
        client = self.app.test_client()
        url = '/api/employees/'
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_employee_get_correct_uuid(self):
        url = f'/api/employees/{self.employee_uuids[0]}'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_employee_get_incorrect_uuid(self):
        url = f'/api/employees/incorrect_uuid'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_employee_post(self):
        client = self.app.test_client()
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = client.post('/api/employees', data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.CREATED)
        self.assertEqual(resp.json['employee_name'], 'Test employee')
        self.assertEqual(resp.json['birth_date'], '2000-01-01')
        self.assertEqual(resp.json['salary'], 12000)

    def test_employee_post_incorrect_department(self):
        client = self.app.test_client()
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': 'incorrect department'
        }
        resp = client.post('/api/employees', data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)

    def test_employee_post_incorrect_data(self):
        client = self.app.test_client()
        data = {
            'incorrect field': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = client.post('/api/employees', data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)

    def test_employee_put_correct_uuid(self):
        client = self.app.test_client()
        url = f'/api/employees/{self.employee_uuids[0]}'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': self.department_uuids[1]
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertEqual(resp.json['employee_name'], 'Updated employee')
        self.assertEqual(resp.json['birth_date'], '2010-02-02')
        self.assertEqual(resp.json['salary'], 15000)

    def test_employee_put_incorrect_data(self):
        client = self.app.test_client()
        url = f'/api/employees/{self.employee_uuids[0]}'
        data = {
            'incorrect field': 'Update',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)

    def test_employee_put_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/api/employees/incorrect_uuid'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': self.department_uuids[1]
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_employee_put_incorrect_department(self):
        client = self.app.test_client()
        url = f'/api/employees/{self.employee_uuids[0]}'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': 'incorrect department'
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)

    def test_delete_employee(self):
        client = self.app.test_client()
        url = f'/api/employees/{self.employee_uuids[0]}'
        resp = client.delete(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NO_CONTENT)

    def test_delete_employee_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/api/employees/incorrect_uuid'
        resp = client.delete(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)
