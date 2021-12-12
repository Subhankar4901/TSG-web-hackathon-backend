from .. import db

class User(db.Model):
    '''
    Create a user object and save it to database.
    Example :
    
    >>> user=User(name:str,username:str,insti_email:str,email:str,
            photo:str,type:int,password:bytes,hall:str)
    >>> db.session.add(user)
    >>> db.session.commit()
        '''
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    roll=db.Column(db.String(20))
    email=db.Column(db.String(100))
    photo=db.Column(db.LargeBinary)
    type=db.Column(db.Integer)
    events_participated=db.relationship('Event',secondary="user_event",backref=db.backref('participants',lazy=True)) # many-many relationship with event.
    events_organised=db.relationship('Event',backref=db.backref('organiser',lazy=True)) # one-many relationship with event
    achievements=db.relationship('Achievement',backref=db.backref('achiever',lazy=True)) # one-many relationship with achievements
    hall=db.Column(db.String(10))
    complaints=db.relationship('Complain',backref=db.backref("user",lazy=True))