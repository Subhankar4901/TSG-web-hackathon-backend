from .. import db
from datetime import datetime
from decouple import config

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
    date=db.Column(db.DateTime, default = datetime.now())
    description=db.Column(db.Text)
    remarks=db.Column(db.Text)
    attachment=db.Column(db.LargeBinary)

    def extractData(self):
        data = {
            "id" : self.id,
            "made_by": self.made_by.name,
            "date" : self.date,
            "description": self.description,
            "remarks" : self.remarks,
            "attachment" : f"{config('host')}/api/complaints/{self.id}/getattachment/" if self.attachment else None
        } 
        return data
