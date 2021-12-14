from flask import Blueprint, json,request,make_response,jsonify
from ...utils.sheet import Sheet
from ...utils.jwt import JWT
from ...models import User

officials_bp=Blueprint('officials',__name__,url_prefix="/officials")

# login required of officials
@officials_bp.route('/',methods=['POST'])
def updateOfficials():
	data=request.get_json()

	if not "token" in data:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)

	userData = JWT.validator(data["token"])

	if (not userData) or (User.query.filter_by(id=userData["id"]).first().type != 1):
		return make_response(jsonify({"message":"Unauthorized access."}), 401)
	
	Sheet.get_officials()
	return jsonify({"message": "officals updated in the database"})