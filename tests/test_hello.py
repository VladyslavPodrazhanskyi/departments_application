import http

from src import app


def test_hello():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK


def test_about():
    client = app.test_client()
    resp = client.get('/about')
    assert resp.status_code == http.HTTPStatus.OK