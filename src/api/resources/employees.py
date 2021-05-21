import datetime
from flask import request
from flask_restful import Resource
from src import db
from src.api.schemas.employees import EmployeeSchema
from src.services.employee import EmployeeService
from src.services.department import DepartmentService
from marshmallow import ValidationError


class EmployeeListApi(Resource):
    employee_schema = EmployeeSchema()

    def get(self, uuid=None):
        if uuid is None:
            employees = EmployeeService.get_all()
            return {'employees': self.employee_schema.dump(employees, many=True)}, 200
        employee = EmployeeService.get_by_uuid(uuid)
        if not employee:
            return {'message': 'object if not found'}, 404
        return self.employee_schema.dump(employee), 200

    def post(self):
        try:
            employee = self.employee_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        if not DepartmentService.get_by_uuid(employee.department_uuid):
            return {'message': "department does not exist"}, 400
        EmployeeService.save_to_db(employee)
        return self.employee_schema.dump(employee), 201

    def put(self, uuid):
        employee = EmployeeService.get_by_uuid(uuid)
        if not employee:
            return {'message': 'object if not found'}, 404
        try:
            employee = self.employee_schema.load(request.json, instance=employee, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        if not DepartmentService.get_by_uuid(employee.department_uuid):
            return {'message': "department does not exist"}, 400
        EmployeeService.save_to_db(employee)
        return self.employee_schema.dump(employee), 200

    def delete(self, uuid):
        employee = EmployeeService.get_by_uuid(uuid)
        if not employee:
            return {'message': f'employee with name {uuid} does not exist'}, 404
        EmployeeService.delete_from_db(employee)
        return {}, 204
