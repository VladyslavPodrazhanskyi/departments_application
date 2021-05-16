import os
from datetime import date

from src import create_app
from src import db
from src.models.models import Department, Employee


def populate_departments():

    d0 = Department(
        name='Department for testing',
        description='without employees'
    )
    d1 = Department(
        name='Sales department',
        description='Department responsible for sales'
    )
    d2 = Department(
        name='Logistic department',
        description='Logistic department - responsible for delivery and customs clearence of international cargoes'
    )
    d3 = Department(
        name='Purchase api department',
        description='Department responsible for purchase of Active Pharmaceutical Ingredients, Equipment'
    )
    d4 = Department(
        name='Warehouse',
        description='Main Warehouse where most of the Goods are stored '
    )
    d5 = Department(
        name='Financial department',
        description='Department responsible for payments, accountant reports etc.'
    )
    d6 = Department(
        name='It department',
        description='It specialists and developers responsible for CRM system, support of corporate web resources'
    )

    db.session.add_all([d0, d1, d2, d3, d4, d5, d6])
    db.session.commit()
    db.session.close()


def populate_employees():
    e1 = Employee(
        employee_name='Irina Kulikova',
        birth_date=date(1986, 7, 2),
        salary=24000,
        department_uuid=Department.query.filter_by(name='Sales department').first().uuid
    )

    e2 = Employee(
        employee_name='Tatyana Yatsun',
        birth_date=date(1982, 8, 22),
        salary=19000,
        department_uuid=Department.query.filter_by(name='Sales department').first().uuid
    )

    e3 = Employee(
        employee_name='Ekaterina Vasilenko',
        birth_date=date(1987, 8, 17),
        salary=16000,
        department_uuid=Department.query.filter_by(name='Purchase api department').first().uuid
    )

    e4 = Employee(
        employee_name='Alexander Onoprienko',
        birth_date=date(1980, 5, 18),
        salary=22000,
        department_uuid=Department.query.filter_by(name='Logistic department').first().uuid
    )
    e5 = Employee(
        employee_name='Olesya Romanova',
        birth_date=date(1987, 7, 11),
        salary=18000,
        department_uuid=Department.query.filter_by(name='Logistic department').first().uuid
    )
    e6 = Employee(
        employee_name='Yana Shkavro',
        birth_date=date(1996, 9, 12),
        salary=12000,
        department_uuid=Department.query.filter_by(name='Logistic department').first().uuid
    )

    e7 = Employee(
        employee_name='Yuriy Dorofeev',
        birth_date=date(1984, 1, 22),
        salary=7200,
        department_uuid=Department.query.filter_by(name='Warehouse').first().uuid
    )

    db.session.add_all([e1, e2, e3, e4, e5, e6, e7])
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    app = create_app('development')
    app_context = app.app_context()
    app_context.push()
    print('Populating db with departments....')
    populate_departments()
    print('Departments successfully populated!')
    print('Populating db with employees....')
    populate_employees()
    print('Employees successfully populated!')
