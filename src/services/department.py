from src.models.models import Department
from src.services.base import Base


class DepartmentService(Base):
    """
    This class is  the controller,
    that process data between the class Department of database and view functions.
    DepartmentService class is inherited from class Base and has all its methods.

    Methods:
        create_obj -  creates and return object of class Department.
        get_all -     retrieves list of all the objects of class Department.
        get_all_uuids - retrieves all the uuids of objects of class Department.
        get_by_uuid -  retrieves the object of class Department by its uuid.
        save_to_db - takes an object of class Department and saves it to db.
        delete_from_db - takes object of class Department and deletes it from db.
    """

    model = Department

    @classmethod
    def avg_salary(cls, uuid):
        """ Takes uuid of department and returns average salary of the employees of the current department"""
        department = cls.get_by_uuid(uuid)
        employees = department.department_employees
        if employees:
            return round(sum(map(lambda e: e.salary, employees)) / len(employees), 2)
        return 0
