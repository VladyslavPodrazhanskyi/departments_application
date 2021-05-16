from flask import Blueprint

core = Blueprint('core', __name__)

from src.web_application.core import views
