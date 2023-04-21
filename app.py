from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import calendar

# Flask Configuration 
app = Flask(__name__)

# Create database to store tasks using SQLlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)


#### PLACEHOLDER FOR OVERLAPS PAGE FUNCTIONALITY
class User_placeholder:
    def __init__(self, name, location = 'London', timezone = 'UCT'):
        self.name = name
        self.location = location
        self.timezone = timezone


@app.route('/')
def index():
    user1 = User_placeholder('Scheffler')
    user2 = User_placeholder('Sterne', 'Berlin', 'HST')
    user3 = User_placeholder('Malia', 'Sydney', 'EST')

    friends = [user1, user2, user3]


    current_time_utc = datetime.utcnow()
    times = []
    for user in friends:
        convert_time = current_time_utc.astimezone(pytz.timezone(user.timezone))
        time = '{:d}:{:02d}'.format(convert_time.hour, convert_time.minute)
        times.append(time)

    friend_times = zip(times, friends)

    current_user = User_placeholder('Mackenzie Bird', 'London', 'Etc/GMT+1')
    user_datetime = current_time_utc.astimezone(pytz.timezone(current_user.timezone))
    user_time = '{:d}:{:02d}'.format(user_datetime.hour, user_datetime.minute)
    user_day = user_datetime.day
    user_month = calendar.month_name[user_datetime.month]

    # CHANGE TO TRUE HOME PAGE LATER #
    return render_template('home.html', friend_times=friend_times, user_day=user_day, current_user=current_user, user_time=user_time, user_month=user_month)


@app.route('/overlaps')
def overlaps():
    current_time_utc = datetime.utcnow()

    current_user = User_placeholder('You', 'London', 'Etc/GMT+1')
    current_user_datetime = current_time_utc.astimezone(pytz.timezone(current_user.timezone))
    current_user_time = '{:d}:{:02d}'.format(current_user_datetime.hour, current_user_datetime.minute)
    current_user_day = current_user_datetime.day
    current_user_month = calendar.month_name[current_user_datetime.month]

    selected_user = User_placeholder('Sterne', 'Berlin', 'HST')
    selected_user_datetime = current_time_utc.astimezone(pytz.timezone(selected_user.timezone))
    selected_user_time = '{:d}:{:02d}'.format(selected_user_datetime.hour, selected_user_datetime.minute)
    selected_user_day = selected_user_datetime.day
    selected_user_month = calendar.month_name[selected_user_datetime.month]

    current_users_times = [i for i in range(current_user_datetime.hour, 25)] + [i for i in range(1, current_user_datetime.hour)]
    selected_user_times = [i for i in range(selected_user_datetime.hour, 25)] + [i for i in range(1, selected_user_datetime.hour)] 
    times = zip(current_users_times, selected_user_times)

    return render_template('overlaps.html', current_user=current_user, selected_user=selected_user, times=times, selected_user_time=selected_user_time, current_user_time=current_user_time, current_user_month=current_user_month, current_user_day=current_user_day, selected_user_month=selected_user_month, selected_user_day=selected_user_day)

@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/users')
def users():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run()