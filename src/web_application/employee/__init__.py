from flask import Blueprint

employee_bp = Blueprint('employee_bp', __name__)

from src.web_application.employee import views
