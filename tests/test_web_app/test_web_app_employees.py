import http

from tests.test_base import BasicTestCase


class EmployeesTestCase(BasicTestCase):
    def test_display_employees(self):
        # test display employees without uuid
        url = '/employees'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Company Employees:', resp.get_data(as_text=True))
        self.assertIn('Search employee by birth date:', resp.get_data(as_text=True))

        # test display employees with correct uuid
        url = f'/employees/{self.employee_uuids[0]}'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Irina Kulikova', resp.get_data(as_text=True))

        # test display employees with incorrect uuid
        url = f'/employees/incorrect_uuid'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)
        self.assertIn('404 PAGE NOT FOUND!', resp.get_data(as_text=True))

    def test_create_employee(self):
        # test get method
        url = '/create_employee'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Add employee page', resp.get_data(as_text=True))

        # test method post correct uuid department
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': self.department_uuids[0]
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)

        # test method post incorrect uuid department
        data = {
            'employee_name': 'Test employee',
            'birth_date': '2000-01-01',
            'salary': 12000,
            'department_uuid': 'incorrect department'
        }
        resp = self.client.post('/create_employee', data=data)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('input the correct uuid of the department', resp.get_data(as_text=True))

    def test_update_employee(self):
        # test get method correct uuid
        url = f'/employees/{self.employee_uuids[0]}/update'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Update employee page', resp.get_data(as_text=True))

        # test get method incorrect uuid
        incorrect_url = '/employees/incorrect_uuid/update'
        resp = self.client.post(incorrect_url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)
        self.assertIn('404 PAGE NOT FOUND!', resp.get_data(as_text=True))

        # test post method correct department
        url = f'/employees/{self.employee_uuids[0]}/update'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': self.department_uuids[1]
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)
        # test that the employee was updated
        url = f'/employees/{self.employee_uuids[0]}'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Updated employee', resp.get_data(as_text=True))

        # test post method incorrect department
        url = f'/employees/{self.employee_uuids[1]}/update'
        data = {
            'employee_name': 'Updated employee',
            'birth_date': '2010-02-02',
            'salary': 15000,
            'department_uuid': 'incorrect department'
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('message: input the correct uuid of the department', resp.get_data(as_text=True))

    def test_delete_employee(self):
        # test delete existing employees
        url = f'/employees/{self.employee_uuids[0]}/delete'
        resp = self.client.post(url)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)
        # test that employee was deleted and is not available any more
        url = f'/employees/{self.department_uuids[0]}'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)

        # test delete employee with incorrect uuid
        client = self.app.test_client()
        url = f'/employees/incorrect_uuid/delete'
        resp = client.post(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)

    def test_search_employee(self):
        # search by start_date only
        url_search = '/employees'
        data = {'start_date': '1986-07-02'}
        resp = self.client.post(url_search, data=data)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)
        # search result by start_date only
        url_result = '/employees/search_results/1986-07-02'
        resp = self.client.get(url_result)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertIn('Irina Kulikova', resp.get_data(as_text=True))
        self.assertIn('birth date: 1986-07-02', resp.get_data(as_text=True))

        # search by start_date and end_date
        start_date, end_date = '1986-07-01', '1986-07-03'
        # end date > start date
        data = dict(start_date=start_date, end_date=end_date)
        resp = self.client.post(url_search, data=data)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)
        # end date < start date
        start_date, end_date = end_date, start_date
        data = dict(start_date=start_date, end_date=end_date)
        resp = self.client.post(url_search, data=data)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)
        # search result by start_date and end_date
        url_result = f'/employees/search_results/{start_date}/{end_date}'
        resp = self.client.get(url_result)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Irina Kulikova', resp.get_data(as_text=True))
        self.assertIn('birth date: 1986-07-02', resp.get_data(as_text=True))
