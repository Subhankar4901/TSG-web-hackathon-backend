import csv
import os
from ..models import User
from .. import db
from .official_type import parse_official_type

class Sheet:

    @classmethod
    def get_students(cls, student_sheet):
        student_reader=csv.reader(student_sheet)
        r_n = 0
        for row in student_reader:
            if not r_n:
                r_n += 1
                continue
                
            user = User.query.filter_by(email=row[0]).first()
            if not user:
                user = User(email=row[0], name=row[1], roll=row[2], type=4)
                db.session.add(user)
                db.session.commit()
            else:
                user.email=row[0]
                user.name=row[1]
                user.roll=row[2]
                db.session.add(user)
                db.session.commit()
    
    @classmethod
    def get_officials(cls, official_sheet):
        official_reader=csv.reader(official_sheet)
        r_n = 0
        for row in official_reader:
            if not r_n:
                r_n += 1
                continue
        
            user = User.query.filter_by(email=row[2]).first()
            if not user:
                user = User(username=row[0], password=row[1], email=row[2], name=row[3], type=parse_official_type(row[0]))
                db.session.add(user)
                db.session.commit()
            else:
                user.username=row[0]
                user.password=row[1]
                user.email=row[2]
                user.name=row[3]
                user.type=parse_official_type(row[0])
                db.session.add(user)
                db.session.commit()