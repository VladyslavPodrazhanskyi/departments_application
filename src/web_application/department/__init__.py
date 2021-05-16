from flask import Blueprint

department_bp = Blueprint('department_bp', __name__)

from src.web_application.department import views
