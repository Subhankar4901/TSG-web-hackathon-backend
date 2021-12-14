from flask import Blueprint,request,make_response,jsonify
from ...utils.sheet import Sheet
from ...utils.jwt import JWT
from ...models import User

students_bp=Blueprint('students',__name__,url_prefix="/students")

# login required of officials
@students_bp.route('/',methods=['POST'])
def updateStudents():
	data=request.get_json()
	userData = JWT.validator(data["token"])
	if (not userData) or (User.query.filter_by(id=userData["id"]).first().type != 1):
		return make_response(jsonify({"message":"Unauthorized access."}), 401)

	Sheet.get_students()
	return jsonify({"message": "students updated in the database"})