from flask import Flask
from flask_cors import CORS

from .db_config import DBConfig
from .global_params import db
from .settings import KEY, STATIC_FOLDER, STATIC_PATH


def create_app():
    '''Create an application of flask'''

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                static_url_path=STATIC_PATH)
    app.config.from_object(DBConfig)
    app.config.update(
        DEBUG=True,
        SECRET_KEY=KEY,
        ENV='development',
    )

    register_blueprint(app)
    db.init_app(app)

    CORS(app, supports_credentials=True)
    return app


def register_blueprint(app):
    '''Register all the blueprints from apps.'''
    # app.register_blueprint(customer_user)
    # app.register_blueprint(customer_addr)
    # app.register_blueprint(customer_dish)
    # app.register_blueprint(customer_order)
    pass
