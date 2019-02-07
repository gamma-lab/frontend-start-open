import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
from . import commands

db = SQLAlchemy()

def create_app(config_name='default'):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config[config_name])

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register customer command
    commands.init_app(app)

    # plugins
    db.init_app(app)
    migrate = Migrate(app, db)

    # blueprint registration
    from .api import api
    app.register_blueprint(api)

    return app
