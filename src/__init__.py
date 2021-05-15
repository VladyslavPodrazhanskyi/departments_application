from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from config import config

db = SQLAlchemy()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)


    from src.api import api_bp
    from src.web_application.core.views import core

    app.register_blueprint(api_bp)
    app.register_blueprint(core)

    return app


from src.models import models
