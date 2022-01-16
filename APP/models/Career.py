from .. import db
from datetime import datetime

class Career(db.Model):
    '''
    Create a career object and save it to database.
    Example :
    
    >>> career=Career(title=str,loaction=str,date=datetime,report = pdf.read())
    >>> db.session.add(career)
    >>> db.session.commit()
        '''
    __tablename__="career"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    location=db.Column(db.String(200))
    date=db.Column(db.DateTime, default = datetime.now())
    report=db.Column(db.LargeBinary(length=(2**24)-1))
    jobprofile=db.Column(db.String(100)) # 
    type=db.Column(db.String(100)) # type = "SDE, Quant, Data, Consulting, Finance, Core, Other"
    uploadedby=db.Column(db.String(100))
