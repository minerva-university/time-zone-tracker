from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import secrets

#instantiate flask app
app = Flask(__name__)
base = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
app.config['DEBUG'] = True
secret_key = secrets.token_hex(24)
app.config['SECRET_KEY'] = secret_key

##instantiate database
db = SQLAlchemy(app) 
from web import serve
