from src.api import api

from src.api.resources.smoke import Smoke
from src.api.resources.departments import DepartmentListApi
from src.api.resources.employees import EmployeeListApi

api.add_resource(Smoke, '/api', strict_slashes=False)
api.add_resource(DepartmentListApi, '/api/departments', '/api/departments/<uuid>', strict_slashes=False)
api.add_resource(EmployeeListApi, '/api/employees', '/api/employees/<uuid>', strict_slashes=False)
