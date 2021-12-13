import csv
import os
from ..models import User
from .. import db

class Sheet:
    official_sheet=os.path.join(os.path.join(os.getcwd(),"docs"),"official.csv")
    student_sheet=os.path.join(os.path.join(os.getcwd(),"docs"),"student.csv")
    
    @classmethod
    def get_students(cls):
        f=open(cls.student_sheet,newline="")
        student_reader=csv.reader(f)
        for row in student_reader:
            user = User.query.filter_by(email=row[0]).first()
            if not user:
                user = User(email=row[0], name=row[1], roll=row[2])
                db.session.add(user)
                db.session.commit()
        f.close()
    
    @classmethod
    def get_officials(cls):
        f=open(cls.official_sheet,newline="")
        official_reader=csv.reader(f)
        for row in official_reader:
            user = User.query.filter_by(email=row[0]).first()
            if not user:
                user = User(username=row[0], password=row[1], email=row[2], name=row[3])
                db.session.add(user)
                db.session.commit()
        f.close()