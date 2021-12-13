from flask import Blueprint, json,request,make_response,jsonify
from ...utils.sheet import Sheet
from ...utils.jwt import JWT
officials_bp=Blueprint('officials',__name__,url_prefix="/officials")

# login required of officials
@officials_bp.route('/',methods=['POST'])
def updateOfficials():
	data=request.get_json()
	userData = JWT.validator(data.token)
	if not userData:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)
	
	# TODO allow only a particular type of user 
	Sheet.get_officials()
	return jsonify({"message": "officals updated in the database"})