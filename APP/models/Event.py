from .. import db

class Event(db.Model):
    '''
    Create a event object and save it to database.
    Example :
    
    >>> event=Event(title=str,description=str,poster=str,venue=str,
            start=str,end=str,report=str)
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
    organizer_id=db.Column (db. Integer, db. ForeignKey("user.id"))