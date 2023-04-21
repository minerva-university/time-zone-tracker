from sqlalchemy import Column, Text, Integer, Date, Boolean, ForeignKey, String, DateTime
from datetime import datetime
from web import db


class User(db.Model):
    #creating user table to be able to log people in
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    #get email to properly authenticate calendar
    #index for email and user as we are going to query a lot (even for friend search)
    email = db.Column(db.String(50),index = True)
    username = db.Column(db.String(50),index=True)
    password = db.Column(db.String(20))
    timezone = db.Column(db.String(10))
    location = db.Column(db.String(50)) 
    #get user's status to check availability time
    status = db.Column(db.String(20))  
    #salt for more secure password
    salt = db.Column(db.String)
    #check to see if the calendar is authenticated or not
    calendar_authenticated = db.Column(db.Boolean, default=False)
    #give users notifications to those they havent talked much
    reminder_frequency = db.Column(db.Integer, default=7 * 24 * 60 * 60)
    last_reminder_date = db.Column(db.DateTime(timezone=True,index = True))
    
    def __repr__(self):
        return (f'<User(id={self.id}, email={self.email}, '
                f'username={self.username}, password={self.password}, '
                f'timezone={self.timezone}, salt={self.salt}, '
                f'location={self.location}), '
                f'status={self.status}), '
                f'calendar_authenticated={self.calendar_authenticated}, '
                f'reminder_frequency={self.reminder_frequency}, '
                f'last_reminder_date={self.last_reminder_date})>')


class Friend(db.Model):
    #creating friends table to display overlapping times
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),index=True)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Friend {self.id}: user {self.user_id} friend {self.friend_id}>'


class Interaction(db.Model):
    #creating interaction tables to query people who talk less 
    #to display on the top.
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #index as we are going to query datetime a lot to display less interacted users
    last_interaction_date =  db.Column(db.DateTime(timezone=True),index=True)

    def __repr__(self):
        return (f'<Interaction(id={self.id}, user_id={self.user_id}, '
                    f'friend_id={self.friend_id}, '
                    f'last_interaction_date={self.last_interaction_date})>')
#commit to database
db.create_all()
db.session.commit()
