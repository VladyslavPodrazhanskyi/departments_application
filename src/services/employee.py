from typing import List
from src.models.models import Employee
from src.services.base import Base
from src import db


class EmployeeService(Base):
    """
    This class is  the controller,
    that process data between the class Employee of database and view functions.
    EmployeeService class is inherited from class Base and has all its methods.

    Methods:
        create_obj -  creates and return object of class Employee.
        get_all -     retrieves list of all the objects of class Employee.
        get_all_uuids - retrieves all the uuids of objects of class Employee.
        get_by_uuid -  retrieves the object of class Employee by its uuid.
        save_to_db - takes an object of class Employee and saves it to db.
        delete_from_db - takes object of class Employee and deletes it from db.
    """

    model = Employee

    @classmethod
    def search_employee(cls, start_date, end_date=None) -> List:
        """ Search of employees by birth date

        Args:
            start_date (str): Format (year-month-day)  - mandatory argument
            end_date (str): Format (year-month-day)  - optional argument

        Returns:
            list: list of employees that were born on start_date or in the period between dates.

        It is possible to search by exact date (fill only start_date),
        or in the period between dates (fill start_date and end_date)

        """
        if end_date is None:
            end_date = start_date
        if end_date < start_date:
            start_date, end_date = end_date, start_date

        employees = db.session.query(cls.model). \
            filter(cls.model.birth_date >= start_date). \
            filter(cls.model.birth_date <= end_date).all()
        return employees
