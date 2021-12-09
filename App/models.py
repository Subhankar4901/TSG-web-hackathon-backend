from . import app
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app=app)


user_event_assosiation=db.Table("user_event",
                                db.Column("user_id",db.Integer,db.ForeignKey('user.id')),
                                db.Column("event_id",db.Integer,db.ForeignKey('event.id')))
class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    events=db.relationship('Event',secondary=user_event_assosiation,backref=db.backref('participants',lazy=True))
class Event(db.Model):
    __tablename__="event"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True)
    