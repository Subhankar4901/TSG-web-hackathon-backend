from flask import Blueprint,request,make_response,jsonify
from ...utils.sheet import Sheet
from ...utils.jwt import JWT
from ...models import User
from io import StringIO
from ... import db

students_bp=Blueprint('students',__name__,url_prefix="/students")

# login required of officials
@students_bp.route('/',methods=['POST'])
def updateStudents():
	token = request.cookies.get('token')
	if not token:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)

	userData = JWT.validator(token)

	if (not userData) or (User.query.filter_by(id=userData["id"]).first().type != 1):
		return make_response(jsonify({"message":"Unauthorized access."}), 401)

	sheet = request.files.get('sheet')
	if sheet:
		Sheet.get_students(StringIO(sheet.read().decode()))
		return jsonify({"message": "students updated in the database"})
	return jsonify({"message": "no sheet uploaded"})