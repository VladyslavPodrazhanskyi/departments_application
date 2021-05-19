import http
import json

from tests.test_base import BasicTestCase


class DepartmentTestCase(BasicTestCase):
    def test_api_department_get(self):
        # test get with correct without uuid
        url_without_uuid = '/api/departments/'
        resp = self.client.get(url_without_uuid)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertIn('departments', resp.json)

        # test get with correct uuid
        url_with_correct_uuid = f'/api/departments/{self.department_uuids[0]}'
        resp = self.client.get(url_with_correct_uuid)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertEqual('Business development', resp.json.get('name'))

        # test get with incorrect uuid
        url_incorrect_uuid = f'/api/departments/incorrect_uuid'
        resp = self.client.get(url_incorrect_uuid)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)

    def test_api_department_post(self):
        # test post with correct data
        url = '/api/departments/'
        correct_data = {
            'name': 'Test department',
            'description': 'Test description'
        }
        resp = self.client.post(url, data=json.dumps(correct_data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.CREATED,  resp.status_code)
        self.assertEqual(resp.json['name'], 'Test department')
        self.assertEqual(resp.json['description'], 'Test description')
        # test post with incorrect data
        incorrect_data = {
            'incorrect_field': 'Test department',
            'description': 'Test description'
        }
        resp = self.client.post('/api/departments', data=json.dumps(incorrect_data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.BAD_REQUEST, resp.status_code)

    def test_api_department_put(self):
        # test put with correct uuid and data
        url_correct_uuid = f'/api/departments/{self.department_uuids[0]}'
        correct_data = {
            'name': 'Update department name',
            'description': 'Updated department description'
        }
        resp = self.client.put(url_correct_uuid, data=json.dumps(correct_data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.OK, resp.status_code)
        self.assertEqual('Update department name', resp.json['name'])
        self.assertEqual('Updated department description', resp.json['description'])

        # test put with correct uuid and incorrect_data
        url_correct_uuid = f'/api/departments/{self.department_uuids[1]}'
        incorrect_data = {
            'incorrect field': 'Update department name',
            'description': 'Updated department description'
        }
        resp = self.client.put(url_correct_uuid, data=json.dumps(incorrect_data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.BAD_REQUEST, resp.status_code)

        # test put with incorrect uuid and correct_data
        url_incorrect_uuid = f'/api/departments/incorrect_uuid'
        resp = self.client.put(url_incorrect_uuid, data=json.dumps(correct_data), content_type='application/json')
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)

    def test_api_department_delete(self):
        # test delete department without employees
        url_without_employees = f'/api/departments/{self.department_uuids[0]}'
        resp = self.client.delete(url_without_employees)
        self.assertEqual(http.HTTPStatus.NO_CONTENT, resp.status_code)

        # test delete department with employees
        url_with_employees = f'/api/departments/{self.department_uuids[1]}'
        resp = self.client.delete(url_with_employees)
        self.assertEqual(http.HTTPStatus.FORBIDDEN, resp.status_code)
        self.assertEqual("department with employees can't be deleted!", resp.json.get('message'))

        # test delete department with employees
        url = f'/api/departments/incorrect_uuid'
        resp = self.client.delete(url)
        self.assertEqual(http.HTTPStatus.NOT_FOUND, resp.status_code)
