import http

from tests.test_base import BasicTestCase


class DepartmentTestCase(BasicTestCase):
    def test_display_departments(self):
        client = self.app.test_client()
        url = '/departments'
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_display_department_correct_uuid(self):
        url = f'/departments/{self.department_uuids[0]}'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_display_department_incorrect_uuid(self):
        url = f'/departments/incorrect_uuid'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_create_department(self):
        client = self.app.test_client()
        data = {
            'name': 'Test department',
            'description': 'Test description'
        }
        resp = client.post('/create_department', data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)
        # separate for 2 methods (get and post ????)
        resp = client.get('/create_department', data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_update_department_correct_uuid(self):
        client = self.app.test_client()
        url = f'/departments/{self.department_uuids[0]}/update'
        data = {
            'name': 'Update department name',
            'description': 'Updated department description'
        }
        resp = client.post(url, data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_update_department_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/departments/incorrect_uuid/update'
        data = {
            'name': 'Update department name',
            'description': 'Updated department description'
        }
        resp = client.post(url, data=data)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_delete_dep_without_employees(self):
        client = self.app.test_client()
        url = f'/departments/{self.department_uuids[0]}/del'
        resp = client.post(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)

    def test_delete_dep_with_employees(self):
        client = self.app.test_client()
        url = f'/departments/{self.department_uuids[1]}/del'
        resp = client.post(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.FOUND)

    def test_delete_dep_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/departments/incorrect_uuid/del'
        resp = client.post(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)
