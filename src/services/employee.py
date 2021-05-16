from src.models.models import Employee
from src.services.base import Base
from src import db


class EmployeeService(Base):
    model = Employee

    @classmethod
    def search_employee(cls, start_date, end_date=None):
        if end_date is None:
            end_date = start_date
        if end_date < start_date:
            start_date, end_date = end_date, start_date
        employees = db.session.query(cls.model).\
            filter(cls.model.birth_date >= start_date). \
            filter(cls.model.birth_date <= end_date).all()
        return employees

