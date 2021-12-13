from flask import Blueprint,request,make_response,jsonify
from ...utils.sheet import Sheet
students_bp=Blueprint('students',__name__,url_prefix="/students")

@students_bp.route('/',methods=['POST'])
def updateStudents():
	Sheet.get_students()
	return jsonify({"message": "students updated in the database"})