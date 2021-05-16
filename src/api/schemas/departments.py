from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested

from src.models.models import Department


class DepartmentSchema(SQLAlchemyAutoSchema):
    name = auto_field()
    description = auto_field()
    uuid = auto_field()
    department_employees = Nested('EmployeeSchema', many=True)

    class Meta:
        model = Department
        exclude = ['id']
        load_instance = True
        include_fk = True
        ordered = True
        dump_only = ('uuid',)




