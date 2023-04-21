import os
import secrets
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) #__name__ - name of the current Python module
    base = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
    app.config['DEBUG'] = True
    secret_key = secrets.token_hex(24)
    app.config['SECRET_KEY'] = secret_key

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app