# import http
#
# from src import create_app
#
# app = create_app('testing')
#
#
# def test_home():
#     client = app.test_client()
#     resp = client.get('/')
#     assert resp.status_code == http.HTTPStatus.OK
#
#
# def test_smoke():
#     client = app.test_client()
#     resp = client.get('/api')
#     assert resp.status_code == http.HTTPStatus.OK
