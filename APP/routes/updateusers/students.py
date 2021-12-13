from flask import Blueprint,request,make_response,jsonify
from ...utils.sheet import Sheet
from ...utils.jwt import JWT
students_bp=Blueprint('students',__name__,url_prefix="/students")

# login required of officials
@students_bp.route('/',methods=['POST'])
def updateStudents():
	data=request.get_json()
	userData = JWT.validator(data.token)
	if not userData:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)
	
	# TODO allow only a particular type of user :
	Sheet.get_students()
	return jsonify({"message": "students updated in the database"})