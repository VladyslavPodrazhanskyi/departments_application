import http
import json

from src import db
from tests.test_base import BasicTestCase
from src.services.department import DepartmentService
from src.models.models import Department


class SmokeTestCase(BasicTestCase):
    def test_smoke(self):
        client = self.app.test_client()
        resp = client.get('/api')
        assert resp.status_code == http.HTTPStatus.OK


class DepartmentTestCase(BasicTestCase):
    def test_dep_get_without_uuid(self):
        client = self.app.test_client()
        url = '/api/departments/'
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_dep_get_correct_uuid(self):
        url = f'/api/departments/{self.department_uuids[0]}'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

    def test_dep_get_incorrect_uuid(self):
        url = f'/api/departments/incorrect_uuid'
        client = self.app.test_client()
        resp = client.get(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_dep_post(self):
        client = self.app.test_client()
        data = {
            'name': 'Test department',
            'description': 'Test description'
        }
        resp = client.post('/api/departments', data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.CREATED)
        self.assertEqual(resp.json['name'], 'Test department')
        self.assertEqual(resp.json['description'], 'Test description')

    def test_dep_post_incorrect_data(self):
        client = self.app.test_client()
        data = {
            'age': 'Test department',
            'description': 'Test description'
        }
        resp = client.post('/api/departments', data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)

    def test_dep_put_correct_uuid(self):
        client = self.app.test_client()
        url = f'/api/departments/{self.department_uuids[0]}'
        data = {
            'name': 'Update department name',
            'description': 'Updated department description'
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertEqual(resp.json['name'], 'Update department name')
        self.assertEqual(resp.json['description'], 'Updated department description')

    def test_dep_put_incorrect_data(self):
        client = self.app.test_client()
        url = f'/api/departments/{self.department_uuids[0]}'
        data = {
            'incorrect field': 'Update department name',
            'description': 'Updated department description'
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)


    def test_dep_put_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/api/departments/incorrect_uuid'
        data = {
            'name': 'Update department name',
            'description': 'Updated department description'
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)

    def test_delete_dep_without_employees(self):
        client = self.app.test_client()
        url = f'/api/departments/{self.department_uuids[0]}'
        print(url)
        resp = client.delete(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NO_CONTENT)

    def test_delete_dep_with_employees(self):
        client = self.app.test_client()
        url = f'/api/departments/{self.department_uuids[1]}'
        print(url)
        resp = client.delete(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.FORBIDDEN)

    def test_delete_dep_incorrect_uuid(self):
        client = self.app.test_client()
        url = f'/api/departments/incorrect_uuid'
        resp = client.delete(url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)


