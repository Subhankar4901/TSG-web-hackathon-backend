from . import db
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
    username=db.Column(db.String(50),unique=True,default=None)
    roll=db.Column(db.String(20))
    insti_email=db.Column(db.String(100))
    email=db.Column(db.String(100),default=None)
    photo=db.Column(db.LargeBinary)
    type=db.Column(db.Integer)
    password=db.Column(db.String(100))
    events_participated=db.relationship('Event',secondary="user_event",backref=db.backref('participants',lazy=True)) # many-many relationship with event.
    events_organised=db.relationship('Event',backref=db.backref('orgaiser',lazy=True)) # one-many relationship with event
    achievements=db.relationship('Achievement',backref=db.backref('achiever',lazy=True)) # one-many relationship with achievements
    hall=db.Column(db.String(10))
    complaints=db.relationship('Complain',backref=db.backref("user",lazy=True))
class Event(db.Model):
    '''
    Create a event object and save it to database.
    Example :
    
    >>> event=Event(title:str,description:str,poster:str,venue:str,
            start:str,end:str,report:str)
    >>> db.session.add(event)
    >>> db.session.commit()
        '''
    __tablename__="event"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    description=db.Column(db.Text)
    poster=db.Column(db.LargeBinary)
    vaenue=db.Column(db.String(200))
    start=db.Column(db.String(50))
    end=db.Column(db.String(50))
    achievements=db.relationship('Achievement',backref=db.backref('event',lazy=True))
    report=db.Column(db.LargeBinary)
class Achievement(db.Model):
    '''
      Create a achievement object and save it to database.
    Example :
    
    >>> achievement=Achievement(user:int,event:int,position:int,certificate:str)
    >>> db.session.add(event)
    >>> db.session.commit()
    '''
    __tablename__='achievement'
    id=db.Column(db.Integer,primary_key=True)
    user=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) # Refrence to user 
    event=db.Column(db.Integer,db.ForeignKey('event.id'),nullable=False) # Reference to event
    position=db.Column(db.Integer) 
    certificate=db.Column(db.LargeBinary)

# Assosiation table to model the many-many relationship of User and Event
user_event_assosiation=db.Table("user_event",
                                db.Column("user_id",db.Integer,db.ForeignKey('user.id')),
                                db.Column("event_id",db.Integer,db.ForeignKey('event.id')))
     
    
    