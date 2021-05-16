import os
from flask import current_app
from flask_migrate import Migrate
from src import create_app, db

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

#
# if __name__ == '__main__':
#     app.run()
