# department/views

from flask import (render_template, flash, url_for,
                   redirect, request, abort)

from src.web_application.department import department_bp
from src.web_application.forms import DepartmentForm
from src.services.department import DepartmentService


# display the department(s)
@department_bp.route('/departments')
@department_bp.route('/departments/<string:uuid>')
def display_departments(uuid=None):
    if uuid:
        department = DepartmentService.get_by_uuid(uuid)
        if not department:
            abort(404)
        avg_salary = DepartmentService.avg_salary(uuid)
        return render_template('department.html', department=department, avg_salary=avg_salary)
    departments = DepartmentService.get_all()
    avg_salary = DepartmentService.avg_salary
    return render_template('all_departments.html', departments=departments, avg_salary=avg_salary)


# create  a department
@department_bp.route('/create_department', methods=["POST", "GET"])
def create_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        department_data = {
            'name': request.form.get('name'),
            'description': request.form.get('description')
        }
        department = DepartmentService.create_obj(department_data)
        DepartmentService.save_to_db(department)
        flash('Department created successfully')
        return redirect(url_for('department_bp.display_departments', uuid=department.uuid))
    return render_template('department_form.html', form=form, page='create')


# update the department

@department_bp.route('/departments/<string:uuid>/update', methods=["POST", "GET"])
def update_department(uuid):
    department = DepartmentService.get_by_uuid(uuid)
    if not department:
        abort(404)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        DepartmentService.save_to_db(department)
        flash('Department updated successfully')
        return redirect(url_for('department_bp.display_departments', uuid=department.uuid))
    return render_template('department_form.html', form=form, page='update')


@department_bp.route('/departments/<string:uuid>/del', methods=["POST", "GET"])
def del_department(uuid):
    department = DepartmentService.get_by_uuid(uuid)
    if not department:
        abort(404)
    if department.department_employees:
        flash('You cannot delete department with the employees')
        return redirect(url_for('department_bp.display_departments', uuid=department.uuid))
    DepartmentService.delete_from_db(department)
    flash('department deleted successfully')
    return redirect(url_for('department_bp.display_departments'))
