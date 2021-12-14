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
    introduction=db.Column(db.Text)
    procedure=db.Column(db.Text)
    jugde_criteria=db.Column(db.Text)
    timeline = db.Column(db.Text) # timeline in form of comma separated strings
    poster=db.Column(db.LargeBinary)
    venue=db.Column(db.String(200))
    start=db.Column(db.String(50))
    end=db.Column(db.String(50))
    achievements=db.relationship('Achievement',backref=db.backref('event',lazy=True))
    report=db.Column(db.LargeBinary)
    organizer_id=db.Column (db.Integer, db.ForeignKey("user.id"))
    type=db.Column(db.String(100)) # type = "Technology, Social and Culture, Sports and Games, Students' Welfare, "
    event_tags=db.Column(db.String(100)) # "Inter IIT, General Championship or None"
