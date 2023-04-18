from sqlalchemy import Column, Text, Integer, Date, Boolean, ForeignKey, String, DateTime
from datetime import datetime
from web import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(20))
    timezone = db.Column(db.String(10))
    location = db.Column(db.String(50)) 
    status = db.Column(db.String(20))  
    salt = db.Column(db.String)
    calendar_authenticated = db.Column(db.Boolean, default=False)
    reminder_frequency = db.Column(db.Integer, default=7 * 24 * 60 * 60)
    last_reminder_date = db.Column(db.DateTime(timezone=True))
    
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
    last_interaction_date =  db.Column(db.DateTime(timezone=True),index=True)

    def __repr__(self):
        return (f'<Interaction(id={self.id}, user_id={self.user_id}, '
                    f'friend_id={self.friend_id}, '
                    f'last_interaction_date={self.last_interaction_date})>')

db.create_all()
db.session.commit()