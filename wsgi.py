# wsgi.py

import os
from flask_migrate import Migrate
from src import create_app, db

app = create_app(os.environ.get('FLASK_CONFIG'))
migrate = Migrate(app, db)

if os.environ.get('FLASK_CONFIG') == 'production':
    with app.app_context():
        db.create_all()
