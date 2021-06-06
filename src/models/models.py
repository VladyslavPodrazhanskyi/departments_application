# src/models/models.py

import uuid

from src import db


class Department(db.Model):
    """Model describing company department"""

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, index=True)
    description = db.Column(db.Text)
    uuid = db.Column(db.String(36), unique=True, index=True, nullable=False)
    department_employees = db.relationship('Employee', backref='Department', lazy='subquery', cascade='all, delete')

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.uuid = str(uuid.uuid4())

    # def __repr__(self):
    #     return f"Department(name: {self.name}, uuid: {self.uuid}, employees: {self.department_employees})"


class Employee(db.Model):
    """Model describing company employee"""

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(120), nullable=False)
    birth_date = db.Column(db.Date, nullable=False, index=True)
    salary = db.Column(db.Integer, nullable=False)
    uuid = db.Column(db.String(36), unique=True, index=True, nullable=False)
    department_uuid = db.Column(db.String, db.ForeignKey('departments.uuid'), nullable=False)

    def __init__(self, employee_name, birth_date, salary, department_uuid):
        self.employee_name = employee_name
        self.birth_date = birth_date
        self.salary = salary
        self.department_uuid = department_uuid
        self.uuid = str(uuid.uuid4())

    # def __repr__(self):
    #     return f"Employee({self.employee_name}, {self.birth_date}, {self.salary}, {self.uuid})"
