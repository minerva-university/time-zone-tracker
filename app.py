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

class Self_placeholder(db.Model):
    # Task Parameters set automatically: id & date_created
    id = db.Column(db.Integer, primary_key = True) # unique ids for each self
    name = db.Column(db.String(200)) 
    timezone = db.Column(db.String(200))
    location = db.Column(db.String(200))

    # Defining self representation
    def __repr__(self):
        return '<Task %r>' % self.id


class User_placeholder(db.Model):
    # Task Parameters set automatically: id & date_created
    id = db.Column(db.Integer, primary_key = True) # unique ids for each self
    name = db.Column(db.String(200)) 
    timezone = db.Column(db.String(200))
    location = db.Column(db.String(200))

    # Defining self representation
    def __repr__(self):
        return '<Task %r>' % self.id
    
new_self = Self_placeholder(name='Malia', timezone='GMT+1', location='London')
friend = User_placeholder(name='Liuda', timezone='GMT-7', location='San Francisco')
db.session.add(new_self) # add users to database
db.session.add(friend)
db.session.commit() # commit modifications

@app.route('/home')
def index():
    # Retrieve all friend's information
    friends_tz = User_placeholder.query(User_placeholder.timezone).all()
    friends_name = User_placeholder.query(User_placeholder.name).all()
    friends_loc = User_placeholder.query(User_placeholder.location).all()

    # check current time
    current_time_utc = datetime.utcnow()

    # Calculate time in friends' timezones
    times = []
    for tz in friends_tz:
        friend_tz = 'Etc/'+tz
        convert_time = current_time_utc.astimezone(pytz.timezone(friend_tz))
        time = '{:d}:{:02d}'.format(convert_time.hour, convert_time.minute)
        times.append(time)

    f_times_names_loc = zip(times, friends_name, friends_loc) # all friend's times and their profiles

    # Get the most recent update of a current user's information
    current_name = Self_placeholder.query(Self_placeholder.name).order_by(Self_placeholder.id.desc()).first()
    current_tz = Self_placeholder.query(Self_placeholder.timezone).order_by(Self_placeholder.id.desc()).first()
    current_loc = Self_placeholder.query(Self_placeholder.location).order_by(Self_placeholder.id.desc()).first()

    # convert time to reflect current user's 
    self_tz = 'Etc/'+current_tz
    user_datetime = current_time_utc.astimezone(pytz.timezone(self_tz))
    user_time = '{:d}:{:02d}'.format(user_datetime.hour, user_datetime.minute)
    
    # Retrieve day and month
    user_day = user_datetime.day
    user_month = calendar.month_name[user_datetime.month]

    return render_template('home.html', f_times_names_loc=f_times_names_loc, user_day=user_day, current_name=current_name, current_loc=current_loc, user_time=user_time, user_month=user_month)


@app.route('/overlaps/<int:user_id>')
def overlaps(user_id):
    '''
    Page depicting overlapping times between you are your friend. 
    '''
    current_time_utc = datetime.utcnow()

    current_user = Self_placeholder.query.order_by(Self_placeholder.id.desc()).first()
    self_tz = 'Etc/'+current_user.timezone
    current_user_datetime = current_time_utc.astimezone(pytz.timezone(self_tz))
    current_user_time = '{:d}:{:02d}'.format(current_user_datetime.hour, current_user_datetime.minute)
    current_user_day = current_user_datetime.day
    current_user_month = calendar.month_name[current_user_datetime.month]

    selected_user = User_placeholder.query.filter_by(id=user_id).first()
    selected_tz = 'Etc/'+current_user.timezone
    selected_user_datetime = current_time_utc.astimezone(pytz.timezone(selected_tz))
    selected_user_time = '{:d}:{:02d}'.format(selected_user_datetime.hour, selected_user_datetime.minute)
    selected_user_day = selected_user_datetime.day
    selected_user_month = calendar.month_name[selected_user_datetime.month]

    current_users_times = [i for i in range(current_user_datetime.hour, 25)] + [i for i in range(1, current_user_datetime.hour)]
    selected_user_times = [i for i in range(selected_user_datetime.hour, 25)] + [i for i in range(1, selected_user_datetime.hour)] 
    times = zip(current_users_times, selected_user_times)

    return render_template('overlaps.html', current_user=current_user, selected_user=selected_user, times=times, selected_user_time=selected_user_time, current_user_time=current_user_time, current_user_month=current_user_month, current_user_day=current_user_day, selected_user_month=selected_user_month, selected_user_day=selected_user_day)

@app.route('/', methods = ['GET','POST'])
@app.route('/settings', methods = ['GET','POST'])
def settings():
    # Get description of the task from form
    self_name = request.form.get("name")
    self_tz = request.form.get("timezone")
    self_city = request.form.get("city")

    # Create a new Task instance
    new_self = Self_placeholder(name=self_name, timezone=self_tz, location=self_city)
    
    # Get description of the task from form
    f_name = request.form.get("friend-name")
    f_tz = request.form.get("friend-timezone")
    f_city = request.form.get("friend-city")

    # Create a new Friend instance
    friend = User_placeholder(name=f_name, timezone=f_tz, location=f_city)

    db.session.add(new_self) # add users to database
    db.session.add(friend)
    db.session.commit() # commit modifications
    return render_template('settings.html')


@app.route('/users')
def users():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True, port = 5000)