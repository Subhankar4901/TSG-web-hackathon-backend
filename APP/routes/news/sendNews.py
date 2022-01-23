from flask import Blueprint,request,make_response,jsonify
from ...utils import JWT, sendEmail

mailNews_bp=Blueprint('mailNews',__name__,url_prefix="/mailNews")

# login required of officials
@mailNews_bp.route('/',methods=['POST'])
def mailNews():
	token = request.cookies.get('token')
	if not token:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)
	
	userData = JWT.validator(token)

	if (not userData) or (not userData.get('type')) or (userData.get("type") == 4):
		return make_response(jsonify({"message":"Unauthorized access."}), 401)
	
	data=request.form

	if data:
		sendEmail(data.get("subject"), data.get("body"), None, all=True)
	return make_response(jsonify(message="News send"))