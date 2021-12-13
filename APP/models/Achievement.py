from .. import db

class Achievement(db.Model):
    '''
      Create a achievement object and save it to database.
    Example :
    
    >>> achievement=Achievement(user=int,event=int,position=int,certificate=str)
    >>> db.session.add(event)
    >>> db.session.commit()
    '''
    __tablename__='achievement'
    id=db.Column(db.Integer,primary_key=True)
    user=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) # Refrence to user 
    event_id=db.Column(db.Integer,db.ForeignKey('event.id'),nullable=False) # Reference to event
    position=db.Column(db.Integer) 
    certificate=db.Column(db.LargeBinary)