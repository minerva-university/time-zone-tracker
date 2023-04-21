import os
import secrets
from sqlalchemy import Column, Text, Integer, Date, Boolean, ForeignKey, String, DateTime
from datetime import datetime
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from database import database as db
# from models import User
app = Flask(__name__)
db = SQLAlchemy(app)


# instantiate flask app
def create_app(config=None):
    base = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['DEBUG'] = True
    secret_key = secrets.token_hex(24)
    app.config['SECRET_KEY'] = secret_key
    # db = SQLAlchemy(app)

    if config:
        app.config.update(config)

    ##instantiate database
    db.init_app(app)
    migrate = Migrate(app, db)

    # Add your Flask application code here
    @app.route('/')
    def hello():
        return 'Hello World!'

    return app

#### PLACEHOLDER FOR OVERLAPS PAGE FUNCTIONALITY


class UserPlaceHolder(db.Model):
    __tablename__ = 'user_placeholder'
    name = db.Column(db.String(50), primary_key=True)
    hour = db.Column(db.Integer, primary_key=True)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    timezone = db.Column(db.Text)
    salt = db.Column(String)
    calendar_authenticated = db.Column(db.Boolean, default=False)
    reminder_frequency = Column(Integer, default=7 * 24 * 60 * 60)
    last_reminder_date = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return (f'<User(id={self.id}, email={self.email}, '
                f'username={self.username}, password={self.password}, '
                f'timezone={self.timezone}, salt={self.salt}, '
                f'calendar_authenticated={self.calendar_authenticated}, '
                f'reminder_frequency={self.reminder_frequency}, '
                f'last_reminder_date={self.last_reminder_date})>')


class Friend(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Friend {self.id}: user {self.user_id} friend {self.friend_id}>'


class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    last_interaction_date = db.Column(db.DateTime(timezone=True), index=True)

    def __repr__(self):
        return (f'<Interaction(id={self.id}, user_id={self.user_id}, '
                f'friend_id={self.friend_id}, '
                f'last_interaction_date={self.last_interaction_date})>')


# @app.route('/')
# def index():
#     # CHANGE TO TRUE HOME PAGE LATER #
#     return render_template('home.html')


@app.route('/overlaps')
def overlaps():
    #### PLACEHOLDER DATA TO FEED INTO PAGE ####
    current_user = User_placeholder('Scheffler', 7)
    selected_user = User_placeholder('Sterne', 20)
    db.session.add(current_user)
    db.session.add(selected_user)

    current_users_times = [i for i in range(current_user.hour, 25)] + [i for i in range(1, current_user.hour)]
    selected_user_times = [i for i in range(selected_user.hour, 25)] + [i for i in range(1, selected_user.hour)]
    times = zip(current_users_times, selected_user_times)
    db.session.commit()

    # CHANGE TO TRUE HOME PAGE LATER #
    return render_template('overlaps.html', current_user=current_user, selected_user=selected_user, times=times)


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    try:
        app.run(debug=True, port=5000)
    except SystemExit:
        pass


