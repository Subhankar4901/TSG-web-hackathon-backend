from .. import db

class Complain(db.Model):
    '''
    Create a complain object and save it to database.
    Example :
    
    >>> complain=Complain(userid=str,date=datetime,description=str,remarks=str)
    >>> db.session.add(complain)
    >>> db.session.commit()
    '''
    __tablename__="complain"
    id=db.Column(db.Integer,primary_key=True)
    userid=db.Column (db.Integer, db.ForeignKey("user.id"))
    date=db.Column(db.DateTime)
    description=db.Column(db.Text)
    remarks=db.Column(db.Text)
