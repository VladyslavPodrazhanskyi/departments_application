from src.models.models import Department
from src.services.base import Base


class DepartmentService(Base):
    model = Department

    @classmethod
    def avg_salary(cls, uuid):
        department = cls.get_by_uuid(uuid)
        employees = department.department_employees
        if employees:
            return round(sum(map(lambda e: e.salary, employees)) / len(employees), 2)
        return 0
