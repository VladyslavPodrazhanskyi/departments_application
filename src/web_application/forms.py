from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional


class DepartmentForm(FlaskForm):
    """   Form for add and update of departments  """

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Submit')


class EmployeeForm(FlaskForm):
    """   Form for add and update of employee  """

    employee_name = StringField('Employee_name', validators=[DataRequired()])
    birth_date = DateField('Birth_date', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    department_uuid = StringField('Department_uuid', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EmployeeSearchForm(FlaskForm):
    """   Form for search employees by birth date  """

    start_date = DateField('Start date', validators=[DataRequired()])
    end_date = DateField('End date', validators=[Optional()])
    submit = SubmitField('Search')
