import http

# from wsgi import app
from src import create_app

app = create_app('testing')
client = app.test_client()


def test_home():
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK


def test_smoke():
    resp = client.get('/api')
    assert resp.status_code == http.HTTPStatus.OK
