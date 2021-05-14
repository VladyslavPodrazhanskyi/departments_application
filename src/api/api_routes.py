from src.api import api
from src.api.resources import Smoke

api.add_resource(Smoke, '/smoke')
