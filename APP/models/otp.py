from .. import db
class OTP(db.Model):
    '''
    Create a OTP object and save it to database.
    
    >>> otp=OTP(email=str,otp=int,unixTimeStamp=float)
    >>> db.session.add(otp)
    >>> db.session.commit() 
    '''
    __tablename__='otp'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100))
    otp=db.Column(db.Integer)
    time=db.Column(db.DateTime)