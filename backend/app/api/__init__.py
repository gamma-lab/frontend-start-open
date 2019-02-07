from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def index():
    return 'api V1.0', 200

from . import users
