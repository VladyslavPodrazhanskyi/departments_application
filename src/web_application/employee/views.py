from flask import (render_template, url_for,
                   redirect, abort, flash)

from src.web_application.employee import employee_bp

from src.web_application.forms import EmployeeForm, EmployeeSearchForm
from src.services.department import DepartmentService
from src.services.employee import EmployeeService


# display the employee(s)
@employee_bp.route('/employees/<string:uuid>', methods=["GET", "POST"])
@employee_bp.route('/employees', methods=["GET", "POST"])
def display_employees(uuid=None):
    if uuid:
        employee = EmployeeService.get_by_uuid(uuid)
        if not employee:
            abort(404)
        department = DepartmentService.get_by_uuid(employee.department_uuid)
        return render_template('employee.html', employee=employee, department=department)
    form = EmployeeSearchForm()
    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data
        return redirect(url_for('employee_bp.search_by_bd', start_date=start_date, end_date=end_date))
    employees = EmployeeService.get_all()
    return render_template('all_employees.html', employees=employees, form=form)


# Search employee by birth date
@employee_bp.route('/employees/search_results/<start_date>')
@employee_bp.route('/employees/search_results/<start_date>/<end_date>')
def search_by_bd(start_date, end_date=None):
    employees = EmployeeService.search_employee(start_date, end_date)
    return render_template(
        'employee_search_results.html',
        employees=employees, start_date=start_date, end_date=end_date
    )


# create employee
@employee_bp.route('/create_employee', methods=["POST", "GET"])
def create_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee_data = {
            'employee_name': form.employee_name.data,
            'birth_date': form.birth_date.data,
            'salary': form.salary.data,
            'department_uuid': form.department_uuid.data
        }
        department = DepartmentService.get_by_uuid(form.department_uuid.data)
        if department:
            employee = EmployeeService.create_obj(employee_data)
            EmployeeService.save_to_db(employee)
            flash('Employee created successfully')
            return redirect(url_for('employee_bp.display_employees', uuid=employee.uuid))
        flash('input the correct uuid of the department')
    return render_template('employee_form.html', form=form, page='create')


# update the employee
@employee_bp.route('/employees/<string:uuid>/update', methods=["POST", "GET"])
def update_employee(uuid):
    employee = EmployeeService.get_by_uuid(uuid)
    if not employee:
        abort(404)
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        employee.employee_name = form.employee_name.data
        employee.birth_date = form.birth_date.data
        employee.salary = form.salary.data
        employee.department_uuid = form.department_uuid.data
        department = DepartmentService.get_by_uuid(employee.department_uuid)
        if department:
            EmployeeService.save_to_db(employee)
            flash('Employee updated successfully')
            return redirect(url_for('employee_bp.display_employees', uuid=employee.uuid))
        flash('input the correct uuid of the department')
    return render_template('employee_form.html', form=form, page='update')


# delete the employee
@employee_bp.route('/employees/<string:uuid>/delete', methods=["POST", "GET"])  # user delete method then
def del_employee(uuid):
    employee = EmployeeService.get_by_uuid(uuid)
    if not employee:
        abort(404)
    EmployeeService.delete_from_db(employee)
    flash('employee deleted successfully')
    return redirect(url_for('employee_bp.display_employees'))
