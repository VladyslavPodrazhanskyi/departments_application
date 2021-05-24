# src/api/resources/employees.py

from flask_restful import Resource


class Smoke(Resource):
    """ Test REST resource. It is used for checking work of rest api. """

    def get(self):
        return {"message": "OK"}
