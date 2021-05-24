from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    """ Factory function create and configure an instance of flask application."""

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from src.api import api_bp
    from src.web_application.core import core
    from src.web_application.department import department_bp
    from src.web_application.employee import employee_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(core)
    app.register_blueprint(department_bp)
    app.register_blueprint(employee_bp)

    from src.models import models

    return app
