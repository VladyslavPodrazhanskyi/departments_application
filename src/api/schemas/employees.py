# src/schemas/employees.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models.models import Employee


class EmployeeSchema(SQLAlchemyAutoSchema):
    """Schema used in the employee rest service for :
     - validation data
     - serialization
     - deserialization
     """

    class Meta:
        model = Employee
        exclude = ['id']
        load_instance = True
        include_fk = True
        ordered = True
        dump_only = ('uuid',)
