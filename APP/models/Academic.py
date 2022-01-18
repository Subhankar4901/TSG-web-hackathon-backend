from email.policy import default
from .. import db
from datetime import datetime

class Academic(db.Model):
    '''
    Create a academic object and save it to database.
    Example :
    
    >>> academic=Academic(title=str,loaction=str,date=datetime,report = pdf.read())
    >>> db.session.add(academic)
    >>> db.session.commit()
        '''
    __tablename__="academic"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    subjectcode=db.Column(db.String(50))
    date=db.Column(db.DateTime, default = datetime.now())
    department=db.Column(db.String(50))
    semester = db.Column(db.String(50))
    type=db.Column(db.String(50)) # type = "Books, Study Material, Question Paper, Research Paper, Other"
    uploadedby=db.Column(db.String(100))
    downloadcount = db.Column(db.Integer, default = 0)
    downloadLink = db.Column(db.String(500))
    attachment=db.Column(db.LargeBinary(length=(2**24)-1))
