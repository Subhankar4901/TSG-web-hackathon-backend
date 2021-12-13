import csv
import os
class Sheet:
    official_sheet=os.path.join(os.path.join(os.getcwd(),"docs"),"official.csv")
    student_sheet=os.path.join(os.path.join(os.getcwd(),"docs"),"student.csv")
    @classmethod
    def get_student(cls,email:str):
        f=open(cls.student_sheet,newline="")
        student_reader=csv.reader(f)
        for row in student_reader:
            if row[0]==email:
                f.close()
                return {"email":row[0],"name":row[1],"roll":row[2]}
        f.close()
        return None
    @classmethod
    def get_official(cls,username:str):
        f=open(cls.official_sheet,newline="")
        official_reader=csv.reader(f)
        for row in official_reader:
            if row[0]==username:
                f.close()
                return {"username":row[0],"password":row[1],"email":row[2],"name":row[3]}
        f.close()
        return None