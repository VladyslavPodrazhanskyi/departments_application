import http

# from wsgi import app
from src import create_app

app = app = create_app('testing')
client = app.test_client()


def test_hello():
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK


def test_about():
    resp = client.get('/about')
    assert resp.status_code == http.HTTPStatus.OK
