# wsgi.py

import os
from flask_migrate import Migrate
from src import create_app, db
from src.insert_db import populate_departments, populate_employees


app = create_app(os.environ.get('FLASK_CONFIG'))
migrate = Migrate(app, db)

populate_departments()
populate_employees()