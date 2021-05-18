import http

from tests.test_base import BasicTestCase


class EmployeesTestCase(BasicTestCase):
    def test_display_employees(self):
        client = self.app.test_client()
        url = '/employees'
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_display_employee_correct_uuid(self):
        url = f'/employees/{self.employee_uuids[0]}'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_display_employee_incorrect_uuid(self):
        url = f'/employees/incorrect_uuid'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_search_employee(self):
        client = self.app.test_client()
        url = '/employees'
        data = {'start_date': '1980-11-02', 'end_date': '1990-11-02'}
        resp = client.post(url, data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)

    def test_search_results(self):
        client = self.app.test_client()
        url = '/employees/search_results/1980-11-02'
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        url = '/employees/search_results/1980-11-02/1990-11-02'
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        url = '/employees/search_results/1990-11-02/1980-11-02'
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_create_employee(self):
        client = self.app.test_client()
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = client.post('/create_employee', data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)
        # separate for 2 methods (get and post ????)
        resp = client.get('/create_department')
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_create_employee_incorrect_department(self):
        client = self.app.test_client()
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': 'incorrect department'
        }
        resp = client.post('/create_employee', data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)


    def test_update_employee_correct_uuid(self):
        client = self.app.test_client()
        url = f'/employees/{self.employee_uuids[0]}/update'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': self.department_uuids[1]
        }
        resp = client.post(url, data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_update_employee_incorrect_department(self):
        client = self.app.test_client()
        url = f'/employees/{self.employee_uuids[0]}/update'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': 'incorrect department'
        }
        resp = client.post(url, data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_update_employee_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/employees/incorrect_uuid/update'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': self.department_uuids[1]
        }
        resp = client.post(url, data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_delete_employee(self):
        client = self.app.test_client()
        url = f'/employees/{self.employee_uuids[0]}/delete'
        resp = client.post(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)

    def test_delete_employee_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/employees/incorrect_uuid/delete'
        resp = client.post(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)
