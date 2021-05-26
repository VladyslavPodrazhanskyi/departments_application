# test/test_web_app/test_web_app_departments.py

import http

from tests.test_base import BasicTestCase


class DepartmentWebTestCase(BasicTestCase):
    """
    Test case for testing all the functions and pages of the web application
    connected with Department model, includes following test methods:

     -  test_display_departments;
     -  test_create_department;
     -  test_update_department;
     -  test_del_department.
    """

    def test_display_departments(self):
        """ Test of the view function display_departments
          of the the web application.
        """
        # test display departments without uuid
        url = '/departments'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Company Departments:', resp.get_data(as_text=True))

        # test display departments with correct uuid
        url = f'/departments/{self.department_uuids[1]}'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Sales department', resp.get_data(as_text=True))
        self.assertIn('Average salary: 21500.0 USD', resp.get_data(as_text=True))

        # test display departments with incorrect uuid
        url = f'/departments/incorrect_uuid'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)
        self.assertIn('404 PAGE NOT FOUND!', resp.get_data(as_text=True))

    def test_create_department(self):
        """ Test of the view function create_department
          of the the web application.
        """
        # test get method
        url = '/create_department'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Add department page', resp.get_data(as_text=True))

        # test method post
        data = {
            'name': 'Test department',
            'description': 'Test description'
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)

    def test_update_department(self):
        """ Test of the view function update_department
          of the the web application.
        """
        # test get method correct uuid
        url = f'/departments/{self.department_uuids[0]}/update'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Update department page', resp.get_data(as_text=True))

        # test get method incorrect uuid
        incorrect_url = '/departments/incorrect_uuid/update'
        resp = self.client.post(incorrect_url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)
        self.assertIn('404 PAGE NOT FOUND!', resp.get_data(as_text=True))

        # test post method
        data = {
            'name': 'Update department name',
            'description': 'Updated department description'
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)
        # test that the employee was updated
        url = f'/departments/{self.department_uuids[0]}'
        resp = self.client.get(url, data=data)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertIn('Update department name', resp.get_data(as_text=True))

    def test_del_department(self):
        """ Test of the view function del_department
          of the the web application.
        """
        # test delete department without employees
        url = f'/departments/{self.department_uuids[0]}/del'
        resp = self.client.post(url)
        self.assertEqual(http.HTTPStatus.FOUND, resp.status_code)
        # test that department without employees was deleted and is not available
        url = f'/departments/{self.department_uuids[0]}'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)

        # test delete department with employees
        url = f'/departments/{self.department_uuids[1]}/del'
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)
        # test that department with employees was not deleted and is available
        url = f'/departments/{self.department_uuids[1]}'
        resp = self.client.get(url)
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)

        # test delete department with incorrect uuid
        url = f'/departments/incorrect_uuid/del'
        resp = self.client.post(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)
