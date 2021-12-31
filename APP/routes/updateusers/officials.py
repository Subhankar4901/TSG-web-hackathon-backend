from flask import Blueprint, json,request,make_response,jsonify
from ...utils.sheet import Sheet
from ...utils.jwt import JWT
from ...models import User
from io import StringIO

officials_bp=Blueprint('officials',__name__,url_prefix="/officials")

# login required of officials
@officials_bp.route('/',methods=['POST'])
def updateOfficials():
	token = request.cookies.get('token')
	if not token:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)

	userData = JWT.validator(token)

	if (not userData) or (User.query.filter_by(id=userData["id"]).first().type != 1):
		return make_response(jsonify({"message":"Unauthorized access."}), 401)
	
	sheet = request.files.get('sheet')
	Sheet.get_officials(StringIO(sheet.read().decode()))
	return jsonify({"message": "officals updated in the database"})