from web import db,app
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
#from .db_models import *


"""

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


"""

#### PLACEHOLDER FOR OVERLAPS PAGE FUNCTIONALITY
class User_placeholder:
    def __init__(self, name, hour):
        self.name = name
        self.hour = hour


@app.route('/')
def index():
    # CHANGE TO TRUE HOME PAGE LATER #
    return render_template('home.html')

@app.route('/overlaps')
def overlaps():
    #### PLACEHOLDER DATA TO FEED INTO PAGE ####
    current_user = User_placeholder('Scheffler', 7)
    selected_user = User_placeholder('Sterne', 20)

    current_users_times = [i for i in range(current_user.hour, 25)] + [i for i in range(1, current_user.hour)]
    selected_user_times = [i for i in range(selected_user.hour, 25)] + [i for i in range(1, selected_user.hour)] 
    times = zip(current_users_times, selected_user_times)

    # CHANGE TO TRUE HOME PAGE LATER #
    return render_template('overlaps.html', current_user=current_user, selected_user=selected_user, times=times)


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
