# src/api/resources/departments.py

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from src import db

from src.api.schemas.departments import DepartmentSchema

from src.services.department import DepartmentService


class DepartmentListApi(Resource):
    """ Department REST resource. """

    department_schema = DepartmentSchema()

    def get(self, uuid=None):
        """ Methog get """
        if uuid is None:
            departments = DepartmentService.get_all()
            return {'departments': self.department_schema.dump(departments, many=True)}, 200
        department = DepartmentService.get_by_uuid(uuid)
        if not department:
            return {'message': 'object is not found '}, 404
        return self.department_schema.dump(department), 200

    def post(self):
        """ Methog post """
        try:
            department = self.department_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        DepartmentService.save_to_db(department)
        return self.department_schema.dump(department), 201

    def put(self, uuid):
        """ Methog put """
        department = DepartmentService.get_by_uuid(uuid)
        if not department:
            return {'message': 'object is not found'}, 404
        try:
            department = self.department_schema.load(request.json, instance=department, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        DepartmentService.save_to_db(department)
        return self.department_schema.dump(department), 200

    def delete(self, uuid):
        """ Methog delete """
        department = DepartmentService.get_by_uuid(uuid)
        if not department:
            return {'message': 'object is not found'}, 404
        if list(department.department_employees):
            return {"message": "department with employees can't be deleted!"}, 403
        DepartmentService.delete_from_db(department)
        return {}, 204
